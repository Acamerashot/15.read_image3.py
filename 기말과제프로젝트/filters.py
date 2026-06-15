import cv2
import numpy as np


def blur_filter(frame):
    return cv2.GaussianBlur(frame, (15, 15), 0)


def sharpen_filter(frame):
    kernel = np.array([
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0]
    ])

    return cv2.filter2D(frame, -1, kernel)


def emboss_filter(frame):
    kernel = np.array([
        [-2, -1, 0],
        [-1, 1, 1],
        [0, 1, 2]
    ])

    return cv2.filter2D(frame, -1, kernel)


def sketch_filter(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    inverted = 255 - gray

    blur = cv2.GaussianBlur(inverted, (21, 21), 0)

    sketch = cv2.divide(
        gray,
        255 - blur,
        scale=256
    )

    return cv2.cvtColor(sketch, cv2.COLOR_GRAY2BGR)