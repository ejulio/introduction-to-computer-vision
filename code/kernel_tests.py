import kernel
import numpy as np

def test_gaussian2d_1():
	sigma = 1
	k = 2

	filter_kernel = kernel.gaussian2d(sigma, k)

	assert filter_kernel.shape[0] == 2 * k + 1
	assert filter_kernel.shape[1] == 2 * k + 1

def test_gaussian2d_2():
	sigma = 1
	k = 2

	filter_kernel = kernel.gaussian2d(sigma, k)

	assert np.sum(filter_kernel) == 1
	
def test_gaussian_1():
	sigma = 2
	k = 1

	filter_kernel = kernel.gaussian(sigma, k)

	assert filter_kernel.shape[0] == 1
	assert filter_kernel.shape[1] == 2 * k + 1

def test_gaussian_2():
	sigma = 2
	k = 3

	filter_kernel = kernel.gaussian(sigma, k)

	assert np.sum(filter_kernel) == 1

def sobel_horizontal_test_1():
	filter_kernel = kernel.sobel_horizontal()

	assert np.sum(filter_kernel) == 0

def sobel_vertical_test_1():
	filter_kernel = kernel.sobel_vertical()

	assert np.sum(filter_kernel) == 0

def sobel_horizontal_test_2():
	filter_kernel = kernel.sobel_horizontal()

	filter_kernel = np.absolute(filter_kernel)

	assert np.sum(filter_kernel) == 1

def sobel_vertical_test_2():
	filter_kernel = kernel.sobel_vertical()

	filter_kernel = np.absolute(filter_kernel)

	assert np.sum(filter_kernel) == 1

print("test_gaussian2d_1")
test_gaussian2d_1()

print("test_gaussian2d_2")
test_gaussian2d_2()

print("test_gaussian_1")
test_gaussian_1()

print("test_gaussian_2")
test_gaussian_2()

print("sobel_horizontal_test_1")
sobel_horizontal_test_1()

print("sobel_horizontal_test_2")
sobel_horizontal_test_2()

print("sobel_vertical_test_1")
sobel_vertical_test_1()

print("sobel_vertical_test_2")
sobel_vertical_test_2()