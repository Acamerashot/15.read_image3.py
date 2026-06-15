import cv2

image = cv2.imread("images/mine1.jpg")
if image is not None: Exception("영상파일 읽기 에러")

params_png = [cv2.IMWRITE_PNG_COMPRESSION, 0]

cv2.imwrite("images/mine1.png", image, params_png)
print("저장 완료")