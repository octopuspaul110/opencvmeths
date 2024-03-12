import cv2

img = cv2.imread('D:\computer vision\opencv\WhatsApp Image 2023-10-04 at 21.18.08.jpg')
cv2.imshow('tobi',img)

def rescaleFrame(frame,scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)
    return cv2.resize(frame,dimensions,interpolation = cv2.INTER_AREA)
capture = cv2.VideoCapture("D:\computer vision\opencv\WhatsApp Video 2023-11-19 at 11.04.44_aea90710.mp4")
while True:
    isTrue,frame = capture.read()
    frame_resized = rescaleFrame(frame)
    cv2.imshow("Video",frame)
    cv2.imshow("Video Resized",frame_resized)
    if cv2.waitKey(20) and 0xff==ord('d'):
        break