from regras import aplicar_regras
from machine_learning.prever import (carregar_modelos, prever_condicoes)

class Agente:

    def __init__(self):

        self.modelo_temperatura, self.modelo_umidade = carregar_modelos()

    def decidir(self, ambiente):

        temperatura_prevista, umidade_prevista = prever_condicoes(self.modelo_temperatura,
            self.modelo_umidade, ambiente.dia, ambiente.mes, ambiente.horario, ambiente.temperatura,
            ambiente.umidade)

        decisao, motivo = aplicar_regras(ambiente, temperatura_prevista, umidade_prevista)

        return (decisao, motivo, temperatura_prevista, umidade_prevista)