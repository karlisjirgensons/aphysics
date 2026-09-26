# -*- coding: utf-8 -*-
"""8. klase, 91. stunda: «Kā aprēķināt nezināmo leņķi?»

Četrstūra leņķu uzdevumi ar pamatojumu: leņķu summa 360°, vienpusleņķi
pie paralēlām malām (trapecē ∠A + ∠D = 180°), ārējais leņķis, vienādojums.
Zīmējuma trapecei leņķi atbilst koordinātēm (63° un 56°).
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, geometrija)

TEMA = "Kā aprēķināt nezināmo leņķi?"

MERKIS = "Aprēķināsim četrstūra nezināmos leņķus un pamatosim risinājumu."

SATURS = [
    Sakums("Cik liels ir ∠D?",
           zimejums=geometrija([("A", 0, 0), ("B", 7, 0), ("C", 5, 3),
                                ("D", 1.5, 3)],
                               nogriezni=["AB", "BC", "CD", "DA"],
                               lenki=[("DAB", "63°"), ("CDA", "?")],
                               iekrasot=[("ABCD", 0)]),
           paraksts="AB ∥ CD, tāpēc ∠A + ∠D = 180° (vienpusleņķi).",
           fakti=["Četrstūrī lieto leņķu summu 360°.",
                  "Pie paralēlām malām vienpusleņķu summa ir 180°.",
                  "Katram solim min pamatojumu."]),

    Doma("Plāns",
         "Vispirms meklē paralēlas malas, tad lieto summu 360°.",
         soli=[
             "Atzīmē zīmējumā visus zināmos leņķus.",
             "Paralēlas malas dod vienpusleņķus ar summu 180°.",
             "Atlikušo leņķi atrod no summas 360°.",
             "Pārbaudi, vai visu leņķu summa ir 360°.",
         ]),

    Paraugs("Trapece",
            uzd="Trapecē ABCD AB ∥ CD, ∠A = 63°, ∠B = 56°. Atrodi ∠C un ∠D.",
            soli=[
                ("∠D = 180° − 63° = 117°", "Vienpusleņķi pie AD."),
                ("∠C = 180° − 56° = 124°", "Vienpusleņķi pie BC."),
                ("63° + 56° + 124° + 117° = 360°", "Pārbaude."),
            ],
            atbilde="∠C = 124°, ∠D = 117°"),

    Ievadi("Aprēķini", [
        {"jaut": "Trapecē AB ∥ CD, ∠A = 70°. ∠D?", "atb": ["110"],
         "padoms": "Vienpusleņķi."},
        {"jaut": "Tai pašā trapecē ∠B = 45°. ∠C?", "atb": ["135"],
         "padoms": "180 − 45."},
        {"jaut": "Četrstūrī ∠A = ∠C = 2∠B un ∠D = 60°. ∠B?", "atb": ["60"],
         "padoms": "5∠B = 300°."},
        {"jaut": "Ārējais leņķis pie A ir 110°. Iekšējais ∠A?",
         "atb": ["70"], "padoms": "Blakusleņķi."},
        {"jaut": "∠A = x, ∠B = x + 20°, ∠C = x + 40°, ∠D = x + 60°. x?",
         "atb": ["60"], "padoms": "4x + 120 = 360."},
    ]),

    Varianti("Pamatojums", [
        {"jaut": "Kāpēc trapecē ∠A + ∠D = 180°?",
         "opcijas": ["Vienpusleņķi pie paralēlām malām", "Krustleņķi",
                     "Blakusleņķi", "Tā ir katrā četrstūrī"],
         "pareizi": 0, "padoms": "AB ∥ CD, AD - krustotājs."},
        {"jaut": "Četrstūrim trīs taisni leņķi. Ceturtais?",
         "opcijas": ["90°", "180°", "45°", "Nevar noteikt"],
         "pareizi": 0, "padoms": "360 − 270."},
        {"jaut": "Kurš apgalvojums par četrstūri ir NEPAREIZS?",
         "opcijas": ["Leņķu summa ir 180°", "Leņķu summa ir 360°",
                     "Pie paralēlām malām vienpusleņķi dod 180°",
                     "Krustleņķi ir vienādi"],
         "pareizi": 0, "padoms": "180° ir trijstūrim."},
    ]),

    Pasaule("Jumta kopne",
            Ievadi("", [
                {"jaut": "Kopne ir trapece ar horizontālām sijām. Slīpā sija "
                         "ar apakšējo veido 35°. Leņķis augšā pie tās pašas "
                         "sijas?",
                 "atb": ["145"], "padoms": "180 − 35."},
                {"jaut": "Otrā slīpā sija arī 35°. Otrs augšējais leņķis?",
                 "atb": ["145"], "padoms": "Tāpat."},
                {"jaut": "Visu četru leņķu summa?", "atb": ["360"],
                 "padoms": "35 + 35 + 145 + 145."},
            ]),
            pavediens="maja",
            konteksts="Kopnes augšējā un apakšējā sija ir paralēlas.",
            kapec="Paralēlas malas dod vienpusleņķus ar summu 180°."),

    Kopsavilkums([
        "Atrodu nezināmos četrstūra leņķus.",
        "Lietoju vienpusleņķus pie paralēlām malām.",
        "Pierakstu katra soļa pamatojumu.",
    ]),

    Majas([
        "Uzzīmē trapeci, izmēri divus leņķus un aprēķini pārējos.",
        "Pārbaudi aprēķinu ar leņķmēru.",
        "Izdomā uzdevumu, kur leņķus atrod ar vienādojumu.",
    ]),
]
