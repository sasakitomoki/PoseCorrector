# README.md

## 概要
このプログラムは、画像フレームをクリックすることで`position_data.csv`を修正するためのものです。ユーザーは画像上の特定の位置をクリックすることで、その位置の座標データをCSVファイルに記録し、データを更新することができます。

## セットアップ手順
1. コマンドプロンプトで以下のコマンドを実行します。
"""cmd
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python main.py
"""
2. ブラウザで`localhost:5000`にアクセスします。

## 使用手順
1. `position_data.csv`へのパスを入力します。
2. 画像フォルダへのパスを入力します（画像名は末尾が連番です）。
3. 部位名を入力します（部位名は`position_data.csv`の列名に従い、末尾の"_x","_y"を削除したものです）。
4. 決定ボタンを押します。
5. 修正したいフレームを表示させ、対応部位をクリックします。`position_data.csv`の対応部位の(x, y)座標が変更されます。
