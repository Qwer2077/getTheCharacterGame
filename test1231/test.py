import cv2 as cv
import numpy as np

img = cv.imread("testImage.png", cv.IMREAD_UNCHANGED)
template = cv.imread("shanZei2.png", cv.IMREAD_UNCHANGED)
# w, h = img.shape[1], img.shape[0]
# blank_img = np.zeros((w, h, 1), dtype="uint8")

res = cv.matchTemplate(img, template, cv.TM_SQDIFF_NORMED)

threshold = 0.40
locations = np.where(res <= threshold)
locations = list(zip(*locations[::-1]))

needle_w = template.shape[1]
needle_h = template.shape[0]
line_color = (0, 255, 0)
line_type = cv.LINE_4

for loc in locations:
    # Determine the box positions
    top_left = loc
    bottom_right = (top_left[0] + needle_w, top_left[1] + needle_h)
    # Draw the box
    cv.rectangle(img, top_left, bottom_right, line_color, line_type)

img = cv.resize(img, (1200, 600))
cv.imshow("img", img)

cv.waitKey(0)
