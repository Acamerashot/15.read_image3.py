import numpy as np, cv2

image = cv2.imread("color.jpg")

x1, y1, w1, h1 = (50, 50, 100, 100)
x2, y2, w2, h2 = (300, 200, 100, 100)

image[y1:y1+h1, x1:x1+w1] = cv2.add(image[y1:y1+h1, x1:x1+w1], 100)
roi = image[y2:y2+h2, x2:x2+w2]
avg = cv2.mean(roi)[0]/2.0
image[y2:y2+h2, x2:x2+w2] = cv2.addWeighted(roi, 2.0, roi, 0, -avg)
cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
