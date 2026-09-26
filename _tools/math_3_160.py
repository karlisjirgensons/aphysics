# -*- coding: utf-8 -*-
"""3. klase, 160. stunda: «Kā uzbūvēt modeli no kociņiem?»

Mikrotemata noslēgums ir praktisks darbs: skolēns pats izvēlas, cik un cik
garus kociņus vajag, un tikai tad būvē. Materiālu saraksts ir tā pati
šķautņu summa, tikai pierakstīta pa garumiem.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         restis)

TEMA = "Kā uzbūvēt modeli no kociņiem?"

MERKIS = ("Veidosim taisnstūru skaldni un piramīdu no kociņiem, izvēloties "
          "vajadzīgos garumus.")

SATURS = [
    Sakums("Cik kociņu vajag kastes modelim?",
           zimejums=restis([["garums", "cik gabalu"],
                            ["5 cm", 4],
                            ["4 cm", 4],
                            ["3 cm", 4]],
                           "materiālu saraksts"),
           paraksts="Katram izmēram četri kociņi - kopā divpadsmit.",
           fakti=["Kvadra modelim vajag 12 kociņus trijos garumos.",
                  "Virsotnēs vajag 8 savienojumus."]),

    Doma("Vispirms saraksts, tad būve",
         "Uzraksti, cik kociņu un kāda garuma vajag, un tikai tad sāc "
         "salikt.",
         soli=[
             "Izvēlies modeļa izmērus: a, b un c.",
             "Katram izmēram pieraksti 4 kociņus.",
             "Saskaiti savienojumus - tik, cik virsotņu.",
             "Saliec vispirms apakšu, tad stāvus, tad augšu.",
         ],
         pieze="Piramīdai saraksts ir cits: četri vienāda garuma kociņi "
               "pamatam un četri slīpie uz virsotni."),

    Petijums("Uzbūvē abus modeļus",
             vajag="salmiņi vai kociņi, plastilīns un lineāls",
             soli=[
                 "Sagriez 4 kociņus pa 5 cm, 4 pa 4 cm un 4 pa 3 cm.",
                 "Saliec apakšējo taisnstūri, tad četrus stāvus kociņus.",
                 "Pabeidz ar augšējo taisnstūri.",
                 "No 8 kociņiem saliec arī četrstūra piramīdu.",
             ],
             secinajums="Kvadram vajag 12 kociņus un 8 savienojumus, "
                        "piramīdai - 8 kociņus un 5 savienojumus."),

    Paraugs("Cik kociņu vajag?",
            uzd="Kvadra modelim izmēri ir 5, 4 un 3 cm. Cik un kādi kociņi "
                "vajadzīgi?",
            soli=[
                ("4 kociņi pa 5 cm",
                 "Garums atkārtojas četras reizes."),
                ("4 kociņi pa 4 cm un 4 pa 3 cm",
                 "Tāpat platums un augstums."),
                ("Kopā 12 kociņi, 48 cm",
                 "Un 8 savienojumi virsotnēs."),
            ],
            atbilde="12 kociņi, kopā 48 cm"),

    Ievadi("Materiālu saraksts", [
        {"jaut": "Cik kociņu vajag kvadra modelim?", "atb": ["12"],
         "padoms": "12 šķautnes."},
        {"jaut": "Cik savienojumu vajag kvadra modelim?", "atb": ["8"],
         "padoms": "8 virsotnes."},
        {"jaut": "Cik kociņu vajag četrstūra piramīdai?", "atb": ["8"],
         "padoms": "4 pamatā un 4 slīpie."},
        {"jaut": "Cik savienojumu vajag piramīdai?", "atb": ["5"],
         "padoms": "4 pamatā un 1 augšā."},
        {"jaut": "Cik centimetru kociņu vajag kubam ar malu 6 cm?",
         "atb": ["72"], "padoms": "12 · 6."},
        {"jaut": "Cik kociņu vajag trim kvadra modeļiem?", "atb": ["36"],
         "padoms": "3 · 12."},
    ], pamats=4),

    Zimejums("Piramīdas saraksts",
             restis([["daļa", "cik gabalu"],
                     ["pamata malas", 4],
                     ["slīpās šķautnes", 4],
                     ["savienojumi", 5]],
                    "četrstūra piramīda"),
             paskaidro="Piramīdai ir mazāk detaļu nekā kvadram, bet slīpās "
                       "šķautnes ir garākas par pamata malām.",
             ievads="Otra modeļa saraksts."),

    Varianti("Cik detaļu vajag?", [
        {"jaut": "Cik kociņu vajag kuba modelim?",
         "opcijas": ["12", "6", "8", "4"],
         "pareizi": 0, "padoms": "Tik, cik šķautņu."},
        {"jaut": "Cik dažādu garumu vajag kvadra modelim?",
         "opcijas": ["3", "1", "12", "6"],
         "pareizi": 0, "padoms": "Garums, platums, augstums."},
        {"jaut": "Cik dažādu garumu vajag kuba modelim?",
         "opcijas": ["1", "3", "2", "12"],
         "pareizi": 0, "padoms": "Visas malas vienādas."},
        {"jaut": "Ar ko sākt būvi?",
         "opcijas": ["Ar apakšējo taisnstūri", "Ar augšu",
                     "Ar stāvajiem kociņiem", "Vienalga"],
         "pareizi": 0, "padoms": "Pamats notur visu pārējo."},
    ], pamats=4),

    Pasaule("Cik materiāla vajag izstādei?",
            Ievadi("", [
                {"jaut": "Vienam modelim 12 kociņi. Cik vajag 10 modeļiem?",
                 "atb": ["120"], "padoms": "10 · 12."},
                {"jaut": "Cik savienojumu vajag 10 modeļiem?", "atb": ["80"],
                 "padoms": "10 · 8."},
                {"jaut": "Viens modelis prasa 48 cm kociņu. Cik centimetru "
                         "vajag 10 modeļiem?",
                 "atb": ["480"], "padoms": "10 · 48."},
                {"jaut": "Cik metru tas ir? Raksti ar komatu.",
                 "atb": ["4,8", "4.8"], "padoms": "480 : 100."},
            ]),
            pavediens="tehnika",
            konteksts="Izstādes maketiem materiālu pasūta pēc saraksta - "
                      "gluži tāpat, kā tu to dari savam modelim.",
            kapec="Saraksts pasaka, cik materiāla pirkt, pirms sākas darbs."),

    Kopsavilkums([
        "Sastādu materiālu sarakstu modelim.",
        "Zinu, cik kociņu un savienojumu vajag kvadram un piramīdai.",
        "Būvēju modeli no apakšas uz augšu.",
        "Izrēķinu materiāla kopgarumu.",
    ]),

    Majas([
        "Uzbūvē kuba modeli no salmiņiem un plastilīna.",
        "Izrēķini, cik centimetru salmiņu tam vajadzēja.",
        "Uzbūvē arī piramīdas modeli un salīdzini detaļu skaitu.",
    ]),
]
