import unittest

from ..Konto import Konto
from ..KontoFirmowe import KontoFirmowe


class TestKsiegowaniePrzelwow(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "50030384515"

    nazwa_firmy = "Januszex sp. z o.o."
    nip = "8461627563"

    def test_udany_przelew_ekspresowy(self):
        konto = Konto(self.imie, self. nazwisko, self.pesel)
        konto.saldo = 600
        konto.przelew_ekspresowy(50)
        self.assertEqual(konto.saldo, 600-50-1)

    def test_nieudany_przelew_ekspresowy(self):
        konto = Konto(self.imie, self. nazwisko, self.pesel)
        konto.saldo = 600
        konto.przelew_ekspresowy(1000)
        self.assertEqual(konto.przelew_ekspresowy(
            1000), "Nie udany przelew ekspresowy!")

    def test_udany_przelew_ekspresowy_firmowy(self):
        kwota = 600
        konto = KontoFirmowe(self.nazwa_firmy, self.nip)
        konto.saldo = 600
        konto.przelew_ekspresowy(kwota)
        self.assertEqual(konto.saldo, 600-kwota-5)

    def test_nieudany_przelew_ekspresowy_firmowy(self):
        konto = KontoFirmowe(self.nazwa_firmy, self.nip)
        konto.saldo = 600
        self.assertEqual(konto.przelew_ekspresowy(
            5000), "Nie udany przelew ekspresowy!")
