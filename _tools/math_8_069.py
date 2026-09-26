# -*- coding: utf-8 -*-
"""8. klase, 69. stunda: «Kā izteiksme apraksta laukumu?»

Bloka noslēgums: izmērus apzīmē ar burtu, laukumu pieraksta kā izteiksmi
un vienkāršo. Trijstūris ar pamatu 2x un augstumu x ir x^2. Ievada
monomus, ko sistemātiski apgūs 8.6. tematā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, geometrija)

TEMA = "Kā izteiksme apraksta laukumu?"

MERKIS = ("Pierakstīsim figūras laukumu ar algebrisku izteiksmi un "
          "vienkāršosim to.")

SATURS = [
    Sakums("Kāds ir laukums, ja izmēri ir burti?",
           zimejums=geometrija([("A", 0, 0), ("B", 6, 0), ("C", 2, 3),
                                ("H", 2, 0, 270)],
                               nogriezni=["AB", "BC", "CA", "CH"],
                               taisni=["CHB"], iekrasot=[("ABC", 0)],
                               malas=[("AB", "2x")],
                               uzraksti=[(2.5, 1.5, "x")]),
           paraksts="S = {2x · x|2} = x^2",
           fakti=["Izmērus var apzīmēt ar burtiem.",
                  "Laukumu tad pieraksta kā izteiksmi ar mainīgo.",
                  "Ievietojot skaitli, iegūst konkrētu laukumu."]),

    Doma("Laukums ar mainīgo",
         "Laukuma formula der arī tad, ja izmērs ir burts.",
         soli=[
             "Apzīmē nezināmos izmērus ar burtu.",
             "Pieraksti katras daļas laukumu.",
             "Saskaiti un savelc līdzīgos locekļus.",
             "Ievieto skaitli un pārbaudi.",
         ]),

    Paraugs("Māja ar platumu a",
            uzd="Siena: taisnstūris a × 6 un virs tā trijstūris ar pamatu a "
                "un augstumu 4. Pieraksti laukumu un aprēķini, ja a = 5.",
            soli=[
                ("6a", "Taisnstūris."),
                ("{a · 4|2} = 2a", "Trijstūris."),
                ("S = 6a + 2a = 8a", "Līdzīgie locekļi."),
                ("a = 5: S = 8 · 5 = 40", "Ievieto."),
            ],
            atbilde="8a; 40"),

    Ievadi("Ieraksti koeficientu", [
        {"jaut": "Trijstūris: pamats 6, augstums x. S = ?x", "atb": ["3"],
         "padoms": "{6x|2}."},
        {"jaut": "Taisnstūris x × 5 un trijstūris ar pamatu x un augstumu 2. "
                 "S = ?x", "atb": ["6"], "padoms": "5x + x."},
        {"jaut": "Taisnleņķa trijstūris ar katetēm 2x un 3x. S = ?x^2",
         "atb": ["3"], "padoms": "{6x^2|2}."},
        {"jaut": "Kvadrāts ar malu 2a. S = ?a^2", "atb": ["4"],
         "padoms": "2a · 2a."},
        {"jaut": "Figūrai S = 6x. Cik tas ir, ja x = 4?", "atb": ["24"],
         "padoms": "6 · 4."},
    ]),

    Varianti("Kura izteiksme?", [
        {"jaut": "Trijstūris ar pamatu 4a un augstumu a. S = ?",
         "opcijas": ["2a^2", "4a^2", "2a", "5a"],
         "pareizi": 0, "padoms": "{4a · a|2}."},
        {"jaut": "Taisnstūris 3 × (x + 2). S = ?",
         "opcijas": ["3x + 6", "3x + 2", "x + 6", "3x"],
         "pareizi": 0, "padoms": "Reizina katru saskaitāmo."},
        {"jaut": "Kvadrāts x × x bez stūra kvadrātiņa 1 × 1. S = ?",
         "opcijas": ["x^2 − 1", "x^2 − 2", "2x − 1", "x − 1"],
         "pareizi": 0, "padoms": "Atņem 1."},
    ]),

    Pasaule("Dārza plāns",
            Ievadi("", [
                {"jaut": "Dārzs ir taisnstūris 10 m × x m; tajā trijstūra "
                         "dobe ar pamatu 4 m un augstumu x m. Zāliens = ?x m²",
                 "atb": ["8"], "padoms": "10x − 2x."},
                {"jaut": "x = 6. Zāliena laukums (m²)?", "atb": ["48"],
                 "padoms": "8 · 6."},
                {"jaut": "Viena sēklu paka ir 20 m². Cik paku vajag?",
                 "atb": ["3"], "padoms": "48 : 20 = 2,4 - uz augšu."},
            ]),
            pavediens="maja",
            konteksts="Plānojot dārzu, izmēru vēl var mainīt. Izteiksme ar x "
                      "parāda laukumu jebkuram x.",
            kapec="Viena izteiksme der visiem plāna variantiem."),

    Kopsavilkums([
        "Pierakstu figūras laukumu ar izteiksmi.",
        "Savelku līdzīgos locekļus.",
        "Aprēķinu laukumu, ievietojot mainīgā vērtību.",
    ]),

    Majas([
        "Uzzīmē figūru, kuras laukums ir 5x.",
        "Pieraksti laukumu L veida figūrai ar izmēriem a un b.",
        "Aprēķini savu izteiksmi, ja x = 3 un x = 10.",
    ]),
]
