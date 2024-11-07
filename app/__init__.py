from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# Instanciar as extensões
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()

def create_app(config_class='app.config.Config'):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Inicializar as extensões
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    
    # Definir a pasta de sessões
    app.config['SESSION_TYPE'] = 'filesystem'
    Session(app)
    
    # Importar as rotas
    from .routes import main
    app.register_blueprint(main)
    
    return app
