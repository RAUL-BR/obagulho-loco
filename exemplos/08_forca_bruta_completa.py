"""Aula 8 - Força bruta completa: o tempo cresce de forma exponencial.

Execute na raiz do projeto: python exemplos/08_forca_bruta_completa.py
Opcional: python exemplos/08_forca_bruta_completa.py abc   (senha de 1 a 4 letras)
"""

import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from seguranca.forca_bruta import forca_bruta
from seguranca.hashing import calcula_hash

senha_nova = sys.argv[1] if len(sys.argv) > 1 else "mar"
if len(senha_nova) > 4:
    sys.exit("Use até 4 caracteres: acima disso a simulação fica muito lenta.")

hash_novo = calcula_hash(senha_nova)
caracteres = "abcdefghijklmnopqrstuvwxyzABC123!@#$"  # dicionário da aula

inicio = time.perf_counter()
encontrada = forca_bruta(hash_novo, caracteres, tamanho=len(senha_nova))
tempo = time.perf_counter() - inicio

print("Senha encontrada:", encontrada)
print(f"Tempo: {tempo:.2f} s")
print(f"Combinações possíveis: {len(caracteres) ** len(senha_nova):,}")
