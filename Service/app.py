from flask import Flask
from flask import send_file
from flask import request
from PIL import Image, ImageDraw, ImageFont
import requests
import json
import pyparsing as pp

app = Flask(__name__)

url = "https://api.powerbi.com/beta/62749e39-ab58-47c0-b2f4-6a8c59465a9c/datasets/9f5368d8-b7b2-4a65-a9c6-7141f8f65548/rows?key=JkUYwx2iNjqlz0hdGgBroU9skFjqUt5w4Ra1m1%2Faw7MnKGLEyHM7xPcEzdeUHg7ZTpzcMM%2FixPTSjWnPL65mzg%3D%3D"

@app.route('/data')

def data():
        slicerValues = pp.commaSeparatedList.parseString(request.args.get('Values')).asList()
        slicerNames = pp.commaSeparatedList.parseString(request.args.get('Filters')).asList()
        slicer =  [(slicerNames[i], slicerValues[i]) for i in range(0, len(slicerNames))]
        unixTime = request.args.get('EPOCH')
        username = request.args.get('UserName')

        arr = []
        for slicer,value in slicer:
            vals = {}
            vals['FilterName'] = slicer
            vals['FilterValue'] = value
            vals['EPOCH'] = unixTime
            vals['UPN'] = username
            arr.append(vals)
        payload = json.dumps(arr)
        headers = {'Content-Type': 'application/json'}
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
        return send_file('unicode-text.png', mimetype='image/png')

