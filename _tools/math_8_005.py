# -*- coding: utf-8 -*-
"""8. klase, 5. stunda: «Kas ir absolūtais un relatīvais biežums?»

Absolūtais biežums ir «cik reizes», relatīvais - «kāda daļa no visiem».
Relatīvais ļauj salīdzināt kopas ar dažādu lielumu, un tieši ar to strādā
eksāmena diagrammas - no vienas zināmas daļas atrod visu kopu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, Zimejums, restis, sektori)

TEMA = "Kas ir absolūtais un relatīvais biežums?"

MERKIS = ("Noteiksim absolūto un relatīvo biežumu un attēlosim tos tabulā.")

_TABULA = restis([["atzīme", "skaits", "daļa"],
                  ["10", "2", "0,08"],
                  ["9", "5", "0,2"],
                  ["8", "8", "0,32"],
                  ["7", "6", "0,24"],
                  ["6", "4", "0,16"]])

SATURS = [
    Sakums("Kurā klasē vairāk devītnieku?",
           zimejums=restis([["klase", "9", "skolēni"],
                            ["8.a", "6", "20"],
                            ["8.b", "7", "28"]]),
           paraksts="8.b devītnieku ir vairāk, bet 8.a - lielāka daļa klases.",
           fakti=["6 no 20 ir 30 %.",
                  "7 no 28 ir 25 %.",
                  "Dažāda lieluma kopas salīdzina ar daļām."]),

    Doma("Biežums - cik reizes; relatīvais - kāda daļa",
         "Absolūtais biežums n ir, cik reizes vērtība parādās. Relatīvais "
         "biežums ir {n|N}, kur N ir visu vērtību skaits. To raksta kā "
         "daļu, decimāldaļu vai procentos.",
         soli=[
             "Saskaiti katras vērtības biežumu n.",
             "Pārbaudi: visu biežumu summa ir N.",
             "Relatīvais biežums: {n|N}.",
             "Visu relatīvo biežumu summa ir 1 jeb 100 %.",
         ],
         pieze="Ja zināms relatīvais biežums un n, tad N = n : daļa. Tā "
               "risina eksāmena uzdevumus ar sektoru diagrammu."),

    Paraugs("Biežumu tabula",
            uzd="Kontroldarbā 25 skolēni saņēma atzīmes: 10 - 2, 9 - 5, "
                "8 - 8, 7 - 6, 6 - 4. Atrodi relatīvos biežumus.",
            soli=[
                ("2 + 5 + 8 + 6 + 4 = 25", "N sakrīt ar skolēnu skaitu."),
                ("{2|25} = 0,08; {5|25} = 0,2", "Katru n dala ar 25."),
                ("{8|25} = 0,32; {6|25} = 0,24; {4|25} = 0,16", "Tāpat."),
                ("0,08 + 0,2 + 0,32 + 0,24 + 0,16 = 1", "Pārbaude."),
            ],
            atbilde="8 %, 20 %, 32 %, 24 %, 16 %"),

    Zimejums("Biežumu tabula", _TABULA,
             paskaidro="Kolonna «daļa» kopā dod 1 - tā ir pārbaude."),

    Ievadi("Aizpildi tabulu", [
        {"jaut": "40 metienos sešnieks uzkrita 8 reizes. Relatīvais biežums "
                 "procentos?",
         "atb": ["20", "20 %", "20%"], "padoms": "8 : 40."},
        {"jaut": "Relatīvais biežums ir 0,15, N = 60. Kāds ir absolūtais "
                 "biežums?",
         "atb": ["9"], "padoms": "0,15 · 60."},
        {"jaut": "Tabulā relatīvie biežumi 0,3; 0,25; 0,1 un x. Kāds ir x?",
         "atb": ["0,35", "0.35"], "padoms": "Summa ir 1."},
        {"jaut": "Vērtībai n = 12, relatīvais biežums 24 %. Cik vērtību "
                 "kopā (N)?",
         "atb": ["50"], "padoms": "12 : 0,24."},
        {"jaut": "Atzīmes: 7, 8, 8, 9, 7, 8, 10, 8. Kāds ir atzīmes 8 "
                 "relatīvais biežums? Atbildi raksti kā a/b.",
         "atb": ["{1|2}", "1/2", "4/8", "0,5", "50 %"],
         "padoms": "4 no 8."},
        {"jaut": "Sektors ir 20 % no apļa. Cik grādu?",
         "atb": ["72", "72°"], "padoms": "0,2 · 360."},
    ], pamats=4),

    Varianti("Salīdzini godīgi", [
        {"jaut": "Skolā A 30 no 150 skolēniem sporto, skolā B 40 no 250. "
                 "Kur sporto lielāka daļa?",
         "opcijas": ["A (20 %)", "B (16 %)", "Vienādi", "Nevar noteikt"],
         "pareizi": 0, "padoms": "Salīdzina daļas, ne skaitus."},
        {"jaut": "Visu relatīvo biežumu summa ir...",
         "opcijas": ["1 jeb 100 %", "N", "0", "atkarīga no datiem"],
         "pareizi": 0, "padoms": "Visas daļas kopā - vesels."},
    ]),

    Pasaule("Mūzikas veikala nedēļa",
            Ievadi("", [
                {"jaut": "Diagrammā: ģitāras 40 %. Pārdeva 20 ģitāras. Cik "
                         "instrumentu pārdeva kopā?",
                 "atb": ["50"], "padoms": "20 : 0,4."},
                {"jaut": "Bungas 10 %. Cik bungu pārdeva?",
                 "atb": ["5"], "padoms": "0,1 · 50."},
                {"jaut": "Vijoles 8 %. Cik vijoļu?",
                 "atb": ["4"], "padoms": "0,08 · 50."},
            ]),
            pavediens="veikals",
            konteksts="Veikals redz daļas diagrammā, bet noliktavai vajag "
                      "skaitus - tos atrod no vienas zināmas daļas.",
            kapec="Tieši šāds uzdevums bija 9. klases eksāmenā.",
            zimejums=sektori([("ģitāras", 40), ("taustiņi", 18),
                              ("citi", 14), ("bungas", 10), ("flautas", 10),
                              ("vijoles", 8)])),

    Kopsavilkums([
        "Nosaku absolūto biežumu un pārbaudu summu N.",
        "Aprēķinu relatīvo biežumu kā daļu un procentos.",
        "No relatīvā biežuma atrodu n vai N.",
        "Salīdzinu dažāda lieluma kopas ar relatīvo biežumu.",
    ]),

    Majas([
        "Met monētu 30 reizes un aizpildi biežumu tabulu.",
        "Aprēķini ģerboņa relatīvo biežumu.",
        "Salīdzini ar klasesbiedra rezultātu - kāpēc tie atšķiras?",
    ]),
]
