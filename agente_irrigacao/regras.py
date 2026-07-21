def aplicar_regras(amb):

    if amb.chuva:
        return "Desligar irrigação"

    if amb.umidade >= 70:
        return "Desligar irrigação"

    if amb.umidade < 30 and amb.temperatura >= 30:
        return "Ligar irrigação"

    if amb.umidade < 30:
        return "Ligar irrigação"

    return "Nenhuma ação necessária"