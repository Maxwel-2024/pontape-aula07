import pandas as pd

# 1. Carregar o arquivo CSV e calcular a receita
df = pd.read_csv("vendas.csv")
df["receita"] = df["quantidade"] * df["preco_unit"]

# 2. Converter a coluna 'data' para datetime
df["data"] = pd.to_datetime(df["data"])

# 3. Filtrar apenas as vendas de fevereiro (mês 2)
df_fevereiro = df[df["data"].dt.month == 2]

# 4. Exibir a tabela filtrada
print("=== Vendas de Fevereiro/2025 ===")
print(df_fevereiro.to_string(index=False))

# 5. Calcular e exibir a receita total de fevereiro
receita_fevereiro = df_fevereiro["receita"].sum()
receita_fmt = (
    f"R$ {receita_fevereiro:,.2f}"
    .replace(",", "X")
    .replace(".", ",")
    .replace("X", ".")
)

print("\n=== Receita de Fevereiro ===")
print(receita_fmt)