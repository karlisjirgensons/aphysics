# -*- coding: utf-8 -*-
"""8. klase, 94. stunda: «Kāda ir daudzstūra leņķu summa?»

Bloka noslēgums: no vienas virsotnes n-stūri sadala n − 2 trijstūros,
tāpēc leņķu summa ir (n − 2) · 180°. Regulāra sešstūra leņķis 120° -
tāpēc bišu šūnas pārklāj plakni bez spraugām.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, geometrija)

TEMA = "Kāda ir daudzstūra leņķu summa?"

MERKIS = "Vispārināsim leņķu summas aprēķinu daudzstūrim ar n malām."

SATURS = [
    Sakums("Cik grādu ir piecstūra leņķiem?",
           zimejums=geometrija([("A", 0, 0), ("B", 5, 0), ("C", 6.5, 3.5),
                                ("D", 2.5, 6), ("E", -1.5, 3.5)],
                               nogriezni=["AB", "BC", "CD", "DE", "EA", "AC",
                                          "AD"],
                               iekrasot=[("ABC", 0), ("ACD", 1),
                                         ("ADE", 0)]),
           paraksts="No virsotnes A: 3 trijstūri, 3 · 180° = 540°.",
           fakti=["n-stūri no vienas virsotnes sadala n − 2 trijstūros.",
                  "Leņķu summa ir (n − 2) · 180°.",
                  "Regulāram n-stūrim visi leņķi ir vienādi."]),

    Doma("Formula",
         "Leņķu summa ir (n − 2) · 180°.",
         soli=[
             "No vienas virsotnes novelc visas diagonāles.",
             "Saskaiti trijstūrus: to ir n − 2.",
             "Reizini ar 180°.",
             "Regulāram n-stūrim viens leņķis ir summa, dalīta ar n.",
         ],
         pieze="Pārbaude: n = 3 dod 180°, n = 4 dod 360° - kā jau zinām."),

    Paraugs("Sešstūris",
            uzd="Atrodi sešstūra leņķu summu un regulāra sešstūra leņķi.",
            soli=[
                ("n − 2 = 4", "Četri trijstūri."),
                ("4 · 180° = 720°", "Leņķu summa."),
                ("720° : 6 = 120°", "Regulāra sešstūra leņķis."),
            ],
            atbilde="720° un 120°"),

    Ievadi("Aprēķini", [
        {"jaut": "Piecstūra leņķu summa?", "atb": ["540"],
         "padoms": "3 · 180."},
        {"jaut": "Desmitstūra leņķu summa?", "atb": ["1440"],
         "padoms": "8 · 180."},
        {"jaut": "Regulāra astoņstūra leņķis?", "atb": ["135"],
         "padoms": "1080 : 8."},
        {"jaut": "Leņķu summa ir 1260°. Cik malu?", "atb": ["9"],
         "padoms": "1260 : 180 = 7 = n − 2."},
        {"jaut": "Regulāra piecstūra leņķis?", "atb": ["108"],
         "padoms": "540 : 5."},
        {"jaut": "Divpadsmitstūra leņķu summa?", "atb": ["1800"],
         "padoms": "10 · 180."},
    ], pamats=4),

    Varianti("Spried", [
        {"jaut": "Cik trijstūros no vienas virsotnes sadala septiņstūri?",
         "opcijas": ["5", "7", "6", "4"],
         "pareizi": 0, "padoms": "n − 2."},
        {"jaut": "Regulāra sešstūra leņķis ir...",
         "opcijas": ["120°", "108°", "135°", "60°"],
         "pareizi": 0, "padoms": "720 : 6."},
        {"jaut": "Vai daudzstūrim var būt leņķu summa 1000°?",
         "opcijas": ["Nē - tā nedalās ar 180°", "Jā", "Tikai ieliektam",
                     "Tikai regulāram"],
         "pareizi": 0, "padoms": "Summa vienmēr ir 180° daudzkārtnis."},
    ]),

    Pasaule("Bišu šūnas",
            Ievadi("", [
                {"jaut": "Bišu šūnas ir regulāri sešstūri. Cik grādu ir "
                         "katram leņķim?",
                 "atb": ["120"], "padoms": "720 : 6."},
                {"jaut": "Cik šūnu satiekas vienā virsotnē?", "atb": ["3"],
                 "padoms": "360 : 120."},
                {"jaut": "Vai ar regulāriem piecstūriem var pārklāt plakni bez "
                         "spraugām? (1 - jā, 0 - nē)",
                 "atb": ["0"], "padoms": "360 : 108 nav vesels skaitlis."},
            ]),
            pavediens="daba",
            konteksts="Bites būvē sešstūra šūnas - tās cieši saskaras bez "
                      "spraugām.",
            kapec="Regulāri sešstūri pārklāj plakni, jo 3 · 120° = 360°."),

    Kopsavilkums([
        "Iegūstu daudzstūra leņķu summas formulu.",
        "Aprēķinu regulāra daudzstūra leņķi.",
        "No leņķu summas atrodu malu skaitu.",
    ]),

    Majas([
        "Uzzīmē sešstūri un sadali to trijstūros no vienas virsotnes.",
        "Atrodi, kuri regulārie daudzstūri pārklāj plakni bez spraugām.",
        "Nofotografē bruģi vai flīzes un nosaki daudzstūru veidus.",
    ]),
]
