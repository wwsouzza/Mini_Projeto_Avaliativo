from datetime import datetime

FORMATO_DATA = "%Y-%m-%d %H:%M:%S"

def validar_quantidade(texto: str) -> bool:
    #Validar se a quantidade é um número inteiro maior que zero.
    try:
        val = int(texto)
        return val > 0
    except ValueError:
        return False

def validar_preco(texto: str) -> bool:
    #Validar se o preço está preenchido e é um número postivo.
    if not texto or texto.strip() == "":
        return False
    try:
        val = float(texto)
        return val >= 0
    except ValueError:
        return False

def converter_data(texto: str):
    #Converter a string no formato ISO via strptime.
    try:
        return datetime.strptime(texto, FORMATO_DATA)
    except (ValueError, TypeError):
        return None

