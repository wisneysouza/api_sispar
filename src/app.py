#responsavel pela criação da aplicação
# creat_app() -> vai confuigurar a instancia do flask

from flask import Flask
from src.controller.colaborador_controller import bp_colaborador
from src.controller.reembolso_controller import bp_reembolso
from src.model import db
from config import Config
from flask_cors import CORS
from flasgger import Swagger 
from src.security.security import bcrypt

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
    app.config['DEBUG'] = True # <-- Habilita o modo debug
    bcrypt.init_app(app)
    app.register_blueprint(bp_colaborador)
    app.register_blueprint(bp_reembolso) # Registra o blueprint -> reembolso
    app.config.from_object(Config)
    db.init_app(app)

    Swagger(app, config=swagger_config)  # Inicializa o Swagger com a configuração definida
    print("Rotas disponíveis:")
    for rule in app.url_map.iter_rules():
        print(f"{rule.methods} {rule}")
    with app.app_context():
        db.create_all()
    return app