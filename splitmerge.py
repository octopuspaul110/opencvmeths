import cv2 as cv
import numpy as np
img = cv.imread("D:\computer vision\opencv\WhatsApp Image 2023-10-04 at 21.18.08.jpg")
cv.imshow('image',img)

blank = np.zeros(img.shape[:2],dtype='uint8')

b,g,r = cv.split(img)

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('Blue',blue)
cv.imshow('Green',green)
cv.imshow('red',red)

print(img.shape)
print(g.shape)
print(b.shape)
print(r.shape)
print('shape',img.shape[:2])

merged_img = cv.merge([b,g,r])
cv.imshow('Merged image',merged_img)
print(f'merged image shape {merged_img.shape}')
cv.waitKey()
