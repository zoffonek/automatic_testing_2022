import unittest

from Konto import Konto, KontoFirmowe

class TestKredytu(unittest.TestCase):
    imie = "Arnold"
    nazwisko = "Januszewski"
    pesel = "50030384515"

    # warunek 1
    def test_przyznany_kredyt_warunek1(self):
        konto=Konto(self.imie,self.nazwisko,self.pesel)
        konto.historia = [100,-100,100,100,100]
        kwota_kredytu = 500
        self.assertTrue(konto.zaciagnij_kredyt(kwota_kredytu))
        self.assertEqual(konto.saldo, kwota_kredytu)

    def test_nieprzyznany_kredyt_warunek1_1(self):
        konto=Konto(self.imie,self.nazwisko,self.pesel)
        konto.historia = [100,100, -100]
        kwota_kredytu = 500
        self.assertFalse(konto.zaciagnij_kredyt(kwota_kredytu))
        self.assertEqual(konto.saldo, 0)

    def test_nieprzyznany_kredyt_warunek1_2(self):
        konto=Konto(self.imie,self.nazwisko,self.pesel)
        konto.historia = [100]
        kwota_kredytu = 500
        self.assertFalse(konto.zaciagnij_kredyt(kwota_kredytu))
        self.assertEqual(konto.saldo, 0)

    
    # warunek 2

    def test_przyznany_kredyt_warunek2(self):
        konto=Konto(self.imie,self.nazwisko,self.pesel)
        konto.historia = [-100,100,-100,100,100]
        kwota_kredytu = 200
        konto.zaciagnij_kredyt(kwota_kredytu)
        self.assertTrue(konto.zaciagnij_kredyt)
        self.assertEqual(konto.saldo, kwota_kredytu)

    def test_nieprzyznany_kredyt_warunek2(self):
        konto=Konto(self.imie,self.nazwisko,self.pesel)
        konto.historia = [-100,100,-100,100,100]
        kwota_kredytu = 500
        konto.zaciagnij_kredyt(kwota_kredytu)
        self.assertFalse(konto.zaciagnij_kredyt)
        self.assertEqual(konto.saldo, 0)


