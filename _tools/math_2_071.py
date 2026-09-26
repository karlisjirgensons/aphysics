# -*- coding: utf-8 -*-
"""2. klase, 71. stunda: «Kā divas darbības salikt vienā pierakstā?»

Divus soļus (40 − 12 = 28, 28 − 8 = 20) var uzrakstīt vienā izteiksmē:
40 − 12 − 8. Izteiksmi, kurā ir tikai «+» un «−», rēķina no kreisās uz
labo - tieši tādā secībā, kā notika stāstā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti)

TEMA = "Kā divas darbības salikt vienā pierakstā?"

MERKIS = ("Šodien pierakstīsim divas secīgas darbības kā vienu skaitlisku "
          "izteiksmi.")

SATURS = [
    Sakums("Kā divus soļus uzrakstīt vienā rindā?",
           fakti=["Pa soļiem: 40 − 12 = 28, 28 − 8 = 20.",
                  "Vienā rindā: 40 − 12 − 8 = 20.",
                  "Tā ir izteiksme ar divām darbībām."]),

    Doma("Izteiksme",
         "Izteiksme ir skaitļi, kas savienoti ar darbību zīmēm.",
         soli=[
             "Pirmā darbība - kā stāstā: 40 − 12.",
             "Otro pievieno uzreiz aiz tās: − 8.",
             "Rēķina no kreisās uz labo.",
             "Izteiksmes vērtība - rezultāts: 20.",
         ]),

    Slidnis("No soļiem uz izteiksmi", [
        {"v": "25 + 8 = 33", "teksts": "Pirmais solis."},
        {"v": "33 − 6 = 27", "teksts": "Otrais solis."},
        {"v": "25 + 8 − 6 = 27", "teksts": "Abi soļi vienā izteiksmē."},
    ]),

    Varianti("Kura izteiksme?", [
        {"jaut": "Bija 50 €, iztērēja 18 €, saņēma 10 €.",
         "opcijas": ["50 − 18 + 10", "50 + 18 − 10", "50 − 18 − 10"],
         "pareizi": 0, "padoms": "Iztērēja - mīnus, saņēma - plus."},
        {"jaut": "Plauktā 34 grāmatas, ielika 12, paņēma 20.",
         "opcijas": ["34 + 12 − 20", "34 − 12 + 20", "34 + 12 + 20"],
         "pareizi": 0, "padoms": "Ielika - plus, paņēma - mīnus."},
        {"jaut": "Autobusā 18 cilvēki, iekāpa 7, vēl iekāpa 5.",
         "opcijas": ["18 + 7 + 5", "18 − 7 + 5", "18 + 7 − 5"],
         "pareizi": 0, "padoms": "Abas reizes iekāpa."},
        {"jaut": "Kastē 60 konfektes, apēda 15, apēda vēl 10.",
         "opcijas": ["60 − 15 − 10", "60 + 15 − 10", "60 − 15 + 10"],
         "pareizi": 0, "padoms": "Abas reizes kļūst mazāk."},
    ]),

    Ievadi("Aprēķini vērtību", [
        {"jaut": "50 − 18 + 10 = ?", "atb": ["42"], "padoms": "32 + 10."},
        {"jaut": "34 + 12 − 20 = ?", "atb": ["26"], "padoms": "46 − 20."},
        {"jaut": "18 + 7 + 5 = ?", "atb": ["30"], "padoms": "25 + 5."},
        {"jaut": "60 − 15 − 10 = ?", "atb": ["35"], "padoms": "45 − 10."},
        {"jaut": "72 − 30 + 8 = ?", "atb": ["50"], "padoms": "42 + 8."},
        {"jaut": "45 + 25 − 40 = ?", "atb": ["30"], "padoms": "70 − 40."},
    ], pamats=4),

    Pasaule("Lifts birojā",
            Ievadi("", [
                {"jaut": "Liftā 6 cilvēki. 3. stāvā iekāpa 4, 5. stāvā "
                         "izkāpa 7. Uzraksti izteiksmi un aprēķini: cik "
                         "palika?", "atb": ["3"], "padoms": "6 + 4 − 7."},
                {"jaut": "Liftā var braukt 12 cilvēki. Cik vēl var iekāpt?",
                 "atb": ["9"], "padoms": "12 − 3."},
            ]),
            pavediens="maja",
            konteksts="Lifts apstājas vairākos stāvos.",
            kapec="Viena izteiksme apraksta visu braucienu."),

    Kopsavilkums([
        "Pierakstu divas darbības vienā izteiksmē.",
        "Rēķinu izteiksmi no kreisās uz labo.",
        "Zinu, ka rezultāts ir izteiksmes vērtība.",
    ]),

    Majas([
        "Pieraksti ar izteiksmi: tev bija 20 €, nopirki par 7 €, dabūji 5 €.",
        "Aprēķini tās vērtību.",
        "Izdomā vēl vienu stāstu ar divām darbībām.",
    ]),
]
