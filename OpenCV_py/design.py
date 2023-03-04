import cv2
from cv2 import FONT_HERSHEY_COMPLEX
import numpy as np

# 制作黑色图片
img = np.zeros((600, 600, 3), np.uint8)

# 画线
# line(照片, (fx1, fy1), (fx2, fy2), 线的颜色， 线的粗度)
# img.shape[1] = width, img.shape[0] = height
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (255, 255, 255), 2)

# 画正方形
# rectangle(照片, (fx1, fy1), (fx2, fy2), 线的颜色， 线的粗度/cv2.FILLED(把正方形填满颜色))
cv2.rectangle(img, (100, 200), (400, 300), (255, 255, 255), cv2.FILLED)

# 画圆形
# circle(照片, (fx1, fy2), 圆的半径, 线的颜色， 线的粗度/cv2.FILLED(把圆形填满颜色))
cv2.circle(img, (300, 400), 30, (255, 0, 0), 1)

# 写文字
# putText(照片, 要写的文字, (fx1, fy2), font style, font size, font color, font粗度)
# !!!不支持中文!!!
cv2.putText(img, 'Hello', (100, 500), cv2.FONT_HERSHEY_COMPLEX, 5, (255, 255, 255), 5)

cv2.imshow('img', img)
cv2.waitKey(0)
