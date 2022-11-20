package com.gestionusuarios.usuarios.Controladores;

import com.gestionusuarios.usuarios.Modelos.Rol;
import com.gestionusuarios.usuarios.Modelos.Usuario;
import com.gestionusuarios.usuarios.Repositorios.RepositorioRol;
import com.gestionusuarios.usuarios.Repositorios.RepositorioUsuario;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.List;

@RestController
@RequestMapping("/usuarios")
public class ControladorUsuario {
    @Autowired
    private RepositorioUsuario miRepoUsuario;
    @Autowired
    private RepositorioRol miRepoRol;

    /*CRUD*/

    @GetMapping("/listar")
    public List<Usuario> listar() {
        return miRepoUsuario.findAll();
    }

    @PostMapping("/crear")
    public Usuario crearUsuario(@RequestBody Usuario usuarioEntrada) {
        usuarioEntrada.setContrasena(convertirSHA256(usuarioEntrada.getContrasena()));
        return miRepoUsuario.save(usuarioEntrada);
    }

    @DeleteMapping("/eliminar")
    public String eliminarUsuario(@RequestParam(value = "idUsuario") String idUsuario) {
        miRepoUsuario.deleteById(idUsuario);
        return "Usuario " + idUsuario + " eliminado";
    }

    @PutMapping("/actualizar/{idUsuario}")
    public String actualizarUsuario(@PathVariable String idUsuario,
                                    @RequestBody Usuario usuarioEntrada) {
        Usuario usuarioConsulta = miRepoUsuario.findById(idUsuario).orElse(null);
        usuarioConsulta.setNombre_usuario(usuarioEntrada.getNombre_usuario());
        usuarioConsulta.setCorreo(usuarioEntrada.getCorreo());
        usuarioConsulta.setContrasena(convertirSHA256(usuarioEntrada.getContrasena()));
        usuarioConsulta.setNombre(usuarioEntrada.getNombre());
        usuarioConsulta.setApellido(usuarioEntrada.getApellido());
        usuarioConsulta.setCiudad(usuarioEntrada.getCiudad());
        usuarioConsulta.setTelefono(usuarioEntrada.getTelefono());
        usuarioConsulta.setCedula(usuarioEntrada.getCedula());
        miRepoUsuario.save(usuarioConsulta);

        return "Usuario " + idUsuario + " actualizado";
    }

    /*ASIGNAR ROL*/

    @PutMapping("/{idUsuario}/rol/{idRol}")
    public String asignarRol(@PathVariable String idUsuario,
                             @PathVariable String idRol) {
        Usuario usuarioConsulta = miRepoUsuario.findById(idUsuario).orElse(null);
        Rol rolConsulta = miRepoRol.findById(idRol).orElse(null);
        usuarioConsulta.setRol(rolConsulta);
        miRepoUsuario.save(usuarioConsulta);
        return "Usuario " + idUsuario + " actualizado";
    }

    /*ENCRIPTAR CONTRASEÑA*/

    public String convertirSHA256(String password) {
        MessageDigest md = null;
        try {
            md = MessageDigest.getInstance("SHA-256");
        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
            return null;
        }
        byte[] hash = md.digest(password.getBytes());
        StringBuffer sb = new StringBuffer();
        for (byte b : hash) {
            sb.append(String.format("%02x", b));
        }
        return sb.toString();
    }

    /*LOGIN*/

    @PostMapping("/login")
    public Usuario iniciarSesion(@RequestBody Usuario usuarioEntrada,
                                 HttpServletResponse codigoRespuestaHttp) throws IOException {
        String correo = usuarioEntrada.getCorreo();
        Usuario usuarioConsulta = miRepoUsuario.buscarUsuarioXCorreo(correo);
        if (usuarioConsulta != null && usuarioConsulta.getContrasena().equals(convertirSHA256(usuarioEntrada.getContrasena()))) {
            System.out.println("Inicio de sesion exitoso");
            usuarioConsulta.setContrasena("");
            return usuarioConsulta;
        } else {
            System.out.println("Datos incorrectos");
            codigoRespuestaHttp.sendError(HttpServletResponse.SC_UNAUTHORIZED);
            return null;
        }
    }
}
