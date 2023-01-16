from app.Konto import Konto


class RejestrKont(object):
    lista_kont = []


    @classmethod
    def znajdz_konto(cls, pesel):
        for konto in cls.lista_kont:
            if konto.pesel==pesel:
                return konto
    
    @classmethod
    def dodaj_konto(cls, konto):
        cls.lista_kont.append(konto)


    @classmethod
    def ile_kont(cls):
        return len(cls.lista_kont)
                