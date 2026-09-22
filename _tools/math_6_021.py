# -*- coding: utf-8 -*-
"""6. klase, 21. stunda: «Cik reižu daļa ietilpst veselajā?»

Pirmā dalīšana *ar* daļu, bet vēl bez algoritma: atbildi te var saskaitīt.
Tieši tāpēc šī stunda ir pirms apgrieztā skaitļa - kad vēlāk parādīsies
formula, būs ar ko to salīdzināt.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Kustiba, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, taisne)

TEMA = "Cik reižu daļa ietilpst veselajā?"

MERKIS = ("Mācīsimies dalīt veselu skaitli ar pamatdaļu un vārdiem "
          "raksturot, ko rezultāts nozīmē.")

SATURS = [
    Sakums("Cik pusstundu ir dienā?",
           zimejums=taisne(0, 3, 1, [(0.5, "1/2"), (1.5, "3/2"),
                                     (2.5, "5/2")]),
           paraksts="Trīs veselos ietilpst sešas pusītes: 3 : {1|2} = 6.",
           fakti=["Dalīšana ar daļu jautā: cik reižu tā ietilpst?",
                  "Diennaktī ir 48 pusstundas - tā ir dalīšana ar {1|2}.",
                  "Rezultāts ir lielāks par dalāmo, un tas ir normāli."]),

    Doma("Dalīt ar daļu nozīmē skaitīt, cik tādu ietilpst",
         "Veselu skaitli dalot ar pamatdaļu {1|n}, rezultāts ir šis skaitlis, "
         "reizināts ar n - jo katrā veselajā ietilpst n tādas daļas.",
         soli=[
             "Pārformulē uzdevumu: cik reižu daļa ietilpst?",
             "Noskaidro, cik tādu daļu ir vienā veselajā - to pasaka saucējs.",
             "Reizini veselo skaitli ar saucēju.",
             "Pārbaudi ar reizināšanu: rezultāts reiz daļa dod dalāmo.",
         ],
         pieze="4 : {1|3} = 12, jo katrā veselajā ir trīs trešdaļas. Atbilde "
               "ir lielāka par 4 - un tieši tāpēc dalīšana ar daļu sākumā "
               "šķiet dīvaina."),

    Paraugs("Cik ceturtdaļas ir piecos veselos?",
            uzd="Dēlis ir 5 m garš. Cik {1|4} m garu gabalu no tā var "
                "izzāģēt?",
            soli=[
                ("5 : {1|4}",
                 "Jautājums: cik reižu {1|4} ietilpst piecos."),
                ("Vienā metrā ir 4 ceturtdaļas",
                 "To pasaka saucējs."),
                ("5 · 4 = 20",
                 "Piecos metros - piecas reizes vairāk."),
                ("Pārbaude: 20 · {1|4} = {20|4} = 5",
                 "Reizinājums atgriež sākotnējo garumu."),
            ],
            atbilde="20 gabalu"),

    Ievadi("Cik reižu ietilpst?", [
        {"jaut": "Cik ir 3 : {1|2}?",
         "atb": ["6"], "padoms": "Katrā veselajā divas pusītes."},
        {"jaut": "Cik ir 4 : {1|5}?",
         "atb": ["20"], "padoms": "4 · 5."},
        {"jaut": "Cik ir 7 : {1|3}?",
         "atb": ["21"], "padoms": "7 · 3."},
        {"jaut": "Cik ir 2 : {1|10}?",
         "atb": ["20"], "padoms": "2 · 10."},
        {"jaut": "Cik {1|8} daļu ir 3 veselos?",
         "atb": ["24"], "padoms": "3 · 8."},
        {"jaut": "Cik ir 1 : {1|6}?",
         "atb": ["6"], "padoms": "Vienā veselajā ir sešas sestdaļas."},
    ], pamats=4,
        ievads="Saucējs pasaka, cik daļu ietilpst vienā veselajā."),

    Pasaule("Cik gabalu sanāks?",
            Kustiba("", [
                {"jaut": "6 m garu lenti griež {1|2} m gabalos. Cik gabalu "
                         "sanāks?",
                 "atb": 12, "beigas": 40, "iedala": 10, "mers": "gabali",
                 "merkis": "gabalu skaits", "objekts": "Griezējs",
                 "padoms": "6 · 2."},
                {"jaut": "Tā pati lente, gabali pa {1|4} m. Cik gabalu?",
                 "atb": 24, "beigas": 40, "iedala": 10, "mers": "gabali",
                 "merkis": "gabalu skaits", "objekts": "Griezējs",
                 "padoms": "6 · 4."},
                {"jaut": "5 m lenti griež {1|5} m gabalos. Cik gabalu?",
                 "atb": 25, "beigas": 40, "iedala": 10, "mers": "gabali",
                 "merkis": "gabalu skaits", "objekts": "Griezējs",
                 "padoms": "5 · 5."},
                {"jaut": "3 m lenti griež {1|10} m gabalos. Cik gabalu?",
                 "atb": 30, "beigas": 40, "iedala": 10, "mers": "gabali",
                 "merkis": "gabalu skaits", "objekts": "Griezējs",
                 "padoms": "3 · 10."},
            ]),
            pavediens="maja",
            konteksts="Griezējs apstājas pie tā skaitļa, cik gabalu tu "
                      "aprēķināji - un tad redzams, vai tas ir ticams.",
            kapec="Jo sīkāki gabali, jo vairāk to sanāk."),

    Varianti("Kāpēc rezultāts ir lielāks?", [
        {"jaut": "6 : {1|3} = 18. Kāpēc atbilde ir lielāka par 6?",
         "opcijas": ["Jo sīkas daļas ietilpst daudz reižu",
                     "Jo dalīšana vienmēr palielina",
                     "Jo 6 ir pāra skaitlis",
                     "Atbilde ir nepareiza"],
         "pareizi": 0,
         "padoms": "Trešdaļa ir mazāka par vienu, tāpēc tādu ietilpst daudz."},
        {"jaut": "Ar ko dalot, rezultāts sanāk 10 reižu lielāks?",
         "opcijas": ["Ar {1|10}", "Ar 10", "Ar {10|1}", "Ar {1|5}"],
         "pareizi": 0,
         "padoms": "Saucējs pasaka reizinātāju."},
        {"jaut": "Ko nozīmē 8 : {1|2} vārdiem?",
         "opcijas": ["Cik pusīšu ietilpst astoņos",
                     "Cik ir puse no astoņiem",
                     "Astoņi, sadalīti uz pusēm",
                     "Astoņi reiz puse"],
         "pareizi": 0,
         "padoms": "Dalīšana jautā par ietilpšanu."},
        {"jaut": "Cik ir 10 : {1|1}?",
         "opcijas": ["10", "1", "100", "0"],
         "pareizi": 0,
         "padoms": "{1|1} ir viens."},
    ], pamats=4),

    Zimejums("Astotdaļas divos veselos",
             taisne(0, 2, 1, [(0.125, "1/8"), (1.0, "8/8"), (2.0, "16/8")]),
             paskaidro="Vienā veselajā ir 8 astotdaļas, divos - 16. Tāpēc "
                       "2 : {1|8} = 16.",
             ievads="Skaitļu taisne pati saskaita, cik daļu ietilpst."),

    Kopsavilkums([
        "Saprotu, ka dalīšana ar daļu jautā «cik reižu ietilpst».",
        "Dalu veselu skaitli ar pamatdaļu, reizinot to ar saucēju.",
        "Paskaidroju, kāpēc rezultāts ir lielāks par dalāmo.",
        "Pārbaudu dalījumu ar reizināšanu.",
    ]),

    Majas([
        "Izrēķini, cik {1|4} stundas ietilpst 3 stundās.",
        "Atrodi mājās trauku un izdomā, cik {1|2} glāžu tajā ietilpst.",
        "Uzraksti vārdiem, ko nozīmē 5 : {1|6}.",
    ]),
]
