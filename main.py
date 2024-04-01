import os
import shutil

import numpy as np
import pandas as pd

from flask import Flask,render_template,request,jsonify

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/select',methods=['POST'])
def select():
    global csv_path
    img_folder_path = request.json["img_folder_path"]
    csv_path = request.json["csv_path"]
    current_dir = os.getcwd()

    if img_folder_path.startswith("~"):
        img_folder_path = os.path.expanduser(img_folder_path)
    img_list = [img for img in os.listdir(img_folder_path) if img.endswith(".jpg")]
    img_name = sorted(img_list)[0][:-6]
    if not os.path.exists(os.path.join(current_dir,"static","img",img_name)):
        os.makedirs(os.path.join(current_dir,"static","img",img_name), exist_ok=True)
        #画像アップロード
        for img_path in img_list:
            shutil.copy(os.path.join(img_folder_path,img_path), os.path.join(current_dir,"static","img",img_name,img_path))
    #画像の総数取得
    max_num = len(img_list)

    df = pd.read_csv(csv_path)
    columns = [column[:-2] for column in df.columns if "_x" in column]

    return jsonify({"max_num":max_num,"img_name":img_name,"columns":columns})

#画像内をクリックしたときの処理
@app.route('/img_click',methods=['POST'])
def img_click():
    try:
        column_name = request.json["column_name"]
        x = request.json["x"]
        y = request.json["y"]
        frame = request.json["frame"]

        df = pd.read_csv(csv_path,index_col="frame")
        df[f"{column_name}_x"][frame] = x
        df[f"{column_name}_y"][frame] = y

        df.to_csv(csv_path)
        return jsonify({"error":"False"})
    
    except Exception as e:
        # エラーが発生した場合、エラーメッセージとステータスコードを返す
        return jsonify({"error":"True"})

if __name__ == "__main__":
    app.run(debug=True,host='localhost',port=5000)

