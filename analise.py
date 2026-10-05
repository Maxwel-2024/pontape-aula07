import pandas as pd

# 1. Carregar o arquivo CSV
df = pd.read_csv("vendas.csv")

# 2. Criar a coluna 'receita' multiplicando quantidade por preco_unit
df["receita"] = df["quantidade"] * df["preco_unit"]

# 3. Exibir o DataFrame com a nova coluna
print("=== Vendas com receita ===")
print(df.head())