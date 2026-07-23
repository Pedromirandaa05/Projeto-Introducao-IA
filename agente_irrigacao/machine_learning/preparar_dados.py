import pandas as pd

arquivo = r"C:\Users\pedro\OneDrive\Área de Trabalho\introd_IA\agente_irrigacao\dados\monteiro_2025.CSV"

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

dados["TEMPERATURA DO AR - BULBO SECO, HORARIA (°C)"] = (
    dados["TEMPERATURA DO AR - BULBO SECO, HORARIA (°C)"]
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

print(dados[["Data", "Hora UTC", "Dia", "Mes", "Hora"]].head())