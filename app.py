# -*- coding:utf-8 -*-
# @Time   ：2020/10/25 17:18
# @Email  ：lmfmxcl@163.com
# @Author ：mingfei_liao
# @File   ：app.py.py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World ee"

if __name__ == '__main__':
    app.run(port='8080',debug=True)