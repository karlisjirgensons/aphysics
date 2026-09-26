# -*- coding: utf-8 -*-
"""4. klase, 14. stunda: «Kad jāsadala tūkstotis?»

Grūtākā vieta rakstiskajā atņemšanā ir nulles mazināmajā: 5000 − 1873.
Te nevar aizņemties no kaimiņa, jo kaimiņš ir tukšs - jāiet līdz
tūkstotim un jāsadala tas: 1 T = 9 S + 9 D + 10 V. Stunda to parāda ar
naudas modeli, lai «aizņemšanās» nav maģija.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, restis)

TEMA = "Kad jāsadala tūkstotis?"

MERKIS = ("Atņemsim ar pāreju citā šķirā un paskaidrosim, kā tūkstoti "
          "sadala simtos, desmitos un vienos.")

SATURS = [
    Sakums("Kā izdot atlikumu, ja kasē tikai tūkstoši?",
           zimejums=restis([["T", "S", "D", "V"],
                            [5, 0, 0, 0],
                            [4, 9, 9, 10]],
                           "5000 pirms un pēc sadalīšanas"),
           paraksts="Tas pats skaitlis - tikai viens tūkstotis izmainīts.",
           fakti=["Kasiere nevar izdot atlikumu no tukšas kases.",
                  "Viņa samaina tūkstoti sīkākos - un tad var.",
                  "Stabiņā dara tieši to pašu."]),

    Doma("Ja kaimiņš ir tukšs, ej tālāk un sadali lielāko šķiru",
         "Viens tūkstotis ir 9 simti, 9 desmiti un 10 vieni - tā to sadala, "
         "kad vajag aizņemties.",
         soli=[
             "Ja vienos nepietiek, mēģini aizņemties no desmitiem.",
             "Ja desmitu nav, ej uz simtiem; ja arī to nav - uz tūkstošiem.",
             "Sadali tūkstoti: tūkstošos paliek par 1 mazāk, simtos 9, "
             "desmitos 9, vienos + 10.",
             "Tagad atņem katru šķiru.",
         ],
         pieze="1000 = 900 + 90 + 10. Pārbaudi: 900 + 90 + 10 = 1000."),

    Slidnis("5000 sadalās",
            soli=[
                {"v": "5 T 0 S 0 D 0 V", "teksts": "Sākumā tikai tūkstoši."},
                {"v": "4 T 10 S 0 D 0 V", "teksts": "Vienu tūkstoti "
                 "samaina 10 simtos."},
                {"v": "4 T 9 S 10 D 0 V", "teksts": "Vienu simtu - 10 "
                 "desmitos."},
                {"v": "4 T 9 S 9 D 10 V", "teksts": "Vienu desmitu - 10 "
                 "vienos. Tagad var atņemt!"},
            ],
            ievads="Skaties, kā viens tūkstotis pārvēršas sīkākā naudā."),

    Paraugs("5000 − 1873",
            uzd="Atņem rakstos 5000 − 1873.",
            soli=[
                ("5000 = 4 T 9 S 9 D 10 V",
                 "Sadala vienu tūkstoti."),
                ("10 − 3 = 7", "Vieni."),
                ("9 − 7 = 2", "Desmiti."),
                ("9 − 8 = 1", "Simti."),
                ("4 − 1 = 3", "Tūkstoši."),
                ("5000 − 1873 = 3127", None),
            ],
            atbilde="3127"),

    Ievadi("Sadali un atņem", [
        {"jaut": "3000 − 1456 = ?", "atb": ["1544"],
         "padoms": "3000 = 2 T 9 S 9 D 10 V."},
        {"jaut": "7000 − 2385 = ?", "atb": ["4615"],
         "padoms": "Sadali vienu tūkstoti."},
        {"jaut": "6003 − 2718 = ?", "atb": ["3285"],
         "padoms": "Vienos 3 < 8 - desmitu nav, simtu nav."},
        {"jaut": "8040 − 3567 = ?", "atb": ["4473"],
         "padoms": "Simtu nav - sadali tūkstoti."},
        {"jaut": "10 000 − 4321 = ?", "atb": ["5679"],
         "padoms": "10 000 = 9 T 9 S 9 D 10 V."},
        {"jaut": "4100 − 2999 = ?", "atb": ["1101"],
         "padoms": "Vai: 4100 − 3000 + 1."},
    ], pamats=4),

    Varianti("Kā sadala?", [
        {"jaut": "Ko iegūst, sadalot vienu tūkstoti simtos?",
         "opcijas": ["10 simtu", "100 simtu", "1 simtu", "1000 simtu"],
         "pareizi": 0, "padoms": "1000 : 100."},
        {"jaut": "Kā pierakstīt 6000, lai varētu atņemt 1 vienu?",
         "opcijas": ["5 T 9 S 9 D 10 V", "6 T 9 S 9 D 10 V",
                     "5 T 10 S 10 D 10 V", "6 T 0 S 0 D 10 V"],
         "pareizi": 0, "padoms": "Tūkstošos paliek par vienu mazāk."},
        {"jaut": "Kurā rēķinā jāsadala tūkstotis?",
         "opcijas": ["4000 − 125", "4567 − 123", "4500 − 400",
                     "4999 − 999"], "pareizi": 0,
         "padoms": "Kur mazināmajā ir nulles un atņēmējā - nē."},
        {"jaut": "Cik ir 1000 − 1?",
         "opcijas": ["999", "900", "990", "0"], "pareizi": 0,
         "padoms": "9 S 9 D 9 V."},
    ], pamats=4),

    Pasaule("Kasē",
            Ievadi("", [
                {"jaut": "Veikals apmaksā rēķinu 2000 € no konta, kurā bija "
                         "5000 €. Cik palika?",
                 "atb": ["3000"], "padoms": "5000 − 2000."},
                {"jaut": "Tad tas samaksā vēl 1847 €. Cik palika?",
                 "atb": ["1153"], "padoms": "3000 − 1847."},
                {"jaut": "Klase krāj 1000 € ekskursijai. Sakrāti 687 €. "
                         "Cik trūkst?",
                 "atb": ["313"], "padoms": "1000 − 687."},
                {"jaut": "Datoram vajag 1500 €, ir 1036 €. Cik trūkst?",
                 "atb": ["464"], "padoms": "1500 − 1036."},
            ]),
            pavediens="veikals",
            konteksts="Kad maksā ar lielu banknoti, pārdevējam jāizdod "
                      "atlikums - tā ir atņemšana ar sadalīšanu.",
            kapec="Kas prot sadalīt tūkstoti, tas pārbauda atlikumu bez "
                  "kalkulatora."),

    Kopsavilkums([
        "Atņemu, ja mazināmajā ir nulles.",
        "Paskaidroju, kā tūkstoti sadala 9 S 9 D 10 V.",
        "Pārbaudu starpību ar saskaitīšanu.",
    ]),

    Majas([
        "Ar spēļu naudu parādi, kā samaina 1000 sīkākos, lai izdotu 1 €.",
        "Saskaiti šodienas soļus un izrēķini, cik trūkst līdz 10 000.",
        "Izdomā divus atņemšanas piemērus, kuros jāsadala tūkstotis.",
    ]),
]
