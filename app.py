#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
__version__     =   "0.0.1"
__author__      =   "@lantip"
__date__        =   "2020/05/11"
__description__ =   "Latin to Javanese Transliterator"
"""
import os
import json
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from latintojavanese import dotransliterate


app = Flask(__name__, template_folder="example", static_folder="example")
app.config.from_pyfile('settings.cfg')
# CORS policy
CORS(app)


@app.route('/', methods=['POST'])
def index():
    text = request.form.get('text')
    result = dotransliterate(text)

    resp = {
        'status': 'OK',
        'result': result
    }

    return json.dumps(resp)


@app.route('/form', methods=['GET'])
def form():
    return render_template('formpage.html')


if __name__ == '__main__':
    app.run(app.config['DEBUG'])
