"""Aula 5 - Hash melhorado: multiplicador, módulo 2**32 e hexadecimal fixo.

Execute na raiz do projeto: python exemplos/05_hash_melhorado.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from seguranca.hashing import calcula_hash

senhas = [
    "marcelo123!@",
    "Ma",
    "Marcelo-criptografia-hash-cifras-bilhete-colab-gemini",
]

for senha in senhas:
    print(f"{senha!r:60} -> {calcula_hash(senha)}")

# Trocando o multiplicador, o resultado muda
print(calcula_hash("Marcelo123!", multiplicador=12))
print(calcula_hash("Marcelo123!", multiplicador=31))
print(calcula_hash("Marcelo123!", multiplicador=500))
