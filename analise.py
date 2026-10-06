import pandas as pd

# 1. Carregar os dados e calcular a receita
df = pd.read_csv("vendas.csv")
df["receita"] = df["quantidade"] * df["preco_unit"]

# 2. Ordenar por receita em ordem decrescente e selecionar os 5 primeiros
top_5 = df.sort_values(by="receita", ascending=False).head(5)

print("=== Top 5 vendas por receita ===")
print(top_5)