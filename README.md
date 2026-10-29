# 🔐 Criptografia, Hash e Segurança de Senhas em Python

Projeto didático que reúne, em ordem, as aulas sobre **criptografia simples**, **hash**, **autenticação** e **ataques de força bruta**. Cada aula virou um exemplo executável em `exemplos/`, e o código reutilizável fica no pacote `seguranca/`.

> ⚠️ **Projeto educacional.** As cifras e o hash daqui são propositalmente simples para ensinar lógica. **Não use em sistemas reais.** Para senhas de verdade use bcrypt, scrypt, argon2 ou PBKDF2 (há um exemplo de PBKDF2 em `seguranca/hashing.py`).

## Estrutura

```
criptografia-hash-python/
├── seguranca/              # código reutilizável
│   ├── cifras.py           # aulas 1-3: cifras numérica e de letras
│   ├── hashing.py          # aulas 4-6: hash e verificação de senha
│   └── forca_bruta.py      # aulas 7-8: ataques de força bruta (didáticos)
├── exemplos/               # um script por aula
│   ├── 01_cifra_numerica.py
│   ├── 02_cifra_letras.py
│   ├── 03_funcoes_codifica.py
│   ├── 04_hash_simples.py
│   ├── 05_hash_melhorado.py
│   ├── 06_login_simulado.py
│   ├── 07_forca_bruta_comuns.py
│   └── 08_forca_bruta_completa.py
├── tests/test_seguranca.py # testes automatizados
└── .github/workflows/tests.yml  # CI do GitHub Actions
```

## Como executar (VS Code ou terminal)

Requer **Python 3.10+**. Não há dependências externas.

```bash
git clone <url-do-seu-repositorio>
cd criptografia-hash-python

python exemplos/01_cifra_numerica.py      # rode qualquer exemplo na raiz do projeto
python -m unittest discover -v            # roda todos os testes
```

---

## Aula 1 — Criptografia numérica

**Ideia:** anotar a senha de forma modificada, com uma regra para reconstruí-la. Aqui, cada dígito vira o seu sucessor: `123456` → `234567`.

**Armadilhas da aula:**
- `numero + 1` com `numero` sendo texto causa `TypeError` → converta com `int()`.
- `numero + "1"` **concatena** (não soma) → por isso `int(numero) + 1`.
- Para juntar o resultado, volte a texto com `str()`.

```python
senha = "123456"
senha_criptografada = ""
for numero in senha:
    numero = int(numero) + 1
    senha_criptografada = senha_criptografada + str(numero)
print(senha_criptografada)  # 234567
```

Código completo: [`exemplos/01_cifra_numerica.py`](exemplos/01_cifra_numerica.py) · função `cifra_numerica` em [`seguranca/cifras.py`](seguranca/cifras.py).

> Na versão em função, usei `% 10` para que o `9` volte a `0` e a senha mantenha o tamanho.

**Força da criptografia:** regra simples e fácil de identificar = criptografia *fraca*; padrão complexo = *mais forte*.

## Aula 2 — Criptografia com letras (ASCII e dicionário)

- `ord(letra)` converte uma letra em número (tabela ASCII): `a` = 97 … `z` = 122.
- `ord(letra) - ord("a")` gera a posição de 0 a 25.
- Um **dicionário de substituição** (letras na ordem do teclado) troca cada letra pela de mesma posição.

```python
alfabeto = "abcdefghijklmnopqrstuvwxyz"
dicionario = "qwertyuiopasdfghjklzxcvbnm"
senha = "marcelo"
senha_criptografada = ""

for letra in senha:                       # percorre a SENHA, não o alfabeto
    posicao = ord(letra) - ord("a")       # 0 até 25
    senha_criptografada += dicionario[posicao]

print(senha_criptografada)  # dqketsg
```

Código completo: [`exemplos/02_cifra_letras.py`](exemplos/02_cifra_letras.py).

## Aula 3 — Funções e caracteres não alfabéticos

Organização do código em uma função `codifica(senha)` com `return`. Com `senha = "marcelo123"` o código simples dá erro, pois `ord("1") - ord("a")` é negativo e o índice sai do dicionário. A solução é um `if "a" <= letra <= "z"` e um `else` que mantém o caractere original.

```python
def codifica_minusculas(senha, dicionario=DICIONARIO):
    resultado = ""
    for letra in senha:
        if "a" <= letra <= "z":
            posicao = ord(letra) - ord("a")
            resultado += dicionario[posicao]
        else:
            resultado += letra
    return resultado
```

**Desafio resolvido:** `codifica()` em [`seguranca/cifras.py`](seguranca/cifras.py) trata minúsculas, maiúsculas e dígitos (símbolos permanecem), e `decodifica()` reverte o processo.

Exemplo: [`exemplos/03_funcoes_codifica.py`](exemplos/03_funcoes_codifica.py).

