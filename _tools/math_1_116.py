# -*- coding: utf-8 -*-
"""1. klase, 116. stunda: «Cik bija sākumā?»

Uzdevumi ar nezināmu sākumu: «Dažas pīles peldēja, 4 atpeldēja klāt,
tagad 11.» - ? + 4 = 11, tātad 11 − 4 = 7. Uz sākumu iet «atpakaļ» ar
pretējo darbību.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti)

TEMA = "Cik bija sākumā?"

MERKIS = ("Šodien risināsim uzdevumus, kuros nezināms ir sākuma lielums.")

SATURS = [
    Sakums("Dažas pīles, atpeldēja vēl 4, tagad 11. Cik bija sākumā?",
           fakti=["? + 4 = 11.",
                  "Atpakaļ ar pretējo darbību: 11 − 4 = 7.",
                  "Pārbaude: 7 + 4 = 11."]),

    Paraugs("Atpakaļ uz sākumu",
            uzd="Ievai bija dažas uzlīmes. Viņa uzdāvināja 6, palika 8. Cik "
                "bija sākumā?",
            soli=[
                ("? − 6 = 8", "Uzdāvināja - atņem."),
                ("8 + 6 = 14", "Atpakaļ - pieskaita."),
                ("14 − 6 = 8", "Pārbaude."),
            ],
            atbilde="sākumā bija 14 uzlīmes."),

    Doma("Iet atpakaļ",
         "Lai atrastu sākumu, dari pretēji tam, kas notika.",
         soli=[
             "Atnāca klāt? - Atņem.",
             "Aizgāja prom? - Pieskaiti.",
             "Pārbaudi ar stāstu.",
         ]),

    Ievadi("Cik bija sākumā?", [
        {"jaut": "Dažas pīles, atpeldēja 4, tagad 11.", "atb": ["7"],
         "padoms": "11 − 4."},
        {"jaut": "Dažas konfektes, apēda 5, palika 7.", "atb": ["12"],
         "padoms": "7 + 5."},
        {"jaut": "Daži baloni, atnesa 8, tagad 17.", "atb": ["9"],
         "padoms": "17 − 8."},
        {"jaut": "Dažas grāmatas, 3 aiznesa, palika 13.", "atb": ["16"],
         "padoms": "13 + 3."},
    ]),

    Varianti("Kura darbība atpakaļ?", [
        {"jaut": "Stāstā «atnāca klāt». Lai atrastu sākumu...",
         "opcijas": ["atņem", "pieskaita"], "jaukt": False, "pareizi": 0,
         "padoms": "Pretēji."},
        {"jaut": "Stāstā «aizgāja prom». Lai atrastu sākumu...",
         "opcijas": ["pieskaita", "atņem"], "jaukt": False, "pareizi": 0,
         "padoms": "Pretēji."},
    ]),

    Pasaule("Monētas krājkasītē",
            Ievadi("", [
                {"jaut": "Tu ieliki krājkasītē 6 €, tagad tur 15 €. Cik bija "
                         "sākumā?", "atb": ["9"], "padoms": "15 − 6."},
            ]),
            pavediens="veikals",
            konteksts="Tu neatceries, cik krājkasītē bija.",
            kapec="Atpakaļ ar pretējo darbību - un zini."),

    Kopsavilkums([
        "Risinu uzdevumus ar nezināmu sākumu.",
        "Eju atpakaļ ar pretējo darbību.",
        "Pārbaudu ar stāstu.",
    ]),

    Majas([
        "Izdomā «cik bija sākumā» uzdevumu mājiniekam.",
        "Pārbaudi viņa atbildi.",
        "Izskaidro, kāpēc darbība ir pretēja.",
    ]),
]
