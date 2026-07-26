def aplicar_regras(amb, temperatura_prevista, umidade_prevista):

    if amb.chuva:
        return (
            "Desligar irrigação",
            "Foi detectada chuva."
        )

    if amb.umidade >= 80:
        return (
            "Desligar irrigação",
            "A umidade atual é superior a 80%."
        )

    if amb.temperatura < 10:
        return (
            "Não irrigar",
            "A temperatura atual é inferior a 10°C."
        )

    if temperatura_prevista > 35:
        return (
            "Adiar irrigação",
            "A temperatura prevista para as próximas 2 horas é superior a 35°C."
        )

    if 12 <= amb.horario <= 15 and umidade_prevista < 30:
        return (
            "Adiar irrigação",
            "Horário de maior insolação e baixa umidade prevista."
        )

    if 18 <= amb.horario <= 22 and umidade_prevista < 40:
        return (
            "Ligar irrigação",
            "Horário adequado e baixa umidade prevista."
        )

    if 0 <= amb.horario <= 6 and umidade_prevista < 40:
        return (
            "Ligar irrigação",
            "Período noturno com baixa umidade prevista."
        )

    # Tomate
    if amb.cultivo == "tomate":

        if umidade_prevista < 35:
            return (
                "Ligar irrigação",
                "A umidade prevista para tomate é inferior a 35%."
            )

        if umidade_prevista >= 60:
            return (
                "Não irrigar",
                "A umidade prevista para tomate é igual ou superior a 60%."
            )

    # Alface
    if amb.cultivo == "alface":

        if umidade_prevista < 40:
            return (
                "Ligar irrigação",
                "A umidade prevista para alface é inferior a 40%."
            )

        if umidade_prevista >= 70:
            return (
                "Não irrigar",
                "A umidade prevista para alface é igual ou superior a 70%."
            )

    # Arroz
    if amb.cultivo == "arroz":

        if umidade_prevista < 60:
            return (
                "Ligar irrigação",
                "A umidade prevista para arroz é inferior a 60%."
            )

    # Milho
    if amb.cultivo == "milho":

        if umidade_prevista < 30:
            return (
                "Ligar irrigação",
                "A umidade prevista para milho é inferior a 30%."
            )

    # Mandioca
    if amb.cultivo == "mandioca":

        if umidade_prevista < 20:
            return (
                "Ligar irrigação",
                "A umidade prevista para mandioca é inferior a 20%."
            )

        return (
            "Não irrigar",
            "A umidade prevista para mandioca é adequada."
        )

    # Cana-de-açúcar
    if amb.cultivo == "cana":

        if umidade_prevista < 35:
            return (
                "Ligar irrigação",
                "A umidade prevista para cana-de-açúcar é inferior a 35%."
            )

    # Feijão
    if amb.cultivo == "feijao":

        if umidade_prevista < 30:
            return (
                "Ligar irrigação",
                "A umidade prevista para feijão é inferior a 30%."
            )

    # Soja
    if amb.cultivo == "soja":

        if umidade_prevista < 35:
            return (
                "Ligar irrigação",
                "A umidade prevista para soja é inferior a 35%."
            )

    return (
        "Monitorar",
        "Nenhuma regra de irrigação foi acionada."
    )