# -*- coding: utf-8 -*-
from gtts import gTTS
import os,errno
import sys
from pygame import mixer,time

filename = 'temp.mp3'
def silentremove(filename):
    try:
        os.remove(filename)
        print("delete temp file")
    except OSError as e: # this would be "except OSError, e:" before Python 2.6
        if e.errno != errno.ENOENT: # errno.ENOENT = no such file or directory
            raise # re-raise exception if a different error occurred

def jatts(words):
    silentremove(filename)
    tts = gTTS(text=words, lang='ja')
    tts.save(filename)
    # mixerモジュールの初期化
    mixer.init()
    # 音楽ファイルの読み込み
    mixer.music.load(filename)
    # 音楽再生、および再生回数の設定(-1はループ再生)
    mixer.music.play(1)
    # 再生の終了
    while mixer.music.get_busy():
        time.Clock().tick(10)
    mixer.music.stop()
    mixer.quit()
# jatts("こんにちわ")