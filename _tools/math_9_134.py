# -*- coding: utf-8 -*-
"""9. klase, 134. stunda: «Vai skaitlis pieder progresijai?»

Skaitlis pieder progresijai, ja vienādojumam a_1 + (n − 1)d = skaitlis ir
naturāla sakne n. Ja n iznāk daļskaitlis vai negatīvs - nepieder. Tā
pamato atbildi, nevis izrakstot locekļus.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, restis)

TEMA = "Vai skaitlis pieder progresijai?"

MERKIS = ("Noteiksim, vai dotais skaitlis ir progresijas loceklis, un "
          "pamatosim atbildi.")

SATURS = [
    Sakums("Vai 100 ir virknē 4, 7, 10, 13, ...?",
           zimejums=restis([["n", "1", "2", "3", "…", "32", "33", "34"],
                            ["aₙ", "4", "7", "10", "…", "97", "100", "103"]]),
           paraksts="3n + 1 = 100 ⇒ n = 33 - pieder!",
           fakti=["Pieraksti vispārīgo locekli un pielīdzini.",
                  "Ja n ir naturāls - pieder.",
                  "Ja n = 33,33... - nepieder."]),

    Doma("Pārbaude ar vienādojumu",
         "Skaitlis b pieder progresijai, ja a_1 + (n − 1)d = b ir atrisināms "
         "ar naturālu n.",
         soli=[
             "Uzraksti a_n ar formulu.",
             "Pielīdzini dotajam skaitlim.",
             "Atrisini attiecībā pret n.",
             "n ∈ ℕ - pieder; citādi - nepieder.",
         ]),

    Paraugs("Nepieder",
            uzd="Vai 50 ir progresijas 2, 9, 16, ... loceklis?",
            soli=[
                ("a_n = 2 + (n − 1) · 7 = 7n − 5", "Formula."),
                ("7n − 5 = 50 ⇒ n = {55|7}", "Nav naturāls."),
                ("Tuvākie: a_7 = 44, a_8 = 51", "Pārbaude."),
            ],
            atbilde="nepieder"),

    Ievadi("Pieder? Ieraksti numuru n (vai 0, ja nepieder)", [
        {"jaut": "Virkne 5, 9, 13, ...; skaitlis 45", "atb": ["11"],
         "padoms": "4n + 1 = 45."},
        {"jaut": "Virkne 3, 8, 13, ...; skaitlis 100", "atb": ["0"],
         "padoms": "5n − 2 = 100 ⇒ n = 20,4."},
        {"jaut": "Virkne 50, 46, 42, ...; skaitlis 2", "atb": ["13"],
         "padoms": "54 − 4n = 2."},
        {"jaut": "Virkne −7, −4, −1, ...; skaitlis 20", "atb": ["10"],
         "padoms": "3n − 10 = 20."},
    ]),

    Varianti("Pamato", [
        {"jaut": "Vai virknē a_n = 6n + 1 ir pāra skaitļi?",
         "opcijas": ["Nē - 6n + 1 vienmēr nepāra", "Jā", "Tikai n > 10",
                     "Tikai a_1"],
         "pareizi": 0, "padoms": "Pāra + 1."},
        {"jaut": "Kurš skaitlis pieder a_n = 4n − 1?",
         "opcijas": ["39", "40", "41", "42"],
         "pareizi": 0, "padoms": "4n = 40."},
    ]),

    Pasaule("Autobusa kustības saraksts",
            Ievadi("", [
                {"jaut": "Autobuss atiet 6:10, pēc tam ik 25 min. Vai ir reiss "
                         "tieši 9:30? Minūtes pēc 6:10: 200. 25(n − 1) = 200 "
                         "⇒ n = ?", "atb": ["9"], "padoms": "n − 1 = 8."},
                {"jaut": "Vai ir reiss 10:00 (230 min)? Ieraksti n vai 0.",
                 "atb": ["0"], "padoms": "230 : 25 = 9,2."},
            ]),
            pavediens="celojums",
            konteksts="Regulārs kustības saraksts ir aritmētiskā progresija "
                      "laikā.",
            kapec="Vienādojums atbild, vai reiss ir, bez visa saraksta."),

    Kopsavilkums([
        "Pārbaudu, vai skaitlis pieder progresijai.",
        "Atrodu tā numuru n.",
        "Pamatoju atbildi ar vienādojumu.",
    ]),

    Majas([
        "Vai 131 pieder progresijai 11, 15, 19, ...?",
        "Vai −40 pieder progresijai 10, 7, 4, ...?",
        "Atrodi sava autobusa sarakstā progresiju.",
    ]),
]
