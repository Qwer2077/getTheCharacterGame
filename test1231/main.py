import cv2 as cv
import numpy as np

img = cv.imread("test8.png", cv.IMREAD_UNCHANGED)
template_ls = []
w, h, channel = img.shape[1], img.shape[0], img.shape[2]
blank_img = np.zeros((h, w, channel), dtype="uint8")

ciKe = cv.imread("ciKe.png", cv.IMREAD_UNCHANGED)
shanZei = cv.imread("shanZei2.png", cv.IMREAD_UNCHANGED)
qianMianRen = cv.imread("qianMianRen.png", cv.IMREAD_UNCHANGED)
zei = cv.imread("zei.png", cv.IMREAD_UNCHANGED)
hei = cv.imread("hei.png", cv.IMREAD_UNCHANGED)
ci = cv.imread("ci.png", cv.IMREAD_UNCHANGED)
she = cv.imread("she.png", cv.IMREAD_UNCHANGED)
mian = cv.imread("mian.png", cv.IMREAD_UNCHANGED)

template_ls.append(ciKe)
template_ls.append(shanZei)
template_ls.append(qianMianRen)
template_ls.append(zei)
template_ls.append(hei)
template_ls.append(ci)
template_ls.append(she)
template_ls.append(mian)

threshold = 0.7

for template in template_ls:
    method = cv.TM_CCOEFF_NORMED
    res = cv.matchTemplate(img, template, method)
    locations = np.where(res >= threshold)
    locations = list(zip(*locations[::-1]))

    temp_w = template.shape[1]
    temp_h = template.shape[0]

    rectangles = []
    for loc in locations:
        rect = [int(loc[0]), int(loc[1]), temp_w, temp_h]
        # Add every box to the list twice in order to retain single (non-overlapping) boxes
        rectangles.append(rect)
        rectangles.append(rect)

    rectangles, weights = cv.groupRectangles(rectangles, groupThreshold=1, eps=0.5)

    for (x, y, w, h) in rectangles:
        top_left = (x - 80, y - 200)
        bottom_right = (x + w + 50, y + h + 50)

        # cv.rectangle(img, top_left, bottom_right, color=(0, 222, 255), thickness=2, lineType=cv.LINE_4)
        blank_img[y - 200:y+h+50, x - 80:x+w+50] = img[y - 200:y+h+50, x - 80:x+w+50]
        print(y, y+h, x, x+w)
        print(h, w)

# imS = cv.resize(img, (1200, 600))                # Resize image
# cv.imshow("img", img)
print(blank_img)

blank_img = cv.resize(blank_img, (1200, 600))
cv.imshow("img", blank_img)

cv.waitKey(0)