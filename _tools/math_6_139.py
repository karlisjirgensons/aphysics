# -*- coding: utf-8 -*-
"""6. klase, 139. stunda: «Kā atrisināt nevienādību?»

Pirmā nevienādība. Atbilde nav viens skaitlis, bet visa skaitļu daļa uz
taisnes - un tieši uz taisnes to arī atrod. Formālu likumu te vēl nav, ir
tikai skaitļu taisne un pārbaude.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, taisne)

TEMA = "Kā atrisināt nevienādību?"

MERKIS = ("Noteiksim nezināmo nevienādībā ar negatīviem skaitļiem, "
          "izmantojot skaitļu taisni.")

SATURS = [
    Sakums("Atbilde ir vesela taisnes daļa",
           zimejums=taisne(-6, 4, 2, [(-2, "robeža")]),
           paraksts="Nevienādībai «x ir lielāks par −2» atbilst visi "
                    "skaitļi pa labi no −2.",
           fakti=["Nevienādības atbilde ir skaitļu kopa, ne viens skaitlis.",
                  "Robežskaitlis parasti pats neietilpst atbildē.",
                  "Atbildi pārbauda, ievietojot vienu skaitli no kopas."]),

    Doma("Atrodi robežu, tad izvēlies pusi",
         "Nevienādību risina divos soļos: atrod robežskaitli tā, it kā būtu "
         "vienādība, un tad nosaka, kura taisnes puse der.",
         soli=[
             "Aizstāj nevienādības zīmi ar vienādības zīmi.",
             "Atrodi robežskaitli.",
             "Atzīmē to uz skaitļu taisnes.",
             "Pārbaudi vienu skaitli katrā pusē no robežas.",
             "Pieraksti, kura puse der.",
         ],
         pieze="Pārbaude ar vienu skaitli ir drošākā metode: ja x = 0 der, "
               "tad der visa labā puse; ja neder, tad kreisā. Tā nav "
               "jāatceras nekādi likumi."),

    Paraugs("Atrisini nevienādību",
            uzd="Kuri veseli skaitļi atbilst nosacījumam: x + 3 ir lielāks "
                "par 1?",
            soli=[
                ("Robeža: x + 3 = 1",
                 "Aizstāj ar vienādību."),
                ("x = 1 − 3 = −2",
                 "Robežskaitlis."),
                ("Pārbaude ar x = 0: 0 + 3 = 3, un 3 ir lielāks par 1",
                 "Labā puse der."),
                ("Pārbaude ar x = −5: −5 + 3 = −2, un −2 nav lielāks par 1",
                 "Kreisā puse neder."),
                ("Atbilde: visi skaitļi, kas lielāki par −2",
                 "−1; 0; 1; 2 un tā tālāk."),
            ],
            atbilde="x ir lielāks par −2"),

    Ievadi("Atrodi robežu", [
        {"jaut": "x + 3 = 1. Kāds ir x?",
         "atb": ["-2", "−2"], "padoms": "1 − 3."},
        {"jaut": "Kurš ir mazākais vesels skaitlis, kas lielāks par −2?",
         "atb": ["-1", "−1"], "padoms": "Nākamais pa labi."},
        {"jaut": "x − 4 = −6. Kāds ir x?",
         "atb": ["-2", "−2"], "padoms": "−6 + 4."},
        {"jaut": "x + 5 = 0. Kāds ir x?",
         "atb": ["-5", "−5"], "padoms": "0 − 5."},
        {"jaut": "Kurš ir lielākais vesels skaitlis, kas mazāks par −3?",
         "atb": ["-4", "−4"], "padoms": "Nākamais pa kreisi."},
        {"jaut": "Cik veselu skaitļu ir lielāki par −4 un mazāki par 1?",
         "atb": ["4"], "padoms": "−3; −2; −1; 0."},
    ], pamats=4),

    Varianti("Kura puse der?", [
        {"jaut": "«x ir lielāks par −2.» Kuri skaitļi der?",
         "opcijas": ["Visi pa labi no −2", "Visi pa kreisi no −2",
                     "Tikai −2", "Visi skaitļi"],
         "pareizi": 0,
         "padoms": "Lielāks nozīmē pa labi."},
        {"jaut": "Vai pats robežskaitlis parasti der?",
         "opcijas": ["Nē, ja zīme ir «lielāks par»",
                     "Jā, vienmēr", "Nekad",
                     "Tikai negatīviem"],
         "pareizi": 0,
         "padoms": "«Lielāks par» neieskaita pašu."},
        {"jaut": "Kā pārbaudīt, kura puse der?",
         "opcijas": ["Ievietot vienu skaitli no katras puses",
                     "Ievietot robežskaitli",
                     "Paskatīties uz zīmi", "Nevar pārbaudīt"],
         "pareizi": 0,
         "padoms": "Pārbaude ir drošākā."},
        {"jaut": "«x mazāks par −1.» Kurš skaitlis der?",
         "opcijas": ["−5", "0", "−1", "3"],
         "pareizi": 0,
         "padoms": "Pa kreisi no −1."},
    ], pamats=4),

    Pasaule("Kad ledus ir drošs?",
            Ievadi("", [
                {"jaut": "Ledus ir drošs, ja temperatūra ir zemāka par "
                         "−5 °C. Vai −7 °C der? Raksti «jā» vai «nē».",
                 "atb": ["jā", "ja"], "padoms": "−7 ir mazāks par −5."},
                {"jaut": "Vai −3 °C der?",
                 "atb": ["nē", "ne"], "padoms": "−3 ir lielāks par −5."},
                {"jaut": "Kurš ir lielākais vesels grādu skaitlis, pie kura "
                         "ledus vēl ir drošs?",
                 "atb": ["-6", "−6"], "padoms": "Nākamais zem −5."},
                {"jaut": "Cik veselu grādu vērtību ir starp −10 un −5, "
                         "neieskaitot galus?",
                 "atb": ["4"], "padoms": "−9; −8; −7; −6."},
            ]),
            pavediens="planeta",
            konteksts="Drošības noteikumos robežas nosaka ar nevienādībām - "
                      "«zemāka par», «ne augstāka par».",
            kapec="Atbilde ir visa vērtību kopa, ne viens skaitlis."),

    Zimejums("Robeža un derīgā puse",
             taisne(-6, 4, 2, [(-2, "robeža"), (0, "der"), (2, "der")]),
             paskaidro="Robežskaitlis ir −2. Visi skaitļi pa labi no tā "
                       "atbilst nosacījumam.",
             ievads="Uz taisnes atbildi var iekrāsot."),

    Kopsavilkums([
        "Atrodu nevienādības robežskaitli.",
        "Pārbaudu, kura taisnes puse der.",
        "Pierakstu atbildi kā skaitļu kopu.",
        "Zinu, kad robežskaitlis pats ietilpst atbildē.",
    ]),

    Majas([
        "Atrisini: x + 4 ir lielāks par 1.",
        "Atrisini: x − 3 ir mazāks par −5.",
        "Katram pieraksti trīs skaitļus, kas der.",
    ]),
]
