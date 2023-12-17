from flask import Flask,render_template,request,jsonify
import os
import shutil
import numpy as np
import pandas as pd

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

    img_list=os.listdir(img_folder_path)
    img_name=sorted(img_list)[0][:-6]
    if not os.path.exists(os.path.join(current_dir,"static","img",img_name)):
        #画像アップロード
        shutil.copytree(img_folder_path, os.path.join(current_dir,"static","img",img_name))

    #画像の総数取得
    max_num = len(img_list)

    return jsonify({"max_num":max_num,"img_name":img_name})

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

