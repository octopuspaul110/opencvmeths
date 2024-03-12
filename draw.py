import cv2
import numpy as np

blank = np.zeros((500,500,3),dtype='uint8')
cv2.imshow('Blank',blank)

blank[200:300,300:400]=0,0,255
cv2.imshow('path',blank)
#img = cv2.imread("D:\computer vision\opencv\WhatsApp Video 2023-11-19 at 11.04.44_aea90710.mp4")
#cv2.imshow('image',img)

#draw a rectangle
cv2.rectangle(blank,(0,0),(blank.shape[1] // 2,blank.shape[0] // 2),(0,255,0),thickness = cv2.FILLED)
cv2.circle(blank,(blank.shape[1] // 2,blank.shape[0] // 2),40,(0,0,255),thickness = cv2.FILLED)
cv2.line(blank,(100 ,250),(300,400),(255,255,255),thickness = cv2.FILLED)
cv2.imshow('rect',blank)
cv2.waitKey(0)