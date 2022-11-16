import unittest

from ..Konto import Konto


class TestKredytu(unittest.TestCase):
    imie = "Arnold"
    nazwisko = "Januszewski"
    pesel = "50030384515"

    # warunek 1
    def test_przyznany_kredyt_warunek1(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.historia = [100, -100, 100, 100, 100]
        kwota_kredytu = 500
        czy_przyznany = konto.zaciagnij_kredyt(kwota_kredytu)
        self.assertTrue(czy_przyznany)
        self.assertEqual(konto.saldo, kwota_kredytu)

    def test_nieprzyznany_kredyt_warunek1_1(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.historia = [100, 100, -100]
        kwota_kredytu = 500
        czy_przyznany = konto.zaciagnij_kredyt(kwota_kredytu)
        self.assertFalse(czy_przyznany)
        self.assertEqual(konto.saldo, 0)

    def test_nieprzyznany_kredyt_warunek1_2(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.historia = [100]
        kwota_kredytu = 500
        czy_przyznany = konto.zaciagnij_kredyt(kwota_kredytu)
        self.assertFalse(czy_przyznany)
        self.assertEqual(konto.saldo, 0)

    # warunek 2

    def test_przyznany_kredyt_warunek2(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.historia = [-100, 100, -100, 100, 500]
        kwota_kredytu = 200
        czy_przyznany = konto.zaciagnij_kredyt(kwota_kredytu)
        self.assertTrue(czy_przyznany)
        self.assertEqual(konto.saldo, kwota_kredytu)

    def test_nieprzyznany_kredyt_warunek2(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.historia = [-100, 100, -100, 100, 100]
        kwota_kredytu = 500
        czy_przyznany = konto.zaciagnij_kredyt(kwota_kredytu)
        self.assertFalse(czy_przyznany)
        self.assertEqual(konto.saldo, 0)
