from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config


db = SQLAlchemy()            # ORM para manipular o banco de dados
migrate = Migrate()          # Gerenciador de migrações (controle de versão do banco)

def create_app():
    app = Flask(__name__)            # Criação da instância principal da aplicação
    app.config.from_object(Config)   # Carrega as configurações definidas em config.py

    app.json.sort_keys = False       # Evita a ordenação automática de chaves nos JSONs

    db.init_app(app)                 # Inicializa o SQLAlchemy com a aplicação Flask
    migrate.init_app(app, db)       # Associa o Flask-Migrate à aplicação e ao banco

    from .routes.messages import messages_bp
    app.register_blueprint(messages_bp, url_prefix="/messages")

    return app