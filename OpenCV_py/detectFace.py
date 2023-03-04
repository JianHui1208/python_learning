import cv2
import numpy as np

img = cv2.imread('image3.png')
img = cv2.resize(img, (0, 0), fx=0.3, fy=0.3)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faceCascade = cv2.CascadeClassifier('face_detect.xml')
faceRect = faceCascade.detectMultiScale(gray, 1.1, 1)
print(len(faceRect))

for (x, y, width, height) in faceRect:
    cv2.rectangle(img, (x, y), (x+width, y+height), (0, 255, 0), 2)

cv2.imshow('img', img)
cv2.waitKey(0)