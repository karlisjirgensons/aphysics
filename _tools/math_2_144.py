# -*- coding: utf-8 -*-
"""2. klase, 144. stunda: «Ko nozīmē reizināt ar 4?»

Reizināt ar 4 - divreiz dubultot: 6 · 4 = 6 · 2 · 2 = 12 · 2 = 24. Ja zina
reizinājumus ar 2, reizinājumus ar 4 var atrast, vienkārši dubultojot
vēlreiz.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, rutinas)

TEMA = "Ko nozīmē reizināt ar 4?"

MERKIS = ("Šodien modelēsim reizināšanu ar 4 kā divkāršu dubultošanu un "
          "pierakstīsim rezultātu.")

SATURS = [
    Sakums("Kā ātri izrēķināt 7 · 4, ja zini tikai reizināšanu ar 2?",
           zimejums=rutinas(7, 4),
           paraksts="4 rindas pa 7 - tās ir 2 rindas pa 7, divreiz.",
           fakti=["7 · 2 = 14 - dubults.",
                  "14 · 2 = 28 - vēlreiz dubults.",
                  "7 · 4 = 28."]),

    Doma("Divreiz dubultot",
         "Reizināt ar 4 - dubultot un vēlreiz dubultot.",
         soli=[
             "Dubulto skaitli: 6 → 12.",
             "Dubulto vēlreiz: 12 → 24.",
             "Tātad 6 · 4 = 24.",
             "Pārbaudi: 6 + 6 + 6 + 6 = 24.",
         ]),

    Slidnis("5 · 4 soli pa solim", [
        {"v": "5", "teksts": "Viena rinda.", "zim": rutinas(5, 4, 5, 1)},
        {"v": "5 · 2 = 10", "teksts": "Dubults.", "zim": rutinas(5, 4, 5, 2)},
        {"v": "10 · 2 = 20", "teksts": "Vēlreiz dubults.",
         "zim": rutinas(5, 4, 5, 4)},
    ]),

    Paraugs("8 · 4",
            uzd="Aprēķini, divreiz dubultojot.",
            soli=[("8 · 2 = 16", "Pirmais dubults."),
                  ("16 · 2 = 32", "Otrais dubults.")],
            atbilde="8 · 4 = 32"),

    Ievadi("Reizini ar 4", [
        {"jaut": "3 · 4 = ?", "atb": ["12"], "padoms": "6, 12."},
        {"jaut": "4 · 4 = ?", "atb": ["16"], "padoms": "8, 16."},
        {"jaut": "6 · 4 = ?", "atb": ["24"], "padoms": "12, 24."},
        {"jaut": "9 · 4 = ?", "atb": ["36"], "padoms": "18, 36."},
        {"jaut": "10 · 4 = ?", "atb": ["40"], "padoms": "20, 40."},
        {"jaut": "7 · 4 = ?", "atb": ["28"], "padoms": "14, 28."},
    ], pamats=4),

    Varianti("Kā aprēķināt?", [
        {"jaut": "Kā ātri aprēķināt 9 · 4?",
         "opcijas": ["18 un vēlreiz dubultot", "9 + 4", "9 · 2 + 2"],
         "pareizi": 0, "padoms": "Divreiz dubultot."},
        {"jaut": "2 · 4 ir tas pats, kas...",
         "opcijas": ["4 · 2 = 8", "2 + 4 = 6", "2 · 2 = 4"], "pareizi": 0,
         "padoms": "Vietas maiņa."},
    ]),

    Pasaule("Galdi ēdnīcā",
            Ievadi("", [
                {"jaut": "Pie katra galda 4 krēsli. Cik krēslu pie 8 galdiem?",
                 "atb": ["32"], "padoms": "16, 32."},
                {"jaut": "Ēdnīcā pusdieno 36 bērni. Cik galdu vajag?",
                 "atb": ["9"], "padoms": "? · 4 = 36."},
            ]),
            pavediens="skola",
            konteksts="Skolas ēdnīcā pie galdiem sēž pa četri.",
            kapec="Dubultojot divreiz, rēķina ātri."),

    Kopsavilkums([
        "Reizinu ar 4, divreiz dubultojot.",
        "Pārbaudu ar saskaitīšanu.",
        "Izmantoju zināmos reizinājumus ar 2.",
    ]),

    Majas([
        "Aprēķini dubultojot: 4 · 4, 6 · 4, 8 · 4.",
        "Pārbaudi ar saskaitīšanu.",
        "Paskaidro mājiniekam triku.",
    ]),
]
