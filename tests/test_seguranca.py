import unittest

from seguranca.cifras import cifra_numerica, codifica, codifica_minusculas, decodifica
from seguranca.forca_bruta import (
    SENHAS_COMUNS,
    encontra_senha_comum,
    forca_bruta,
    gera_hashes,
)
from seguranca.hashing import (
    calcula_hash,
    calcula_hash_simples,
    gera_hash_pbkdf2,
    verifica_pbkdf2,
    verifica_senha,
)


class TestCifras(unittest.TestCase):
    def test_cifra_numerica(self):
        self.assertEqual(cifra_numerica("123456"), "234567")
        self.assertEqual(cifra_numerica("9"), "0")

    def test_cifra_numerica_rejeita_letras(self):
        with self.assertRaises(ValueError):
            cifra_numerica("12a")

    def test_codifica_minusculas(self):
        self.assertEqual(codifica_minusculas("marcelo"), "dqketsg")
        self.assertEqual(codifica_minusculas("marcelo123"), "dqketsg123")

    def test_codifica_e_decodifica(self):
        for senha in ["Marcelo123!", "abc", "XYZ 09", "ç-é"]:
            self.assertEqual(decodifica(codifica(senha)), senha)

    def test_codifica_muda_o_texto(self):
        self.assertNotEqual(codifica("Marcelo123!"), "Marcelo123!")


class TestHash(unittest.TestCase):
    def test_hash_simples(self):
        self.assertEqual(calcula_hash_simples("olecram"), 739)

    def test_hash_formato_fixo(self):
        self.assertEqual(calcula_hash("Ma"), "0x000009b4")
        for senha in ["a", "Ma", "x" * 200]:
            self.assertEqual(len(calcula_hash(senha)), 10)

    def test_hash_deterministico(self):
        self.assertEqual(calcula_hash("marcelo123"), calcula_hash("marcelo123"))

    def test_multiplicador_muda_hash(self):
        self.assertNotEqual(
            calcula_hash("Marcelo123!", multiplicador=12),
            calcula_hash("Marcelo123!", multiplicador=31),
        )

    def test_login(self):
        cadastrado = calcula_hash("marcelo123")
        self.assertTrue(verifica_senha("marcelo123", cadastrado))
        self.assertFalse(verifica_senha("oi", cadastrado))

    def test_pbkdf2(self):
        salt, h = gera_hash_pbkdf2("marcelo123", iteracoes=1000)
        self.assertTrue(verifica_pbkdf2("marcelo123", salt, h, iteracoes=1000))
        self.assertFalse(verifica_pbkdf2("outra", salt, h, iteracoes=1000))


class TestForcaBruta(unittest.TestCase):
    def test_gera_hashes(self):
        hashes = gera_hashes(SENHAS_COMUNS)
        self.assertEqual(len(hashes), len(SENHAS_COMUNS))
        self.assertTrue(all(h.startswith("0x") for h in hashes))

    def test_senha_comum_e_encontrada(self):
        self.assertEqual(encontra_senha_comum(calcula_hash("123456")), "123456")

    def test_senha_incomum_nao_e_encontrada(self):
        self.assertIsNone(encontra_senha_comum(calcula_hash("marcelo123")))

    def test_forca_bruta_acha_senha_curta(self):
        alvo = calcula_hash("mar")
        achada = forca_bruta(alvo, "abcdefghijklmnopqrstuvwxyz", tamanho=3)
        self.assertEqual(calcula_hash(achada), alvo)

    def test_forca_bruta_sem_resultado(self):
        self.assertIsNone(forca_bruta(calcula_hash("zzz"), "abc", tamanho=3))


if __name__ == "__main__":
    unittest.main()
