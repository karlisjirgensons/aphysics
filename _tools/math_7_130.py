# -*- coding: utf-8 -*-
"""7. klase, 130. stunda: «Kas ir vienādojums?»

Vienādojums ir vienādība ar nezināmo. Tā sakne ir skaitlis, ar kuru
vienādība kļūst patiesa. Stunda iemāca pārbaudīt, vai skaitlis ir sakne,
un parāda vienādojumu kā svaru līdzsvaru.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kas ir vienādojums?"

MERKIS = ("Paskaidrosim, kas ir vienādojums un tā sakne, un pārbaudīsim, "
          "vai skaitlis ir sakne.")

SATURS = [
    Sakums("Svari līdzsvarā",
           zimejums=restis([["kreisais kauss", "labais kauss"],
                            ["3 kastītes + 2 kg", "11 kg"],
                            ["3x + 2", "11"]]),
           paraksts="Vienādojums 3x + 2 = 11: cik sver kastīte?",
           fakti=["Svari līdzsvarā - abas puses vienādas.",
                  "Kastītes svars x ir nezināmais.",
                  "x = 3 kg: 9 + 2 = 11 - līdzsvars."]),

    Doma("Vienādojums un sakne",
         "Vienādojums ir vienādība, kurā ir nezināmais. Vienādojuma sakne ir "
         "nezināmā vērtība, ar kuru vienādojums kļūst par patiesu skaitlisku "
         "vienādību.",
         soli=[
             "Kreisā puse - izteiksme pirms «=», labā - pēc.",
             "Lai pārbaudītu skaitli, ievieto to abās pusēs.",
             "Ja vērtības vienādas - skaitlis ir sakne.",
             "Ja atšķiras - nav sakne.",
         ],
         pieze="Izteiksmei nav «=»; vienādojumam ir. 3x + 2 ir izteiksme, "
               "3x + 2 = 11 - vienādojums."),

    Paraugs("Pārbaudi sakni",
            uzd="Vai x = 4 ir vienādojuma 5x − 7 = 2x + 5 sakne?",
            soli=[
                ("Kreisā: 5 · 4 − 7 = 13", "Ievieto."),
                ("Labā: 2 · 4 + 5 = 13", "Ievieto."),
                ("13 = 13 - patiesa vienādība", "Salīdzina."),
            ],
            atbilde="Jā, x = 4 ir sakne."),

    Varianti("Vienādojums vai nē?", [
        {"jaut": "2x + 5 = 17",
         "opcijas": ["Vienādojums", "Izteiksme", "Skaitliska vienādība"],
         "pareizi": 0, "jaukt": False, "padoms": "Ir x un =."},
        {"jaut": "2x + 5",
         "opcijas": ["Vienādojums", "Izteiksme", "Skaitliska vienādība"],
         "pareizi": 1, "jaukt": False, "padoms": "Nav =."},
        {"jaut": "2 · 6 + 5 = 17",
         "opcijas": ["Vienādojums", "Izteiksme", "Skaitliska vienādība"],
         "pareizi": 2, "jaukt": False, "padoms": "Nav nezināmā."},
        {"jaut": "Kurš skaitlis ir sakne vienādojumam x + 9 = 4?",
         "opcijas": ["−5", "5", "13", "−13"],
         "pareizi": 0, "padoms": "−5 + 9 = 4."},
    ], pamats=4),

    Ievadi("Pārbaudi vai atrodi", [
        {"jaut": "Vai x = 3 ir sakne 4x − 1 = 11? Raksti «jā» vai «nē».",
         "atb": ["jā", "ja"], "padoms": "12 − 1 = 11."},
        {"jaut": "Vai x = −2 ir sakne x² = 4?",
         "atb": ["jā", "ja"], "padoms": "(−2)² = 4."},
        {"jaut": "Vai x = 5 ir sakne 2(x − 3) = 6?",
         "atb": ["nē", "ne"], "padoms": "2 · 2 = 4."},
        {"jaut": "Atrodi sakni prātā: x + 15 = 40",
         "atb": ["25"], "padoms": "40 − 15."},
        {"jaut": "Atrodi sakni prātā: 7x = 56",
         "atb": ["8"], "padoms": "56 : 7."},
        {"jaut": "Atrodi sakni prātā: {x|3} = 12",
         "atb": ["36"], "padoms": "12 · 3."},
    ], pamats=4),

    Pasaule("Cik maksā pica?",
            Ievadi("", [
                {"jaut": "3 vienādas picas un 2 € piegāde - kopā 29 €. "
                         "Vienādojums 3x + 2 = 29. Vai x = 9 ir sakne?",
                 "atb": ["jā", "ja"], "padoms": "27 + 2 = 29."},
                {"jaut": "Cik € maksā viena pica?",
                 "atb": ["9"], "padoms": "Sakne."},
                {"jaut": "Ja picas būtu 4, cik € kopā?",
                 "atb": ["38"], "padoms": "36 + 2."},
            ]),
            pavediens="virtuve",
            konteksts="Čekā redz tikai kopsummu - vienādojums atjauno "
                      "vienas preces cenu.",
            kapec="Sakne ir atbilde uz jautājumu «cik?»."),

    Kopsavilkums([
        "Zinu, kas ir vienādojums un tā sakne.",
        "Pārbaudu sakni, ievietojot abās pusēs.",
        "Atšķiru vienādojumu no izteiksmes.",
        "Atrodu vienkāršu sakni prātā.",
    ]),

    Majas([
        "Izdomā 3 vienādojumus ar sakni 5.",
        "Pārbaudi, vai 2 ir sakne 3x − 4 = x.",
        "Pārvērt čeku vienādojumā un atrodi cenu.",
    ]),
]
