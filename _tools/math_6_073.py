# -*- coding: utf-8 -*-
"""6. klase, 73. stunda: «Kāpēc litrs ir kubikdecimetrs?»

Sakarība 1 l = 1 dm³ savieno divas pasaules: ģeometriju un veikalu. Pēc šīs
stundas tilpuma uzdevumā drīkst parādīties gan centimetri, gan litri, un
skolēns zina, kā tos savienot.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Kustiba, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kāpēc litrs ir kubikdecimetrs?"

MERKIS = ("Skaidrosim sakarību 1 l = 1 dm³ un lietosim to aprēķinos.")

SATURS = [
    Sakums("Litrs ir kubs ar malu 10 cm",
           zimejums=restis([["1 l", "1 dm³", "1000 cm³"],
                            ["1 ml", "1 cm³", "0,001 l"]]),
           paraksts="Viena rinda - viens un tas pats tilpums trijos "
                    "pierakstos.",
           fakti=["1 l = 1 dm³ = 1000 cm³.",
                  "1 ml = 1 cm³ - tieši tāpēc šļircēs ir mililitri.",
                  "Litrs nav atsevišķa vienība - tas ir cits nosaukums."]),

    Doma("Litrs un kubikdecimetrs ir viens un tas pats",
         "Šķidruma tilpumu mēra litros, bet ķermeņa - kubikvienībās; starp "
         "tiem ir vienādība 1 l = 1 dm³ = 1000 cm³.",
         soli=[
             "Aprēķini tilpumu kubikcentimetros.",
             "Izdali ar 1000 - iegūsi kubikdecimetrus.",
             "Pieraksti to pašu skaitli litros.",
             "Ja vajag mililitrus, kubikcentimetru skaits jau ir atbilde.",
             "Pārbaudi ar novērtējumu: vai trauks tiešām ir tik liels?",
         ],
         pieze="Tieši tāpēc uz iepakojumiem raksta gan «500 ml», gan "
               "«0,5 l» - tas ir viens un tas pats. Un 500 ml ir 500 cm³."),

    Paraugs("No centimetriem uz litriem",
            uzd="Kaste ir 30 cm x 20 cm x 25 cm. Cik litru ūdens tajā "
                "ietilpst?",
            soli=[
                ("30 · 20 · 25 = 15 000 cm³",
                 "Tilpums kubikcentimetros."),
                ("15 000 : 1000 = 15 dm³",
                 "Uz kubikdecimetriem."),
                ("15 dm³ = 15 l",
                 "Litrs ir kubikdecimetrs."),
                ("Pārbaude: 15 l ir apmēram spainis",
                 "Novērtējums ir ticams."),
            ],
            atbilde="15 l"),

    Ievadi("Pārej uz litriem", [
        {"jaut": "Cik litru ir 3000 cm³?",
         "atb": ["3"], "padoms": "3000 : 1000."},
        {"jaut": "Cik cm³ ir 0,5 l?",
         "atb": ["500"], "padoms": "0,5 · 1000."},
        {"jaut": "Kaste 20 x 10 x 10 cm. Cik litru tajā ietilpst?",
         "atb": ["2"], "padoms": "2000 cm³."},
        {"jaut": "Cik ml ir 1 cm³?",
         "atb": ["1"], "padoms": "Tie ir vienādi."},
        {"jaut": "Kaste 40 x 25 x 20 cm. Cik litru tajā ietilpst?",
         "atb": ["20"], "padoms": "20 000 cm³."},
        {"jaut": "Cik litru ir 250 000 cm³?",
         "atb": ["250"], "padoms": "250 000 : 1000."},
    ], pamats=4),

    Pasaule("Cik ilgi pildīsies tvertne?",
            Kustiba("", [
                {"jaut": "Tvertne 50 x 40 x 25 cm. Cik litru tajā ietilpst?",
                 "atb": 50, "beigas": 200, "iedala": 50, "mers": "litri",
                 "merkis": "pilna tvertne", "objekts": "Ūdens",
                 "padoms": "50 000 cm³."},
                {"jaut": "Tvertne 1 m x 0,5 m x 0,2 m. Cik litru?",
                 "atb": 100, "beigas": 200, "iedala": 50, "mers": "litri",
                 "merkis": "pilna tvertne", "objekts": "Ūdens",
                 "padoms": "100 dm · 5 dm · 2 dm = 0,1 m³ = 100 l."},
                {"jaut": "Muca 40 x 40 x 50 cm. Cik litru?",
                 "atb": 80, "beigas": 200, "iedala": 50, "mers": "litri",
                 "merkis": "pilna tvertne", "objekts": "Ūdens",
                 "padoms": "80 000 cm³."},
                {"jaut": "Kaste 30 x 30 x 20 cm. Cik litru?",
                 "atb": 18, "beigas": 200, "iedala": 50, "mers": "litri",
                 "merkis": "pilna tvertne", "objekts": "Ūdens",
                 "padoms": "18 000 cm³."},
            ]),
            pavediens="planeta",
            konteksts="Lietus ūdens tvertnes izmēru izvēlas pēc tā, cik "
                      "litru vajag dārzam - bet mēra centimetros.",
            kapec="Viena vienādība savieno ģeometriju ar ikdienu."),

    Varianti("Kurš pieraksts ir tas pats?", [
        {"jaut": "1 l ir tas pats, kas...",
         "opcijas": ["1 dm³", "1 cm³", "1 m³", "100 cm³"],
         "pareizi": 0,
         "padoms": "Kubs ar malu 10 cm."},
        {"jaut": "1 ml ir tas pats, kas...",
         "opcijas": ["1 cm³", "1 dm³", "10 cm³", "0,1 l"],
         "pareizi": 0,
         "padoms": "Tūkstošdaļa litra."},
        {"jaut": "Cik litru ir 1 m³?",
         "opcijas": ["1000", "100", "10", "1 000 000"],
         "pareizi": 0,
         "padoms": "1 m³ = 1000 dm³."},
        {"jaut": "Pudele 0,33 l. Cik cm³ tas ir?",
         "opcijas": ["330", "33", "3300", "0,33"],
         "pareizi": 0,
         "padoms": "0,33 · 1000."},
    ], pamats=4),

    Kopsavilkums([
        "Zinu, ka 1 l = 1 dm³ = 1000 cm³.",
        "Pārveidoju tilpumu no kubikcentimetriem uz litriem.",
        "Lietoju sakarību 1 ml = 1 cm³.",
        "Pārbaudu rezultātu ar novērtējumu.",
    ]),

    Majas([
        "Izmēri kādu mājas trauku un aprēķini tā tilpumu litros.",
        "Pārbaudi savu aprēķinu, ielejot ūdeni ar mērglāzi.",
        "Pieraksti, cik cm³ ir tavai ūdens pudelei.",
    ]),
]
