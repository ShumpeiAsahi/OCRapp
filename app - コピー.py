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
    the_file = request.files['the_file']
    the_file.save("./" + the_file.filename)
    print(request.form['other_data'])
    print(the_file)  # 999
    return ""

if __name__ == "__main__":
    app.run(debug=True)