from flask import Blueprint
from . import db
from flask import Blueprint, Flask, render_template
from flask_login import login_required, current_user


main = Blueprint('main',__name__)

@main.route('/')
def index():
    return render_template('PaginaPrincipal.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.nombre)


@main.route("/Contacto")
def Contacto(): return render_template('Contacto.html')


