import cv2
import numpy as np

# img = cv2.imread('mypic.jpg',cv2.IMREAD_COLOR)
# px=img[55,55]
# px=[255,255,255]
# #change region to black
# img[100:150,100:150]=[0,0,0]
#
# #copy region to the top
# watch_face=img[37:111,107:194]
# img[0:74,0:87]=watch_face
#
# cv2.imshow('img',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# #read img and draw lines labels
# img = cv2.imread('mypic.jpg',cv2.IMREAD_COLOR)
#
# cv2.line(img,(0,0),(150,150),(225,225,225),15)
# cv2.rectangle(img,(15,25),(200,150),(0,225,0),5)
#
# pts=np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)
# cv2.polylines(img,[pts],True,(0,255,255),5)
#
# font=cv2.FONT_HERSHEY_SIMPLEX
# cv2.putText(img,'OpenCV',(0,130),font,5,(200,255,255),5,cv2.LINE_AA)
# cv2.imshow('mypic.jpg',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# #camera
detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
# #save to video
# fourcc=cv2.VideoWriter_fourcc(*'XVID')
# out=cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))

while True:
    ret,img=cap.read()
    gray =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # size, likelyhood
    faces=detector.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        # draw rectangle around faces (x,y) start point w=width h=high ,color , thickness
        cv2.rectangle(img, (x,y),(x+w,y+h),(255,0,0),2)
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=img[y:y+h,x:x+w]

    cv2.imshow('img',img)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

# create your own cascade
cap.release()
cv2.destroyAllWindows()

