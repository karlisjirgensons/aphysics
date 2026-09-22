# -*- coding: utf-8 -*-
"""6. klase, 36. stunda: «Kā kāpināt daļu?»

Kāpināšana daļām nav jauna darbība - tā ir vienādu reizinātāju reizinājums.
Tomēr tieši te rodas priekšstats, kas noder gan tilpumam, gan procentiem:
kāpinot īstu daļu, tā sarūk ļoti ātri.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, dala)

TEMA = "Kā kāpināt daļu?"

MERKIS = ("Iemācīsimies kāpināt parasto daļu un jauktu skaitli, izmantojot "
          "reizināšanu.")

SATURS = [
    Sakums("Papīru nevar pārlocīt septiņas reizes",
           zimejums=dala(8, 1, "1/8"),
           paraksts="Pēc trim locījumiem katra daļa ir {1|8} no sākuma - "
                    "tas ir {1|2} trešajā pakāpē.",
           fakti=["Katrs locījums lapu padara divreiz biezāku un uz pusi "
                  "mazāku.",
                  "Pēc 7 locījumiem biezums aug 128 reizes.",
                  "Tāpēc parasta lapa vairs nelokās."]),

    Doma("Kāpina gan skaitītāju, gan saucēju",
         "Daļu kāpinot, kāpinājumā tiek gan skaitītājs, gan saucējs, jo "
         "kāpināšana ir vienādu daļu reizinājums.",
         soli=[
             "Pieraksti, cik reižu daļa jāreizina pati ar sevi.",
             "Kāpini skaitītāju un saucēju atsevišķi.",
             "Jauktu skaitli vispirms pārveido par neīstu daļu.",
             "Saīsini rezultātu, ja var.",
             "Pārbaudi: īsta daļa kāpinot sarūk, neīsta - aug.",
         ],
         pieze="Pieraksts «daļa otrajā pakāpē» nozīmē divus vienādus "
               "reizinātājus. Tāpēc {2|3} otrajā pakāpē ir {4|9}, nevis "
               "{4|6}: kāpinās arī saucējs."),

    Slidnis("Kas notiek ar katru nākamo pakāpi",
            [{"v": "{1|2} pirmajā pakāpē", "teksts": "= {1|2}",
              "josla": 50, "zim": dala(2, 1)},
             {"v": "{1|2} otrajā pakāpē", "teksts": "= {1|4}",
              "josla": 25, "zim": dala(4, 1)},
             {"v": "{1|2} trešajā pakāpē", "teksts": "= {1|8}",
              "josla": 12, "zim": dala(8, 1)},
             {"v": "{1|2} ceturtajā pakāpē", "teksts": "= {1|16}",
              "josla": 6, "zim": dala(16, 1)}],
            ievads="Spied soli pa solim: katra nākamā pakāpe ir uz pusi "
                   "mazāka par iepriekšējo."),

    Paraugs("Kāpini daļu un jauktu skaitli",
            uzd="Cik ir {2|3} otrajā pakāpē un 1{1|2} otrajā pakāpē?",
            soli=[
                ("{2|3} · {2|3} = {4|9}",
                 "Kāpina abus locekļus."),
                ("1{1|2} = {3|2}",
                 "Jauktais skaitlis kļūst par neīstu daļu."),
                ("{3|2} · {3|2} = {9|4}",
                 "Kāpina abus locekļus."),
                ("{9|4} = 2{1|4}",
                 "Atdala veselās daļas."),
            ],
            atbilde="{4|9} un 2{1|4}"),

    Ievadi("Kāpini daļu", [
        {"jaut": "Cik ir {1|3} otrajā pakāpē? Atbildi raksti kā a/b.",
         "atb": ["1/9"], "padoms": "1 · 1 un 3 · 3."},
        {"jaut": "Cik ir {2|5} otrajā pakāpē? Atbildi raksti kā a/b.",
         "atb": ["4/25"], "padoms": "2 · 2 un 5 · 5."},
        {"jaut": "Cik ir {1|2} trešajā pakāpē? Atbildi raksti kā a/b.",
         "atb": ["1/8"], "padoms": "2 · 2 · 2."},
        {"jaut": "Cik ir {3|4} otrajā pakāpē? Atbildi raksti kā a/b.",
         "atb": ["9/16"], "padoms": "3 · 3 un 4 · 4."},
        {"jaut": "Cik ir 1{1|3} otrajā pakāpē? Atbildi raksti kā a/b.",
         "atb": ["16/9", "1 7/9"], "padoms": "{4|3} · {4|3}."},
        {"jaut": "Cik ir {2|3} trešajā pakāpē? Atbildi raksti kā a/b.",
         "atb": ["8/27"], "padoms": "2 · 2 · 2 un 3 · 3 · 3."},
    ], pamats=4,
        ievads="Kāpinot kāpinās abi locekļi - arī saucējs."),

    Varianti("Aug vai sarūk?", [
        {"jaut": "Kas notiek ar īstu daļu, to kāpinot?",
         "opcijas": ["Tā kļūst mazāka", "Tā kļūst lielāka",
                     "Tā nemainās", "Tā kļūst par veselu skaitli"],
         "pareizi": 0,
         "padoms": "Puse no puses ir ceturtdaļa."},
        {"jaut": "Kas notiek ar jauktu skaitli, to kāpinot?",
         "opcijas": ["Tas kļūst lielāks", "Tas kļūst mazāks",
                     "Tas nemainās", "Tas kļūst par īstu daļu"],
         "pareizi": 0,
         "padoms": "Jaukts skaitlis ir lielāks par 1."},
        {"jaut": "{2|3} otrajā pakāpē ir...",
         "opcijas": ["{4|9}", "{4|6}", "{2|9}", "{4|3}"],
         "pareizi": 0,
         "padoms": "Kāpina arī saucēju."},
        {"jaut": "Ko nozīmē «{1|2} piektajā pakāpē»?",
         "opcijas": ["Pieci vienādi reizinātāji", "{1|2} · 5",
                     "{5|10}", "{1|10}"],
         "pareizi": 0,
         "padoms": "Kāpināšana ir vienādu reizinātāju reizinājums."},
    ], pamats=4),

    Pasaule("Cik paliek pēc katras filtrēšanas?",
            Ievadi("", [
                {"jaut": "Katrs filtrs atstāj {1|2} piesārņojuma. Cik paliek "
                         "pēc diviem filtriem? Atbildi raksti kā a/b.",
                 "atb": ["1/4"], "padoms": "{1|2} otrajā pakāpē."},
                {"jaut": "Cik paliek pēc trim filtriem? Atbildi raksti kā "
                         "a/b.",
                 "atb": ["1/8"], "padoms": "{1|2} trešajā pakāpē."},
                {"jaut": "Cits filtrs atstāj {1|3}. Cik paliek pēc diviem "
                         "tādiem? Atbildi raksti kā a/b.",
                 "atb": ["1/9"], "padoms": "{1|3} otrajā pakāpē."},
                {"jaut": "Sākumā bija 900 daļiņu. Cik paliek pēc diviem "
                         "trešdaļu filtriem?",
                 "atb": ["100"], "padoms": "900 · {1|9}."},
            ]),
            pavediens="planeta",
            konteksts="Ūdens attīrīšanā katrs filtrs atstāj vienu un to pašu "
                      "daļu - tāpēc rezultāts ir pakāpe, ne summa.",
            kapec="Kāpināta īsta daļa sarūk ļoti ātri."),

    Kopsavilkums([
        "Kāpinu parasto daļu, kāpinot gan skaitītāju, gan saucēju.",
        "Pārveidoju jauktu skaitli par neīstu daļu pirms kāpināšanas.",
        "Zinu, ka īsta daļa kāpinot sarūk, bet jaukts skaitlis aug.",
        "Saistu kāpināšanu ar vienādu reizinātāju reizinājumu.",
    ]),

    Majas([
        "Izrēķini {3|5} otrajā pakāpē un 2{1|2} otrajā pakāpē.",
        "Pārloki papīra lapu tik reižu, cik vari, un pieraksti locījumu "
        "skaitu.",
        "Izrēķini, cik liela ir lapas daļa pēc pieciem locījumiem.",
    ]),
]
