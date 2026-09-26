# -*- coding: utf-8 -*-
"""2. klase, 159. stunda: «Cik veikli dali?»

Mikrotemata noslēgums: patstāvīgi dala skaitļus līdz 50 ar 2, 3, 4 un 5,
pārbaudot ar reizināšanu. Jaukti piemēri un dzīves uzdevumi.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Kustiba, Majas,
                         Pasaule, Sakums, Varianti)

TEMA = "Cik veikli dali?"

MERKIS = ("Šodien patstāvīgi dalīsim skaitļus līdz 50 ar 2, 3, 4 un 5 un "
          "pārbaudīsim rezultātu.")

SATURS = [
    Sakums("Vai vari dalīt tikpat ātri kā reizināt?",
           fakti=["Katram dalījumam ir palīgreizinājums.",
                  "40 : 5 = 8, jo 5 · 8 = 40.",
                  "Šodien trenējamies patstāvīgi."]),

    Doma("Mans plāns",
         "Dalījums - palīgreizinājums - pārbaude.",
         soli=[
             "Izlasi: 32 : 4.",
             "Pajautā: 4 · ? = 32.",
             "Atbilde: 8.",
             "Pārbaude: 8 · 4 = 32.",
         ]),

    Ievadi("Treniņš", [
        {"jaut": "32 : 4 = ?", "atb": ["8"], "padoms": "4 · 8."},
        {"jaut": "45 : 5 = ?", "atb": ["9"], "padoms": "5 · 9."},
        {"jaut": "18 : 2 = ?", "atb": ["9"], "padoms": "2 · 9."},
        {"jaut": "21 : 3 = ?", "atb": ["7"], "padoms": "3 · 7."},
        {"jaut": "28 : 4 = ?", "atb": ["7"], "padoms": "4 · 7."},
        {"jaut": "35 : 5 = ?", "atb": ["7"], "padoms": "5 · 7."},
        {"jaut": "24 : 3 = ?", "atb": ["8"], "padoms": "3 · 8."},
        {"jaut": "40 : 4 = ?", "atb": ["10"], "padoms": "4 · 10."},
    ], pamats=6),

    Kustiba("Robots dala ceļu", [
        {"jaut": "Ceļš 40 m, robots veic to 5 vienādos gājienos. Cik m "
                 "vienā gājienā?", "atb": 8, "beigas": 10, "iedala": 1,
         "mers": "m", "objekts": "robots", "merkis": "40 : 5",
         "padoms": "5 · 8 = 40."},
        {"jaut": "Ceļš 27 m, 3 vienādi gājieni. Cik m vienā?", "atb": 9,
         "beigas": 10, "iedala": 1, "mers": "m", "objekts": "robots",
         "merkis": "27 : 3", "padoms": "3 · 9 = 27."},
    ]),

    Varianti("Kurš dalījums lielāks?", [
        {"jaut": "20 : 4 vai 20 : 5?", "opcijas": ["20 : 4 = 5",
                                                    "20 : 5 = 4"],
         "jaukt": False, "pareizi": 0,
         "padoms": "Mazāk daļu - lielāka katra."},
        {"jaut": "Kurš dalījums ir 6?", "opcijas": ["24 : 4", "24 : 3",
                                                    "24 : 2"],
         "pareizi": 0, "padoms": "4 · 6 = 24."},
    ]),

    Pasaule("Maizes klaipi",
            Ievadi("", [
                {"jaut": "Maiznīca izcepa 45 klaipus. Tos liek kastēs pa 5. "
                         "Cik kastu?", "atb": ["9"], "padoms": "45 : 5."},
                {"jaut": "Kastes aizved uz 3 veikaliem vienādi. Cik kastu "
                         "katram?", "atb": ["3"], "padoms": "9 : 3."},
            ]),
            pavediens="virtuve",
            konteksts="No rīta maiznīca sadala maizi veikaliem.",
            kapec="Divas dalīšanas - un katrs veikals zina, cik saņems."),

    Kopsavilkums([
        "Patstāvīgi dalu ar 2, 3, 4 un 5.",
        "Izmantoju palīgreizinājumu.",
        "Pārbaudu katru dalījumu.",
    ]),

    Majas([
        "Atrisini 6 dalījumus no uzdevumu krājuma.",
        "Katram uzraksti pārbaudi.",
        "Atzīmē, kuri bija grūti.",
    ]),
]
