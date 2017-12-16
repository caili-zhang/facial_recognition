## 引用したサイト：
{% youtube 1Jz24sVsLE4&t=7s %}
OpenCV Face Detection | How to setup OpenCV with python and Write a face detection program
Codacusさんのチュートリアルありがとうございます。

## 仕様
- python3.5.0
- opencv3.3.1 
PS：この辺の依存関係結構重要，バージョンが違うと動かない場合が多い


## ファイル

- getImageFromCamera.py : ウェブカメラから，２０枚学習用写真を取る
- makeClassifier.py:写真を学習し，特徴量抽出、分類器をつくる。＝＞trainingData.yml に保存する
- faceDetector.py:traningData.yml を読み込む，カメラで顔を認識し，名前を表示する

## 使い方

1. getImageFromCamera.py 回してカメラから学習データを取る
2. makeClassifier.py　回して分類器をつくる
3. faceDetector.pyを回して顔認識する

## TODO
1. 挨拶機能追加，google text to speech api を使う
- gTTS api，pip install gTTS 文字＝＞音声に変換する
- pygame api, pip install pygame , 音声ファイルの操作

2. 音声認識する，googole speech to text api を使う
- google speech to text api, pip install Speech_Recognition 音声認識し，日本語に変換
- pyaudio が必要，pip install pyaudio

3. 会話のロジック：追加予定