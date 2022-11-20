from modelos.candidato import Candidato
from repositorios.repositorioCandidato import RepositorioCandidato

class CandidatoControlador():
  def __init__(self):
    self._repositorio_candidato = RepositorioCandidato()
  
  def listar_candidato(self):
    datos_candidato =  self._repositorio_candidato.findAll()
    return datos_candidato 

  def crear_candidato(self,datos_entrada):
    _candidato = Candidato(datos_entrada)
    return self._repositorio_candidato.save(_candidato)

  def eliminar_candidato(self,id):
    return self._repositorio_candidato.delete(id)
    
  def actualizar_candidato(self,id,datos_entrada): 
    _candidato_bd = self._repositorio_candidato.findById(id)
    _candidato_obj = Candidato(_candidato_bd)
    _candidato_obj.nombre = datos_entrada["nombre"]
    _candidato_obj.apellido = datos_entrada["apellido"]
    _candidato_obj.partido = datos_entrada["partido"]
    _candidato_obj.ciudad = datos_entrada["ciudad"]    
    
    return self._repositorio_candidato.save(_candidato_obj)