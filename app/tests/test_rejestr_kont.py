import unittest
from ..Konto import Konto
from ..RejestrKont import RejestrKont


class TestRejestrKont(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "50030384515"

    @classmethod
    def tearDownClass(cls):
        RejestrKont.lista_kont = []
        
    @classmethod
    def setUpClass(cls):
        cls.tearDownClass
        konto = Konto(cls.imie, cls.nazwisko, cls.pesel)
        RejestrKont.dodaj_konto(konto)

    def test_1_dodawanie_konta(self):
        konto = Konto(self.imie, self.nazwisko, '98120545612')
        RejestrKont.dodaj_konto(konto)
        print(RejestrKont.lista_kont)
        self.assertEqual(RejestrKont.ile_kont(), 2)

    def test_2_dodawanie_konta(self):
        konto = Konto(self.imie, self.nazwisko, '99120545612')
        RejestrKont.dodaj_konto(konto)
        print(RejestrKont.lista_kont)
        self.assertEqual(RejestrKont.ile_kont(), 3)


    def test_3_znajdywanie_peselu(self):
        self.assertEqual(RejestrKont.znajdz_konto(
            self.pesel).pesel, self.pesel)

    def test_4_usuwanie_konta(self):
        self.assertEqual(RejestrKont.znajdz_konto(
            self.pesel).pesel, self.pesel)
        RejestrKont.usun_konto(
            self.pesel)
        self.assertEqual(RejestrKont.znajdz_konto(
            self.pesel), None)

    
    