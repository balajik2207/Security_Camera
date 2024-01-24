#Face detection

import numpy as np
import cv2
import time

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

camera = cv2.VideoCapture()-1

while camera.isOpened():
    ret, img = camera.read()

    if not ret:
        print("Can't receive frame (stream end?). Exiting...")
        break

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

        cv2.putText(img, f"Face Detected at {timestamp}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

        print(f"Alert: Face detected at {timestamp}")

    cv2.imshow('img', img)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()