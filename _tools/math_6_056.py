# -*- coding: utf-8 -*-
"""6. klase, 56. stunda: «Kā rēķināt jauktā izteiksmē?»

Visas četras darbības vienā izteiksmē, kurā skaitļi rakstīti abos veidos.
Te sanāk kopā viss temats: darbību secība, pieraksta izvēle un pārveidošana.
Grūtākais nav rēķināt, bet izlemt, ar ko sākt.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti)

TEMA = "Kā rēķināt jauktā izteiksmē?"

MERKIS = ("Mācīsimies saskaitīt, atņemt, reizināt un dalīt daļskaitļus, kas "
          "pierakstīti abos veidos.")

SATURS = [
    Sakums("Vispirms viens pieraksts, tad darbības",
           fakti=["Izteiksmē 0,5 + {1|4} · 8 vispirms reizina, tad saskaita.",
                  "Visus skaitļus pārraksta vienā veidā pirms rēķināšanas.",
                  "Darbību secība paliek tā pati, kas veseliem skaitļiem."]),

    Doma("Vienots pieraksts, tad parastā secība",
         "Jauktā izteiksmē vispirms visus skaitļus pieraksta vienā veidā, un "
         "tad rēķina parastajā darbību secībā.",
         soli=[
             "Izlasi izteiksmi un atrodi, kura darbība ir pirmā.",
             "Izlem, kurā pierakstā strādāsi.",
             "Pārraksti visus skaitļus šajā pierakstā.",
             "Izrēķini pa darbībām: iekavas, reizināšana un dalīšana, tad "
             "saskaitīšana un atņemšana.",
             "Pieraksti atbildi vienkāršākajā formā.",
         ],
         pieze="Ja izteiksmē ir {1|3} vai {1|7}, decimālpieraksts nav "
               "precīzs - tad strādā ar parastajām daļām, lai kā gribētos "
               "citādi."),

    Paraugs("Trīs darbības vienā izteiksmē",
            uzd="Cik ir 0,5 + {1|4} · 8?",
            soli=[
                ("Vispirms reizināšana: {1|4} · 8 = 2",
                 "Darbību secība neatkarīga no pieraksta."),
                ("0,5 + 2",
                 "Paliek saskaitīšana."),
                ("= 2,5",
                 "Rezultāts decimālpierakstā."),
                ("Pārbaude: {1|2} + 2 = 2{1|2}",
                 "Tas pats skaitlis otrā pierakstā."),
            ],
            atbilde="2,5"),

    Ievadi("Izrēķini jaukto izteiksmi", [
        {"jaut": "Cik ir 0,5 + {1|4} · 8?",
         "atb": ["2,5", "2.5"], "padoms": "Vispirms reizina."},
        {"jaut": "Cik ir {1|2} · 6 − 0,5?",
         "atb": ["2,5", "2.5"], "padoms": "3 − 0,5."},
        {"jaut": "Cik ir 0,2 · 5 + {1|5}?",
         "atb": ["1,2", "1.2"], "padoms": "1 + 0,2."},
        {"jaut": "Cik ir {3|4} + 0,25?",
         "atb": ["1"], "padoms": "0,75 + 0,25."},
        {"jaut": "Cik ir (0,4 + {1|10}) · 10?",
         "atb": ["5"], "padoms": "Iekavās 0,5."},
        {"jaut": "Cik ir 2 − {1|4} · 0,8?",
         "atb": ["1,8", "1.8"], "padoms": "{1|4} · 0,8 = 0,2."},
    ], pamats=4,
        ievads="Darbību secība te ir tieši tāda pati kā veseliem skaitļiem."),

    Varianti("Ar ko sākt?", [
        {"jaut": "Izteiksmē 0,5 + {1|4} · 8 ar ko sāk?",
         "opcijas": ["Ar reizināšanu", "Ar saskaitīšanu",
                     "Ar pārveidošanu decimāldaļās", "Ar atņemšanu"],
         "pareizi": 0,
         "padoms": "Reizināšana pirms saskaitīšanas."},
        {"jaut": "Izteiksmē ({1|2} + 0,25) · 4 ar ko sāk?",
         "opcijas": ["Ar iekavām", "Ar reizināšanu",
                     "Ar dalīšanu", "Ar pārveidošanu"],
         "pareizi": 0,
         "padoms": "Iekavas vienmēr pirmās."},
        {"jaut": "Kurā pierakstā rēķināt {1|3} + 0,5?",
         "opcijas": ["Parastajās daļās", "Decimāldaļās",
                     "Jebkurā", "Rēķināt nevar"],
         "pareizi": 0,
         "padoms": "{1|3} decimālpierakstā nav precīzs."},
        {"jaut": "Cik ir ({1|2} + 0,25) · 4?",
         "opcijas": ["3", "0,75", "1,5", "4"],
         "pareizi": 0,
         "padoms": "0,75 · 4."},
    ], pamats=4),

    Pasaule("Cik maksā viss pasūtījums?",
            Ievadi("", [
                {"jaut": "3 kg pa 2,4 € un {1|2} kg pa 4 €. Cik eiro kopā?",
                 "atb": ["9,2", "9.2"], "padoms": "7,2 + 2."},
                {"jaut": "Piegāde maksā 0,75 € par katru kilogramu. Cik eiro "
                         "par 3,5 kg?",
                 "atb": ["2,625", "2.625"], "padoms": "3,5 · 0,75."},
                {"jaut": "Atlaide ir {1|4} no 9,2 €. Cik eiro tā ir?",
                 "atb": ["2,3", "2.3"], "padoms": "9,2 : 4."},
                {"jaut": "Cik eiro jāmaksā pēc atlaides?",
                 "atb": ["6,9", "6.9"], "padoms": "9,2 − 2,3."},
            ]),
            pavediens="veikals",
            konteksts="Čekā viena rinda ir daļa, otra - decimāldaļa, bet "
                      "summa ir viena.",
            kapec="Vienots pieraksts padara garu rēķinu pārbaudāmu."),

    Kopsavilkums([
        "Rēķinu izteiksmes, kurās skaitļi rakstīti abos veidos.",
        "Pārrakstu visus skaitļus vienā pierakstā pirms darbībām.",
        "Ievēroju darbību secību un iekavas.",
        "Pieraksta atbildi vienkāršākajā formā.",
    ]),

    Majas([
        "Izrēķini 1,5 − {1|4} · 2 un ({2|5} + 0,1) · 5.",
        "Izdomā izteiksmi ar trim darbībām un atrisini to.",
        "Pieraksti, kurā pierakstā strādāji un kāpēc.",
    ]),
]
