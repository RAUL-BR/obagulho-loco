"""Simulação educacional de força bruta (aulas 7 e 8).

Use apenas nos hashes didáticos criados neste projeto, para entender por
que senhas curtas e comuns são fracas. Não use contra sistemas de terceiros.
"""

import itertools
import string

from .hashing import calcula_hash

SENHAS_COMUNS = [
    "123456",
    "password",
    "123456789",
    "qwerty",
    "12345678",
    "111111",
    "12345",
    "columbia",
    "senha",
    "iloveyou",
]

# Conjunto de caracteres completo (minúsculas, maiúsculas, dígitos, símbolos)
CARACTERES_COMPLETOS = string.ascii_letters + string.digits + string.punctuation


def gera_hashes(senhas):
    """Aula 7: devolve a lista com o hash de cada senha.

    (Corrige a aula: a lista começa vazia, só com hashes, sem as senhas.)
    """
    hashes = []
    for senha in senhas:
        hashes.append(calcula_hash(senha))
    return hashes


def encontra_senha_comum(hash_alvo, senhas=SENHAS_COMUNS):
    """Aula 7: testa cada senha comum; devolve a que bater ou None."""
    for senha in senhas:
        if calcula_hash(senha) == hash_alvo:
            return senha
    return None


def forca_bruta(hash_alvo, caracteres=CARACTERES_COMPLETOS, tamanho=3):
    """Aula 8: testa todas as combinações de `tamanho` caracteres.

    Devolve a primeira combinação cujo hash seja igual ao alvo, ou None.
    Observação: como o hash didático tem só 32 bits, pode haver colisão e a
    senha encontrada pode ser diferente da original (mas com o mesmo hash).
    """
    for combinacao in itertools.product(caracteres, repeat=tamanho):
        tentativa = "".join(combinacao)
        if calcula_hash(tentativa) == hash_alvo:
            return tentativa
    return None
