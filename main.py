import cv2
import numpy as np
import serial

# Initialize serial communication with Sabertooth
ser = serial.Serial('/dev/serial0', 9600)  # Adjust the port as needed

# Open camera
cap = cv2.VideoCapture(0)
cap.set(3, 160)
cap.set(4, 120)

# Define color ranges for line detection
red_lower = np.array([0, 120, 70])
red_upper = np.array([10, 255, 255])
yellow_lower = np.array([20, 100, 100])
yellow_upper = np.array([30, 255, 255])

def stop():
    ser.write(b'\x00')  # Stop both motors

def move_forward():
    ser.write(b'\xC8')  # Command for moving forward 

def move_left():
    ser.write(b'\xB4')  # Command for turning left 

def move_right():
    ser.write(b'\xCC')  # Command for turning right 

while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    red_mask = cv2.inRange(hsv, red_lower, red_upper)
    yellow_mask = cv2.inRange(hsv, yellow_lower, yellow_upper)

    lower_black = np.uint8([0, 0, 0])
    upper_black = np.uint8([180, 255, 30])
    black_mask = cv2.inRange(hsv, lower_black, upper_black)

    contours, _ = cv2.findContours(black_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    red_detected = np.sum(red_mask)
    yellow_detected = np.sum(yellow_mask)

    if red_detected > 1000:
        print("Red line detected, stopping the car.")
        stop()

    elif yellow_detected > 1000:
        print("Yellow line detected, stopping the car.")
        stop()

    else:
        if len(contours) > 0:
            c = max(contours, key=cv2.contourArea)
            M = cv2.moments(c)
            if M["m00"] != 0:
                cx = int(M['m10'] / M['m00'])
                cy = int(M['m01'] / M['m00'])
                print("CX : " + str(cx) + "  CY : " + str(cy))

                if cx >= 120:
                    print("Turn Left")
                    move_left()
                elif 40 < cx < 120:
                    print("On Track!")
                    move_forward()
                else:
                    print("Turn Right")
                    move_right()

                cv2.circle(frame, (cx, cy), 5, (255, 255, 255), -1)
        else:
            print("I don't see the line")
            stop()

    cv2.imshow("Red Mask", red_mask)
    cv2.imshow("Yellow Mask", yellow_mask)
    cv2.imshow("Frame", frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        stop()
        break

cap.release()
cv2.destroyAllWindows()
