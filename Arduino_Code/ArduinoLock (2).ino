#include <Keypad.h>
#include <Servo.h>

const int row = 4;
const int col = 4;
int redLed = 12;     // Red LED for incorrect passcode
int greenLed = 13;   // Green LED for correct passcode
int servoPin = 11;   // Servo control pin

char numPad[row][col] = {
  {'1', '2', '3', 'A'},
  {'4', '5', '6', 'B'},
  {'7', '8', '9', 'C'},
  {'*', '0', '#', 'D'}
};

byte rowPin[row] = {9, 8, 7, 6};
byte colPin[col] = {5, 4, 3, 2};

String password = "4567";  // Default passcode
String vstup = "";         // Input buffer for passcode

bool isLocked = true;      // Track lock state

Keypad cKeypad = Keypad(makeKeymap(numPad), rowPin, colPin, row, col);
Servo lockServo;

void setup() {
    pinMode(redLed, OUTPUT);
    pinMode(greenLed, OUTPUT);
    lockServo.attach(servoPin);
    lockServo.write(90);  // Lock position

    Serial.begin(9600);   // Initialize serial communication
    Serial.println("Enter Passcode: ");
}

void sendIncorrectPasscodeSignal() {
    Serial.println("INCORRECT_PASSCODE"); // Notify the laptop
}

void loop() {
    // Check for serial command for facial recognition
    if (Serial.available() > 0) {
        String command = Serial.readStringUntil('\n');
        if (command == "TRIGGER") {
            Serial.println("Facial recognition signal detected. Unlocking...");
            digitalWrite(redLed, LOW);
            digitalWrite(greenLed, HIGH);
            lockServo.write(0);  // Unlock position
            delay(5000);         // Keep unlocked for 5 seconds
            lockServo.write(90); // Relock position
            digitalWrite(greenLed, LOW);
            isLocked = true;     // Reset lock state
            Serial.println("Enter Passcode: ");
        }
    }

    // Process keypad input
    char cKey = cKeypad.getKey();

    if (cKey != NO_KEY) {  // If a key is pressed
        if (isLocked) {
            if (vstup.length() < 4) {  // Build passcode input
                Serial.print("*");     // Mask input with "*"
                vstup = vstup + cKey;
            }

            if (vstup.length() == 4) {  // When 4 digits are entered
                delay(1500);           // Wait for 1.5 seconds
                if (password == vstup) {  // Correct passcode
                    Serial.println("\nCorrect Passcode. Unlocking...");
                    digitalWrite(redLed, LOW);
                    digitalWrite(greenLed, HIGH);
                    lockServo.write(0);  // Unlock position
                    isLocked = false;    // Update lock state
                    delay(5000);         // Keep unlocked for 5 seconds
                    lockServo.write(90); // Relock position
                    isLocked = true;     // Reset lock state
                } else {  // Incorrect passcode
                    Serial.println("\nWrong Passcode");
                    digitalWrite(redLed, HIGH);
                    digitalWrite(greenLed, LOW);
                    sendIncorrectPasscodeSignal();  // Notify laptop to play audio
                    delay(1000);  // Delay before resetting
                }
                delay(1500);  // Reset input delay
                vstup = "";   // Clear input buffer
                Serial.println("Enter Passcode: ");
                digitalWrite(redLed, LOW);
                digitalWrite(greenLed, LOW);
            }
        } else if (cKey == '0') {  // Manual lock when unlocked
            Serial.println("Manual lock triggered.");
            digitalWrite(redLed, HIGH);
            digitalWrite(greenLed, LOW);
            lockServo.write(90);  // Lock position
            isLocked = true;      // Reset lock state
            Serial.println("Enter Passcode: ");
        }
    }
}
