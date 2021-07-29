#C:\Users\Twss9002\AppData\Local\Programs\Python\Python39\python.exe
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import sys
import cgi

#recieve = sys.stdin.readline()
#recieve = recieve + "OK!"

print('Content-type: text/html\n')
print("OK")

def outputText():
    if request.method == 'POST':
        print("OKです")
        #posted_img = request.FILES['image']
        #new_image = Image.objects.create(image=posted_img)
        #return HttpResponse(new_image.image.url)
        return "ok"
    else :
        return print("ダメ")
    return print("mada")
    
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
