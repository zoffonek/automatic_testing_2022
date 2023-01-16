import unittest
from parameterized import parameterized, parameterized_class

from ..Konto import Konto


class TestKredytuNormalnego(unittest.TestCase):
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
    def test_kredyt_przyznanie_normalny(self, historia, kwota, przyznanie, saldo):
        self.konto.historia = historia
        czy_przyznany = self.konto.zaciagnij_kredyt(kwota)
        self.assertEqual(czy_przyznany, przyznanie)
        self.assertEqual(self.konto.saldo, saldo)
