from flask import Flask, render_template, request,make_response
import flask
from flask_cors import CORS,cross_origin
import post as post
import json
import werkzeug
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

@app.route("/" ,methods=["POST"])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def upload():
    print("upload()が呼び出された")
    if 'file' not in flask.request.files:
        return 'ファイル未指定'

    # fileの取得（FileStorage型で取れる）
    # https://tedboy.github.io/flask/generated/generated/werkzeug.FileStorage.html
    fs = flask.request.files['file']

    # 下記のような情報がFileStorageからは取れる
    app.logger.info('file_name={}'.format(fs.filename))
    app.logger.info('content_type={} content_length={}, mimetype={}, mimetype_params={}'.format(
        fs.content_type, fs.content_length, fs.mimetype, fs.mimetype_params))

    # ファイルを保存
    fs.save('保存するファイルパス')

    return "フィアルアップロード成功"
def outputText():
    if request.method == 'POST':
        print("outputText()が呼び出された")
        print("OKです")
        posted_img = flask.request.FILES['file']
        #print(posted_img)
        #new_image = Image.objects.create(image=posted_img)
        #return HttpResponse(new_image.image.url)
        return "ok"
    else :
        return print("ダメ")
    return print("mada")


if __name__ == "__main__":
    app.run(debug=True)