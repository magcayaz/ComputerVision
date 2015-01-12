# (b) write and run code that {gets RGB (see attached or choose another RGB) image and display / print the image,
# transform the RGB image to gray scale, find out the mean and variance for both RGB and gray-scale images,
# normalize the gray-scale image using min and max gray values(e.g.,  range), calculate, display, and
# print  the histogram for both RGB and gray value images}, and transform the gray level image to a binary image}
# (c) Computational Photography (using D01-slide 23 <original vs. fog added>: (c1) using Matlab; and (c2)using  OpenCV
# find the best mix of gamma correction and histogram equalization to defog images. Towards that end define some
# measure of image quality (e.g., high frequency contents) to seek for best image quality.

import cv2
import numpy as np
from matplotlib import pyplot as plt 

#load image
img = cv2.imread('test.jpg')

#show original Image and pring mean + variance
cv2.imshow('Original Image', img)
print 'Original Image mean:', img.mean()
print 'Original Image varianca:', img.var()

#transform the image into Greyscale and show image, print mean + variance
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Greyscale Image', grayImg)
print 'Grayscale Image mean:', grayImg.mean()
print 'Grayscale Image varianca:', grayImg.var()

#Normalize the image histogram
normImg = cv2.equalizeHist(grayImg)
cv2.imshow('Normalized Greyscale Image', normImg)
histNormImg = cv2.calcHist([normImg],[0], None, [256], [0,256])
plt.plot(histNormImg)
plt.xlabel('Normalized Greyscale Image Histogram')
plt.show()

#calculate and view RGB histogram
Red = img[:,:,2]
Green = img[:,:,1]
Blue = img[:,:,0]

histImg = cv2.calcHist([Red],[0], None, [256], [0,256])
plt.plot(histImg, 'r')
plt.xlabel('Red histogram')
plt.show()

histImg = cv2.calcHist([Green],[0], None, [256], [0,256])
plt.plot(histImg, 'g')
plt.xlabel('Green histogram')
plt.show()

histImg = cv2.calcHist([Blue],[0], None, [256], [0,256])
plt.plot(histImg, 'b')
plt.xlabel('Blue histogram')
plt.show()

#calculate and view grayScale histogram
histGrayImg = cv2.calcHist([grayImg],[0], None, [256], [0,256])
plt.plot(histGrayImg)
plt.xlabel('Grayscale histogram')
plt.show()

#Graylevel to binary
binaryImg = cv2.inRange(grayImg,np.array(128), np.array(255) )
cv2.imshow('Binary Image', binaryImg)

#Computational Photography:

#load image
fogImg = cv2.imread('frogdefrog2.png')
cv2.imshow('Foggy Image', fogImg)
degammaFogImg = np.divide((fogImg),255.0)
degammaFogImg = np.multiply(degammaFogImg, 255)
degammaFogImg = np.power(degammaFogImg,(1/0.3))
cv2.imshow('dehaze Image', degammaFogImg)

cv2.waitKey(0)
cv2.destroyAllWindows()