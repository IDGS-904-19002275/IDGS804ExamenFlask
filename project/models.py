from flask_login import UserMixin
from . import db

class Juegos(db.Model):
    __tablaname__='juegos'
    id = db.Column(db.Integer, primary_key = True)
    nombre=db.Column(db.String(32))
    precio = db.Column(db.Integer)
    url=db.Column(db.String(999))

    desarrolladora=db.Column(db.String(64))
    ano = db.Column(db.Integer)

class Usuarios(UserMixin,db.Model):
    __tablaname__='usuarios'

    id = db.Column(db.Integer, primary_key = True)
    nombre=db.Column(db.String(32))
    contrasena = db.Column(db.String(256))
    rol=db.Column(db.String(16))
    correo=db.Column(db.String(64))
