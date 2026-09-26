# -*- coding: utf-8 -*-
"""1. klase, 57. stunda: «Cik ir desmitu un cik vienu?»

Divciparu skaitlī pirmais cipars pasaka desmitus, otrais - vienus:
46 = 4 desmiti un 6 vieni = 40 + 6. To modelē ar stieņiem un kubiņiem.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, desmiti, restis)

TEMA = "Cik ir desmitu un cik vienu?"

MERKIS = ("Šodien noteiksim divciparu skaitļa sastāvu - cik desmitu un cik "
          "vienu - un modelēsim to.")

SATURS = [
    Sakums("46 - ko nozīmē 4 un ko 6?",
           zimejums=desmiti(4, 6),
           paraksts="4 desmiti un 6 vieni: 46 = 40 + 6.",
           fakti=["Pirmais cipars - desmiti.",
                  "Otrais cipars - vieni.",
                  "46 = 40 + 6."]),

    Doma("Cipara vieta",
         "Viens un tas pats cipars dažādās vietās nozīmē dažādu skaitu.",
         soli=[
             "Kreisais cipars - cik stieņu (desmitu).",
             "Labais cipars - cik atsevišķu kubiņu (vienu).",
             "Skaitli var uzrakstīt kā desmitu un vienu summu.",
         ],
         pieze="64 = 6 desmiti un 4 vieni - pavisam cits skaitlis."),

    Ievadi("Desmiti un vieni", [
        {"jaut": "Cik desmitu ir 46?", "zim": desmiti(4, 6), "atb": ["4"],
         "padoms": "Pirmais cipars."},
        {"jaut": "Cik vienu ir 73?", "atb": ["3"],
         "padoms": "Otrais cipars."},
        {"jaut": "5 desmiti un 2 vieni ir ...", "atb": ["52"],
         "padoms": "50 + 2."},
        {"jaut": "8 desmiti un 0 vienu ir ...", "atb": ["80"],
         "padoms": "Vienu nav - raksti 0."},
        {"jaut": "35 = 30 + ?", "atb": ["5"], "padoms": "Vieni."},
        {"jaut": "? = 60 + 9", "atb": ["69"], "padoms": "6 desmiti, 9 vieni."},
    ], pamats=4),

    Varianti("Kurš skaitlis?", [
        {"jaut": "Kurš skaitlis zīmējumā?", "zim": desmiti(2, 7),
         "opcijas": ["27", "72", "9"], "pareizi": 0,
         "padoms": "2 stieņi, 7 kubiņi."},
        {"jaut": "Kurā skaitlī ir 7 desmiti?",
         "opcijas": ["71", "17", "7"], "pareizi": 0,
         "padoms": "7 pirmajā vietā."},
        {"jaut": "Kas ir vairāk: 3 desmiti vai 9 vieni?",
         "opcijas": ["3 desmiti", "9 vieni"], "jaukt": False, "pareizi": 0,
         "padoms": "30 un 9."},
    ]),

    Pasaule("Monētas krājkasītē",
            Ievadi("", [
                {"jaut": "Krājkasītē 3 monētas pa 10 centiem un 5 pa 1 centam. "
                         "Cik centu?", "atb": ["35"], "padoms": "30 + 5."},
                {"jaut": "Tabulā: desmiti 6, vieni 4. Cik centu?",
                 "zim": restis([["desmiti", "vieni"], [6, 4]]),
                 "atb": ["64"], "padoms": "60 + 4."},
            ]),
            pavediens="veikals",
            konteksts="10 centu monēta ir kā desmits, 1 centa - kā viens.",
            kapec="Nauda arī sastāv no desmitiem un vieniem."),

    Kopsavilkums([
        "Nosaku, cik divciparu skaitlī ir desmitu un vienu.",
        "Modelēju skaitli ar stieņiem un kubiņiem.",
        "Rakstu skaitli kā summu: 46 = 40 + 6.",
    ]),

    Majas([
        "Uzraksti savu mājas numuru kā desmitus un vienus.",
        "Ar kociņiem izveido 32 un 23. Kāda atšķirība?",
        "Izdomā skaitli ar 5 desmitiem.",
    ]),
]
