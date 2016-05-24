import cv2
import math
import numpy as np

def apply_filter(img, kernel):
	k = (kernel.shape[0] - 1) // 2
	out = np.zeros(img.shape[:2], dtype = img.dtype)

	for i in range(0, out.shape[1]):
		for j in range(0, out.shape[0]):
			for u in range(-k, k + 1):
				for v in range(-k, k + 1):
					if j + v >= img.shape[0] or i + u >= img.shape[1]:
						continue
					
					if j + v < 0 or i + u < 0:
						continue

					out[j, i] += kernel[v + k, u + k] * img[j + v, i + u]
	
	return out

def gaussian_kernel(sigma, k):
	size = (2 * k) + 1
	kernel = np.zeros((size, size), dtype = np.float32)

	sigma_squared = sigma ** 2
	denominator = 2 * math.pi * sigma_squared
	for i in range(0, size):
		for j in range(0, size):
			power = - (((i - k)**2 + (j - k)**2) / (2 * sigma_squared))
			kernel[j, i] = (1 / denominator) * math.exp(power)

	return kernel

img = cv2.imread('../images/dolphin.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

k = 3
sigma = 1
kernel = gaussian_kernel(sigma, k)
print(kernel)

out = apply_filter(img, kernel)

cv2.imshow("original", img)
cv2.imshow("result", out)
cv2.waitKey(0)

def test_1():
	img = np.matrix([
		[10, 20, 30, 40],
		[50, 20, 20, 10],
		[30, 60, 75, 50],
		[30, 60, 75, 40]], dtype = np.uint8)

	kernel = np.matrix([
		[1, 1, 1],
		[1, 1, 1],
		[1, 1, 1]], dtype = np.float32)
	kernel = kernel * (1/9)

	out = apply_filter(img, kernel)

	expected = ((img[0, 0] // 9) + (img[0, 1] // 9) +
		(img[1, 0] // 9) + (img[1, 1] // 9))
	print("{} == {}".format(out[0, 0], expected))
	assert out[0, 0] == expected

	expected = ((img[0, 0] // 9) + (img[0, 1] // 9) + (img[0, 2] // 9) + 
		(img[1, 0] // 9) + (img[1, 1] // 9) + (img[1, 2] // 9) + 
		(img[2, 0] // 9) + (img[2, 1] // 9) + (img[2, 2] // 9))
	print("{} == {}".format(out[1, 1], expected))
	assert out[1, 1] == expected

	expected = ((img[1, 0] // 9) + (img[1, 1] // 9) + 
		(img[2, 0] // 9) + (img[2, 1] // 9) + 
		(img[3, 0] // 9) + (img[3, 1] // 9))
	print("{} == {}".format(out[2, 0], expected))
	assert out[2, 0] == expected

	expected = ((img[1, 0] // 9) + (img[1, 1] // 9) + (img[1, 2] // 9) + 
		(img[2, 0] // 9) + (img[2, 1] // 9) + (img[2, 2] // 9) + 
		(img[3, 0] // 9) + (img[3, 1] // 9) + (img[3, 2] // 9))
	print("{} == {}".format(out[2, 1], expected))
	assert out[2, 1] == expected

	expected = ((img[1, 1] // 9) + (img[1, 2] // 9) + (img[1, 3] // 9) + 
		(img[2, 1] // 9) + (img[2, 2] // 9) + (img[2, 3] // 9) + 
		(img[3, 1] // 9) + (img[3, 2] // 9) + (img[3, 3] // 9))
	print("{} == {}".format(out[2, 2], expected))
	assert out[2, 2] == expected

	expected = ((img[2, 2] // 9) + (img[2, 3] // 9) +
		(img[3, 2] // 9) + (img[3, 3] // 9))
	print("{} == {}".format(out[3, 3], expected))
	assert out[3, 3] == expected

def test_2():
	img = np.matrix([
		[10, 20, 30, 40, 73, 42, 53],
		[50, 20, 20, 10, 88, 35, 92],
		[30, 60, 75, 50, 12, 92, 42],
		[30, 60, 75, 50, 12, 92, 42],
		[30, 60, 75, 50, 12, 92, 42],
		[30, 60, 75, 40, 38, 31, 57]], dtype = np.uint8)

	kernel = np.matrix([
		[1, 1, 1, 1, 1],
		[1, 1, 1, 1, 1],
		[1, 1, 1, 1, 1],
		[1, 1, 1, 1, 1],
		[1, 1, 1, 1, 1]], dtype = np.float32)
	kernel = kernel * (1/9)

	out = apply_filter(img, kernel)

	expected = ((img[3, 4] // 9) + (img[3, 5] // 9) + (img[3, 6] // 9) +
		(img[4, 4] // 9) + (img[4, 5] // 9) + (img[4, 6] // 9) +
		(img[5, 4] // 9) + (img[5, 5] // 9) + (img[5, 6] // 9))
	print("{} == {}".format(out[0, 0], expected))
	assert out[5, 6] == expected


# test_1()
# test_2()