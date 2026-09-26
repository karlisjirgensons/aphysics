# -*- coding: utf-8 -*-
"""3. klase, 27. stunda: «Kā dalīt 48 ar 4?»

Dalīšana pa daļām ir reizināšanas pa daļām spogulis: desmitus izdala
atsevišķi, vienus atsevišķi. Grūtākais gadījums ir tas, kurā desmiti nedalās
gludi (72 : 6), un to te modelē ar desmita sadalīšanu - no šī soļa vēlāk aug
dalīšana ar aizņēmumu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, Zimejums,
                         restis)

TEMA = "Kā dalīt 48 ar 4?"

MERKIS = ("Iemācīsimies dalīt divciparu skaitli ar viencipara skaitli, "
          "izmantojot decimālā sastāva modeli.")

SATURS = [
    Sakums("Kā izdalīt to, kā tabulā nav?",
           zimejums=restis([[48, "=", 40, "+", 8],
                            [": 4", "", 10, "+", 2]],
                           "48 : 4 = 12"),
           paraksts="Vispirms dala desmitus, tad vienus.",
           fakti=["Tabulā lielākais dalāmais ir 100, bet ne katrs skaitlis.",
                  "Divciparu skaitli dala pa daļām - vispirms desmitus."]),

    Doma("Vispirms izdali desmitus, tad vienus",
         "48 : 4 = 40 : 4 + 8 : 4 - katru daļu dala atsevišķi un rezultātus "
         "saskaita.",
         soli=[
             "Sadali dalāmo desmitos un vienos: 48 ir 40 un 8.",
             "Izdali desmitus: 40 : 4 = 10.",
             "Izdali vienus: 8 : 4 = 2.",
             "Saskaiti abus rezultātus: 10 + 2 = 12.",
         ],
         pieze="Ja desmiti gludi nedalās, vienu desmitu sadala vienos: "
               "72 : 6 - ņem 60 : 6 = 10 un 12 : 6 = 2, kopā 12."),

    Slidnis("Kā dala 72 ar 6",
            soli=[
                {"v": "72 = 60 + 12",
                 "teksts": "Sadala tā, lai abas daļas dalītos ar 6.",
                 "josla": 30},
                {"v": "60 : 6 = 10", "teksts": "Izdala desmitus.",
                 "josla": 60},
                {"v": "12 : 6 = 2", "teksts": "Izdala atlikušos.",
                 "josla": 80},
                {"v": "10 + 2 = 12", "teksts": "Saskaita abas daļas.",
                 "josla": 100},
            ],
            ievads="Sadalījums nav jāņem pēc kārtas - to izvēlas tā, lai "
                   "abas daļas dalītos."),

    Paraugs("Cik ir 96 : 3?",
            uzd="Izdali 96 ar 3, sadalot skaitli pa daļām.",
            soli=[
                ("96 = 90 + 6",
                 "Sadala desmitos un vienos."),
                ("90 : 3 = 30",
                 "Deviņi desmiti, sadalīti trijās daļās, ir trīs desmiti."),
                ("6 : 3 = 2",
                 "Vienus dala pēc tabulas."),
                ("30 + 2 = 32",
                 "Abas daļas saskaita; pārbaude: 32 · 3 = 96."),
            ],
            atbilde="32"),

    Ievadi("Dali pa daļām", [
        {"jaut": "48 : 4 = ?", "atb": ["12"], "padoms": "10 + 2."},
        {"jaut": "69 : 3 = ?", "atb": ["23"], "padoms": "20 + 3."},
        {"jaut": "84 : 4 = ?", "atb": ["21"], "padoms": "20 + 1."},
        {"jaut": "72 : 6 = ?", "atb": ["12"], "padoms": "60 : 6 un 12 : 6."},
        {"jaut": "90 : 5 = ?", "atb": ["18"], "padoms": "50 : 5 un 40 : 5."},
        {"jaut": "56 : 4 = ?", "atb": ["14"], "padoms": "40 : 4 un 16 : 4."},
    ], pamats=4,
        ievads="Sadali dalāmo tā, lai abas daļas dalītos bez atlikuma."),

    Zimejums("Divi soļi vienā dalījumā",
             restis([["60 : 6 = 10", "12 : 6 = 2"],
                     ["desmiti", "atlikušie"]],
                    "72 : 6 = 12"),
             paskaidro="Sadalījumu izvēlas pats: 72 var sadalīt arī kā "
                       "30 + 42, un atbilde būs tā pati.",
             ievads="Tā izskatās dalīšana pa daļām."),

    Varianti("Kurš sadalījums ir ērtākais?", [
        {"jaut": "Kā ērtāk sadalīt 84, dalot ar 4?",
         "opcijas": ["80 + 4", "40 + 44", "84 + 0", "8 + 4"],
         "pareizi": 0, "padoms": "Abas daļas dalās ar 4."},
        {"jaut": "Kā ērtāk sadalīt 78, dalot ar 6?",
         "opcijas": ["60 + 18", "70 + 8", "40 + 38", "78 + 0"],
         "pareizi": 0, "padoms": "60 un 18 abi dalās ar 6."},
        {"jaut": "Cik ir 75 : 5?",
         "opcijas": ["15", "14", "16", "25"],
         "pareizi": 0, "padoms": "50 : 5 = 10 un 25 : 5 = 5."},
        {"jaut": "Kā pārbaudīt, ka 84 : 4 = 21?",
         "opcijas": ["21 · 4 = 84", "84 · 4", "21 : 4", "84 + 4"],
         "pareizi": 0, "padoms": "Pretējā darbība."},
    ], pamats=4),

    Pasaule("Cik maksā viena prece?",
            Ievadi("", [
                {"jaut": "4 burtnīcas kopā maksā 48 ct. Cik maksā viena?",
                 "atb": ["12"], "padoms": "48 : 4."},
                {"jaut": "6 zīmuļi maksā 72 ct. Cik maksā viens?",
                 "atb": ["12"], "padoms": "72 : 6."},
                {"jaut": "3 mapes maksā 69 ct. Cik maksā viena?",
                 "atb": ["23"], "padoms": "69 : 3."},
                {"jaut": "Cik maksās 5 zīmuļi, ja viens maksā 12 ct?",
                 "atb": ["60"], "padoms": "5 · 12."},
            ]),
            pavediens="veikals",
            konteksts="Uz cenu zīmes bieži raksta komplekta cenu - vienas "
                      "preces cenu pircējs izrēķina pats.",
            kapec="Tikai zinot vienas preces cenu, var salīdzināt divus "
                  "veikalus."),

    Kopsavilkums([
        "Dalu divciparu skaitli ar viencipara skaitli.",
        "Sadalu dalāmo tā, lai abas daļas dalītos bez atlikuma.",
        "Vispirms dalu desmitus, tad atlikušos vienus.",
        "Pārbaudu rezultātu ar reizināšanu.",
    ]),

    Majas([
        "Izdali 96 ar 4, 85 ar 5 un 78 ar 6 un pārbaudi katru.",
        "Atrodi veikalā komplekta cenu un izrēķini vienas preces cenu.",
        "Izdomā divciparu skaitli, kas dalās gan ar 3, gan ar 4.",
    ]),
]
