# -*- coding: utf-8 -*-

import os
import json
from sqlalchemy import create_engine
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, jsonify
from django.utils.encoding import smart_str, smart_unicode

# create our application :)
app = Flask(__name__)

def connect_db(connection_string):
    #"""Connects to the specific database."""
    eng = create_engine(connection_string)
    conn = eng.connect()
    return conn

@app.errorhandler(500)
def custom500(error):
    response = jsonify(message=str(error))
    response.status_code = 500
    return response

@app.route('/', methods=['POST'])
def show_result():
    conn = connect_db(request.headers.get('connection_string'))
    rs = conn.execute(request.headers.get('query'))
    result =  [ dict(zip(i.keys(), i.values())) for i in rs ]
    result = [dict([a, smart_str(x)] for a, x in b.iteritems()) for b in result]
    return json.dumps(result)


if __name__ == '__main__':
    app.run(debug=False)
