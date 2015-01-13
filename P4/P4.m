% 1. Apply Otsu threshold method to 3 (three) different  B/W  images using (a) textbook algorithm;
% and (b) recursion equations. Display outputs and compare timing for both methods.
% 2. Expand on Otsu’ binarization method to 3 (three) different B/W images consisting of several non-overlapping
% objects of almost constant but different gray-level.

% Report includes (a) flow-chart of (input-output) stepwise methods used;(b1) histograms for input B/W images;
% (b2) input-output displays; (c) timing; and (d) MATLAB code.

%Otsurec written by: Alceu Costa: 
%http://www.mathworks.com/matlabcentral/fileexchange/43410-em-mpm-image-segmentation-algorithm/content/otsurec.m
%image reference 2nd: http://www.usaflagsupply.com/
M1 = imread('M1.JPG');
M2 = imread('M2.JPG');
M3 = imread('M3.png');
M1 = rgb2gray(M1);
M2 = rgb2gray(M2);
M3 = rgb2gray(M3);
tic;
M1l = graythresh(M1);
M2l = graythresh(M2);
M3l = graythresh(M3);
otsutime = toc
tic
M1lr = otsurec(M1, 1);
M2lr = otsurec(M2, 1);
M3lr = otsurec(M3, 1);
rectime = toc
BW1 = im2bw(M1, M1l);
BW2 = im2bw(M2, M2l);
BW3 = im2bw(M3, M3l);
BW1r = im2bw(M1, M1lr);
BW2r = im2bw(M2, M2lr);
BW3r = im2bw(M3, M3lr);
figure();
subplot(3,4,1)
imshow(M1)
subplot(3,4,5)
imshow(M2)
subplot(3,4,9)
imshow(M3)
subplot(3,4,2)
imhist(M1);
subplot(3,4,6)
imhist(M2);
subplot(3,4,10)
imhist(M3);
subplot(3,4,3)
imshow(BW1);
subplot(3,4,7)
imshow(BW2);
subplot(3,4,11)
imshow(BW3);
subplot(3,4,4)
imshow(BW1r);
subplot(3,4,8)
imshow(BW2r);
subplot(3,4,12)
imshow(BW3r);

