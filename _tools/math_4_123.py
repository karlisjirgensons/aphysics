# -*- coding: utf-8 -*-
"""4. klase, 123. stunda: «Kāda daļa no figūras laukuma?»

Mikrotemata noslēgums. Figūra rūtiņās ir veselais, rūtiņu skaits - tā
lielums. Iekrāsotā daļa ir {iekrāsotās rūtiņas|visas rūtiņas}, pat ja
iekrāsojums nav «smuks» gabals - arī trijstūris vai izkaisītas rūtiņas.
Pusrūtiņas saliek kopā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, figura, kvadrats)

TEMA = "Kāda daļa no figūras laukuma?"

MERKIS = ("Noteiksim daļu no rūtiņās dotas figūras laukuma, arī tad, ja "
          "figūru nevar sadalīt vienādās daļās acīmredzami.")

SATURS = [
    Sakums("Kāda daļa karoga ir iekrāsota?",
           zimejums=kvadrats(4, 4, 4, 1, virsraksts="16 rūtiņas"),
           paraksts="Iekrāsota viena rinda - 4 rūtiņas no 16.",
           fakti=["{4|16} = {1|4} - ceturtdaļa.",
                  "Rūtiņas palīdz saskaitīt daļu precīzi."]),

    Doma("Saskaiti rūtiņas",
         "Daļa no figūras ir {iekrāsotās rūtiņas|visas rūtiņas}; "
         "pusrūtiņas saliek pa divām.",
         soli=[
             "Saskaiti visas figūras rūtiņas - tas ir saucējs.",
             "Saskaiti iekrāsotās rūtiņas - tas ir skaitītājs.",
             "Divas pusrūtiņas = viena rūtiņa.",
             "Ja var, atrodi vienkāršāku pierakstu: {4|16} = {1|4}.",
         ],
         pieze="Nav svarīgi, kur rūtiņas atrodas - svarīgs ir to skaits."),

    Zimejums("Trijstūris taisnstūrī",
             figura([(0, 0), (6, 0), (6, 4), (0, 4), (0, 0), (6, 4)],
                    platums=7, augstums=5, aizpildi=False),
             paskaidro="Trijstūris ir tieši puse no taisnstūra 6 × 4: 12 "
                       "rūtiņas no 24, jeb {1|2}.",
             ievads="Diagonāle sadala taisnstūri divās vienādās daļās."),

    Paraugs("Kāda daļa?",
            uzd="Taisnstūrī 5 × 4 iekrāsotas 6 rūtiņas. Kāda daļa?",
            soli=[
                ("5 · 4 = 20", "Visas rūtiņas."),
                ("{6|20}", "Iekrāsotās no visām."),
            ],
            atbilde="{6|20}"),

    Ievadi("Rūtiņu daļas", [
        {"jaut": "Kvadrāts 4 × 4, iekrāsotas 8 rūtiņas. Kāda daļa? (ar "
                 "saucēju 16)", "atb": ["8/16"], "vieta": "piem., 1/2",
         "padoms": "8 no 16."},
        {"jaut": "Taisnstūris 3 × 5, iekrāsotas 5. Kāda daļa?",
         "atb": ["5/15"], "vieta": "piem., 1/2", "padoms": "5 no 15."},
        {"jaut": "Taisnstūris 6 × 2, iekrāsotas 3 veselas un 2 pusrūtiņas. "
                 "Cik rūtiņu iekrāsots?", "atb": ["4"],
         "padoms": "3 + 1."},
        {"jaut": "Kāda daļa tas ir? (ar saucēju 12)", "atb": ["4/12"],
         "vieta": "piem., 1/2", "padoms": "4 no 12."},
    ]),

    Varianti("Kāda daļa?", [
        {"jaut": "Kvadrāts 2 × 2, iekrāsota 1 rūtiņa.",
         "opcijas": ["{1|4}", "{1|2}", "{1|3}", "{2|4}"], "pareizi": 0,
         "padoms": "1 no 4."},
        {"jaut": "Taisnstūris 10 × 1, iekrāsotas 5.",
         "opcijas": ["{1|2}", "{1|5}", "{5|5}", "{1|10}"], "pareizi": 0,
         "padoms": "{5|10} = {1|2}."},
        {"jaut": "Vai izkaisītas 3 rūtiņas no 12 ir tā pati daļa, kas 3 "
                 "rūtiņas vienā rindā?",
         "opcijas": ["jā, {3|12}", "nē", "atkarīgs no krāsas"],
         "pareizi": 0, "padoms": "Svarīgs skaits, ne vieta."},
    ]),

    Pasaule("Dārza dobes plāns",
            Ievadi("", [
                {"jaut": "Dārzs 8 × 5 m rūtiņās (1 rūtiņa - 1 m²). Cik "
                         "rūtiņu?",
                 "atb": ["40"], "padoms": "8 · 5."},
                {"jaut": "Kartupeļiem {1|2} dārza. Cik rūtiņu?", "atb": ["20"],
                 "padoms": "40 : 2."},
                {"jaut": "Burkāniem {1|8} dārza. Cik rūtiņu?", "atb": ["5"],
                 "padoms": "40 : 8."},
                {"jaut": "Kāda daļa dārza paliek puķēm? Raksti ar saucēju 8.",
                 "atb": ["3/8"], "vieta": "piem., 1/2",
                 "padoms": "{8|8} − {4|8} − {1|8}."},
            ]),
            pavediens="maja",
            konteksts="Dārznieki plāno dobes rūtiņu papīrā - katra rūtiņa ir "
                      "kvadrātmetrs.",
            kapec="Rūtiņas pārvērš dārza daļas skaitļos."),

    Kopsavilkums([
        "Nosaku iekrāsoto daļu no figūras rūtiņās.",
        "Saskaitu pusrūtiņas pa divām.",
        "Zinu, ka svarīgs ir rūtiņu skaits, nevis izvietojums.",
    ]),

    Majas([
        "Uzzīmē 4 × 6 taisnstūri un iekrāso {1|3} trīs dažādos veidos.",
        "Uzzīmē savas istabas plānu rūtiņās: kāda daļa ir gulta?",
        "Paskaidro, kāpēc trijstūris taisnstūrī ir puse.",
    ]),
]
