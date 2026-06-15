import numpy as np
import cv2

red = (0, 0, 255)
image = np.zeros((600, 400, 3), np.uint8)
image[:] = (255, 255, 255)

pt1, pt2 = (100, 100), (300,400)

cv2.rectangle(image, pt1, pt2, red, 2)

cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()