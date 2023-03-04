# 1. import Package
import cv2
import numpy as np
import face_recognition

# 2. Loading IMG
liu = cv2.imread("image/liu.jpg")
guo = cv2.imread("image/guo.jpg")

# 3. BRG to RGB
liu_RGB = liu[:, :, ::-1]
guo_RGB = guo[:, :, ::-1]

# 4. detect face
liu_face = face_recognition.face_locations(liu_RGB)
guo_face = face_recognition.face_locations(guo_RGB)

# 5. Face Encoding
liu_encoding = face_recognition.face_encodings(liu_RGB, liu_face)[0]
guo_encoding = face_recognition.face_encodings(guo_RGB, guo_face)[0]

# 6. Create Module
encodings = [liu_encoding, guo_encoding]
names = ["liu de hua", "guo fu cheng"]

# 7. Open Cam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise IOError("Camera Error!")

while True:
    ret, frame = cap.read()
    # 8. BRG to RGB for cap image
    frame_RGB = frame[:, :, ::-1]
    # 9. Face Detect for Cap
    faces_locations = face_recognition.face_locations(frame_RGB)
    # 10. Image Encoding for Cap
    faces_encoding = face_recognition.face_encodings(frame_RGB, faces_locations)
    # 11. 使用Module和Cap的Image进行对比
    for (top, right, bottom, left), face_encoding in zip(faces_locations, faces_encoding):
        # 12. 进行匹配
        matche = face_recognition.compare_faces(encodings, face_encoding)
        # 13. 计算距离
        distances = face_recognition.face_distance(encodings, face_encoding)
        min_distance_index = np.argmin(distances)
        # 14. 判断
        name = "Unknown"
        if matche[min_distance_index]:
            name = names[min_distance_index]
        # 15. 画框框
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 3)
        # 16. 写名字
        cv2.rectangle(frame, (left, bottom-30), (right, bottom), (0, 0, 255), 3)
        cv2.putText(frame, name, (left+10, bottom-10), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1)

    # 显示图片
    cv2.imshow('Face Recognition', frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
