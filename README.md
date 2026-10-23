# Mini_Projeto_Avaliativo
Mini-Projeto Avaliativo - Organização dos registros e verificação dos pedidos por canais e períodos da empresa "Festa em Cena"

Este repositório contém a solução desenvolvida para a auditoria, limpeza e análise exploratória dos dados de vendas da rede **Festa em Cena**.

## 📌 Descrição do Problema
A empresa comercializa fantasias e acessórios de Halloween nos canais **Mercado**, **Loja física** e **Web**. O objetivo do programa é processar 1.500 registros de vendas com problemas de qualidade de dados antes da aplicação de modelos analíticos.

### Explicação das Colunas Selecionadas
1. `pedido_id`: Identificador único de cada transação.
2. `data_venda`: dia e hora do registro da venda (Horário local de São Paulo).
3. `quantidade`: Quantidade de itens comprados no pedido.
4. `status_pedido`: Status da venda (`Concluído`, `Cancelado` ou `Devolvido`).

## 🛠️ Regras de Limpeza e Tratamento Adotadas
- **Textos e Categorias**: Nulos preenchidos com `"sem categoria"`. Expressões regulares (`re.sub`) aplicadas para remoção de pontuações e padronização para minúsculas.
- **Canais**: Mapeamento via dicionário de chaves padronizadas (`Web`, `Loja física`, `Mercado`).
- **Números**: Registros com quantidade < 1 ou preços nulos/negativos foram isolados e registrados via `set` por `pedido_id` (19 pedidos afetados).
- **Datas**: Conversão com `datetime.strptime`. Registros com textos inválidos (`"data_invalida"`) foram isolados sem comprometer a execução do script.

## 🚀 Como Executar o Projeto
```bash
python main.py

## Video com apresentação da solução
https://github.com/user-attachments/assets/0ab78632-b5b2-49a0-819f-982a2f0ed944



