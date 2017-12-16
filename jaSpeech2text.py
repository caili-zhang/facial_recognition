# -*- coding: utf-8 -*-
import speech_recognition as sr

r=sr.Recognizer()

with sr.Microphone() as source:
    print('say something')
    audio = r.listen(source)
try:
    #print('googole respond:\n' + r.recognize_google(audio)) #デフォルト設定は英語
    print('googole respond:\n' +r.recognize_google(audio,language="ja-JP"))
    #print('googole respond:\n' + r.recognize_google(audio, language="cmn-Hans-CN"))
except:
    pass