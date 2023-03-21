import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import urllib
from flask_login import LoginManager
from flask_wtf import CSRFProtect
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    csrf = CSRFProtect()
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.urandom(24)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@127.0.0.1/pylogin'

    db.init_app(app)
    csrf.init_app(app)
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    from .models import Usuarios

    @login_manager.user_loader
    def load_user(user_id): return Usuarios.query.get(int(user_id))


# rutan aunth
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    
# rutan no aunth
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app