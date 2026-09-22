# -*- coding: utf-8 -*-
"""6. klase, 128. stunda: «Kāda būs summas zīme?»

Algoritma stunda, bet uzrakstīta kā prognoze. Summas zīmi var pateikt,
neizrēķinot pašu summu - un tas ir gan ātrāk, gan drošāk, jo kļūdainu zīmi
pamana uzreiz.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti)

TEMA = "Kāda būs summas zīme?"

MERKIS = ("Formulēsim apgalvojumus par summas zīmi un noteiksim to pirms "
          "aprēķina.")

SATURS = [
    Sakums("Zīmi var pateikt pirms rēķina",
           fakti=["Ja abi saskaitāmie ir ar vienu zīmi, summai ir tā pati "
                  "zīme.",
                  "Ja zīmes ir dažādas, summas zīmi nosaka lielākais "
                  "modulis.",
                  "Ja moduļi ir vienādi, summa ir nulle."]),

    Doma("Vienādas zīmes - saskaiti, dažādas - atņem",
         "Saskaitot divus skaitļus ar vienādām zīmēm, moduļus saskaita un "
         "saglabā zīmi; ar dažādām zīmēm - no lielākā moduļa atņem mazāko un "
         "ņem lielākā moduļa zīmi.",
         soli=[
             "Salīdzini abu saskaitāmo zīmes.",
             "Ja tās sakrīt, saskaiti moduļus un pieliec kopīgo zīmi.",
             "Ja atšķiras, atrodi, kuram modulis ir lielāks.",
             "No lielākā moduļa atņem mazāko.",
             "Rezultātam pieliec lielākā moduļa zīmi.",
         ],
         pieze="Šis nav jauns likums - tas ir tas pats bultiņu modelis, tikai "
               "pierakstīts vārdos. Garāka bultiņa nosaka virzienu, un tās "
               "«pārpalikums» ir rezultāts."),

    Slidnis("Kad zīme mainās",
            [{"v": "−8 + 2", "teksts": "= −6, negatīva", "josla": 20},
             {"v": "−8 + 6", "teksts": "= −2, negatīva", "josla": 40},
             {"v": "−8 + 8", "teksts": "= 0, robeža", "josla": 50},
             {"v": "−8 + 10", "teksts": "= 2, pozitīva", "josla": 70},
             {"v": "−8 + 14", "teksts": "= 6, pozitīva", "josla": 100}],
            ievads="Spied soli pa solim: pirmais saskaitāmais paliek −8. Zīme "
                   "mainās tieši tad, kad otrais modulis pārsniedz astoņi."),

    Paraugs("Nosaki zīmi, tad rēķini",
            uzd="Kāda ir summas zīme izteiksmēs −9 + (−4) un −9 + 4?",
            soli=[
                ("−9 + (−4): abas zīmes ir mīnusi",
                 "Summa būs negatīva."),
                ("Moduļi 9 un 4: 9 + 4 = 13",
                 "Rezultāts −13."),
                ("−9 + 4: zīmes atšķiras",
                 "Lielākais modulis ir 9, tam mīnuss."),
                ("9 − 4 = 5, zīme mīnus",
                 "Rezultāts −5."),
            ],
            atbilde="−13 un −5"),

    Ievadi("Nosaki zīmi un summu", [
        {"jaut": "Cik ir −9 + (−4)?",
         "atb": ["-13", "−13"], "padoms": "Vienādas zīmes - moduļus "
                                          "saskaita."},
        {"jaut": "Cik ir −9 + 4?",
         "atb": ["-5", "−5"], "padoms": "9 − 4, zīme mīnus."},
        {"jaut": "Cik ir 9 + (−4)?",
         "atb": ["5"], "padoms": "9 − 4, zīme pluss."},
        {"jaut": "Cik ir −3 + 11?",
         "atb": ["8"], "padoms": "11 − 3, zīme pluss."},
        {"jaut": "Cik ir −15 + 15?",
         "atb": ["0"], "padoms": "Vienādi moduļi."},
        {"jaut": "Cik ir −7 + (−13)?",
         "atb": ["-20", "−20"], "padoms": "7 + 13, zīme mīnus."},
    ], pamats=4,
        ievads="Pirms rēķini, pasaki, kāda būs zīme."),

    Varianti("Kāda būs zīme?", [
        {"jaut": "−12 + (−5). Summas zīme ir...",
         "opcijas": ["mīnus", "pluss", "nav zīmes", "nevar zināt"],
         "pareizi": 0,
         "padoms": "Abas zīmes vienādas."},
        {"jaut": "−12 + 20. Summas zīme ir...",
         "opcijas": ["pluss", "mīnus", "nav zīmes", "nevar zināt"],
         "pareizi": 0,
         "padoms": "Lielākais modulis ir 20."},
        {"jaut": "Ja moduļi ir vienādi, bet zīmes dažādas, summa ir...",
         "opcijas": ["nulle", "pozitīva", "negatīva", "dubulta"],
         "pareizi": 0,
         "padoms": "Pretēji skaitļi."},
        {"jaut": "Summas zīmi nosaka...",
         "opcijas": ["tas saskaitāmais, kuram lielāks modulis",
                     "pirmais saskaitāmais",
                     "otrais saskaitāmais", "vienmēr pluss"],
         "pareizi": 0,
         "padoms": "Garākā bultiņa."},
    ], pamats=4),

    Pasaule("Vai konts paliks mīnusā?",
            Ievadi("", [
                {"jaut": "Kontā −120 €, alga 200 €. Cik eiro būs kontā?",
                 "atb": ["80"], "padoms": "200 − 120, zīme pluss."},
                {"jaut": "Kontā −120 €, alga 90 €. Cik eiro būs kontā?",
                 "atb": ["-30", "−30"], "padoms": "120 − 90, zīme mīnus."},
                {"jaut": "Kontā −120 €, vēl viens rēķins 45 €. Cik eiro būs?",
                 "atb": ["-165", "−165"], "padoms": "120 + 45, zīme mīnus."},
                {"jaut": "Cik eiro vajag, lai konts kļūtu tieši nulle no "
                         "−165 €?",
                 "atb": ["165"], "padoms": "Pretējais skaitlis."},
            ]),
            pavediens="veikals",
            konteksts="Pirms maksājuma var pateikt, vai konts paliks mīnusā - "
                      "tam pietiek salīdzināt moduļus.",
            kapec="Zīmi nosaka lielākais modulis, ne secība."),

    Kopsavilkums([
        "Nosaku summas zīmi pirms aprēķina.",
        "Saskaitu moduļus, ja zīmes sakrīt.",
        "Atņemu moduļus, ja zīmes atšķiras.",
        "Pielieku rezultātam lielākā moduļa zīmi.",
    ]),

    Majas([
        "Nosaki zīmi un izrēķini −14 + 9; −14 + (−9); 14 + (−9).",
        "Uzraksti trīs izteiksmes, kuru summa ir negatīva.",
        "Uzraksti vienu, kuras summa ir tieši nulle.",
    ]),
]
