package com.gestionusuarios.usuarios.Repositorios;

import com.gestionusuarios.usuarios.Modelos.Rol;
import com.gestionusuarios.usuarios.Modelos.RolPermiso;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.mongodb.repository.Query;

public interface RepositorioRolPermiso extends MongoRepository<RolPermiso,String> {

    @Query("{\"rol.$id\": ObjectId(?0),\"permiso.$id\": ObjectId(?1)}")
    public RolPermiso consultarRolPermiso(String idRol, String idPermiso);
}
