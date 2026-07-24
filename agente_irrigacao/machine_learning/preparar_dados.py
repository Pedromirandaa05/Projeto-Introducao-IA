import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

arquivo = BASE_DIR / "dados" / "monteiro_2025.CSV"

df = pd.read_csv(
    arquivo,
    sep=";",
    skiprows=8,
    encoding="latin1"
)

# Seleciona apenas as colunas que serão utilizadas
dados = df[
    [
        "Data",
        "Hora UTC",
        "TEMPERATURA DO AR - BULBO SECO, HORARIA (°C)",
        "UMIDADE RELATIVA DO AR, HORARIA (%)"
    ]
].copy()

dados = dados.rename(columns={
    "TEMPERATURA DO AR - BULBO SECO, HORARIA (°C)": "Temperatura",
    "UMIDADE RELATIVA DO AR, HORARIA (%)": "Umidade"
})

dados["Temperatura"] = (
    dados["Temperatura"]
    .str.replace(",", ".", regex=False)
    .astype(float)
)

dados["Data"] = pd.to_datetime(dados["Data"], format="%Y/%m/%d")

dados["Dia"] = dados["Data"].dt.day
dados["Mes"] = dados["Data"].dt.month

dados["Hora"] = (
    dados["Hora UTC"]
    .str.replace(" UTC", "", regex=False)
    .str[:2]
    .astype(int)
)


dados["Temperatura_2h"] = dados["Temperatura"].shift(-2)
dados["Umidade_2h"] = dados["Umidade"].shift(-2)

dados = dados.dropna()

saida = BASE_DIR / "dados" / "dados_tratados.csv"

dados.to_csv(
    saida,
    index=False,
    encoding="utf-8"
)

print(f"Arquivo salvo em: {saida}")