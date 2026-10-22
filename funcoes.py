import pandas as pd
import re
from datetime import datetime

# Mapeamento oficial para padronização de canais
CANAIS_VALIDOS = {
    "mercado": "Mercado",
    "loja física": "Loja física",
    "loja fisica": "Loja física",
    "web": "Web"
}

FORMATO_DATA = "%Y-%m-%d %H:%M:%S"

def carregar_csv(caminho: str) -> list:
    """
    Lê o CSV garantindo que todos os campos entrem como texto sem conversão automática.
    Retorna uma lista de dicionários para processamento nativo.
    """
    df = pd.read_csv(caminho, dtype=str, keep_default_na=False)
    return df.to_dict(orient='records')

def limpar_categoria(texto: str):
    """
    Aplica .strip(), .lower() e expressões regulares com re.sub para remover pontuações.
    Classifica a alteração conforme os critérios das aulas.
    """
    if not texto or texto.strip() == "":
        return "sem categoria", "vazia"
    
    orig = texto
    limpo = orig.strip().lower()
    # Preserva apenas letras sem acento e espaços
    limpo = re.sub(r"[^a-z\s]", "", limpo)
    limpo = re.sub(r"\s+", " ", limpo).strip()
    
    if limpo == "":
        return "sem categoria", "vazia"
    elif limpo != orig.lower():
        return limpo, "alterada_conteudo"  # Caso tenha mudado pontuação ou espaços extras
    else:
        return limpo, "so_caixa"            # Apenas conversão de maiúsculas/minúsculas

def padronizar_canal(texto: str):
    #Retorna o nome do canal padronizado usando o dicionário CANAIS_VALIDOS.
    return CANAIS_VALIDOS.get(texto.strip().lower())

def validar_quantidade(texto: str) -> bool:
    """Valida se a quantidade é um número inteiro estritamente maior que zero."""
    try:
        val = int(texto)
        return val > 0
    except ValueError:
        return False

def validar_preco(texto: str) -> bool:
    """Valida se o preço está preenchido e é um número não negativo."""
    if not texto or texto.strip() == "":
        return False
    try:
        val = float(texto)
        return val >= 0
    except ValueError:
        return False

def converter_data(texto: str):
    """Converte a string no formato ISO via strptime. Retorna None em caso de falha."""
    try:
        return datetime.strptime(texto, FORMATO_DATA)
    except (ValueError, TypeError):
        return None

def formatar_data_br(dt: datetime) -> str:
    """Gera a apresentação brasileira de datas (dd/mm/aaaa)."""
    return dt.strftime("%d/%m/%Y") if dt else ""