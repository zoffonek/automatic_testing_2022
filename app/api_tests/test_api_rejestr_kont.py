
import unittest
import requests

class TestRejestrKontAPI(unittest.TestCase):
    body = {
        "imie": "Maria",
        "nazwisko": "Monica",
        "pesel": "99101155984"
    }
    
    url = "http://localhost:5000"
    
    def test_1_tworzenie_konta(self):
        utworz_konto_res = requests.post(self.url + "/konta/stworz_konto", json = self.body)
        self.assertEqual(utworz_konto_res.status_code, 201)
    
    def test_2_wyszukanie_stworzonego_konta(self):
        znajdz_konto_res = requests.get(self.url + "/konta/konto/" + self.body['pesel'])
        self.assertEqual(znajdz_konto_res.status_code, 200)
        res_json = znajdz_konto_res.json()
        self.assertEqual(res_json["imie"], self.body["imie"])
        self.assertEqual(res_json["nazwisko"], self.body["nazwisko"])
        self.assertEqual(res_json["saldo"], 0)
    
        
        
    
    