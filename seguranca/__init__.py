"""Pacote educacional: cifras simples, hash, autenticação e força bruta."""

from .cifras import codifica, decodifica, cifra_numerica
from .hashing import (
    calcula_hash,
    calcula_hash_simples,
    gera_hash_pbkdf2,
    verifica_pbkdf2,
    verifica_senha,
)
from .forca_bruta import (
    gera_hashes,
    encontra_senha_comum,
    forca_bruta,
)

__all__ = [
    "codifica",
    "decodifica",
    "cifra_numerica",
    "calcula_hash",
    "calcula_hash_simples",
    "gera_hash_pbkdf2",
    "verifica_pbkdf2",
    "verifica_senha",
    "gera_hashes",
    "encontra_senha_comum",
    "forca_bruta",
]
