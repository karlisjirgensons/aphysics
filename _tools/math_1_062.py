# -*- coding: utf-8 -*-
"""1. klase, 62. stunda: «Kurš skaitlis ir lielāks?»

Divciparu skaitļus salīdzina pēc desmitiem; ja desmiti vienādi - pēc
vieniem. 52 > 48, jo 5 desmiti ir vairāk nekā 4, lai gan 8 > 2.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, desmiti)

TEMA = "Kurš skaitlis ir lielāks?"

MERKIS = ("Šodien salīdzināsim divciparu skaitļus - vispirms desmitus, tad "
          "vienus.")


def _k(a, b):
    lielakais = max(a, b)
    return {"jaut": "Kurš lielāks: %d vai %d?" % (a, b),
            "opcijas": [str(a), str(b)], "jaukt": False,
            "pareizi": 0 if lielakais == a else 1,
            "padoms": ("Desmiti vienādi - salīdzini vienus."
                       if a // 10 == b // 10 else "Salīdzini desmitus.")}


SATURS = [
    Sakums("48 vai 52 - kurš lielāks? Bet 8 ir vairāk nekā 2!",
           zimejums=desmiti(5, 2),
           paraksts="52: pieci stieņi. 48: tikai četri.",
           fakti=["Vispirms salīdzina desmitus.",
                  "Kam vairāk desmitu - tas lielāks.",
                  "Ja desmiti vienādi - salīdzina vienus."]),

    Slidnis("Salīdzinām", [
        {"v": "52", "teksts": "5 desmiti un 2 vieni", "zim": desmiti(5, 2)},
        {"v": "48", "teksts": "4 desmiti un 8 vieni - mazāk",
         "zim": desmiti(4, 8)},
    ]),

    Doma("Vispirms desmiti",
         "Viens desmits ir vairāk nekā jebkurš vienu skaits līdz 9.",
         soli=[
             "Salīdzini desmitu ciparus.",
             "Dažādi? Lielākais desmits - lielākais skaitlis.",
             "Vienādi? Salīdzini vienus.",
         ]),

    Varianti("Kurš lielāks?", [
        _k(52, 48), _k(36, 39), _k(71, 17), _k(60, 59), _k(44, 40),
        _k(29, 92),
    ], pamats=4),

    Ievadi("Atrodi", [
        {"jaut": "Lielākais no 34, 43, 39", "atb": ["43"],
         "padoms": "Kuram 4 desmiti?"},
        {"jaut": "Mazākais no 65, 56, 61", "atb": ["56"],
         "padoms": "Kuram 5 desmiti?"},
        {"jaut": "Lielākais divciparu skaitlis", "atb": ["99"],
         "padoms": "9 desmiti un 9 vieni."},
        {"jaut": "Mazākais divciparu skaitlis", "atb": ["10"],
         "padoms": "1 desmits, 0 vienu."},
    ]),

    Pasaule("Kurš savāca vairāk?",
            Varianti("", [
                {"jaut": "Anna savāca 47 kastaņus, Pēteris 51. Kurš vairāk?",
                 "opcijas": ["Pēteris", "Anna"], "jaukt": False,
                 "pareizi": 0, "padoms": "5 desmiti > 4 desmiti."},
                {"jaut": "Liene 63, Marta 68. Kura vairāk?",
                 "opcijas": ["Marta", "Liene"], "jaukt": False,
                 "pareizi": 0, "padoms": "Desmiti vienādi, 8 > 3."},
            ]),
            pavediens="daba",
            konteksts="Rudenī klase vāc kastaņus dzīvnieku barošanai.",
            kapec="Salīdzinot desmitus, uzvarētāju redz uzreiz."),

    Kopsavilkums([
        "Salīdzinu vispirms desmitus.",
        "Ja desmiti vienādi, salīdzinu vienus.",
        "Atrodu lielāko un mazāko skaitli.",
    ]),

    Majas([
        "Salīdzini divu māju numurus uz ielas.",
        "Kurš vecāks: vecmāmiņa vai vectētiņš? Salīdzini gadus.",
        "Izdomā divus skaitļus ar vienādiem desmitiem.",
    ]),
]
