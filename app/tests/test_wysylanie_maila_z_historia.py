import unittest
from parameterized import parameterized
from unittest.mock import patch, MagicMock
from app.SMTPConnection import SMTPConnection
from app.Konto import Konto
from app.KontoFirmowe import KontoFirmowe
from datetime import date


class TestMailZHistoriaOsobiste(unittest.TestCase):
    imie = "Anna"
    nazwisko = "Wesołowska"
    pesel = "99012258784"

    @classmethod
    def setUp(self):
        self.konto = Konto(self.imie,self.nazwisko,self.pesel)
        
    @parameterized.expand([
        ("maria.anna@sedzia.pl", [15, -300, 200], True),
        ("marian.nowak@sedzia.pl", [1000, -20, 80], False)
    ])
    
    def test_mail_na_konto_osobiste(self, email, historia, oczekiwany_rezultat):
        self.konto.historia = historia
        smtp = SMTPConnection()
        smtp.wyslij = MagicMock(return_value = oczekiwany_rezultat)
        rezultat = self.konto.wyslij_historie_na_maila(email, smtp)
        self.assertEqual(rezultat, oczekiwany_rezultat)
        temat = f"Wyciąg z dnia {str(date.today())}"
        tresc = f"Twoja historia konta to:{historia}"
        smtp.wyslij.assert_called_once_with(temat,tresc,email)
        
class TestMailZHistoriaFirmowe(unittest.TestCase):
    nazwa_firmy = "Wesołowska S.A."
    nip = "4856715242"
    
    @patch('app.KontoFirmowe.KontoFirmowe.walidacja_nip_api', return_value=True)
    def setUp(self,mock):
        self.konto_firmowe = KontoFirmowe(self.nazwa_firmy, self.nip)
        
    @parameterized.expand([
        ("ksiegowosc@wesolowska.pl", [15, -300, 200], True),
        ("ksiegowosc@wesola.pl", [1000, -20, 80], False)
    ])
    
    def test_mail_na_konto_firmowe(self, email, historia, oczekiwany_rezultat):
        self.konto_firmowe.historia = historia
        smtp = SMTPConnection()
        smtp.wyslij = MagicMock(return_value = oczekiwany_rezultat)
        rezultat = self.konto_firmowe.wyslij_historie_na_maila(email, smtp)
        self.assertEqual(rezultat, oczekiwany_rezultat)
        temat = f"Wyciąg z dnia {str(date.today())}"
        tresc = f"Historia konta Twojej firmy to:{historia}"
        smtp.wyslij.assert_called_once_with(temat, tresc, email)