% 1. Apply Otsu threshold method to 3 (three) different  B/W  images using (a) textbook algorithm;
% and (b) recursion equations. Display outputs and compare timing for both methods.
% 2. Expand on Otsu’ binarization method to 3 (three) different B/W images consisting of several non-overlapping
% objects of almost constant but different gray-level.

% Report includes (a) flow-chart of (input-output) stepwise methods used;(b1) histograms for input B/W images;
% (b2) input-output displays; (c) timing; and (d) MATLAB code.

%Otsurec written by: Alceu Costa: 
%http://www.mathworks.com/matlabcentral/fileexchange/43410-em-mpm-image-segmentation-algorithm/content/otsurec.m
%image reference 1st: http://bobbycorpus.files.wordpress.com/2012/01/sample_gray_levels.png
%image reference 2nd: http://bobbycorpus.files.wordpress.com/2012/01/levels_of_gray.png
%image reference 3rd: http://scien.stanford.edu/pages/labsite/2000/psych221/projects/00/trek/CameraGamma.html

M1 = imread('G1.JPG');
M2 = imread('G2.JPG');
M3 = imread('G3.JPG');
M1 = rgb2gray(M1);
M2 = rgb2gray(M2);
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
subplot(3,3,1)
imshow(M1)
subplot(3,3,4)
imshow(M2)
subplot(3,3,7)
imshow(M3)
subplot(3,3,2)
imhist(M1);
subplot(3,3,5)
imhist(M2);
subplot(3,3,8)
imhist(M3);
subplot(3,3,3)
imshow(BW1);
subplot(3,3,6)
imshow(BW2);
subplot(3,3,9)
imshow(BW3);


