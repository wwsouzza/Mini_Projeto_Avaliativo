Python

import pandas as pd
import re
from datetime import datetime

# Padronizando os canais de vendas para evitar inconsistências.
CANAIS_VALIDOS = {
    "mercado": "Mercado",
    "loja física": "Loja física",
    "loja fisica": "Loja física",
    "web": "Web"
}

def carregar_csv(caminho: str) -> list:
    #Lê o CSV garantindo entrada como texto sem alteração do arquivo original.
    df = pd.read_csv(caminho, dtype=str, keep_default_na=False)
    return df.to_dict(orient='records')

def limpar_categoria(texto: str):
    #Limpa e classifica a categoria com .strip(), .lower() e regex.
    if not texto or texto.strip() == "":
        return "sem categoria", "vazia"
    
    orig = texto
    limpo = orig.strip().lower()
    limpo = re.sub(r"[^a-z\s]", "", limpo)
    limpo = re.sub(r"\s+", " ", limpo).strip()
    
    if limpo == "":
        return "sem categoria", "vazia"
    elif limpo != orig.lower():
        return limpo, "alterada_conteudo"
    else:
        return limpo, "so_caixa"

def padronizar_canal(texto: str):
    #Padroniza o canal de vendas utilizando dicionário de canais válidos.
    return CANAIS_VALIDOS.get(texto.strip().lower())

