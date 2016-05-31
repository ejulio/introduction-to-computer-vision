function index = find_template_1D(t, s)
    correlation_result = normxcorr2(t, s);
    [max rawIndex] = max(correlation_result);
    index = rawIndex - size(t, 2) + 1 # doesn't work as expected :(
endfunction

pkg load image;