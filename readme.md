## 仕様
- python3.5.0
- opencv3.3.1 
PS：この辺の依存関係結構重要，バージョンが違うと動かない場合が多い


##ファイル

- getImageFromCamera.py : ウェブカメラから，２０枚学習用写真を取る
- makeClassifier.py:写真を学習し，特徴量抽出、分類器をつくる。＝＞trainingData.yml に保存する
- faceDetector.py:traningData.yml を読み込む，カメラで顔を認識し，名前を表示する

##使い方

1. getImageFromCamera.py 回してカメラから学習データを取る
2. makeClassifier.py　回して分類器をつくる
3. faceDetector.pyを回して顔認識する