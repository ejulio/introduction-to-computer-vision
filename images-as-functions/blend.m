function output = blend(a, b, alpha)
  a = a .* alpha;
  b = b .* (1 - alpha);
  output = a + b;
endfunction