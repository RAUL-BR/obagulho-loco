"""Aula 4 - Hash simples: soma dos valores ASCII.

Execute na raiz do projeto: python exemplos/04_hash_simples.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from seguranca.hashing import calcula_hash_simples

senha = "olecram"
valor = 0
for letra in senha:
    valor = valor + ord(letra)
print(valor)  # 739

# Entradas diferentes podem gerar o mesmo hash (colisão): não é reversível
print(calcula_hash_simples("olecram"))  # 739
print(calcula_hash_simples("marcelo"))  # 739 (mesmas letras, outra ordem)
print(calcula_hash_simples("marcelo123"))
