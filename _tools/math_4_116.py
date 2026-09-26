# -*- coding: utf-8 -*-
"""4. klase, 116. stunda: «Kāds skaitlis der vienādībā?»

4.5. temata pēdējā stunda pirms PD. Nezināmais vienādībā vai nevienādībā
ar daļām: {3|8} + x = 1, k · {1|4} < 1, {x|6} > {1|2}. Skolēns modelē
situāciju ar joslu vai taisni un atrod vienu vai visas atbildes.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, taisne)

TEMA = "Kāds skaitlis der vienādībā?"

MERKIS = ("Noteiksim nezināmo vienādībā vai nevienādībā ar daļām, "
          "modelējot situāciju.")

SATURS = [
    Sakums("Kuri skaitļi der: {x|6} > {1|2}?",
           zimejums=taisne(0, 1, 1, [(0.5, "3/6"), (4 / 6.0, "4/6"),
                                     (5 / 6.0, "5/6"), (1.0, "6/6")],
                           sikas=6),
           paraksts="Der x = 4, 5, 6 (un vēl lielāki).",
           fakti=["Vienādībai parasti viena atbilde.",
                  "Nevienādībai - bieži vairākas."]),

    Doma("Modelē un pārbaudi",
         "Nezināmo vienādībā atrod ar pretējo darbību; nevienādībā - "
         "pārbauda skaitļus pēc kārtas vai atrod robežu uz taisnes.",
         soli=[
             "Vienādība: {3|8} + x = 1 → x = {8|8} − {3|8} = {5|8}.",
             "Nevienādība: atrod robežu, kur būtu vienādība.",
             "{x|6} = {1|2}, ja x = 3 - tā ir robeža.",
             "{x|6} > {1|2}, ja x > 3: x = 4, 5, 6, ...",
         ],
         pieze="Pārbaudi atbildi, ieliekot to sākotnējā izteiksmē."),

    Paraugs("k · {1|4} < 1",
            uzd="Kuri naturāli skaitļi k der: k · {1|4} < 1?",
            soli=[
                ("k · {1|4} = {k|4}", None),
                ("{k|4} < {4|4}", "1 = {4|4}."),
                ("k < 4 → k = 1, 2, 3", None),
            ],
            atbilde="k = 1, 2, 3"),

    Ievadi("Atrodi nezināmo", [
        {"jaut": "{3|8} + x = 1. x = ?", "atb": ["5/8"],
         "vieta": "piem., 1/2", "padoms": "{8|8} − {3|8}."},
        {"jaut": "{x|10} = {1|2}. x = ?", "atb": ["5"],
         "padoms": "Puse no 10."},
        {"jaut": "Cik naturālu x der: {x|5} < 1?", "atb": ["4"],
         "padoms": "x = 1, 2, 3, 4."},
        {"jaut": "Mazākais naturālais k: k · {1|3} > 2?", "atb": ["7"],
         "padoms": "2 = {6|3}, vajag > 6."},
        {"jaut": "{2|9} + {x|9} = {7|9}. x = ?", "atb": ["5"],
         "padoms": "7 − 2."},
        {"jaut": "Lielākais x: {x|12} < {3|4}?", "atb": ["8"],
         "padoms": "{3|4} = {9|12}."},
    ], pamats=4),

    Varianti("Kurš der?", [
        {"jaut": "Kurš x der: {x|7} > {5|7}?",
         "opcijas": ["6", "5", "4", "3"], "pareizi": 0,
         "padoms": "x > 5."},
        {"jaut": "Kurš x der: 2 · {x|9} = {8|9}?",
         "opcijas": ["4", "8", "2", "6"], "pareizi": 0,
         "padoms": "2 · x = 8."},
        {"jaut": "Cik atbilžu ir vienādībai {x|5} = {3|5}?",
         "opcijas": ["viena", "divas", "bezgalīgi daudz"], "pareizi": 0,
         "padoms": "Tikai x = 3."},
        {"jaut": "Kurš x *neder*: {x|4} < 1?",
         "opcijas": ["4", "1", "2", "3"], "pareizi": 0,
         "padoms": "{4|4} = 1, nevis mazāk."},
    ], pamats=4),

    Pasaule("Ceļojuma rezerves",
            Ievadi("", [
                {"jaut": "Bākā {3|8} degvielas. Cik astotdaļu jāuzpilda līdz "
                         "pilnai?",
                 "atb": ["5"], "padoms": "8 − 3."},
                {"jaut": "Ceļam vajag vairāk nekā {1|2} bākas. Mazākais "
                         "astotdaļu skaits, kas der?",
                 "atb": ["5"], "padoms": "{4|8} ir tieši puse."},
                {"jaut": "Katru stundu patērē {1|8} bākas. Cik stundu var "
                         "braukt ar {6|8}?",
                 "atb": ["6"], "padoms": "6 · {1|8} = {6|8}."},
                {"jaut": "Lielākais stundu skaits, lai patērētu mazāk nekā "
                         "{3|4} bākas?",
                 "atb": ["5"], "padoms": "{3|4} = {6|8}; mazāk - 5."},
            ]),
            pavediens="celojums",
            konteksts="Degvielas mērītājs rāda daļas - un vadītājs rēķina, "
                      "vai pietiks līdz nākamajai stacijai.",
            kapec="Nevienādība atbild uz jautājumu «vai pietiks?»."),

    Kopsavilkums([
        "Atrodu nezināmo vienādībā ar daļām.",
        "Atrodu visus skaitļus, kas der nevienādībā.",
        "Modelēju ar taisni un pārbaudu atbildi.",
        "Esmu gatavs 4.5. temata pārbaudes darbam.",
    ]),

    Majas([
        "Atrodi visus x: {x|10} < {1|2}.",
        "Pavēro degvielas mērītāju auto un uzraksti, kāda daļa bākas pilna.",
        "Atkārto: salīdzināšana, saskaitīšana, reizināšana ar veselu.",
    ], ievads="Nākamajā stundā - pārbaudes darbs par 4.5. tematu."),
]
