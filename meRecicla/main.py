from flask import Flask
from flask import request
from flask import abort
app = Flask(__name__)

@app.route('/objects/', methods = ['GET'])
def get_all_objects(): # get all objects
    return 'Retornar todos os objetos'

@app.route('/object/<string:object>', methods = ['GET'])
def get_object(object): # search for the given object
    return 'Objeto a ser buscado é: %s' % object

@app.route('/object/', methods = ['POST'])
def insert_object(): # insert the new object
    if request.is_json:
        content = request.get_json()
        return 'Novo objeto adicionado \n Nome: %s ,Categoria: %s' % (content["objectName"],content["categoriy"])
    else:
        return abort(400, 'ERROR   Must receive a json')

@app.route('/object/', methods = ['PUT'])
def replace_object(): # replace the object
    if request.is_json:
        content = request.get_json()
        return 'Objeto %s atualizado' % content["objectName"]
    else:
        abort(400, 'ERROR   Must receive a json')

@app.route('/object/', methods = ['DELETE'])
def delete_object(): # delete the object
    if request.is_json:
        content = request.get_json()
        return 'Objeto %s deletado' % content["objectName"]
    else:
        abort(400, 'ERROR   Must receive a json')

@app.route('/')
def test(): # search for the given object name in the data base
    return 'Olá me recicla'
