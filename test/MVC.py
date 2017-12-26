# -*- coding: utf-8 -*-
import cv2
from speech_api import jatts
class Model:
    def __init__(self):
        #　観察者　データの初期化
        self.__observer = None
        self.__name = None
        self.detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FPS, 10)  # カメラFPSを60FPSに設定
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 720)  # カメラ画像の横幅を1280に設定
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)  # カメラ画像の縦幅を720に設定

        self.recognizer = cv2.face.LBPHFaceRecognizer_create()

        self.recognizer.read("trainingData.yml")

        self.id = -1
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.flag = False
        self.detect_threshold = 10
        self.username = ""
        self.img=None
        self.conf=0
        self.x=0
        self.y=0
        self.h=0
        self.w=0

    def update(self):
        # 各種類の計算処理：
        self.ret, self.img = self.cap.read()
        gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        # size, likelyhood
        faces = self.detector.detectMultiScale(gray, 1.3, 5)

        for (self.x, self.y, self.w, self.h) in faces:
            # draw rectangle around faces (x,y) start point w=width h=high ,color , thickness
            cv2.rectangle(self.img, (self.x, self.y), (self.x + self.w, self.y + self.h), (255, 0, 0), 2)
            username=""
            self.id, self.conf = self.recognizer.predict(gray[self.y:self.y + self.h, self.x:self.x + self.w])
            if (self.conf > 90):
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
            self.username=username



    def add_observer(self, observer):
        #観察者を追加、状態変化を監視
        self.__observer = observer

    def notify_observer(self):
        #変化があったら、更新する
        self.__observer.update(self)

    @property
    def name(self):
        #ゲッターですね
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name
        self.notify_observer()


class View:
    # 顔認識のメインロジック



    def input(self):
        return input("Enter name: ")

    def update(self, model):
        #ここで画面を更新する
        cv2.putText(model.img, "User:" + model.username, (model.x, model.y - 10), model.font, 1, (0, 255, 0), 3)
        cv2.putText(model.img, "Conf:" + str(model.conf), (model.x, model.y - 50), model.font, 1, (0, 255, 0), 3)
        cv2.imshow('face recognition', model.img)




class Controller:
    #　全体の流れを制御する
    def __init__(self):
        #object を生成する
        self.model = Model()
        self.view = View()
        #self.model.add_observer(self.view)

    def start(self):
        #メイン処理をする
        while True:
            #各種変数計算と更新
            self.model.update()
            #変数を画面に表示する
            self.view.update(self.model)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        self.end()

    def end(self):
        self.model.cap.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    Controller().start()
