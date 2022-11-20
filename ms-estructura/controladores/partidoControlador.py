from modelos.partido import Partido
from repositorios.repositorioPartido import RepositorioPartido

class PartidoControlador():
  def __init__(self):
    self._repositorio_partido = RepositorioPartido()
  
  def listar_partido(self):
    datos_partido =  self._repositorio_partido.findAll()
    return datos_partido 

  def crear_partido(self,datos_entrada):
    _partido = Partido(datos_entrada)
    return self._repositorio_partido.save(_partido)

  def eliminar_partido(self,id):
    return self._repositorio_partido.delete(id)
    
  def actualizar_partido(self,id,datos_entrada): 
    _partido_bd = self._repositorio_partido.findById(id)
    _partido_obj = Partido(_partido_bd)
    _partido_obj.nombre_partido = datos_entrada["nombre_partido"] 
    
    return self._repositorio_partido.save(_partido_obj)