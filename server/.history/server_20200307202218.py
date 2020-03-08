from pathlib import Path
from flask import Flask, render_template, request, send_file, send_from_directory, safe_join, abort, current_app
# from werkzeug import secure_filename
import pandas as pd
import os
import time
import json
from flask_cors import CORS
from haikunator import Haikunator
import unidecode
import PyPDF2

haikunator = Haikunator()

app = Flask(__name__)
CORS(app)

applicationVersion = 0

@app.route('/upload')
def upload_file():
   return render_template('upload.html')

@app.route('/api/titles', methods = ['GET', 'POST'])
def get_titles():
   if request.method == 'POST':
        f = request.files['file']
        filename = request.form['filename']

        name = filename + '.pdf'
        while Path(name).exists():
            name = filename + '.pdf'
        f.save(name)

        pdfFileObject = open(name, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObject)
        pageObject = pdfReader.getPage(0)
        print(pageObject.extractText())
        
        return 1


if __name__ == '__main__':
   app.run(debug = False, host='0.0.0.0')



        