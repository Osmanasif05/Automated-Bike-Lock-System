import cv2
import mediapipe as mp
import numpy as np
import pickle
import serial
import time

# Serial communication setup
arduino_port = "/dev/tty.usbmodem1101"  # Correct port for your Arduino
baud_rate = 9600  # Same as Arduino's Serial.begin()

try:
    arduino = serial.Serial(arduino_port, baud_rate, timeout=1)
    time.sleep(2)  # Wait for connection
    print(f"Connected to Arduino on {arduino_port}")
except Exception as e:
    print(f"Error connecting to Arduino: {e}")
    arduino = None

# File to store face profiles
PROFILE_FILE = "./face_profiles.pkl"

# Initialize MediaPipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils

# Load or initialize face profiles
try:
    with open(PROFILE_FILE, "rb") as f:
        face_profiles = pickle.load(f)
except FileNotFoundError:
    face_profiles = {}

# Save a new face profile
def save_profile(name, landmarks):
    name = name.strip()  # Remove accidental whitespace or newlines
    print(f"Saving profile for: {name}")
    face_profiles[name] = landmarks
    with open(PROFILE_FILE, "wb") as f:
        pickle.dump(face_profiles, f)
    print(f"Profile saved for {name}!")

# Recognize a face and calculate accuracy
def recognize_profile(landmarks):
    closest_name = None
    closest_distance = float('inf')
    closest_accuracy = 0

    for name, saved_landmarks in face_profiles.items():
        # Calculate Euclidean distance
        distance = np.linalg.norm(np.array(saved_landmarks) - np.array(landmarks))
        accuracy = max(0, 1 - distance) * 100  # Convert to percentage
        if distance < closest_distance:
            closest_name = name
            closest_distance = distance
            closest_accuracy = accuracy

    print(f"Closest Name: {closest_name}, Accuracy: {closest_accuracy:.2f}%, Distance: {closest_distance:.5f}")
    if closest_distance < 0.03:
        return closest_name, closest_accuracy
    return None, 0

# Send signal to Arduino
def send_signal():
    if arduino:
        print("Sending unlock signal to Arduino via serial...")
        arduino.write(b'TRIGGER\n')  # Send "TRIGGER" command
    else:
        print("Arduino not connected. Skipping signal.")

# Main function to run the facial recognition system
def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not access webcam.")
        return

    with mp_face_mesh.FaceMesh(
        max_num_faces=1, refine_landmarks=True, min_detection_confidence=0.5
    ) as face_mesh:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Convert frame to RGB
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Process frame for face landmarks
            face_results = face_mesh.process(rgb_frame)

            # Handle face recognition
            landmarks = None
            if face_results.multi_face_landmarks:
                for face_landmarks in face_results.multi_face_landmarks:
                    mp_drawing.draw_landmarks(frame, face_landmarks, mp_face_mesh.FACEMESH_TESSELATION)
                    landmarks = [(lm.x, lm.y, lm.z) for lm in face_landmarks.landmark]

            # Handle keypresses
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):  # Quit the script
                print("Exiting...")
                break
            elif key == ord('n'):  # Save a new profile
                if landmarks:
                    name = input("Enter name for new profile: ")
                    save_profile(name, landmarks)
                else:
                    print("No face detected. Cannot save profile.")

            # If landmarks are detected, recognize the profile
            if landmarks:
                recognized_name, accuracy = recognize_profile(landmarks)
                if recognized_name and accuracy >= 60:
                    print(f"Recognized {recognized_name} with {accuracy:.2f}% accuracy.")
                    send_signal()
                else:
                    print("Unknown face or low accuracy.")

            # Display the frame
            cv2.imshow("Face Recognition", frame)

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

