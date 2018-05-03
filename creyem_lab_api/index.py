import datetime as dt
import os
import logging

from flask import Flask, jsonify, request
from pymongo import MongoClient

from creyem_lab_api.model.case import Case, CaseSchema
from creyem_lab_api.model.hotspot import Hotspot, HotspotSchema


app = Flask(__name__)

if app.config['ENV'] == "development":
    config = os.path.join(app.root_path, 'config/development.cfg')
else:
    config = os.path.join(app.root_path, 'config/production.cfg')

app.config.from_pyfile(config)


@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response


client = MongoClient(app.config['MONGODB_URL'])
db = client['creyem_lab_api']


@app.route('/')
def get_todos():
    return 'Creyem Labs API'


@app.route('/cases')
def get_cases():
    cases = db.cases.find()

    schema = CaseSchema(many=True)
    cases_list = schema.dump(
        cases
    )

    return jsonify(cases_list.data)


@app.route('/cases', methods=['POST'])
def add_case():
    case_data = request.get_json()
    case_data['created_at'] = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    case = CaseSchema().load(case_data)
    db.cases.insert_one(case.data)

    return '', 204


@app.route('/hotspots/<case_id>')
def get_hotspots(case_id):
    hotspots = db.hotspots.find({"case_id": case_id})

    schema = HotspotSchema(many=True)
    hotspots_list = schema.dump(
        hotspots
    )

    return jsonify(hotspots_list.data)


@app.route('/hotspots', methods=['POST'])
def add_hotspot():
    hotspot_data = request.get_json()
    hotspot_data['created_at'] = dt.datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S")

    hotspot = HotspotSchema().load(hotspot_data)
    db.hotspots.insert_one(hotspot.data)

    return '', 204


if __name__ == "__main__":
    app.run()
