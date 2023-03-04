import cv2
import numpy as np
img_red_panda = cv2.imread("red_panda.jpg")
img_red_panda_height, img_red_panda_width, img_red_panda_channels = img_red_panda.shape
print(img_red_panda.shape)

# define color
blue = (255, 0, 0)
red = (0,0,255)
green = (0,255,0)
violet = (255,0,255)
yellow = (255,255,0)
white = (0,0,0)

# # draw line
# cv2.line(img_red_panda, (50, 30), (450, 35), blue, thickness=5)
#
# # draw circle
# cv2.circle(img_red_panda, (10, 15), 10, red, -1)
#
# # draw rectangle
# cv2.rectangle(img_red_panda, (50, 60), (450, 95), green, -1)
#
# # draw eclipse
# cv2.ellipse(img_red_panda, (250, 150), (100, 50), 0, 0, 260, violet, -1)

# points array
points_array = np.array( [[ [100,200],[20,120],[60,200] ]], np.int32)
# # draw poly lines
# cv2.polylines(img_red_panda, points_array, True, yellow,thickness=5)

font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img_red_panda, "panda", (20, 100), font, 4, white)

cv2.imshow("red panda", img_red_panda)

cv2.waitKey(0)
cv2.destroyAllWindows()
