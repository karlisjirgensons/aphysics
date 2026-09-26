# -*- coding: utf-8 -*-
"""3. klase, 129. stunda: «Cik simtu, desmitu un vienu?»

Decimālais sastāvs ir tas, uz kā balstās visa saskaitīšana un atņemšana
stabiņā. Te skolēns to pieraksta izvērstā formā un iemācās arī otro
jautājumu: cik *pavisam* desmitu ir skaitlī 357 - ne 5, bet 35.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, Zimejums,
                         restis)

TEMA = "Cik simtu, desmitu un vienu?"

MERKIS = ("Noteiksim trīsciparu skaitļa decimālo sastāvu un pierakstīsim to "
          "izvērstā formā.")

SATURS = [
    Sakums("Cik desmitu ir skaitlī 357?",
           zimejums=restis([[357, "=", 300, "+", 50, "+", 7]],
                           "decimālais sastāvs"),
           paraksts="Desmitu vietā ir 5, bet desmitu pavisam ir 35.",
           fakti=["Skaitlī 357 ir 3 simti, 5 desmiti un 7 vieni.",
                  "Bet desmitu pavisam ir 35, jo katrā simtā ir 10 desmitu."]),

    Doma("Vietas cipars un kopējais skaits ir divi dažādi jautājumi",
         "Desmitu vietā ir 5, bet desmitu pavisam ir 35 - jo arī simti "
         "sastāv no desmitiem.",
         soli=[
             "Pieraksti skaitli vietu tabulā.",
             "Nosauc katras vietas ciparu.",
             "Lai uzzinātu, cik desmitu pavisam, aizsedz vienu ciparu.",
             "Lai uzzinātu, cik simtu pavisam, aizsedz divus ciparus.",
         ],
         pieze="Tāpēc, atņemot 40 no 357, var strādāt ar desmitiem: 35 "
               "desmiti mīnus 4 desmiti ir 31 desmits, tas ir, 317."),

    Slidnis("Cik ir pavisam",
            soli=[
                {"v": "357", "teksts": "Pats skaitlis.", "josla": 100},
                {"v": "35 desmiti", "teksts": "Aizsedz pēdējo ciparu.",
                 "josla": 60},
                {"v": "3 simti", "teksts": "Aizsedz divus pēdējos.",
                 "josla": 30},
            ],
            ievads="Aizsedzot ciparus, redz, cik ir pavisam."),

    Paraugs("Kāds ir skaitļa 357 sastāvs?",
            uzd="Nosaki, cik simtu, desmitu un vienu ir skaitlī 357, un "
                "pieraksti to izvērstā formā.",
            soli=[
                ("3 simti, 5 desmiti, 7 vieni",
                 "Katras vietas cipars."),
                ("357 = 300 + 50 + 7",
                 "Izvērstā forma."),
                ("Desmitu pavisam ir 35",
                 "Jo 3 simti ir 30 desmitu, un vēl 5 klāt."),
            ],
            atbilde="300 + 50 + 7"),

    Ievadi("Decimālais sastāvs", [
        {"jaut": "Cik simtu ir skaitlī 357?", "atb": ["3"],
         "padoms": "Simtu cipars."},
        {"jaut": "Cik desmitu ir desmitu vietā skaitlī 357?", "atb": ["5"],
         "padoms": "Desmitu cipars."},
        {"jaut": "Cik desmitu pavisam ir skaitlī 357?", "atb": ["35"],
         "padoms": "Aizsedz pēdējo ciparu."},
        {"jaut": "Cik simtu pavisam ir skaitlī 748?", "atb": ["7"],
         "padoms": "Simtu cipars."},
        {"jaut": "Cik desmitu pavisam ir skaitlī 480?", "atb": ["48"],
         "padoms": "Aizsedz pēdējo ciparu."},
        {"jaut": "300 + 50 + 7 = ?", "atb": ["357"],
         "padoms": "Saskaita izvērsto formu."},
    ], pamats=4),

    Zimejums("Divi jautājumi par vienu skaitli",
             restis([["jautājums", "atbilde"],
                     ["Cik desmitu vietā?", 5],
                     ["Cik desmitu pavisam?", 35]],
                    "skaitlis 357"),
             paskaidro="Pirmais jautājums ir par ciparu, otrais - par visu "
                       "skaitli.",
             ievads="Abi jautājumi ir pareizi, bet dažādi."),

    Varianti("Cik tur ir?", [
        {"jaut": "Cik desmitu pavisam ir skaitlī 620?",
         "opcijas": ["62", "2", "6", "620"],
         "pareizi": 0, "padoms": "Aizsedz pēdējo ciparu."},
        {"jaut": "Cik simtu pavisam ir skaitlī 905?",
         "opcijas": ["9", "0", "90", "905"],
         "pareizi": 0, "padoms": "Simtu cipars."},
        {"jaut": "Kā izvērst 506?",
         "opcijas": ["500 + 6", "50 + 6", "500 + 60", "5 + 0 + 6"],
         "pareizi": 0, "padoms": "Desmitu vietā nulle."},
        {"jaut": "400 + 80 + 3 = ?",
         "opcijas": ["483", "438", "384", "4803"],
         "pareizi": 0, "padoms": "Saskaita pa vietām."},
    ], pamats=4),

    Pasaule("Cik dienu ir misijā?",
            Ievadi("", [
                {"jaut": "Misija ilgst 357 dienas. Cik pilnu simtu tajā ir?",
                 "atb": ["3"], "padoms": "Simtu cipars."},
                {"jaut": "Cik desmitu pavisam ir 357 dienās?", "atb": ["35"],
                 "padoms": "Aizsedz pēdējo ciparu."},
                {"jaut": "Cik pilnu nedēļu ir 357 dienās?", "atb": ["51"],
                 "padoms": "357 : 7."},
                {"jaut": "Cik dienu paliek pāri?", "atb": ["0"],
                 "padoms": "51 · 7 = 357."},
            ]),
            pavediens="kosmoss",
            konteksts="Misijas ilgumu saka gan dienās, gan nedēļās - abi "
                      "skaitļi apraksta vienu un to pašu laiku.",
            kapec="Decimālais sastāvs ļauj pārrēķināt bez kalkulatora."),

    Kopsavilkums([
        "Nosaku trīsciparu skaitļa decimālo sastāvu.",
        "Pierakstu skaitli izvērstā formā.",
        "Atšķiru «cik desmitu vietā» no «cik desmitu pavisam».",
        "Saskaitu izvērsto formu atpakaļ.",
    ]),

    Majas([
        "Izvērs skaitļus 726, 408 un 950.",
        "Pasaki, cik desmitu pavisam ir katrā.",
        "Atrodi skaitli, kurā ir tieši 40 desmitu.",
    ]),
]