**Por que essa cifra é fraca?** Quem descobre algumas trocas (`A → Q`, `L → P`…) reconstrói todo o dicionário, e um computador testa possibilidades muito rápido.

## Aula 4 — Hash (transformação irreversível)

Em sistemas reais a senha não é guardada diretamente: guarda-se um **hash**. Primeira versão: somar os valores ASCII.

```python
def calcula_hash_simples(senha):
    valor = 0
    for letra in senha:
        valor += ord(letra)
    return valor

calcula_hash_simples("olecram")  # 739
```

Entradas diferentes podem gerar o mesmo valor (**colisão**): `"olecram"` e `"marcelo"` dão 739. Por isso não há como voltar à senha original.

Exemplo: [`exemplos/04_hash_simples.py`](exemplos/04_hash_simples.py).

## Aula 5 — Hash melhorado

Três ajustes na função:

1. **Multiplicador** (o "tempero" da aula): `valor = valor * 31 + ord(letra)`.
2. **Módulo** `% 2**32`: o resultado cabe sempre em 32 bits (como os ponteiros do relógio, que voltam a zero).
3. **Hexadecimal de tamanho fixo**: `f"0x{valor:08x}"`, para que o tamanho da saída não revele o tamanho da senha.

```python
def calcula_hash(senha, multiplicador=31, bits=32):
    valor = 0
    for letra in senha:
        valor = valor * multiplicador + ord(letra)
        valor %= 2**bits
    return f"0x{valor:08x}"
```

Resultados conferidos com os da aula: `"Ma"` → `0x000009b4`, `"Marcelo123!@"` → `0xe76d642e`.

Exemplo: [`exemplos/05_hash_melhorado.py`](exemplos/05_hash_melhorado.py).

> 📝 Nota: na aula chama-se esse multiplicador de *salt*. Num sistema real, o **salt** é um valor **aleatório, diferente por usuário**, guardado junto do hash. O exemplo `gera_hash_pbkdf2` em `seguranca/hashing.py` mostra isso.

## Aula 6 — Simulação de cadastro e login

Fluxo: cadastro guarda o **hash**; no login, aplica-se o **mesmo algoritmo e parâmetros** à senha digitada e **compara-se hash com hash**.

```python
hash_cadastrado = calcula_hash("marcelo123")
senha_digitada = input("Digite sua senha: ")
if calcula_hash(senha_digitada) == hash_cadastrado:
    print("Acesso liberado")
else:
    print("Acesso negado")
```

- `=` atribui; `==` compara.
- **Hash** não pode ser revertido; **criptografia** pode ser revertida com uma chave.

Exemplo: [`exemplos/06_login_simulado.py`](exemplos/06_login_simulado.py) (senha de teste: `marcelo123`).

## Aula 7 — Força bruta com senhas comuns

Existem listas de senhas já vazadas. Um atacante calcula o hash de cada uma e compara com o hash da vítima.

```python
hashes_comuns = []                      # começa vazia, só com hashes
for senha in senhas_comuns:
    hashes_comuns.append(calcula_hash(senha))
```

> 🐛 **Correção em relação à aula:** o código da aula iniciava `hashes_comuns` já com as senhas em texto e só depois adicionava os hashes, misturando os dois. Aqui a lista começa vazia.

`itertools.product([hash_cadastrado], hashes_comuns)` gera os pares (hash cadastrado, hash comum); `list()` permite visualizá-los.

Exemplo: [`exemplos/07_forca_bruta_comuns.py`](exemplos/07_forca_bruta_comuns.py).

## Aula 8 — Força bruta completa

Quando a senha não está na lista, testa-se **toda combinação** possível:

```python
for combinacao in itertools.product(caracteres, repeat=tamanho):
    tentativa = "".join(combinacao)
    if calcula_hash(tentativa) == hash_alvo:
        print(tentativa)
        break
```

O número de combinações é `len(caracteres) ** tamanho`: cresce de forma **exponencial**. Com 36 caracteres, 3 posições = 46.656 combinações; 6 posições = mais de 2 bilhões.

> ℹ️ Como o hash didático tem só 32 bits, pode ocorrer colisão: a senha "encontrada" pode ser outra com o mesmo hash.

Exemplo: [`exemplos/08_forca_bruta_completa.py`](exemplos/08_forca_bruta_completa.py) (aceita a senha como argumento, até 4 caracteres).

## ✅ Boas práticas de senha

- Evite senhas comuns e não reutilize senhas.
- Crie senhas **longas** e misture letras, números e símbolos.
- Se um sistema avisar que sua senha foi vazada, troque imediatamente.
- Em sistemas reais, guarde senhas com bcrypt/argon2/PBKDF2 e salt aleatório.

## Licença

Uso educacional. Adicione a licença de sua preferência (ex.: MIT) ao publicar.
