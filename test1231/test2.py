import cv2 as cv
import numpy as np

img = cv.imread("testImage.png")
# img = cv.imread("testImage.png")
# template = cv.imread("shanZei2.png", cv.IMREAD_UNCHANGED)
# w, h = img.shape[1], img.shape[0]
# channel = img.shape[2]
print(img.shape)
# blank_img = np.zeros((h, w, channel), dtype="uint8")
# blank_img[50:100][0:1000] = img[50:200][0:1500]

crop_img = img[500:807, 200:1739].copy()
# print(crop_img)
# print(len(img))

# cv.imshow("img", blank_img)
cv.imshow("cropped", crop_img)
# cv.imshow("img", img)

cv.waitKey(0)