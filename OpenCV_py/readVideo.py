import cv2

# 读取影片
cap = cv2.VideoCapture('video.mp4')
# 使用电脑摄像头提取画面
# default = 0 外接摄像头 = 1 或以此类推
# cap = cv2.VideoCapture(0)

# Return Two Value
# rat is boolean, for checking the video FPS
# frame is img, for 当他检测到还有下一张照片的时候就会传回来
while True:
    ret, frame = cap.read()
    # 显示图片 如果是true 如果是false 就出去
    if ret: 
        frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
        cv2.imshow('video', frame)
    else:
        break
    if cv2.waitKey(10) == ord('q'):
        break
