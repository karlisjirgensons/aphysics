# -*- coding: utf-8 -*-
"""2. klase, 18. stunda: «Cik apmēram?»

Pirms mērīšanas garumu novērtē pēc acumēra, un pēc tam pārbauda. Ja gals
iznāk starp iedaļām, garumu noapaļo līdz tuvākajam veselajam centimetram -
tuvāk kurai iedaļai, tā ir atbilde.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Varianti, lineals)

TEMA = "Cik apmēram?"

MERKIS = ("Šodien novērtēsim garumu pēc acumēra un pārbaudīsim to, mērot "
          "līdz tuvākajam veselajam centimetram.")

SATURS = [
    Sakums("Cik garš ir šis nogrieznis - apmēram?",
           zimejums=lineals(10, [(0, 6.8, "")], mm=True),
           paraksts="Gals ir starp 6 un 7, tuvāk 7.",
           fakti=["Apmēram 7 cm.",
                  "Acumērs - novērtējums, skatoties ar aci.",
                  "Labs acumērs ļauj pamanīt kļūdu mērījumā."]),

    Doma("Tuvākais veselais centimetrs",
         "Ja gals ir starp iedaļām, izvēlas to, kura ir tuvāk.",
         soli=[
             "Atrodi, starp kuriem centimetriem ir gals.",
             "Paskaties uz vidus iedaļu (5 mm).",
             "Ja gals ir pirms vidus - ņem mazāko skaitli.",
             "Ja pēc vidus - ņem lielāko.",
         ]),

    Ievadi("Apmēram cik cm?", [
        {"jaut": "Apmēram cik cm?", "zim": lineals(10, [(0, 4.2, "")],
                                                   mm=True),
         "atb": ["4"], "padoms": "Tuvāk 4."},
        {"jaut": "Apmēram cik cm?", "zim": lineals(10, [(0, 8.7, "")],
                                                   mm=True),
         "atb": ["9"], "padoms": "Tuvāk 9."},
        {"jaut": "Apmēram cik cm?", "zim": lineals(10, [(0, 2.9, "")],
                                                   mm=True),
         "atb": ["3"], "padoms": "Gandrīz 3."},
        {"jaut": "Apmēram cik cm?", "zim": lineals(10, [(0, 5.1, "")],
                                                   mm=True),
         "atb": ["5"], "padoms": "Tikko pāri 5."},
        {"jaut": "Apmēram cik cm?", "zim": lineals(10, [(0, 1.8, "")],
                                                   mm=True),
         "atb": ["2"], "padoms": "Tuvāk 2."},
        {"jaut": "Apmēram cik cm?", "zim": lineals(10, [(0, 7.3, "")],
                                                   mm=True),
         "atb": ["7"], "padoms": "Tuvāk 7."},
    ], pamats=4),

    Varianti("Kurš novērtējums ticams?", [
        {"jaut": "Mācību grāmatas garums", "opcijas": ["25 cm", "5 cm",
                                                        "2 m"],
         "pareizi": 0, "padoms": "Iedomājies lineālu."},
        {"jaut": "Durvju augstums", "opcijas": ["2 m", "20 cm", "10 m"],
         "pareizi": 0, "padoms": "Pieaugušais iziet cauri."},
        {"jaut": "Tava pirksta garums", "opcijas": ["6 cm", "60 cm",
                                                     "6 mm"],
         "pareizi": 0, "padoms": "Salīdzini ar lineālu."},
        {"jaut": "Klases tāfeles garums", "opcijas": ["3 m", "30 cm",
                                                       "30 m"],
         "pareizi": 0, "padoms": "Tāfele ir garāka par skolotāju."},
    ]),

    Petijums("Minēšanas spēle", [
        "Izvēlies 4 lietas klasē.",
        "Katrai uzraksti savu novērtējumu cm.",
        "Izmēri un noapaļo līdz veselam cm.",
        "Par cik tu kļūdījies? Kurš klasē minēja visprecīzāk?",
    ], vajag="lineāls, mērlente, lapa tabulai"),

    Pasaule("Cik garu diegu nogriezt?",
            Varianti("", [
                {"jaut": "Aprocei vajag diegu ap roku - apmēram 15 cm. Kuru "
                         "gabalu nogriezt?",
                 "opcijas": ["20 cm - lai pietiek mezglam",
                             "10 cm", "15 mm"], "pareizi": 0,
                 "padoms": "Mezglam vajag nedaudz rezervē."},
                {"jaut": "Izmērīts 14 cm 8 mm. Apmēram cik cm?",
                 "opcijas": ["15 cm", "14 cm", "148 cm"], "pareizi": 0,
                 "padoms": "8 mm ir tuvāk nākamajam cm."},
            ]),
            pavediens="maja",
            konteksts="Pērļu aprocei jānogriež diegs.",
            kapec="Apmērs palīdz nenogriezt par īsu."),

    Kopsavilkums([
        "Novērtēju garumu pēc acumēra.",
        "Noapaļoju mērījumu līdz tuvākajam veselajam cm.",
        "Atšķiru ticamu novērtējumu no neticama.",
    ]),

    Majas([
        "Novērtē pēc acumēra 3 lietu garumu mājās.",
        "Izmēri un salīdzini ar novērtējumu.",
        "Pieraksti, par cik kļūdījies.",
    ]),
]
