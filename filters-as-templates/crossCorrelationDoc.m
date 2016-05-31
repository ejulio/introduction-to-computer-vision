pkg load image;

fruits = rgb2gray(imread('../images/fruits.jpg'));
apple = rgb2gray(imread('../images/apple.jpg'));

# not implemented on octave
#imshowpair(fruits, apple, 'montage');

# normalized correlation
result = normxcorr2(apple, fruits);
figure, surf(result), shading flat;