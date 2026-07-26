from ambiente import Ambiente
from agente import Agente


def main():

    agente = Agente()

    casos = [
        Ambiente(10, 1, 20, 35, False, 19, "tomate"),
        Ambiente(18, 3, 45, 25, False, 10, "alface"),
        Ambiente(22, 7, 15, 32, False, 13, "milho"),
        Ambiente(5, 9, 25, 30, False, 9, "mandioca"),
        Ambiente(28, 11, 70, 22, True, 11, "arroz")
    ]

    for i, ambiente in enumerate(casos, start=1):

        decisao, motivo, temp_prevista, umid_prevista = agente.decidir(ambiente)

        print(f"CASO {i}")

        print(f"Cultivo: {ambiente.cultivo.capitalize()}")
        print(f"Data: {ambiente.dia:02d}/{ambiente.mes:02d}")
        print(f"Horário: {ambiente.horario}:00")
        print(f"Temperatura atual: {ambiente.temperatura:.1f} °C")
        print(f"Umidade atual: {ambiente.umidade:.1f}%")
        print(f"Chuva: {'Sim' if ambiente.chuva else 'Não'}")

        print("\nPrevisão para +2 horas")
        print(f"Temperatura prevista: {temp_prevista:.1f} °C")
        print(f"Umidade prevista: {umid_prevista:.1f}%")

        print("\nDecisão do agente")
        print(f"Ação: {decisao}")
        print(f"Motivo: {motivo}")

        print()


if __name__ == "__main__":
    main()