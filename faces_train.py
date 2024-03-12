import os
import numpy as np
import cv2 as cv

people = ['klopp','salah','trent','vdd']
dir_images = 'D:/computer vision/opencv/faces/'
features = []
labels = []

haar_cascade = cv.CascadeClassifier('haar_face.xml')

def create_train():
    for person in people:
        path = os.path.join(dir_images,person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path,img)
            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array,cv.COLOR_BGR2GRAY)
            faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor = 1.1,minNeighbors = 20)
            for (x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h,x:x+w]
                features.append(faces_roi)
                labels.append(label)
create_train()
#print(f'Lenght of features = {len(features)}')
#print(f'Lenght of labels = {len(labels)}')
print('Training done------')
features = np.array(features,dtype='object')
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.train(features,labels)
face_recognizer.save('face_trained.yml')
np.save(f'features.npy',features)
np.save('labels.npy',labels)