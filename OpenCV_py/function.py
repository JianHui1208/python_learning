import cv2
import numpy as np

# 二维数组
kernel1 = np.ones((10, 10), np.uint8)
kernel2 = np.ones((10, 10), np.uint8)

img = cv2.imread('image.png')
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

# 转换图片变成灰阶
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 转换图片变成模糊
# ()里面的号码一定要是odd
blur = cv2.GaussianBlur(img, (15, 15), 10)

# 找到图片中的边缘
canny = cv2.Canny(img, 200, 250)

# 制作膨胀图片 线条变粗
# kernal的数组越大 膨胀系数越大
dilate = cv2.dilate(canny, kernel1, iterations=1)

# 制作膨胀图片 线条变细
erode = cv2.erode(dilate, kernel2, iterations=1)

cv2.imshow('img', img)
# cv2.imshow('gray', gray)
# cv2.imshow('blur', blur)
cv2.imshow('canny', canny)
cv2.imshow('dilate', dilate)
cv2.imshow('erode', erode)
cv2.waitKey(0)