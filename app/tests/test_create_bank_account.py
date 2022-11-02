import re
import unittest

from ..Konto import Konto


class TestCreateBankAccount(unittest.TestCase):

    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "50030384515"
    kod = "PROM_NNE"

    def test_tworzenie_konta(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel, self.kod)
        self.assertEqual(konto.imie, self.imie,
                         "Imie nie zostało zapisane!")
        self.assertEqual(konto.nazwisko, self.nazwisko,
                         "Nazwisko nie zostało zapisane!")
        self.assertEqual(konto.pesel, self.pesel,
                         "Pesel nie został zapisany!")
        self.assertEqual(konto.saldo, 0, "Saldo nie jest zerowe.")

    def test_za_dlugi_pesel(self, konto):
        konto = Konto(self.imie, self.nazwisko, self.pesel, self.kod)
        konto.pesel = "05555858488485582756"
        self.assertEqual(len(konto.pesel), "Niepoprawny pesel!")

    def test_za_krotki_pesel(self, konto):
        konto = Konto(self.imie, self.nazwisko, self.pesel, self.kod)
        konto.pesel = "055558"
        self.assertEqual(len(konto.pesel), "Niepoprawny pesel!")

    # realizacja kodu rabatowego
    def test_niepoprawny_kod_rabatowy(self, konto):
        konto = Konto(self.imie, self. nazwisko, self.pesel)
        konto.kod_rabatowy = "ccc"
        self.assertTrue(
            konto.kod_rabatowy, "Błędny kod rabatowy")
        self.assertEqual(konto.saldo, 0, "Saldo nie jest zerowe!")

    def test_poprawny_kod_rabatowy(self, konto):
        konto = Konto(self.imie, self. nazwisko, self.pesel)
        konto.kod_rabatowy = "PROM_5845"
        self.assertFalse(
            konto.kod_rabatowy, "Błędny kod rabatowy")
        # sprawdzanie czy konto zostało doładowane
        self.assertEqual(konto.saldo, 50, "Kod nie zadziałał.")
