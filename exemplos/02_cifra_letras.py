"""Aula 2 - Cifra com letras: tabela ASCII e dicionário de substituição.

Execute na raiz do projeto: python exemplos/02_cifra_letras.py
"""

alfabeto = "abcdefghijklmnopqrstuvwxyz"
dicionario = "qwertyuiopasdfghjklzxcvbnm"  # mesmo tamanho do alfabeto

# ord() converte uma letra em número (tabela ASCII): a=97 ... z=122
for letra in alfabeto[:8]:
    print(letra, ord(letra))

senha = "marcelo"
senha_criptografada = ""

# O laço percorre a SENHA (e não o alfabeto)
for letra in senha:
    posicao = ord(letra) - ord("a")  # 0 até 25
    senha_criptografada += dicionario[posicao]

print(senha_criptografada)  # dqketsg
