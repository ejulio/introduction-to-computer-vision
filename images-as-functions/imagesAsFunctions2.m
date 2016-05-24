img = imread('../images/dolphin.jpg');
imshow(img);
disp(size(img)); % size of the image
disp(class(img)); % image datatype

% img(row, column)
disp(img(50, 30)); % intensity at row 50, column 30

pause(3);

disp(img(50:55, 30:35)); % intensity at row 50 to 55, column 30 to 35

pause(3);

disp(img(50, :)); % all column intensities of row 50

pause(3);

disp(img(:, 30)); % all row intensities of column 30