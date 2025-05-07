
from flask import Blueprint, request, jsonify
#request é um recurso do flak, trabalha com  as requisições
#jsonify e um retorno, responsavel por transformar os dados em json e envia o status cold ex 404, 504 e etc.
from src.model.colaborador_model import Colaborador
from src.model import db
import src.security.security
from flasgger import swag_from

bp_colaborador = Blueprint('colaborador', __name__, url_prefix= '/colaborador')


@bp_colaborador.route('/todos-colaboradores')
def pegar_dados_todos_colaboradores():

    colaboradores = db.session.execute(
        db.select(Colaborador)
        ).scalars().all()
    #                   Expressão                  item           iteravel
    colaboradores = [colaborador.all_data() for colaborador in colaboradores]

    return jsonify(colaboradores), 200

@bp_colaborador.route('/cadastrar', methods=['POST'])
@swag_from('../docs/colaborador/cadastrar_colaborador.yml')
def cadastrar_novo_colaborador():
    dados_requisicao = request.get_json()

    novo_colaborador = Colaborador(

        nome= dados_requisicao['nome'],
        email=dados_requisicao['email'],
        senha= dados_requisicao['senha'],
        cargo= dados_requisicao['cargo'],
        salario= dados_requisicao['salario']
    )

    #INSERT INTO tb_colaborador (nome, email, senha, cargo, salario )
    db.session.add(novo_colaborador)
    db.session.commit()

    return jsonify( {'mensagem': 'Colaborador cadastrado com sucesso'}), 201


#sinaliza que os dados enviados
# endereco