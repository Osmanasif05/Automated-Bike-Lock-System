import serial
import pygame  # For audio playback

# Replace with your Arduino port
arduino_port = "/dev/tty.usbmodem1101"  
baud_rate = 9600

# Initialize serial connection to Arduino
try:
    arduino = serial.Serial(arduino_port, baud_rate, timeout=1)
    print(f"Listening for signals on {arduino_port}...")
except Exception as e:
    print(f"Error connecting to Arduino: {e}")
    exit()

def play_incorrect_passcode_audio():
    """Plays an MP3 file for incorrect passcode using pygame."""
    print("Playing incorrect passcode audio...")
    pygame.mixer.init()
    pygame.mixer.music.load("incorrect_passcode.mp3")  # Replace with your MP3 file path
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():  # Wait until the audio finishes playing
        pygame.time.Clock().tick(10)
    print("Audio playback finished.")

# Main loop to listen for Arduino signals
while True:
    if arduino.in_waiting > 0:
        message = arduino.readline().decode().strip()
        if message == "INCORRECT_PASSCODE":
            play_incorrect_passcode_audio()

