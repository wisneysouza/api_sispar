#responsavel pela criação da aplicação
# creat_app() -> vai confuigurar a instancia do flask

from flask import Flask
from src.controller.colaborador_controller import bp_colaborador
from src.model import db
from config import Config
from flask_cors import CORS
from flasgger import Swagger 

swagger_config = {
    "headers": [],
    "specs":[
        {
            "endpoint": 'apispec', # referencia da api
            "route": '/apispec.json/',
            "rule_filter": lambda rule:True, # < indica que todas as rotas vão estar na documentação
            "model_filter": lambda tag: True, #< entidades que serão mostradas
        }
    ],
    "static_url_path": "/flasgger_static", #ira trazer o que voce tem padronizado na sua estilização, para a funcionalidade
    "swagger_ui": True,
    "specs_route": "/apidocs/"
}

def create_app():
    app = Flask(__name__)
    CORS(app, origins="*")#NUNCA COLOCAR O * EM CORS
    # <-- Adicione a autorização do cors para todas as rotas na aplicação.
    app.register_blueprint(bp_colaborador)
    app.config.from_object(Config)
    db.init_app(app)

    Swagger(app, config=swagger_config)

    with app.app_context():
        db.create_all()
    return app