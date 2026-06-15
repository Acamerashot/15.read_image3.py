import numpy as np, cv2

image1 = cv2.imread("images/add1.jpg")
image2 = cv2.imread("images/add2.jpg")

alpha, beta = 0.5, 0.5
add_img = cv2.addWeighted(image1,alpha,image2,beta,0)

cv2.imshow("add1", add_img)
cv2.waitKey(0)
cv2.destroyAllWindows()