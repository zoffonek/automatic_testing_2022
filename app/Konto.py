import re


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

        # bonus za kod rabatowy
        def zrealizuj_kod():
            if kod_rabatowy != None:
                codePat = re.compile(r'^PROM_([a-zA-Z0-9]){3}$')
                codeCorrect = True if re.match(
                    codePat, kod_rabatowy) else False

                codeRules = (((int(self.pesel[0:2]) in range(61, 100)) and (int(self.pesel[2]) in [0, 1]))
                             or ((int(self.pesel[0:2]) in range(2, 100)) and (int(self.pesel[2]) in range(2, 7))))
                if codeCorrect and codeRules:
                    self.saldo += 50
                else:
                    self.kod_rabatowy = "Błędny kod rabatowy!"

        zrealizuj_kod()

    # przelewy

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


class KontoFirmowe(Konto):

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
