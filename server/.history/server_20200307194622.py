from pathlib import Path
from flask import Flask, render_template, request, send_file, send_from_directory, safe_join, abort, current_app
# from werkzeug import secure_filename
import pandas as pd
import os
import time
import titles
import readerClass as rc
import json
import columns
import comparison
from flask_cors import CORS
from haikunator import Haikunator
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
      excelType = request.form['type']
      filename = request.form['filename']

      # TODO: maybe check if file alreay exists and not save multipletime
      # - get list of all files
      # - if filename variable is a substr of any file name in folder: compare their contents
      # - if match don`t save file again but use that one
      name = "uploads/" + filename + "-" + haikunator.haikunate(token_chars='ABCDEFGHIJKLMNOPQRSTUVXYZ') + ".xlsx"
      while Path(name).exists():
          name = "uploads/" + filename + "-" + haikunator.haikunate(token_chars='ABCDEFGHIJKLMNOPQRSTUVXYZ') + ".xlsx"
      f.save(name)

      df = pd.read_excel(Path(name), sheet_name=0)
      
      return json.dumps(ret, indent=4, sort_keys=True, default=str)


@app.route("/api/sendReport", methods=['POST'])
def addReport():
    report = request.json
    with open("reports.json", 'r+', encoding='utf8') as f:
        reports = json.load(f)
        reports.append(report)
        f.seek(0)
        f.write(json.dumps(reports))
    return "OK"

@app.route("/api/getReports", methods=['GET'])
def getReporsts():
    with open("reports.json", 'r', encoding='utf8') as f:
        reports = json.load(f)
        return json.dumps(reports)

@app.route("/api/setReports", methods=['POST'])
def setReports():
    try:
        reports = request.json
        with open("reports.json", 'w', encoding='utf8') as f:
            f.write(json.dumps(reports))
        return "OK"
    except:
        return "NOT OK:("

@app.route('/api/goodTitles', methods = ['GET', 'POST'])
def get_good_titles():
   titles = request.json
   return comparison.getComparisonJson(titles)

@app.route('/api/version', methods = ['GET'])
def getApplicationVersion():
    applicationVersionFile = open(Path('data/applicationVersion.txt'), "r")
    return applicationVersionFile.readline(3)


if __name__ == '__main__':
   app.run(debug = False, host='0.0.0.0')
        