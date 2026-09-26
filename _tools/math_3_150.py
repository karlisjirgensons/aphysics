# -*- coding: utf-8 -*-
"""3. klase, 150. stunda: «Cik smaga ir prece?»

Masas mērvienības un to pieraksts ar komatu. Kilograms sadalās tūkstoš
gramos, tāpēc 0,357 kg ir tieši 357 g - tas pats decimāldaļu pieraksts, ko
skolēns jau pazīst no naudas.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Cik smaga ir prece?"

MERKIS = ("Lietosim gramus un kilogramus; sapratīsim, ka 0,357 kg ir 357 g.")

SATURS = [
    Sakums("Ko nozīmē 0,357 kg uz iepakojuma?",
           zimejums=restis([["1 kg", "=", "1000 g"],
                            ["0,5 kg", "=", "500 g"],
                            ["0,357 kg", "=", "357 g"]],
                           "kilogrami un grami"),
           paraksts="Aiz komata ir grami - tieši tāpat kā centi pie eiro.",
           fakti=["1 kg = 1000 g.",
                  "0,357 kg ir 357 grami."]),

    Doma("Aiz komata ir grami",
         "Kilogramu sadala 1000 gramos, tāpēc cipari aiz komata parāda "
         "gramus.",
         soli=[
             "Pirms komata ir veselie kilogrami.",
             "Aiz komata ir grami - vienmēr trīs cipari.",
             "Lai pārvērstu kilogramus gramos, reizini ar 1000.",
             "Lai pārvērstu gramus kilogramos, dali ar 1000.",
         ],
         pieze="Tāpēc 0,5 kg raksta arī kā 0,500 kg - abos gadījumos tie ir "
               "500 grami."),

    Paraugs("Cik gramu ir 2,350 kg?",
            uzd="Izsaki 2,350 kg gramos.",
            soli=[
                ("2 kg = 2000 g",
                 "Katrā kilogramā ir 1000 gramu."),
                ("350 g",
                 "Cipari aiz komata."),
                ("2000 + 350 = 2350",
                 "Kopā 2350 grami."),
            ],
            atbilde="2350 g"),

    Ievadi("Kilogrami un grami", [
        {"jaut": "Cik gramu ir 1 kg?", "atb": ["1000"],
         "padoms": "Tūkstotis."},
        {"jaut": "Cik gramu ir 0,357 kg?", "atb": ["357"],
         "padoms": "Cipari aiz komata."},
        {"jaut": "Cik gramu ir 2,350 kg?", "atb": ["2350"],
         "padoms": "2000 + 350."},
        {"jaut": "Cik gramu ir 0,5 kg?", "atb": ["500"],
         "padoms": "Puse kilograma."},
        {"jaut": "Izsaki 750 g kilogramos. Raksti ar komatu.",
         "atb": ["0,75", "0,750", "0.75", "0.750"], "padoms": "750 : 1000."},
        {"jaut": "Cik gramu ir 3 kg un 200 g?", "atb": ["3200"],
         "padoms": "3000 + 200."},
    ], pamats=4),

    Zimejums("Masas mērvienības",
             restis([["g", "kg", "t"],
                     ["1000 g = 1 kg", "1000 kg = 1 t", ""]],
                    "katra nākamā 1000 reižu lielāka"),
             paskaidro="Grams, kilograms un tonna - katra nākamā ir tūkstoš "
                       "reižu lielāka.",
             ievads="Trīs masas vienības."),

    Varianti("Cik tas ir?", [
        {"jaut": "Cik gramu ir 0,25 kg?",
         "opcijas": ["250", "25", "2500", "0,25"],
         "pareizi": 0, "padoms": "Ceturtdaļa kilograma."},
        {"jaut": "Kura masa ir lielāka?",
         "opcijas": ["0,9 kg", "800 g", "0,5 kg", "750 g"],
         "pareizi": 0, "padoms": "Pārvērt visu gramos."},
        {"jaut": "Cik kilogramu ir 2500 g?",
         "opcijas": ["2,5", "25", "250", "0,25"],
         "pareizi": 0, "padoms": "2500 : 1000."},
        {"jaut": "Cik gramu ir 1 kg un 50 g?",
         "opcijas": ["1050", "150", "1500", "10050"],
         "pareizi": 0, "padoms": "1000 + 50."},
    ], pamats=4),

    Pasaule("Cik smaga ir skolas soma?",
            Ievadi("", [
                {"jaut": "Soma sver 3 kg 200 g. Cik gramu tas ir?",
                 "atb": ["3200"], "padoms": "3000 + 200."},
                {"jaut": "Viena grāmata sver 400 g. Cik gramu sver 5 "
                         "grāmatas?",
                 "atb": ["2000"], "padoms": "5 · 400."},
                {"jaut": "Cik kilogramu tas ir?", "atb": ["2"],
                 "padoms": "2000 : 1000."},
                {"jaut": "Cik gramu sver pārējās somas lietas?",
                 "atb": ["1200"], "padoms": "3200 − 2000."},
            ]),
            pavediens="skola",
            konteksts="Skolas somai ieteicamais svars ir ap 3 kg - to var "
                      "pārbaudīt ar mājas svariem.",
            kapec="Gramus un kilogramus jāprot pārvērst, jo uz iepakojumiem "
                  "raksta abus."),

    Kopsavilkums([
        "Zinu, ka 1 kg = 1000 g.",
        "Izsaku kilogramus gramos un otrādi.",
        "Saprotu pierakstu 0,357 kg.",
        "Salīdzinu masas, kas izteiktas dažādās vienībās.",
    ]),

    Majas([
        "Atrodi mājās trīs iepakojumus un pieraksti to masu gramos.",
        "Nosver savu skolas somu.",
        "Izsaki tās masu gan kilogramos, gan gramos.",
    ]),
]
