import cv2


image_panda = cv2.imread("red_panda.jpg")
crope_panda = image_panda[100:280, 150:320]

cv2.imshow("panda", image_panda)
cv2.imshow("crop_panda", crope_panda)
cv2.waitKey(0)
cv2.destroyAllWindows()

