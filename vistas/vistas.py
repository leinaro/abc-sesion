from flask import request
from sqlalchemy.exc import SQLAlchemyError
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from flask_restful import Resource
import hashlib
from datetime import datetime
from sqlalchemy.orm import joinedload
import random

from modelos import (
    db,
    Usuario,
    UsuarioSchema,
    Rol,
)

usuario_schema = UsuarioSchema()

class VistaRegistro(Resource):
    def post(self):
        usuario = Usuario.query.filter(
            Usuario.usuario == request.json["usuario"]
        ).first()
        if usuario is None:
            contrasena_encriptada = hashlib.md5(
                request.json["contrasena"].encode("utf-8")
            ).hexdigest()
            nuevo_usuario = Usuario(
                usuario=request.json["usuario"],
                contrasena=contrasena_encriptada,
                rol=request.json["rol"],
            )
            db.session.add(nuevo_usuario)
            db.session.commit()
            return {"mensaje": "usuario creado exitosamente", "id": nuevo_usuario.id}
        else:
            return "El usuario ya existe", 404
        
class VistaAutenticacion(Resource):
    def post(self):
        contrasena_encriptada = hashlib.md5(
            request.json["contrasena"].encode("utf-8")
        ).hexdigest()
        usuario = Usuario.query.filter(
            Usuario.usuario == request.json["usuario"],
            Usuario.contrasena == contrasena_encriptada,
        ).first()
        db.session.commit()
        if usuario is None:
            return "El usuario no existe", 404
        else:
            token_de_acceso = create_access_token(identity=usuario.id)
            return {
                "mensaje": "Inicio de sesión exitoso",
                "token": token_de_acceso,
                "id": usuario.id,
                "rol": usuario.rol.name,
            }

class VistaAutorizacion(Resource):
    @jwt_required()
    def get(self):
        usuario = Usuario.query.filter(
            Usuario.id == get_jwt_identity()
        ).first()

        if usuario is None:
            return "El usuario no existe", 404
        if usuario.rol != Rol.EMPRESA:
            return "El usuario no tiene permisos", 401

        return { "mensaje": get_jwt_identity()}
        
