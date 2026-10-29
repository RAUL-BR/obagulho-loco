"""Aula 6 - Simulação de cadastro e login com hash.

Execute na raiz do projeto: python exemplos/06_login_simulado.py
(senha de teste: marcelo123)
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from seguranca.hashing import calcula_hash

# 1) Cadastro: guarda-se apenas o HASH, nunca a senha
senha_cadastrada = "marcelo123"
hash_cadastrado = calcula_hash(senha_cadastrada)
print("Hash guardado no banco:", hash_cadastrado)

# 2) Login: aplica-se o MESMO algoritmo à senha digitada
try:
    senha_digitada = input("Digite sua senha: ")
except EOFError:
    senha_digitada = ""
hash_digitado = calcula_hash(senha_digitada)

# 3) Compara hash com hash
if hash_cadastrado == hash_digitado:
    print("Acesso liberado")
else:
    print("Acesso negado")
