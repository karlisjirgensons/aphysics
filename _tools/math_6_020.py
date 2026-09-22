# -*- coding: utf-8 -*-
"""6. klase, 20. stunda: «Kad daļu izdevīgi paplašināt?»

Šī ir stunda par izvēli, nevis par jaunu darbību. Paplašināšana daļu
nemaina, bet padara to dalāmu - un tieši tāpēc to lieto tad, kad skaitītājs
ar dalītāju nedalās.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, dala)

TEMA = "Kad daļu izdevīgi paplašināt?"

MERKIS = ("Skaidrosim, kāpēc, dalot daļu ar veselu skaitli, to dažkārt "
          "vispirms paplašina.")

SATURS = [
    Sakums("Tā pati daļa, tikai sīkākos gabalos",
           zimejums=dala(4, 3, "3/4"),
           paraksts="{3|4} un {6|8} ir viena un tā pati daļa - otrajā tikai "
                    "gabali ir uz pusi mazāki.",
           fakti=["Daļas pamatīpašība: abus locekļus drīkst reizināt ar "
                  "vienu skaitli.",
                  "Vērtība nemainās, bet skaitītājs kļūst dalāms."]),

    Doma("Paplašini tā, lai skaitītājs dalītos",
         "Ja skaitītājs ar dalītāju nedalās, daļu paplašina tieši ar to "
         "dalītāju - tad dalīšana sanāk vienā solī.",
         soli=[
             "Pārbaudi, vai skaitītājs dalās ar dalītāju.",
             "Ja nedalās, reizini abus daļas locekļus ar dalītāju.",
             "Tagad izdali skaitītāju ar dalītāju.",
             "Saīsini, ja rezultātu var padarīt vienkāršāku.",
             "Pārbaudi ar reizināšanu.",
         ],
         pieze="{2|5} : 3 - skaitītājs 2 ar 3 nedalās. Paplašina: "
               "{2|5} = {6|15}. Tagad {6 : 3|15} = {2|15}. Tas pats, kas "
               "reizināt saucēju, bet solis ir redzams."),

    Paraugs("Paplašini un tad dali",
            uzd="Cik ir {3|7} : 2?",
            soli=[
                ("3 ar 2 nedalās",
                 "Tāpēc tiešais ceļš neder."),
                ("{3|7} = {3 · 2|7 · 2} = {6|14}",
                 "Daļas pamatīpašība: vērtība nemainās."),
                ("{6 : 2|14} = {3|14}",
                 "Tagad skaitītājs dalās."),
                ("Pārbaude: {3|14} · 2 = {6|14} = {3|7}",
                 "Reizināšana atgriež sākotnējo daļu."),
            ],
            atbilde="{3|14}"),

    Ievadi("Paplašini un izdali", [
        {"jaut": "Cik ir {3|5} : 2? Atbildi raksti kā a/b.",
         "atb": ["3/10"], "padoms": "Paplašini ar 2: {6|10}."},
        {"jaut": "Cik ir {2|7} : 3? Atbildi raksti kā a/b.",
         "atb": ["2/21"], "padoms": "Paplašini ar 3: {6|21}."},
        {"jaut": "Cik ir {5|6} : 2? Atbildi raksti kā a/b.",
         "atb": ["5/12"], "padoms": "Paplašini ar 2: {10|12}."},
        {"jaut": "Ar kādu skaitli paplašināt {4|9}, lai to varētu dalīt "
                 "ar 5?",
         "atb": ["5"], "padoms": "Vienmēr ar pašu dalītāju."},
        {"jaut": "Cik ir {7|8} : 3? Atbildi raksti kā a/b.",
         "atb": ["7/24"], "padoms": "{21|24} : 3."},
        {"jaut": "Cik ir {9|10} : 6? Atbildi raksti kā a/b.",
         "atb": ["3/20", "9/60"], "padoms": "{9|60} saīsināts ar 3."},
    ], pamats=4,
        ievads="Paplašināšana nemaina daļas vērtību - tā tikai sagatavo "
               "dalīšanu."),

    Zimejums("Viena daļa, divi pieraksti",
             dala(8, 6, "6/8"),
             paskaidro="{6|8} ir tas pats, kas {3|4}: iekrāsotais laukums "
                       "ir tāds pats, mainījies tikai gabalu skaits.",
             ievads="Paplašinot daļu, iekrāsotā daļa nepaliek ne lielāka, "
                    "ne mazāka."),

    Varianti("Vai daļa mainījās?", [
        {"jaut": "{2|3} paplašināja par {8|12}. Kas notika ar vērtību?",
         "opcijas": ["Tā nemainījās", "Tā kļuva četras reizes lielāka",
                     "Tā kļuva mazāka", "Tā kļuva par veselu skaitli"],
         "pareizi": 0,
         "padoms": "Abi locekļi reizināti ar vienu un to pašu skaitli."},
        {"jaut": "Kad paplašināšana *nav* vajadzīga?",
         "opcijas": ["Kad skaitītājs jau dalās ar dalītāju",
                     "Kad saucējs ir pāra skaitlis",
                     "Kad daļa ir īsta", "Nekad"],
         "pareizi": 0,
         "padoms": "{6|7} : 3 sanāk uzreiz."},
        {"jaut": "Kurš pieraksts ir vienāds ar {3|5}?",
         "opcijas": ["{12|20}", "{6|15}", "{3|10}", "{8|10}"],
         "pareizi": 0,
         "padoms": "Abus locekļus reizina ar 4."},
        {"jaut": "Kāpēc paplašinot drīkst reizināt abus locekļus?",
         "opcijas": ["Tā ir daļas pamatīpašība",
                     "Tas ir tikai paradums",
                     "Tā ir atļauts tikai saucējam",
                     "Tas maina daļu, bet nedaudz"],
         "pareizi": 0,
         "padoms": "Reizinot ar {n|n}, reizina ar vieninieku."},
    ], pamats=4),

    Pasaule("Kā sadalīt materiālu bez atlikuma?",
            Ievadi("", [
                {"jaut": "{3|4} m auduma sadala 2 vienādās daļās. Cik metru "
                         "ir vienā? Atbildi raksti kā a/b.",
                 "atb": ["3/8"], "padoms": "{6|8} : 2."},
                {"jaut": "{2|3} kg krāsas sadala 4 traukos. Cik kg ir vienā? "
                         "Atbildi raksti kā a/b.",
                 "atb": ["1/6", "2/12"], "padoms": "{8|12} : 4 = {2|12}."},
                {"jaut": "{5|8} l laka sadala 5 daļās. Cik litru ir vienā? "
                         "Atbildi raksti kā a/b.",
                 "atb": ["1/8"], "padoms": "Skaitītājs dalās uzreiz."},
                {"jaut": "{7|10} kg javas sadala 2 spaiņos. Cik kg ir vienā? "
                         "Atbildi raksti kā a/b.",
                 "atb": ["7/20"], "padoms": "{14|20} : 2."},
            ]),
            pavediens="maja",
            konteksts="Remontā materiālu dala precīzi: pāri palikušo "
                      "iepakojumu atpakaļ salikt nevar.",
            kapec="Paplašināšana ļauj dalīt arī tad, kad skaitļi «neiet "
                  "kopā»."),

    Kopsavilkums([
        "Zinu daļas pamatīpašību un lietoju to apzināti.",
        "Paplašinu daļu tad, kad skaitītājs ar dalītāju nedalās.",
        "Izvēlos paplašinātāju - to pašu dalītāju.",
        "Pārbaudu, vai daļas vērtība nav mainījusies.",
    ]),

    Majas([
        "Pieraksti {3|4} trīs dažādos veidos, paplašinot to.",
        "Izrēķini {5|7} : 4, izmantojot paplašināšanu.",
        "Izdomā daļu, kuru ar 3 var dalīt bez paplašināšanas.",
    ]),
]
