import cv2
img = cv2.imread("D:\computer vision\opencv\WhatsApp Image 2023-10-04 at 21.18.08.jpg")
cv2.imshow('image',img)
#grayscale an image
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('gray',gray)
#bluring
blur = cv2.GaussianBlur(img,(5,5),cv2.BORDER_DEFAULT)
cv2.imshow('blur',blur)
#edge casscading
canny = cv2.Canny(img,125,175)
cv2.imshow('canny',canny)
#image dilation
dilated_img = cv2.dilate(canny,(10,10),iterations = 1)
cv2.imshow('dilated',dilated_img)
#eroding
eroded_img = cv2.erode(dilated_img,(3,3),iterations = 1)
cv2.imshow('eroded',eroded_img)
#resizing
resized_img = cv2.resize(img,(500,500),interpolation = cv2.INTER_AREA)
cv2.imshow('resized',resized_img)
#cropping
cropped_img = img[50:200,200:400]
cv2.imshow('cropped',cropped_img)
cv2.waitKey(0)