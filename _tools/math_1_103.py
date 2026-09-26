# -*- coding: utf-8 -*-
"""1. klase, 103. stunda: «Kāds stāsts der šai izteiksmei?»

Tāpat kā 40. stundā, bet 20 apjomā un ar pāriešanu: izteiksmei (15 − 7,
8 + 6) izdomā stāstu no dzīves. Stāstā jābūt tiem pašiem skaitļiem un
pareizajai darbībai.
"""

from math_saturs import (Doma, Kopsavilkums, Majas, Pasaule, Petijums,
                         Sakums, Varianti)

TEMA = "Kāds stāsts der šai izteiksmei?"

MERKIS = ("Šodien izdomāsim dzīves stāstu dotai izteiksmei 20 apjomā.")

SATURS = [
    Sakums("15 − 7 - kāds stāsts?",
           fakti=["«Bija 15 baloni, 7 aizlidoja.»",
                  "«Autobusā 15 cilvēki, 7 izkāpa.»",
                  "Pirmais skaitlis - sākumā; «−» - kaut kas aiziet."]),

    Doma("Stāsts izteiksmei",
         "Stāstā ir sākums, notikums un jautājums.",
         soli=[
             "Sākums: pirmais skaitlis.",
             "Notikums: «+» nāk klāt, «−» aiziet.",
             "Jautājums: cik tagad?",
         ]),

    Varianti("Kurš stāsts der?", [
        {"jaut": "8 + 6",
         "opcijas": ["8 bērni rotaļlaukumā, atnāca vēl 6",
                     "8 bērni, 6 aizgāja", "6 bērni, 8 aizgāja"],
         "pareizi": 0, "padoms": "Klāt."},
        {"jaut": "15 − 7",
         "opcijas": ["15 ābolu, 7 apēda", "15 ābolu, nopirka 7",
                     "7 āboli, 15 apēda"], "pareizi": 0,
         "padoms": "Aiziet."},
        {"jaut": "20 − 11",
         "opcijas": ["20 € makā, samaksāja 11 €",
                     "11 € makā, samaksāja 20 €",
                     "20 € makā, atrada 11 €"], "pareizi": 0,
         "padoms": "Samaksāja - aiziet."},
    ]),

    Varianti("Kura izteiksme der stāstam?", [
        {"jaut": "Plauktā 12 grāmatas, nolika vēl 5.",
         "opcijas": ["12 + 5", "12 − 5", "5 − 12"], "pareizi": 0,
         "padoms": "Nolika - klāt."},
        {"jaut": "Dīķī 16 pīles, 9 aizlidoja.",
         "opcijas": ["16 − 9", "16 + 9", "9 − 16"], "pareizi": 0,
         "padoms": "Aizlidoja - prom."},
    ]),

    Petijums("Stāstu kartītes", [
        "Paņem kartīti ar izteiksmi (piem., 9 + 8).",
        "Izdomā stāstu par savu klasi.",
        "Uzzīmē to.",
        "Pastāsti - lai klase uzmin izteiksmi.",
    ], vajag="izteiksmju kartītes, krāsu zīmuļi"),

    Pasaule("Stāsts no pagalma",
            Varianti("", [
                {"jaut": "Kurš stāsts der 13 − 4?",
                 "opcijas": ["Pagalmā 13 baloži, 4 aizlidoja",
                             "Pagalmā 4 baloži, atlidoja 13",
                             "13 baloži un 4 kaķi"],
                 "pareizi": 0, "padoms": "Sākumā 13, aiziet 4."},
            ]),
            pavediens="daba",
            konteksts="Pagalmā vienmēr kaut kas notiek.",
            kapec="Katra izteiksme ir īss stāsts."),

    Kopsavilkums([
        "Izdomāju stāstu izteiksmei 20 apjomā.",
        "Atrodu izteiksmi stāstam.",
        "Pārbaudu darbību un skaitļus.",
    ]),

    Majas([
        "Izdomā stāstu 17 − 8 par savu māju.",
        "Izdomā stāstu 6 + 9 par pastaigu.",
        "Pastāsti vakariņās!",
    ]),
]
