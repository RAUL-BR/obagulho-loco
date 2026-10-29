"""Cifras simples (aulas 1 a 3).

ATENÇÃO: são cifras didáticas e fracas. Servem para aprender lógica de
programação, não para proteger dados reais.
"""

ALFABETO = "abcdefghijklmnopqrstuvwxyz"
DICIONARIO = "qwertyuiopasdfghjklzxcvbnm"  # letras na ordem do teclado

ALFABETO_MAIUSCULO = ALFABETO.upper()
DICIONARIO_MAIUSCULO = DICIONARIO.upper()

DIGITOS = "0123456789"
DICIONARIO_DIGITOS = "5827419036"  # uma permutação dos dígitos 0-9


def cifra_numerica(senha, deslocamento=1):
    """Aula 1: soma `deslocamento` a cada dígito ("123456" -> "234567").

    Usa % 10 para que o 9 volte ao 0 e a senha mantenha o mesmo tamanho.
    """
    resultado = ""
    for numero in senha:
        if not numero.isdigit():
            raise ValueError(f"Caractere não numérico: {numero!r}")
        resultado += str((int(numero) + deslocamento) % 10)
    return resultado


def codifica_minusculas(senha, dicionario=DICIONARIO):
    """Aulas 2 e 3: troca apenas letras minúsculas pelo dicionário.

    Qualquer outro caractere (números, maiúsculas, símbolos) é mantido.
    """
    resultado = ""
    for letra in senha:
        if "a" <= letra <= "z":
            posicao = ord(letra) - ord("a")  # 0 até 25
            resultado += dicionario[posicao]
        else:
            resultado += letra
    return resultado


def codifica(senha):
    """Versão final (desafio da aula 3): minúsculas, maiúsculas e dígitos.

    Símbolos e demais caracteres são mantidos como estão.
    """
    resultado = ""
    for letra in senha:
        if "a" <= letra <= "z":
            resultado += DICIONARIO[ord(letra) - ord("a")]
        elif "A" <= letra <= "Z":
            resultado += DICIONARIO_MAIUSCULO[ord(letra) - ord("A")]
        elif "0" <= letra <= "9":
            resultado += DICIONARIO_DIGITOS[ord(letra) - ord("0")]
        else:
            resultado += letra
    return resultado


def decodifica(senha_criptografada):
    """Reverte `codifica` (criptografia pode ser revertida; hash não)."""
    resultado = ""
    for letra in senha_criptografada:
        if letra in DICIONARIO:
            resultado += chr(DICIONARIO.index(letra) + ord("a"))
        elif letra in DICIONARIO_MAIUSCULO:
            resultado += chr(DICIONARIO_MAIUSCULO.index(letra) + ord("A"))
        elif letra in DICIONARIO_DIGITOS:
            resultado += chr(DICIONARIO_DIGITOS.index(letra) + ord("0"))
        else:
            resultado += letra
    return resultado
