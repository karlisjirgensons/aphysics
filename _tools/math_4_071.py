# -*- coding: utf-8 -*-
"""4. klase, 71. stunda: «Kā reizināt ar pilniem desmitiem?»

23 · 40 = 23 · 4 · 10: vispirms reizina ar viencipara skaitli (to jau
prot), tad ar 10. Tā divciparu reizinātājs vairs nebaida - pilns desmits ir
tikai viencipara skaitlis, kam piekabināta nulle.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, restis)

TEMA = "Kā reizināt ar pilniem desmitiem?"

MERKIS = ("Reizināsim divciparu skaitli ar pilniem desmitiem, izsakot tos kā "
          "reizinājumu ar 10.")

SATURS = [
    Sakums("Cik maksā 30 biļetes pa 23 €?",
           zimejums=restis([["23 · 30", "=", "23 · 3 · 10"],
                            ["", "=", "69 · 10"],
                            ["", "=", "690"]],
                           "pilns desmits = viencipara · 10"),
           paraksts="30 = 3 · 10.",
           fakti=["Klases braucienam vajag 30 biļetes.",
                  "Divi viegli soļi aizstāj vienu grūtu."]),

    Doma("Pilns desmits ir viencipara skaitlis reiz 10",
         "a · 40 = a · 4 · 10: vispirms reizina ar 4, tad ar 10.",
         soli=[
             "Uzraksti pilno desmitu kā reizinājumu: 40 = 4 · 10.",
             "Sareizini ar viencipara skaitli: 23 · 4 = 92.",
             "Reizini ar 10: 92 · 10 = 920.",
             "Aptuvenā pārbaude: 20 · 40 = 800 - tuvu.",
         ],
         pieze="Reizinātājus drīkst grupēt - tāpēc drīkst rēķināt pa "
               "soļiem."),

    Paraugs("56 · 70",
            uzd="Izrēķini 56 · 70.",
            soli=[
                ("70 = 7 · 10", None),
                ("56 · 7 = 392", "Ar viencipara skaitli."),
                ("392 · 10 = 3920", None),
            ],
            atbilde="3920"),

    Slidnis("Divi soļi",
            soli=[
                {"v": "34 · 60", "teksts": "Uzdevums."},
                {"v": "34 · 6 · 10", "teksts": "60 = 6 · 10."},
                {"v": "204 · 10", "teksts": "34 · 6 = 204."},
                {"v": "2040", "teksts": "Pieliek nulli."},
            ]),

    Ievadi("Reizini ar desmitiem", [
        {"jaut": "23 · 30 = ?", "atb": ["690"], "padoms": "69 · 10."},
        {"jaut": "14 · 50 = ?", "atb": ["700"], "padoms": "70 · 10."},
        {"jaut": "48 · 20 = ?", "atb": ["960"], "padoms": "96 · 10."},
        {"jaut": "36 · 40 = ?", "atb": ["1440"], "padoms": "144 · 10."},
        {"jaut": "75 · 80 = ?", "atb": ["6000"], "padoms": "600 · 10."},
        {"jaut": "99 · 90 = ?", "atb": ["8910"], "padoms": "891 · 10."},
    ], pamats=4),

    Varianti("Kurš ceļš pareizs?", [
        {"jaut": "Kā izrēķināt 27 · 40?",
         "opcijas": ["27 · 4 · 10", "27 · 4 + 10", "27 + 40",
                     "27 · 40 · 10"], "pareizi": 0,
         "padoms": "40 = 4 · 10."},
        {"jaut": "Cik ir 27 · 40?",
         "opcijas": ["1080", "108", "10 800", "1040"], "pareizi": 0,
         "padoms": "27 · 4 = 108."},
        {"jaut": "Kurš reizinājums lielākais?",
         "opcijas": ["45 · 90", "45 · 9", "45 · 80", "40 · 90"],
         "pareizi": 0, "padoms": "Salīdzini reizinātājus."},
    ]),

    Pasaule("Sporta nometnes iepirkums",
            Ievadi("", [
                {"jaut": "Nometnē 30 bērni, katram T-krekls 12 €. Cik maksā "
                         "krekli?",
                 "atb": ["360"], "padoms": "12 · 3 · 10."},
                {"jaut": "Katram 20 € ēdināšanai. Cik par 30 bērniem?",
                 "atb": ["600"], "padoms": "20 · 30."},
                {"jaut": "Nometne ilgst 5 dienas, katru dienu 30 bērniem pa "
                         "2 āboliem. Cik ābolu dienā?",
                 "atb": ["60"], "padoms": "30 · 2."},
                {"jaut": "Cik ābolu visās 5 dienās?", "atb": ["300"],
                 "padoms": "60 · 5."},
            ]),
            pavediens="sports",
            konteksts="Nometnes organizatori rēķina visu 30 bērniem - un 30 "
                      "ir ērts pilns desmits.",
            kapec="Pilni desmiti padara lielus pasūtījumus vieglus."),

    Kopsavilkums([
        "Reizinu ar pilniem desmitiem divos soļos.",
        "Izsaku pilnu desmitu kā viencipara skaitli · 10.",
        "Pārbaudu ar aptuveno vērtību.",
    ]),

    Majas([
        "Izrēķini, cik maksā 20 tavas mīļākās konfektes.",
        "Izrēķini, cik minūšu ir 30 stundās (60 · 30).",
        "Izdomā divus reizinājumus ar pilniem desmitiem.",
    ]),
]
