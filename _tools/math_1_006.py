# -*- coding: utf-8 -*-
"""1. klase, 6. stunda: «Kāds būs nākamais?»

Ritmiska virkne: grupa, kas atkārtojas. Nākamo elementu nevis min, bet
nolasa no likuma - «aplis, trijstūris, aplis, trijstūris...». Skolēns
pastāsta, kā izdomāja.
"""

from math_saturs import (Doma, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, bildes)

TEMA = "Kāds būs nākamais?"

MERKIS = ("Šodien turpināsim virknes un pastāstīsim, kā izdomājām "
          "nākamo.")

_FIG = ["aplis", "trijsturis", "kvadrats", "zvaigzne", "sirds"]
_VARDI = {"aplis": "aplis", "trijsturis": "trijstūris",
          "kvadrats": "kvadrāts", "zvaigzne": "zvaigzne", "sirds": "sirds",
          "aplis*": "oranžs aplis"}


def _virkne(elementi):
    return bildes([list(elementi) + [None]])


def _karta(elementi, pareizais, citi):
    return {"jaut": "Kas būs nākamais?", "zim": _virkne(elementi),
            "opcijas": [_VARDI[pareizais]] + [_VARDI[c] for c in citi],
            "pareizi": 0, "padoms": "Atrodi grupu, kas atkārtojas."}


SATURS = [
    Sakums("Aplis, trijstūris, aplis, trijstūris... kas tālāk?",
           zimejums=_virkne(["aplis", "trijsturis"] * 3),
           paraksts="Grupa «aplis, trijstūris» atkārtojas.",
           fakti=["Virknē kāda grupa atkārtojas atkal un atkal.",
                  "Atrodi grupu - tad zini nākamo.",
                  "Pastāsti, kā izdomāji."]),

    Doma("Atrodi, kas atkārtojas",
         "Nākamo neuzmin, bet nolasi no grupas, kas atkārtojas.",
         soli=[
             "Nosauc virkni skaļi no sākuma.",
             "Atrodi vietu, kur viss sākas no jauna.",
             "Turpini ar grupas nākamo elementu.",
         ]),

    Varianti("Turpini virkni", [
        _karta(["aplis", "trijsturis"] * 3, "aplis", ["trijsturis",
                                                       "kvadrats"]),
        _karta(["kvadrats", "kvadrats", "zvaigzne"] * 2, "kvadrats",
               ["zvaigzne", "aplis"]),
        _karta(["aplis", "aplis*"] * 3, "aplis", ["aplis*", "sirds"]),
        _karta(["sirds", "zvaigzne", "aplis"] * 2, "sirds",
               ["aplis", "zvaigzne"]),
        _karta(["trijsturis", "aplis", "aplis"] * 2, "trijsturis",
               ["aplis", "kvadrats"]),
        _karta(["zvaigzne", "kvadrats", "kvadrats", "zvaigzne",
                "kvadrats"], "kvadrats", ["zvaigzne", "aplis"]),
    ], pamats=4),

    Varianti("Kā tu to izdomāji?", [
        {"jaut": "Aplis, trijstūris, aplis, trijstūris. Kas atkārtojas?",
         "opcijas": ["aplis un trijstūris", "tikai aplis",
                     "trīs trijstūri"],
         "pareizi": 0, "padoms": "Grupā ir divi."},
        {"jaut": "Sirds, zvaigzne, aplis, sirds, zvaigzne, aplis. Cik "
                 "figūru ir grupā?",
         "opcijas": ["3", "2", "6"], "pareizi": 0,
         "padoms": "Sirds, zvaigzne, aplis - un no jauna."},
    ]),

    Pasaule("Krelles",
            Varianti("", [
                {"jaut": "Anna ver krelles. Kāda pērle būs nākamā?",
                 "zim": _virkne(["aplis", "aplis*", "aplis*"] * 2),
                 "opcijas": ["violeta", "oranža"], "jaukt": False,
                 "pareizi": 0, "padoms": "Viena violeta, divas oranžas."},
                {"jaut": "Un pēc tās?",
                 "opcijas": ["oranža", "violeta"], "jaukt": False,
                 "pareizi": 0, "padoms": "Pēc violetās nāk oranža."},
            ]),
            pavediens="maja",
            konteksts="Krellēs pērles bieži ir pēc rakstura, kas atkārtojas.",
            kapec="Kas zina grupu, zina arī, kādas pērles vajadzēs."),

    Kopsavilkums([
        "Atrodu grupu, kas virknē atkārtojas.",
        "Turpinu virkni ar nākamo elementu.",
        "Pastāstu, kā izdomāju.",
    ]),

    Majas([
        "Saliec no karotēm un dakšām virkni, kas atkārtojas.",
        "Atrodi mājās rakstu, kas atkārtojas (flīzes, audums).",
        "Uzzīmē virkni un palūdz kādam to turpināt.",
    ]),
]
