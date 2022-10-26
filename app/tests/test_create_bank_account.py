import re
import unittest

from ..Konto import Konto


class TestCreateBankAccount(unittest.TestCase):

    def test_tworzenie_konta(self):

        # konto seniora
        imie_01 = "Dariusz"
        nazwisko_01 = "Januszewski"
        pesel_01 = "50030384515"
        kod_01 = "PROM_NNE"
        konto_01 = Konto(imie_01, nazwisko_01, pesel_01, kod_01)

        # konto normalne
        imie_02 = "Grażyna"
        nazwisko_02 = "Januszewska"
        pesel_02 = "61011225848"
        kod_02 = "PROM_K26"
        konto_02 = Konto(imie_02, nazwisko_02, pesel_02, kod_02)

        # sprawdzanie czy informacje zostały zapisane
        self.assertEqual(konto_01.imie, imie_01,
                         "Imie nie zostało zapisane!")
        self.assertEqual(konto_01.nazwisko, nazwisko_01,
                         "Nazwisko nie zostało zapisane!")
        self.assertEqual(konto_01.pesel, pesel_01,
                         "Pesel nie został zapisany!")

        self.assertEqual(konto_02.imie, imie_02,
                         "Imie nie zostało zapisane!")
        self.assertEqual(konto_02.nazwisko, nazwisko_02,
                         "Nazwisko nie zostało zapisane!")
        self.assertEqual(konto_02.pesel, pesel_02,
                         "Pesel nie został zapisany!")

        def sprawdzanie_poprawnosci_nr_pesel(konto):
            self.assertTrue(isinstance(konto.pesel, str),
                            "Pesel nie może być liczbą!")
            self.assertEqual(len(konto.pesel),
                             11, "Niepoprawny pesel!")

        # sprawdzanie peseli dla kont
        sprawdzanie_poprawnosci_nr_pesel(konto_01)
        sprawdzanie_poprawnosci_nr_pesel(konto_01)

        # realizacja kodu rabatowego
        def sprawdzanie_kodu_rabatowego(konto):
            if (konto.kod_rabatowy != None) and (konto.pesel[0:2] > "60") and (konto.pesel[4] < "8"):
                pattern = re.compile(r'^PROM_([a-zA-Z0-9]){3}$')
                self.assertTrue(
                    re.match(pattern, konto.kod_rabatowy), "Błędny kod rabatowy")

                # sprawdzanie czy konto zostało doładowane
                self.assertEqual(konto.saldo, 50, "Kod nie zadziałał.")

            else:
                self.assertEqual(konto.saldo, 0, "Saldo nie jest zerowe!")

        # sprawdzanie kodów dla kont
        sprawdzanie_kodu_rabatowego(konto_01)
        sprawdzanie_kodu_rabatowego(konto_02)

        # sprawdzenie czy konta na pewno się różnią rabatem
        self.assertTrue(konto_01.saldo != konto_02.saldo)
