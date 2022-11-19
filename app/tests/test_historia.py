import unittest

from ..Konto import Konto, KontoFirmowe


class TestHistoria(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "50030384515"

    nazwa_firmy = "Januszex sp. z o.o."
    nip = "8461627563"

    def setUp(self):
        self.konto = Konto(self.imie, self.nazwisko, self.pesel)
        self.kontoF = KontoFirmowe(self.nazwa_firmy, self.nip)

    def test_udana_historia_przychodzace(self):
        self.konto.przelew_przychodzacy(50)
        self.konto.przelew_przychodzacy(100)
        self.konto.przelew_przychodzacy(20)
        self.assertEqual(self.konto.historia, [
                         50, 100, 20], "Nieudany zapis historii - przychodzące")

    def test_nieudana_historia_wychodzace(self):
        self.konto.saldo = 150
        self.konto.przelew_wychodzacy(50)
        self.konto.przelew_wychodzacy(100)
        self.konto.przelew_wychodzacy(20)
        self.assertEqual(
            self.konto.historia, [-50, -100], "Nieudany zapis historii - wychodzące")

    def test_udana_historia_wychodzace(self):

        self.konto.saldo = 60000
        self.konto.przelew_wychodzacy(35)
        self.konto.przelew_wychodzacy(110)
        self.konto.przelew_wychodzacy(200)
        self.assertEqual(
            self.konto.historia, [-35, -110, -200], "Nieudany zapis historii - wychodzące")

    def test_udana_historia_ekspres(self):
        self.konto.saldo = 60000
        self.konto.przelew_ekspresowy(35)
        self.konto.przelew_ekspresowy(110)
        self.konto.przelew_ekspresowy(200)
        self.assertEqual(
            self.konto.historia, [-35, -1, -110, -1, -200, -1], "Nieudany zapis historii - wychodzące (ekspres)")

    def test_nieudana_historia_ekspres(self):
        self.konto.saldo = 40
        self.konto.przelew_ekspresowy(35)
        self.konto.przelew_ekspresowy(5)
        self.konto.przelew_ekspresowy(200)
        self.assertEqual(
            self.konto.historia, [-35, -1], "Nieudany zapis historii - wychodzące (ekspres)")

    # przelewy firmowe

    def test_udana_historia_przychodzace_firma(self):
        self.kontoF.przelew_przychodzacy(50)
        self.kontoF.przelew_przychodzacy(100)
        self.kontoF.przelew_przychodzacy(20)
        self.assertEqual(self.kontoF.historia, [
                         50, 100, 20], "Nieudany zapis historii - przychodzące, firma")

    def test_nieudana_historia_wychodzace_firma(self):
        self.kontoF.saldo = 150
        self.kontoF.przelew_wychodzacy(50)
        self.kontoF.przelew_wychodzacy(100)
        self.kontoF.przelew_wychodzacy(20)
        self.assertEqual(
            self.kontoF.historia, [-50, -100], "Nieudany zapis historii - wychodzące firma")

    def test_udana_historia_wychodzace_firma(self):
        self.kontoF.saldo = 60000
        self.kontoF.przelew_wychodzacy(35)
        self.kontoF.przelew_wychodzacy(110)
        self.kontoF.przelew_wychodzacy(200)
        self.assertEqual(
            self.kontoF.historia, [-35, -110, -200], "Nieudany zapis historii - wychodzące firma")

    def test_udana_historia_ekspres_firma(self):
        self.kontoF.saldo = 60000
        self.kontoF.przelew_ekspresowy(35)
        self.kontoF.przelew_ekspresowy(110)
        self.kontoF.przelew_ekspresowy(200)
        self.assertEqual(
            self.kontoF.historia, [-35, -5, -110, -5, -200, -5], "Nieudany zapis historii - wychodzące (ekspres - firma)")

    def test_nieudana_historia_ekspres_firma(self):
        self.kontoF.saldo = 40
        self.kontoF.przelew_ekspresowy(35)
        self.kontoF.przelew_ekspresowy(5)
        self.kontoF.przelew_ekspresowy(200)
        self.assertEqual(
            self.kontoF.historia, [-35, -5], "Nieudany zapis historii - wychodzące (ekspres - firma)")
