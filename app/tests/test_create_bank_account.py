import re
import unittest

from ..Konto import Konto


class TestCreateBankAccount(unittest.TestCase):

    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "50030384515"

    def test_tworzenie_konta(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        self.assertEqual(konto.imie, self.imie,
                         "Imie nie zostało zapisane!")
        self.assertEqual(konto.nazwisko, self.nazwisko,
                         "Nazwisko nie zostało zapisane!")
        self.assertEqual(konto.pesel, self.pesel,
                         "Pesel nie został zapisany!")
        self.assertEqual(konto.saldo, 0, "Saldo nie jest zerowe.")

    def test_za_dlugi_pesel(self):
        pesel = "05555858488485582756"
        konto = Konto(self.imie, self.nazwisko, pesel)
        self.assertEqual(konto.pesel, "Niepoprawny pesel!")

    def test_za_krotki_pesel(self):
        pesel = "055558"
        konto = Konto(self.imie, self.nazwisko, pesel)
        self.assertEqual(konto.pesel, "Niepoprawny pesel!")

    # realizacja kodu rabatowego
    def test_niepoprawny_kod_rabatowy(self):
        kod_rabatowy = "ccc"
        konto = Konto(self.imie, self.nazwisko, self.pesel, kod_rabatowy)
        self.assertEqual(
            konto.kod_rabatowy, "Błędny kod rabatowy!")
        self.assertEqual(konto.saldo, 0, "Saldo nie jest zerowe!")

    def test_poprawny_kod_rabatowy_i_niepoprawne_warunki(self):
        kod_rabatowy = "PROM_585"
        pesel = "50030384515"
        konto = Konto(self.imie, self.nazwisko, pesel, kod_rabatowy)
        self.assertEqual(
            konto.kod_rabatowy, "Błędny kod rabatowy!")
        # sprawdzanie czy konto nie zostało doładowane
        self.assertEqual(
            konto.saldo, 0, "Warunki nie zostały spełnione, a saldo wzrosło!")

    def test_poprawny_kod_rabatowy_i_warunki(self):
        kod_rabatowy = "PROM_585"
        pesel = "70030384515"
        konto = Konto(self.imie, self.nazwisko, pesel, kod_rabatowy)
        self.assertNotEqual(
            konto.kod_rabatowy, "Błędny kod rabatowy!")
        # sprawdzanie czy konto zostało doładowane
        self.assertEqual(konto.saldo, 50, "Kod nie zadziałał.")
