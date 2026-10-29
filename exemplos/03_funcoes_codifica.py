"""Aula 3 - Funções: codifica() e tratamento de caracteres.

Execute na raiz do projeto: python exemplos/03_funcoes_codifica.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from seguranca.cifras import codifica, codifica_minusculas, decodifica

print(codifica_minusculas("marcelo"))     # dqketsg
print(codifica_minusculas("marcelo123"))  # dqketsg123 (números mantidos)
print(codifica_minusculas("Marcelo"))     # Mqketsg (maiúscula mantida)

# Desafio da aula: tratar também maiúsculas e números
criptografada = codifica("Marcelo123!")
print(criptografada)
print(decodifica(criptografada))  # Marcelo123!
