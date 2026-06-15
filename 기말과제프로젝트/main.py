import cv2
import os
import datetime

from filters import (
    blur_filter,
    sharpen_filter,
    emboss_filter,
    sketch_filter
)

if not os.path.exists("saved_images"):
    os.makedirs("saved_images")

cap = cv2.VideoCapture(0)

current_filter = 0

while True:

    ret, frame = cap.read()

    if not ret:
        break

    output = frame.copy()

    if current_filter == 1:
        output = blur_filter(frame)

    elif current_filter == 2:
        output = sharpen_filter(frame)

    elif current_filter == 3:
        output = emboss_filter(frame)

    elif current_filter == 4:
        output = sketch_filter(frame)

    cv2.putText(
        output,
        f"Filter: {current_filter}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.imshow("Video Filter App", output)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('0'):
        current_filter = 0

    elif key == ord('1'):
        current_filter = 1

    elif key == ord('2'):
        current_filter = 2

    elif key == ord('3'):
        current_filter = 3

    elif key == ord('4'):
        current_filter = 4

    elif key == ord('s'):

        filename = datetime.datetime.now().strftime(
            "saved_images/%Y%m%d_%H%M%S.jpg"
        )

        cv2.imwrite(filename, output)

        print("저장 완료:", filename)

    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()