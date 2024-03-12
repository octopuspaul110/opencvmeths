import cv2 as cv
import numpy as np

blank = np.zeros((400,400),dtype='uint8')
rectangle = cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
circle = cv.circle(blank.copy(),(200,200),200,255,-1)

cv.imshow('rect',rectangle)
cv.imshow('circ',circle)

#bitwise And -> intersecting regions
bitwise_and = cv.bitwise_and(rectangle,circle)
cv.imshow('bitwise_and',bitwise_and)

#bitwise or ->non-intersecting and intersecting regions
bitwise_or = cv.bitwise_or(rectangle,circle)
cv.imshow('bitwise_or',bitwise_or)

#bitwise XOR ->non-intersecting regions
bitwise_xor = cv.bitwise_xor(rectangle,circle)
cv.imshow('bitwise xor',bitwise_xor)

#bitwise not
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow('rect not',bitwise_not)

#bitwise not
bitwise_not = cv.bitwise_not(circle)
cv.imshow('rect not',bitwise_not)

cv.waitKey()