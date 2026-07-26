import pandas as pd
from pathlib import Path
from joblib import load

BASE_DIR = Path(__file__).resolve().parent.parent

def carregar_modelos():

    modelo_temperatura = load(BASE_DIR / "machine_learning" / "modelo_temperatura.pkl")

    modelo_umidade = load(BASE_DIR / "machine_learning" / "modelo_umidade.pkl")

    return modelo_temperatura, modelo_umidade

def prever_condicoes(modelo_temperatura, modelo_umidade, dia, mes, hora, temperatura, umidade):
    entrada = pd.DataFrame({"Dia": [dia], "Mes": [mes], "Hora": [hora],"Temperatura": [temperatura],
    "Umidade": [umidade]})

    temperatura_prevista = modelo_temperatura.predict(entrada)[0]

    umidade_prevista = modelo_umidade.predict(entrada)[0]

    return temperatura_prevista, umidade_prevista

def main():

    modelo_temperatura, modelo_umidade = carregar_modelos()

    temperatura_prevista, umidade_prevista = prever_condicoes(modelo_temperatura, modelo_umidade,
        dia=15, mes=7, hora=14, temperatura=30, umidade=45)

    print(f"Temperatura prevista: {temperatura_prevista:.1f} °C")
    print(f"Umidade prevista: {umidade_prevista:.1f} %")


if __name__ == "__main__":
    main()