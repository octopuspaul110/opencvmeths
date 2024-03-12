import cv2 

#read in an image
#img = cv2.imread("D:\computer vision\opencv\WhatsApp Image 2023-10-04 at 21.18.08.jpg")
#cv2.imshow('image',img)


#read in a video
capture = cv2.VideoCapture("D:\computer vision\opencv\WhatsApp Video 2023-11-19 at 11.04.44_aea90710.mp4")
i = 0
while True:
    i += 1
    isTrue,frame = capture.read()
    cv2.imwrite(f'frame{i}.png',frame)
    cv2.imshow('Video',frame)
    if cv2.waitKey(20) and 0xff==ord('d'):
        break

capture.release()
cv2.destroyAllWindows()    
#cv2.waitKey(0)