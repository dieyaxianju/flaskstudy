# -*- coding:utf-8 -*-
# @Time   ：2020/10/25 17:18
# @Email  ：lmfmxcl@163.com
# @Author ：mingfei_liao
# @File   ：app.py.py
from flask import Flask
from flask import render_template

import settings
app = Flask(__name__)
app.config.from_object(settings)

@app.route('/')
def register():
    return render_template('register.html')

if __name__ == '__main__':
    app.run()