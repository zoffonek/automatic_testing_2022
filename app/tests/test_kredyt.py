import unittest
from parameterized import parameterized, parameterized_class

from ..Konto import Konto


class TestKredytu(unittest.TestCase):
    imie = "Arnold"
    nazwisko = "Januszewski"
    pesel = "50030384515"

    def setUp(self):
        self.konto = Konto(self.imie, self.nazwisko, self.pesel)

    @parameterized.expand([
        # warunek 1
        ([-25, 100, 100, 100], 25, True, 25),  # yes
        ([100, -100, 100], 100, False, 0),  # no
        ([100], 500, False, 0),  # no
        # warunek 2
        ([-100, 100, -100, 100, 500], 200, True, 200),  # yes
        ([-100, 100, -100, 100, 100], 500, False, 0)  # no

    ])
    def test_przyznany_kredyt(self, historia, kwota, przyznanie, saldo):
        self.konto.historia = historia
        czy_przyznany = self.konto.zaciagnij_kredyt(kwota)
        self.assertEqual(czy_przyznany, przyznanie)
        self.assertEqual(self.konto.saldo, saldo)

    # def test_nieprzyznany_kredyt_warunek1_1(self, historia, kwota, saldo):
    #     self.konto.historia = historia
    #     czy_przyznany = self.konto.zaciagnij_kredyt(kwota)
    #     self.assertFalse(czy_przyznany)
    #     self.assertEqual(self.konto.saldo, saldo)

    # def test_nieprzyznany_kredyt_warunek1_2(self, historia, kwota, saldo):
    #     self.konto.historia = historia
    #     czy_przyznany = self.konto.zaciagnij_kredyt(kwota)
    #     self.assertFalse(czy_przyznany)
    #     self.assertEqual(self.konto.saldo, saldo)

    # # warunek 2

    # def test_przyznany_kredyt_warunek2(self, historia, kwota, saldo):
    #     self.konto.historia = historia
    #     czy_przyznany = self.konto.zaciagnij_kredyt(kwota)
    #     self.assertTrue(czy_przyznany)
    #     self.assertEqual(self.konto.saldo, saldo)

    # def test_nieprzyznany_kredyt_warunek2(self, historia, kwota, saldo):
    #     self.konto.historia = historia
    #     czy_przyznany = self.konto.zaciagnij_kredyt(kwota)
    #     self.assertFalse(czy_przyznany)
    #     self.assertEqual(self.konto.saldo, saldo)
