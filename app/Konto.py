from datetime import date
import re
from app.SMTPConnection import SMTPConnection

class Konto(object):
    def __init__(self, imie, nazwisko, pesel, kod_rabatowy=None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.saldo = 0
        self.pesel = pesel if len(pesel) == 11 and isinstance(
            pesel, str) else "Niepoprawny pesel!"

        self.kod_rabatowy = kod_rabatowy
        self.oplata_ekspres = 1
        self.historia = []
        
        self.tresc_email="Twoja historia konta to:"

        # _____bonus za kod rabatowy _____

        def urodzenie_po_1961():
            pesel_1961_2000 = ((int(self.pesel[0:2]) in range(
                61, 100)) and (int(self.pesel[2]) in [0, 1]))
            pesel_po_2000 = ((int(self.pesel[0:2]) in range(2, 100)) and (
                int(self.pesel[2]) in range(2, 7)))
            return (pesel_1961_2000 or pesel_po_2000)

        def poprawny_kod():
            wzor = re.compile(r'^PROM_([a-zA-Z0-9]){3}$')
            return True if re.match(wzor, self.kod_rabatowy) else False

        def zrealizuj_kod():
            if self.kod_rabatowy != None:
                if poprawny_kod() and urodzenie_po_1961():
                    self.saldo += 50
                else:
                    self.kod_rabatowy = "Błędny kod rabatowy!"

        zrealizuj_kod()

    #  ____________________przelewy___________________________

    def przelew_wychodzacy(self, kwota):
        if kwota > self.saldo:
            return "Nie zaksiegowano przelewu wychodzącego!"
        else:
            self.saldo -= kwota
            self.historia.append(-kwota)

    def przelew_przychodzacy(self, kwota):
        self.saldo += kwota
        self.historia.append(kwota)

    def przelew_ekspresowy(self, kwota):
        if self.przelew_wychodzacy(kwota) == "Nie zaksiegowano przelewu wychodzącego!":
            return "Nie udany przelew ekspresowy!"

        else:
            self.saldo -= self.oplata_ekspres
            self.historia.append(-self.oplata_ekspres)

    # _________________________kredyt ___________________________________

    def historia_niemniejsza_od_3(self):
        return len(self.historia) >= 3

    def ostatnie_3_transakcje_przychodzace(self):
        return (self.historia[-1] > 0 and self.historia[-2] > 0 and self.historia[-3] > 0)

    def suma_5_ostatnich_transakji_wieksza_od_kwoty(self, kwota):
        return (len(self.historia) >= 5 and sum(self.historia[-5:]) > kwota)

    def zaciagnij_kredyt(self, kwota):
        if self.historia_niemniejsza_od_3() and \
                (self.ostatnie_3_transakcje_przychodzace() or
                 self.suma_5_ostatnich_transakji_wieksza_od_kwoty(kwota)):
            self.saldo += kwota
            return True
        return False

    # _____________________MAIL_HISTORIA_________________________
    
    def wyslij_historie_na_maila(self, adresat, smtp):
        temat = f"Wyciąg z dnia {str(date.today())}"
        tresc = f"{self.tresc_email}{self.historia}"
        print(f"Wysylanie historii na email: {adresat}")
        if smtp.wyslij(temat, tresc, adresat):
            print("Wysylanie powiodlo sie")
            return True
        print("Wiadomosc niedostarczona")
        return False