# -*- coding: utf-8 -*-
"""1. klase, 145. stunda: «Kā saskaitīt pilnus desmitus?»

30 + 40: 3 desmiti un 4 desmiti ir 7 desmiti = 70 - tāpat kā 3 + 4 = 7.
Atņem tāpat: 80 − 50 = 30.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, desmiti)

TEMA = "Kā saskaitīt pilnus desmitus?"

MERKIS = ("Šodien saskaitīsim un atņemsim pilnus desmitus 100 apjomā, "
          "saskatot līdzību ar vieniem.")

SATURS = [
    Sakums("30 + 40 - cik desmitu?",
           zimejums=desmiti(7, 0),
           paraksts="3 desmiti + 4 desmiti = 7 desmiti = 70.",
           fakti=["Desmitus skaita kā vienus.",
                  "3 + 4 = 7, tātad 30 + 40 = 70.",
                  "Atņem tāpat: 80 − 50 = 30."]),

    Slidnis("Tāpat kā vieni", [
        {"v": "3 + 4 = 7", "teksts": "Vieni", "zim": desmiti(0, 7)},
        {"v": "30 + 40 = 70", "teksts": "Desmiti", "zim": desmiti(7, 0)},
    ]),

    Doma("Desmiti kā vieni",
         "Pilnus desmitus saskaita un atņem kā viencipara skaitļus - un "
         "pieliek 0.",
         soli=[
             "Nosauc desmitu skaitu: 30 - 3 desmiti.",
             "Saskaiti vai atņem desmitus.",
             "Pieliec 0: 7 desmiti = 70.",
         ]),

    Ievadi("Aprēķini", [
        {"jaut": "20 + 50 = ?", "atb": ["70"], "padoms": "2 + 5 = 7."},
        {"jaut": "60 + 30 = ?", "atb": ["90"], "padoms": "6 + 3 = 9."},
        {"jaut": "80 − 50 = ?", "atb": ["30"], "padoms": "8 − 5 = 3."},
        {"jaut": "100 − 40 = ?", "atb": ["60"], "padoms": "10 − 4 = 6."},
        {"jaut": "40 + 60 = ?", "atb": ["100"], "padoms": "4 + 6 = 10."},
        {"jaut": "70 − 70 = ?", "atb": ["0"], "padoms": "Viss prom."},
    ], pamats=4),

    Varianti("Kurš palīdz?", [
        {"jaut": "Kurš piemērs palīdz izrēķināt 50 + 20?",
         "opcijas": ["5 + 2", "50 + 2", "5 + 20"], "pareizi": 0,
         "padoms": "Desmitu skaits."},
    ]),

    Pasaule("Monētas pa 10 centiem",
            Ievadi("", [
                {"jaut": "Tev 40 c, iedeva vēl 30 c. Cik tagad?",
                 "atb": ["70"], "padoms": "4 + 3 desmiti."},
                {"jaut": "Nopirki par 50 c. Cik palika?", "atb": ["20"],
                 "padoms": "70 − 50."},
            ]),
            pavediens="veikals",
            konteksts="Krājkasītē ir tikai 10 centu monētas.",
            kapec="Desmitus skaita tikpat viegli kā vienus."),

    Kopsavilkums([
        "Saskaitu pilnus desmitus.",
        "Atņemu pilnus desmitus.",
        "Izmantoju piemērus ar vieniem.",
    ]),

    Majas([
        "Izrēķini 20 + 70, 90 − 60, 50 + 50.",
        "Saskaiti 10 centu monētas mājās.",
        "Izdomā piemēru ar desmitiem.",
    ]),
]
