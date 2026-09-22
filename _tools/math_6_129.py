# -*- coding: utf-8 -*-
"""6. klase, 129. stunda: «Kā saskaitīt vairākus skaitļus?»

Mikrotemata noslēgums. Kad saskaitāmo ir trīs vai četri, izšķir kārtība:
vispirms sagrupē pozitīvos un negatīvos, tad saskaita divas grupas. Tas ir
ātrāk un drošāk nekā rēķināt no kreisās uz labo.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kā saskaitīt vairākus skaitļus?"

MERKIS = ("Saskaitīsim trīs vai četrus veselus skaitļus, izmantojot "
          "saskaitāmo maiņu vietām.")

SATURS = [
    Sakums("Divas grupas divu darbību vietā",
           zimejums=restis([["+9", "+4", "−6", "−12"],
                            ["+13", "", "−18", ""]]),
           paraksts="Vispirms atsevišķi pozitīvie un negatīvie, tad viena "
                    "darbība: 13 + (−18) = −5.",
           fakti=["Saskaitāmos drīkst mainīt vietām - summa nemainās.",
                  "Ērtāk ir sagrupēt pozitīvos un negatīvos.",
                  "Beigās paliek tikai viena darbība."]),

    Doma("Sagrupē, tad saskaiti divas grupas",
         "Saskaitot vairākus skaitļus, saskaitāmos maina vietām: vispirms "
         "saskaita visus pozitīvos, tad visus negatīvos, un tikai beigās "
         "abas summas.",
         soli=[
             "Pārraksti visus saskaitāmos ar to zīmēm.",
             "Izsvītro pretēju skaitļu pārus, ja tādi ir.",
             "Saskaiti visus pozitīvos.",
             "Saskaiti visus negatīvos.",
             "Saskaiti abas summas.",
         ],
         pieze="Šāda kārtība ir mazāk kļūdaina nekā rēķināšana no kreisās uz "
               "labo: tur zīme mainās pie katra soļa, bet te tikai vienu "
               "reizi."),

    Paraugs("Četri saskaitāmie",
            uzd="Cik ir 9 + (−6) + 4 + (−12)?",
            soli=[
                ("Pozitīvie: 9 un 4",
                 "9 + 4 = 13."),
                ("Negatīvie: −6 un −12",
                 "−6 + (−12) = −18."),
                ("13 + (−18)",
                 "Viena darbība."),
                ("= −5",
                 "18 − 13, zīme mīnus."),
            ],
            atbilde="−5"),

    Ievadi("Saskaiti vairākus", [
        {"jaut": "Cik ir 9 + (−6) + 4 + (−12)?",
         "atb": ["-5", "−5"], "padoms": "13 un −18."},
        {"jaut": "Cik ir −3 + 7 + (−9)?",
         "atb": ["-5", "−5"], "padoms": "7 un −12."},
        {"jaut": "Cik ir 12 + (−5) + (−7)?",
         "atb": ["0"], "padoms": "12 un −12."},
        {"jaut": "Cik ir −4 + (−6) + 15?",
         "atb": ["5"], "padoms": "15 un −10."},
        {"jaut": "Cik ir 8 + (−3) + (−8) + 3?",
         "atb": ["0"], "padoms": "Divi pāri."},
        {"jaut": "Cik ir −10 + 4 + (−2) + 20?",
         "atb": ["12"], "padoms": "24 un −12."},
    ], pamats=4,
        ievads="Vispirms grupē, tikai tad rēķini."),

    Varianti("Kāda kārtība ir ērtāka?", [
        {"jaut": "Saskaitot četrus skaitļus, vispirms izdevīgi...",
         "opcijas": ["sagrupēt pozitīvos un negatīvos",
                     "rēķināt no kreisās uz labo",
                     "saskaitīt moduļus", "sakārtot augošā secībā"],
         "pareizi": 0,
         "padoms": "Divas grupas - viena darbība."},
        {"jaut": "Vai saskaitāmos drīkst mainīt vietām?",
         "opcijas": ["Jā, summa nemainās", "Nē, nekad",
                     "Tikai pozitīvos", "Tikai negatīvos"],
         "pareizi": 0,
         "padoms": "Saskaitīšanas īpašība."},
        {"jaut": "Izteiksmē 5 + (−5) + 8 ērtākais pirmais solis ir...",
         "opcijas": ["izsvītrot pretējo pāri", "saskaitīt 5 + 8",
                     "saskaitīt visu pēc kārtas", "atņemt 8"],
         "pareizi": 0,
         "padoms": "Pāris dod nulli."},
        {"jaut": "Cik ir 6 + (−2) + (−4) + 1?",
         "opcijas": ["1", "−1", "13", "−13"],
         "pareizi": 0,
         "padoms": "7 un −6."},
    ], pamats=4),

    Pasaule("Kāds ir mēneša rezultāts?",
            Ievadi("", [
                {"jaut": "Mēnesī: +250; −80; −120; +40 €. Cik eiro ir "
                         "ienākumi kopā?",
                 "atb": ["290"], "padoms": "250 + 40."},
                {"jaut": "Cik eiro ir izdevumi kopā?",
                 "atb": ["200"], "padoms": "80 + 120."},
                {"jaut": "Kāds ir mēneša rezultāts eiro?",
                 "atb": ["90"], "padoms": "290 − 200."},
                {"jaut": "Ja nākamajā mēnesī izdevumi pieaugtu par 150 €, "
                         "kāds būtu rezultāts?",
                 "atb": ["-60", "−60"], "padoms": "290 − 350."},
            ]),
            pavediens="veikals",
            konteksts="Mēneša budžetu rēķina tieši tā: atsevišķi ienākumi, "
                      "atsevišķi izdevumi, tad starpība.",
            kapec="Divas grupas ir drošāk nekā rinda ar mainīgām zīmēm."),

    Zimejums("Divas grupas, viens rezultāts",
             restis([["ienākumi", "izdevumi", "rezultāts"],
                     ["+290", "−200", "+90"]]),
             paskaidro="Tas pats budžets trijos skaitļos. Rezultāts ir abu "
                       "grupu summa.",
             ievads="Tā izskatās mēneša pārskats."),

    Kopsavilkums([
        "Saskaitu trīs vai četrus skaitļus, tos sagrupējot.",
        "Izmantoju saskaitāmo maiņu vietām.",
        "Izsvītroju pretēju skaitļu pārus.",
        "Beigās veicu tikai vienu darbību starp divām grupām.",
    ]),

    Majas([
        "Izrēķini −7 + 12 + (−5) + 3, vispirms sagrupējot.",
        "Pieraksti savas nedēļas ienākumus un izdevumus divās grupās.",
        "Aprēķini nedēļas rezultātu.",
    ]),
]
