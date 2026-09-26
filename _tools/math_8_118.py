# -*- coding: utf-8 -*-
"""8. klase, 118. stunda: «Kā reizina polinomu ar monomu?»

Sadalīšanas likums a(b + c) = ab + ac: monomu reizina ar katru locekli.
Zīmējumā taisnstūris 2x × (x + 3) sadalās daļās 2x^2 un 6x.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, geometrija)

TEMA = "Kā reizina polinomu ar monomu?"

MERKIS = ("Reizināsim polinomu ar monomu un pierakstīsim rezultātu "
          "normālformā.")

_T = "text"

SATURS = [
    Sakums("2x(x + 3) - cik tas ir?",
           zimejums=geometrija([("A", 0, 0), ("E", 3, 0), ("B", 5, 0),
                                ("C", 5, 3), ("F", 3, 3), ("D", 0, 3)],
                               nogriezni=["AB", "BC", "CD", "DA", "EF"],
                               iekrasot=[("AEFD", 0), ("EBCF", 1)],
                               malas=[("AE", "x"), ("EB", "3"),
                                      ("DA", "2x")],
                               uzraksti=[(1.5, 1.5, "2x²"),
                                         (4, 1.5, "6x")]),
           paraksts="2x(x + 3) = 2x^2 + 6x",
           fakti=["Monomu reizina ar katru polinoma locekli.",
                  "a(b + c) = ab + ac - sadalīšanas likums.",
                  "Katram loceklim ievēro zīmi."]),

    Doma("Sadalīšanas likums",
         "Monoms «ieiet» iekavās pie katra locekļa.",
         soli=[
             "Reizini monomu ar pirmo locekli.",
             "Tad ar otro, trešo - ar visiem.",
             "Ievēro zīmes: −x · (−4) = +4x.",
             "Pieraksti normālformā.",
         ]),

    Paraugs("Reizini",
            uzd="Aprēķini −3x(2x^2 − x + 4).",
            soli=[
                ("−3x · 2x^2 = −6x^3", "Pirmais loceklis."),
                ("−3x · (−x) = +3x^2", "Otrais - mīnuss reiz mīnuss."),
                ("−3x · 4 = −12x", "Trešais."),
                ("−6x^3 + 3x^2 − 12x", "Rezultāts."),
            ],
            atbilde="−6x^3 + 3x^2 − 12x"),

    Ievadi("Atver iekavas", [
        {"jaut": "2(x + 5)", "atb": ["2x + 10"], "tastatura": _T,
         "padoms": "2 · x + 2 · 5."},
        {"jaut": "a(a − 3)", "atb": ["a^2 − 3a"], "tastatura": _T,
         "padoms": "a · a − a · 3."},
        {"jaut": "−x(x − 4)", "atb": ["−x^2 + 4x"], "tastatura": _T,
         "padoms": "−x · (−4) = +4x."},
        {"jaut": "3x(2x + 1)", "atb": ["6x^2 + 3x"], "tastatura": _T,
         "padoms": "3x · 2x."},
        {"jaut": "2a(a^2 − a + 1)", "atb": ["2a^3 − 2a^2 + 2a"],
         "tastatura": _T, "padoms": "Trīs locekļi."},
        {"jaut": "x(x + 1) − x^2", "atb": ["x"], "tastatura": _T,
         "padoms": "x^2 + x − x^2."},
    ], pamats=4),

    Varianti("Izvēlies", [
        {"jaut": "3(a − 2) = ?",
         "opcijas": ["3a − 6", "3a − 2", "a − 6", "3a + 6"],
         "pareizi": 0, "padoms": "Reizina abus locekļus."},
        {"jaut": "x(x + 2) = ?",
         "opcijas": ["x^2 + 2x", "x^2 + 2", "2x + 2", "x^2 + x"],
         "pareizi": 0, "padoms": "x · 2 = 2x."},
        {"jaut": "−2(x − 3) = ?",
         "opcijas": ["−2x + 6", "−2x − 6", "2x − 6", "−2x − 3"],
         "pareizi": 0, "padoms": "−2 · (−3) = 6."},
    ]),

    Pasaule("Dārza pagarināšana",
            Ievadi("", [
                {"jaut": "Dārzs 10 m × x m; to pagarina par 4 m: 10(x + 4). "
                         "Laukums = 10x + ?",
                 "atb": ["40"], "padoms": "10 · 4."},
                {"jaut": "x = 12. Jaunais laukums (m²)?", "atb": ["160"],
                 "padoms": "120 + 40."},
                {"jaut": "Par cik m² laukums pieauga?", "atb": ["40"],
                 "padoms": "Neatkarīgi no x."},
            ]),
            pavediens="maja",
            konteksts="Pagarinot dārzu, piebūvētās daļas laukums ir viens no "
                      "saskaitāmajiem.",
            kapec="Sadalīšanas likums parāda katru daļu atsevišķi."),

    Kopsavilkums([
        "Reizinu polinomu ar monomu.",
        "Ievēroju katra locekļa zīmi.",
        "Parādu reizinājumu ar taisnstūra laukumu.",
    ]),

    Majas([
        "Atver iekavas: 4x(x^2 − 2x + 3); −a(5 − a).",
        "Uzzīmē taisnstūri, kas parāda 3a(a + 2).",
        "Pārbaudi rezultātus ar x = 1.",
    ]),
]
