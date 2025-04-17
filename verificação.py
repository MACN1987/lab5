import re
import os

def validar_cartao(numero_cartao):
    """
    Valida o número do cartão de crédito e identifica a bandeira.
    
    Args:
        numero_cartao (str): Número do cartão de crédito.
    
    Returns:
        str: Bandeira do cartão ou mensagem de erro.
    """
    # Remove espaços ou traços do número do cartão
    numero_cartao = numero_cartao.replace(" ", "").replace("-", "")
    
    # Verifica se o número contém apenas dígitos
    if not numero_cartao.isdigit():
        return "Número de cartão inválido. Deve conter apenas dígitos."
    
    # Verifica a bandeira com base nos padrões
    if numero_cartao.startswith(("4011", "4312", "4389")):
        return "Elo"
    elif numero_cartao.startswith("4"):
        return "Visa"
    elif re.match(r"^5[1-5]", numero_cartao) or re.match(r"^2(2[2-9]|[3-6][0-9]|7[01]|720)", numero_cartao):
        return "MasterCard"    
    elif numero_cartao.startswith(("34", "37")):
        return "American Express"
    elif numero_cartao.startswith(("20", "21")):
        return "Enroute"
    elif numero_cartao.startswith(("30", "36", "38")):
        return "Diners Club"
    elif re.match(r"^(6011|65|64[4-9])", numero_cartao):
        return "Discover"
    elif numero_cartao.startswith("6062"):
        return "Hipercard"
    elif numero_cartao.startswith("35"):
        return "JCB"
    elif numero_cartao.startswith("50"):
        return "Aura"
    else:
        return "Bandeira desconhecida ou número inválido."

# Exemplo de uso
numero = str(input("Digite o número do cartão de crédito: "))
bandeira = validar_cartao(numero)
print(f"Bandeira: {bandeira}")


