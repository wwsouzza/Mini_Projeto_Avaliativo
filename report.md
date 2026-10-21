# Relatório de Análise de Dados: Festa em Cena

## 1. Contexto e Objetivos
A Festa em Cena é uma empresa não real, atuante no segmento de fantasias e acessórios de Halloween, comercializando produtos por meio de três canais principais: Mercado, Loja física e Web. O estudo analisa uma base de dados composta por 1.500 registros de pedidos realizados entre agosto e novembro dos anos de 2024 e 2025. O objetivo central consiste em limpar a base de dados, auditar inconsistências e gerar métricas descritivas para apoiar tomadas de decisão gerenciais.

## 2. Qualidade dos Dados e limpeza/ajustes
A auditoria identificou diversas anomalias estruturais na base original:
- **Categorias de Produtos:** Foram identificados 18 registros originalmente nulos ou vazios, devidamente preenchidos com o rótulo `"sem categoria"`. Além disso, 131 registros continham alteração no conteúdo por espaçamentos extras, caracteres maiúsculos e pontuações indevidas (como `"FANTASIA!!!"`), os quais foram ajustados via expressões regulares, resultando em três categorias padronizadas: `fantasia`, `acessorio` e `sem categoria`.
- **Integridade Numérica:** Constataram-se 7 pedidos com quantidade não valídas (valores negativos, especificamente `-1`) e 12 pedidos com preço unitário ausente (`NaN`). O total de pedidos afetados por anomalias numéricas foi de 19 registros (sem sobreposição entre as falhas).
- **Consistência Temporal:** Registraram-se 4 ocorrências com texto de data inválido (`"data_invalida"`), que foram isoladas sem comprometer a análise temporal dos demais 1.496 registros válidos.

## 3. Investigação da Regra de Negócio de Entrega
Investigou-se a hipótese de que todos os pedidos sem data de entrega registrada pertenceriam ao status "Cancelado". A análise refutou a hipótese:
- Do total de 143 pedidos sem data de entrega, 109 correspondem de fato a pedidos `Cancelado`.
- No entanto, 34 pedidos constam com status `Concluído` mesmo sem possuir data de entrega cadastrada.
- *Exemplos de contraexemplos:* Pedido ID 1170 (status Concluído, data de venda 19/08/2025), Pedido ID 990 (Concluído, 13/10/2025) e Pedido ID 740 (Concluído). Essa evidência confirma a falsidade da hipótese e aponta para falhas no fluxo de atualização logística.

## 4. Descobertas e Métricas Operacionais
- **Distribuição por Canal de Venda:** O canal `Web` lidera o volume de registros com 666 pedidos (44,4%), seguido pela `Loja física` com 551 pedidos (36,7%) e `Mercado` com 283 pedidos (18,9%). *Limitação:* Os dados refletem contagem de pedidos cadastrados, e não faturamento real ou volume financeiro arrecadado.
- **Sazonalidade e Comportamento Temporal:** As vendas apresentam extrema concentração no mês de outubro em ambos os anos, registrando 393 pedidos em 10/2024 e 410 pedidos em 10/2025, representando cerca de 53,5% do total anual acumulado no período de pico devido as festas de Halloween (31 de outubro).