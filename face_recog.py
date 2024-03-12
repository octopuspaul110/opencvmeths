import numpy as np
import cv2 as cv

haar_cascade = cv.CascadeClassifier('haar_face.xml')

people = ['klopp','salah','trent','vdd']
#features = np.load('features.npy')
#labels = np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

img = cv.imread(r'val/F-Geq3eXQAAP7ci.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('person',gray)

faces_rect = haar_cascade.detectMultiScale(gray,1.1,4)
for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y + h,x:x+h]
    label,confidence = face_recognizer.predict(faces_roi)

    print(f'label = {people[label]} with confidence of  {confidence}')
    cv.putText(img,str(people[label]),(100,100),cv.FONT_HERSHEY_COMPLEX,3.0,(0,255,0),thickness = 2)
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness = 2)
cv.imshow('detected face',img)
cv.waitKey(0)

