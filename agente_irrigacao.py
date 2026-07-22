# ==========================================================
# LÓGICA DO AGENTE DE IRRIGAÇÃO
# Baseado em Agentes e Ambientes (PEAS)
# ==========================================================

import random
import statistics

"""
Performance : manter solo saudável e economizar água
Environment : jardim/plantação; parcialmente observável e não-determinístico
Actuators   : ligar/desligar sistema de irrigação
Sensors     : temperatura, umidade do solo, umidade do ar, previsão de chuva
Tipo        : agente reativo simples baseado em regras
"""

LIMIARES = {
    "umidade_solo": 30,
    "temp_alta": 30
}


def gerar_dado_sensor():
    """Gera uma leitura simulada de sensores para um dia."""
    return {
        "temperatura": round(random.uniform(-5, 45), 1),
        "umidade_solo": round(random.uniform(0, 100), 1),
        "umidade_ar": round(random.uniform(0, 100), 1),
        "previsao_chuva": random.random() < 0.3
    }


def decidir_irrigacao(dados, limiar_umidade_solo=30, limiar_temp_alta=30):
    """Retorna (True/False, motivo) para ligar ou não a irrigação."""
    if dados["previsao_chuva"]:
        return False, "Chuva prevista - irrigação não necessária"

    if dados["umidade_solo"] < limiar_umidade_solo:
        return True, f"Solo seco ({dados['umidade_solo']}% < {limiar_umidade_solo}%)"

    if dados["temperatura"] > limiar_temp_alta and dados["umidade_solo"] < 50:
        return True, f"Calor intenso ({dados['temperatura']}°C) com solo moderadamente seco"

    return False, "Condições adequadas - sem necessidade de irrigar"


def simular(dias=30):
    """Roda o agente por N dias simulados e retorna o histórico."""
    historico = []
    for dia in range(1, dias + 1):
        dados = gerar_dado_sensor()
        ligou, motivo = decidir_irrigacao(
            dados,
            limiar_umidade_solo=LIMIARES["umidade_solo"],
            limiar_temp_alta=LIMIARES["temp_alta"]
        )
        historico.append({"dia": dia, **dados, "irrigou": ligou, "motivo": motivo})
    return historico


def avaliar(historico):
    """Calcula estatísticas simples do histórico simulado."""
    total_dias = len(historico)
    dias_irrigados = sum(1 for d in historico if d["irrigou"])
    dias_com_chuva = sum(1 for d in historico if d["previsao_chuva"])
    media_umidade_solo = statistics.mean(d["umidade_solo"] for d in historico)
    return {
        "total_dias": total_dias,
        "dias_irrigados": dias_irrigados,
        "dias_com_chuva": dias_com_chuva,
        "media_umidade_solo": media_umidade_solo
    }