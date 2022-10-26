import re
import unittest

from ..Konto import Konto


class TestCreateBankAccount(unittest.TestCase):

    def test_tworzenie_konta(self):
        imie01 = "Dariusz"
        nazwisko01 = "Januszewski"
        pesel01 = 90030384515
        kod01 = "PROM_NNE"
        pierwsze_konto = Konto(imie01, nazwisko01, pesel01, kod01)

        self.assertEqual(pierwsze_konto.imie, imie01,
                         "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, nazwisko01,
                         "Nazwisko nie zostało zapisane!")

        # sprawdzanie numeru pesel
        self.assertEqual(pierwsze_konto.pesel, pesel01,
                         "Brak numeru pesel!")  # feature 2
        self.assertEqual(len(str(pierwsze_konto.pesel)),
                         11, "Niepoprawny pesel!")

        # realizacja kodu rabatowego

        def sprawdzanie_kodu_rabatowego(kod, saldo):
            if (kod != None):
                pattern = re.compile(r"PROM_([a-zA-Z0-9]){3}")
                self.assertTrue(re.match(pattern, kod), "Błędny kod rabatowy")
                self.assertEqual(len(kod), 8, "Niepoprawna długość kodu.")

                # sprawdzanie czy konto zostało doładowane
                self.assertEqual(saldo, 50, "Kod nie zadziałał.")

            else:
                self.assertEqual(saldo, 0, "Saldo nie jest zerowe!")

        sprawdzanie_kodu_rabatowego(
            pierwsze_konto.kod_rabatowy, pierwsze_konto.saldo)
