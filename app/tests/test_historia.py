import unittest

from ..Konto import Konto, KontoFirmowe


class TestHistoria(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "50030384515"

    nazwa_firmy = "Januszex sp. z o.o."
    nip = "8461627563"

    def test_udana_historia_przychodzace(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.przelew_przychodzacy(50)
        konto.przelew_przychodzacy(100)
        konto.przelew_przychodzacy(20)
        self.assertEqual(konto.historia, [
                         50, 100, 20], "Nieudany zapis historii - przychodzące")

    def test_nieudana_historia_wychodzace(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 150
        konto.przelew_wychodzacy(50)
        konto.przelew_wychodzacy(100)
        konto.przelew_wychodzacy(20)
        self.assertEqual(
            konto.historia, [-50, -100], "Nieudany zapis historii - wychodzące")

    def test_udana_historia_wychodzace(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 60000
        konto.przelew_wychodzacy(35)
        konto.przelew_wychodzacy(110)
        konto.przelew_wychodzacy(200)
        self.assertEqual(
            konto.historia, [-35, -110, -200], "Nieudany zapis historii - wychodzące")

    def test_udana_historia_ekspres(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 60000
        konto.przelew_ekspresowy(35)
        konto.przelew_ekspresowy(110)
        konto.przelew_ekspresowy(200)
        self.assertEqual(
            konto.historia, [-35, -1, -110, -1, -200, -1], "Nieudany zapis historii - wychodzące (ekspres)")

    def test_nieudana_historia_ekspres(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 40
        konto.przelew_ekspresowy(35)
        konto.przelew_ekspresowy(5)
        konto.przelew_ekspresowy(200)
        self.assertEqual(
            konto.historia, [-35, -1], "Nieudany zapis historii - wychodzące (ekspres)")

    # przelewy firmowe

    def test_udana_historia_przychodzace_firma(self):
        konto = KontoFirmowe(self.nazwa_firmy, self.nip)
        konto.przelew_przychodzacy(50)
        konto.przelew_przychodzacy(100)
        konto.przelew_przychodzacy(20)
        self.assertEqual(konto.historia, [
                         50, 100, 20], "Nieudany zapis historii - przychodzące, firma")

    def test_nieudana_historia_wychodzace_firma(self):
        konto = KontoFirmowe(self.nazwa_firmy, self.nip)
        konto.saldo = 150
        konto.przelew_wychodzacy(50)
        konto.przelew_wychodzacy(100)
        konto.przelew_wychodzacy(20)
        self.assertEqual(
            konto.historia, [-50, -100], "Nieudany zapis historii - wychodzące firma")

    def test_udana_historia_wychodzace_firma(self):
        konto = KontoFirmowe(self.nazwa_firmy, self.nip)
        konto.saldo = 60000
        konto.przelew_wychodzacy(35)
        konto.przelew_wychodzacy(110)
        konto.przelew_wychodzacy(200)
        self.assertEqual(
            konto.historia, [-35, -110, -200], "Nieudany zapis historii - wychodzące firma")

    def test_udana_historia_ekspres_firma(self):
        konto = KontoFirmowe(self.nazwa_firmy, self.nip)
        konto.saldo = 60000
        konto.przelew_ekspresowy(35)
        konto.przelew_ekspresowy(110)
        konto.przelew_ekspresowy(200)
        self.assertEqual(
            konto.historia, [-35, -5, -110, -5, -200, -5], "Nieudany zapis historii - wychodzące (ekspres - firma)")

    def test_nieudana_historia_ekspres_firma(self):
        konto = KontoFirmowe(self.nazwa_firmy, self.nip)
        konto.saldo = 40
        konto.przelew_ekspresowy(35)
        konto.przelew_ekspresowy(5)
        konto.przelew_ekspresowy(200)
        self.assertEqual(
            konto.historia, [-35, -5], "Nieudany zapis historii - wychodzące (ekspres - firma)")
