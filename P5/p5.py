#code reference: http://code.google.com/p/pymeanshift/wiki/Examples

import cv2
import numpy as np
import pymeanshift as pms


def data(p, l):
	#p = pixel label value
	#l = labelthat we are cheking against
	#potts model:
	c = 3  #the penalty for missing the pixel label.
	if (p-l != 0):
		return c
	return 0

def smoothness(fp, fq):
	#fp = current pixel label
	#fq = label right next to us
	#potts model:
	c = 3  #the penalty for missing the pixel label.
	if (fp-fq != 0):
		return c
	return 0
def allEnergy(fp, segmented):
	energy = 0
	energyu = 0
	energyd = 0
	energyl = 0
	energyr = 0
	if (fp[0]>0 and fp[0]<len(segmented[1])-1):
		if (fp[1]>0 and fp[1]<len(segmented)-1):
			energy += data(segmented[fp[0]][fp[1]],segmented[fp[0]][fp[1]])
			energyu = smoothness(segmented[fp[0]][fp[1]], segmented[fp[0]-1][fp[1]])  #towards up
			energyd = smoothness(segmented[fp[0]][fp[1]], segmented[fp[0]+1][fp[1]])	 #towards down
			energyl = smoothness(segmented[fp[0]][fp[1]], segmented[fp[0]][fp[1]-1])  #towards left
			energyr = smoothness(segmented[fp[0]][fp[1]], segmented[fp[0]][fp[1]+1])  #towards right
	e = [energyu,energyd,energyr,energyl]
	pos = e.index(max(e));
	energy += energyu+energyd+energyr+energyl
	return (energy, pos)

original_image = cv2.imread("AnnieYukiTim.bmp")
original_image = cv2.resize(original_image, None, fx = 0.4, fy = 0.4, interpolation = cv2.INTER_CUBIC)

(segmented_image, labels_image, number_regions) = pms.segment(original_image, spatial_radius=10,range_radius=21, min_density=7000)
#(segmented_image, labels_image, number_regions) = pms.segment(original_image, spatial_radius=10,range_radius=21, min_density=1000)
segmented_image = cv2.cvtColor(segmented_image, cv2.COLOR_BGR2GRAY)

centers = [[0,0, 0], [0,0,0], [0,0,0], [0,0,0]]
for i in range(0, len(labels_image)-1):
	for j in range(0, len(labels_image[1])-1):
		if (labels_image[i][j] == 0):
			centers[0][0] += j
			centers[0][1] += i
			centers[0][2] +=1
		if (labels_image[i][j] == 1):
			centers[1][0] += j
			centers[1][1] += i
			centers[1][2] +=1
		if (labels_image[i][j] == 2):
			centers[2][0] += j
			centers[2][1] += i
			centers[2][2] +=1
		if (labels_image[i][j] == 3):
			centers[3][0] += j
			centers[3][1] += i
			centers[3][2] +=1
cv2.circle(original_image, (int(centers[0][0]/centers[0][2]),int(centers[0][1]/centers[0][2])), 5, (0,0,255), 5)
cv2.circle(original_image, (int(centers[1][0]/centers[1][2]),int(centers[1][1]/centers[1][2])), 5, (0,255,255), 5)
cv2.circle(original_image, (int(centers[2][0]/centers[2][2]),int(centers[2][1]/centers[2][2])), 5, (0,255,0), 5)
cv2.circle(original_image, (int(centers[3][0]/centers[3][2]),int(centers[3][1]/centers[3][2])), 5, (255,0,0), 5)

print("number of labels " + str(number_regions))
cv2.imshow('original Image', original_image)
cv2.imshow('segmented Image', segmented_image)

#belief propogation: Message passing
termination = 10
changedPix = 0
for k in range(0,termination):
	for i in range(0, len(segmented_image)-1):
		for j in range(0, len(segmented_image[1])-1):
			energy = allEnergy([i,j], segmented_image)
			if (energy[0] != 0):
				if (energy[1] == 0):
					segmented_image[i,j] = segmented_image[i-1,j]
				if (energy[1] == 1):
					segmented_image[i,j] = segmented_image[i+1,j]
				if (energy[1] == 2):
					segmented_image[i,j] = segmented_image[i,j-1]
				if (energy[1] == 3):
					segmented_image[i,j] = segmented_image[i,j+1]
				changedPix+=1
	cv2.imshow('Segmented Image iteration: '+str(k), segmented_image)


#performance evalieation:
print("Performance evaluation: Number of picels changed = "+str(changedPix))

cv2.waitKey(0)
cv2.destroyAllWindows()