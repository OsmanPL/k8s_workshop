from flask import Flask, jsonify
from flask import request 
import json
from flask_cors import CORS
from services import registro
from os import getenv

app = Flask(__name__)
CORS(app)

@app.route('/getRegistros', methods=['GET'])
def getRegistro():
    if request.method == 'GET':
        return registro.getRegistros()
    else:
        retorno = {"server": "python", 'mensaje': 'Metodo no manejado'}
        return jsonify(retorno)

@app.route('/addRegistro', methods=['POST'])
def registrar():
    nombre = request.json['nombre']
    if request.method == 'POST':
        return registro.registrar(nombre)
    else:
        retorno = {'server': 'python', 'mensaje': 'Metodo no manejado'}
        return jsonify(retorno)



if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True,port=3000)

