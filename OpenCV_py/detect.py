import cv2
import numpy as np

def empty(v):
    pass


img = cv2.imread('image2.jpg')
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

# 制作一个新窗口
cv2.namedWindow('TrackBar')
# resizeWindow(窗口名, width, height)
cv2.resizeWindow('TrackBar', 640, 320)

cv2.createTrackbar('Hue Min', 'TrackBar', 0,  179, empty)
cv2.createTrackbar('Hue Max', 'TrackBar', 179,  179, empty)
cv2.createTrackbar('Saturation Min', 'TrackBar', 0,  255, empty)
cv2.createTrackbar('Saturation Max', 'TrackBar', 255,  255, empty)
cv2.createTrackbar('Value Min', 'TrackBar', 0,  255, empty)
cv2.createTrackbar('Value Max', 'TrackBar', 255,  255, empty)

# HSV
# h = Hue 色调
# s = Saturation 饱和度
# v = Value 亮度
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

while True:
    h_min = cv2.getTrackbarPos('Hue Min', 'TrackBar')
    h_max = cv2.getTrackbarPos('Hue Max', 'TrackBar')
    s_min = cv2.getTrackbarPos('Saturation Min', 'TrackBar')
    s_max = cv2.getTrackbarPos('Saturation Max', 'TrackBar')
    v_min = cv2.getTrackbarPos('Value Min', 'TrackBar')
    v_max = cv2.getTrackbarPos('Value Max', 'TrackBar')
    print(h_min, h_max, s_min, s_max, v_min, v_max)

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])

    mask = cv2.inRange(hsv, lower, upper)
    result = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow('img', img)
    cv2.imshow('hsv', hsv)
    cv2.imshow('mask', mask)
    cv2.imshow('result', result)
    cv2.waitKey(1)



