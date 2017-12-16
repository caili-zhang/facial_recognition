# -*- coding: utf-8 -*-
import cv2
from speech_api import jatts
import time
detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, 60)           # カメラFPSを60FPSに設定
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280) # カメラ画像の横幅を1280に設定
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720) # カメラ画像の縦幅を720に設定




recognizer =cv2.face.LBPHFaceRecognizer_create()

recognizer.read("trainingData.yml")

print(str(recognizer))

id=-1
font=cv2.FONT_HERSHEY_SIMPLEX
flag=False

while True:
    ret,img=cap.read()
    gray =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # size, likelyhood
    faces=detector.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        # draw rectangle around faces (x,y) start point w=width h=high ,color , thickness
        cv2.rectangle(img, (x,y),(x+w,y+h),(255,0,0),2)

        id,conf =recognizer.predict(gray[y:y+h,x:x+w])
        if(conf>90):
            username="Unknown"
        else:
            if(id==1):
                username="chou"

            elif(id==2):
                username="kitajima"
            elif(id==3):
                username="Uwano"
            elif(id==-1):
                username="Unknown"

        if( (username !="Unknown") & flag==False):
            flag=True
            jatts.jatts("こんにちわ"+username+"さん")

        cv2.putText(img,"User:"+username,(x,y-10),font,1,(0,255,0),3)
        cv2.putText(img, "Conf:" + str(conf), (x, y - 50), font, 1, (0, 255, 0), 3)



    cv2.imshow('img',img)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()