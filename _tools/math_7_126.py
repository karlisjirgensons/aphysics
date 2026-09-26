# -*- coding: utf-8 -*-
"""7. klase, 126. stunda: «Kā izteiksme palīdz aprēķināt perimetru?»

Ja figūras malas izsaka ar mainīgo, perimetrs un laukums arī ir izteiksmes.
Tās vienkāršo un aprēķina jebkuram mainīgā lielumam - tā projektē
istabas, dārzus un iepakojumus.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, geometrija)

TEMA = "Kā izteiksme palīdz aprēķināt perimetru?"

MERKIS = ("Pierakstīsim ar izteiksmi figūras perimetru vai laukumu un "
          "vienkāršosim to.")

_L = geometrija([("A", 0, 0), ("B", 6, 0), ("C", 6, 2), ("D", 3, 2),
                 ("E", 3, 7), ("F", 0, 7)],
                nogriezni=["AB", "BC", "CD", "DE", "EF", "FA"],
                malas=[("AB", "2x"), ("BC", "x − 1"), ("EF", "x"),
                       ("FA", "x + 4")])

SATURS = [
    Sakums("L formas istaba",
           zimejums=_L,
           paraksts="Perimetrs - visu malu summa, arī nezināmo.",
           fakti=["Horizontālās malas: AB = FE + DC.",
                  "Vertikālās: FA = BC + DE.",
                  "Tātad P = 2 · AB + 2 · FA."]),

    Doma("Perimetrs = malu summa, tad vienkāršo",
         "Figūras perimetru ar mainīgajiem iegūst, saskaitot visu malu "
         "izteiksmes un savelkot līdzīgos. Laukumu - reizinot vai saskaitot "
         "daļu laukumus.",
         soli=[
             "Izsaki katru malu ar mainīgo (arī tās, kas nav dotas).",
             "Saskaiti visas malas.",
             "Savelc līdzīgos saskaitāmos.",
             "Ievieto skaitli, lai iegūtu konkrētu perimetru.",
         ],
         pieze="Taisnleņķa «L» figūrai perimetrs ir tāds pats kā "
               "taisnstūrim, kurā tā ievilkta."),

    Paraugs("L forma",
            uzd="Sākuma figūrā AB = 2x, FA = x + 4. Uzraksti perimetru un "
                "aprēķini, ja x = 5 m.",
            soli=[
                ("P = 2 · AB + 2 · FA", "(L formas malas)"),
                ("P = 2 · 2x + 2(x + 4)", "Ievieto."),
                ("P = 4x + 2x + 8 = 6x + 8", "Vienkāršo."),
                ("x = 5: P = 38 (m)", "Aprēķina."),
            ],
            atbilde="P = 6x + 8; 38 m"),

    Ievadi("Aprēķini", [
        {"jaut": "Trijstūra malas x, x + 2, 2x − 1. Perimetrs vienkāršots: "
                 "?x + 1. Koeficients?",
         "atb": ["4"], "padoms": "x + x + 2x."},
        {"jaut": "Tas pats perimetrs, ja x = 3?",
         "atb": ["13"], "padoms": "4 · 3 + 1."},
        {"jaut": "Taisnstūra malas a un a + 5. Perimetrs, ja a = 4?",
         "atb": ["26"], "padoms": "2(2a + 5)."},
        {"jaut": "Tā laukums a(a + 5), ja a = 4?",
         "atb": ["36"], "padoms": "4 · 9."},
    ]),

    Varianti("Kura izteiksme?", [
        {"jaut": "Kvadrāta mala 3a. Perimetrs?",
         "opcijas": ["12a", "9a", "3a + 4", "6a"],
         "pareizi": 0, "padoms": "4 · 3a."},
        {"jaut": "Vienādsānu trijstūra sāns y, pamats y − 2. Perimetrs?",
         "opcijas": ["3y − 2", "2y − 2", "3y + 2", "y − 2"],
         "pareizi": 0, "padoms": "y + y + y − 2."},
        {"jaut": "Taisnstūra malas x un 2x. Laukums?",
         "opcijas": ["2x²", "3x", "2x", "6x"],
         "pareizi": 0, "padoms": "x · 2x."},
    ]),

    Pasaule("Grīdlīstes istabai",
            Ievadi("", [
                {"jaut": "Istaba x × (x + 2) m, durvis 1 m (bez līstes). "
                         "Līstes garums 4x + 4 − 1. Cik m, ja x = 3,5?",
                 "atb": ["17"], "padoms": "14 + 3."},
                {"jaut": "Grīdas laukums x(x + 2), ja x = 3,5 (m²)?",
                 "atb": ["19,25"], "padoms": "3,5 · 5,5."},
                {"jaut": "Parkets pakā 2 m². Cik paku jāpērk?",
                 "atb": ["10"], "padoms": "19,25 : 2 ≈ 9,6 - uz augšu."},
            ]),
            pavediens="maja",
            konteksts="Remontā materiālus rēķina no telpas izmēriem - "
                      "viena izteiksme der visām istabām.",
            kapec="Izteiksme ļauj pārrēķināt katrai istabai."),

    Kopsavilkums([
        "Izsaku figūras malas ar mainīgo.",
        "Pierakstu un vienkāršoju perimetru.",
        "Pierakstu laukumu kā izteiksmi.",
        "Aprēķinu konkrētam mainīgā lielumam.",
    ]),

    Majas([
        "Izmēri savu istabu un uzraksti līstes garumu ar x.",
        "Uzzīmē L figūru un uzraksti tās perimetru.",
        "Aprēķini parketa paku skaitu savai istabai.",
    ]),
]
