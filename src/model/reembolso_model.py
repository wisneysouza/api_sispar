from src.model import db
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, String, DECIMAL, DATE
from sqlalchemy import func

class Reembolso(db.Model): # Interpreta que essa classe vai ser o modelo para a entidade

    #---------------------ATRIBUTOS--------------------------------
    id = Column(Integer, primary_key True, autoincremente=True)
    colaborador = Column(String(150), nullabel=False)
    empresa = Column(String(50), nullable=False)#os nomes serão abreviados, por isso 50 caracteres
    num_prestacao = Column(Integer, nullable=False)
    descricao = Column(String(255))
    data = Column(DATE, server_default=func.current_date(), nullable=False)
    tipo_reembolso = Column(String(35), nullable=False)
    centro_custo = Column(String(50), nullable = False)
    ordem_interna = Column(String(50))
    divisao = Column(String(50))
    pep =Column(String(50))
    moeda = Column(String(20), nullable=False)
    distancia_km = Column(String(50))
    valor_km = Column(String(50))
    valor_faturado = Column(DECIMAL(10,2), nullable=False)#9999999999.11
    despesa = Column(DECIMAL(10,2))
    id_colaborador = Column(Integer, ForeignKey(Column='colaborador.id'))
    status = Column(String(25))

    #----------------------Metodo Construtor-------------------------------------
    def __init__(self, colaborador, empresa, num_prestação, descricao, data, tipo_reembolso, centro_custo, ordem_interna, divisao, pep, moeda, distancia_km, valor_km, valor_faturado, despesa, id_colabolador, status='Em analise'):
        self.colaborador = colaborador
        self.empresa = empresa
        self.num_prestacao = num_prestação
        self.descricao = descricao
        self.data = data
        self.tipo_reembolso = tipo_reembolso
        self.centro_custo = centro_custo
        self.ordem_interna = ordem_interna
        self.divisao = divisao
        self.pep = pep
        self.moeda = moeda
        self.distancia_km = distancia_km
        self.valor_km = valor_km
        self.valor_faturado = valor_faturado
        self.despesa = despesa
        self.id_colaborador = id_colabolador
        self.status = status