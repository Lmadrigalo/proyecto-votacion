from flask import Flask
from flask import request
from flask import jsonify
from waitress import serve
import json
from controladores.candidatoControlador import CandidatoControlador
from controladores.partidoControlador import PartidoControlador
from controladores.mesaControlador import MesaControlador

mi_aplicacion = Flask(__name__)

#instanciar un objeto de tipo controlador de candidato
_controlador_candidato = CandidatoControlador()
_controlador_partido = PartidoControlador()
_controlador_mesa = MesaControlador()

##########################################################################################
##########################################################################################

"""PATH PARA ADMINISTRAR CANDIDATOS"""
#GET - LISTAR
@mi_aplicacion.route('/candidatos',methods=['GET'])
def listar_candidato():
  datos_salida = _controlador_candidato.listar_candidato()
  return jsonify(datos_salida)

#POST - CREAR
@mi_aplicacion.route('/candidatos',methods=['POST'])
def crear_candidato():
  datos_entrada = request.get_json()
  datos_salida  = _controlador_candidato.crear_candidato(datos_entrada)
  return jsonify(datos_salida)
  
#DELETE - ELIMINAR
@mi_aplicacion.route('/candidatos/<string:id>',methods=['DELETE'])
def eliminar_candidato(id):
  datos_salida =  _controlador_candidato.eliminar_candidato(id)
  return jsonify(datos_salida)

#PUT - ACTUALIZAR
@mi_aplicacion.route("/candidatos/<string:id>",methods=['PUT']) 
def actualizar_candidato(id):
    datos_entrada = request.get_json()
    json=_controlador_candidato.actualizar_candidato(id,datos_entrada)
    return jsonify(json)
    
##########################################################################################
##########################################################################################

"""PATH PARA ADMINISTRAR PARTIDOS"""
#GET - LISTAR
@mi_aplicacion.route('/partidos',methods=['GET'])
def listar_partido():
  datos_salida = _controlador_partido.listar_partido()
  return jsonify(datos_salida)

#POST - CREAR
@mi_aplicacion.route('/partidos',methods=['POST'])
def crear_partido():
  datos_entrada = request.get_json()
  datos_salida  = _controlador_partido.crear_partido(datos_entrada)
  return jsonify(datos_salida)
  
#DELETE - ELIMINAR
@mi_aplicacion.route('/partidos/<string:id>',methods=['DELETE'])
def eliminar_partido(id):
  datos_salida =  _controlador_partido.eliminar_partido(id)
  return jsonify(datos_salida)

#PUT - ACTUALIZAR
@mi_aplicacion.route("/partidos/<string:id>",methods=['PUT']) 
def actualizar_partido(id):
    datos_entrada = request.get_json()
    json=_controlador_partido.actualizar_partido(id,datos_entrada)
    return jsonify(json)

##########################################################################################
##########################################################################################

"""PATH PARA ADMINISTRAR MESAS"""
#GET - LISTAR
@mi_aplicacion.route('/mesas',methods=['GET'])
def listar_mesa():
  datos_salida = _controlador_mesa.listar_mesa()
  return jsonify(datos_salida)

#POST - CREAR
@mi_aplicacion.route('/mesas',methods=['POST'])
def crear_mesa():
  datos_entrada = request.get_json()
  datos_salida  = _controlador_mesa.crear_mesa(datos_entrada)
  return jsonify(datos_salida)

#POST - ELIMINAR
@mi_aplicacion.route('/mesas/<string:id>',methods=['DELETE'])
def eliminar_mesa(id):
  datos_salida =  _controlador_mesa.eliminar_mesa(id)
  return jsonify(datos_salida)

#PUT - ACTUALIZAR
@mi_aplicacion.route("/mesas/<string:id>",methods=['PUT']) 
def actualizar_mesa(id):
    datos_entrada = request.get_json()
    json=_controlador_mesa.actualizar_mesa(id,datos_entrada)
    return jsonify(json)

#########################################################################################
#########################################################################################

def cargar_configuracion():
  with open("config.json") as archivo:
    datos_configuracion = json.load(archivo)
  return datos_configuracion

if __name__ == '__main__':
  datos_configuracion = cargar_configuracion()
  print("servidor ejecutandose...","http://"+datos_configuracion["servidor"]+":"+datos_configuracion["puerto"])
  serve(mi_aplicacion, host=datos_configuracion["servidor"], port=datos_configuracion["puerto"])