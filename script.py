import numpy as np
import cv2
camera = cv2.VideoCapture(0)

while True:
    ret, img = camera.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('e'):
        break
camera.release()
cv2.destroyAllWindows()