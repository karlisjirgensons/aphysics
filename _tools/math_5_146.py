# -*- coding: utf-8 -*-
"""5. klase, 146. stunda: «Puse vai 50 %?»

Stunda, kurā nav jauna rēķina, bet ir jauna brīvība: biežāk lietotās daļas
un procentus drīkst lietot pārmaiņus. «Puse», {1|2}, 0,5 un 50 % ir viens
skaitlis, un prasme izvēlēties ērtāko pierakstu ir tikpat vērtīga kā prasme
rēķināt.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Puse vai 50 %?"

MERKIS = ("Mācīsimies salīdzināt biežāk lietotās daļas un procentus un lietot "
          "tos kā sinonīmus.")

SATURS = [
    Sakums("Viens skaitlis, četri vārdi",
           zimejums=restis([["1/2", "0,5", "50 %"]],
                           virsraksts="Puse"),
           paraksts="«Puse», {1|2}, 0,5 un 50 % nozīmē vienu un to pašu.",
           fakti=["Sarunā saka «puse».",
                  "Veikalā raksta «50 %».",
                  "Kalkulatorā parādās 0,5."]),

    Doma("Izvēlies ērtāko pierakstu",
         "Biežāk lietotās daļas un procentus lieto pārmaiņus; katrā situācijā "
         "izvēlas to pierakstu, ar kuru vieglāk rēķināt.",
         soli=[
             "Atpazīsti, vai skaitlis ir kāds no biežāk lietotajiem.",
             "Pārtulko to pierakstā, kurš uzdevumam ērtāks.",
             "Daļa ir ērta, ja jādala ar mazu skaitli.",
             "Procenti ir ērti, ja jāsalīdzina.",
             "Pārbaudi, vai pārtulkojums ir pareizs.",
         ],
         pieze="Ar {1|4} rēķināt ir vieglāk nekā ar 25 %: pietiek dalīt ar 4. "
               "Bet salīdzināt 25 % un 30 % ir vieglāk nekā {1|4} un "
               "{3|10}."),

    Paraugs("Kurš pieraksts ērtāks?",
            uzd="Jāatrod 25 % no 80 €. Kuru pierakstu izvēlēties?",
            soli=[
                ("25 % = {1|4}",
                 "Biežāk lietotais pāris."),
                ("{1|4} no 80 ir 80 : 4",
                 "Dalīšana ar mazu skaitli."),
                ("80 : 4 = 20",
                 "Rēķins galvā."),
                ("Ar procentiem tas pats būtu garāk",
                 "Tāpēc te ērtāka ir daļa."),
            ],
            atbilde="20 €"),

    Ievadi("Pārtulko ērtākajā pierakstā", [
        {"jaut": "50 % kā parastā daļa. Atbildi raksti kā a/b.",
         "atb": ["1/2", "50/100"], "padoms": "Puse."},
        {"jaut": "{1|4} procentos. Ieraksti skaitli.",
         "atb": ["25"], "padoms": "{25|100}."},
        {"jaut": "{3|4} procentos. Ieraksti skaitli.",
         "atb": ["75"], "padoms": "{75|100}."},
        {"jaut": "20 % kā parastā daļa. Atbildi raksti kā a/b.",
         "atb": ["1/5", "20/100"], "padoms": "{20|100}."},
        {"jaut": "Cik ir 25 % no 80? Ieraksti skaitli.",
         "atb": ["20"], "padoms": "80 : 4."},
        {"jaut": "Cik ir 50 % no 60?",
         "atb": ["30"], "padoms": "60 : 2."},
        {"jaut": "Cik ir 10 % no 90?",
         "atb": ["9"], "padoms": "90 : 10."},
        {"jaut": "Cik ir 75 % no 40?",
         "atb": ["30"], "padoms": "40 : 4 · 3."},
    ], pamats=4,
        ievads="Vispirms izlem, ar kuru pierakstu rēķināt būs vieglāk."),

    Zimejums("Pieci biežāk lietotie skaitļi",
             restis([["10 %", "20 %", "25 %", "50 %", "75 %"],
                     ["1/10", "1/5", "1/4", "1/2", "3/4"]],
                    virsraksts="Augšā procenti, apakšā daļas"),
             paskaidro="Šos piecus pārus lieto tik bieži, ka tos atceras no "
                       "galvas - tieši tāpēc atlaides veikalā ir tieši šādas.",
             ievads="Piecas kolonnas, kas atrisina lielāko daļu uzdevumu."),

    Varianti("Kurš pieraksts ir ērtāks?", [
        {"jaut": "Jāatrod 25 % no 80. Kurš pieraksts ērtāks?",
         "opcijas": ["{1|4}, jo var dalīt ar 4", "25 %, jo tas ir īsāks",
                     "0,25, jo tas ir precīzāks", "Visi vienlīdz"],
         "pareizi": 0,
         "padoms": "Dalīšana ar mazu skaitli."},
        {"jaut": "Jāsalīdzina {1|4} un {3|10}. Kurš pieraksts ērtāks?",
         "opcijas": ["Procenti: 25 % un 30 %", "Daļas", "Decimāldaļas",
                     "Visi vienlīdz"],
         "pareizi": 0,
         "padoms": "Vienāds saucējs."},
        {"jaut": "50 % no 60 ir...",
         "opcijas": ["30", "50", "6", "120"],
         "pareizi": 0,
         "padoms": "Puse."},
        {"jaut": "{1|10} procentos ir...",
         "opcijas": ["10 %", "1 %", "100 %", "0,1 %"],
         "pareizi": 0,
         "padoms": "{10|100}."},
        {"jaut": "Vai «puse» un «50 %» ir viens un tas pats?",
         "opcijas": ["Jā", "Nē", "Tikai naudai", "To nevar zināt"],
         "pareizi": 0,
         "padoms": "Divi vārdi vienam skaitlim."},
        {"jaut": "75 % no 40 ir...",
         "opcijas": ["30", "10", "75", "3"],
         "pareizi": 0,
         "padoms": "{3|4} no 40."},
    ], pamats=4),

    Pasaule("Kura reklāma sola vairāk?",
            Ievadi("", [
                {"jaut": "Viens veikals sola «puse cenas», otrs «40 %» "
                         "atlaidi. Cik procentu ir puse?",
                 "atb": ["50"], "padoms": "{1|2} = {50|100}."},
                {"jaut": "Kura atlaide ir lielāka? Ieraksti procentus.",
                 "atb": ["50"], "padoms": "50 > 40."},
                {"jaut": "Trešais sola atlaidi {1|4}. Cik procentu tas ir?",
                 "atb": ["25"], "padoms": "{25|100}."},
                {"jaut": "Prece maksā 80 €, atlaide 25 %. Cik eiro ir "
                         "atlaide?",
                 "atb": ["20"], "padoms": "80 : 4."},
            ]),
            pavediens="veikals",
            konteksts="Reklāmas raksta dažādi tieši tāpēc, lai atlaides "
                      "būtu grūtāk salīdzināt.",
            kapec="Pārtulkojot visas vienā pierakstā, salīdzinājums ir "
                  "acīmredzams."),

    Kopsavilkums([
        "Zinu, ka {1|2}, 0,5 un 50 % ir viens skaitlis.",
        "Pārtulkoju biežāk lietotās daļas procentos un atpakaļ.",
        "Izvēlos pierakstu, ar kuru rēķināt ir vieglāk.",
        "Atceros piecus biežāk lietotos pārus no galvas.",
    ]),

    Majas([
        "Uzraksti piecus biežāk lietotos pārus no galvas.",
        "Aprēķini 25 % no 120 un 50 % no 90.",
        "Atrodi reklāmu, kurā atlaide rakstīta kā daļa.",
    ]),
]
