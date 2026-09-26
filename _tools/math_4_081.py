# -*- coding: utf-8 -*-
"""4. klase, 81. stunda: «Kā dalīt galvā?»

Dalīšana ar divciparu skaitli sākas galvā - ar pilniem desmitiem
(240 : 60 = 24 : 6) un ar «cik reižu ietilpst» (96 : 12 = 8, jo
12 · 8 = 96). Katru dalījumu pārbauda ar reizināšanu, tāpat kā 4.2.
tematā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, restis)

TEMA = "Kā dalīt galvā?"

MERKIS = ("Dalīsim galvā divciparu un trīsciparu skaitļus ar divciparu "
          "skaitli un pārbaudīsim ar reizināšanu.")

SATURS = [
    Sakums("Cik olu kastīšu pa 12 sanāk no 96 olām?",
           zimejums=restis([["12 · 7", "84"],
                            ["12 · 8", "96"],
                            ["12 · 9", "108"]],
                           "meklē reizinājumu"),
           paraksts="12 · 8 = 96, tātad 96 : 12 = 8.",
           fakti=["Dalīšana ir jautājums: cik reižu ietilpst?",
                  "Atbildi meklē reizināšanas rindā."]),

    Doma("Dali, domājot par reizināšanu",
         "a : b ir skaitlis, kuru reizinot ar b, iegūst a; to atrod, "
         "izmēģinot reizinājumus, vai noņemot vienādas nulles.",
         soli=[
             "Pilni desmiti: 240 : 60 = 24 : 6 = 4 (abus dala ar 10).",
             "Cik reižu: 96 : 12 - meklē 12 · ? = 96.",
             "Izmēģini: 12 · 8 = 96 - atrasts.",
             "Pārbaudi: dalījums · dalītājs = dalāmais.",
         ],
         pieze="Noņemt vienādu nuļļu skaitu var tikai no abiem skaitļiem "
               "reizē: 3600 : 90 = 360 : 9 = 40."),

    Paraugs("135 : 15",
            uzd="Izrēķini 135 : 15 galvā.",
            soli=[
                ("15 · 10 = 150", "Par daudz."),
                ("15 · 9 = 135", "Tieši."),
                ("135 : 15 = 9", None),
            ],
            atbilde="9"),

    Slidnis("Nulles pazūd pa pāriem",
            soli=[
                {"v": "4800 : 60", "teksts": "Abiem ir nulles galā."},
                {"v": "480 : 6", "teksts": "Noņem vienu nulli abiem."},
                {"v": "80", "teksts": "480 : 6 = 80. Pārbaude: 80 · 60 = "
                 "4800."},
            ]),

    Ievadi("Galvā", [
        {"jaut": "96 : 12 = ?", "atb": ["8"], "padoms": "12 · 8."},
        {"jaut": "240 : 60 = ?", "atb": ["4"], "padoms": "24 : 6."},
        {"jaut": "135 : 15 = ?", "atb": ["9"], "padoms": "15 · 9."},
        {"jaut": "3600 : 90 = ?", "atb": ["40"], "padoms": "360 : 9."},
        {"jaut": "144 : 12 = ?", "atb": ["12"], "padoms": "12 · 12."},
        {"jaut": "175 : 25 = ?", "atb": ["7"], "padoms": "25 · 7."},
        {"jaut": "560 : 70 = ?", "atb": ["8"], "padoms": "56 : 7."},
        {"jaut": "300 : 25 = ?", "atb": ["12"], "padoms": "Četri 25 ir 100."},
    ], pamats=6),

    Varianti("Kā pārbaudīt?", [
        {"jaut": "Kā pārbaudīt 168 : 14 = 12?",
         "opcijas": ["12 · 14 = 168", "168 · 14", "168 − 14 = 12",
                     "14 + 12"], "pareizi": 0,
         "padoms": "Dalījums · dalītājs."},
        {"jaut": "Toms: 6300 : 70 = 9. Kas nav kārtībā?",
         "opcijas": ["pazaudēja nulli, pareizi 90", "viss pareizi",
                     "jābūt 900"], "pareizi": 0,
         "padoms": "630 : 7 = 90."},
        {"jaut": "Kurš dalījums ir 5?",
         "opcijas": ["75 : 15", "75 : 25", "60 : 15", "90 : 15"],
         "pareizi": 0, "padoms": "15 · 5 = 75."},
    ]),

    Pasaule("Piegādes dienests",
            Ievadi("", [
                {"jaut": "Kurjeram 96 pakas, mašīnā vienā reisā 12. Cik "
                         "reisu?",
                 "atb": ["8"], "padoms": "96 : 12."},
                {"jaut": "Dienā 480 km, stundā 60 km. Cik stundu?",
                 "atb": ["8"], "padoms": "48 : 6."},
                {"jaut": "Noliktavā 900 kastes, paletē 45. Cik palešu?",
                 "atb": ["20"], "padoms": "45 · 20 = 900."},
                {"jaut": "Degviela 240 € mēnesī, 30 dienas. Cik € dienā?",
                 "atb": ["8"], "padoms": "24 : 3."},
            ]),
            pavediens="tehnika",
            konteksts="Kurjeri un noliktavas katru dienu dala lielus "
                      "daudzumus vienādās kravās.",
            kapec="Galvas dalīšana ļauj plānot, pirms kalkulators ieslēgts."),

    Kopsavilkums([
        "Dalu galvā ar divciparu skaitli, meklējot reizinājumu.",
        "Noņemu vienādas nulles no dalāmā un dalītāja.",
        "Pārbaudu dalījumu ar reizināšanu.",
    ]),

    Majas([
        "Izrēķini, cik pilnu stundu ir 480 minūtēs.",
        "Izrēķini, cik nedēļu ir 84 dienās.",
        "Izdomā 3 dalīšanas piemērus, kurus var noņemot nulles.",
    ]),
]
