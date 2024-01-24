#Face detection

import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

camera = cv2.VideoCapture(0)
#camera.open(0)
while camera.isOpened():
    ret, img = camera.read()

    if not ret:
        print("Can't receive frame (stream end?). Exiting...")
        break

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow('img', img)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        #print("Alert")
        break

camera.release()
cv2.destroyAllWindows()

