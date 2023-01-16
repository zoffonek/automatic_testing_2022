from app.Konto import Konto


class RejestrKont(object):
    lista_kont = []

    @classmethod
    def dodaj_konto(cls, konto):
        cls.lista_kont.append(konto)

    @classmethod
    def znajdz_konto(cls, pesel):
        for konto in cls.lista_kont:
            if konto.pesel==pesel:
                return konto
        return "Account doesn't exist!"

    @classmethod
    def ile_kont(cls):
        return len(cls.lista_kont)

    @classmethod
    def usun_konto_z_peselem(cls, pesel):
        for konto in cls.lista:
            if konto.pesel == pesel:
                cls.lista.remove(konto)
