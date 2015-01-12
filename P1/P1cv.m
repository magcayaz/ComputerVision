% (b) write and run code that {gets RGB (see attached or choose another RGB) image and display / print the image,
% transform the RGB image to gray scale, find out the mean and variance for both RGB and gray-scale images,
% normalize the gray-scale image using min and max gray values(e.g.,  range), calculate, display, and
% print  the histogram for both RGB and gray value images}, and transform the gray level image to a binary image}
% (c) Computational Photography (using D01-slide 23 <original vs. fog added>: (c1) using Matlab; and (c2)using  OpenCV
% find the best mix of gamma correction and histogram equalization to defog images. Towards that end define some
% measure of image quality (e.g., high frequency contents) to seek for best image quality.


img = imread('test.jpg');

%show original Image and pring mean + variance
figure();
imshow(img);
title(['Original Image'])
xlabel(['x pixels'])
ylabel(['y pixels'])
disp('Original Image mean');
muImg = mean(img(:))
disp('Original Image variance');
varImg = var(double(img(:)))

%transform the image into Greyscale and show image, print mean + variance
figure();
grayImg = rgb2gray(img);
imshow(grayImg);
title(['Greyscale Image'])
xlabel(['x pixels'])
ylabel(['y pixels'])
disp('Greyscale Image mean');
muGrayImg = mean(grayImg(:))
disp('Greyscale Image variance');
varGrayImg = var(double(grayImg(:)))

%Normalize the image histogram
figure();
normGrayImg = (double(grayImg) - muGrayImg)./sqrt(varGrayImg);
imshow(normGrayImg);
title(['Normalized Greyscale Image'])
xlabel(['x pixels'])
ylabel(['y pixels'])
disp('Normalized Greyscale Image mean');
muNormImg = mean(normGrayImg(:))
disp('Normalized Greyscale Image variance');
varNormImg = var(double(normGrayImg(:)))

%calculate and view RGB histogram
figure()
imhist(double(img(:,:,1))) %R
title(['Red Histogram'])
figure()
imhist(double(img(:,:,2))) %G
title(['Green Histogram'])
figure()
imhist(double(img(:,:,3))) %B
title(['Blue Histogram'])

%calculate and view Grayscale histogram
figure()
imhist(double(grayImg(:)))
title(['Grayscale Histogram'])

%calculate and view Normalized Grayscale histogram
figure()
imhist(double(normGrayImg(:)))
title(['Normalized Grayscale Histogram'])

%Graylevel to binary
figure();
binaryImg = im2bw(grayImg, 0.5);
imshow(binaryImg)
title(['Binary Image'])
xlabel(['x pixels'])
ylabel(['y pixels'])

%% Computational Photography. 
figure()
fogImg = imread('frogdefrog2.png');
imshow(fogImg);
title(['Frog Image'])
xlabel(['x pixels'])
ylabel(['y pixels'])

%  gamma correction
figure()
degammaFogImg = uint8(255.*(double(fogImg)./255.0).^(1/0.2));
imshow(degammaFogImg); %+25 here works a little bettwer
title(['de gamma Image'])
xlabel(['x pixels'])
ylabel(['y pixels'])

% Trying to normalize the image
figure()
degammaFogImg = double(degammaFogImg);
redImg = degammaFogImg(:,:,1);
greenImg = degammaFogImg(:,:,2);
blueImg = degammaFogImg(:,:,3);


k = 3;

muRedImg = mean(redImg(:))
varRedImg = var(redImg(:))
normRedImg = (redImg - muRedImg)./sqrt(varRedImg*k);

muGreenImg = mean(greenImg(:))
varGreenImg = var(greenImg(:))
normGreenImg = (greenImg - muGreenImg)./sqrt(varGreenImg*k);

muBlueImg = mean(blueImg(:))
varBlueImg = var(blueImg(:))
normBlueImg = (blueImg - muBlueImg)./sqrt(varBlueImg*k);

dehazedImg = degammaFogImg;
dehazedImg(:,:,1) = normRedImg;
dehazedImg(:,:,2) = normGreenImg;
dehazedImg(:,:,3) = normBlueImg;


imshow(dehazedImg);
title(['dehazed Image'])
xlabel(['x pixels'])
ylabel(['y pixels'])
