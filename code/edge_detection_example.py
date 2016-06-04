import filter
import kernel
import cv2
import math
import numpy as np

image = cv2.imread("../images/octagon.png")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

sobel_horizontal = kernel.sobel_horizontal()
sobel_vertical = kernel.sobel_vertical()

out_horizontal = filter.cross_correlation(image, sobel_horizontal)
out_vertical = filter.cross_correlation(image, sobel_vertical)

r = [math.sqrt(h**2 + v**2) for h, v in zip(out_horizontal.flat, out_vertical.flat)]
edges = np.array(r).reshape(image.shape)
edges = cv2.convertScaleAbs(edges.copy())

r = [math.degrees(math.atan(v/h)) if h > 0 else 0 for h, v in zip(out_horizontal.flat, out_vertical.flat)]
directions = np.array(r).reshape(image.shape)
directions = cv2.convertScaleAbs(directions.copy())

cv2.imshow("H", out_horizontal)
cv2.imshow("V", out_vertical)
cv2.imshow("E", edges)
cv2.imshow("D", directions)
cv2.waitKey(0)