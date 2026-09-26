# -*- coding: utf-8 -*-
"""3. klase, 31. stunda: «Kā atrisināt divu darbību uzdevumu?»

Pirmais uzdevums, kurā atbilde nav pieejama ar vienu rēķinu. Galvenais nav
aritmētika, bet secība: ko var izrēķināt tūlīt un ko - tikai pēc tam. Tāpēc
risinājumu vispirms pieraksta pa darbībām un tikai tad kā vienu izteiksmi.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, Zimejums,
                         restis)

TEMA = "Kā atrisināt divu darbību uzdevumu?"

MERKIS = ("Risināsim divu darbību situācijas uzdevumu un pierakstīsim "
          "risinājumu gan pa darbībām, gan ar vienu izteiksmi.")

SATURS = [
    Sakums("Ko var izrēķināt uzreiz un ko - tikai pēc tam?",
           zimejums=restis([["5 kastes pa 8", "→", 40],
                            ["40 − 12", "→", 28]],
                           "divi soļi pēc kārtas"),
           paraksts="Otro darbību var izdarīt tikai tad, kad ir pirmās "
                    "atbilde.",
           fakti=["Divu darbību uzdevumā viena atbilde ir starpatbilde.",
                  "Grūtākais ir izvēlēties, kura darbība ir pirmā."]),

    Doma("Vispirms izrēķini to, ko vari",
         "Atrodi darbību, kurai visi skaitļi jau ir zināmi - tā ir pirmā.",
         soli=[
             "Izlasi uzdevumu un pieraksti, kas ir zināms.",
             "Atrodi darbību, kurai abi skaitļi jau ir doti.",
             "Izrēķini to un pieraksti starpatbildi.",
             "Ar starpatbildi izrēķini galveno jautājumu.",
             "Pieraksti visu kā vienu izteiksmi.",
         ],
         pieze="Starpatbilde uzdevuma jautājumā nekad neparādās - tā ir "
               "tikai pakāpiens uz īsto atbildi."),

    Slidnis("Divi soļi, viena atbilde",
            soli=[
                {"v": "5 · 8 = 40",
                 "teksts": "Pirmais solis: cik cepumu ir kastēs.",
                 "josla": 50},
                {"v": "40 − 12 = 28",
                 "teksts": "Otrais solis: cik palika pēc apēšanas.",
                 "josla": 80},
                {"v": "5 · 8 − 12 = 28",
                 "teksts": "Abi soļi vienā izteiksmē.", "josla": 100},
            ],
            ievads="Spied soļus un skaties, kā no diviem rēķiniem sanāk "
                   "viena izteiksme."),

    Paraugs("Cik naudas paliek pāri?",
            uzd="Kabatā ir 90 ct. Nopirka 4 zīmuļus pa 15 ct. Cik naudas "
                "palika?",
            soli=[
                ("4 · 15 = 60",
                 "Pirmais solis: cik maksāja pirkums."),
                ("90 − 60 = 30",
                 "Otrais solis: cik palika no kabatā esošās naudas."),
                ("90 − 4 · 15 = 30",
                 "Viena izteiksme; reizināšanu izpilda pirms atņemšanas."),
            ],
            atbilde="30 ct"),

    Ievadi("Divi soļi", [
        {"jaut": "6 kastes pa 7 olām; 5 olas saplīsa. Cik olu palika?",
         "atb": ["37"], "padoms": "6 · 7 = 42; 42 − 5."},
        {"jaut": "Kabatā 80 ct; nopirka 3 preces pa 20 ct. Cik palika?",
         "atb": ["20"], "padoms": "3 · 20 = 60; 80 − 60."},
        {"jaut": "Klasē 24 skolēni; 3 grupās pa 6 aizgāja. Cik palika?",
         "atb": ["6"], "padoms": "3 · 6 = 18; 24 − 18."},
        {"jaut": "9 somas pa 4 grāmatām; vēl 7 grāmatas plauktā. Cik kopā?",
         "atb": ["43"], "padoms": "9 · 4 = 36; 36 + 7."},
        {"jaut": "48 ābolus salika 6 grozos; 2 grozus aiznesa. Cik ābolu "
                 "aiznesa?",
         "atb": ["16"], "padoms": "48 : 6 = 8; 2 · 8."},
        {"jaut": "Bija 60 lapas; izdalīja 5 bērniem pa 8. Cik palika?",
         "atb": ["20"], "padoms": "5 · 8 = 40; 60 − 40."},
    ], pamats=4,
        ievads="Ieraksti tikai galīgo atbildi - starpatbildi izrēķini galvā "
               "vai uz lapas."),

    Zimejums("Risinājuma pieraksts",
             restis([["1. darbība", "4 · 15 = 60"],
                     ["2. darbība", "90 − 60 = 30"],
                     ["izteiksme", "90 − 4 · 15"]],
                    "divi pieraksti, viena atbilde"),
             paskaidro="Pieraksts pa darbībām parāda domu gaitu; izteiksme "
                       "to pašu pasaka īsāk.",
             ievads="Abi pieraksti ir pareizi."),

    Varianti("Kura darbība ir pirmā?", [
        {"jaut": "«7 kastes pa 6, no tām 9 izņēma» - kura darbība pirmā?",
         "opcijas": ["Reizināšana", "Atņemšana", "Dalīšana", "Saskaitīšana"],
         "pareizi": 0, "padoms": "Vispirms jāzina, cik bija kopā."},
        {"jaut": "«56 ābolus salika 8 grozos, 3 grozus aiznesa» - kura "
                 "darbība pirmā?",
         "opcijas": ["Dalīšana", "Atņemšana", "Reizināšana", "Saskaitīšana"],
         "pareizi": 0, "padoms": "Vispirms jāzina, cik ir vienā grozā."},
        {"jaut": "Kura izteiksme atbilst uzdevumam «bija 100 ct, nopirka 4 "
                 "preces pa 20 ct»?",
         "opcijas": ["100 − 4 · 20", "100 · 4 − 20", "(100 − 4) · 20",
                     "100 − 4 + 20"],
         "pareizi": 0, "padoms": "Vispirms izrēķina pirkuma summu."},
        {"jaut": "Kas ir starpatbilde?",
         "opcijas": ["Rezultāts, kas vajadzīgs otrajai darbībai",
                     "Galīgā atbilde", "Uzdevuma jautājums",
                     "Pārbaudes rēķins"],
         "pareizi": 0, "padoms": "Tā ir pakāpiens, ne atbilde."},
    ], pamats=4),

    Pasaule("Cik naudas paliks pēc iepirkšanās?",
            Ievadi("", [
                {"jaut": "Kabatā 100 ct. Nopirka 5 burtnīcas pa 12 ct. Cik "
                         "maksāja pirkums?",
                 "atb": ["60"], "padoms": "5 · 12."},
                {"jaut": "Cik naudas palika?",
                 "atb": ["40"], "padoms": "100 − 60."},
                {"jaut": "Par atlikušo naudu pirka zīmuļus pa 8 ct. Cik "
                         "zīmuļu var nopirkt?",
                 "atb": ["5"], "padoms": "40 : 8."},
                {"jaut": "Cik naudas paliks pēc zīmuļiem?",
                 "atb": ["0"], "padoms": "40 − 40."},
            ]),
            pavediens="veikals",
            konteksts="Iepirkšanās gandrīz vienmēr ir vairāku soļu rēķins: "
                      "summa, atlikums un tad nākamais pirkums.",
            kapec="Katrs solis atbild uz savu jautājumu, un tikai pēdējais - "
                  "uz uzdevuma jautājumu."),

    Kopsavilkums([
        "Risinu divu darbību situācijas uzdevumu.",
        "Atrodu, kura darbība ir pirmā un kura - otrā.",
        "Pierakstu risinājumu pa darbībām un kā vienu izteiksmi.",
        "Atšķiru starpatbildi no galīgās atbildes.",
    ]),

    Majas([
        "Izrēķini: kabatā 70 ct, nopirka 3 preces pa 15 ct - cik palika?",
        "Pieraksti to pašu uzdevumu kā vienu izteiksmi.",
        "Izdomā savu divu darbību uzdevumu par mājas pirkumiem.",
    ]),
]
