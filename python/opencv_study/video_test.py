import cv2
import numpy as np

cap = cv2.VideoCapture("D:\\4_School_Works\\2022_Gradproj\\chopsticks_credit.mp4")
# test commit

if cap.isOpened() is False:
    print("Error opening video stream or file")

while cap.isOpened():
    ret, frame = cap.read()
    if ret is True:
        cv2.imshow('Frame', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
