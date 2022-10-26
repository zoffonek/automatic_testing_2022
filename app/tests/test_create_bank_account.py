import string
import unittest

from ..Konto import Konto


class TestCreateBankAccount(unittest.TestCase):

    def test_tworzenie_konta(self):
        imie = "Dariusz"
        nazwisko = "Januszewski"
        pesel = 90030384515
        pierwsze_konto = Konto(imie, nazwisko, pesel)
        self.assertEqual(pierwsze_konto.imie, "Dariusz",
                         "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, "Januszewski",
                         "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")
        self.assertEqual(pierwsze_konto.pesel, pesel,
                         "Brak numeru pesel!")  # feature 2
        self.assertEqual(len(str(pierwsze_konto.pesel)) == 11,
                         True, "Niepoprawny pesel!")

    # tutaj proszę dodawać nowe testy
