# -*- coding: utf-8 -*-
"""5. klase, 144. stunda: «Kā procentus pierakstīt kā daļu?»

Tagad, kad procents ir saprasts, tam tiek pievienoti abi pārējie pieraksti.
25 %, {1|4} un 0,25 ir viens un tas pats skaitlis, tikai trīs valodās. Tieši
šīs trīs valodas visu atlikušo tematu lieto pārmaiņus, tāpēc pāreja starp
tām jāprot abos virzienos.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kā procentus pierakstīt kā daļu?"

MERKIS = ("Iemācīsimies pierakstīt procentus kā parasto daļu un kā "
          "decimāldaļu.")

SATURS = [
    Sakums("Trīs pieraksti vienam skaitlim",
           zimejums=restis([["25 %", "25/100", "0,25"]],
                           virsraksts="Viens skaitlis, trīs valodas"),
           paraksts="25 % = {25|100} = {1|4} = 0,25.",
           fakti=["Procentu zīme nozīmē saucēju 100.",
                  "Tāpēc procentus uzreiz var uzrakstīt kā daļu.",
                  "Bet daļu ar saucēju 100 - kā decimāldaļu."]),

    Doma("Procentu skaitu raksti skaitītājā",
         "Procentus pieraksta kā daļu ar saucēju 100; to pašu daļu var "
         "saīsināt vai uzrakstīt ar komatu.",
         soli=[
             "Procentu skaitu raksti skaitītājā.",
             "Saucējā raksti 100.",
             "Saīsini daļu, ja tā ir saīsināma.",
             "Decimāldaļu iegūsti, liekot komatu: divi cipari aiz tā.",
             "Pārbaudi: visiem trim pierakstiem jābūt vienādiem.",
         ],
         pieze="1 % = {1|100} = 0,01, tāpēc arī 7 % = 0,07, nevis 0,7. "
               "Šī nulle ir tā pati, kas 131. stundā - divi cipari aiz "
               "komata ir simtdaļas."),

    Paraugs("Pieraksti 25 % trīs veidos",
            uzd="Uzraksti 25 % kā parasto daļu, saīsinātu daļu un "
                "decimāldaļu.",
            soli=[
                ("25 % = {25|100}",
                 "Procentu skaits skaitītājā."),
                ("{25|100} = {1|4}",
                 "Abus locekļus dala ar 25."),
                ("{25|100} = 0,25",
                 "Divi cipari aiz komata."),
                ("25 % = {1|4} = 0,25",
                 "Visi trīs pieraksti vienādi."),
            ],
            atbilde="25 % = {1|4} = 0,25"),

    Ievadi("Pārtulko pierakstu", [
        {"jaut": "25 % kā parastā daļa. Atbildi raksti kā a/b.",
         "atb": ["1/4", "25/100"], "padoms": "{25|100}."},
        {"jaut": "50 % kā parastā daļa. Atbildi raksti kā a/b.",
         "atb": ["1/2", "50/100"], "padoms": "{50|100}."},
        {"jaut": "10 % kā parastā daļa. Atbildi raksti kā a/b.",
         "atb": ["1/10", "10/100"], "padoms": "{10|100}."},
        {"jaut": "25 % kā decimāldaļa. Ieraksti skaitli.",
         "atb": ["0,25"], "padoms": "Divi cipari aiz komata."},
        {"jaut": "7 % kā decimāldaļa. Ieraksti skaitli.",
         "atb": ["0,07"], "padoms": "Vajag nulli."},
        {"jaut": "60 % kā decimāldaļa. Ieraksti skaitli.",
         "atb": ["0,6", "0,60"], "padoms": "{60|100}."},
        {"jaut": "75 % kā parastā daļa. Atbildi raksti kā a/b.",
         "atb": ["3/4", "75/100"], "padoms": "Abus dala ar 25."},
        {"jaut": "20 % kā parastā daļa. Atbildi raksti kā a/b.",
         "atb": ["1/5", "20/100"], "padoms": "Abus dala ar 20."},
    ], pamats=4,
        ievads="Procentu skaits skaitītājā, simts saucējā."),

    Zimejums("Biežāk lietotie pāri",
             restis([["25 %", "50 %", "75 %"],
                     ["1/4", "1/2", "3/4"]],
                    virsraksts="Šos ir vērts zināt no galvas"),
             paskaidro="Trīs biežākās atlaides un trīs biežākās daļas ir "
                       "viens un tas pats. Tos neatceroties, katru reizi "
                       "jārēķina no jauna.",
             ievads="Dažus pārus nav vērts rēķināt katru reizi."),

    Varianti("Kurš pieraksts ir tas pats?", [
        {"jaut": "25 % kā decimāldaļa ir...",
         "opcijas": ["0,25", "2,5", "25,0", "0,025"],
         "pareizi": 0,
         "padoms": "Divi cipari aiz komata."},
        {"jaut": "7 % kā decimāldaļa ir...",
         "opcijas": ["0,07", "0,7", "7,0", "0,007"],
         "pareizi": 0,
         "padoms": "{7|100}."},
        {"jaut": "50 % kā parastā daļa ir...",
         "opcijas": ["{1|2}", "{1|50}", "{50|10}", "{5|100}"],
         "pareizi": 0,
         "padoms": "{50|100}."},
        {"jaut": "Ko nozīmē procentu zīme?",
         "opcijas": ["Saucēju 100", "Saucēju 10", "Reizināšanu",
                     "Dalīšanu ar 2"],
         "pareizi": 0,
         "padoms": "Viena simtdaļa."},
        {"jaut": "75 % kā parastā daļa ir...",
         "opcijas": ["{3|4}", "{7|5}", "{1|75}", "{75|10}"],
         "pareizi": 0,
         "padoms": "{75|100}."},
        {"jaut": "0,6 kā procenti ir...",
         "opcijas": ["60 %", "6 %", "0,6 %", "600 %"],
         "pareizi": 0,
         "padoms": "0,6 = {60|100}."},
    ], pamats=4),

    Pasaule("Kura atlaide ir lielāka?",
            Ievadi("", [
                {"jaut": "Atlaide 25 %. Kāda daļa no cenas tā ir? Atbildi "
                         "raksti kā a/b.",
                 "atb": ["1/4", "25/100"], "padoms": "{25|100}."},
                {"jaut": "Cita veikala atlaide ir {1|5}. Cik procentu tas "
                         "ir?",
                 "atb": ["20"], "padoms": "{20|100}."},
                {"jaut": "Kura atlaide ir lielāka? Ieraksti procentus.",
                 "atb": ["25"], "padoms": "25 % pret 20 %."},
                {"jaut": "Trešā veikala atlaide ir 0,3. Cik procentu tas ir?",
                 "atb": ["30"], "padoms": "0,3 = {30|100}."},
            ]),
            pavediens="veikals",
            konteksts="Viens veikals raksta procentus, otrs daļas, trešais "
                      "skaitli ar komatu.",
            kapec="Salīdzināt var tikai tad, kad visas trīs valodas ir "
                  "vienā."),

    Kopsavilkums([
        "Pierakstu procentus kā daļu ar saucēju 100.",
        "Saīsinu iegūto daļu.",
        "Pierakstu procentus kā decimāldaļu.",
        "Zinu no galvas 25 %, 50 % un 75 % daļas.",
    ]),

    Majas([
        "Pieraksti kā daļas un decimāldaļas 40 %, 5 % un 80 %.",
        "Pieraksti procentos {1|4}, {3|5} un 0,9.",
        "Iemācies no galvas trīs biežākos pārus.",
    ]),
]
