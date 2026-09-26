# -*- coding: utf-8 -*-
"""1. klase, 98. stunda: «Kurš skaitlis pazudis vienādībā?»

Nezināmais var būt jebkurā vietā: 8 + ? = 15, ? − 6 = 9, 14 − ? = 5.
Palīdz skaitļa mājiņa: atrod, kas ir «viss» un kas - daļas.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, majina)

TEMA = "Kurš skaitlis pazudis vienādībā?"

MERKIS = ("Šodien noteiksim nezināmo skaitli vienādībā ar «+», «−» un "
          "«=».")

SATURS = [
    Sakums("8 + ? = 15 - kurš skaitlis pazudis?",
           zimejums=majina(15, [(8, None)]),
           paraksts="15 ir viss, 8 - viena daļa, ? - otra: 7.",
           fakti=["Atrodi «visu» un daļas.",
                  "Trūkst daļas - atņem.",
                  "Trūkst visa - saskaiti."]),

    Doma("Viss un daļas",
         "Saskaitīšanā summa ir viss; atņemšanā viss ir pirmais skaitlis.",
         soli=[
             "8 + ? = 15: viss 15, daļa 8 → 15 − 8 = 7.",
             "? − 6 = 9: viss nezināms → 9 + 6 = 15.",
             "14 − ? = 5: viss 14, daļa 5 → 14 − 5 = 9.",
         ]),

    Ievadi("Atrodi pazudušo", [
        {"jaut": "8 + ? = 15", "atb": ["7"], "padoms": "15 − 8."},
        {"jaut": "? + 6 = 13", "atb": ["7"], "padoms": "13 − 6."},
        {"jaut": "? − 6 = 9", "atb": ["15"], "padoms": "9 + 6."},
        {"jaut": "14 − ? = 5", "atb": ["9"], "padoms": "14 − 5."},
        {"jaut": "17 − ? = 10", "atb": ["7"], "padoms": "17 − 10."},
        {"jaut": "? + 9 = 18", "atb": ["9"], "padoms": "18 − 9."},
    ], pamats=4),

    Varianti("Saskaitīt vai atņemt?", [
        {"jaut": "Lai atrastu ? vienādībā ? − 4 = 8, jā...",
         "opcijas": ["saskaita 8 + 4", "atņem 8 − 4"], "jaukt": False,
         "pareizi": 0, "padoms": "Trūkst visa."},
        {"jaut": "Lai atrastu ? vienādībā 5 + ? = 12, jā...",
         "opcijas": ["atņem 12 − 5", "saskaita 12 + 5"], "jaukt": False,
         "pareizi": 0, "padoms": "Trūkst daļas."},
    ]),

    Pasaule("Paslēptās konfektes",
            Ievadi("", [
                {"jaut": "Mammai bija dažas konfektes. Viņa iedeva 6, palika "
                         "8. Cik bija sākumā?", "atb": ["14"],
                 "padoms": "? − 6 = 8."},
            ]),
            pavediens="maja",
            konteksts="Ne vienmēr zināms, cik bija sākumā.",
            kapec="Vienādība ar «?» palīdz atrast pazudušo."),

    Kopsavilkums([
        "Atrodu nezināmo vienādībā.",
        "Nosaku, kas ir viss un kas - daļas.",
        "Pārbaudu, ievietojot skaitli.",
    ]),

    Majas([
        "Izdomā 3 vienādības ar «?» dažādās vietās.",
        "Palūdz mājiniekam atrast.",
        "Pārbaudi viņa atbildes.",
    ]),
]
