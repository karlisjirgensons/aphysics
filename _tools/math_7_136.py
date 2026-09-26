# -*- coding: utf-8 -*-
"""7. klase, 136. stunda: «Kā pārnest saskaitāmo uz otru pusi?»

Ja nezināmais ir abās pusēs, saskaitāmos pārnes: tie ar x - uz kreiso, bez
x - uz labo. Pārnesot saskaitāmais maina zīmi - tas ir tas pats, kas
atņemt to no abām pusēm.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti)

TEMA = "Kā pārnest saskaitāmo uz otru pusi?"

MERKIS = ("Atrisināsim lineāru vienādojumu, pārnesot saskaitāmos un "
          "savelkot līdzīgos.")

SATURS = [
    Sakums("7x − 3 = 4x + 9: x abās pusēs",
           fakti=["Saskaitāmos ar x savāc vienā pusē, skaitļus - otrā.",
                  "Pārnesot zīme mainās: 4x → −4x, −3 → +3.",
                  "3x = 12, x = 4."]),

    Doma("Pārnes ar pretēju zīmi",
         "Saskaitāmo var pārnest no vienas vienādojuma puses uz otru, mainot "
         "tā zīmi uz pretējo. Tas ir tas pats, kas abām pusēm atņemt (vai "
         "pieskaitīt) šo saskaitāmo.",
         soli=[
             "Saskaitāmos ar x pārnes uz kreiso pusi.",
             "Skaitļus pārnes uz labo pusi.",
             "Katram pārnestajam maina zīmi.",
             "Savelc līdzīgos abās pusēs.",
             "Dali ar koeficientu pie x.",
         ],
         pieze="Saskaitāmie, kas paliek savā pusē, zīmi nemaina."),

    Paraugs("Pārnes un savelc",
            uzd="Atrisini 7x − 3 = 4x + 9.",
            soli=[
                ("7x − 4x = 9 + 3", "4x → kreisā (−), −3 → labā (+)."),
                ("3x = 12", "Savelk."),
                ("x = 4", "(: 3)"),
                ("Pārbaude: 28 − 3 = 25; 16 + 9 = 25", "Pareizi."),
            ],
            atbilde="x = 4"),

    Ievadi("Atrisini", [
        {"jaut": "5x + 2 = 3x + 10",
         "atb": ["4"], "padoms": "2x = 8."},
        {"jaut": "9 − 2x = x + 3",
         "atb": ["2"], "padoms": "−3x = −6."},
        {"jaut": "4x − 7 = 6x + 5",
         "atb": ["−6", "-6"], "padoms": "−2x = 12."},
        {"jaut": "x + 1 = 13 − 2x",
         "atb": ["4"], "padoms": "3x = 12."},
        {"jaut": "0,3x + 2 = 0,1x + 3",
         "atb": ["5"], "padoms": "0,2x = 1."},
        {"jaut": "12 − 5x = 2 − 3x",
         "atb": ["5"], "padoms": "−2x = −10."},
    ], pamats=4),

    Varianti("Kur kļūda?", [
        {"jaut": "6x − 2 = 4x + 8 → 6x + 4x = 8 − 2",
         "opcijas": ["Zīmes nomainītas nepareizi: jābūt 6x − 4x = 8 + 2",
                     "Pareizi", "Jāpārnes skaitļi pa kreisi",
                     "Jādala ar 6"],
         "pareizi": 0, "padoms": "Pārnestais maina zīmi."},
        {"jaut": "3x = 5x − 8 → −2x = −8 → x = −4",
         "opcijas": ["Kļūda dalot: x = 4", "Pareizi",
                     "Kļūda pārnesot", "Jābūt x = −8"],
         "pareizi": 0, "padoms": "−8 : (−2) = 4."},
    ]),

    Pasaule("Divi krājkonti panāk viens otru",
            Ievadi("", [
                {"jaut": "Anna: 60 € + 5 € nedēļā. Pēteris: 20 € + 9 € nedēļā. "
                         "Pēc cik nedēļām vienādi? (60 + 5n = 20 + 9n)",
                 "atb": ["10"], "padoms": "40 = 4n."},
                {"jaut": "Cik € tad katram?",
                 "atb": ["110"], "padoms": "60 + 50."},
                {"jaut": "Kuram būs vairāk pēc 15 nedēļām - «Anna» vai "
                         "«Pēteris»?",
                 "atb": ["Pēteris", "peteris", "pēteris"],
                 "padoms": "155 > 135.", "tastatura": "text"},
            ]),
            pavediens="veikals",
            konteksts="Kurš krāj ātrāk, tas agrāk vai vēlāk panāk - "
                      "vienādojums pasaka, kad.",
            kapec="x abās pusēs - pārnešana."),

    Kopsavilkums([
        "Pārnesu saskaitāmos ar zīmes maiņu.",
        "Savācu x vienā pusē, skaitļus - otrā.",
        "Savelku un dalu ar koeficientu.",
        "Pārbaudu sakni sākotnējā vienādojumā.",
    ]),

    Majas([
        "Atrisini: 11x − 4 = 5x + 20; 3 − 4x = 2x − 9.",
        "Izdomā «panākšanas» uzdevumu un atrisini.",
        "Paskaidro, kāpēc pārnešana maina zīmi.",
    ]),
]
