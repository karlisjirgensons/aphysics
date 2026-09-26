# -*- coding: utf-8 -*-
"""4. klase, 31. stunda: «Kā dalīt bez pārejas citā šķirā?»

Pilnus desmitus dala kā viencipara skaitļus (80 : 4 = 8 desmiti : 4 =
2 desmiti), un divciparu skaitli bez pārejas - pa šķirām. Katru dalījumu
pārbauda ar reizināšanu: tas kļūst par ieradumu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, restis)

TEMA = "Kā dalīt bez pārejas citā šķirā?"

MERKIS = ("Dalīsim pilnus desmitus un divciparu skaitli bez pārejas un "
          "pārbaudīsim ar reizināšanu.")

SATURS = [
    Sakums("Cik maksā viena biļete, ja trīs maksā 90 €?",
           zimejums=restis([["90 : 3", "9 desmiti : 3", "3 desmiti", "30"]],
                           "pilnus desmitus dala kā mazus skaitļus"),
           paraksts="9 : 3 = 3, tātad 90 : 3 = 30.",
           fakti=["Pilnu desmitu dalīšana ir tabulas dalīšana.",
                  "Pārbaude: 30 · 3 = 90."]),

    Doma("Dali katru šķiru un pārbaudi ar reizināšanu",
         "Ja katra šķira dalās bez atlikuma, dalījumu raksta pa šķirām; "
         "pārbaudē dalījumu reizina ar dalītāju.",
         soli=[
             "Pilnie desmiti: 80 : 4 = 8 desmiti : 4 = 2 desmiti = 20.",
             "Divciparu skaitlis: 68 : 2 = 60 : 2 + 8 : 2 = 30 + 4 = 34.",
             "Pārbaude: 34 · 2 = 68 - sakrīt.",
         ],
         pieze="Ja pārbaudē nesakrīt, kļūda ir dalīšanā."),

    Paraugs("93 : 3 ar pārbaudi",
            uzd="Izrēķini 93 : 3 un pārbaudi.",
            soli=[
                ("90 : 3 = 30", None),
                ("3 : 3 = 1", None),
                ("30 + 1 = 31", "Dalījums."),
                ("31 · 3 = 93", "Pārbaude sakrīt."),
            ],
            atbilde="31"),

    Slidnis("Pilni desmiti",
            soli=[
                {"v": "8 : 4 = 2", "teksts": "Tabulā."},
                {"v": "80 : 4 = 20", "teksts": "Desmit reizes lielāks "
                 "dalāmais - desmit reizes lielāks dalījums."},
                {"v": "800 : 4 = 200", "teksts": "Un simtiem tāpat."},
            ],
            ievads="Viena tabulas rinda der visām šķirām."),

    Ievadi("Dali un pārbaudi", [
        {"jaut": "60 : 3 = ?", "atb": ["20"], "padoms": "6 desmiti : 3."},
        {"jaut": "80 : 2 = ?", "atb": ["40"], "padoms": "8 desmiti : 2."},
        {"jaut": "88 : 4 = ?", "atb": ["22"], "padoms": "80 : 4 + 8 : 4."},
        {"jaut": "77 : 7 = ?", "atb": ["11"], "padoms": "70 : 7 + 7 : 7."},
        {"jaut": "46 : 2 = ?", "atb": ["23"], "padoms": "40 : 2 + 6 : 2."},
        {"jaut": "99 : 3 = ?", "atb": ["33"], "padoms": "90 : 3 + 9 : 3."},
    ], pamats=4),

    Varianti("Kā pārbaudīt?", [
        {"jaut": "Kā pārbaudīt 84 : 4 = 21?",
         "opcijas": ["21 · 4 = 84", "84 · 4", "21 + 4", "84 − 21"],
         "pareizi": 0, "padoms": "Dalījums reiz dalītājs."},
        {"jaut": "Toms: 66 : 3 = 23. Pārbaude 23 · 3 = 69. Ko tas nozīmē?",
         "opcijas": ["Toms kļūdījās", "viss pareizi",
                     "pārbaude nestrādā"], "pareizi": 0,
         "padoms": "69 ≠ 66; pareizi 22."},
        {"jaut": "Cik ir 40 : 2?",
         "opcijas": ["20", "2", "80", "38"], "pareizi": 0,
         "padoms": "4 desmiti : 2."},
    ]),

    Pasaule("Klases ekskursijas budžets",
            Ievadi("", [
                {"jaut": "Autobuss uz Rundāli 90 € par 3 stundām. Cik maksā "
                         "viena stunda?",
                 "atb": ["30"], "padoms": "90 : 3."},
                {"jaut": "Pils ekskursija 86 € grupai; grupu dala 2 daļās. "
                         "Cik maksā viena daļa?",
                 "atb": ["43"], "padoms": "80 : 2 + 6 : 2."},
                {"jaut": "4 vecāki sadala 48 € pusdienu rēķinu. Cik katram?",
                 "atb": ["12"], "padoms": "40 : 4 + 8 : 4."},
                {"jaut": "Ieejas biļetes 3 skolotājiem maksāja 36 €. Cik "
                         "viena?",
                 "atb": ["12"], "padoms": "30 : 3 + 6 : 3."},
            ]),
            pavediens="celojums",
            konteksts="Braucot uz Rundāles pili, izmaksas dala starp "
                      "stundām, grupām un cilvēkiem.",
            kapec="Pārbaude ar reizināšanu garantē, ka nauda sadalīta "
                  "pareizi."),

    Kopsavilkums([
        "Dalu pilnus desmitus un simtus.",
        "Dalu divciparu skaitli bez pārejas pa šķirām.",
        "Pārbaudu dalījumu ar reizināšanu.",
    ]),

    Majas([
        "Izdomā 3 dalīšanas piemērus bez pārejas un pārbaudi tos.",
        "Izrēķini, cik maksā viens pusdienu komplekts, ja ģimenes 4 komplekti "
        "maksā 48 €.",
        "Paskaidro, kāpēc 800 : 4 = 200.",
    ]),
]
