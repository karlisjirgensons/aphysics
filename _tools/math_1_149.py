# -*- coding: utf-8 -*-
"""1. klase, 149. stunda: «Kurš skaitlis trūkst?»

Nezināmo 100 apjomā meklē ar «mēģinu un pārbaudu»: 30 + ? = 70 - mēģinu
30, 40 - pārbaudu: 30 + 40 = 70. Mēģinājumus pieraksta.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, restis)

TEMA = "Kurš skaitlis trūkst?"

MERKIS = ("Šodien noteiksim vienādībā nezināmo lielumu ar paņēmienu «mēģinu "
          "un pārbaudu».")

_MEG = restis([["mēģinu", "pārbaude", "?"], [30, "30 + 30 = 60", "maz"],
               [40, "30 + 40 = 70", "✓"]])

SATURS = [
    Sakums("30 + ? = 70 - kā atrast?",
           zimejums=_MEG,
           paraksts="Mēģinu 30 - par maz; mēģinu 40 - der!",
           fakti=["Izvēlies skaitli un pārbaudi.",
                  "Par maz? Mēģini lielāku.",
                  "Par daudz? Mēģini mazāku."]),

    Doma("Mēģinu un pārbaudu",
         "Katrs mēģinājums pasaka, vai iet uz augšu vai uz leju.",
         soli=[
             "Izvēlies gudru pirmo mēģinājumu.",
             "Ievieto un izrēķini.",
             "Salīdzini ar vajadzīgo - maini.",
             "Pieraksti mēģinājumus tabulā.",
         ]),

    Ievadi("Atrodi", [
        {"jaut": "30 + ? = 70", "atb": ["40"], "padoms": "Mēģini 40."},
        {"jaut": "? + 25 = 45", "atb": ["20"], "padoms": "Mēģini 20."},
        {"jaut": "80 − ? = 50", "atb": ["30"], "padoms": "80 − 30."},
        {"jaut": "56 + ? = 59", "atb": ["3"], "padoms": "Vieni."},
        {"jaut": "? − 10 = 44", "atb": ["54"], "padoms": "44 + 10."},
        {"jaut": "47 − ? = 40", "atb": ["7"], "padoms": "Vieni prom."},
    ], pamats=4),

    Varianti("Ko darīt tālāk?", [
        {"jaut": "20 + ? = 90. Mēģināju 50: 20 + 50 = 70.",
         "opcijas": ["mēģināt lielāku", "mēģināt mazāku", "gatavs"],
         "jaukt": False, "pareizi": 0, "padoms": "70 < 90."},
        {"jaut": "60 − ? = 20. Mēģināju 30: 60 − 30 = 30.",
         "opcijas": ["mēģināt lielāku", "mēģināt mazāku", "gatavs"],
         "jaukt": False, "pareizi": 0,
         "padoms": "Jāpaliek mazāk - jāatņem vairāk."},
    ]),

    Pasaule("Uzkrājums",
            Ievadi("", [
                {"jaut": "Velosipēds 90 €. Tev ir 60 €. Cik vēl jākrāj?",
                 "atb": ["30"], "padoms": "60 + ? = 90."},
            ]),
            pavediens="veikals",
            konteksts="Tu krāj naudu velosipēdam.",
            kapec="«Cik vēl?» - nezināmais saskaitāmais."),

    Kopsavilkums([
        "Atrodu nezināmo ar mēģināšanu.",
        "Pārbaudu katru mēģinājumu.",
        "Pierakstu mēģinājumus.",
    ]),

    Majas([
        "Izdomā vienādību ar «?» mājiniekam.",
        "Vērojiet, cik mēģinājumos viņš atrod.",
        "Mainieties.",
    ]),
]
