# -*- coding: utf-8 -*-
"""9. klase, 32. stunda: «Kā Pitagora teorēma palīdz trapecē?»

Augstums nogriež taisnleņķa trijstūri, kurā hipotenūza ir sānu mala, bet
katetes - augstums un pamatu starpības daļa. Laukuma uzdevumos augstums
bieži nav dots, un to atrod tieši tā.
"""

from math_saturs import (TRAPECES_MALAS, Doma, Ievadi, Kopsavilkums, Majas,
                         Paraugs, Pasaule, Sakums, Varianti, geometrija,
                         trapece)

TEMA = "Kā Pitagora teorēma palīdz trapecē?"

MERKIS = ("Aprēķināsim trapeces augstumu vai sānu malu, lietojot Pitagora "
          "teorēmu.")

SATURS = [
    Sakums("Augstums nav dots - bet laukums jāatrod",
           zimejums=geometrija(trapece(16, 4, 8, pedas=True),
                               nogriezni=TRAPECES_MALAS + ["DH", "CK"],
                               taisni=["DHB", "CKA"],
                               iekrasot=[("AHD", 1)],
                               malas=[("AD", "10"), ("AH", "6"),
                                      ("DH", "h")]),
           paraksts="Vienādsānu: pamati 16 un 4, sānu mala 10.",
           fakti=["AH = {16 − 4|2} = 6.",
                  "h^2 = 10^2 − 6^2 = 64, h = 8.",
                  "S = {16 + 4|2} · 8 = 80."]),

    Doma("Trijstūris pie sānu malas",
         "Sānu mala^2 = h^2 + AH^2, kur vienādsānu trapecē AH = {a − b|2}.",
         soli=[
             "Novelc augstumu no augšējā pamata virsotnes.",
             "Atrodi AH no pamatiem.",
             "Pitagora teorēma trijstūrī AHD.",
             "Tad laukums, perimetrs vai diagonāle.",
         ]),

    Paraugs("Diagonāle",
            uzd="Vienādsānu trapecē pamati 14 un 6, augstums 3. Atrodi "
                "diagonāli AC.",
            soli=[
                ("AK = {14 + 6|2} = 10", "Līdz augstuma CK pēdai."),
                ("AC^2 = AK^2 + CK^2 = 100 + 9 = 109", "Trijstūris AKC."),
                ("AC = √109 ≈ 10,4", "Kvadrātsakne."),
            ],
            atbilde="√109 ≈ 10,4"),

    Ievadi("Aprēķini (vienādsānu)", [
        {"jaut": "a = 14, b = 8, sānu mala 5. h = ?", "atb": ["4"],
         "padoms": "AH = 3."},
        {"jaut": "Tie paši. S = ?", "atb": ["44"], "padoms": "11 · 4."},
        {"jaut": "a = 20, b = 10, h = 12. Sānu mala?", "atb": ["13"],
         "padoms": "AH = 5."},
        {"jaut": "a = 12, b = 4, h = 3. Diagonāle?", "atb": ["√73", "√(73)"],
         "tastatura": "text", "padoms": "AK = 8; 64 + 9."},
        {"jaut": "Taisnleņķa: a = 11, b = 5, slīpā mala 10. h = ?",
         "atb": ["8"], "padoms": "Katete 6."},
        {"jaut": "Taisnleņķa: a = 11, b = 5, slīpā mala 10. S = ?",
         "atb": ["64"], "padoms": "8 · 8."},
    ], pamats=4),

    Varianti("Kurš trijstūris?", [
        {"jaut": "Lai atrastu augstumu, izmanto trijstūri...",
         "opcijas": ["ar hipotenūzu - sānu malu", "ar hipotenūzu - pamatu",
                     "ABC", "jebkuru"],
         "pareizi": 0, "padoms": "AHD: katetes h un AH."},
        {"jaut": "Vienādsānu trapecē pamati 10 un 10. Tā ir...",
         "opcijas": ["nav trapece - paralelograms", "vienādsānu trapece",
                     "trijstūris", "kvadrāts noteikti"],
         "pareizi": 0, "padoms": "Abi malu pāri paralēli."},
    ]),

    Pasaule("Jumta slīpne",
            Ievadi("", [
                {"jaut": "Mansarda šķērsgriezums: grīda 9 m, griesti 3 m "
                         "(vienādsānu), augstums 4 m. Slīpās sienas garums (m)?",
                 "atb": ["5"], "padoms": "AH = 3."},
                {"jaut": "Siltumizolāciju liek uz abām slīpnēm, māja 10 m gara. "
                         "Cik m²?", "atb": ["100"], "padoms": "2 · 5 · 10."},
            ]),
            pavediens="maja",
            konteksts="Siltinot mansardu, jāzina slīpo sienu laukums, bet "
                      "mērīt var tikai grīdu un griestus.",
            kapec="Pitagora teorēma dod slīpni no horizontāliem mēriem."),

    Kopsavilkums([
        "Atrodu taisnleņķa trijstūri trapecē.",
        "Aprēķinu augstumu vai sānu malu.",
        "Aprēķinu diagonāli un laukumu.",
    ]),

    Majas([
        "Vienādsānu trapecē pamati 22 un 10, sānu mala 10. Atrodi laukumu.",
        "Aprēķini tās diagonāli.",
        "Izmēri slīpu virsmu mājās (jumts, rampa) un pārbaudi ar Pitagoru.",
    ]),
]
