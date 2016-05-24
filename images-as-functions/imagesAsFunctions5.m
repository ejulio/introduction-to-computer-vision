pkg load image;
img = imread('../images/fruits.jpg');
img = rgb2gray(img);

sigma = 7;
noise = randn(size(img)) .* sigma;

imgWithNoise = img + noise;

imshow(img);
figure, imshow(imgWithNoise);

figure, plot(img(50, :));
figure, plot(imgWithNoise(50, :));

noise = randn([1 10000]);
[counts bins] = hist(noise, linspace(-3, 3, 21)); % 21 bins from -3 to 3
disp([bins; counts]);
figure, plot(bins, counts);