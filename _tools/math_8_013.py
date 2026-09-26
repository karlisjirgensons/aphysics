# -*- coding: utf-8 -*-
"""8. klase, 13. stunda: «Ko dati patiesībā rāda?»

Secinājums drīkst apgalvot tikai to, ko dati parāda. Galvenā lamatas:
«kopā mainās» nenozīmē «viens izraisa otru». Punktu diagramma plaknē rāda
sakarību; stunda māca to aprakstīt godīgi.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, Zimejums, plakne)

TEMA = "Ko dati patiesībā rāda?"

MERKIS = ("Analizēsim datus ar statistiskajiem rādītājiem un formulēsim "
          "pamatotus secinājumus.")

# Temperatūra (°C) un nopirkto saldējumu skaits kioskā dienā.
_SALDEJUMS = [(14, 40), (16, 55), (18, 60), (20, 80), (22, 90), (24, 110),
              (26, 120), (28, 140)]

SATURS = [
    Sakums("Saldējums un peldētāji",
           zimejums=plakne(punkti=_SALDEJUMS, no_x=12, lidz_x=30, no_y=0,
                           lidz_y=150, solis=2, solis_y=30, x_nos="°C",
                           y_nos="gab."),
           paraksts="Jo siltāks, jo vairāk saldējuma - un vairāk peldētāju.",
           fakti=["Saldējums un peldētāji aug kopā.",
                  "Bet saldējums peldētājus neizraisa.",
                  "Abus izraisa trešais - karstums."]),

    Doma("Godīgs secinājums",
         "Secinājums atbild uz pētījuma jautājumu ar skaitļiem un nesaka "
         "vairāk, nekā dati rāda.",
         soli=[
             "Sāc ar skaitļiem: «Vidēji ..., mediāna ..., amplitūda ...».",
             "Atbildi uz jautājumu: jā, nē vai daļēji.",
             "Ja divi lielumi mainās kopā, saki «ir saistīti», nevis "
             "«izraisa».",
             "Nosauc ierobežojumus: izlases lielums, kā savākti dati.",
         ],
         pieze="Zinātnē cēloni pārbauda ar eksperimentu: maina vienu "
               "lielumu un pārējos notur nemainīgus."),

    Zimejums("Sakarības veidi",
             plakne(punkti=[(1, 2), (2, 3), (3, 3.5), (4, 5), (5, 5.5),
                            (6, 7)],
                    grafiki=[([(1, 6), (6, 1.5)], "pretēji")],
                    no_x=0, lidz_x=7, no_y=0, lidz_y=8, solis=1),
             paskaidro="Punkti iet uz augšu - lielumi aug kopā. Līnija uz leju "
                       "- viens aug, otrs samazinās."),

    Ievadi("Lasi punktu diagrammu", [
        {"jaut": "Saldējuma diagrammā: cik saldējumu pārdeva 20 °C?",
         "atb": ["80"], "padoms": "Punkts pie 20."},
        {"jaut": "Par cik gabaliem vairāk pārdeva 28 °C nekā 14 °C?",
         "atb": ["100"], "padoms": "140 − 40."},
        {"jaut": "Aptuveni par cik gabaliem pieaug pārdošana uz katriem "
                 "2 °C?",
         "atb": ["14", "15"], "padoms": "100 : 7 ≈ 14."},
        {"jaut": "Visu 8 dienu vidējais pārdoto saldējumu skaits?",
         "atb": ["86,875", "86.875", "87"], "padoms": "695 : 8."},
    ]),

    Varianti("Vai secinājums ir pamatots?", [
        {"jaut": "Skolēni, kas vairāk lasa, saņem augstākas atzīmes. "
                 "Secinājums «lasīšana paaugstina atzīmes»...",
         "opcijas": ["nav pierādīts - var būt citi iemesli",
                     "ir pierādīts", "ir nepareizs pilnīgi",
                     "ir pierādīts tikai zēniem"],
         "pareizi": 0, "padoms": "Saistība nav cēlonis."},
        {"jaut": "Aptaujāja 6 skolēnus; 4 patīk matemātika. Secinājums "
                 "«67 % skolēnu patīk matemātika»...",
         "opcijas": ["ir nedrošs - izlase par mazu", "ir drošs",
                     "ir aprēķināts nepareizi", "der visai Latvijai"],
         "pareizi": 0, "padoms": "6 cilvēki nav skola."},
        {"jaut": "Kurš secinājums ir labākais?",
         "opcijas": ["Mediānais miegs 7,2 h - zem normas 8 h (izlase 40)",
                     "Skolēni guļ par maz",
                     "Miegs ir ļoti svarīgs",
                     "Visi skolēni guļ 7,2 h"],
         "pareizi": 0, "padoms": "Skaitļi, norma un izlase."},
    ]),

    Pasaule("Saldējuma kiosks plāno",
            Ievadi("", [
                {"jaut": "Laika prognoze - 24 °C. Cik saldējumu būs "
                         "vajadzīgi pēc datiem?",
                 "atb": ["110"], "padoms": "Punkts pie 24."},
                {"jaut": "Kiosks pasūta par 10 % vairāk nekā paredzēts. Cik "
                         "gabalu?",
                 "atb": ["121"], "padoms": "110 · 1,1."},
                {"jaut": "Viens saldējums nes 0,40 € peļņas. Cik eiro nes "
                         "110 saldējumi?",
                 "atb": ["44"], "padoms": "110 · 0,4."},
            ]),
            pavediens="planeta",
            konteksts="Tirgotāji plāno krājumus pēc laika prognozes - dati "
                      "rāda, ka pārdošana ir saistīta ar temperatūru.",
            kapec="Sakarība ļauj prognozēt, pat ja nav zināms cēlonis."),

    Kopsavilkums([
        "Formulēju secinājumu ar skaitļiem.",
        "Atšķiru «ir saistīti» no «izraisa».",
        "Nosaucu pētījuma ierobežojumus.",
    ]),

    Majas([
        "Aprēķini sava pētījuma datiem vidējo, mediānu, modu un amplitūdu.",
        "Uzraksti 3 teikumu secinājumu ar skaitļiem.",
        "Uzraksti vienu sava pētījuma ierobežojumu.",
    ]),
]
