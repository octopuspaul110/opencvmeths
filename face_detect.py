import cv2 as cv
img = cv.imread('F7ti7B9WMAA03yA.jpeg')
#cv.imshow('Person',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('GRAY',gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')
faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor = 1.1 , minNeighbors = 10)
print(f'Number of faces found: {len(faces_rect)}')
for (x,y,w,h) in faces_rect:
    cv.rectangle(img,(x,y),(x +w,y + h),(0,255,0),thickness = 2)
cv.imshow('detected faces',img)

cv.waitKey()