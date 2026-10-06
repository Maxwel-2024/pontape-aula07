import pandas as pd

# 1. Carregar os dados e criar a coluna receita
df = pd.read_csv("vendas.csv")
df["receita"] = df["quantidade"] * df["preco_unit"]

# 2. Salvar em formato JSON
df.to_json("vendas_com_receita.json", orient="records", force_ascii=False)

# 3. Salvar em formato Excel (.xlsx)
df.to_excel("vendas_com_receita.xlsx", index=False)

# 4. Exibir mensagem de confirmação
print("=== Arquivos gerados ===")
print("✓ vendas_com_receita.json")
print("✓ vendas_com_receita.xlsx")