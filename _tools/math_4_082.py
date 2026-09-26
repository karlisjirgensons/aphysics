# -*- coding: utf-8 -*-
"""4. klase, 82. stunda: «Kā dalāmo izteikt kā summu?»

575 : 25 = (500 + 75) : 25 = 20 + 3. Dalāmo sadala gabalos, kas katrs
dalās ar dalītāju - tā pati ideja, kas 32. stundā, tikai dalītājs tagad
divciparu. Galvenā prasme - atrast «draudzīgus» gabalus.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, restis)

TEMA = "Kā dalāmo izteikt kā summu?"

MERKIS = ("Dalīsim trīsciparu skaitli, izsakot dalāmo kā summu, piemēram, "
          "575 : 25 = (500 + 75) : 25.")

SATURS = [
    Sakums("Cik 25 € biļešu par 575 €?",
           zimejums=restis([["575", "=", "500", "+", "75"],
                            [": 25", "", "20", "+", "3"]],
                           "575 : 25 = 23"),
           paraksts="500 : 25 = 20 un 75 : 25 = 3.",
           fakti=["500 un 75 abi dalās ar 25.",
                  "Gabalu dalījumus saskaita."]),

    Doma("Sadali dalāmo gabalos, kas dalās",
         "(a + b) : c = a : c + b : c, ja abi gabali dalās ar c.",
         soli=[
             "Atrodi lielu gabalu, kas dalās: 575 → 500.",
             "Atlikušais: 575 − 500 = 75.",
             "Izdali katru: 500 : 25 = 20, 75 : 25 = 3.",
             "Saskaiti: 20 + 3 = 23. Pārbaude: 23 · 25 = 575.",
         ],
         pieze="Gabali var būt arī vairāk nekā divi: 888 : 24 = 720 : 24 + "
               "168 : 24 = 30 + 7."),

    Paraugs("672 : 32",
            uzd="Izrēķini 672 : 32.",
            soli=[
                ("672 = 640 + 32", "640 = 32 · 20."),
                ("640 : 32 = 20", None),
                ("32 : 32 = 1", None),
                ("20 + 1 = 21", "Pārbaude: 21 · 32 = 672."),
            ],
            atbilde="21"),

    Ievadi("Sadali un dali", [
        {"jaut": "575 : 25 = ?", "atb": ["23"], "padoms": "500 + 75."},
        {"jaut": "672 : 32 = ?", "atb": ["21"], "padoms": "640 + 32."},
        {"jaut": "455 : 35 = ?", "atb": ["13"], "padoms": "350 + 105."},
        {"jaut": "828 : 36 = ?", "atb": ["23"], "padoms": "720 + 108."},
        {"jaut": "990 : 45 = ?", "atb": ["22"], "padoms": "900 + 90."},
        {"jaut": "624 : 24 = ?", "atb": ["26"], "padoms": "480 + 144."},
    ], pamats=4),

    Varianti("Kurš sadalījums der?", [
        {"jaut": "Kā sadalīt 540, lai dalītu ar 45?",
         "opcijas": ["450 + 90", "500 + 40", "540 + 0", "300 + 240"],
         "pareizi": 0, "padoms": "450 = 45 · 10, 90 = 45 · 2."},
        {"jaut": "Cik ir 540 : 45?",
         "opcijas": ["12", "10", "14", "120"], "pareizi": 0,
         "padoms": "10 + 2."},
        {"jaut": "Kurš gabals *nedalās* ar 25?",
         "opcijas": ["130", "125", "250", "75"], "pareizi": 0,
         "padoms": "25 · 5 = 125, 25 · 6 = 150."},
    ]),

    Pasaule("Skolas ekskursijas autobusi",
            Ievadi("", [
                {"jaut": "Skolā 575 skolēni, autobusā 25 vietas. Cik "
                         "autobusu vajag?",
                 "atb": ["23"], "padoms": "575 : 25."},
                {"jaut": "Ekskursija maksā 672 € grupai no 32. Cik katram?",
                 "atb": ["21"], "padoms": "672 : 32."},
                {"jaut": "Pusdienas 455 € par 35 skolēniem. Cik katram?",
                 "atb": ["13"], "padoms": "350 + 105."},
                {"jaut": "Muzejs: 360 € par 24 skolēniem. Cik katram?",
                 "atb": ["15"], "padoms": "240 + 120."},
            ]),
            pavediens="skola",
            konteksts="Skolas pasākumu izmaksas sadala uz katru skolēnu - "
                      "dalāmais ir kopsumma.",
            kapec="Ar draudzīgiem gabaliem var dalīt bez stūrīša."),

    Kopsavilkums([
        "Izsaku dalāmo kā summu, kurā katrs gabals dalās.",
        "Dalu katru gabalu un saskaitu dalījumus.",
        "Pārbaudu ar reizināšanu.",
    ]),

    Majas([
        "Izrēķini 768 : 32 divos dažādos sadalījumos.",
        "Izrēķini, cik katram jāmaksā par klases pasākumu (izdomā summu).",
        "Paskaidro, kāpēc 575 : 25 var dalīt pa gabaliem.",
    ]),
]
