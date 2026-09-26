# -*- coding: utf-8 -*-
"""9. klase, 114. stunda: «Kā risināt ar saskaitīšanas paņēmienu?»

Saskaitīšana: vienādojumus saskaita (vai atņem), lai viens nezināmais
pazūd. Ja koeficienti nav pretēji, vienādojumus vispirms pareizina ar
piemērotiem skaitļiem - kā daļām atrod kopsaucēju.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Slidnis, Varianti, paris, restis)

TEMA = "Kā risināt ar saskaitīšanas paņēmienu?"

MERKIS = ("Atrisināsim sistēmu, saskaitot vai atņemot vienādojumus.")

_T = "text"

SATURS = [
    Sakums("x + y = 10 un x − y = 4 - saskaiti!",
           zimejums=restis([["x + y = 10"], ["x − y = 4"], ["2x = 14"]]),
           paraksts="+y un −y saīsinās - paliek tikai x.",
           fakti=["Saskaitot vienādības, iegūst vienādību.",
                  "2x = 14 ⇒ x = 7, tad y = 3.",
                  "Pretēji koeficienti pazūd."]),

    Doma("Saskaitīšanas paņēmiens",
         "Pareizini vienādojumus tā, lai viena nezināmā koeficienti būtu "
         "pretēji skaitļi, un saskaiti tos.",
         soli=[
             "Salīdzini koeficientus pie x un pie y.",
             "Ja vajag, reizini vienu vai abus vienādojumus.",
             "Saskaiti (vai atņem) - viens nezināmais pazūd.",
             "Atrisini un ievieto, lai atrastu otru.",
         ]),

    Slidnis("Ar reizināšanu", [
        {"v": "Dots", "teksts": "3x + 2y = 16 un 5x − 4y = 12"},
        {"v": "· 2", "teksts": "Pirmo reizina ar 2: 6x + 4y = 32"},
        {"v": "+", "teksts": "6x + 4y + 5x − 4y = 32 + 12 ⇒ 11x = 44"},
        {"v": "x", "teksts": "x = 4"},
        {"v": "y", "teksts": "3 · 4 + 2y = 16 ⇒ y = 2; atbilde (4; 2)"},
    ]),

    Paraugs("Abus reizina",
            uzd="Atrisini: 2x + 3y = 12 un 3x − 2y = 5.",
            soli=[
                ("· 2 un · 3: 4x + 6y = 24; 9x − 6y = 15", "Pretēji ±6y."),
                ("13x = 39 ⇒ x = 3", "Saskaita."),
                ("6 + 3y = 12 ⇒ y = 2", "Ievieto."),
            ],
            atbilde="(3; 2)"),

    Ievadi("Atrisini ar saskaitīšanu", [
        {"jaut": "x + y = 8 un x − y = 2", "atb": paris(5, 3),
         "tastatura": _T, "vieta": "(x; y)", "padoms": "2x = 10."},
        {"jaut": "2x + y = 11 un 3x − y = 4", "atb": paris(3, 5),
         "tastatura": _T, "vieta": "(x; y)", "padoms": "5x = 15."},
        {"jaut": "x + 2y = 10 un x − y = 1", "atb": paris(4, 3),
         "tastatura": _T, "vieta": "(x; y)", "padoms": "Atņem: 3y = 9."},
        {"jaut": "3x + y = 7 un x + 2y = 4", "atb": paris(2, 1),
         "tastatura": _T, "vieta": "(x; y)", "padoms": "Pirmo · 2, atņem."},
        {"jaut": "4x − 3y = 1 un 2x + 5y = 7", "atb": paris(1, 1),
         "tastatura": _T, "vieta": "(x; y)", "padoms": "Otro · 2, atņem."},
    ], pamats=3),

    Varianti("Ar ko reizināt?", [
        {"jaut": "2x + 5y = 1 un 3x − y = 10. Lai pazustu y, otro reizina ar...",
         "opcijas": ["5", "2", "3", "−1"],
         "pareizi": 0, "padoms": "5y un −5y."},
        {"jaut": "4x + 3y = 5 un 6x + 2y = 10. Lai pazustu x...",
         "opcijas": ["pirmo · 3, otro · 2, atņem", "saskaita uzreiz",
                     "pirmo · 2, otro · 3, saskaita", "nevar"],
         "pareizi": 0, "padoms": "12x abos."},
    ]),

    Pasaule("Augļu grozs",
            Ievadi("", [
                {"jaut": "3 kg ābolu un 2 kg bumbieru maksā 7,90 €; 1 kg ābolu "
                         "un 2 kg bumbieru - 4,70 €. Atņemot: 2 kg ābolu = ? €",
                 "atb": ["3,2"], "padoms": "7,90 − 4,70."},
                {"jaut": "1 kg ābolu (€)?", "atb": ["1,6"], "padoms": "3,20 : 2."},
                {"jaut": "1 kg bumbieru (€)?", "atb": ["1,55"],
                 "padoms": "(4,70 − 1,60) : 2."},
            ]),
            pavediens="veikals",
            konteksts="Divi čeki ar tām pašām precēm - atņemot tos, vienas "
                      "preces daudzums pazūd.",
            kapec="Saskaitīšanas paņēmiens ir «čeku salīdzināšana»."),

    Kopsavilkums([
        "Saskaitu vai atņemu vienādojumus.",
        "Reizinu, lai iegūtu pretējus koeficientus.",
        "Atrodu abus nezināmos un pārbaudu.",
    ]),

    Majas([
        "Atrisini: 5x + 2y = 16, 3x − 2y = 0.",
        "Atrisini: 2x + 3y = 13, 5x − 4y = −2.",
        "Atrodi mājās divus čekus ar vienādām precēm un izrēķini cenas.",
    ]),
]
