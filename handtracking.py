import cv2
import mediapipe as mp
import time

# start running webcam

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()

    cv2.imshow("Image", img)
    cv2.waitKey(1)

# Getting different values for points/landmarks is tricky but we'll create a module to easily pinpoint particular points/locations.

