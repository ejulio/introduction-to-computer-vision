function [yIndex xIndex] = find_template_2D(template, img)
    pkg load image;
    
    c = normxcorr2(template, img);
    [v, index] = max(c(:));
    [y, x] = ind2sub(size(c), index);
    y = y - size(template, 1) + 1;
    x = x - size(template, 2) + 1;
    
    yIndex = y;
    xIndex = x;
endfunction
