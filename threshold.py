import cv2 as cv
img = cv.imread('D:\computer vision\opencv\WhatsApp Image 2023-10-04 at 21.18.08.jpg')
cv.imshow('img',img)
grey = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#simple thresholding
threhold,thresh = cv.threshold(grey, 100,255,cv.THRESH_BINARY)
cv.imshow('thresh',thresh)

threhold,thresh_inv = cv.threshold(grey, 100,255,cv.THRESH_BINARY_INV)
cv.imshow('inverse thresh inverse',thresh_inv)

#Adaptive Thresholding
adaptive_thresh = cv.adaptiveThreshold(grey,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY_INV,3,3)
cv.imshow('adaptive_thresh',adaptive_thresh)

cv.waitKey()