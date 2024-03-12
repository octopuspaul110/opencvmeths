import cv2
import numpy as np

img = cv2.imread("D:\computer vision\opencv\WhatsApp Image 2023-10-04 at 21.18.08.jpg")
#cv2.imshow("Tobi",img)

#translation(moving)
def translate(img,x,y):
    #performs shifting of images
    #-x --> Left
    #-y --> Up
    #x --> Right
    #y --> Down
    transMat = np.float32(([1,0,x],[0,1,y]))
    dimension = (img.shape[1],img.shape[0])
    return cv2.warpAffine(img,transMat,dimension)
translate_img = translate(img,200,- 300)
cv2.imshow('translated',translate_img)

#rotation
def Rotate(img,angle,rotation_point = None):
    (height,width) = img.shape[:2]
    if rotation_point is None:
        rotation_point = (width // 2,height//2) #rotate around center
    rotMat = cv2.getRotationMatrix2D(rotation_point,angle,1.0)
    dimensions = (width,height)
    return cv2.warpAffine(img,rotMat,dimensions)
rotated_img = Rotate(img,-90)
cv2.imshow('rotated',rotated_img)

#resizing
resized_img = cv2.resize(img,(500,500),interpolation = cv2.INTER_CUBIC)
cv2.imshow('resized',resized_img)

#flipping
flip_img = cv2.flip(img,0)
cv2.imshow('flip',flip_img)

#cropping
cropped_img = img[200:500,400:600]
cv2.imshow('cropped',cropped_img)
cv2.waitKey()