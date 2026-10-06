📊 Estudo Prático de Análise de Dados com Python
Este repositório é um material de estudo prático criado para demonstrar o fluxo essencial de manipulação, análise e visualização de dados em Python. O objetivo principal é exercitar o uso das bibliotecas Pandas e Matplotlib através de dados fictícios de vendas.

🎯 Como Funciona Cada Tarefa do Estudo
O estudo é estruturado em 7 etapas progressivas:

Tarefa 1 — Leitura do CSV e Inspeção: Carrega a base de dados vendas.csv utilizando o Pandas para visualizar as primeiras linhas e conferir a quantidade total de registros importados.

Tarefa 2 — Engenharia de Atributos: Cria a coluna receita multiplicando a quantidade vendida pelo preço unitário (quantidade * preco_unit), preparando o conjunto de dados para análises financeiras.

Tarefa 3 — Métricas de Faturamento: Calcula o faturamento total do trimestre e agrupa os valores por categoria de produto (groupby), identificando os setores que geraram mais receita.

Tarefa 4 — Filtragem Temporal: Converte os dados do campo de data para o tipo datetime para realizar filtros temporais precisos, isolando apenas o histórico de vendas de um mês específico (Fevereiro/2025).

Tarefa 5 — Ordenação (Top 5): Reordena as vendas em ordem decrescente de faturamento para extrair e destacar os 5 produtos/transações de maior valor do período.

Tarefa 6 — Exportação em Múltiplos Formatos: Salva o conjunto de dados tratado nos formatos .json (com codificação UTF-8) e .xlsx (Excel) para permitir a integração com outras ferramentas e sistemas.

Tarefa 7 — Visualização Gráfica: Gera um gráfico de barras com Matplotlib exibindo a receita comparativa de cada categoria e salva o resultado final como uma imagem .png.

⚙️ Como o Código Roda
Execução: Ao rodar o script Python, ele lê o arquivo vendas.csv localizado no mesmo diretório do projeto e executa todas as transformações em memória.

Saídas Automáticas: Durante a execução, o script imprime as métricas no terminal, exporta os arquivos vendas_com_receita.json e vendas_com_receita.xlsx, além de salvar o gráfico em grafico_receita.png.

Interface Visual: No final do processo, uma janela é aberta na tela exibindo o gráfico formatado de receita por categoria.

💡 Dica para Praticar
Por se tratar de um projeto didático, tente alterar os parâmetros das tarefas diretamente no código — por exemplo, filtrando as vendas de março, modificando as cores do gráfico ou descobrindo o Top 10 produtos mais vendidos.