# -*- coding: utf-8 -*-
"""9. klase, 103. stunda: «Kas ir vienādojuma atrisinājums?»

Vienādojumam ar diviem nezināmajiem x + y = 10 atrisinājums ir skaitļu
PĀRIS, un tādu pāru ir bezgalīgi daudz. Stunda sākas ar maksājumu ar divu
veidu monētām - katrs veids, kā samaksāt, ir viens atrisinājums.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, restis)

TEMA = "Kas ir vienādojuma atrisinājums?"

MERKIS = ("Noteiksim skaitļu pārus, kas apmierina vienādojumu ar diviem "
          "nezināmajiem.")

SATURS = [
    Sakums("10 € ar 1 € un 2 € monētām - cik veidu?",
           zimejums=restis([["1 € (x)", "10", "8", "6", "4", "2", "0"],
                            ["2 € (y)", "0", "1", "2", "3", "4", "5"]]),
           paraksts="x + 2y = 10: katra kolonna ir viens atrisinājums.",
           fakti=["Atrisinājums ir skaitļu pāris (x; y).",
                  "Pārī secība svarīga: (2; 4) ≠ (4; 2).",
                  "Ja der arī daļskaitļi - pāru ir bezgalīgi daudz."]),

    Doma("Vienādojums ar diviem nezināmajiem",
         "Skaitļu pāris (x; y) ir vienādojuma atrisinājums, ja, ievietojot x "
         "un y, iegūst patiesu vienādību.",
         soli=[
             "Pāri raksta (x; y) - vispirms x, tad y.",
             "Pārbaude: ievieto abus skaitļus.",
             "Lai atrastu pāri: izvēlies x un aprēķini y.",
             "Lineāram vienādojumam atrisinājumu ir bezgalīgi daudz.",
         ]),

    Paraugs("Pārbaudi pāri",
            uzd="Vai pāris (3; −1) ir vienādojuma 2x − 5y = 11 atrisinājums?",
            soli=[
                ("2 · 3 − 5 · (−1) = 6 + 5 = 11", "Ievieto x = 3, y = −1."),
                ("11 = 11", "Patiesa vienādība."),
            ],
            atbilde="jā"),

    Varianti("Atrisinājums vai nē?", [
        {"jaut": "(2; 3) vienādojumam x + y = 5",
         "opcijas": ["Jā", "Nē"], "jaukt": False,
         "pareizi": 0, "padoms": "2 + 3 = 5."},
        {"jaut": "(3; 2) vienādojumam 2x − y = 1",
         "opcijas": ["Jā", "Nē"], "jaukt": False,
         "pareizi": 1, "padoms": "6 − 2 = 4 ≠ 1."},
        {"jaut": "(−1; 4) vienādojumam 3x + y = 1",
         "opcijas": ["Jā", "Nē"], "jaukt": False,
         "pareizi": 0, "padoms": "−3 + 4 = 1."},
        {"jaut": "(0; 0) vienādojumam 5x − 7y = 0",
         "opcijas": ["Jā", "Nē"], "jaukt": False,
         "pareizi": 0, "padoms": "0 = 0."},
    ]),

    Ievadi("Atrodi trūkstošo", [
        {"jaut": "x + y = 12, x = 5. y = ?", "atb": ["7"],
         "padoms": "12 − 5."},
        {"jaut": "2x + y = 9, x = 3. y = ?", "atb": ["3"],
         "padoms": "9 − 6."},
        {"jaut": "x − 3y = 4, y = 2. x = ?", "atb": ["10"],
         "padoms": "4 + 6."},
        {"jaut": "3x + 2y = 12, y = 0. x = ?", "atb": ["4"],
         "padoms": "3x = 12."},
        {"jaut": "y = 2x − 1, x = −2. y = ?", "atb": ["−5", "-5"],
         "padoms": "−4 − 1."},
    ], pamats=3),

    Pasaule("Kino biļetes",
            Ievadi("", [
                {"jaut": "Bērnu biļete 4 €, pieaugušā 7 €; kopā samaksāti 29 €. "
                         "4x + 7y = 29. Ja pieaugušais ir viens (y = 1), "
                         "aprēķini x.", "atb": ["5,5"],
                 "padoms": "4x = 22; x = 5,5 - bērnu skaitam neder!"},
                {"jaut": "Ja pieaugušie ir trīs (y = 3), cik bērnu?",
                 "atb": ["2"], "padoms": "4x = 8."},
            ]),
            pavediens="veikals",
            konteksts="Kasē redz tikai kopsummu; no tās jāuzmin, cik biļešu "
                      "katra veida pirka.",
            kapec="Matemātiski der daudzi pāri, dzīvē - tikai veseli."),

    Kopsavilkums([
        "Zinu, ka atrisinājums ir skaitļu pāris.",
        "Pārbaudu pāri, ievietojot abus skaitļus.",
        "Atrodu atrisinājumus, izvēloties vienu nezināmo.",
    ]),

    Majas([
        "Atrodi 3 atrisinājumus vienādojumam 2x + 3y = 12.",
        "Cik veidos 20 € var samaksāt ar 2 € un 5 € monētām?",
        "Izdomā vienādojumu, kuram (1; 4) ir atrisinājums.",
    ]),
]
