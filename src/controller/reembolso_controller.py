from flask import Blueprint, request, jsonify
from src.model.reembolso_model import Reembolso
from src.model import db
from flasgger import swag_from


bp_reembolso = Blueprint('reembolso', __name__, url_prefix= '/reembolso')

@bp_reembolso.route('/reembolso')
def pegar_todos_reembolso():

    reembolso = db.session.execute(
        db.select(Reembolso)
    ).scalars().all()

    reembolso = [reembolso.all_data() for reembolso in reembolso]

    return jsonify(reembolso), 200

@bp_reembolso.route('/solicitacao', methods=['POST'])
@swag_from('../docs/reembolso/solitacao_reembolso.yml')
def solicitar_novo_reembolso():
    dados_requisicao = request.get_json()

    nova_solicitacao = Reembolso(

        id= dados_requisicao['id'],
        colaborador = dados_requisicao['colaborador'],
        empresa = dados_requisicao['empresa'],
        num_prestacao = dados_requisicao['num_prestação'],
        descricao = dados_requisicao['descricao'],
        data= dados_requisicao['data'],
        tipo_reembolso= dados_requisicao['dados_requisicao'],
        centro_custo= dados_requisicao['centro_custo'],
        ordem_interna= dados_requisicao['ordem_interna'],
        divisao= dados_requisicao['divisao'],
        pep= dados_requisicao['pep'],
        moeda= dados_requisicao['moeda'],
        distancia_km= dados_requisicao['distancia_km'],
        valor_km= dados_requisicao['valor_km'],
        valor_faturado= dados_requisicao['valor_faturado'],
        despesa= dados_requisicao['despesa'],
        id_colabolador= dados_requisicao ['id_colabolador'],
        status= dados_requisicao ['status']
    )

    db.session.add(nova_solicitacao)
    db.session.commit

    return jsonify({'mensagem': 'solicitação cadastrada com sucesso'}),201



