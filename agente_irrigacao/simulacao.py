from ambiente import Ambiente
from agente import Agente

agente = Agente()

casos = [
    Ambiente(10, 1, 20, 35, False, 19, "tomate"),
    Ambiente(18, 3, 45, 25, False, 10, "alface"),
    Ambiente(22, 7, 15, 32, False, 13, "milho"),
    Ambiente(5, 9, 25, 30, False, 9, "mandioca"),
    Ambiente(28, 11, 70, 22, True, 11, "arroz")
]

# Testa cada cenário
for i, ambiente in enumerate(casos, start=1):

    acao, motivo, temp_prevista, umid_prevista = agente.decidir(ambiente)

    print(f"\nPrevisão para +2h:")
    print(f"Temperatura prevista: {temp_prevista:.1f}°C")
    print(f"Umidade prevista: {umid_prevista:.1f}%")

    print(f"Decisão: {acao}")
    print(f"Motivo: {motivo}")