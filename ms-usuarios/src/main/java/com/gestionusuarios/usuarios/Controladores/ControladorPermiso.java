package com.gestionusuarios.usuarios.Controladores;

import com.gestionusuarios.usuarios.Modelos.Permiso;
import com.gestionusuarios.usuarios.Repositorios.RepositorioPermiso;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/permisos")
public class ControladorPermiso {
    @Autowired
    private RepositorioPermiso miRepoPermiso;

    @PostMapping("/crear")
    public Permiso crearPermiso(@RequestBody Permiso permisoEntrada){
        return this.miRepoPermiso.save(permisoEntrada);
    }

    @GetMapping("/listar")
    public List<Permiso> listarPermiso(){
        return this.miRepoPermiso.findAll();
    }

    @DeleteMapping("/eliminar")
    public String eliminarPermiso(@RequestParam(value = "idPermiso") String idPermiso){
        miRepoPermiso.deleteById(idPermiso);
        return "se ha eliminado el permiso con el codigo"+ idPermiso;
    }

    @PutMapping("/actualizar/{id}")
    public String actualizarPermiso(@PathVariable String id,
                                    @RequestBody Permiso permisoEntrada) {
        Permiso permisoConsulta = miRepoPermiso.findById(id).orElse(null);
        permisoConsulta.setUrl(permisoEntrada.getUrl());
        permisoConsulta.setMetodo(permisoEntrada.getMetodo());
        miRepoPermiso.save(permisoConsulta);
        return "el permiso se ha actualizado";}

}