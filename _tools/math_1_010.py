# -*- coding: utf-8 -*-
"""1. klase, 10. stunda: «Kā figūra dabū savu vārdu?»

Daudzstūra vārds nāk no stūru (virsotņu) skaita: trīs stūri - trijstūris,
četri - četrstūris, pieci - piecstūris. Malu ir tikpat, cik stūru. Krāsa
un lielums vārdu nemaina.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, figura)

TEMA = "Kā figūra dabū savu vārdu?"

MERKIS = ("Šodien nosauksim trijstūri, četrstūri un piecstūri pēc stūru un "
          "malu skaita.")

_TRIJ = figura([(0, 0), (6, 0), (2, 4)])
_CETR = figura([(0, 0), (6, 0), (5, 4), (1, 3)])
_PIEC = figura([(1, 0), (5, 0), (6, 3), (3, 5), (0, 3)])
_KVADR = figura([(0, 0), (4, 0), (4, 4), (0, 4)])
_SESS = figura([(1, 0), (4, 0), (5, 2), (4, 4), (1, 4), (0, 2)])

SATURS = [
    Sakums("Kāpēc trijstūri sauc par trijstūri?",
           zimejums=_TRIJ,
           paraksts="Trīs stūri - trijstūris.",
           fakti=["Stūri sauc par virsotni.",
                  "Malu ir tikpat, cik stūru.",
                  "Krāsa un lielums vārdu nemaina."]),

    Slidnis("Saskaiti stūrus", [
        {"v": "3", "teksts": "Trīs stūri - trijstūris", "zim": _TRIJ},
        {"v": "4", "teksts": "Četri stūri - četrstūris", "zim": _CETR},
        {"v": "5", "teksts": "Pieci stūri - piecstūris", "zim": _PIEC},
    ]),

    Doma("Vārds no stūriem",
         "Saskaiti stūrus - skaitlis ir figūras vārdā.",
         soli=[
             "Pieskaries katram stūrim un skaiti.",
             "3 - trijstūris, 4 - četrstūris, 5 - piecstūris.",
             "Pārbaudi: saskaiti arī malas.",
         ],
         pieze="Kvadrāts arī ir četrstūris - tam ir 4 stūri."),

    Varianti("Kā figūru sauc?", [
        {"jaut": "Kā sauc šo figūru?", "zim": _PIEC,
         "opcijas": ["piecstūris", "četrstūris", "trijstūris"],
         "pareizi": 0, "padoms": "Saskaiti stūrus."},
        {"jaut": "Kā sauc šo figūru?", "zim": _CETR,
         "opcijas": ["četrstūris", "trijstūris", "piecstūris"],
         "pareizi": 0, "padoms": "Saskaiti stūrus."},
        {"jaut": "Vai kvadrāts ir četrstūris?", "zim": _KVADR,
         "opcijas": ["Jā", "Nē"], "jaukt": False, "pareizi": 0,
         "padoms": "Tam ir 4 stūri."},
        {"jaut": "Kā sauc šo figūru?", "zim": _TRIJ,
         "opcijas": ["trijstūris", "četrstūris", "piecstūris"],
         "pareizi": 0, "padoms": "Saskaiti stūrus."},
    ]),

    Ievadi("Saskaiti", [
        {"jaut": "Cik malu ir piecstūrim?", "atb": ["5"],
         "padoms": "Malu tikpat, cik stūru."},
        {"jaut": "Cik stūru ir šai figūrai?", "zim": _SESS, "atb": ["6"],
         "padoms": "Pieskaries katram."},
        {"jaut": "Cik stūru ir 2 trijstūriem kopā?", "atb": ["6"],
         "padoms": "3 un vēl 3."},
    ]),

    Pasaule("Figūras uz ielas",
            Varianti("", [
                {"jaut": "Ceļa zīme «Dodiet ceļu» ir...",
                 "opcijas": ["trijstūris", "četrstūris", "piecstūris"],
                 "pareizi": 0, "padoms": "Tai ir 3 stūri."},
                {"jaut": "Logs parasti ir...",
                 "opcijas": ["četrstūris", "trijstūris", "piecstūris"],
                 "pareizi": 0, "padoms": "Saskaiti loga stūrus."},
                {"jaut": "Mājiņa ar jumtu (zīmējumā) ir...",
                 "zim": figura([(0, 0), (4, 0), (4, 3), (2, 5), (0, 3)]),
                 "opcijas": ["piecstūris", "četrstūris", "trijstūris"],
                 "pareizi": 0, "padoms": "Četri stūri un jumta gals."},
            ]),
            pavediens="celojums",
            konteksts="Ceļā uz skolu redzam daudz figūru: zīmes, logus, "
                      "mājas.",
            kapec="Figūru vārds palīdz pastāstīt, ko redzi."),

    Kopsavilkums([
        "Nosaucu trijstūri, četrstūri un piecstūri.",
        "Saskaitu stūrus un malas.",
        "Zinu, ka krāsa un lielums vārdu nemaina.",
    ]),

    Majas([
        "Atrodi mājās 3 četrstūrus.",
        "Vai atradi trijstūri? Kur?",
        "Uzzīmē piecstūri un saskaiti tā malas.",
    ]),
]
