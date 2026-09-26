# -*- coding: utf-8 -*-
"""7. klase, 164. stunda: «Cik preču var nopirkt par šo summu?»

Uzdevumos par budžetu atbilde nav viens skaitlis, bet kopa: «ne vairāk kā
6 preces». Stunda risina nevienādību un nosaka iespējamo vērtību kopu,
ņemot vērā, ka preču skaits ir vesels.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, taisne)

TEMA = "Cik preču var nopirkt par šo summu?"

MERKIS = ("Risināsim uzdevumu, kurā atbilde ir nezināmā vērtību kopa.")

SATURS = [
    Sakums("Kino ar 25 €: biļete 7 €, popkorns 4 €",
           zimejums=taisne(0, 6, 1, [(0, ""), (1, ""), (2, ""), (3, "")]),
           paraksts="Biļešu skaits n: 0; 1; 2; 3.",
           fakti=["7n + 4 ≤ 25 ⇒ n ≤ 3.",
                  "Atbilde - kopa {0; 1; 2; 3}, nevis viens skaitlis.",
                  "Visvairāk - 3 biļetes."]),

    Doma("Nevienādība → veseli atrisinājumi",
         "Ja nezināmais ir skaits, no nevienādības atrisinājuma izvēlas "
         "tikai veselos nenegatīvos skaitļus. Bieži jautā par lielāko vai "
         "mazāko no tiem.",
         soli=[
             "Uzraksti nevienādību.",
             "Atrisini: x ≤ 3,6.",
             "Izvēlies veselos: 0; 1; 2; 3.",
             "Atbildi uz jautājumu (lielākais - 3).",
         ]),

    Paraugs("Budžets",
            uzd="Ir 50 €. Jāpērk sporta krekls par 18 € un zeķes pa 3,5 € "
                "pārī. Cik pāru zeķu var nopirkt?",
            soli=[
                ("18 + 3,5n ≤ 50", "Nevienādība."),
                ("3,5n ≤ 32, n ≤ 9,14...", "Atrisina."),
                ("n ∈ {0; 1; ...; 9}", "Veseli."),
            ],
            atbilde="Ne vairāk kā 9 pārus."),

    Ievadi("Aprēķini", [
        {"jaut": "Ir 20 €, klade 1,8 €. Lielākais klažu skaits?",
         "atb": ["11"], "padoms": "20 : 1,8 ≈ 11,1."},
        {"jaut": "Ir 100 €, jāatstāj vismaz 30 €, spēle 12 €. Cik spēļu?",
         "atb": ["5"], "padoms": "12n ≤ 70."},
        {"jaut": "Taksometrs 3 € + 0,9 € par km, ir 15 €. Cik pilnu km?",
         "atb": ["13"], "padoms": "0,9x ≤ 12, x ≤ 13,3."},
        {"jaut": "Vismaz 40 punkti; par uzdevumu 6 punkti. Mazākais "
                 "uzdevumu skaits?",
         "atb": ["7"], "padoms": "6n ≥ 40, n ≥ 6,67."},
    ]),

    Varianti("Pareizā atbilde", [
        {"jaut": "Atrisinājums n ≤ 4,8 (n - preču skaits). Atbilde?",
         "opcijas": ["0; 1; 2; 3; 4", "4,8", "5", "Visi skaitļi līdz 4,8"],
         "pareizi": 0, "padoms": "Veseli."},
        {"jaut": "Atrisinājums n ≥ 2,1 (autobusu skaits). Mazākais?",
         "opcijas": ["3", "2", "2,1", "1"],
         "pareizi": 0, "padoms": "Vesels, ne mazāks par 2,1."},
    ]),

    Pasaule("Klases ballīte",
            Ievadi("", [
                {"jaut": "Budžets 120 €. Picas pa 11 €, dzērieni kopā 25 €. "
                         "Cik picu var pasūtīt?",
                 "atb": ["8"], "padoms": "11n ≤ 95."},
                {"jaut": "Cik € paliks, ja pasūta maksimālo skaitu?",
                 "atb": ["7"], "padoms": "120 − 25 − 88."},
                {"jaut": "Klasē 24 skolēni, picā 8 gabali. Vai pietiks pa 2 "
                         "gabaliem katram? Raksti «jā» vai «nē».",
                 "atb": ["jā", "ja"], "padoms": "64 ≥ 48."},
            ]),
            pavediens="skola",
            konteksts="Pasākuma budžets vienmēr ir «ne vairāk kā» - "
                      "nevienādība.",
            kapec="Atbilde - iespēju kopa."),

    Kopsavilkums([
        "Uzrakstu nevienādību budžeta uzdevumam.",
        "Izvēlos veselos atrisinājumus.",
        "Atrodu lielāko vai mazāko iespējamo skaitu.",
        "Pārbaudu, ka paliek nauda (≥ 0).",
    ]),

    Majas([
        "Plāno dzimšanas dienas budžetu ar nevienādību.",
        "Aprēķini, cik biļešu var nopirkt ģimenei par 60 €.",
        "Izdomā uzdevumu ar atbildi «vismaz 5».",
    ]),
]
