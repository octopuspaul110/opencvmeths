import cv2 as cv
import numpy as np

img = cv.imread('WhatsApp Image 2023-10-04 at 21.18.08.jpg')
cv.imshow('image',img)

blank = np.zeros(img.shape[:2],dtype = 'uint8')

#masking
mask = cv.rectangle(blank,(img.shape[1]//2,img.shape[0]//2),(img.shape[1] // 2 + 100,img.shape[0] // 2 + 100),255,-1)
#cv.imshow('mask',mask)

masked_img = cv.bitwise_and(img,img,mask = mask)
#cv.imshow('masked im
# age',masked_img)


cv.waitKey()