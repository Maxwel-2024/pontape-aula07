import pandas as pd

# 1. Carregar o CSV e criar a coluna receita
df = pd.read_csv("vendas.csv")
df["receita"] = df["quantidade"] * df["preco_unit"]

# 2. Receita total da loja no trimestre
receita_total = df["receita"].sum()
print("=== Receita total ===")
print(
    f"R$ {receita_total:,.2f}"
    .replace(",", "X")
    .replace(".", ",")
    .replace("X", ".")
)

# 3. Receita por categoria ordenada do maior para o menor
receita_categoria = (
    df.groupby("categoria")["receita"].sum().sort_values(ascending=False)
)

print("\n=== Receita por categoria ===")
for categoria, valor in receita_categoria.items():
    valor_formatado = (
        f"R$ {valor:,.2f}"
        .replace(",", "X")
        .replace(".", ",")
        .replace("X", ".")
    )
    print(f"{categoria:<15}{valor_formatado}")