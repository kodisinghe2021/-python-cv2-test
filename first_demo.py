import cv2

image = cv2.imread("red_panda.jpg")
image_gray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
cv2.imwrite("gray_panda.jpg",image_gray)
# cv2.imshow("red panda", image_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
