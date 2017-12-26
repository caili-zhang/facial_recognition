# -*- coding: utf-8 -*-
from gtts import gTTS
# import os,errno
import pygame
#import time
#import threading
# thread 機能追加、インスタンス生成したら、スレッド生成、時間間隔制御可能,無駄でした。。。。
# speak 機能呼び出せるならいい
# https://stackoverflow.com/questions/18416116/python-class-instance-starts-method-in-new-thread
class jatts():

    def __init__(self,words='こんにちわ',filename='temp.mp3'):

        self.filename = filename
        self.words=words

    #t秒置きｎ回呼び出す
    # def __init__(self,words='こんにちわ',filename='temp.mp3',t=5):
    #     super(jatts, self).__init__()
    #     self.cancelled = False
    #     #self.daemon=True
    #     self.filename = filename
    #     self.words=words
    #     self.t=t


    # def run(self):
    #     """Overloaded Thread.run, runs the update
    #             method once per every 10 milliseconds."""
    #     while not self.cancelled:
    #         self.speak()
    #         time.sleep(self.t)
    #
    # def cancel(self):
    #     """End this timer thread"""
    #     self.cancelled = True


    # 使わなくても問題ない　なんで？？
    # def silentremove(self):
    #     try:
    #         os.remove(self.filename)
    #         print("delete {}".format(self.filename))
    #     except OSError as e: # this would be "except OSError, e:" before Python 2.6
    #         if e.errno != errno.ENOENT: # errno.ENOENT = no such file or directory
    #             raise # re-raise exception if a different error occurred

    def speak(self):
        #self.silentremove()
        tts = gTTS(text=self.words, lang='ja')

        tts.save(self.filename)
        # mixerモジュールの初期化
        pygame.mixer.init()
        # 音楽ファイルの読み込み
        #print(threading.current_thread().getName())
        with open(self.filename, 'rb') as file_object:
            pygame.mixer.music.load(file_object)
            # 音楽再生、および再生回数の設定(-1はループ再生)
            pygame.mixer.music.play(1)
            # wait till the music end
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)

            pygame.mixer.music.stop()
            pygame.mixer.quit()

#　Threadオブジェクト生成
# speaker = jatts("aaaa")
# speaker.speak()