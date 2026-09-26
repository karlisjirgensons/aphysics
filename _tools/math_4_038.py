# -*- coding: utf-8 -*-
"""4. klase, 38. stunda: «Kā reizināt veikli?»

Ne katru reizinājumu vajag rēķināt pa šķirām. 199 · 5 = (200 − 1) · 5, un
120 · 5 = 12 · 10 · 5 = 12 · 50. Stunda krāj «trikus», kas balstās uz jau
zināmām īpašībām, un māca pamanīt, kad tie der.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, restis)

TEMA = "Kā reizināt veikli?"

MERKIS = ("Lietosim ērtus pārveidojumus: 199 · 5 = (200 − 1) · 5 un "
          "120 · 5 = 12 · 10 · 5.")

SATURS = [
    Sakums("Cik maksā 5 telefoni pa 199 €?",
           zimejums=restis([["199 · 5", "=", "(200 − 1) · 5"],
                            ["", "=", "1000 − 5"],
                            ["", "=", "995"]],
                           "veikls triks"),
           paraksts="199 ir gandrīz 200 - tāpēc rēķina ar 200.",
           fakti=["Cenas bieži beidzas ar 99 - lai izskatās lētāk.",
                  "Bet reizināt tās ir viegli, ja domā par apaļo skaitli."]),

    Doma("Pārveido, lai rēķins kļūtu apaļš",
         "Tuvu apaļam skaitlim - reizini apaļo un atņem liekumu; reizinātāja "
         "nulli vai 5 - apvieno ar pāri.",
         soli=[
             "Tuvu apaļam: 198 · 4 = 200 · 4 − 2 · 4 = 800 − 8.",
             "Nulle galā: 120 · 5 = 12 · 50 = 600.",
             "Pāris ar 5: 5 · 146 = 146 · 10 : 2 = 730.",
             "Pārbaudi ar aptuveno vērtību.",
         ],
         pieze="Reizināt ar 5 ir tas pats, kas reizināt ar 10 un dalīt ar 2."),

    Paraugs("299 · 3",
            uzd="Izrēķini veikli 299 · 3.",
            soli=[
                ("299 = 300 − 1", None),
                ("300 · 3 = 900", None),
                ("1 · 3 = 3", None),
                ("900 − 3 = 897", None),
            ],
            atbilde="897"),

    Ievadi("Triku stunda", [
        {"jaut": "199 · 5 = ?", "atb": ["995"], "padoms": "1000 − 5."},
        {"jaut": "120 · 5 = ?", "atb": ["600"], "padoms": "12 · 50."},
        {"jaut": "98 · 6 = ?", "atb": ["588"], "padoms": "600 − 12."},
        {"jaut": "250 · 4 = ?", "atb": ["1000"], "padoms": "25 · 4 = 100."},
        {"jaut": "401 · 7 = ?", "atb": ["2807"], "padoms": "2800 + 7."},
        {"jaut": "146 · 5 = ?", "atb": ["730"], "padoms": "1460 : 2."},
        {"jaut": "999 · 8 = ?", "atb": ["7992"], "padoms": "8000 − 8."},
        {"jaut": "160 · 5 = ?", "atb": ["800"], "padoms": "16 · 50."},
    ], pamats=6),

    Varianti("Kurš triks der?", [
        {"jaut": "Kā veikli izrēķināt 399 · 4?",
         "opcijas": ["400 · 4 − 4", "399 + 4", "400 · 4 + 1",
                     "4 · 4 · 99"], "pareizi": 0,
         "padoms": "399 = 400 − 1."},
        {"jaut": "Kā veikli izrēķināt 240 · 5?",
         "opcijas": ["24 · 50", "24 · 5", "240 + 5", "2 · 4 · 5"],
         "pareizi": 0, "padoms": "240 = 24 · 10."},
        {"jaut": "Kā veikli izrēķināt 88 · 5?",
         "opcijas": ["880 : 2", "88 · 10 · 2", "88 + 5", "80 · 5"],
         "pareizi": 0, "padoms": "Reizini ar 10, dali ar 2."},
        {"jaut": "Cik ir 201 · 6?",
         "opcijas": ["1206", "1260", "1200", "1216"], "pareizi": 0,
         "padoms": "1200 + 6."},
    ], pamats=4),

    Pasaule("Iepirkšanās ar 99 centiem",
            Ievadi("", [
                {"jaut": "Grāmata maksā 9 € 99 ct = 999 ct. Cik centu maksā "
                         "3 grāmatas?",
                 "atb": ["2997"], "padoms": "3000 − 3."},
                {"jaut": "Austiņas 49 €. Cik maksā 4 austiņas?",
                 "atb": ["196"], "padoms": "200 − 4."},
                {"jaut": "Šokolāde 1 € 99 ct = 199 ct. Cik centu maksā 6?",
                 "atb": ["1194"], "padoms": "1200 − 6."},
                {"jaut": "Bumba 25 €. Cik maksā 8 bumbas?",
                 "atb": ["200"], "padoms": "25 · 4 · 2."},
            ]),
            pavediens="veikals",
            konteksts="Tirgotāji cenas beidz ar 99 - bet tu vari tās "
                      "sareizināt galvā ātrāk par kasi.",
            kapec="Veikls triks pārbauda čeku divās sekundēs."),

    Kopsavilkums([
        "Reizinu skaitli, kas tuvu apaļam, ar trikiem (200 − 1).",
        "Izmantoju nulles galā: 120 · 5 = 12 · 50.",
        "Reizinu ar 5 kā ar 10 un dalu ar 2.",
    ]),

    Majas([
        "Atrodi reklāmā 3 cenas, kas beidzas ar 99, un izrēķini 4 gab. cenu.",
        "Izdomā savu triku reizināšanai ar 9.",
        "Izaicini mājiniekus: kurš ātrāk izrēķinās 499 · 2?",
    ]),
]
