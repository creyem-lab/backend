import os
import logging

from flask import Flask, jsonify, request
from pymongo import MongoClient

from creyem_lab_api.model.case import Case, CaseSchema


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
    case = CaseSchema().load(request.get_json())
    db.cases.insert_one(case.data)

    return '', 204


if __name__ == "__main__":
    app.run()
