from flask import Flask
from flask import request
from flask import abort
from flask import jsonify
from flask_cors import CORS

import companiesDB
import objectsDB

app = Flask(__name__)
CORS(app)

@app.route('/objects/', methods = ['GET'])
def get_all_objects():
    objects = objectsDB.get_all()
    return jsonify(objects)

@app.route('/object/<string:name>', methods = ['GET'])
def get_object(name):
    objects = objectsDB.get_by_name(name)
    return jsonify(objects)

# TODO: finish
@app.route('/object/', methods = ['POST'])
def insert_object():
    if request.is_json:
        content = request.get_json()
        return 'Novo objeto adicionado \nNome: %s | Categoria: %s' % (content["objectName"], content["category"])
    else:
        return abort(400, 'ERROR: Must receive a json')

# TODO: finish
@app.route('/object/', methods = ['PUT'])
def replace_object():
    if request.is_json:
        content = request.get_json()
        return 'Objeto %s atualizado' % content["objectName"]
    else:
        abort(400, 'ERROR: Must receive a json')

# TODO: finish
@app.route('/object/', methods = ['DELETE'])
def delete_object():
    if request.is_json:
        content = request.get_json()
        return 'Objeto %s deletado' % content["objectName"]
    else:
        abort(400, 'ERROR: Must receive a json')

@app.route('/companies/', methods = ['GET'])
def get_all_companies():
    companies = companiesDB.get_all()
    return jsonify(companies)

@app.route('/companies/<string:object_name>', methods = ['GET'])
def get_companies(object_name):
    object_category = objectsDB.get_category(object_name)
    companies = companiesDB.get_by_category(object_category)
    return jsonify(companies)

# TODO: finish
@app.route('/company/', methods = ['POST'])
def insert_company():
    if request.is_json:
        content = request.get_json()
        return 'Nova empresa adicionada \nNome: %s' % content["nome"]
    else:
        return abort(400, 'ERROR: Must receive a json')

# TODO: finish
@app.route('/company/', methods = ['DELETE'])
def delete_company():
    if request.is_json:
        content = request.get_json()
        return 'Empresa %s deletada' % content["nome"]
    else:
        abort(400, 'ERROR: Must receive a json')

@app.route('/', methods = ['GET'])
def test():
    response = jsonify({'message': 'Oá Me-Recicla'})
    return response