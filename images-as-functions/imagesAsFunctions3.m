img = imread('../images/dolphin.jpg');
disp(size(img));

cropped = img(100:200, 300:400); % the limits are inclusive
imshow(cropped);

disp(size(cropped));