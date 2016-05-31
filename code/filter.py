import cv2
import numpy as np

def cross_correlation(img, kernel):
	k = (kernel.shape[0] - 1) // 2
	out = np.zeros(img.shape[:2], dtype = img.dtype)

	for i in range(0, out.shape[1]):
		for j in range(0, out.shape[0]):
			for u in range(-k, k + 1):
				for v in range(-k, k + 1):
					# check for indexes greater than the image
					if j + v >= img.shape[0] or i + u >= img.shape[1]:
						continue
					
					# check for indexes less than the image
					if j + v < 0 or i + u < 0:
						continue

					out[j, i] += kernel[v + k, u + k] * img[j + v, i + u]
	
	return out

def convolution(img, kernel):
	j_k = (kernel.shape[0] - 1) // 2
	i_k = (kernel.shape[1] - 1) // 2
	out = np.zeros(img.shape[:2], dtype = img.dtype)

	for i in range(0, out.shape[1]):
		for j in range(0, out.shape[0]):
			for u in range(-i_k, i_k + 1):
				for v in range(-j_k, j_k + 1):
					# check for indexes greater than the image
					if j - v >= img.shape[0] or i - u >= img.shape[1]:
						continue
					
					# check for indexes less than the image
					if j - v < 0 or i - u < 0:
						continue

					out[j, i] += kernel[v + j_k, u + i_k] * img[j - v, i - u]
	
	return out

def median(img, k):
	size = (2 * k) + 1

	out = np.zeros(img.shape[:2], dtype = img.dtype)

	for i in range(0, out.shape[1]):
		for j in range(0, out.shape[0]):
			if j < k:
				j_above = k - (j + 1)
			else:
				j_above = k

			if j + k > out.shape[0]:
				j_below = (out.shape[0] - (j + k))
			else:
				j_below = k

			if i < k:
				i_left = k - (i + 1)
			else:
				i_left = k
			
			if i + k > out.shape[1]:
				i_right = (out.shape[1] - (i + k))
			else:
				i_right = k

			i_right += 1
			j_below += 1

			window = img[j-j_above:j+j_below, i-i_left:i+i_right]
			window = window.A1 # matrix as row vector
			out[j, i] = np.median(window)
	
	return out

def cross_correlation(img, kernel):
	k = (kernel.shape[0] - 1) // 2
	out = np.zeros(img.shape[:2], dtype = img.dtype)

	img_standard_deviation = img.A1.std()
	img_mean = img.A1.mean()
	kernel_standard_deviation = kernel.A1.std()
	kernel_mean = kernel.A1.mean()
	denominator = img_standard_deviation * kernel_standard_deviation

	for i in range(0, out.shape[1]):
		for j in range(0, out.shape[0]):
			for u in range(-k, k + 1):
				for v in range(-k, k + 1):
					# check for indexes greater than the image
					if j + v >= img.shape[0] or i + u >= img.shape[1]:
						continue
					
					# check for indexes less than the image
					if j + v < 0 or i + u < 0:
						continue

					value = (kernel[v + k, u + k] - kernel_mean) * 
						(img[j + v, i + u] - img_mean)
					value = value / denominator

					out[j, i] += value
	return out