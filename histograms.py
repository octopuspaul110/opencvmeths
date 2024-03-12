import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
img = cv.imread('WhatsApp Image 2023-10-04 at 21.18.08.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)
gray_hist = cv.calcHist([gray],[0],None,[256],[0,256])

plt.figure(figsize = (6,6))
plt.title('colour Histogram')
plt.xlabel('Bins')
plt.ylabel('#no of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])

colors = ('b','g','r',)
for i,col in enumerate(colors):
    hist = cv.calcHist([img],[i],None,[256],[0,256])
    print(cv.calcHist([img],[i],None,[256],[0,256]))
    plt.plot(hist,color = col)
    plt.xlim([0,256])
plt.show()
cv.waitKey()