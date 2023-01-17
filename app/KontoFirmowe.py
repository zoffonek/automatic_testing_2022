from datetime import date
import os
from urllib import request
from app.Konto import Konto


class KontoFirmowe(Konto):
    
    url_mf = os.getenv('BANK_APP_MF_URL', 'https://wl-test.mf.gov.pl/')

    def __init__(self, nazwa_firmy, nip):
        self.nazwa_firmy = nazwa_firmy
        self.nip = nip if len(nip) == 10 else "Niepoprawny NIP!"
        self.saldo = 0
        self.historia = []
        self.oplata_ekspres = 5

    def przelew_przychodzacy(self, kwota):
        return super().przelew_przychodzacy(kwota)

    def przelew_wychodzacy(self, kwota):
        return super().przelew_wychodzacy(kwota)

    def przelew_ekspresowy(self, kwota):
        return super().przelew_ekspresowy(kwota)

    # _____________________kredyt_________________________

    def przelew_do_ZUS_min_1(self):
        return (-1775 in self.historia)

    def min_2x_wieksze_saldo_od_kwoty(self, kwota):
        return sum(self.historia) >= kwota

    def zaciagnij_kredyt(self, kwota):
        if self.przelew_do_ZUS_min_1() and \
                self.min_2x_wieksze_saldo_od_kwoty(kwota):
            self.saldo += kwota
            return True
        return False
    
    # _____________________NIP_________________________

    @classmethod
    def walidacja_nip_api(self, nip):
        today = str(date.today())
        endpoint = f"{self.url_mf}api/search/nip/{nip}?date={today}"
        print(f"Request to {endpoint}")
        res = request.get(endpoint)
        print(f"Response {nip}: {res.status_code}, {res.json()}")
        if res.status_code == 200:
            return True 
        self.nip = "Pranie!"