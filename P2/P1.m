

img1 = imread('img1.png');
%reference: http://stackoverflow.com/questions/25469203/how-can-i-improve-my-sobel-operator-edge-detection
grayImg = rgb2gray(img1);
kernelx = [-1, 0, 1;
		   -2, 0, 2;
		   -1, 0, 1];
kernely = [1, 2, 1;
		   0, 0, 0;
		   -1, -2, -1];

figure();
imshow(grayImg)
img1 = imfilter(grayImg, kernelx);
img2 = imfilter(grayImg, kernely);

%adding filtered image in x and y
img = img1+img2./2; 
figure();
imshow(img)

%directional derivative 45 degrees
kerneldir = [2, 1, 0;
		     1, 0, -1;
		     0, -1, -2];
img3 = imfilter(grayImg, kerneldir);

imgFinal = (img3+img1+img2)./2;

figure();
imshow(imgFinal)

% without directional we miss some of the edges but with directional we get some much more noise. 
