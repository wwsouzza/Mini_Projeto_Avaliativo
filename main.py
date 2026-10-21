import funcoes as f

def executar_pipeline():
    registros = f.carregar_csv("halloween_vendas.csv")
    
    qtd_invalidas = 0
    preco_invalidos = 0
    pedidos_com_erro_num = set()
    datas_invalidas = 0

    for r in registros:
        pid = r['pedido_id']
        
        q_ok = f.validar_quantidade(r['quantidade'])
        p_ok = f.validar_preco(r['preco_unitario'])
        if not q_ok:
            qtd_invalidas += 1
            pedidos_com_erro_num.add(pid)
        if not p_ok:
            preco_invalidos += 1
            pedidos_com_erro_num.add(pid)
            
        dt = f.converter_data(r['data_venda'])
        if not dt:
            datas_invalidas += 1

    print("\n--- RESULTADOS Passo 2 ---")
    print(f"Quantidades Inválidas: {qtd_invalidas}")
    print(f"Preços Ausentes/Inválidos: {preco_invalidos}")
    print(f"Total de Pedidos Afetados por Erros Numéricos: {len(pedidos_com_erro_num)}")
    print(f"Datas Inválidas: {datas_invalidas}")

if __name__ == "__main__":
    executar_pipeline()