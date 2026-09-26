# -*- coding: utf-8 -*-
"""9. klase, 64. stunda: «Kā to parādīt ar laukumu?»

Formulas ģeometriskā jēga: kvadrāts ar malu a + b sastāv no kvadrāta a^2,
kvadrāta b^2 un diviem taisnstūriem ab. Pitagoriešu veids, kā formulu
«redzēt», nevis iekalt.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Slidnis, Varianti,
                         binoma_kvadrats)

TEMA = "Kā to parādīt ar laukumu?"

MERKIS = ("Skaidrosim binoma kvadrāta formulu, izmantojot kvadrāta laukumu.")

_T = "text"

SATURS = [
    Sakums("Kvadrāts ar malu a + b",
           zimejums=binoma_kvadrats(),
           paraksts="Četras daļas: a², ab, ab, b².",
           fakti=["Viss laukums: (a + b)^2.",
                  "Pa daļām: a^2 + ab + ab + b^2.",
                  "Tātad (a + b)^2 = a^2 + 2ab + b^2."]),

    Slidnis("Saliec kvadrātu", [
        {"v": "a²", "teksts": "Liels kvadrāts ar malu a",
         "zim": binoma_kvadrats(izcelt="a2")},
        {"v": "2ab", "teksts": "Divi taisnstūri a × b",
         "zim": binoma_kvadrats(izcelt="ab")},
        {"v": "b²", "teksts": "Mazs kvadrāts ar malu b",
         "zim": binoma_kvadrats(izcelt="b2")},
    ]),

    Doma("Laukuma pierādījums",
         "Viena un tā pati figūra - divi laukuma pieraksti; tie ir vienādi.",
         soli=[
             "Kvadrāta mala a + b - laukums (a + b)^2.",
             "Sadali ar divām līnijām četrās daļās.",
             "Saskaiti daļu laukumus: a^2 + 2ab + b^2.",
         ],
         pieze="Tā pati ideja der konkrētiem skaitļiem: 13^2 = (10 + 3)^2 = "
               "100 + 60 + 9 = 169."),

    Petijums("Izgriez un saliec", [
        "Izgriez no papīra kvadrātu 8 cm × 8 cm.",
        "Sadali to ar līnijām 5 cm un 3 cm attālumā no stūra.",
        "Izgriez četras daļas un aprēķini katras laukumu.",
        "Pārbaudi: 25 + 15 + 15 + 9 = 64.",
    ], vajag="papīrs, lineāls, šķēres",
       secinajums="(5 + 3)^2 = 5^2 + 2 · 5 · 3 + 3^2 = 64."),

    Ievadi("Laukumi pa daļām", [
        {"jaut": "a = 6, b = 2. Abu taisnstūru kopējais laukums?",
         "atb": ["24"], "padoms": "2 · 6 · 2."},
        {"jaut": "a = 6, b = 2. Viss kvadrāts?", "atb": ["64"],
         "padoms": "36 + 24 + 4."},
        {"jaut": "21^2 = (20 + 1)^2 = 400 + ? + 1", "atb": ["40"],
         "padoms": "2 · 20 · 1."},
        {"jaut": "32^2 = ?", "atb": ["1024"], "padoms": "900 + 120 + 4."},
    ]),

    Varianti("Kurš zīmējums?", [
        {"jaut": "Kura daļa kvadrātā atbilst loceklim 2ab?",
         "opcijas": ["Divi vienādi taisnstūri", "Lielais kvadrāts",
                     "Mazais kvadrāts", "Diagonāle"],
         "pareizi": 0, "padoms": "Katrs a × b."},
        {"jaut": "Ja b = 0, zīmējumā paliek...",
         "opcijas": ["tikai kvadrāts a²", "tikai b²", "divi taisnstūri",
                     "nekas"],
         "pareizi": 0, "padoms": "(a + 0)^2 = a^2."},
    ]),

    Pasaule("Dārza paplašināšana",
            Ievadi("", [
                {"jaut": "Kvadrātveida dobe 5 m × 5 m. Paplašina par 1 m uz "
                         "divām pusēm (kļūst 6 × 6). Cik m² pieliek?",
                 "atb": ["11"], "padoms": "2 · 5 · 1 + 1."},
                {"jaut": "Paplašina par 2 m (7 × 7). Cik m² pieliek?",
                 "atb": ["24"], "padoms": "2 · 5 · 2 + 4."},
            ]),
            pavediens="maja",
            konteksts="Paplašinot kvadrātveida dobi uz divām pusēm, pieliek "
                      "divas joslas un mazu stūri.",
            kapec="Tieši 2ab + b^2 ir papildu laukums.",
            zimejums=binoma_kvadrats(5, 1, ("5", "1"), izcelt="ab")),

    Kopsavilkums([
        "Parādu (a + b)^2 ar kvadrāta laukumu.",
        "Atrodu katras daļas laukumu.",
        "Rēķinu skaitļu kvadrātus galvā.",
    ]),

    Majas([
        "Uzzīmē laukuma modeli izteiksmei (x + 4)^2.",
        "Aprēķini galvā: 41^2, 52^2, 103^2.",
        "Kā ar laukumu parādīt (a + b + c)^2? Uzzīmē.",
    ]),
]
