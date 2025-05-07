# Automated Bike Lock System 🚲🔐

A dual-authentication bike lock that uses facial recognition and a keypad to secure your ride.

## 📌 Overview

Developed as a mechatronics engineering capstone project, this system enhances security using:
- **MediaPipe face recognition**
- **4-digit keypad passcode**
- **Arduino-controlled servo motor lock**

## 🛠 Technologies

- Arduino UNO with C++
- Python (OpenCV, MediaPipe)
- Serial Communication (PySerial)
- SolidWorks (3D-printed enclosure)

## 💻 Features

- Facial recognition-based unlock (via webcam)
- Passcode input via 4x4 keypad
- Serial-triggered servo rotation (lock/unlock)
- Audio feedback on invalid input
- Portable and modular enclosure

## 🔩 Hardware Components

- Arduino UNO
- 4x4 Matrix Keypad
- Servo Motor (180°)
- Webcam
- Wires, Breadboard
- Custom 3D-printed lock enclosure

---

## 📂 File Structure

```
📁 Arduino_Code/
    └── ArduinoLock.ino
📁 Python_Code/
    ├── face_recognition_serial_trigger.py
    ├── play_audio_on_signal.py
    ├── haarcascade_frontalface_default.xml
    ├── haarcascade_eye.xml
    └── incorrect_passcode.wav
📁 SolidWorks_Design/
    ├── Lockassem.SLDASM
    ├── hook1.SLDPRT, hook3.SLDPRT, locker.SLDPRT
    ├── holder.SLDPRT, Arm.SLDPRT
    └── frame1.SLDPRT, frame2.SLDPRT
📄 Final_Report.pdf
```

## 🚀 How to Run

### 1. Upload `ArduinoLock.ino` to your Arduino UNO  
Connect via USB and use the Arduino IDE.

### 2. Run the Python script  
Install dependencies:
```bash
pip install opencv-python mediapipe pyserial
```

Run:
```bash
python face_recognition_serial_trigger.py
```

### 3. Profile Registration
- Press `n` in the webcam window to save your face profile
- Enter your name to save profile
- The system will unlock when it recognizes your face with >60% accuracy

---

## 👥 Team Members

- Osman Asif  
- Mohammed Dar  
- Hamzah Faisal  
- Muntadher Alzuaibel  

---

## 📘 License

This project is licensed under the [MIT License](LICENSE).
