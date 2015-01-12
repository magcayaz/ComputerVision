#Reference for plotting and everything else: http://docs.opencv.org/trunk/doc/py_tutorials/py_imgproc/py_transforms/py_fourier_transform/py_fourier_transform.html
#Array question reference:http://stackoverflow.com/questions/13157961/2d-array-of-zeros
# Homework#3 due October 21
# MANMADE vs. NATURE TEXTURE CLASSIFICATION
# http://ccv.wordpress.fos.auckland.ac.nz/data/textures/
# 1. Data Collection (5 - 10 images of same size for each class)
# 2. Method: Use FT Rings and Wedges Energy
# 3. Performance Evaluation (Confusion Matrix, ROC, ..)


import cv2
import numpy as np
from matplotlib import pyplot as plt 
import math
from sklearn import svm

#load image
M = []  #Manmade pictures
N = []	#Non manmade pictures
Mdft = []   #Manmade pictures in FT
Ndft = []	#Non manmade pictures in FT

for i in range(1,11):
	M.append(cv2.equalizeHist(cv2.imread('M'+str(i)+'.JPG',0)[0:480,0:640]))
for i in range(1,11):
	N.append(cv2.equalizeHist(cv2.imread('N'+str(i)+'.jpg',0)[0:480,0:640]))

for i in range(0,10):
	dft = np.fft.fft2(M[i])
	shftDft = np.fft.fftshift(dft)
	magnitude = 20*np.log(np.abs(shftDft))
	Mdft.append(magnitude)
for i in range(0,10):
	dft = np.fft.fft2(N[i])
	shftDft = np.fft.fftshift(dft)
	magnitude = 20*np.log(np.abs(shftDft))
	Ndft.append(magnitude)

for i in range(0,10):
	plt.subplot(221),plt.imshow(N[i], cmap = 'gray')
	plt.title('Non Man Made Original'), plt.xticks([]), plt.yticks([])
	plt.subplot(222),plt.imshow(Ndft[i], cmap = 'gray')
	plt.title('Non Man Made FT'), plt.xticks([]), plt.yticks([])
	plt.subplot(223),plt.imshow(M[i], cmap = 'gray')
	plt.title('Man Made Original'), plt.xticks([]), plt.yticks([])
	plt.subplot(224),plt.imshow(Mdft[i], cmap = 'gray')
	plt.title('Man Made FT'), plt.xticks([]), plt.yticks([])
	plt.show()


trainSize = 6
wedgeSize = (math.pi/6)
numWedge = (math.pi*2)/wedgeSize
sumWedge = [[0]*int(numWedge) for _ in xrange(20) ]
numPixWedge = (M[0].shape[0]*M[0].shape[1])/numWedge
for i in range(0,10):
	for x in range(0,640):
		for y in range(0,480):
			xind = x - 640/2
			yind = y - 480/2
			rad = math.atan2(yind,xind)
			if rad <0 :
				rad = 2*math.pi - math.fabs(rad)
			if rad < wedgeSize:
				sumWedge[i][0]+= (Mdft[i][y,x]/numPixWedge)
				sumWedge[i+10][0]+= (Ndft[i][y,x]/numPixWedge)
			if wedgeSize<= rad < 2*wedgeSize:
				sumWedge[i][1]+= (Mdft[i][y,x]/numPixWedge)
				sumWedge[i+10][1]+= (Ndft[i][y,x]/numPixWedge)
			if 2*wedgeSize<= rad < 3*wedgeSize:
				sumWedge[i][2]+= (Mdft[i][y,x]/numPixWedge)
				sumWedge[i+10][2]+= (Ndft[i][y,x]/numPixWedge)
			if 3*wedgeSize<= rad < 4*wedgeSize:
				sumWedge[i][3]+= (Mdft[i][y,x]/numPixWedge)
				sumWedge[i+10][3]+= (Ndft[i][y,x]/numPixWedge)
			if 4*wedgeSize<= rad < 5*wedgeSize:
				sumWedge[i][4]+= (Mdft[i][y,x]/numPixWedge)
				sumWedge[i+10][4]+= (Ndft[i][y,x]/numPixWedge)
			if 5*wedgeSize<= rad < 6*wedgeSize:
				sumWedge[i][5]+= (Mdft[i][y,x]/numPixWedge)
				sumWedge[i+10][5]+= (Ndft[i][y,x]/numPixWedge)
			if 6*wedgeSize<= rad < 7*wedgeSize:
				sumWedge[i][6]+= (Mdft[i][y,x]/numPixWedge)
				sumWedge[i+10][6]+= (Ndft[i][y,x]/numPixWedge)
			if 7*wedgeSize<= rad < 8*wedgeSize:
				sumWedge[i][7]+= (Mdft[i][y,x]/numPixWedge)
				sumWedge[i+10][7]+= (Ndft[i][y,x]/numPixWedge)
			if 8*wedgeSize<= rad < 9*wedgeSize:
				sumWedge[i][8]+= (Mdft[i][y,x]/numPixWedge)
				sumWedge[i+10][8]+= (Ndft[i][y,x]/numPixWedge)
			if 9*wedgeSize<= rad < 10*wedgeSize:
				sumWedge[i][9]+= (Mdft[i][y,x]/numPixWedge)
				sumWedge[i+10][9]+= (Ndft[i][y,x]/numPixWedge)
			if 10*wedgeSize<= rad < 11*wedgeSize:
				sumWedge[i][10]+= (Mdft[i][y,x]/numPixWedge)
				sumWedge[i+10][10]+= (Ndft[i][y,x]/numPixWedge)
			if 11*wedgeSize<= rad < 12*wedgeSize:
				sumWedge[i][11]+= (Mdft[i][y,x]/numPixWedge)
				sumWedge[i+10][11]+= (Ndft[i][y,x]/numPixWedge)
Predict = []
X = []
for i in range(0,6):
	X.append(sumWedge[i])
for i in range(0,6):
	X.append(sumWedge[i+10])
for i in range(6,10):
	Predict.append(sumWedge[i])
for i in range(6,10):
	Predict.append(sumWedge[i+10])
y = ['Man-Made', 'Man-Made', 'Man-Made', 'Man-Made', 'Man-Made', 'Man-Made',
	'Non Man-Made', 'Non Man-Made', 'Non Man-Made', 'Non Man-Made', 'Non Man-Made', 'Non Man-Made']
clf = svm.SVC()
clf.fit(X,y)

for i in Predict:
	print clf.predict([i])

#the following code was completely copied and pasted here for debugging purposes Reference 1
for i in range(6,10):
	plt.subplot(221),plt.imshow(N[i], cmap = 'gray')
	plt.title('Original'), plt.xticks([]), plt.yticks([])
	plt.subplot(222),plt.imshow(Ndft[i], cmap = 'gray')
	plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
	plt.subplot(223),plt.imshow(M[i], cmap = 'gray')
	plt.title('Original'), plt.xticks([]), plt.yticks([])
	plt.subplot(224),plt.imshow(Mdft[i], cmap = 'gray')
	plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
	plt.show()


# dft = cv2.dft(np.float32(M[i]), flags = cv2.DFT_COMPLEX_OUTPUT)
# shftDft = np.fft.fftshift(dft)
# magnitude = 20*np.log(cv2.magnitude(shftDft[:,:,0],shftDft[:,:,1]))
# Mdft.append(magnitude)





cv2.waitKey(0)
cv2.destroyAllWindows()