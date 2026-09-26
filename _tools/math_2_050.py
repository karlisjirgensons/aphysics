# -*- coding: utf-8 -*-
"""2. klase, 50. stunda: «Ko stāsta tabula un diagramma?»

Dati tabulā un stabiņu diagrammā: nolasa vērtības un rēķina ar tām -
cik kopā, par cik vairāk. Tas ir tas pats, ko 2.1. tematā dara ar
aptauju, tikai skaitļi tagad ir līdz 100.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, kolonnas, restis)

TEMA = "Ko stāsta tabula un diagramma?"

MERKIS = ("Šodien nolasīsim datus no tabulas un stabiņu diagrammas un "
          "izmantosim tos aprēķinos.")

_MAKULATURA = kolonnas([("2.a", 46), ("2.b", 38), ("2.c", 57)], " kg")
_TABULA = restis([["diena", "apmeklētāji"], ["pirmdiena", 34],
                  ["otrdiena", 28], ["trešdiena", 45]])

SATURS = [
    Sakums("Kura klase savāca visvairāk makulatūras?",
           zimejums=_MAKULATURA,
           paraksts="Augstākais stabiņš - 2.c.",
           fakti=["Diagrammā uzreiz redz, kurš ir lielākais.",
                  "Precīzu skaitli nolasa virs stabiņa.",
                  "Ar skaitļiem var rēķināt tālāk."]),

    Doma("Dati rēķiniem",
         "Vispirms nolasi vajadzīgos skaitļus, tad izvēlies darbību.",
         soli=[
             "Atrodi rindu vai stabiņu, par ko jautā.",
             "Nolasi skaitli ar mērvienību.",
             "«Kopā» - saskaiti, «par cik» - atņem.",
             "Pārbaudi, vai atbilde saskan ar attēlu.",
         ]),

    Ievadi("Diagramma", [
        {"jaut": "Cik kg savāca 2.a?", "zim": _MAKULATURA, "atb": ["46"],
         "mers": "kg", "padoms": "Nolasi virs stabiņa."},
        {"jaut": "Par cik kg 2.c savāca vairāk nekā 2.b?",
         "zim": _MAKULATURA, "atb": ["19"], "mers": "kg",
         "padoms": "57 − 38."},
        {"jaut": "Cik kg savāca 2.a un 2.b kopā?", "zim": _MAKULATURA,
         "atb": ["84"], "mers": "kg", "padoms": "46 + 38."},
        {"jaut": "Cik kg 2.b pietrūka līdz 50 kg?", "zim": _MAKULATURA,
         "atb": ["12"], "mers": "kg", "padoms": "50 − 38."},
    ]),

    Ievadi("Tabula", [
        {"jaut": "Cik apmeklētāju bibliotēkā bija otrdien?", "zim": _TABULA,
         "atb": ["28"], "padoms": "Rinda «otrdiena»."},
        {"jaut": "Cik pirmdien un otrdien kopā?", "zim": _TABULA,
         "atb": ["62"], "padoms": "34 + 28."},
        {"jaut": "Par cik trešdien vairāk nekā pirmdien?", "zim": _TABULA,
         "atb": ["11"], "padoms": "45 − 34."},
        {"jaut": "Cik trūka otrdien līdz 50?", "zim": _TABULA,
         "atb": ["22"], "padoms": "50 − 28."},
    ]),

    Varianti("Ko dati stāsta?", [
        {"jaut": "Kurā dienā bibliotēkā bija vismazāk cilvēku?",
         "zim": _TABULA, "opcijas": ["otrdien", "pirmdien", "trešdien"],
         "pareizi": 0, "padoms": "Mazākais skaitlis."},
        {"jaut": "Kurš apgalvojums ir patiess?", "zim": _MAKULATURA,
         "opcijas": ["2.c savāca vairāk nekā 2.a un 2.b katra atsevišķi",
                     "2.b savāca visvairāk",
                     "Visas savāca vienādi"], "pareizi": 0,
         "padoms": "Salīdzini stabiņus."},
    ]),

    Pasaule("Makulatūras konkurss",
            Ievadi("", [
                {"jaut": "Balvu saņem klase, kas savāc vismaz 55 kg. Par "
                         "cik kg 2.a vēl jāsavāc?", "zim": _MAKULATURA,
                 "atb": ["9"], "mers": "kg", "padoms": "55 − 46."},
            ]),
            pavediens="planeta",
            konteksts="Savākts papīrs aizbrauc uz pārstrādi, un tiek "
                      "saudzēti koki.",
            kapec="Diagramma parāda, kurai klasei jāpacenšas."),

    Kopsavilkums([
        "Nolasu skaitļus no tabulas un diagrammas.",
        "Rēķinu ar tiem: kopā un par cik vairāk.",
        "Salīdzinu datus un izdaru secinājumu.",
    ]),

    Majas([
        "Pieraksti tabulā, cik minūtes katru dienu lasi grāmatu.",
        "Pēc nedēļas uzzīmē stabiņus.",
        "Kurā dienā lasīji visvairāk?",
    ]),
]
