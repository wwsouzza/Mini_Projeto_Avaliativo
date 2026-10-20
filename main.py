Python

import funcoes as f

def executar_pipeline():
    registros = f.carregar_csv("halloween_vendas.csv")
    print(f"Total de linhas lidas: {len(registros)}")
    print("Exemplo dos 3 primeiros registros:", registros[:3])

    cat_vazias = 0
    cat_alteradas_conteudo = 0
    cat_so_caixa = 0
    canais_padronizados = 0

    for r in registros:
        cat_limpa, cat_status = f.limpar_categoria(r['categoria'])
        if cat_status == "vazia":
            cat_vazias += 1
        elif cat_status == "alterada_conteudo":
            cat_alteradas_conteudo += 1
        else:
            cat_so_caixa += 1

        canal_padr = f.padronizar_canal(r['canal_venda'])
        if canal_padr and r['canal_venda'] != canal_padr:
            canais_padronizados += 1

    print("\n--- RESULTADOS AULA 1 ---")
    print(f"Categorias Vazias: {cat_vazias}")
    print(f"Categorias Alteradas no Conteúdo: {cat_alteradas_conteudo}")
    print(f"Categorias Apenas Caixa: {cat_so_caixa}")
    print(f"Canais Padronizados: {canais_padronizados}")

if __name__ == "__main__":
    executar_pipeline()
