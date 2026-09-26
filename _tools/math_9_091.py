# -*- coding: utf-8 -*-
"""9. klase, 91. stunda: «Kā to risinātu eksāmenā?»

Kvadrātvienādojumi eksāmena formātā: 1. daļā 7.2. tipa uzdevums
(3 punkti) un atbilžu izvēle par sakņu skaitu, 2. daļā - situācijas
uzdevums, kurā vienādojums jāsastāda pašam un jāizvērtē saknes.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, restis, saknes)

TEMA = "Kā to risinātu eksāmenā?"

MERKIS = ("Risināsim eksāmena formāta uzdevumus par kvadrātvienādojumiem.")

_T = "text"

SATURS = [
    Sakums("Metodes izvēle - pusminūtē",
           zimejums=restis([["vienādojums", "metode"],
                            ["ax² + bx = 0", "iznes x"],
                            ["ax² + c = 0", "x² = −c : a"],
                            ["x² + bx + c = 0 (veseli)", "Vjeta / spriežot"],
                            ["jebkurš", "D un sakņu formula"]]),
           paraksts="Ātrākā metode - mazāk kļūdu.",
           fakti=["Nepilnajiem D nevajag.",
                  "Sakņu formula der vienmēr.",
                  "Saknes pārbauda ar Vjetu vai ievietojot."]),

    Doma("Pilns risinājums eksāmenā",
         "Standartforma → D → x_{1;2} → atbilde; situācijas uzdevumā vēl "
         "«kura sakne der».",
         soli=[
             "Pieraksti vienādojumu standartformā.",
             "D ar ievietotām vērtībām (ne tikai rezultātu).",
             "Abas saknes ar formulu.",
             "Situācijā: izmet saknes, kas neder (negatīvs garums u. tml.).",
             "Atbilde ar mērvienību.",
         ]),

    Paraugs("2. daļas stilā",
            uzd="Taisnstūra laukums ir 60 cm², viena mala par 7 cm garāka par "
                "otru. Aprēķini malas.",
            soli=[
                ("x(x + 7) = 60 ⇒ x^2 + 7x − 60 = 0", "Vienādojums."),
                ("D = 49 + 240 = 289 = 17^2", "Diskriminants."),
                ("x = {−7 ± 17|2}: x_1 = 5, x_2 = −12", "Saknes."),
                ("x = 5 (garums > 0); otra mala 12", "Izvērtē."),
            ],
            atbilde="5 cm un 12 cm"),

    Ievadi("1. daļa: atrisini", [
        {"jaut": "2x^2 + 7x − 4 = 0", "atb": saknes("−4", "0,5"),
         "tastatura": _T, "vieta": "x₁; x₂", "padoms": "D = 81."},
        {"jaut": "x^2 − 8x + 15 = 0", "atb": saknes("3", "5"),
         "tastatura": _T, "vieta": "x₁; x₂", "padoms": "D = 4."},
        {"jaut": "3x^2 − 12x = 0", "atb": saknes("0", "4"),
         "tastatura": _T, "vieta": "x₁; x₂", "padoms": "3x(x − 4) = 0."},
        {"jaut": "x^2 + 6x + 9 = 0", "atb": ["−3", "-3"],
         "padoms": "D = 0."},
    ]),

    Varianti("Atbilžu izvēle", [
        {"jaut": "Vienādojuma x^2 − 3x + 5 = 0 saknes",
         "opcijas": ["nav reālu sakņu", "divas", "viena", "0 un 3"],
         "pareizi": 0, "padoms": "D = 9 − 20 < 0."},
        {"jaut": "Vienādojuma x^2 + px + 12 = 0 viena sakne ir 3. p = ?",
         "opcijas": ["−7", "7", "−4", "4"],
         "pareizi": 0, "padoms": "Otra sakne 4; summa 7 = −p."},
        {"jaut": "Kurš vienādojums ir ar saknēm −2 un 5?",
         "opcijas": ["x^2 − 3x − 10 = 0", "x^2 + 3x − 10 = 0",
                     "x^2 − 3x + 10 = 0", "x^2 + 7x + 10 = 0"],
         "pareizi": 0, "padoms": "Summa 3, reizinājums −10."},
    ]),

    Pasaule("Futbola laukuma žogs",
            Ievadi("", [
                {"jaut": "Mini futbola laukums 800 m², garums par 20 m lielāks "
                         "par platumu. Platums (m)?", "atb": ["20"],
                 "padoms": "x^2 + 20x − 800 = 0; D = 3600."},
                {"jaut": "Cik m žoga vajag apkārt?", "atb": ["120"],
                 "padoms": "2(20 + 40)."},
            ]),
            pavediens="sports",
            konteksts="Skolas pagalmā plāno sporta laukumu ar zināmu laukumu "
                      "un proporciju.",
            kapec="Tieši tāds ir tipisks 2. daļas uzdevums."),

    Kopsavilkums([
        "Izvēlos ātrāko metodi.",
        "Noformēju risinājumu ar D un formulu.",
        "Izvērtēju sakņu jēgu situācijā.",
    ]),

    Majas([
        "Atkārto 80.-90. stundu.",
        "Atrisini: 6x^2 − x − 2 = 0; {x^2|4} − x = 3.",
        "Izdomā situācijas uzdevumu ar kvadrātvienādojumu.",
    ]),
]
