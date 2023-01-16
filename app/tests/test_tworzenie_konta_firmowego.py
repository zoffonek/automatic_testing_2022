import unittest

from ..Konto import Konto
from ..KontoFirmowe import KontoFirmowe


class TestTworzenieKontaFiromwego(unittest.TestCase):
    nazwa_firmy = "Januszex sp. z o.o."
    nip = "8461627563"

    def test_tworzenie_konta(self):
        konto = KontoFirmowe(self.nazwa_firmy, self.nip)
        self.assertEqual(konto.nazwa_firmy, self.nazwa_firmy)
        self.assertEqual(konto.nip, self.nip)
        self.assertEqual(konto.saldo, 0, "Saldo nie jest zerowe.")

    def test_zbyt_dlugi_nip(self):
        konto = KontoFirmowe(self.nazwa_firmy, "55555555555555555555")
        self.assertEqual(konto.nip, "Niepoprawny NIP!")

    def test_zbyt_krotki_nip(self):
        konto = KontoFirmowe(self.nazwa_firmy, "555")
        self.assertEqual(konto.nip, "Niepoprawny NIP!")
