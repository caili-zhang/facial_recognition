# -*- coding: utf-8 -*-
import cv2
import os

cap = cv2.VideoCapture(0)
faceDetector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

if not os.path.exists('dataSet'):
    os.makedirs('dataSet')

id,name=input('スペースで区切って，IDと名前を入力してください: ').split()

picnumber =0

while True:
    ret,img=cap.read()
    gray =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # size, likelyhood
    faces=faceDetector.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        # draw rectangle around faces (x,y) start point w=width h=high ,color , thickness
        cv2.rectangle(img, (x,y),(x+w,y+h),(255,0,0),2)
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=img[y:y+h,x:x+w]

        cv2.imwrite("dataSet/User."+str(id)+"."+name+"."+str(picnumber)+".jpg",gray[y:y+h,x:x+w])
        picnumber+=1
        cv2.waitKey(1000)

    cv2.imshow('img',img)
                        #take 20 pics
    if cv2.waitKey(1) & picnumber==20:
        break

# create your own cascade


cap.release()
cv2.destroyAllWindows()
