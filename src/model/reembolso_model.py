from src.model import db
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String, DECIMAL, DATE
from sqlalchemy import func

class Reembolso(db.Model): # Interpreta que essa classe vai ser o modelo para a entidade

    #---------------------ATRIBUTOS--------------------------------
    id = Column(Integer, primary_key True, autoincremente=True)
    colaborador = Column(String(150), nullabel=False)
    empresa = Column(String(50))#os nomes serão abreviados, por isso 50 caracteres
    num_prestacao = Column(Integer)
    descricao = Column(String(255))
    data = Column(DATE, server_default=func.current_date())
    tipo_reembolso = Column(String(35))
    centro_custo = Column(String(50))
    ordem_interna = Column(String(50))
    divisao = Column(String(50))
    pep =Column(String(50))
    moeda = Column(String(20))
    distancia_km = Column(String(50))
    valor_km = Column(String(50))
    valor_faturado = Column(DECIMAL(10,2))#9999999999.11
    despesa = Column(DECIMAL(10,2))

    #----------------------Metodo Construtor-------------------------------------
    def __init__(self):