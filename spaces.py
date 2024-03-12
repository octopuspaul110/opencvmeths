import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("WhatsApp Image 2023-10-04 at 21.18.08.jpg")
#cv.imshow('real image',img)

#plt.imshow(img[:,:,::-1])
#plt.show()

#gray
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('GRAY image',gray)

#bgr to hsv
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('HSV image',hsv)

#bgr to lab
lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('LAB image',lab)

#rgb to bgr
rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('rgb image',rgb)

#HSV to BGR
hsv_bgr = cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
cv.imshow('hsv_bgr image',hsv_bgr)

#lab to BGR
lab_bgr = cv.cvtColor(lab,cv.COLOR_LAB2BGR)
cv.imshow('lab_bgr image',lab_bgr)

cv.waitKey(0)