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

    def test_dodawanie_konta_1(self):
        konto = Konto(self.imie, self.nazwisko, '98120545612')
        RejestrKont.dodaj_konto(konto)
        print(RejestrKont.lista_kont)
        self.assertEqual(RejestrKont.ile_kont(), 2)

    def test_dodawanie_konta_2(self):
        konto = Konto(self.imie, self.nazwisko, '99120545612')
        RejestrKont.dodaj_konto(konto)
        print(RejestrKont.lista_kont)
        self.assertEqual(RejestrKont.ile_kont(), 3)


    def test_znajdywanie_peselu(self):
        self.assertEqual(RejestrKont.znajdz_konto(
            self.pesel).pesel, self.pesel)
    

    def test_znajdywanie_peselu(self):
        self.tearDownClass()
        self.assertEqual(RejestrKont.znajdz_konto(
            self.pesel), "Account doesn't exist!")
