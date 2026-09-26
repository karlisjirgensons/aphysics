# -*- coding: utf-8 -*-
"""4. klase, 76. stunda: «Kāpēc sanāk četri saskaitāmie?»

Ģeometriskais modelis: taisnstūris 23 × 14 sadalās četrās daļās, jo abus
reizinātājus sadala desmitos un vienos - 20 · 10, 20 · 4, 3 · 10, 3 · 4.
Šis «logs» ir tas pats, ko 8. klasē sauks par (a + b)(c + d).
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kāpēc sanāk četri saskaitāmie?"

MERKIS = ("Modelēsim reizinājumu ģeometriski un secināsim, ka tas veidojas "
          "no četriem reizinājumiem.")

SATURS = [
    Sakums("Kā izrēķināt dārza laukumu 23 m × 14 m?",
           zimejums=restis([["·", "20", "3"],
                            ["10", "200", "30"],
                            ["4", "80", "12"]],
                           "23 · 14 - četri gabali"),
           paraksts="200 + 30 + 80 + 12 = 322.",
           fakti=["Abus skaitļus sadala: 23 = 20 + 3, 14 = 10 + 4.",
                  "Taisnstūris sadalās četrās mazākās daļās."]),

    Doma("Divi sadalījumi - četri gabali",
         "Ja abus reizinātājus sadala desmitos un vienos, reizinājums ir "
         "četru mazu reizinājumu summa.",
         soli=[
             "Sadali: 23 = 20 + 3, 14 = 10 + 4.",
             "Uzzīmē tabulu: rindās 10 un 4, kolonnās 20 un 3.",
             "Aizpildi katru rūtiņu ar reizinājumu.",
             "Saskaiti visas četras rūtiņas.",
         ],
         pieze="Šo tabulu sauc arī par «reizināšanas logu» - tā parāda, kāpēc "
               "neviens gabals nepazūd."),

    Paraugs("36 · 25 ar logu",
            uzd="Izrēķini 36 · 25, izmantojot četrus gabalus.",
            soli=[
                ("30 · 20 = 600", None),
                ("6 · 20 = 120", None),
                ("30 · 5 = 150", None),
                ("6 · 5 = 30", None),
                ("600 + 120 + 150 + 30 = 900", None),
            ],
            atbilde="900"),

    Zimejums("Logs 36 · 25",
             restis([["·", "30", "6"],
                     ["20", "600", "120"],
                     ["5", "150", "30"]],
                    "36 · 25 = 900"),
             paskaidro="Lielākais gabals ir desmiti reiz desmiti; mazākais - "
                       "vieni reiz vieni.",
             ievads="Katra rūtiņa - viens no četriem reizinājumiem."),

    Ievadi("Aizpildi logu", [
        {"jaut": "23 · 14: gabals 20 · 10 = ?", "atb": ["200"],
         "padoms": "2 · 1 un 00."},
        {"jaut": "23 · 14: gabals 3 · 4 = ?", "atb": ["12"],
         "padoms": "Vieni reiz vieni."},
        {"jaut": "42 · 31: visu četru gabalu summa?", "atb": ["1302"],
         "padoms": "1200 + 40 + 60 + 2."},
        {"jaut": "15 · 15 = ?", "atb": ["225"],
         "padoms": "100 + 50 + 50 + 25."},
        {"jaut": "27 · 13 = ?", "atb": ["351"],
         "padoms": "200 + 70 + 60 + 21."},
        {"jaut": "64 · 22 = ?", "atb": ["1408"],
         "padoms": "1200 + 80 + 120 + 8."},
    ], pamats=4),

    Varianti("Kas trūkst?", [
        {"jaut": "Ieva: 23 · 14 = 200 + 12 = 212. Kas nav kārtībā?",
         "opcijas": ["pazaudēja divus gabalus (30 un 80)",
                     "viss pareizi", "sajauca ciparus"], "pareizi": 0,
         "padoms": "Jābūt četriem saskaitāmajiem."},
        {"jaut": "Cik gabalu sanāk, reizinot 45 · 32 ar logu?",
         "opcijas": ["4", "2", "3", "6"], "pareizi": 0,
         "padoms": "2 · 2."},
        {"jaut": "Kurš gabals ir lielākais 45 · 32 logā?",
         "opcijas": ["40 · 30", "5 · 2", "40 · 2", "5 · 30"], "pareizi": 0,
         "padoms": "Desmiti reiz desmiti."},
    ]),

    Pasaule("Futbola laukuma mākslīgais zālājs",
            Ievadi("", [
                {"jaut": "Treniņu laukums 42 m × 25 m. Gabals 40 · 20 = ?",
                 "atb": ["800"], "padoms": "4 · 2 un 00."},
                {"jaut": "Visi četri gabali: 800 + 200 + 40 + 10. Laukums m²?",
                 "atb": ["1050"], "padoms": "Saskaiti."},
                {"jaut": "Zālāja rullis sedz 25 m². Cik rulļu vajag 1050 m²?",
                 "atb": ["42"], "padoms": "1050 : 25."},
                {"jaut": "Rullis maksā 90 €. Cik maksā 42 rulļi?",
                 "atb": ["3780"], "padoms": "90 · 40 + 90 · 2."},
            ]),
            pavediens="sports",
            konteksts="Laukumu platība ir taisnstūris - tās aprēķināšana ir "
                      "tas pats «logs».",
            kapec="Logs parāda, kāpēc katram gabalam jābūt saskaitītam."),

    Kopsavilkums([
        "Modelēju reizinājumu ar taisnstūri, sadalītu četrās daļās.",
        "Zinu, ka divu divciparu skaitļu reizinājumā ir 4 saskaitāmie.",
        "Lietoju «reizināšanas logu».",
    ]),

    Majas([
        "Uzzīmē logu 24 · 13 un aizpildi.",
        "Izmēri istabu soļos un izrēķini laukumu ar logu.",
        "Paskaidro kādam, kāpēc 23 · 14 nav 200 + 12.",
    ]),
]
