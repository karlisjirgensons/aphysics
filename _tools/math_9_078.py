# -*- coding: utf-8 -*-
"""9. klase, 78. stunda: «Kā to risinātu eksāmenā?»

9.4. temata noslēgums eksāmena formātā: 1. daļas «Izpildi darbības»
(3.1.-3.4. uzdevums 2025. gadā), sadalīšana reizinātājos un nepilnie
kvadrātvienādojumi ar noformējumu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, restis, saknes)

TEMA = "Kā to risinātu eksāmenā?"

MERKIS = ("Risināsim eksāmena formāta uzdevumus par izteiksmju "
          "pārveidojumiem.")

_T = "text"

SATURS = [
    Sakums("Eksāmens 2025: «Izpildi darbības» - 5 punkti",
           zimejums=restis([["uzdevums", "punkti"], ["x⁸ · x²", "1"],
                            ["3(a − 6)", "1"], ["(4 + b)²", "1"],
                            ["(2c − 3)(5 + c) − 3c", "2"]]),
           paraksts="Visi četri - šī temata prasmes.",
           fakti=["Formulu lapā: (a ± b)^2 un a^2 − b^2.",
                  "Par garāko uzdevumu - 2 punkti: risinājums jāparāda.",
                  "Beigās savelc līdzīgos locekļus."]),

    Doma("Eksāmena kontrolsaraksts",
         "Katrā pārveidojumā: formula → iekavas → zīmes → līdzīgie locekļi → "
         "pārbaude.",
         soli=[
             "Pirms atver - nosaki, kura formula der.",
             "Mīnuss pirms iekavām: atver ar iekavām!",
             "Sadalot - vai viss sadalīts līdz galam?",
             "Vienādojumā - vai nav pazaudēta sakne 0?",
         ]),

    Paraugs("2 punktu uzdevums",
            uzd="Sadali reizinātājos: 2x^3 − 18x.",
            soli=[
                ("2x^3 − 18x = 2x(x^2 − 9)", "Iznes kopīgo 2x."),
                ("= 2x(x − 3)(x + 3)", "Kvadrātu starpība."),
            ],
            atbilde="2x(x − 3)(x + 3)"),

    Ievadi("1. daļa: Izpildi darbības", [
        {"jaut": "x^8 · x^2", "atb": ["x^10"], "tastatura": _T,
         "padoms": "Kāpinātājus saskaita."},
        {"jaut": "3(a − 6)", "atb": ["3a − 18"], "tastatura": _T,
         "padoms": "Reizina abus."},
        {"jaut": "(4 + b)^2", "atb": ["16 + 8b + b^2", "b^2 + 8b + 16"],
         "tastatura": _T, "padoms": "Summas kvadrāts."},
        {"jaut": "(2c − 3)(5 + c) − 3c", "atb": ["2c^2 + 4c − 15"],
         "tastatura": _T, "padoms": "2c^2 + 7c − 15 − 3c."},
    ]),

    Ievadi("Vienādojumi", [
        {"jaut": "x^2 − 3x = 0", "atb": saknes("0", "3"), "tastatura": _T,
         "vieta": "x₁; x₂", "padoms": "x(x − 3) = 0."},
        {"jaut": "x^2 − 64 = 0", "atb": saknes("−8", "8"), "tastatura": _T,
         "vieta": "x₁; x₂", "padoms": "±8."},
        {"jaut": "(x − 2)(3x + 9) = 0", "atb": saknes("−3", "2"),
         "tastatura": _T, "vieta": "x₁; x₂", "padoms": "3x = −9."},
    ]),

    Varianti("Atbilžu izvēle", [
        {"jaut": "Izteiksmi x^2 − 10x + 25 var uzrakstīt kā",
         "opcijas": ["(x − 5)^2", "(x + 5)^2", "(x − 5)(x + 5)",
                     "(x − 25)^2"],
         "pareizi": 0, "padoms": "Starpības kvadrāts."},
        {"jaut": "{x^2 − 4|x + 2} = ?",
         "opcijas": ["x − 2", "x + 2", "x − 4", "{x − 4|2}"],
         "pareizi": 0, "padoms": "(x − 2)(x + 2)."},
        {"jaut": "Kurai izteiksmei ir 2 saknes?",
         "opcijas": ["x^2 − 1 = 0", "x^2 + 1 = 0", "x^2 = 0",
                     "(x − 1)^2 = 0"],
         "pareizi": 0, "padoms": "x^2 = 1."},
    ]),

    Pasaule("Kvadrātveida laukuma paplašināšana",
            Ievadi("", [
                {"jaut": "Kvadrātveida laukuma malu palielina par 3 m, un "
                         "laukums pieaug par 81 m². Sākotnējā mala x: "
                         "(x + 3)^2 − x^2 = 81. x = ?", "atb": ["12"],
                 "padoms": "6x + 9 = 81."},
                {"jaut": "Jaunais laukums (m²)?", "atb": ["225"],
                 "padoms": "15^2."},
            ]),
            pavediens="maja",
            konteksts="Tipisks 2. daļas uzdevums: situācija → vienādojums → "
                      "formula → atbilde.",
            kapec="Formula pārvērš «kvadrātu» vienādojumu lineārā."),

    Kopsavilkums([
        "Risinu 1. daļas pārveidojumus bez kļūdām.",
        "Sadalu reizinātājos līdz galam.",
        "Atrisinu nepilnos kvadrātvienādojumus.",
    ]),

    Majas([
        "Atkārto 9.4. tematu - nākamajā stundā pārbaudes darbs.",
        "Sadali: 3a^3 − 12a; x^2 + 14x + 49.",
        "Atrisini: 5x^2 = 20x; 9x^2 − 4 = 0.",
    ]),
]
