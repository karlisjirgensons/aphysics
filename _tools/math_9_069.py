# -*- coding: utf-8 -*-
"""9. klase, 69. stunda: «Kā formulu lasīt abos virzienos?»

No kreisās uz labo formula atver iekavas, no labās uz kreiso - sadala
reizinātājos. x^2 + 6x + 9 = (x + 3)^2 ir tā pati vienādība otrādi. Lai to
atpazītu, jāatrod a un b un jāpārbauda vidējais loceklis.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Slidnis, Varianti, binoma_kvadrats)

TEMA = "Kā formulu lasīt abos virzienos?"

MERKIS = ("Lietosim formulu gan izteiksmes atvēršanai, gan sadalīšanai "
          "reizinātājos.")

_T = "text"

SATURS = [
    Sakums("x² + 6x + 9 - vai tas ir kvadrāts?",
           zimejums=binoma_kvadrats(4, 1.5, ("x", "3")),
           paraksts="x² + 3x + 3x + 9 - kvadrāts ar malu x + 3.",
           fakti=["→ atver: (x + 3)^2 = x^2 + 6x + 9.",
                  "← sadala: x^2 + 6x + 9 = (x + 3)^2.",
                  "Vienādība ir viena, virzieni divi."]),

    Slidnis("Atpazīsti binoma kvadrātu", [
        {"v": "1", "teksts": "x^2 + 6x + 9: kvadrāti x^2 = (x)^2 un 9 = 3^2"},
        {"v": "2", "teksts": "a = x, b = 3: pārbaudi 2ab = 2 · x · 3 = 6x ✔"},
        {"v": "3", "teksts": "Zīme pie 6x ir + → (x + 3)^2"},
        {"v": "Otrs", "teksts": "4a^2 − 20a + 25: (2a)^2, 5^2, 2 · 2a · 5 = "
                                "20a, zīme − → (2a − 5)^2"},
    ]),

    Doma("No trinoma uz kvadrātu",
         "a^2 ± 2ab + b^2 = (a ± b)^2 - ja divi locekļi ir kvadrāti un trešais "
         "ir to «sakņu» divkāršots reizinājums.",
         soli=[
             "Atrodi divus kvadrātus - tie dod a un b.",
             "Pārbaudi trešo locekli: vai tas ir 2ab?",
             "Zīme pie 2ab nosaka + vai − iekavās.",
             "Ja 2ab nesakrīt - tas NAV binoma kvadrāts.",
         ]),

    Paraugs("Sadali reizinātājos",
            uzd="Sadali: 9y^2 + 12y + 4.",
            soli=[
                ("9y^2 = (3y)^2; 4 = 2^2", "Kvadrāti."),
                ("2 · 3y · 2 = 12y ✔", "Vidējais sakrīt."),
                ("(3y + 2)^2", "Zīme +."),
            ],
            atbilde="(3y + 2)^2"),

    Ievadi("Uzraksti kā kvadrātu", [
        {"jaut": "x^2 + 10x + 25", "atb": ["(x + 5)^2", "(5 + x)^2"],
         "tastatura": _T, "padoms": "5^2 = 25, 2 · 5x = 10x."},
        {"jaut": "a^2 − 8a + 16", "atb": ["(a − 4)^2", "(4 − a)^2"],
         "tastatura": _T, "padoms": "Zīme −."},
        {"jaut": "4x^2 + 4x + 1", "atb": ["(2x + 1)^2", "(1 + 2x)^2"],
         "tastatura": _T, "padoms": "(2x)^2 un 1^2."},
        {"jaut": "m^2 − 2mn + n^2", "atb": ["(m − n)^2", "(n − m)^2"],
         "tastatura": _T, "padoms": "Formula."},
        {"jaut": "25 − 10b + b^2", "atb": ["(5 − b)^2", "(b − 5)^2"],
         "tastatura": _T, "padoms": "5^2, b^2, 2 · 5b."},
    ], pamats=3),

    Varianti("Vai tas ir binoma kvadrāts?", [
        {"jaut": "x^2 + 4x + 16",
         "opcijas": ["Nē - vidējam jābūt 8x", "(x + 4)^2", "(x + 2)^2",
                     "(x − 4)^2"],
         "pareizi": 0, "padoms": "2 · x · 4 = 8x."},
        {"jaut": "x^2 − 12x + 36",
         "opcijas": ["(x − 6)^2", "(x + 6)^2", "(x − 6)(x + 6)", "Nē"],
         "pareizi": 0, "padoms": "2 · 6x = 12x, zīme −."},
        {"jaut": "x^2 + 9",
         "opcijas": ["Nē - trūkst vidējā locekļa", "(x + 3)^2",
                     "(x − 3)(x + 3)", "(x + 9)^2"],
         "pareizi": 0, "padoms": "Divi locekļi, summa."},
    ]),

    Pasaule("Kvadrātveida laukums",
            Ievadi("", [
                {"jaut": "Parka laukuma platība x^2 + 20x + 100 m². Kāda ir "
                         "malas izteiksme? (x + ?) m", "atb": ["10"],
                 "padoms": "100 = 10^2, 2 · 10x = 20x."},
                {"jaut": "x = 30. Malas garums (m)?", "atb": ["40"],
                 "padoms": "30 + 10."},
            ]),
            pavediens="maja",
            konteksts="Arhitekts saņēma laukuma formulu un grib uzzināt, kāda "
                      "ir kvadrāta mala.",
            kapec="Sadalīšana «atrod» malu no laukuma."),

    Kopsavilkums([
        "Lietoju formulu abos virzienos.",
        "Atpazīstu binoma kvadrātu pēc vidējā locekļa.",
        "Pierakstu trinomu kā (a ± b)^2.",
    ]),

    Majas([
        "Sadali: x^2 − 14x + 49; 16a^2 + 24a + 9.",
        "Papildini līdz kvadrātam: x^2 + 8x + ? .",
        "Izdomā trinomu, kas izskatās pēc kvadrāta, bet nav.",
    ]),
]
