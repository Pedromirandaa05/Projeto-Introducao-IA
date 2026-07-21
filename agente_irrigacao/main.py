from ambiente import Ambiente
from agente import Agente

print("===== Sistema Inteligente de Irrigação =====")

umidade = float(input("Umidade do solo (%): "))
temperatura = float(input("Temperatura (°C): "))

chuva = input("Está chovendo? (sim/nao): ")

if chuva.lower() == "sim":
    chuva = True
else:
    chuva = False

ambiente = Ambiente(
    umidade,
    temperatura,
    chuva
)

agente = Agente()

decisao = agente.decidir(ambiente)

print("\nDecisão do agente:")
print(decisao)