from modelos.mesa import Mesa
from repositorios.repositorioMesa import RepositorioMesa

class MesaControlador():
  def __init__(self):
    self._repositorio_mesa = RepositorioMesa()
  
  def listar_mesa(self):
    datos =  self._repositorio_mesa.findAll()
    return datos 

  def crear_mesa(self,datos_entrada):
    _mesa = Mesa(datos_entrada)
    return self._repositorio_mesa.save(_mesa)

  def eliminar_mesa(self,id):
    return self._repositorio_mesa.delete(id)
    
  def actualizar_mesa(self,id,datos_entrada): 
    _mesa_bd = self._repositorio_mesa.findById(id)
    _mesa_obj = Mesa(_mesa_bd)
    _mesa_obj.numero_mesa = datos_entrada["numero_mesa"]
    _mesa_obj.ciudad = datos_entrada["ciudad"]    
    
    return self._repositorio_mesa.save(_mesa_obj)