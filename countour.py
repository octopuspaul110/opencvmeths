import cv2 
import numpy as np

img = cv2.imread('D:\computer vision\opencv\WhatsApp Image 2023-10-04 at 21.18.08.jpg')
#cv2.imshow('tobi',img)
blank = np.zeros(img.shape,dtype='uint8')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#cv2.imshow('grayimg',gray)

#blur = cv2.GaussianBlur(gray,(5,5),cv2.BORDER_DEFAULT)
#cv2.imshow('Blur',blur)

#canny = cv2.Canny(img,125,175)
#cv2.imshow('canny edges',canny)

ret,thresh = cv2.threshold(gray,125,255,cv2.THRESH_BINARY)
cv2.imshow('thresh',thresh)
contours,hierarchies = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
print(f"{len(contours)} contous found!")
cv2.drawContours(blank,contours,-1,(0,0,255),1)
cv2.imshow('drawcontour',blank)

cv2.waitKey(0)