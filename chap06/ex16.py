import numpy as np, cv2
from Common.histogram import draw_histo
image = cv2.imread("images/low2.jpg", cv2.IMREAD_GRAYSCALE)
bins, ranges = [256], [0, 256]
hist = cv2.calcHist([image], [0], None, bins, ranges)
hist_img = draw_histo(hist)

dst = cv2.normalize(image, None, 0, 255, cv2.NORM_MINMAX)
hist_dst = cv2.calcHist([dst], [0], None, bins, ranges)
hist_dst_img = draw_histo(hist_dst, (200,360))

cv2.imshow("image", image)
cv2.imshow("hist_img", hist_img)
cv2.imshow("stretching", dst);
cv2.imshow("hist_stretching_img", hist_dst_img)
cv2.waitKey(0)