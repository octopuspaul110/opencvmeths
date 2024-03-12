import cv2 as cv
import numpy as np
img = cv.imread("WhatsApp Image 2023-10-04 at 21.18.08.jpg")
cv.imshow(' ',img)
#laplace
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#cv.imshow('gray',gray)

lap = cv.Laplacian(gray,cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('lapplacian',lap)

#sobel
sobelx = cv.Sobel(gray,cv.CV_64F,1,0)
sobely = cv.Sobel(gray,cv.CV_64F,0,1)
combinedsobel = cv.bitwise_or(sobelx,sobely)
cv.imshow('combinesobel',combinedsobel)

canny = cv.Canny(gray,150,157)
cv.imshow('canny',canny)

cv.imshow('sobel_X',sobelx)
cv.imshow('sobel_y',sobely)
cv.waitKey()