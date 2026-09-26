# -*- coding: utf-8 -*-
"""4. klase, 149. stunda: «Kā atrast nezināmo malu?»

Formula otrādi: ja S = a · b un zināms S un a, tad b = S : a. Tas pats
nezināmais reizinātājs, ko skolēns zina no reizināšanas tabulas.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, figura)

TEMA = "Kā atrast nezināmo malu?"

MERKIS = ("Aprēķināsim taisnstūra malas garumu, ja zināms laukums un otra "
          "mala.")

SATURS = [
    Sakums("Laukums 24, garums 6. Cik plats?",
           zimejums=figura([(0, 0), (6, 0), (6, 4), (0, 4)],
                           uzraksti=[(3, -0.5, "6"), (6.8, 2, "?")],
                           platums=8, augstums=5),
           paraksts="24 : 6 = 4.",
           fakti=["Laukums ir malu reizinājums.",
                  "Nezināmo malu atrod ar dalīšanu."]),

    Doma("b = S : a",
         "Ja zināms laukums S un viena mala a, otra mala b = S : a.",
         soli=[
             "Pieraksti formulu: S = a · b.",
             "Ievieto zināmo: 24 = 6 · b.",
             "Atrodi nezināmo reizinātāju: b = 24 : 6 = 4.",
             "Pārbaudi: 6 · 4 = 24.",
         ],
         pieze="Kvadrātam: ja S = 49, mala ir skaitlis, kas reiz sevi dod "
               "49 - 7."),

    Paraugs("Dārza plāns",
            uzd="Dobes laukums 36 m², garums 9 m. Cik plata dobe?",
            soli=[
                ("S = a · b", None),
                ("36 = 9 · b", None),
                ("b = 36 : 9 = 4", None),
            ],
            atbilde="4 m"),

    Ievadi("Atrodi malu", [
        {"jaut": "S = 48 cm², a = 8 cm. b = ?", "atb": ["6"],
         "padoms": "48 : 8."},
        {"jaut": "S = 72 m², a = 9 m. b = ?", "atb": ["8"],
         "padoms": "72 : 9."},
        {"jaut": "Kvadrāts S = 64 dm². Mala?", "atb": ["8"],
         "padoms": "8 · 8 = 64."},
        {"jaut": "S = 120 m², a = 15 m. b = ?", "atb": ["8"],
         "padoms": "120 : 15."},
        {"jaut": "S = 1000 m², a = 40 m. b = ?", "atb": ["25"],
         "padoms": "1000 : 40."},
        {"jaut": "Kvadrāts S = 100 cm². Perimetrs?", "atb": ["40"],
         "padoms": "Mala 10."},
    ], pamats=4),

    Varianti("Kā atrast?", [
        {"jaut": "S = 56, a = 7. b = ?",
         "opcijas": ["56 : 7 = 8", "56 · 7", "56 − 7", "7 : 56"],
         "pareizi": 0, "padoms": "Dalīšana."},
        {"jaut": "Kvadrāta S = 81. Mala?",
         "opcijas": ["9", "81", "20", "40"], "pareizi": 0,
         "padoms": "9 · 9."},
        {"jaut": "Taisnstūris S = 30, mala 5. Perimetrs?",
         "opcijas": ["22", "30", "11", "35"], "pareizi": 0,
         "padoms": "Otrā mala 6: 5 + 6 + 5 + 6."},
    ]),

    Pasaule("Paklāja pirkšana",
            Ievadi("", [
                {"jaut": "Paklājs 6 m², garums 3 m. Cik plats?", "atb": ["2"],
                 "padoms": "6 : 3."},
                {"jaut": "Istaba 20 m², platums 4 m. Garums?", "atb": ["5"],
                 "padoms": "20 : 4."},
                {"jaut": "Grīdas segums rullī 2 m plats. Cik m jānogriež "
                         "20 m² istabai?", "atb": ["10"], "padoms": "20 : 2."},
                {"jaut": "Segums maksā 12 € par m². Cik maksā 20 m²?",
                 "atb": ["240"], "padoms": "20 · 12."},
            ]),
            pavediens="maja",
            konteksts="Grīdas segumu pārdod rullī ar zināmu platumu - "
                      "garumu aprēķina no laukuma.",
            kapec="Nezināmā mala - tas, cik metru nogriezt."),

    Kopsavilkums([
        "Atrodu nezināmo malu: b = S : a.",
        "Atrodu kvadrāta malu pēc laukuma.",
        "Pārbaudu ar reizināšanu.",
    ]),

    Majas([
        "Izdomā taisnstūri ar laukumu 36 un atrodi 4 dažādus malu pārus.",
        "Aprēķini, cik m linoleja no 3 m plata ruļļa vajag 18 m² istabai.",
        "Atrodi kvadrāta malu, ja S = 144 cm².",
    ]),
]
