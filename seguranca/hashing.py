"""Funções de hash (aulas 4, 5 e 6).

ATENÇÃO: `calcula_hash` é um hash DIDÁTICO. Em sistemas reais use
algoritmos próprios para senhas (bcrypt, scrypt, argon2 ou PBKDF2).
`gera_hash_pbkdf2` mostra a opção da biblioteca padrão do Python.
"""

import hashlib
import hmac
import os


def calcula_hash_simples(senha):
    """Aula 4: soma dos valores ASCII. Ex.: "olecram" -> 739."""
    valor = 0
    for letra in senha:
        valor += ord(letra)
    return valor


def calcula_hash(senha, multiplicador=31, bits=32):
    """Aula 5: hash melhorado.

    - multiplicador: o "tempero" da aula (12, 31, 500...), que embaralha
      melhor os caracteres;
    - % 2**bits: mantém o resultado sempre no mesmo tamanho;
    - saída em hexadecimal com 8 dígitos, ex.: "0x000009b4".
    """
    valor = 0
    for letra in senha:
        valor = valor * multiplicador + ord(letra)
        valor %= 2**bits
    return f"0x{valor:08x}"


def verifica_senha(senha_digitada, hash_cadastrado, **parametros):
    """Aula 6: compara hash com hash (nunca senha com senha).

    O mesmo algoritmo e os mesmos parâmetros do cadastro devem ser usados.
    """
    return calcula_hash(senha_digitada, **parametros) == hash_cadastrado


def gera_hash_pbkdf2(senha, salt=None, iteracoes=200_000):
    """Extra: PBKDF2 (biblioteca padrão) com salt aleatório por usuário.

    Retorna (salt_hex, hash_hex). Guarde os dois no banco de dados.
    """
    if salt is None:
        salt = os.urandom(16)
    resultado = hashlib.pbkdf2_hmac("sha256", senha.encode("utf-8"), salt, iteracoes)
    return salt.hex(), resultado.hex()


def verifica_pbkdf2(senha, salt_hex, hash_hex, iteracoes=200_000):
    """Extra: confere uma senha contra (salt, hash) gerados por PBKDF2."""
    _, novo = gera_hash_pbkdf2(senha, bytes.fromhex(salt_hex), iteracoes)
    return hmac.compare_digest(novo, hash_hex)
