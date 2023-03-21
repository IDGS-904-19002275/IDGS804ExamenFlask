from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user,current_user
from .models import Usuarios,Juegos

from flask import Blueprint,render_template, url_for,redirect,request,flash
from . import db

auth = Blueprint('auth',__name__)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    correo = request.form.get('correo')
    contrasena = request.form.get('contrasena')
    U = Usuarios.query.filter_by(correo=correo).first()

    if not U or not check_password_hash(U.contrasena, contrasena) :
            flash('El usuario o la contraseña son incorrectos')
            return redirect(url_for('auth.login'))
    login_user(U)
    return redirect(url_for('main.profile'))
@auth.route('/singup')
def singup():
    return render_template('singup.html')

@auth.route('/singup', methods=['POST'])
def singup_post():
    correo = request.form.get('correo')
    nombre = request.form.get('nombre')
    contrasena = request.form.get('contrasena')

    user = Usuarios.query.filter_by(correo=correo).first()
    if user:
        flash('Email  en uso')
        return redirect(url_for('auth.singup'))
    
    new_u = Usuarios(
        correo=correo, 
        nombre=nombre,
        rol='mortal',
        contrasena=generate_password_hash(contrasena, method='sha256'))
    db.session.add(new_u)
    db.session.commit()
    return redirect(url_for('auth.login'))

@auth.route('/GaleriaDeProductos')
@login_required
def Galeria():
    juegos = Juegos.query.all()
    return render_template('GaleriaDeProductos.html', juegos = juegos,U=current_user)

@auth.route("/SeccionDeAdministrador", methods=['GET','POST'])
@login_required
def Administrador():
    if request.method == 'POST':

        if request.form.get('accion') == 'update':
            id = request.form.get('id')
            j = db.session.query(Juegos).filter(Juegos.id == id).first()

            j.nombre = request.form.get('nombre'),
            j.precio = request.form.get('precio'),
            j.url = request.form.get('url'),
            j.ano = request.form.get('ano'),
            j.desarrolladora = request.form.get('desarrolladora')
            db.session.add(j)
            db.session.commit()

        if request.form.get('accion') == 'add':
            j = Juegos(nombre = request.form.get('nombre'),precio = request.form.get('precio'),url = request.form.get('url'),ano = request.form.get('ano'),desarrolladora = request.form.get('desarrolladora'))
            db.session.add(j)
            db.session.commit()

    if request.method == 'GET' and request.args.get('id'):
        id = request.args.get('id')
        nuevo_juego = db.session.query(Juegos).filter(Juegos.id == id).first()
        db.session.delete(nuevo_juego)
        db.session.commit()
        
    juegos = Juegos.query.all()
    return render_template('SeccionDeAdministrador.html', juegos=juegos,U=current_user)