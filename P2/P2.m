

img = imread('img1.png');
boxFilter= [1, 1, 1;
		   1, 1, 1;
		   1, 1, 1];
boxFilter = boxFilter./9;
gausImg = img;
figure();
imshow(img)

%run a filter
for i = 1:30
	img = imfilter(img, boxFilter);
end
%plot final image;
figure();
imshow(img)

% see how it works with a gaussian filter
boxFilter= [1, 1, 1;
		   1, 4, 1;
		   1, 1, 1];
boxFilter = boxFilter./(sum(sum(boxFilter)));	 

img = imfilter(gausImg, boxFilter);
%plot final Gauss image;
figure();
imshow(img)


%Gauss filter, instead of filtering everything with the same value like the box filter, 
%	filters the outer values more than the values that are closer. 

% radius of a gauss filter is 2k+1 sized. 
