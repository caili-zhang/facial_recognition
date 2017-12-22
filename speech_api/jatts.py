# -*- coding: utf-8 -*-
from gtts import gTTS
import os,errno
from pygame import mixer,time
# from tempfile import TemporaryFile


class jatts:
    def __init__(self,words='こんにちわ',filename='temp.mp3'):
        self.filename = filename
        self.words=words

    def silentremove(self):
        try:
            os.remove(self.filename)
            print("delete {}".format(self.filename))
        except OSError as e: # this would be "except OSError, e:" before Python 2.6
            if e.errno != errno.ENOENT: # errno.ENOENT = no such file or directory
                raise # re-raise exception if a different error occurred

    def speak(self):
        tts = gTTS(text=self.words, lang='ja')
        # f=TemporaryFile()
        # tts.write_to_fp(f)
        tts.save('temp.mp3')
        # f.close()
        #subprocess.call("vlc -I rc --play-and-stop temp.mp3", shell=True)

        # mixerモジュールの初期化
        mixer.init()
        # 音楽ファイルの読み込み

        with open('temp.mp3', 'rb') as file_object:

            mixer.music.load(file_object)
            # 音楽再生、および再生回数の設定(-1はループ再生)
            mixer.music.play(1)
            # 再生の終了
            while mixer.music.get_busy():
                time.Clock().tick(10)
            mixer.music.stop()
            mixer.quit()



# #　オブジェクト生成
# speaker = jatts('あ')
# #話す
# speaker.speak()
# speaker.silentremove()
#
# #　オブジェクト生成
# speaker = jatts('ああ')
# #話す
# speaker.speak()
# speaker.silentremove()
#
# #　オブジェクト生成
# speaker = jatts('あああ')
# #話す
# speaker.speak()
#
# #　オブジェクト生成
# speaker = jatts('あああ')
# #話す
# speaker.speak()
#
# #　オブジェクト生成
# speaker = jatts('あああ')
# #話す
# speaker.speak()
