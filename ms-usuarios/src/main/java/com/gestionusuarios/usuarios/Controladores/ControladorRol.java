package com.gestionusuarios.usuarios.Controladores;

import com.gestionusuarios.usuarios.Modelos.Rol;
import com.gestionusuarios.usuarios.Repositorios.RepositorioRol;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/roles")
public class ControladorRol {
    @Autowired
    private RepositorioRol miRepoRol;

    @GetMapping("/listar")
    public List<Rol> listar(){
        return miRepoRol.findAll();
    }

    @PostMapping("/crear")
    public Rol crearRol(@RequestBody Rol rolEntrada){
        return miRepoRol.save(rolEntrada);
    }

    @DeleteMapping("/eliminar")
    public String eliminarRol(@RequestParam(value = "idRol") String _idRol){
        miRepoRol.deleteById(_idRol);
        return "Rol " + _idRol + " eliminado";}

    @PutMapping("/actualizar/{id}")
    public String actualizarRol(@PathVariable String id, @RequestBody Rol rol){
        Rol  rolConsulta = miRepoRol.findById(id).orElse(null);
        rolConsulta.setNombre(rol.getNombre());
        rolConsulta.setDescripcion(rol.getDescripcion());
        miRepoRol.save(rolConsulta);
        return "SE ACTUALIZÓ UN ROL";}

}
