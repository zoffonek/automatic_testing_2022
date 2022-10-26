class Konto:
    def __init__(self, imie, nazwisko, pesel, kod_rabatowy=None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.saldo = 0
        self.pesel = pesel  # feature_2
        self.kod_rabatowy = kod_rabatowy  # fearute_3

        # bonus za kod rabatowy
        if (self.kod_rabatowy != None):
            self.saldo += 50
