from concurrent.futures import wait
import cv2
import numpy as np
import random

# # 读取图片
img = cv2.imread('image.png')
# # img type is 矩阵array
# print(img.shape)

# # 调整图片大小
# # ()里面是自由调整图片大小
# # fx和fy是倍数 0.5倍或2倍
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

# # 显示图片
# cv2.imshow('img', img)

# # 等待视窗自动关闭 或是 有操作键盘按键
# # 0 = 无限 
# # 1000 = 1 sec
# cv2.waitKey(0)

# Remark
# In OpenCV is BGR
# Normal Color is RGB

# 创建新图片
# img = np.empty((300, 300, 3), np.uint8)
# for row in range(300):
#     for col in range(img.shape[1]):
#         img[row][col] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

# 切割出指定区域的照片
newImg = img[300:550, 450:1000]

cv2.imshow('img', img)
cv2.imshow('newImg', newImg)
cv2.waitKey(0)
