# -*- coding: utf-8 -*-
"""3. klase, 120. stunda: «Vai apgalvojums ir patiess?»

Mikrotemata noslēgums. Tas pats spriešanas veids, kas 96. stundā bija ar
daļām, tagad ar taisnstūriem: apgalvojumu apgāž ar konkrētu pretpiemēru -
divām figūrām, kurām skaitļi to atspēko.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         restis)

TEMA = "Vai apgalvojums ir patiess?"

MERKIS = ("Veidosim pretpiemēru, lai apgāztu aplamu apgalvojumu par "
          "taisnstūriem.")

SATURS = [
    Sakums("Vai lielāks perimetrs nozīmē lielāku laukumu?",
           zimejums=restis([["figūra", "perimetrs", "laukums"],
                            ["9 x 1", 20, 9],
                            ["5 x 5", 20, 25]],
                           "vienādi perimetri, dažādi laukumi"),
           paraksts="Abiem perimetrs ir 20, bet laukumi atšķiras gandrīz "
                    "trīs reizes.",
           fakti=["Perimetrs un laukums ir neatkarīgi lielumi.",
                  "Viens pretpiemērs apgāž apgalvojumu."]),

    Doma("Pretpiemērs ir divas konkrētas figūras",
         "Lai apgāztu apgalvojumu par taisnstūriem, pietiek uzzīmēt divus, "
         "kuriem skaitļi to atspēko.",
         soli=[
             "Izlasi apgalvojumu un saproti, ko tas apgalvo.",
             "Izvēlies divus taisnstūrus ar zināmiem izmēriem.",
             "Izrēķini abiem perimetru un laukumu.",
             "Parādi skaitļus, kas apgalvojumu atspēko.",
         ],
         pieze="Pretpiemēram jābūt konkrētam: ar skaitļiem, ne ar vārdiem "
               "«dažreiz nesanāk»."),

    Paraugs("Vai apgalvojums ir patiess?",
            uzd="«Ja diviem taisnstūriem ir vienāds perimetrs, tiem ir "
                "vienāds laukums.» Vai tas ir patiess?",
            soli=[
                ("9 x 1: P = 20, S = 9",
                 "Pirmais taisnstūris."),
                ("5 x 5: P = 20, S = 25",
                 "Otrais taisnstūris ar to pašu perimetru."),
                ("9 ≠ 25",
                 "Laukumi atšķiras - apgalvojums ir aplams."),
            ],
            atbilde="aplams"),

    Petijums("Uzzīmē savu pretpiemēru",
             vajag="rūtiņu lapa un zīmulis",
             soli=[
                 "Uzzīmē divus taisnstūrus ar perimetru 16 rūtiņas.",
                 "Izrēķini abu laukumus.",
                 "Pieraksti abus skaitļus blakus.",
                 "Uzraksti vienā teikumā, ko tas pierāda.",
             ],
             secinajums="Divi taisnstūri ar vienādu perimetru un dažādu "
                        "laukumu apgāž apgalvojumu par to, ka perimetrs "
                        "nosaka laukumu."),

    Ievadi("Izrēķini un salīdzini", [
        {"jaut": "Taisnstūris 9 x 1. Cik ir perimetrs?", "atb": ["20"],
         "padoms": "2 · 10."},
        {"jaut": "Taisnstūris 9 x 1. Cik ir laukums?", "atb": ["9"],
         "padoms": "9 · 1."},
        {"jaut": "Kvadrāts 5 x 5. Cik ir perimetrs?", "atb": ["20"],
         "padoms": "4 · 5."},
        {"jaut": "Kvadrāts 5 x 5. Cik ir laukums?", "atb": ["25"],
         "padoms": "5 · 5."},
        {"jaut": "Par cik kvadrātvienībām kvadrāta laukums ir lielāks?",
         "atb": ["16"], "padoms": "25 − 9."},
        {"jaut": "Taisnstūris 7 x 3. Cik ir perimetrs?", "atb": ["20"],
         "padoms": "2 · 10."},
    ], pamats=4),

    Zimejums("Vienāds laukums, dažādi perimetri",
             restis([["figūra", "laukums", "perimetrs"],
                     ["1 x 16", 16, 34],
                     ["4 x 4", 16, 16]],
                    "arī otrādi"),
             paskaidro="Tagad laukumi sakrīt, bet perimetri atšķiras vairāk "
                       "nekā divas reizes.",
             ievads="Pretpiemērs der abos virzienos."),

    Varianti("Patiess vai aplams?", [
        {"jaut": "«Vienāds perimetrs nozīmē vienādu laukumu.»",
         "opcijas": ["Aplams", "Patiess", "Tikai kvadrātiem",
                     "To nevar pateikt"],
         "pareizi": 0, "padoms": "9 x 1 un 5 x 5."},
        {"jaut": "«Vienāds laukums nozīmē vienādu perimetru.»",
         "opcijas": ["Aplams", "Patiess", "Tikai lielām figūrām",
                     "To nevar pateikt"],
         "pareizi": 0, "padoms": "1 x 16 un 4 x 4."},
        {"jaut": "«Kvadrātam ar dotu perimetru laukums ir vislielākais.»",
         "opcijas": ["Patiess", "Aplams", "Tikai maziem kvadrātiem",
                     "To nevar pateikt"],
         "pareizi": 0, "padoms": "Vienādākas malas - lielāks laukums."},
        {"jaut": "Kas jābūt pretpiemērā?",
         "opcijas": ["Konkrēti skaitļi", "Vārdisks paskaidrojums",
                     "Krāsains zīmējums", "Vairāki apgalvojumi"],
         "pareizi": 0, "padoms": "Bez skaitļiem tas nav pierādījums."},
    ], pamats=4),

    Pasaule("Vai būvnieka apgalvojums ir pareizs?",
            Ievadi("", [
                {"jaut": "Dārzs 1 m x 16 m. Cik kvadrātmetru ir laukums?",
                 "atb": ["16"], "padoms": "1 · 16."},
                {"jaut": "Cik metru žoga tam vajag?", "atb": ["34"],
                 "padoms": "2 · 17."},
                {"jaut": "Dārzs 4 m x 4 m. Cik metru žoga vajag?",
                 "atb": ["16"], "padoms": "4 · 4."},
                {"jaut": "Par cik metriem mazāk žoga vajag otrajam dārzam?",
                 "atb": ["18"], "padoms": "34 − 16."},
            ]),
            pavediens="maja",
            konteksts="Abiem dārziem laukums ir vienāds, bet žogs pirmajam "
                      "maksā vairāk nekā divreiz dārgāk.",
            kapec="Tāpēc būvnieks vienmēr rēķina abus lielumus, ne tikai "
                  "vienu."),

    Kopsavilkums([
        "Veidoju pretpiemēru ar konkrētiem skaitļiem.",
        "Apgāžu aplamu apgalvojumu par taisnstūriem.",
        "Zinu, ka perimetrs un laukums ir neatkarīgi lielumi.",
        "Pamatoju spriedumu ar aprēķinu.",
    ]),

    Majas([
        "Atrodi divus taisnstūrus ar perimetru 18 un dažādiem laukumiem.",
        "Atrodi divus ar laukumu 12 un dažādiem perimetriem.",
        "Uzraksti savu apgalvojumu par taisnstūriem un pārbaudi to.",
    ]),
]
