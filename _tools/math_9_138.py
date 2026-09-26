# -*- coding: utf-8 -*-
"""9. klase, 138. stunda: «Kā progresija apraksta uzkrājumu?»

Regulārs pieaugums vai samazinājums: krājkasīte, kurā katru nedēļu liek
par 1 € vairāk, treniņu plāns ar pieaugošu distanci, kredīta atmaksa ar
dilstošiem procentiem. Viena virkne - a_n (šī nedēļa), otra - S_n (kopā).
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Kustiba, Majas, Pasaule,
                         Sakums, Varianti, restis)

TEMA = "Kā progresija apraksta uzkrājumu?"

MERKIS = ("Risināsim praktisku uzdevumu par regulāru pieaugumu vai "
          "samazinājumu.")

SATURS = [
    Sakums("52 nedēļu izaicinājums",
           zimejums=restis([["nedēļa", "1", "2", "3", "…", "52"],
                            ["iemaksa, €", "1", "2", "3", "…", "52"],
                            ["kopā, €", "1", "3", "6", "…", None]]),
           paraksts="Katru nedēļu par 1 € vairāk - cik gada beigās?",
           fakti=["Iemaksa - a_n = n.",
                  "Kopsumma - S_n = {n(n + 1)|2}.",
                  "S_{52} = 1378 € - no 1 € nedēļā sākuma!"]),

    Doma("a_n vai S_n?",
         "Jautājums «cik šonedēļ?» - loceklis a_n; «cik kopā?» - summa S_n.",
         soli=[
             "Nosaki a_1 un d no situācijas.",
             "«n-tajā reizē» → a_n = a_1 + (n − 1)d.",
             "«Kopā n reizēs» → S_n = {(a_1 + a_n)n|2}.",
             "Pārbaudi mērvienības un to, vai n ir vesels.",
         ]),

    Ievadi("Aprēķini", [
        {"jaut": "Treniņš: 1. dienā 2 km, katru dienu +0,5 km. 10. dienā km?",
         "atb": ["6,5"], "padoms": "2 + 9 · 0,5."},
        {"jaut": "Cik km kopā 10 dienās?", "atb": ["42,5"],
         "padoms": "{(2 + 6,5) · 10|2}."},
        {"jaut": "Krājkasīte: 5 €, tad katru mēnesi par 2 € vairāk. Cik "
                 "€ 12. mēnesī?", "atb": ["27"], "padoms": "5 + 22."},
        {"jaut": "Cik kopā 12 mēnešos?", "atb": ["192"],
         "padoms": "{(5 + 27) · 12|2}."},
    ]),

    Varianti("Loceklis vai summa?", [
        {"jaut": "«Cik lappušu Anna izlasīs 7. dienā?»",
         "opcijas": ["a_7", "S_7", "d", "a_1"],
         "pareizi": 0, "padoms": "Vienā dienā."},
        {"jaut": "«Cik lappušu kopā nedēļā?»",
         "opcijas": ["S_7", "a_7", "7d", "a_1 + d"],
         "pareizi": 0, "padoms": "Kopā."},
    ]),

    Pasaule("Kredīta atmaksa",
            Kustiba("", [
                {"jaut": "Aizņēmums atmaksāts ar maksājumiem: 1. mēnesī 120 €, "
                         "katru nākamo par 5 € mazāk (procenti sarūk). Cik € "
                         "maksā 10. mēnesī?",
                 "atb": 75, "beigas": 150, "iedala": 25, "mers": "€",
                 "merkis": "10. mēnesis", "objekts": "Maksājums",
                 "padoms": "120 − 45."},
                {"jaut": "Cik € kopā samaksāts 10 mēnešos?",
                 "atb": 975, "beigas": 1200, "iedala": 200, "mers": "€",
                 "merkis": "kopā", "objekts": "Summa",
                 "padoms": "{(120 + 75) · 10|2}."},
            ]),
            pavediens="veikals",
            konteksts="Bankas dilstošo maksājumu grafiks ir dilstoša "
                      "aritmētiskā progresija.",
            kapec="Progresija parāda gan katru maksājumu, gan kopsummu."),

    Kopsavilkums([
        "Modelēju regulāru pieaugumu ar progresiju.",
        "Izvēlos a_n vai S_n pēc jautājuma.",
        "Aprēķinu uzkrājumu un atmaksu.",
    ]),

    Majas([
        "Izplāno savu «52 nedēļu» izaicinājumu ar 0,50 € soli.",
        "Cik km noskries, ja sāk ar 1 km un katru nedēļu pieliek 0,5 km "
        "(10 nedēļas, 3 reizes nedēļā)?",
        "Pajautā vecākiem par kādu regulāru maksājumu.",
    ]),
]
