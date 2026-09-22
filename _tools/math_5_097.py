# -*- coding: utf-8 -*-
"""5. klase, 97. stunda: «Kā saskaitīt jauktus skaitļus?»

Pirmā darbība ar jauktiem skaitļiem, un tā ir vienkāršākā: veselos ar
veselajiem, daļas ar daļām. Vienīgā vieta, kur var paklupt, ir brīdis, kad
daļu summa pati kļūst lielāka par vienu - tad iegūto veselo pieskaita
veselajai daļai, tieši tāpat kā iepriekšējā stundā virknē.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, dala, restis)

TEMA = "Kā saskaitīt jauktus skaitļus?"

MERKIS = ("Iemācīsimies saskaitīt jauktus skaitļus ar vienādiem saucējiem un "
          "saīsināt rezultātu.")

SATURS = [
    Sakums("Divi dēļi vienā garumā",
           zimejums=restis([["1 1/4", "+", "2 1/4", "3 1/2"]],
                           virsraksts="Veselie ar veselajiem"),
           paraksts="1{1|4} m + 2{1|4} m = 3{2|4} m = 3{1|2} m.",
           fakti=["Veselos saskaita atsevišķi no daļām.",
                  "Daļas saskaita savā starpā.",
                  "Beigās rezultātu saīsina."]),

    Doma("Veselos ar veselajiem, daļas ar daļām",
         "Jauktus skaitļus ar vienādiem saucējiem saskaita pa daļām: "
         "atsevišķi veselos, atsevišķi daļas, un rezultātu saīsina.",
         soli=[
             "Saskaiti veselās daļas.",
             "Saskaiti daļas, saucēju atstājot to pašu.",
             "Ja daļu summa ir neīsta, atdali no tās veselo.",
             "Pieskaiti to veselajai daļai.",
             "Saīsini atlikušo daļu, ja tā ir saīsināma.",
         ],
         pieze="1{3|4} + 2{3|4} = 3{6|4} = 3 + 1{2|4} = 4{1|2}. Divi soļi "
               "vienā: vispirms atdala veselo, tad saīsina."),

    Paraugs("1{1|4} + 2{1|4}",
            uzd="Saskaiti divus jauktus skaitļus un saīsini rezultātu.",
            soli=[
                ("1 + 2 = 3",
                 "Veselās daļas."),
                ("{1|4} + {1|4} = {2|4}",
                 "Daļas; saucējs paliek 4."),
                ("3{2|4}",
                 "Starprezultāts."),
                ("{2|4} = {1|2}",
                 "Saīsina daļu."),
                ("3{1|2}",
                 "Galīgā atbilde."),
            ],
            atbilde="1{1|4} + 2{1|4} = 3{1|2}"),

    Ievadi("Saskaiti jauktus skaitļus", [
        {"jaut": "1{1|4} + 2{1|4} = ? Atbildi raksti kā a b/c.",
         "atb": ["3 1/2", "3 2/4"], "padoms": "3{2|4} = 3{1|2}."},
        {"jaut": "2{1|5} + 1{2|5} = ? Atbildi raksti kā a b/c.",
         "atb": ["3 3/5"], "padoms": "Veselie 3, daļas {3|5}."},
        {"jaut": "1{1|3} + 1{1|3} = ? Atbildi raksti kā a b/c.",
         "atb": ["2 2/3"], "padoms": "Veselie 2, daļas {2|3}."},
        {"jaut": "1{3|4} + 2{3|4} = ? Atbildi raksti kā a b/c.",
         "atb": ["4 1/2", "4 2/4"], "padoms": "3{6|4} = 4{2|4}."},
        {"jaut": "2{5|6} + 1{1|6} = ? Ieraksti skaitli.",
         "atb": ["4"], "padoms": "{6|6} = 1."},
        {"jaut": "3{1|8} + 2{3|8} = ? Atbildi raksti kā a b/c.",
         "atb": ["5 1/2", "5 4/8"], "padoms": "{4|8} = {1|2}."},
        {"jaut": "1{2|3} + 2{2|3} = ? Atbildi raksti kā a b/c.",
         "atb": ["4 1/3"], "padoms": "3{4|3} = 4{1|3}."},
        {"jaut": "2{3|10} + 1{1|10} = ? Atbildi raksti kā a b/c.",
         "atb": ["3 2/5", "3 4/10"], "padoms": "{4|10} = {2|5}."},
    ], pamats=4,
        ievads="Vispirms veselie, tad daļas, beigās - saīsināšana."),

    Zimejums("Kad daļas savācas par veselu",
             dala(4, 2, "2/4 = 1/2"),
             paskaidro="Divas ceturtdaļas ir puse; ja to būtu četras, iznāktu "
                       "vesels, un veselā daļa augtu par vienu.",
             ievads="Daļu summa reizēm pati kļūst par veselu skaitli."),

    Varianti("Ko dara ar neīstu daļu summā?", [
        {"jaut": "Kā saskaita jauktus skaitļus ar vienādiem saucējiem?",
         "opcijas": ["Veselos ar veselajiem, daļas ar daļām",
                     "Visu kopā vienā rindā",
                     "Veselos ar daļām",
                     "Saucējus ar saucējiem"],
         "pareizi": 0,
         "padoms": "Divas atsevišķas summas."},
        {"jaut": "Cik ir 1{3|4} + 2{3|4}?",
         "opcijas": ["4{1|2}", "3{6|4}", "3{1|2}", "4{6|4}"],
         "pareizi": 0,
         "padoms": "3{6|4} = 4{2|4} = 4{1|2}."},
        {"jaut": "Ko dara, ja daļu summa ir neīsta?",
         "opcijas": ["Atdala veselo un pieskaita veselajai daļai",
                     "Atstāj kā ir",
                     "Saīsina saucēju",
                     "Atņem vienu"],
         "pareizi": 0,
         "padoms": "{6|4} = 1{2|4}."},
        {"jaut": "Cik ir 2{5|6} + 1{1|6}?",
         "opcijas": ["4", "3{6|6}", "3", "4{1|6}"],
         "pareizi": 0,
         "padoms": "{6|6} = 1."},
        {"jaut": "Kas notiek ar saucēju, saskaitot daļas?",
         "opcijas": ["Paliek tas pats", "Saskaitās", "Reizinās", "Dalās"],
         "pareizi": 0,
         "padoms": "Gabalu lielums nemainās."},
        {"jaut": "Rezultāts iznāca 3{4|8}. Kā to raksta atbildē?",
         "opcijas": ["3{1|2}", "3{4|8}", "3{2|4}", "{28|8}"],
         "pareizi": 0,
         "padoms": "Saīsina līdz galam."},
    ], pamats=4),

    Pasaule("Cik gara sanāk siena?",
            Ievadi("", [
                {"jaut": "Divi dēļi: 1{1|4} m un 2{1|4} m. Cik metru kopā? "
                         "Atbildi raksti kā a b/c.",
                 "atb": ["3 1/2", "3 2/4"], "padoms": "3{2|4}."},
                {"jaut": "Vēl viens dēlis 1{1|2} m. Cik metru kopā ar "
                         "iepriekšējiem? Ieraksti skaitli.",
                 "atb": ["5"], "padoms": "3{1|2} + 1{1|2}."},
                {"jaut": "Divas līstes: 2{3|4} m un 1{3|4} m. Cik metru kopā? "
                         "Atbildi raksti kā a b/c.",
                 "atb": ["4 1/2", "4 2/4"], "padoms": "3{6|4}."},
                {"jaut": "Divas tapetes strēmeles: 2{1|3} m un 1{2|3} m. Cik "
                         "metru kopā? Ieraksti skaitli.",
                 "atb": ["4"], "padoms": "{3|3} = 1."},
            ]),
            pavediens="maja",
            konteksts="Remontā materiālus mēra ar jauktiem skaitļiem, un "
                      "kopgarums jāzina pirms pirkšanas.",
            kapec="Saskaitot pa daļām, kopgarumu var izrēķināt galvā."),

    Kopsavilkums([
        "Saskaitu jauktus skaitļus ar vienādiem saucējiem.",
        "Saskaitu atsevišķi veselos un atsevišķi daļas.",
        "Atdalu veselo, ja daļu summa ir neīsta.",
        "Saīsinu rezultātu līdz galam.",
    ]),

    Majas([
        "Izrēķini 2{2|5} + 3{4|5} un pieraksti visus soļus.",
        "Atrodi divus jauktus skaitļus, kuru summa ir vesels skaitlis.",
        "Izmēri divus priekšmetus mājās un saskaiti to garumus.",
    ]),
]
