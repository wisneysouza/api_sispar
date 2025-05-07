from os import environ # traz para o arquivo o acecsso para as variaveis ded ambiente
from dotenv import load_dotenv #traz a funçao para carregar as b=variaveis ded ambiente nesse arquivo

load_dotenv() #Carrega as variaveis de ambiente para este arquivo

class Config():
    SQLALCHEMY_DATABASE_URI = environ.get('URL_DATABASE_PROD')
    SQLALCHEMY_TRACK_MODIFICATIONS = False #Evita carregamento desnecessario

    