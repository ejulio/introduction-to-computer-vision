import math
import numpy as np

def gaussian2d(sigma, k):
	size = (2 * k) + 1
	kernel = np.zeros((size, size), dtype = np.float32)

	sigma_squared = sigma ** 2
	denominator = 2 * math.pi * sigma_squared
	p_denominator = 2 * sigma_squared
	for i in range(0, size):
		for j in range(0, size):
			x_squared = (i - k) ** 2
			y_squared = (j - k) ** 2
			p = (x_squared + y_squared) / p_denominator
			kernel[j, i] = math.exp(-p) / denominator

	kernel = kernel / np.sum(kernel)

	return kernel

def gaussian(sigma, k):
	size = (2 * k) + 1
	kernel = np.zeros((1, size), dtype = np.float32)

	sigma_squared = sigma ** 2
	p_denominator = 2 * sigma_squared
	denominator = math.sqrt(2 * math.pi) * sigma

	for i in range(0, size):
		x_squared = (i - k) ** 2
		p = x_squared / p_denominator
		kernel[0, i] = math.exp(-p) / denominator

	kernel = kernel / np.sum(kernel)

	return kernel

def sobel_horizontal():
	kernel = np.array([
		[-1, 0, 1],
		[-2, 0, 2],
		[-1, 0, 1]
		], dtype = np.float32)

	kernel = kernel / 8

	return kernel

def sobel_vertical():
	kernel = np.array([
		[-1, -2, -1],
		[0,   0,  0],
		[1,   2,  1],
		], dtype = np.float32)

	kernel = kernel / 8

	return kernel