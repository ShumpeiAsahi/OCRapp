from flask import Flask, render_template, request,make_response
import flask
from flask_cors import CORS,cross_origin
import post as post
import json
import werkzeug
import os
from PIL import Image, ImageOps
import pyocr
app = flask.Flask(__name__)
api = Flask(__name__)
CORS(app)

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', 'http://127.0.0.1:5000/')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response


@app.route('/')
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/capture')
def caputure():
    return render_template('capture.html')

@app.route("/" ,methods=["POST"])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def test():
    if request.method == 'POST':
        f = flask.request.json
        image = f["image"]
        print(f"{image}")
        img = Image.open(f"{image}").convert(mode="L")
        #img = ImageOps.invert(img)

        #pyocrへ利用するOCRエンジンをTesseractに指定する。
        #tools = pyocr.get_available_tools()
        #tool = tools[0]

        #画像から文字を読み込む
        #builder = pyocr.builders.TextBuilder(tesseract_layout=4)
        #text2 = tool.image_to_string(img, lang="jpn", builder=builder)

        #print(text2)


        return "Response('ok')"

if __name__ == "__main__":
    app.run(debug=True)