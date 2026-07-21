from regras import aplicar_regras

class Agente:

    def decidir(self, ambiente):

        decisao = aplicar_regras(ambiente)

        return decisao