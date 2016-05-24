noise = randn([1000 1000]) .* 2;
imshow(noise, [-100 100]); % [LOW HIGH]

noise = randn([1000 1000]) .* 16;
figure, imshow(noise, [-100 100]); % [LOW HIGH]

noise = randn([1000 1000]) .* 32;
figure, imshow(noise, [-100 100]); % [LOW HIGH]

noise = randn([1000 1000]) .* 64;
figure, imshow(noise, [-100 100]); % [LOW HIGH]

noise = randn([1000 1000]) .* 16;
figure, imshow(noise, []); % [] compute automatically