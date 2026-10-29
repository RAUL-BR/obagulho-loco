"""Aula 1 - Cifra numérica: cada dígito vira o seu sucessor.

Execute na raiz do projeto: python exemplos/01_cifra_numerica.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from seguranca.cifras import cifra_numerica

senha = "123456"

# Versão passo a passo, como na aula
senha_criptografada = ""
for numero in senha:
    numero = int(numero) + 1  # int() evita o TypeError de somar texto com número
    senha_criptografada = senha_criptografada + str(numero)  # str() para concatenar
print(senha_criptografada)  # 234567

# Mesma ideia, agora como função (permite escolher o deslocamento)
print(cifra_numerica(senha))                  # 234567
print(cifra_numerica(senha, deslocamento=3))  # 456789
