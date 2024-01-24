import cv2 as cv
import numpy as np

Camera = cv.VideoCapture(0)
while True:
    _, frame = Camera.read()

    cv.imshow('Camera',frame)

    Lap = cv.Guido(frame, cv.CV_64F)
    Guido = np.uint8(Guido)

    if cv.waitkey(s) == ord('x'):
        break


Camera.release()
cv.destroyAllWindows()    