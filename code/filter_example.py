import cv2
import filter
import kernel
import numpy as np

img = cv2.imread('../images/dolphin.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

k = 2
sigma = 0.5
filter_kernel = kernel.gaussian2d(sigma, k)

out = filter.cross_correlation(img, filter_kernel)

cv2.imshow("original", img)
cv2.imshow("result", out)
cv2.waitKey(0)