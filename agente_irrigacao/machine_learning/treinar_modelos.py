import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split

BASE_DIR = Path(__file__).resolve().parent.parent

arquivo = BASE_DIR / "dados" / "dados_tratados.csv"

dados = pd.read_csv(arquivo)

X = dados[["Dia","Mes","Hora","Temperatura","Umidade"]]

y_temperatura = dados["Temperatura_2h"]

y_umidade = dados["Umidade_2h"]

X_train, X_test, y_temp_train, y_temp_test = train_test_split(X, y_temperatura, test_size=0.2,
    shuffle=False)

X_train, X_test, y_umid_train, y_umid_test = train_test_split(X, y_umidade, test_size=0.2, shuffle=False)

print("=== Conjunto de treino ===")
print(f"Entradas (X): {X_train.shape}")
print(f"Temperatura (y): {y_temp_train.shape}")
print(f"Umidade (y): {y_umid_train.shape}")

print("\n=== Conjunto de teste ===")
print(f"Entradas (X): {X_test.shape}")
print(f"Temperatura (y): {y_temp_test.shape}")
print(f"Umidade (y): {y_umid_test.shape}")