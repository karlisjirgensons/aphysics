# -*- coding: utf-8 -*-
"""5. klase, 80. stunda: «Kā pieraksta «a pret b»?»

Viena un tā pati doma sadzīvē tiek izteikta piecos veidos: «3 no 5»,
«3 pret 5», «trīs piektdaļas», {3|5} un 3 : 5. Skolēnam tie izskatās pēc
pieciem dažādiem uzdevumiem, tāpēc šī stunda tos saliek blakus un parāda,
ka pārtulkot no viena pieraksta otrā var bez rēķināšanas.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, dala, restis)

TEMA = "Kā pieraksta «a pret b»?"

MERKIS = ("Iemācīsimies dažādos veidos pierakstīt, ka viens skaitlis ir otra "
          "skaitļa daļa.")

SATURS = [
    Sakums("Viena doma, daudz pierakstu",
           zimejums=restis([["3/5", "3:5"]],
                           virsraksts="Trīs no pieciem"),
           paraksts="«3 no 5», «3 pret 5» un {3|5} nozīmē vienu un to pašu.",
           fakti=["Sarunā saka «trīs no pieciem».",
                  "Sportā raksta «3 pret 5».",
                  "Matemātikā to pašu raksta kā daļu."]),

    Doma("Pirmais skaitlis - skaitītājā",
         "Pierakstos «a no b» un «a pret b» pirmais skaitlis nonāk "
         "skaitītājā, otrais - saucējā; tā pati daļa ir arī dalījums a : b.",
         soli=[
             "Nosaki, kurš skaitlis ir gabals un kurš - veselais.",
             "Gabalu raksti skaitītājā, veselo - saucējā.",
             "Izlasi daļu vārdiem: «trīs piektdaļas».",
             "Pieraksti to pašu kā dalījumu a : b.",
             "Saīsini daļu, ja tā ir saīsināma.",
         ],
         pieze="Secība ir svarīga: {3|5} un {5|3} nav viens un tas pats. "
               "«3 pret 5» vienmēr nozīmē {3|5}, tāpat kā «3 no 5»."),

    Paraugs("Pieraksti «7 no 10» visos veidos",
            uzd="Basketbolists trāpīja 7 metienus no 10. Pieraksti to "
                "dažādos veidos.",
            soli=[
                ("Gabals ir 7, veselais 10",
                 "Kurš skaitlis kur."),
                ("{7|10}",
                 "Pieraksts ar daļu."),
                ("7 pret 10",
                 "Tā pati doma sportā."),
                ("7 : 10",
                 "Tā pati daļa kā dalījums."),
                ("«Septiņas desmitdaļas»",
                 "Izlasīts vārdiem."),
            ],
            atbilde="{7|10} = 7 : 10 = «7 no 10»"),

    Ievadi("Pārtulko pierakstu", [
        {"jaut": "«3 no 5» kā daļa. Atbildi raksti kā a/b.",
         "atb": ["3/5"], "padoms": "Pirmais skaitlis skaitītājā."},
        {"jaut": "«7 pret 10» kā daļa. Atbildi raksti kā a/b.",
         "atb": ["7/10"], "padoms": "Pirmais skaitlis skaitītājā."},
        {"jaut": "«4 no 8» kā saīsināta daļa. Atbildi raksti kā a/b.",
         "atb": ["1/2", "4/8"], "padoms": "{4|8} = {1|2}."},
        {"jaut": "«6 pret 9» kā saīsināta daļa. Atbildi raksti kā a/b.",
         "atb": ["2/3", "6/9"], "padoms": "Abus dala ar 3."},
        {"jaut": "«9 no 12» kā saīsināta daļa. Atbildi raksti kā a/b.",
         "atb": ["3/4", "9/12"], "padoms": "Abus dala ar 3."},
        {"jaut": "Kāds ir daļas {2|7} pieraksts kā dalījums? Ieraksti "
                 "skaitītāju.",
         "atb": ["2"], "padoms": "2 : 7."},
        {"jaut": "«15 no 20» kā saīsināta daļa. Atbildi raksti kā a/b.",
         "atb": ["3/4", "15/20"], "padoms": "Abus dala ar 5."},
        {"jaut": "«2 pret 6» kā saīsināta daļa. Atbildi raksti kā a/b.",
         "atb": ["1/3", "2/6"], "padoms": "Abus dala ar 2."},
    ], pamats=4,
        ievads="Pirmais skaitlis vienmēr nonāk skaitītājā."),

    Zimejums("Trīs no pieciem",
             dala(5, 3, "3/5"),
             paskaidro="Josla ir veselais - pieci gabali. Iekrāsotie trīs ir "
                       "tas, ko nozīmē «3 no 5».",
             ievads="Katrs no pieciem pierakstiem apzīmē šo pašu joslu."),

    Varianti("Kurš pieraksts nozīmē to pašu?", [
        {"jaut": "«4 no 9» ir tas pats, kas...",
         "opcijas": ["{4|9}", "{9|4}", "4 · 9", "9 - 4"],
         "pareizi": 0,
         "padoms": "Pirmais skaitlis skaitītājā."},
        {"jaut": "Vai {3|5} un {5|3} nozīmē vienu un to pašu?",
         "opcijas": ["Nē, secība ir svarīga", "Jā", "Tikai sportā",
                     "To nevar zināt"],
         "pareizi": 0,
         "padoms": "Skaitītājs un saucējs nav maināmi vietām."},
        {"jaut": "{3|4} kā dalījums ir...",
         "opcijas": ["3 : 4", "4 : 3", "3 · 4", "4 - 3"],
         "pareizi": 0,
         "padoms": "Skaitītājs dalās ar saucēju."},
        {"jaut": "«6 pret 8» saīsinātā veidā ir...",
         "opcijas": ["{3|4}", "{6|8} nesaīsināts", "{4|3}", "{8|6}"],
         "pareizi": 0,
         "padoms": "Abus dala ar 2."},
        {"jaut": "Kā izlasa {5|8}?",
         "opcijas": ["Piecas astotdaļas", "Astoņas piektdaļas",
                     "Pieci ar astoņi", "Pieci mīnus astoņi"],
         "pareizi": 0,
         "padoms": "Skaitītājs, tad saucēja nosaukums."},
        {"jaut": "Kurš skaitlis ir veselais pierakstā «2 no 7»?",
         "opcijas": ["7", "2", "9", "5"],
         "pareizi": 0,
         "padoms": "Otrais skaitlis."},
    ], pamats=4),

    Pasaule("Cenu zīme un daļa",
            Ievadi("", [
                {"jaut": "No 20 precēm 5 ir atlaidē. Kāda daļa? Atbildi "
                         "raksti kā a/b.",
                 "atb": ["1/4", "5/20"], "padoms": "{5|20}."},
                {"jaut": "No 30 precēm 10 ir atlaidē. Kāda daļa? Atbildi "
                         "raksti kā a/b.",
                 "atb": ["1/3", "10/30"], "padoms": "{10|30}."},
                {"jaut": "No 24 precēm 18 ir atlaidē. Kāda daļa? Atbildi "
                         "raksti kā a/b.",
                 "atb": ["3/4", "18/24"], "padoms": "Abus dala ar 6."},
                {"jaut": "No 50 precēm 20 ir atlaidē. Kāda daļa? Atbildi "
                         "raksti kā a/b.",
                 "atb": ["2/5", "20/50"], "padoms": "Abus dala ar 10."},
            ]),
            pavediens="veikals",
            konteksts="Reklāmā raksta «katra ceturtā prece», bet plauktā ir "
                      "tikai divi skaitļi.",
            kapec="Pārtulkot no viena pieraksta otrā ir ātrāk nekā skaitīt."),

    Kopsavilkums([
        "Pierakstu «a no b» un «a pret b» kā daļu.",
        "Zinu, ka pirmais skaitlis nonāk skaitītājā.",
        "Pierakstu daļu arī kā dalījumu a : b.",
        "Izlasu daļu vārdiem un saīsinu to.",
    ]),

    Majas([
        "Pieraksti «12 no 16» visos veidos un saīsini.",
        "Atrodi reklāmā pierakstu «a no b» un pārraksti to kā daļu.",
        "Paskaidro, kāpēc {2|3} un {3|2} nav viens un tas pats.",
    ]),
]
