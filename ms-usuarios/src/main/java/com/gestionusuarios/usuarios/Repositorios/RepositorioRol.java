package com.gestionusuarios.usuarios.Repositorios;

import com.gestionusuarios.usuarios.Modelos.Rol;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface RepositorioRol extends MongoRepository<Rol,String> {
}
