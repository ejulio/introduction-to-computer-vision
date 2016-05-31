import cv2
import filter
import numpy as np

def cross_correlation_test_1():
	img = np.matrix([
		[0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0],
		[0, 0, 1, 0, 0],
		[0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0]
		], dtype = np.uint8)

	kernel = np.matrix([
		[1, 2, 3],
		[4, 5, 6],
		[7, 8, 9]
		], dtype = np.uint8)

	out = filter.cross_correlation(img, kernel)

	assert out[1, 1] == kernel[2, 2]
	assert out[1, 2] == kernel[2, 1]
	assert out[1, 3] == kernel[2, 0]

	assert out[2, 1] == kernel[1, 2]
	assert out[2, 2] == kernel[1, 1]
	assert out[2, 3] == kernel[1, 0]
	
	assert out[3, 1] == kernel[0, 2]
	assert out[3, 2] == kernel[0, 1]
	assert out[3, 3] == kernel[0, 0]

def cross_correlation_test_2():
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

	out = filter.cross_correlation(img, kernel)

	expected = ((img[0, 0] // 9) + (img[0, 1] // 9) +
		(img[1, 0] // 9) + (img[1, 1] // 9))
	assert out[0, 0] == expected

	expected = ((img[0, 0] // 9) + (img[0, 1] // 9) + (img[0, 2] // 9) + 
		(img[1, 0] // 9) + (img[1, 1] // 9) + (img[1, 2] // 9) + 
		(img[2, 0] // 9) + (img[2, 1] // 9) + (img[2, 2] // 9))
	assert out[1, 1] == expected

	expected = ((img[1, 0] // 9) + (img[1, 1] // 9) + 
		(img[2, 0] // 9) + (img[2, 1] // 9) + 
		(img[3, 0] // 9) + (img[3, 1] // 9))
	assert out[2, 0] == expected

	expected = ((img[1, 0] // 9) + (img[1, 1] // 9) + (img[1, 2] // 9) + 
		(img[2, 0] // 9) + (img[2, 1] // 9) + (img[2, 2] // 9) + 
		(img[3, 0] // 9) + (img[3, 1] // 9) + (img[3, 2] // 9))
	assert out[2, 1] == expected

	expected = ((img[1, 1] // 9) + (img[1, 2] // 9) + (img[1, 3] // 9) + 
		(img[2, 1] // 9) + (img[2, 2] // 9) + (img[2, 3] // 9) + 
		(img[3, 1] // 9) + (img[3, 2] // 9) + (img[3, 3] // 9))
	assert out[2, 2] == expected

	expected = ((img[2, 2] // 9) + (img[2, 3] // 9) +
		(img[3, 2] // 9) + (img[3, 3] // 9))
	assert out[3, 3] == expected

def cross_correlation_test_3():
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

	out = filter.cross_correlation(img, kernel)

	expected = ((img[3, 4] // 9) + (img[3, 5] // 9) + (img[3, 6] // 9) +
		(img[4, 4] // 9) + (img[4, 5] // 9) + (img[4, 6] // 9) +
		(img[5, 4] // 9) + (img[5, 5] // 9) + (img[5, 6] // 9))
	assert out[5, 6] == expected

def convolution_test_1():
	img = np.matrix([
		[0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0],
		[0, 0, 1, 0, 0],
		[0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0]], dtype = np.uint8)

	kernel = np.matrix([
		[1, 2, 3],
		[4, 5, 6],
		[7, 8, 9]], dtype = np.uint8)

	out = filter.convolution(img, kernel)

	assert out[1, 1] == kernel[0, 0]
	assert out[1, 2] == kernel[0, 1]
	assert out[1, 3] == kernel[0, 2]

	assert out[2, 1] == kernel[1, 0]
	assert out[2, 2] == kernel[1, 1]
	assert out[2, 3] == kernel[1, 2]
	
	assert out[3, 1] == kernel[2, 0]
	assert out[3, 2] == kernel[2, 1]
	assert out[3, 3] == kernel[2, 2]

def convolution_test_2():
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

	out = filter.convolution(img, kernel)

	expected = ((img[3, 4] // 9) + (img[3, 5] // 9) + (img[3, 6] // 9) +
		(img[4, 4] // 9) + (img[4, 5] // 9) + (img[4, 6] // 9) +
		(img[5, 4] // 9) + (img[5, 5] // 9) + (img[5, 6] // 9))
	assert out[5, 6] == expected

def convolution_test_3():
	img = np.matrix([
		[0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0],
		[0, 0, 1, 0, 0],
		[0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0]], dtype = np.uint8)

	kernel = np.matrix([
		[1, 2, 1]], dtype = np.uint8)

	kernel_t = np.transpose(kernel)

	out = filter.convolution(img, kernel_t)
	out = filter.convolution(out, kernel)

	assert out[1, 1] == kernel[0, 0]
	assert out[1, 2] == kernel[0, 1]
	assert out[1, 3] == kernel[0, 2]

	assert out[2, 1] == 2
	assert out[2, 2] == 4
	assert out[2, 3] == 2
	
	assert out[3, 1] == kernel[0, 0]
	assert out[3, 2] == kernel[0, 1]
	assert out[3, 3] == kernel[0, 2]

def convolution_test_4():
	img = np.matrix([
		[0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0],
		[0, 0, 1, 0, 0],
		[0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0]], dtype = np.uint8)

	kernel = np.matrix([
		[1, 2, 1]], dtype = np.uint8)

	kernel_t = np.transpose(kernel)

	out = filter.convolution(img, kernel)
	out = filter.convolution(out, kernel_t)

	assert out[1, 1] == kernel[0, 0]
	assert out[1, 2] == kernel[0, 1]
	assert out[1, 3] == kernel[0, 2]

	assert out[2, 1] == 2
	assert out[2, 2] == 4
	assert out[2, 3] == 2
	
	assert out[3, 1] == kernel[0, 0]
	assert out[3, 2] == kernel[0, 1]
	assert out[3, 3] == kernel[0, 2]

def median_test_1():
	img = np.matrix([
		[10, 20, 30, 40, 50],
		[50, 40, 30, 20, 10],
		[70, 30, 80, 25, 13],
		[12, 23, 1, 100, 65],
		[34, 63, 3, 145, 42]], dtype = np.uint8)

	k = 1
	out = filter.median(img, k)

	print(img)
	print(out)

	assert out[0, 0] == 30
	assert out[0, 1] == 30
	assert out[0, 2] == 30
	assert out[0, 3] == 30
	assert out[0, 4] == 30

	assert out[1, 0] == 35
	assert out[1, 1] == 30
	assert out[1, 2] == 30
	assert out[1, 3] == 30
	assert out[1, 4] == 22

	assert out[2, 0] == 35
	assert out[2, 1] == 30
	assert out[2, 2] == 30
	assert out[2, 3] == 25
	assert out[2, 4] == 22

	assert out[3, 0] == 32
	assert out[3, 1] == 30
	assert out[3, 2] == 30
	assert out[3, 3] == 42
	assert out[3, 4] == 53

	assert out[4, 0] == 28
	assert out[4, 1] == 17
	assert out[4, 2] == 43
	assert out[4, 3] == 53
	assert out[4, 4] == 82

print("correlation_test_1")
cross_correlation_test_1()

print("correlation_test_2")
cross_correlation_test_2()

print("correlation_test_3")
cross_correlation_test_3()

print("convolution_test_1")
convolution_test_1()

print("convolution_test_2")
convolution_test_2()

print("convolution_test_3")
convolution_test_3()

print("convolution_test_4")
convolution_test_4()

print("median_test_1")
median_test_1()