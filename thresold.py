import cv2
import numpy as np

image_road = cv2.imread("road.jpg")
image_car = cv2.imread("car.jpg")

cv2.imshow("car",image_car)
cv2.imshow("road", image_road)

cv2.waitKey(0)
cv2.destroyAllWindows()