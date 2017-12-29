# -*- coding: utf-8 -*-
import cv2
from speech_api.jatts import jatts
import time
from datetime import datetime
#import multiprocessing as mp
import threading
import fps
import numpy as np
import requests
import json
# #　オブジェクト生成qqq
# speaker = jatts('あああああ')
# #話す
# speaker.speak()
# logic
## subscriber = speaker
# Publisher = detector ,が顔を認識したら、Speakerに名前を送る
# 解決した問題：発音のとき画面が止まった、threading なんとかする
# threading 処理をラッパーして、定義した、@threaded 追加でthreading できる


def threaded(fn):
    def wrapper(*args, **kwargs):
        thread = threading.Thread(target=fn, args=args, kwargs=kwargs)
        thread.daemon = True
        thread.start()
        return thread
    return wrapper


class Speaker:
    url = 'https://hooks.slack.com/services/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'

    def __init__(self, name='Speaker'):
        self.name = name

    def update(self, message):
        speaker = jatts(message)
        speaker.speak()
        # speaker.speak()
        now = datetime.now()
        payload = {"text": message + datetime.now().strftime("  %Y/%m/%d %H:%M:%S"),
                   }

        requests.post(Speaker.url, data=json.dumps(payload))
        print(threading.current_thread().getName() + " in speaker:" + datetime.now().strftime("%H:%M:%S"))


class FaceDetector:
    gFrameRate = fps.FrameRate()

    def __init__(self):

        self.subscribers = dict()
        self.detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        self.cap = cv2.VideoCapture(0)
        ret, self.img = self.cap.read()
        self.cap.set(cv2.CAP_PROP_FPS, 25)  # カメラFPSを60FPSに設定
        self.cap.set(cv2.CAP_PROP_BUFFERSIZE, 3)  # バッファ３フレームだけを保存
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # カメラ画像の横幅を1280に設定
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)  # カメラ画像の縦幅を720に設定

        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.recognizer.read("trainingData.yml")
        # 各種の初期化
        self.id = -1  # user ID
        self.conf = 0.0  # 顔の近似度を表す指標、低いほど似ている
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.flag = False
        self.detect_threshold = 10
        self.username = ""
        self.startTime = time.time()
        self.img = np.array([])

        self.faces = np.array([])
        self.fps = 0
        self.gray = []
        self.lastName = ""  # 前回　検知した名前
    # detect Face Area in camera and return the parameters

    @threaded
    def detectFaceArea(self):
        while True:
            time.sleep(0.5)
            ret, self.img = self.cap.read()
            # print(self.img.shape)
            fps = self.gFrameRate.get()
            self.gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)

            # print(self.gray.shape)# (480,640)

            faces = self.detector.detectMultiScale(self.gray, 1.3, 5)
            if(faces != ()):
                self.faces = faces
                self.fps = fps
            for (x, y, h, w) in faces:
                self.id, self.conf = self.recognizer.predict(self.gray[y:y + h, x:x + w])

            print(threading.current_thread().getName() + " detect:" + datetime.now().strftime("%H:%M:%S"))
    #@threaded

    def update(self):
        # 描画の関数
        username = ""
        while True:
            time.sleep(0.1)
            ret, self.img = self.cap.read()
            for (x, y, w, h) in self.faces:
                # draw rectangle around faces (x,y) start point w=width h=high ,color , thickness
                cv2.rectangle(self.img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                if (self.conf > 90):
                    username = "Unknown"
                else:
                    if (self.id == 1):
                        username = "chou"
                    elif (self.id == 2):
                        username = "kitajima"
                    elif (self.id == 3):
                        username = "Uwano"
                    elif (self.id == -1):
                        username = "unkown"

                # VIEWの部分
                cv2.putText(self.img, "User:" + username + " fps:" + str(self.fps), (x, y - 10), self.font, 1, (0, 255, 0), 3)
                cv2.putText(self.img, "Conf:" + str(self.conf), (x, y - 50), self.font, 1, (0, 255, 0), 3)
                self.username = username

            cv2.imshow('aaa', self.img)
            print(threading.current_thread().getName() + " :" + datetime.now().strftime("%H:%M:%S"))

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    def end(self):
        self.cap.release()
        cv2.destroyAllWindows()

    def register(self, who, callback=None):
        if callback is None:
            callback = getattr(who, 'update')
        self.subscribers[who] = callback

    def unregister(self, who):
        del self.subscribers[who]

    def dispath(self, message):
        # ここのcallable はSubscriber のupdate 関数を指す
        for subscriber, callable in self.subscribers.items():
            callable(message)

    @threaded
    def sendName(self):  # これをサブスレッドにする, ３秒置きメセージを送る
        self.lastName = ""
        while True:
            time.sleep(3)
            if(self.username != "" and self.username != self.lastName):
                self.dispath(self.username + "さんが研究室に入りました")
                self.lastName = self.username
                print(threading.current_thread().getName() + " from camera:" + datetime.now().strftime("%H:%M:%S"))


if __name__ == '__main__':

    # 顔認識のオブジェクト生成
    face = FaceDetector()
    #　スピーカのオブジェクト生成
    speaker = Speaker()
    # スピーカーを顔認識機に登録する＝リスンニングする
    face.register(speaker, speaker.update)

    #　thread-1 :１,顔検出＋２，顔認識の処理をこのスレッドで処理する

    face.detectFaceArea()
    # thread-2 :１,新しい顔認識したら、その名前を送る　２，スピーカーが受け取ったら発話
    face.sendName()

    # MainThread :画面を更新する
    face.update()

    face.end()
