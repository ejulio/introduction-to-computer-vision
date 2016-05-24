im = imread('../images/fruits.jpg');
% all rows and columns, only channel 2 (green)
imgreen = im(:, :, 2);
imshow(imgreen);

% horizontal red line from (1, 100) to (350, 100)
line([1 350], [100 100], 'color', 'r');
% vertical green line from (50, 1) to (50, 209)
line([50 50], [1 209], 'color', 'g');
% line(X, Y)
% first argument are X coordinates and second argument are Y corrdinates

pause(10);
% plot the intensities for all columns of row 150
plot(imgreen(150, :))