import pandas as pd

# 1. Carregar o arquivo CSV
df = pd.read_csv("vendas.csv")

# 2. Exibir as 5 primeiras linhas e o total de registros
print("=== Primeiras 5 vendas ===")
print(df.head())
print(f"\nTotal de registros: {len(df)}")