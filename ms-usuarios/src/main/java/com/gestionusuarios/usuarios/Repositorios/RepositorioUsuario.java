package com.gestionusuarios.usuarios.Repositorios;

import com.gestionusuarios.usuarios.Modelos.Usuario;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.mongodb.repository.Query;

public interface RepositorioUsuario extends MongoRepository<Usuario,String> {

    @Query("{'correo': ?0}")
    public Usuario buscarUsuarioXCorreo(String correo);
}
