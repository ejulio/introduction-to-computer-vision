img = imread('../images/dolphin.jpg');

hsize = 31;
sigma = 5;
h = fspecial('gaussian', hsize, sigma);

surf(h); % plot surface of h
figure, imagesc(h); % show h

output = imfilter(img, h);
figure, imshow(output);