pkg load image;

img = imread('../images/fall-leaves.jpg');
imshow(img);

% gaussian 11x11 sigma = 8
gaussian = fspecial('gaussian', 11, 8);

% black clipping
filtered = imfilter(img, gaussian, 0);
figure, imshow(filtered);

% white clipping
filtered = imfilter(img, gaussian, 255);
figure, imshow(filtered);

% wraping around
filtered = imfilter(img, gaussian, 'circular');
figure, imshow(filtered);

% copying edges
filtered = imfilter(img, gaussian, 'circular');
figure, imshow(filtered);

% reflecting edges
filtered = imfilter(img, gaussian, 'symmetric');
figure, imshow(filtered);