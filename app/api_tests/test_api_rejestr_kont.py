
import unittest
import requests

class TestRejestrKontAPI(unittest.TestCase):
    body = {
        "imie": "Maria",
        "nazwisko": "Monica",
        "pesel": "99101155984"
    }
    
    body_update = {
        "imie": "Anna"
    }
    
    body2 = {
        "imie": "Laura",
        "nazwisko": "Palmer",
        "pesel": "99101155984"
    }
    
    url = "http://localhost:5000"
    

    
    def test_1a_tworzenie_konta(self):
        utworz_konto_res = requests.post(self.url + "/konta/stworz_konto", json = self.body)
        self.assertEqual(utworz_konto_res.status_code, 201)
  
    def test_1b_tworzenie_konta_istniejacy_pesel(self):
        utworz_drugie_konto_res = requests.post(self.url + "/konta/stworz_konto", json = self.body2)
        self.assertEqual(utworz_drugie_konto_res.status_code, 400)      
    
    
    def test_2_wyszukanie_stworzonego_konta(self):
        znajdz_konto_res = requests.get(self.url + "/konta/konto/" + self.body['pesel'])
        self.assertEqual(znajdz_konto_res.status_code, 200)
        znalezione_konto = znajdz_konto_res.json()
        self.assertEqual(znalezione_konto["imie"], self.body["imie"])
        self.assertEqual(znalezione_konto["nazwisko"], self.body["nazwisko"])
        self.assertEqual(znalezione_konto["saldo"], 0)
        
    def test_3_aktualizacja_konta(self):
        znajdz_konto_res = requests.get(self.url + "/konta/konto/" + self.body['pesel'])
        self.assertEqual(znajdz_konto_res.status_code, 200)
        znalezione_konto = znajdz_konto_res.json()
        aktualizuj_konto_res = requests.put(self.url + "/konta/konto/" + self.body['pesel'], json = self.body_update)
        oczekiwane_dane = {**znalezione_konto, **self.body_update}
        self.assertEqual(aktualizuj_konto_res.status_code, 200)
        zaktualizowane_konto_res = requests.get(self.url + "/konta/konto/" + oczekiwane_dane["pesel"])
        self.assertEqual(zaktualizowane_konto_res.status_code, 200)
        zaktualizowane_dane = zaktualizowane_konto_res.json()
          
        self.assertEqual(zaktualizowane_dane["imie"], oczekiwane_dane["imie"])   
        self.assertEqual(zaktualizowane_dane["nazwisko"], oczekiwane_dane["nazwisko"])   
        self.assertEqual(zaktualizowane_dane["pesel"], oczekiwane_dane["pesel"])   
        self.assertEqual(zaktualizowane_dane["saldo"], oczekiwane_dane["saldo"])  
        
    def test_4_usuwanie_konta(self):
        ilosc_kont_przed_usuwaniem = int(requests.get(self.url + "/konta/ile_kont").json())
        usun_konto_res = requests.delete(self.url + "/konta/konto/" + self.body['pesel'])
        self.assertEqual(usun_konto_res.status_code, 200)
        ilosc_kont_po_usuniencu = int(requests.get(self.url + "/konta/ile_kont").json())
        self.assertEqual(ilosc_kont_przed_usuwaniem - 1, ilosc_kont_po_usuniencu)
        
    
    