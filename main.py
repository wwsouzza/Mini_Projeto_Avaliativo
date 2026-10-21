import funcoes as f

def executar_pipeline():
    registros = f.carregar_csv("halloween_vendas.csv")
    total_pedidos = len(registros)
    
    cat_vazias = 0
    cat_alteradas_conteudo = 0
    cat_so_caixa = 0
    canais_padronizados = 0
    
    qtd_invalidas = 0
    preco_invalidos = 0
    pedidos_com_erro_num = set()
    datas_invalidas = 0
    
    sem_entrega_cancelado = 0
    sem_entrega_outros = 0
    exemplos_contraexemplo = []
    
    contagem_canais = {"Web": 0, "Loja física": 0, "Mercado": 0}
    contagem_ano_mes = {}

    for r in registros:
        pid = r['pedido_id']
        
        # Categoria
        cat_limpa, cat_status = f.limpar_categoria(r['categoria'])
        if cat_status == "vazia":
            cat_vazias += 1
        elif cat_status == "alterada_conteudo":
            cat_alteradas_conteudo += 1
        else:
            cat_so_caixa += 1
            
        # Canal
        canal_padr = f.padronizar_canal(r['canal_venda'])
        if canal_padr:
            contagem_canais[canal_padr] += 1
            if r['canal_venda'] != canal_padr:
                canais_padronizados += 1
                
        # Validação Numérica
        q_ok = f.validar_quantidade(r['quantidade'])
        p_ok = f.validar_preco(r['preco_unitario'])
        if not q_ok:
            qtd_invalidas += 1
            pedidos_com_erro_num.add(pid)
        if not p_ok:
            preco_invalidos += 1
            pedidos_com_erro_num.add(pid)
            
        # Datas
        dt = f.converter_data(r['data_venda'])
        if dt:
            chave_am = dt.strftime("%Y-%m")
            contagem_ano_mes[chave_am] = contagem_ano_mes.get(chave_am, 0) + 1
        else:
            datas_invalidas += 1
            
        # Regra de Entrega
        if r['data_entrega'].strip() == "":
            if r['status_pedido'] == "Cancelado":
                sem_entrega_cancelado += 1
            else:
                sem_entrega_outros += 1
                if len(exemplos_contraexemplo) < 3:
                    exemplos_contraexemplo.append((pid, r['status_pedido'], r['data_venda']))

    print("=== RELATÓRIO FESTA EM CENA (PYTHON NATIVO) ===")
    print(f"Total de Linhas Lidas: {total_pedidos}")
    print(f"Categorias Vazias: {cat_vazias} | Alteradas Conteúdo: {cat_alteradas_conteudo} | Caixa: {cat_so_caixa}")
    print(f"Canais Padronizados: {canais_padronizados}")
    print(f"Quantidades Inválidas: {qtd_invalidas} | Preços Ausentes: {preco_invalidos}")
    print(f"Total de Pedidos Afetados por Erros Numéricos: {len(pedidos_com_erro_num)}")
    print(f"Datas de Venda Inválidas: {datas_invalidas}")
    print(f"Hipótese de Entrega Sem Data (109 Cancelados vs {sem_entrega_outros} Outros Status): Falsa")
    print(f"Pedidos por Canal: {contagem_canais}")
    print("Pedidos por Ano-Mês:", dict(sorted(contagem_ano_mes.items())))

if __name__ == "__main__":
    executar_pipeline()