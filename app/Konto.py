import re


class Konto:
    def __init__(self, imie, nazwisko, pesel, kod_rabatowy=None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.saldo = 0
        self.pesel = pesel

        # bonus za kod rabatowy

        codePat = re.compile(r'^PROM_([a-zA-Z0-9]){3}$')
        codeCorrect = True if re.match(
            codePat, self.kod_rabatowy) else "Niepoprawny kod!"

        codeRules = (((int(self.pesel[0:2]) in range(61, 100)) and (int(self.pesel[2]) in [0, 1]))
                     or ((int(self.pesel[0:2]) in range(2, 100)) and (int(self.pesel[2]) in range(2, 7))))

        self.kod_rabatowy = kod_rabatowy if codeRules else "Niespełnione warunki promocji!"

        if codeCorrect and codeRules:
            self.saldo += 50

    def zaksieguj_przelew_wychodzacy(self, kwota):
        if kwota > self.saldo:
            return "Nie zaksiegowano przelewu przychodzącego!"
        else:
            self.saldo -= kwota

    def zaksieguj_przelew_przychodzacy(self, kwota):
        self.saldo += kwota


class KontoFirmowe(Konto):

    def __init__(self, nazwa_firmy, nip):
        self.nazwa_firmy = nazwa_firmy
        self.nip = nip if len(nip) == 10 else "Niepoprwany NIP!"
        self.saldo = 0
