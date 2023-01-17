# RapidAPI Client

from flask import Flask, request, jsonify
from app.RejestrKont import RejestrKont
from app.Konto import Konto

app = Flask(__name__)


@app.route("/konta/stworz_konto", methods=['POST'])
def stworz_konto():
    dane = request.get_json()
    print(f"Request o stworzenie konta z danymi: {dane}")
    if RejestrKont.znajdz_konto(dane["pesel"])!=None: 
        return jsonify("Konto o podanym peselu już istnieje"), 400
    konto = Konto(dane["imie"], dane["nazwisko"], dane["pesel"])
    RejestrKont.dodaj_konto(konto)
    return jsonify("Konto stworzone"), 201


@app.route("/konta/ile_kont", methods=['GET'])
def ile_kont():
    liczba_kont = RejestrKont.ile_kont()
    print(f"Ilosc kont w rejestrze {liczba_kont}")
    return jsonify(liczba_kont), 200


@app.route("/konta/konto/<pesel>", methods=['GET'])
def wyszukaj_konto_z_peselem(pesel):
    print(f"Szukanie konta z peselem: {pesel}")
    konto = RejestrKont.znajdz_konto(pesel)
    print(konto)
    if konto==None: return "Nie znaleziono konta", 404
    return jsonify(imie=konto.imie, nazwisko=konto.nazwisko, saldo=konto.saldo, pesel=konto.pesel), 200

@app.route("/konta/konto/<pesel>", methods=['PUT'])
def aktualizuj_konto(pesel):
    nowe_dane = request.get_json()
    print(f"Aktualizacja konta z peselem: {pesel}")
    konto = RejestrKont.znajdz_konto(pesel)
    if konto==None: return jsonify("Konto o podanym peselu nie istnieje"), 404
    konto.imie = nowe_dane["imie"] if "imie" in nowe_dane else konto.imie
    konto.nazwisko = nowe_dane["nazwisko"] if "nazwisko" in nowe_dane else konto.nazwisko
    konto.pesel = nowe_dane["pesel"] if "pesel" in nowe_dane else konto.pesel
    konto.saldo = nowe_dane["saldo"] if "saldo" in nowe_dane else konto.saldo
    print("Zaktualizowano")
    return jsonify("Zaktualizowano"), 200

@app.route("/konta/konto/<pesel>", methods=['DELETE'])
def usun_konto(pesel):
    print(f"Usuwanie konta z peselem: {pesel}")
    RejestrKont.usun_konto(pesel)
    return jsonify(f"Konto z peselem {pesel} zostalo usuniete"), 200