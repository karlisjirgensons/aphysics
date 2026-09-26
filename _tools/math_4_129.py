# -*- coding: utf-8 -*-
"""4. klase, 129. stunda: «Kāda daļa no kilometra?»

Daļa no lieluma mazākās mērvienībās: {1|4} km = 250 m, {1|2} kg = 500 g,
{3|4} h = 45 min. Vispirms veselo pārvērš mazākajā vienībā, tad dala.
Tā mērvienības no 5. stundas sastopas ar daļām.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, restis)

TEMA = "Kāda daļa no kilometra?"

MERKIS = ("Pārveidosim pamatdaļu no lieluma mazākās mērvienībās (puse "
          "kilograma, ceturtdaļa kilometra).")

SATURS = [
    Sakums("Cik metru ir ceturtdaļkilometrs?",
           zimejums=restis([["daļa", "no 1 km", "no 1 kg", "no 1 l"],
                            ["1/2", "500 m", "500 g", "500 ml"],
                            ["1/4", "250 m", "250 g", "250 ml"],
                            ["1/10", "100 m", "100 g", "100 ml"]],
                           "1000 dalās ērti"),
           fakti=["Kilo- nozīmē tūkstoš.",
                  "Tāpēc daļas no km, kg un l ir ērti rēķināt."]),

    Doma("Pārvērt mazākā vienībā, tad dali",
         "Lai atrastu daļu no lieluma, veselo izsaka mazākā mērvienībā un "
         "tad dala ar saucēju (un reizina ar skaitītāju).",
         soli=[
             "1 km = 1000 m.",
             "{1|4} km = 1000 : 4 = 250 m.",
             "{3|4} km = 3 · 250 = 750 m.",
             "Atbildi raksti ar mazāko mērvienību.",
         ],
         pieze="{1|5} h = 60 : 5 = 12 min; {1|5} m = 100 : 5 = 20 cm."),

    Paraugs("{3|8} kg",
            uzd="Cik gramu ir {3|8} kg?",
            soli=[
                ("1 kg = 1000 g", None),
                ("1000 : 8 = 125 g", "{1|8} kg."),
                ("3 · 125 = 375 g", None),
            ],
            atbilde="375 g"),

    Ievadi("Pārvērt", [
        {"jaut": "{1|2} km = ? m", "atb": ["500"], "padoms": "1000 : 2."},
        {"jaut": "{3|4} kg = ? g", "atb": ["750"], "padoms": "3 · 250."},
        {"jaut": "{1|5} m = ? cm", "atb": ["20"], "padoms": "100 : 5."},
        {"jaut": "{2|5} l = ? ml", "atb": ["400"], "padoms": "2 · 200."},
        {"jaut": "{3|10} km = ? m", "atb": ["300"], "padoms": "3 · 100."},
        {"jaut": "{1|4} € = ? ct", "atb": ["25"], "padoms": "100 : 4."},
    ], pamats=4),

    Varianti("Kas ir vairāk?", [
        {"jaut": "{1|2} kg vai 400 g?",
         "opcijas": ["{1|2} kg", "400 g", "vienādi"], "pareizi": 0,
         "padoms": "500 g > 400 g."},
        {"jaut": "{1|4} km vai 300 m?",
         "opcijas": ["300 m", "{1|4} km", "vienādi"], "pareizi": 0,
         "padoms": "250 m < 300 m."},
        {"jaut": "{3|4} l vai 750 ml?",
         "opcijas": ["vienādi", "{3|4} l", "750 ml"], "pareizi": 0,
         "padoms": "{3|4} l = 750 ml."},
    ]),

    Pasaule("Skrējiens un maltīte",
            Ievadi("", [
                {"jaut": "Stadiona aplis ir {2|5} km. Cik metru?",
                 "atb": ["400"], "padoms": "1000 : 5 · 2."},
                {"jaut": "Pēc skrējiena izdzēra {3|4} l ūdens. Cik ml?",
                 "atb": ["750"], "padoms": "1000 : 4 · 3."},
                {"jaut": "Maltītei {1|4} kg makaronu. Cik gramu?",
                 "atb": ["250"], "padoms": "1000 : 4."},
                {"jaut": "Skrējiens ilga {5|12} stundas. Cik minūšu?",
                 "atb": ["25"], "padoms": "60 : 12 · 5."},
            ]),
            pavediens="sports",
            konteksts="Sportistu ēdienkartēs un treniņos daļas no kg, l un "
                      "km ir ikdiena.",
            kapec="Daļa no lieluma kļūst saprotama mazākās vienībās."),

    Kopsavilkums([
        "Izsaku daļu no km, kg, l, h mazākās vienībās.",
        "Vispirms pārvēršu, tad dalu.",
        "Salīdzinu lielumus, kas doti ar daļām un vienībām.",
    ]),

    Majas([
        "Atrodi virtuvē iepakojumu un izrēķini {1|4} no tā gramos.",
        "Izrēķini, cik metru ir {3|4} no tava ceļa uz skolu.",
        "Pārvērt: {1|5} kg, {1|8} km, {2|3} h.",
    ]),
]
