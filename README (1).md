# Automated Bike Lock System 🚲🔐

A dual-authentication smart locking mechanism that secures bicycles using facial recognition and a passcode system, powered by Arduino and Python.

---

## 🧠 Project Motivation

Bike theft is a growing issue in urban environments, especially in university campuses and city cores. Traditional locks can be easily cut, and many smart locks are expensive or complex to use. Our project solves this with a **cost-effective**, **easy-to-use**, and **secure** locking system that combines:

- **Facial recognition** (to eliminate the need for keys)
- **4-digit keypad passcode** (as backup or second layer)
- **Servo-based motorized lock** (triggered via serial communication)

---

## 🔧 System Overview

The system uses a **Python application** to handle real-time facial recognition via a webcam using **MediaPipe** and **OpenCV**. If the face is recognized, it communicates with an **Arduino microcontroller** to activate a **servo motor**, which physically unlocks the bike lock. Alternatively, the user can input a passcode via a 4x4 matrix keypad to achieve the same result.

All components are housed in a **custom 3D-printed enclosure**, designed in **SolidWorks**, for portability and protection.

---

## ⚙️ Components Used

### Hardware:
- Arduino UNO
- 4x4 Matrix Keypad
- Servo Motor (180° rotation)
- Webcam
- Jumper wires, Breadboard
- 3D-printed enclosure (SolidWorks)

### Software:
- Python 3
- OpenCV
- MediaPipe
- PySerial
- Arduino IDE
- SolidWorks (CAD)

---

## 💻 Features

- 🔐 **Dual Authentication**: Unlock using either your face or a 4-digit PIN
- 📷 **Real-time Facial Recognition**: Uses 3D landmark detection with high accuracy
- 🔄 **Serial Communication**: Python sends unlock signals to Arduino
- 🔊 **Audio Feedback**: Error sound when the incorrect passcode is entered
- 📦 **Modular Design**: Easy to assemble and upgrade

---

## 📁 File Structure

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
📄 README.md
📄 .gitignore
```

---

## 🚀 Setup Instructions

### Arduino Side:
1. Open `ArduinoLock.ino` in the Arduino IDE
2. Upload it to the Arduino UNO via USB

### Python Side:
1. Install Python packages:
   ```bash
   pip install opencv-python mediapipe pyserial
   ```
2. Run:
   ```bash
   python face_recognition_serial_trigger.py
   ```
3. Register a new face profile:
   - Press `n` while the webcam window is open
   - Enter your name to save your face profile
   - The system will recognize you next time

---

## 📓 How It Works

1. When powered on, the system waits for either:
   - A 4-digit input on the keypad
   - Recognition of a registered face

2. If authenticated:
   - A `TRIGGER` signal is sent from the Python program to the Arduino via USB
   - The Arduino rotates the servo motor 90° to unlock the mechanism
   - After 5 seconds, it returns to the locked position

3. If authentication fails:
   - An error message is shown
   - An alert sound plays through the Python program

---

## 🔒 Security & Considerations

- Password attempts are limited in the code (can be extended with lockout logic)
- Face accuracy threshold is set at 60% to prevent false positives
- Future upgrades may include:
  - Mobile app integration
  - GPS tracking
  - Multi-user database with Firebase

---

## 👥 Team Members

- Osman Asif  
- Mohammed Dar  
- Hamzah Faisal  
- Muntadher Alzuaibel  

---

## 📘 License

This project is licensed under the [MIT License](LICENSE)

---

## 📄 Final Report

You can find the full technical documentation in [`Final_Report.pdf`](./Final_Report.pdf)

---

## 🧾 Conclusion

The Automated Bike Lock System successfully demonstrates how mechatronics, computer vision, and embedded systems can work together to build secure and user-friendly smart devices. Designed with affordability and accessibility in mind, this project lays the groundwork for practical, real-world deployment in campuses or public bike stations. With further refinement, it could evolve into a market-ready product for personal or commercial use.
