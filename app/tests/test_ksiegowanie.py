import unittest

from ..Konto import Konto
from ..KontoFirmowe import KontoFirmowe


class TestKsiegowanie(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "50030384515"

    nazwa_firmy = "Januszex sp. z o.o."
    nip = "8461627563"

    # przelewy osobiste

    def test_udany_przelew_wychodzacy(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 1000
        konto.przelew_wychodzacy(800)
        self.assertEqual(konto.saldo, 1000-800)

    def test_nieudany_przelew_wychodzacy(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 100

        self.assertEqual(konto.przelew_wychodzacy(
            800), "Nie zaksiegowano przelewu wychodzącego!")

    def test_udany_przelew_przychodzacy(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 1000
        konto.przelew_przychodzacy(800)
        self.assertEqual(konto.saldo, 1000+800)

    # przelewy firmowe

    def test_udany_przelew_wychodzacy_firma(self):
        konto = KontoFirmowe(self.nazwa_firmy, self.nip)
        konto.saldo = 1000
        konto.przelew_wychodzacy(800)
        self.assertEqual(konto.saldo, 1000-800)

    def test_nieudany_przelew_wychodzacy_firma(self):
        konto = KontoFirmowe(self.nazwa_firmy, self.nip)
        konto.saldo = 100

        self.assertEqual(konto.przelew_wychodzacy(
            800), "Nie zaksiegowano przelewu wychodzącego!")

    def test_udany_przelew_przychodzacy_firma(self):
        konto = KontoFirmowe(self.nazwa_firmy, self.nip)
        konto.saldo = 1000
        konto.przelew_przychodzacy(800)
        self.assertEqual(konto.saldo, 1000+800)
