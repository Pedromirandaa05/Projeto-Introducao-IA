
import math
import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

BASE_DIR = Path(__file__).resolve().parent.parent

def carregar_dados():
    arquivo = BASE_DIR / "dados" / "dados_tratados.csv"

    dados = pd.read_csv(arquivo)

    return dados

def dividir_dados(dados):

    X = dados[["Dia", "Mes", "Hora", "Temperatura", "Umidade"]]

    y_temperatura = dados["Temperatura_2h"]

    y_umidade = dados["Umidade_2h"]

    X_train, X_test, y_temp_train, y_temp_test = train_test_split(
        X, y_temperatura, test_size=0.2, shuffle=False
        )

    X_train, X_test, y_umid_train, y_umid_test = train_test_split(
        X, y_umidade, test_size=0.2, shuffle=False
        )

    return (X_train, X_test, y_temp_train, y_temp_test, y_umid_train, y_umid_test)

def treinar_modelo(X_train, y_train):

    modelo = DecisionTreeRegressor(random_state=42, max_depth=10)

    modelo.fit(X_train, y_train)

    return modelo

def avaliar_modelo(y_real, y_previsto):

    mae = mean_absolute_error(
        y_real,
        y_previsto
    )

    rmse = math.sqrt(
        mean_squared_error(
            y_real,
            y_previsto
        )
    )

    r2 = r2_score(
        y_real,
        y_previsto
    )

    return mae, rmse, r2

def main():

    dados = carregar_dados()

    (X_train, X_test, y_temp_train, y_temp_test, y_umid_train, y_umid_test) = dividir_dados(dados)

    modelo_temperatura = treinar_modelo(X_train, y_temp_train)
    modelo_umidade = treinar_modelo(X_train, y_umid_train)

    previsao_temperatura = modelo_temperatura.predict(X_test)
    previsao_umidade = modelo_umidade.predict(X_test)

    mae_temp, rmse_temp, r2_temp = avaliar_modelo(y_temp_test, previsao_temperatura)

    mae_umid, rmse_umid, r2_umid = avaliar_modelo(y_umid_test, previsao_umidade)

    print("\nTemperatura: ")
    print(f"MAE  : {mae_temp:.2f}")
    print(f"RMSE : {rmse_temp:.2f}")
    print(f"R²   : {r2_temp:.3f}")

    print("\nUmidade: ")
    print(f"MAE  : {mae_umid:.2f}")
    print(f"RMSE : {rmse_umid:.2f}")
    print(f"R²   : {r2_umid:.3f}")

if __name__ == "__main__":
    main()