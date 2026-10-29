"""Aula 7 - Ataque com lista de senhas comuns.

Execute na raiz do projeto: python exemplos/07_forca_bruta_comuns.py
"""

import itertools
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from seguranca.forca_bruta import SENHAS_COMUNS, encontra_senha_comum, gera_hashes
from seguranca.hashing import calcula_hash

hashes_comuns = gera_hashes(SENHAS_COMUNS)
print(hashes_comuns)

for senha_cadastrada in ["123456", "marcelo123"]:
    hash_cadastrado = calcula_hash(senha_cadastrada)

    # Pares (hash cadastrado, hash comum), como no itertools.product da aula
    combinacoes = itertools.product([hash_cadastrado], hashes_comuns)
    achou = any(alvo == comum for alvo, comum in combinacoes)

    print(f"\nSenha cadastrada: {senha_cadastrada}")
    print("Está na lista de senhas comuns?", "SIM, quebrada!" if achou else "não")
    print("Senha descoberta:", encontra_senha_comum(hash_cadastrado))
