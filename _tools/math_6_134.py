# -*- coding: utf-8 -*-
"""6. klase, 134. stunda: «Kurš skaitlis trūkst?»

Apgrieztais uzdevums: zināms rezultāts, meklē vienu no locekļiem. Tas ir
pirmais solis uz vienādojumiem, un te to risina ar skaitļu taisni un ar
pārbaudi, nevis ar pārnešanu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Kustiba, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, taisne)

TEMA = "Kurš skaitlis trūkst?"

MERKIS = ("Noteiksim nezināmo darbības locekli un pierakstīsim aprēķinu.")

SATURS = [
    Sakums("Zināms gals, meklē soli",
           zimejums=taisne(-8, 4, 2, [(-6, "sākums"), (1, "beigas")],
                           bultas=[(-6, 1, "?")]),
           paraksts="No −6 nonācām pie 1. Cik liels bija solis? "
                    "1 − (−6) = 7.",
           fakti=["Trūkstošo saskaitāmo atrod, no summas atņemot zināmo.",
                  "Trūkstošo mazināmo atrod, starpībai pieskaitot "
                  "mazinātāju.",
                  "Katru atbildi pārbauda, ievietojot to izteiksmē."]),

    Doma("Ej pretējā virzienā",
         "Nezināmo locekli atrod ar pretējo darbību: saskaitīšanai - "
         "atņemšana, atņemšanai - saskaitīšana.",
         soli=[
             "Pieraksti izteiksmi ar nezināmo.",
             "Nosaki, kurš loceklis trūkst.",
             "Veic pretējo darbību.",
             "Izrēķini nezināmo.",
             "Pārbaudi, ievietojot to sākotnējā izteiksmē.",
         ],
         pieze="Ja nezināmais ir mazinātājs, pretējā darbība nav tik "
               "acīmredzama: no 5 − x = 8 seko x = 5 − 8 = −3. Tāpēc "
               "pārbaude te ir obligāta."),

    Paraugs("Atrodi trūkstošo",
            uzd="−6 + x = 1. Kāds ir x?",
            soli=[
                ("Nezināmais ir saskaitāmais",
                 "Pretējā darbība ir atņemšana."),
                ("x = 1 − (−6)",
                 "No summas atņem zināmo."),
                ("= 1 + 6 = 7",
                 "Atņemt negatīvu nozīmē pieskaitīt."),
                ("Pārbaude: −6 + 7 = 1",
                 "Sakrīt ar doto."),
            ],
            atbilde="x = 7"),

    Ievadi("Atrodi nezināmo", [
        {"jaut": "−6 + x = 1. Kāds ir x?",
         "atb": ["7"], "padoms": "1 − (−6)."},
        {"jaut": "x + 5 = −3. Kāds ir x?",
         "atb": ["-8", "−8"], "padoms": "−3 − 5."},
        {"jaut": "x − 4 = −9. Kāds ir x?",
         "atb": ["-5", "−5"], "padoms": "−9 + 4."},
        {"jaut": "5 − x = 8. Kāds ir x?",
         "atb": ["-3", "−3"], "padoms": "5 − 8."},
        {"jaut": "−2 − x = 3. Kāds ir x?",
         "atb": ["-5", "−5"], "padoms": "−2 − 3."},
        {"jaut": "x + (−7) = 0. Kāds ir x?",
         "atb": ["7"], "padoms": "Pretējais skaitlis."},
    ], pamats=4,
        ievads="Pēc katras atbildes pārbaudi to izteiksmē."),

    Pasaule("Cik liels bija solis?",
            Kustiba("", [
                {"jaut": "Lifts no −6 stāva nonāca 1. stāvā. Par cik "
                         "stāviem tas pacēlās?",
                 "atb": 7, "beigas": 20, "iedala": 5, "mers": "stāvi",
                 "merkis": "solis", "objekts": "Lifts",
                 "padoms": "1 − (−6)."},
                {"jaut": "No 3. stāva tas nonāca −5 stāvā. Par cik stāviem "
                         "tas nolaidās?",
                 "atb": 8, "beigas": 20, "iedala": 5, "mers": "stāvi",
                 "merkis": "solis", "objekts": "Lifts",
                 "padoms": "3 + 5."},
                {"jaut": "No −8 stāva tas nonāca −2 stāvā. Par cik stāviem "
                         "tas pacēlās?",
                 "atb": 6, "beigas": 20, "iedala": 5, "mers": "stāvi",
                 "merkis": "solis", "objekts": "Lifts",
                 "padoms": "−2 − (−8)."},
                {"jaut": "No −4 stāva tas nonāca 9. stāvā. Par cik stāviem?",
                 "atb": 13, "beigas": 20, "iedala": 5, "mers": "stāvi",
                 "merkis": "solis", "objekts": "Lifts",
                 "padoms": "9 + 4."},
            ]),
            pavediens="maja",
            konteksts="Ja zināms sākuma un gala stāvs, brauciena garumu var "
                      "izrēķināt - tā ir attālums starp skaitļiem.",
            kapec="Trūkstošais loceklis ir pretējās darbības rezultāts."),

    Varianti("Kura darbība te der?", [
        {"jaut": "x + 5 = −3. Lai atrastu x, jā...",
         "opcijas": ["atņem 5 no −3", "pieskaita 5 pie −3",
                     "reizina", "dala"],
         "pareizi": 0,
         "padoms": "Pretējā darbība."},
        {"jaut": "x − 4 = −9. Lai atrastu x, jā...",
         "opcijas": ["pieskaita 4 pie −9", "atņem 4 no −9",
                     "reizina", "dala"],
         "pareizi": 0,
         "padoms": "Pretējā darbība atņemšanai."},
        {"jaut": "5 − x = 8. Kāds ir x?",
         "opcijas": ["−3", "3", "13", "−13"],
         "pareizi": 0,
         "padoms": "Pārbaudi: 5 − (−3) = 8."},
        {"jaut": "Kāpēc pārbaude te ir obligāta?",
         "opcijas": ["Jo nezināmais mēdz būt mazinātājs",
                     "Jo skaitļi ir lieli",
                     "Jo tā prasa skolotājs", "Nav obligāta"],
         "pareizi": 0,
         "padoms": "Tur pretējā darbība nav acīmredzama."},
    ], pamats=4),

    Kopsavilkums([
        "Nosaku nezināmo darbības locekli.",
        "Lietoju pretējo darbību.",
        "Pierakstu aprēķinu pa soļiem.",
        "Pārbaudu atbildi, ievietojot to izteiksmē.",
    ]),

    Majas([
        "Atrodi x: x − 7 = −2; −4 + x = −9; 3 − x = 10.",
        "Katram pieraksti pārbaudi.",
        "Izdomā uzdevumu, kurā nezināmais ir mazinātājs.",
    ]),
]
