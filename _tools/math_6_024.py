# -*- coding: utf-8 -*-
"""6. klase, 24. stunda: «Kā reizināt bez zīmējuma?»

No modeļa uz algoritmu. Zīmējums bija pierādījums; tagad no tā paliek viena
rinda: skaitītājs reiz skaitītājs, saucējs reiz saucējs. Stunda vingrina
pierakstu, jo tieši tur rodas lielākā daļa kļūdu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, kvadrats)

TEMA = "Kā reizināt bez zīmējuma?"

MERKIS = ("Iemācīsimies sareizināt divas parastās daļas un veidot skaidru "
          "darbības pierakstu.")

SATURS = [
    Sakums("Viena rinda tā vietā, lai zīmētu 100 rūtiņu",
           zimejums=kvadrats(5, 4, 3, 3, paraksts="9 no 20"),
           paraksts="{3|5} · {3|4} = {9|20}. Zīmējums to apstiprina, bet "
                    "rēķins ir ātrāks.",
           fakti=["Reizinot daļas, kopsaucējs nav vajadzīgs.",
                  "Skaitītājus reizina ar skaitītājiem, saucējus ar "
                  "saucējiem."]),

    Doma("Augšu ar augšu, apakšu ar apakšu",
         "Divas daļas reizina pa taisno: skaitītāju reizinājums kļūst par "
         "skaitītāju, saucēju reizinājums - par saucēju.",
         soli=[
             "Pieraksti abas daļas viena aiz otras ar reizināšanas zīmi.",
             "Sareizini skaitītājus un pieraksti tos virs svītras.",
             "Sareizini saucējus un pieraksti tos zem svītras.",
             "Saīsini rezultātu, ja var.",
             "Ja iznāk neīsta daļa, atdali veselās daļas.",
         ],
         pieze="Vesels skaitlis reizināšanā ir daļa ar saucēju 1: "
               "4 = {4|1}. Tad viens un tas pats likums der visiem "
               "gadījumiem."),

    Paraugs("Sareizini divas daļas",
            uzd="Cik ir {3|5} · {3|4}?",
            soli=[
                ("{3 · 3|5 · 4}",
                 "Skaitītājus ar skaitītājiem, saucējus ar saucējiem."),
                ("= {9|20}",
                 "Izrēķina abus reizinājumus."),
                ("9 un 20 kopīgu dalītāju nav",
                 "Saīsināt nevar - atbilde ir gatava."),
                ("Pārbaude: rezultāts ir mazāks par abiem reizinātājiem",
                 "Tā tam jābūt, ja abas daļas ir īstas."),
            ],
            atbilde="{9|20}"),

    Ievadi("Sareizini daļas", [
        {"jaut": "Cik ir {1|2} · {1|3}? Atbildi raksti kā a/b.",
         "atb": ["1/6"], "padoms": "1 · 1 un 2 · 3."},
        {"jaut": "Cik ir {2|3} · {4|5}? Atbildi raksti kā a/b.",
         "atb": ["8/15"], "padoms": "2 · 4 un 3 · 5."},
        {"jaut": "Cik ir {3|7} · {2|5}? Atbildi raksti kā a/b.",
         "atb": ["6/35"], "padoms": "3 · 2 un 7 · 5."},
        {"jaut": "Cik ir {5|6} · {1|2}? Atbildi raksti kā a/b.",
         "atb": ["5/12"], "padoms": "5 · 1 un 6 · 2."},
        {"jaut": "Cik ir {2|9} · {3|4}? Atbildi raksti kā a/b saīsinātā "
                 "veidā.",
         "atb": ["1/6", "6/36"], "padoms": "{6|36} saīsināts ar 6."},
        {"jaut": "Cik ir {4|5} · 3? Atbildi raksti kā a/b.",
         "atb": ["12/5", "2 2/5"], "padoms": "3 = {3|1}."},
    ], pamats=4,
        ievads="Kopsaucējs te nav vajadzīgs - tas ir saskaitīšanas rīks."),

    Varianti("Kur ir kļūda?", [
        {"jaut": "Skolēns rēķina {1|2} · {1|3} = {2|5}. Kas nav labi?",
         "opcijas": ["Viņš saskaitīja, nevis reizināja",
                     "Viņš aizmirsa saīsināt",
                     "Viņš sajauca skaitītāju un saucēju",
                     "Viss ir pareizi"],
         "pareizi": 0,
         "padoms": "Reizinot nemeklē kopsaucēju."},
        {"jaut": "{3|4} · {4|3} ir vienāds ar...",
         "opcijas": ["1", "{7|7}", "{12|7}", "{9|16}"],
         "pareizi": 0,
         "padoms": "{12|12} = 1."},
        {"jaut": "Kā pierakstīt veselu skaitli 5 kā daļu?",
         "opcijas": ["{5|1}", "{1|5}", "{5|5}", "{10|2} tikai"],
         "pareizi": 0,
         "padoms": "Dalot ar vienu, skaitlis nemainās."},
        {"jaut": "Kurā gadījumā reizinājums ir vesels skaitlis?",
         "opcijas": ["Kad skaitītāju reizinājums dalās ar saucēju "
                     "reizinājumu",
                     "Vienmēr", "Nekad", "Kad abas daļas ir vienādas"],
         "pareizi": 0,
         "padoms": "{2|3} · {3|2} = 1."},
    ], pamats=4),

    Zimejums("Pārbaudi rēķinu ar zīmējumu",
             kvadrats(3, 5, 2, 4, paraksts="8 no 15"),
             paskaidro="{2|3} · {4|5} = {8|15}. Rūtiņu ir 15, iekrāsotas 8 - "
                       "tieši tā, kā pasaka rēķins.",
             ievads="Zīmējums paliek kā pārbaudes rīks, ne kā darba veids."),

    Pasaule("Cik daudz no visa tas ir?",
            Ievadi("", [
                {"jaut": "{3|4} klases piedalās sacensībās, no tiem {2|3} ir "
                         "skrējēji. Kāda daļa no klases ir skrējēji? Atbildi "
                         "raksti kā a/b.",
                 "atb": ["1/2", "6/12"], "padoms": "{3|4} · {2|3} = {6|12}."},
                {"jaut": "Klasē ir 24 skolēni. Cik ir skrējēju?",
                 "atb": ["12"], "padoms": "Puse no 24."},
                {"jaut": "No skrējējiem {1|3} skrien garo distanci. Kāda daļa "
                         "no klases tā ir? Atbildi raksti kā a/b.",
                 "atb": ["1/6"], "padoms": "{1|2} · {1|3}."},
                {"jaut": "Cik skolēnu skrien garo distanci?",
                 "atb": ["4"], "padoms": "24 : 6."},
            ]),
            pavediens="sports",
            konteksts="Sacensību protokolā daļas rēķina cita no citas, nevis "
                      "katra no visas klases.",
            kapec="Daļa no daļas ir reizinājums - tāpēc rezultāts vienmēr "
                  "sarūk."),

    Kopsavilkums([
        "Sareizinu divas parastās daļas bez zīmējuma.",
        "Veidoju skaidru pierakstu: skaitītāji virs, saucēji zem svītras.",
        "Pierakstu veselu skaitli kā daļu ar saucēju 1.",
        "Saīsinu rezultātu un atdalu veselās daļas.",
    ]),

    Majas([
        "Izrēķini {2|5} · {5|8} un saīsini rezultātu.",
        "Atrodi divas daļas, kuru reizinājums ir tieši 1.",
        "Uzzīmē kvadrātu, kas pārbauda vienu no taviem rēķiniem.",
    ]),
]
