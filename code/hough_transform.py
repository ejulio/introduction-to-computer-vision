import cv2
import numpy as np
import math

image = np.zeros((100, 100), dtype = np.uint8)
line_js = np.arange(25, 75)
line_is = line_js[::-1]
image[line_is, line_js] = 255
image[line_js, line_js] = 255

def euclidean_distance(a, b):
	return math.sqrt(a ** 2 + b ** 2)

def smooth_voting(space, i, j):
	start_i = i if i == 0 else i - 1
	end_i = i if i == space.shape[0] - 1 else i + 1
	start_j = j if j == 0 else j - 1
	end_j = j if j == space.shape[1] - 1 else j + 1
	
	for u in xrange(start_i, end_i + 1):
		for v in xrange(start_j, end_j + 1):
			space[u, v] += 1

def hough_lines(image, theta_precision = 5, d_precision = 2):
	d_max = euclidean_distance(image.shape[1], image.shape[0])
	d_max = math.ceil(d_max)
	d_bins = np.arange(-d_max, d_max + 1, d_precision)

	theta_bins = np.arange(0, 181, theta_precision)

	hough_size = (d_bins.shape[0], theta_bins.shape[0])
	hough_space = np.zeros(hough_size, dtype = np.uint8)
	
	for i in xrange(0, image.shape[0]):
		for j in xrange(0, image.shape[1]):
			if image[i, j] == 0:
				continue

			for theta_index, theta in enumerate(theta_bins):
				theta = math.radians(theta)
				d = j * math.cos(theta) + i * math.sin(theta)
				d_distances = np.absolute(d - d_bins)
				d_index = np.argmin(d_distances)
				hough_space[d_index, theta_index] += 1

	hough_space = cv2.normalize(hough_space, 0, 255, cv2.NORM_MINMAX)
	return (hough_space, d_bins, theta_bins)

def hough_peaks(hough_space, d_bins, theta_bins):
	hough_max = np.max(hough_space)
	threshold = 0.5 * hough_max

	params = []

	for i in xrange(0, hough_space.shape[0]):
		for j in xrange(0, hough_space.shape[1]):
			if hough_space[i, j] > threshold:
				params.append((d_bins[i], theta_bins[j]))

	return params
			

hough_space, d_bins, theta_bins = hough_lines(image)
lines_params = hough_peaks(hough_space, d_bins, theta_bins)

print hough_space[105, 8]
print hough_space[105, 9]
print hough_space[105, 10]
print hough_space[106, 8]
print hough_space[106, 9]
print hough_space[106, 10]
print hough_space[107, 8]
print hough_space[107, 9]
print hough_space[107, 10]
# expected params (70, 45)
out = cv2.merge([image, image, image])

for d, theta in lines_params:
	theta = math.radians(theta)

	x1 = 0
	y1 = int(float(d - x1 * math.cos(theta)) / math.sin(theta))
	
	x2 = image.shape[1]
	y2 = int(float(d - x2 * math.cos(theta)) / math.sin(theta))

	cv2.line(out, (x1, y1), (x2, y2), (0, 0, 255), 1)

cv2.imshow("OUT", out)
cv2.waitKey(0)