# -*- coding: utf-8 -*-
"""2. klase, 142. stunda: «Kā aprēķināt vairāku vienādu pirkumu summu?»

Veikalā: 4 bulciņas pa 3 € - 3 + 3 + 3 + 3 = 4 · 3 = 12 €. Vienādu
saskaitāmo summu pieraksta kā reizinājumu - īsāk un ātrāk.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, restis)

TEMA = "Kā aprēķināt vairāku vienādu pirkumu summu?"

MERKIS = ("Šodien pierakstīsim vienādu saskaitāmo summu kā reizinājumu un "
          "aprēķināsim rezultātu.")

_CENAS = restis([["prece", "cena"], ["burtnīca", "2 €"],
                 ["zīmulis", "1 €"], ["lineāls", "3 €"],
                 ["krāsas", "5 €"]])

SATURS = [
    Sakums("Cik maksā 4 lineāli pa 3 €?",
           zimejums=_CENAS,
           paraksts="3 + 3 + 3 + 3 = 4 · 3 = 12 €.",
           fakti=["Vienādi pirkumi - vienādi saskaitāmie.",
                  "Tos pieraksta kā reizinājumu.",
                  "Pirmais - cik gabalu, otrais - cena."]),

    Doma("Vienādi pirkumi",
         "Kopējā cena = gabalu skaits · viena gabala cena.",
         soli=[
             "Atrodi viena gabala cenu.",
             "Saskaiti, cik gabalu pērk.",
             "Pieraksti reizinājumu.",
             "Aprēķini un pieraksti mērvienību.",
         ]),

    Paraugs("3 burtnīcas",
            uzd="Burtnīca maksā 2 €. Cik maksā 3 burtnīcas?",
            soli=[("2 + 2 + 2", "Summa."), ("3 · 2 = 6", "Reizinājums.")],
            atbilde="6 €"),

    Ievadi("Cik maksā?", [
        {"jaut": "5 zīmuļi pa 1 €?", "zim": _CENAS, "atb": ["5"],
         "mers": "€", "padoms": "5 · 1."},
        {"jaut": "7 burtnīcas pa 2 €?", "zim": _CENAS, "atb": ["14"],
         "mers": "€", "padoms": "7 · 2."},
        {"jaut": "6 lineāli pa 3 €?", "zim": _CENAS, "atb": ["18"],
         "mers": "€", "padoms": "6 · 3."},
        {"jaut": "3 krāsu komplekti pa 5 €?", "zim": _CENAS, "atb": ["15"],
         "mers": "€", "padoms": "3 · 5 = 5 + 5 + 5."},
        {"jaut": "9 lineāli pa 3 €?", "zim": _CENAS, "atb": ["27"],
         "mers": "€", "padoms": "9 · 3."},
        {"jaut": "10 burtnīcas pa 2 €?", "zim": _CENAS, "atb": ["20"],
         "mers": "€", "padoms": "10 · 2."},
    ], pamats=4),

    Varianti("Kurš pieraksts?", [
        {"jaut": "Cena 3 € + 3 € + 3 € + 3 € + 3 €",
         "opcijas": ["5 · 3 €", "3 · 3 €", "5 + 3 €"], "pareizi": 0,
         "padoms": "Pieci pirkumi."},
        {"jaut": "Kas ir lētāk: 4 burtnīcas vai 3 lineāli?", "zim": _CENAS,
         "opcijas": ["4 burtnīcas - 8 €", "3 lineāli - 9 €", "vienādi"],
         "pareizi": 0, "padoms": "4 · 2 un 3 · 3."},
    ]),

    Pasaule("Iepirkšanās skolai",
            Ievadi("", [
                {"jaut": "Nopirka 3 burtnīcas un 2 lineālus. Cik kopā? "
                         "(3 · 2 + 2 · 3)", "zim": _CENAS, "atb": ["12"],
                 "mers": "€", "padoms": "6 + 6."},
                {"jaut": "Samaksāja ar 20 €. Cik atdeva?", "atb": ["8"],
                 "mers": "€", "padoms": "20 − 12."},
            ]),
            pavediens="veikals",
            konteksts="Pirms skolas pērk vairākus vienādus piederumus.",
            kapec="Reizināšana saīsina garas summas."),

    Kopsavilkums([
        "Pierakstu vienādu pirkumu summu kā reizinājumu.",
        "Aprēķinu kopējo cenu.",
        "Pierakstu atbildi ar mērvienību.",
    ]),

    Majas([
        "Atrodi mājās čeku, kur nopirktas vairākas vienādas preces.",
        "Pārbaudi summu ar reizināšanu.",
        "Izdomā uzdevumu mājiniekam.",
    ]),
]
