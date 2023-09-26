import enum
from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


db = SQLAlchemy()

class Rol(enum.Enum):
    EMPRESA = 1
    CANDIDATO = 2

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(128))
    contrasena = db.Column(db.String(50))
    rol = db.Column(db.Enum(Rol))

class UsuarioSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Usuario
        include_relationships = True
        load_instance = True

    id = fields.String()
    rol = fields.String()