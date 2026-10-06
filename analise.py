import matplotlib.pyplot as plt
import pandas as pd

# 1. Carregar os dados e criar a coluna receita
df = pd.read_csv("vendas.csv")
df["receita"] = df["quantidade"] * df["preco_unit"]

# 2. Agrupar a receita por categoria (ordenada do maior para o menor)
receita_cat = (
    df.groupby("categoria")["receita"].sum().sort_values(ascending=False)
)

# 3. Criar a figura com o tamanho 10x6
plt.figure(figsize=(10, 6))

# 4. Gerar o gráfico de barras com a cor #4A90E2
bars = plt.bar(
    receita_cat.index,
    receita_cat.values,
    color="#4A90E2",
    edgecolor="black",
    alpha=0.85,
)

# 5. Configurar Título e Rótulos dos Eixos
plt.title(
    "Receita por Categoria — 1º Trimestre 2025",
    fontsize=14,
    fontweight="bold",
    pad=15,
)
plt.xlabel("Categoria", fontsize=12, labelpad=10)
plt.ylabel("Receita (R$)", fontsize=12, labelpad=10)

# Configurar grade auxiliar
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Adicionar os valores formatados no topo de cada barra
for bar in bars:
    yval = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        yval + 200,
        f"R$ {yval:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."),
        ha="center",
        va="bottom",
        fontsize=10,
        fontweight="bold",
    )

plt.tight_layout()

# 6. Salvar o gráfico como imagem
plt.savefig("grafico_receita.png", dpi=300)

# 7. Exibir o gráfico na tela
plt.show()