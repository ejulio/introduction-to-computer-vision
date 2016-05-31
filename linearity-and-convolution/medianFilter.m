pkg load image;

img = imread('../images/moon.jpg');
img = rgb2gray(img);
imshow(img);

noisy_img = imnoise(img, 'salt & pepper', 0.02);
figure, imshow(noisy_img);

median_filtered = medfilt2(noisy_img);
figure, imshow(median_filtered);