import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    flipper = cv2.flip(frame,0)

    cv2.imshow("vid",flipper)
    cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()
