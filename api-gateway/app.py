import datetime
import re

from flask import Flask
from flask import request
from flask import jsonify
from waitress import serve
from flask_jwt_extended import create_access_token, verify_jwt_in_request
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import JWTManager
import json
import requests

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "123" # Change this!
jwt = JWTManager(app)

############################## INICIO DE SESION ##############################
@app.route("/login", methods=["POST"])
def inicio_sesion():
    datos_entrada = request.get_json()
    configuracion = cargar_configuracion()
    headers = {"Content-Type": "application/json; charset=utf8"}
    respuesta = requests.post(configuracion["url-ms-usuarios"] + "/usuarios/login", json=datos_entrada, headers=headers)
    print(configuracion["url-ms-usuarios"] + "/usuarios/login")
    print(respuesta.status_code)

    if respuesta.status_code == 200:
        usuario = respuesta.json()
        tiempo_caducidad_token = datetime.timedelta(60 * 60 * 24)
        token_acceso = create_access_token(identity=usuario, expires_delta=tiempo_caducidad_token)
        return {"token_acceso": token_acceso}
    else:
        return jsonify({"mensaje": "verificar correo y contraseña"})

############################## VERIFICA SESION ##############################
@app.before_request
def verificar_peticion():
    print("ejecuci'on callback ...")
    #print("url->",request.url)
    #print("url->", limpiarURL(request.url))
    #print("metodo->", request.method)

    endPoint = limpiarURL(request.path)
    excludedRoutes = ["/login","/candidatos","/partidos","/mesas"]

    if excludedRoutes.__contains__(request.path):
        pass
    elif verify_jwt_in_request():
        usuario = get_jwt_identity()
        if usuario["rol"] is not None:
            tienePermiso = validarPermiso(endPoint, request.method, usuario["rol"]["_id"])
            if not tienePermiso:
                return jsonify({"message": "Permission denied"}), 401
        else:
            return jsonify({"message": "Permission denied"}), 401

############################## LIMPIA URL ##############################
def limpiarURL(url):
    partes = url.split("/")
    for laParte in partes:
        if re.search('\\d', laParte):
            url = url.replace(laParte, "?")
    return url

############################## VALIDA PERMISO ##############################
def validarPermiso(endPoint, metodo, idRol):
    configuracion = cargar_configuracion()
    url = configuracion["url-ms-usuarios"] + "/rolpermiso/" + str(idRol)
    tienePermiso = False
    headers = {"Content-Type": "application/json; charset=utf-8"}
    body = {
        "url": endPoint,
        "metodo": metodo
    }
    response = requests.post(url, json=body, headers=headers)
    try:
        data = response.json()
        if ("_id" in data):
            tienePermiso = True
    except:
        pass
    return tienePermiso

############################## CRUD CANDIDATOS ##############################
@app.route('/candidatos', methods=["GET"])
def consulta_candidato():
    headers = {"Content-Type": "application/json; charset=utf8"}
    configuracion = cargar_configuracion()
    url = configuracion["url-ms-estructura"] + "/candidatos"
    respuesta = requests.get(url,headers=headers)
    json = respuesta.json()
    return jsonify(json)

@app.route('/candidatos', methods=["POST"])
def crear_candidato():
    datosEntrada = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf8"}
    configuracion = cargar_configuracion()
    url = configuracion["url-ms-estructura"] + "/candidatos"
    respuesta = requests.post(url,json=datosEntrada,headers=headers)
    json = respuesta.json()
    return jsonify(json)

@app.route("/candidatos/<string:id>", methods=['PUT'])
def modificarCandidato(id):
    datosEntrada = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    configuracion = cargar_configuracion()
    url = configuracion["url-ms-estructura"] + "/candidatos/" + id
    respuesta = requests.put(url, headers=headers, json=datosEntrada)
    json = respuesta.json()
    return jsonify(json)

@app.route("/candidatos/<string:id>", methods=['DELETE'])
def eliminarCandidato(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    configuracion = cargar_configuracion()
    url = configuracion["url-ms-estructura"] + "/candidatos/" + id
    print(url)
    respuesta = requests.delete(url, headers=headers)
    json = respuesta.json()
    return jsonify(json)

############################## CRUD PARTIDOS ##############################
@app.route('/partidos', methods=["GET"])
def consulta_partido():
    headers = {"Content-Type": "application/json; charset=utf8"}
    configuracion = cargar_configuracion()
    url = configuracion["url-ms-estructura"] + "/partidos"
    respuesta = requests.get(url,headers=headers)
    json = respuesta.json()
    return jsonify(json)

@app.route('/partidos', methods=["POST"])
def crear_partido():
    datosEntrada = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf8"}
    configuracion = cargar_configuracion()
    url = configuracion["url-ms-estructura"] + "/partidos"
    respuesta = requests.post(url,json=datosEntrada,headers=headers)
    json = respuesta.json()
    return jsonify(json)

@app.route("/partidos/<string:id>", methods=['PUT'])
def modificarPartido(id):
    datosEntrada = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    configuracion = cargar_configuracion()
    url = configuracion["url-ms-estructura"] + "/partidos/" + id
    respuesta = requests.put(url, headers=headers, json=datosEntrada)
    json = respuesta.json()
    return jsonify(json)

@app.route("/partidos/<string:id>", methods=['DELETE'])
def eliminarPartido(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    configuracion = cargar_configuracion()
    url = configuracion["url-ms-estructura"] + "/partidos/" + id
    print(url)
    respuesta = requests.delete(url, headers=headers)
    json = respuesta.json()
    return jsonify(json)

############################## CRUD MESAS ##############################
@app.route('/mesas', methods=["GET"])
def consulta_mesa():
    headers = {"Content-Type": "application/json; charset=utf8"}
    configuracion = cargar_configuracion()
    url = configuracion["url-ms-estructura"] + "/mesas"
    respuesta = requests.get(url,headers=headers)
    json = respuesta.json()
    return jsonify(json)

@app.route('/mesas', methods=["POST"])
def crear_mesa():
    datosEntrada = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf8"}
    configuracion = cargar_configuracion()
    url = configuracion["url-ms-estructura"] + "/mesas"
    respuesta = requests.post(url,json=datosEntrada,headers=headers)
    json = respuesta.json()
    return jsonify(json)

@app.route("/mesas/<string:id>", methods=['PUT'])
def modificarMesa(id):
    datosEntrada = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    configuracion = cargar_configuracion()
    url = configuracion["url-ms-estructura"] + "/mesas/" + id
    respuesta = requests.put(url, headers=headers, json=datosEntrada)
    json = respuesta.json()
    return jsonify(json)

@app.route("/mesas/<string:id>", methods=['DELETE'])
def eliminarMesa(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    configuracion = cargar_configuracion()
    url = configuracion["url-ms-estructura"] + "/mesas/" + id
    print(url)
    respuesta = requests.delete(url, headers=headers)
    json = respuesta.json()
    return jsonify(json)

##################################################################################

@app.route('/')
def home():
    print("path home")
    return 'API GATEWAY RUNNING . . .'

def cargar_configuracion():
    with open("config.json") as archivo:
        datos_configuracion = json.load(archivo)
    return datos_configuracion


if __name__ == '__main__':
    dataConfig = cargar_configuracion()
    print("Server running : " + "http://" + dataConfig["url-api-gateway"] + ":" + str(dataConfig["puerto-api-gateway"]))
    serve(app, host=dataConfig["url-api-gateway"], port=dataConfig["puerto-api-gateway"])