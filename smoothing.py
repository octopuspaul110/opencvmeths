import cv2 as cv

img = cv.imread('WhatsApp Image 2023-10-04 at 21.18.08.jpg')
cv.imshow('normal image',img)

#averaging
average = cv.blur(img,(3,3))
cv.imshow('average blur',average)

#gaussian blur
gaussblur = cv.GaussianBlur(img,(9,9),0)
cv.imshow('Gaussian blur',gaussblur)

#Median Blur
median = cv.medianBlur(img,3)
cv.imshow('median blur',median)

#Bilateral
bilateral = cv.bilateralFilter(img,30,35,25)
cv.imshow('bilateral',bilateral)


cv.waitKey(0)