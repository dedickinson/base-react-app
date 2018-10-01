from flask import Flask, Response
from flask_cors import CORS
import json
import time

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

with open('data/postcodes.json', 'r') as data:
    postcode_data = json.load(data)


@app.route("/postcodes", methods=['GET'])
def get_postcodes():
    return Response(json.dumps(postcode_data), mimetype='application/json')


@app.route("/postcodes/<postcode>", methods=['GET'])
def get_postcode(postcode: str):
    data = [record for record in postcode_data
            if record['postal_code'] == postcode]
    #time.sleep(10)
    return Response(json.dumps(data), mimetype='application/json')
