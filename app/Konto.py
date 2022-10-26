class Konto:
    def __init__(self, imie, nazwisko, pesel, kod_rabatowy=None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.saldo = 0
        self.pesel = pesel  # feature_2
        self.kod_rabatowy = kod_rabatowy  # fearute_3

        # bonus za kod rabatowy
        if (self.kod_rabatowy != None) and (self.pesel[0:2] > "60") and (self.pesel[4] < "8"):
            self.saldo += 50
