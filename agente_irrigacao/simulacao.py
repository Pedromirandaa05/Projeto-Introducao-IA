from ambiente import Ambiente
from agente import Agente

agente = Agente()

casos = [
    Ambiente(20, 35, False, 19, "tomate"),
    Ambiente(45, 25, False, 10, "alface"),
    Ambiente(15, 32, False, 13, "milho"),
    Ambiente(25, 30, False, 9, "mandioca"),
    Ambiente(70, 22, True, 11, "arroz")
]

# Testa cada cenário
for i, ambiente in enumerate(casos, start=1):

    acao = agente.decidir(ambiente)

    print(f"\nCASO {i}")
    print(f"Cultura: {ambiente.cultivo}")
    print(f"Umidade: {ambiente.umidade}%")
    print(f"Temperatura: {ambiente.temperatura}°C")
    print(f"Horário: {ambiente.horario}:00")
    print(f"Chuva: {'Sim' if ambiente.chuva else 'Não'}")

    print(f"\nDecisão: {acao}")