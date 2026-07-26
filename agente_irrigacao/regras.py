def aplicar_regras(amb, temperatura_prevista, umidade_prevista):

    # Regras gerais

    if amb.chuva:
        return "Desligar irrigação"

    if amb.umidade >= 80:
        return "Desligar irrigação"

    if amb.temperatura < 10:
        return "Não irrigar"

    # Regras de horario

    if 12 <= amb.horario <= 15 and umidade_prevista < 30:
        return "Adiar irrigação"

    if 18 <= amb.horario <= 22 and umidade_prevista < 40:
        return "Ligar irrigação"

    if 0 <= amb.horario <= 6 and umidade_prevista < 40:
        return "Ligar irrigação"

    # Regras por cultivo

    # Tomate

    if amb.cultivo == "tomate":

        if umidade_prevista < 35:
            return "Ligar irrigação"

        if umidade_prevista >= 60:
            return "Não irrigar"

    # Alface

    if amb.cultivo == "alface":

        if umidade_prevista < 40:
            return "Ligar irrigação"
               
        if umidade_prevista >= 70:
            return "Não irrigar"

    # Arroz

    if amb.cultivo == "arroz":

        if umidade_prevista < 60:
            return "Ligar irrigação"

    # Milho

    if amb.cultivo == "milho":

        if umidade_prevista < 30:
            return "Ligar irrigação"

    # Mandioca

    if amb.cultivo == "mandioca":

        if umidade_prevista < 20:
            return "Ligar irrigação"

        if umidade_prevista >= 20:
            return "Não irrigar"

    # Cana-de-açúcar

    if amb.cultivo == "cana":

        if umidade_prevista < 35:
            return "Ligar irrigação"

    # Feijão

    if amb.cultivo == "feijao":

        if umidade_prevista < 30:
            return "Ligar irrigação"

    # Soja

    if amb.cultivo == "soja":

        if umidade_prevista < 35:
            return "Ligar irrigação"

    return "Monitorar"