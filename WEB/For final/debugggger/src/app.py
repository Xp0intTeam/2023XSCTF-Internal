# -*- coding: utf-8 -*-
from flask import Flask, request, render_template, render_template_string
import os

app = Flask(import_name=__name__,
            static_url_path='/static',
            static_folder='static',
            template_folder='templates')


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    filepath = './uploads/'
    filelist = []
    for i, j, k in os.walk(filepath):
        filelist = k
    textfile = request.args.get('file')
    if textfile is None:
        return render_template("index.html", filelist=filelist, text='')
    else:
        with open(filepath + textfile, 'r', encoding='utf-8') as f:
            content = f.read()
        f.close()
        return render_template("index.html", filelist=filelist, text=content)



if(__name__ == "__main__"):
    app.run("0.0.0.0",5000,debug=True)
