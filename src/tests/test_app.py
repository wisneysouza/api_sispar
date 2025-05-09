import pytest # traz a biblioteca de testes
from src.app import create_app
from src.model.colaborador_model import Colaborador
import time #manipular o tempo


# -----------------------------CONFIGURAÇÕES ------------------------------

@pytest.fixture # configurar os testes
def app():
    app = create_app()
    yield app #Armazenar o valor em memoria / é uma variavel global que vai ser auto destruida, para não consukir espaço, otimizabdo o codigo.

@pytest.fixture # configura nossos testes de requisição
def client(app):
    return app.test_client()

    #-------------------------------------------------------------------

def test_pegar_todos_colaboradores(client): # assim como o arquivo tem que começar com teste, as unçoes tem que começar com test.
    resposta = client.get('/colaborador/todos-colaboradores')

    assert resposta.status_code == 200
    assert  isinstance(resposta.json, list)

def test_desempenho_requisicao_get(client):
    comeco = time.time() # pega a hora atual e transforma em segundos

    for _ in range (100): # _ omitir a variavel auxiliar
        resposta = client.get('/colaborador/todos-colaboradores')

    fim = time.time() - comeco

    assert fim < 0.2 # segundos