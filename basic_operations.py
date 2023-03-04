import cv2


image_flag = cv2.imread("flag.jpg")
print(image_flag[175,300])
image_flag[175,300] = (0,0,0)

3
cv2.imshow("flag", image_flag)

cv2.waitKey(0)
cv2.destroyAllWindows()

