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
import unidecode

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

        # TODO: maybe check if file alreay exists and not save multipletime
        # - get list of all files
        # - if filename variable is a substr of any file name in folder: compare their contents
        # - if match don`t save file again but use that one
        name = filename + '.pdf'
        if Path(name).exists():
            name = filename + '.pdf'
        f.save(name)

        pdfFileObject = open('clauze.pdf', 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObject)
        pages = pdfReader.numPages
        clauzeDoc = ''
        for page in pages:
            clauzeDoc += pdfReader.getPage(page).extractText()
        
        pdfFileObject1 = open(name, 'rb')
        pdfReader1 = PyPDF2.PdfFileReader(pdfFileObject1)
        pages1 = pdfReader1.numPages
        contractDoc = ''
        for page in pages1:
            contractDoc += pdfReader1.getPage(page).extractText()

        for i in len(clauzeDoc) - 30:
            substring = clauzeDoc[i:i+30]
            if substring in 
         


        return 1


if __name__ == '__main__':
   app.run(debug = False, host='0.0.0.0')



        