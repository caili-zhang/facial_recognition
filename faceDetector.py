# -*- coding: utf-8 -*-
import cv2
from speech_api.jatts import jatts
import time
#import multiprocessing as mp
import threading
import fps

# #　オブジェクト生成
# speaker = jatts('あああああ')
# #話す
# speaker.speak()

## logic
## subscriber = speaker
## Publisher = detector ,が顔を認識したら、Speakerに名前を送る

## 解決した問題：発音のとき画面が止まった、threading なんとかする

class Speaker:
    def __init__(self,name='Speaker'):
        self.name=name

    def update(self,message):
        speaker = jatts(message)
        speaker.speak()

        print(threading.current_thread().getName()+" in speaker:"+str(time.time()))

class FaceDetector:
    gFrameRate = fps.FrameRate()
    def __init__(self):

        self.subscribers=dict()
        self.detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        self.cap = cv2.VideoCapture(0)

        self.cap.set(cv2.CAP_PROP_FPS, 1)  # カメラFPSを60FPSに設定
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 720)  # カメラ画像の横幅を1280に設定
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)  # カメラ画像の縦幅を720に設定

        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.recognizer.read("trainingData.yml")
        # 各種の初期化
        self.id = -1
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.flag = False
        self.detect_threshold = 10
        self.username = ""
        self.startTime = time.time()
        subthread = threading.Thread(target=self.subThread,name='send name')
        subthread.daemon = True  # Daemonize thread
        subthread.start()  # Start the execution
    def update(self):
        # 顔認識のメインロジック
        username=""
        while True:
            ret, self.img = self.cap.read()
            fps = self.gFrameRate.get()
            gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
            # size, likelyhood
            faces = self.detector.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                # draw rectangle around faces (x,y) start point w=width h=high ,color , thickness
                # VIEW の部分
                cv2.rectangle(self.img, (x, y), (x + w, y + h), (255, 0, 0), 2)

                id, conf = self.recognizer.predict(gray[y:y + h, x:x + w])
                if (conf > 90):
                    username = "Unknown"
                else:
                    if (id == 1):
                        username = "chou"

                    elif (id == 2):
                        username = "kitajima"
                    elif (id == 3):
                        username = "Uwano"
                    elif (id == -1):
                        username = "Unknown"

                # VIEWの部分
                cv2.putText(self.img, "User:" + username+" fps:"+str(fps), (x, y - 10), self.font, 1, (0, 255, 0), 3)
                cv2.putText(self.img, "Conf:" + str(conf), (x, y - 50), self.font, 1, (0, 255, 0), 3)
                self.username=username
                cv2.imshow('aaa', self.img)
                print(threading.current_thread().getName()+" :"+str(time.time()))

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    def end(self):
        self.cap.release()
        cv2.destroyAllWindows()
    def register(self,who,callback=None):
        if callback is None:
            callback=getattr(who,'update')
        self.subscribers[who]=callback
    def unregister(self,who):
        del self.subscribers[who]
    def dispath(self,message):
        # ここのcallable はSubscriber のupdate 関数を指す
        for subscriber,callable in self.subscribers.items():
            callable(message)

    def subThread(self):# これをサブスレッドにする, ３秒置きメセージを送る
        while True:
            elapsedTime = time.time() - self.startTime
            if (elapsedTime > 3 and self.username!=""):
                print(threading.current_thread().getName()+" from camera:"+ str(time.time()))
                self.startTime = time.time()
                self.dispath(self.username)








if __name__=='__main__':


    face=FaceDetector()
    speaker=Speaker()
    face.register(speaker,speaker.update)

    face.update()


    face.end()
