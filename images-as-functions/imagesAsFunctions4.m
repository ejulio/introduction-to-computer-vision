pkg load image;

dolphin = imread('../images/dolphin.jpg');
bicycle = imread('../images/bicycle.jpg');

bicycle = rgb2gray(bicycle);

disp(size(dolphin));
disp(size(bicycle));

sum = dolphin + bicycle; % washed effect
imshow(sum);
pause(3);

sum = dolphin / 2 + bicycle / 2; % average sum without the washed effect
imshow(sum);
pause(3);

sum = (dolphin + bicycle) / 2; % average sum clipping the value because the limit of 255
imshow(sum);

pause(3);

imshow(scale(0.5, dolphin));

pause(3);

imshow(scale(1.5, dolphin));

pause(3);

imshow(blend(bicycle, dolphin, 0.15));

pause(3);

imshow(blend(bicycle, dolphin, 0.9));