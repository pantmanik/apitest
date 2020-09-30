import cv2
import numpy as np

def fin_col(img):
	img=cv2.resize(img,(100,100))
	cols,freq=np.unique(img,return_counts=True)
	ind=np.argsort(freq)[::-1]
	return cols[ind],freq[ind]

img=cv2.imread("kppl_logo.png")
cols,freq=fin_col(img)
print(cols[0])
print(freq[0])