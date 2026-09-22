# -*- coding: utf-8 -*-
"""5. klase, 58. stunda: «Kā izskatās pareizs pieraksts?»

Rēķins jau ir zināms, te runa ir par to, kā to uzrakstīt uz papīra. Tas nav
formalitāte: ja pierakstā redzams tikai gatavais rezultāts, ne skolotājs, ne
pats skolēns nevar atrast, kurā vietā aizgāja greizi. Tāpēc te māca pierakstu,
kurā reizinātājs vai dalītājs stāv gan pie skaitītāja, gan pie saucēja.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kā izskatās pareizs pieraksts?"

MERKIS = ("Mācīsimies veidot pierakstu, kurā redzams, ar ko reizināts vai "
          "dalīts gan skaitītājs, gan saucējs.")

SATURS = [
    Sakums("Divi burtnīcas ieraksti",
           zimejums=restis([["2/3", "= ?", "10/15"],
                            ["2/3", "·5", "10/15"]],
                           virsraksts="Augšā trūkst soļa, apakšā tas ir"),
           paraksts="Abās rindās viena atbilde, bet tikai vienā redzams, "
                    "kā tā iegūta.",
           fakti=["No gatavas atbildes kļūdu atrast nevar.",
                  "Pierakstā jābūt redzamam reizinātājam.",
                  "Tas pats attiecas uz dalītāju, saīsinot."]),

    Doma("Pierakstā redz abus locekļus un darbību",
         "Paplašinot vai saīsinot, pieraksta reizinājumu vai dalījumu gan "
         "skaitītājam, gan saucējam - tikai tad pieraksts pierāda rezultātu.",
         soli=[
             "Uzraksti doto daļu.",
             "Liec vienādības zīmi.",
             "Skaitītāja vietā raksti reizinājumu vai dalījumu.",
             "Saucēja vietā raksti to pašu darbību ar to pašu skaitli.",
             "Tikai pēc tam raksti gatavo rezultātu.",
         ],
         pieze="Paplašinot: {2|3} = {2 · 5|3 · 5} = {10|15}. Saīsinot: "
               "{24|30} = {24 : 6|30 : 6} = {4|5}. Abos pierakstos uzreiz "
               "redz, ka abiem locekļiem darīts viens un tas pats."),

    Paraugs("Pieraksti abus soļus",
            uzd="Paplašini {3|4} līdz saucējam 20 un saīsini {24|30} līdz "
                "nesaīsināmai. Pieraksti abus ar pilnu soli.",
            soli=[
                ("{3|4} = {3 · 5|4 · 5}",
                 "Reizinātājs redzams pie abiem locekļiem."),
                ("{3 · 5|4 · 5} = {15|20}",
                 "Tikai tagad - gatavais rezultāts."),
                ("{24|30} = {24 : 6|30 : 6}",
                 "Dalītājs redzams pie abiem locekļiem."),
                ("{24 : 6|30 : 6} = {4|5}",
                 "Nesaīsināmā daļa."),
            ],
            atbilde="{3|4} = {15|20} un {24|30} = {4|5}"),

    Ievadi("Kāds skaitlis stāv abos locekļos?", [
        {"jaut": "{2|7} = {2 · ?|7 · ?} = {8|28}. Kāds ir reizinātājs?",
         "atb": ["4"], "padoms": "8 : 2 vai 28 : 7."},
        {"jaut": "{5|6} = {5 · ?|6 · ?} = {20|24}. Kāds ir reizinātājs?",
         "atb": ["4"], "padoms": "20 : 5."},
        {"jaut": "{18|24} = {18 : ?|24 : ?} = {3|4}. Kāds ir dalītājs?",
         "atb": ["6"], "padoms": "18 : 3."},
        {"jaut": "{35|50} = {35 : ?|50 : ?} = {7|10}. Kāds ir dalītājs?",
         "atb": ["5"], "padoms": "35 : 7."},
        {"jaut": "{4|9} = {4 · ?|9 · ?} = {12|27}. Kāds ir reizinātājs?",
         "atb": ["3"], "padoms": "27 : 9."},
        {"jaut": "{40|60} = {40 : ?|60 : ?} = {2|3}. Kāds ir dalītājs?",
         "atb": ["20"], "padoms": "40 : 2."},
        {"jaut": "{1|8} = {1 · ?|8 · ?} = {9|72}. Kāds ir reizinātājs?",
         "atb": ["9"], "padoms": "72 : 8."},
        {"jaut": "{63|81} = {63 : ?|81 : ?} = {7|9}. Kāds ir dalītājs?",
         "atb": ["9"], "padoms": "63 : 7."},
    ], pamats=4,
        ievads="Vienu un to pašu skaitli meklē abās vietās - citādi "
               "pieraksts nav pareizs."),

    Zimejums("Pilns pieraksts abos virzienos",
             restis([["3/4", "·5", "15/20"],
                     ["24/30", ":6", "4/5"]],
                    virsraksts="Augšā paplašina, apakšā saīsina"),
             paskaidro="Vidējā ailē stāv skaitlis, ar kuru darbojas abi "
                       "locekļi. Bez tā pieraksts ir nepabeigts.",
             ievads="Vienādības vidū vienmēr ir solis, ne tikai atbilde."),

    Varianti("Kur pieraksts ir sabojāts?", [
        {"jaut": "{3|5} = {3 · 4|5} = {12|5}. Kur ir kļūda?",
         "opcijas": ["Saucējs nav reizināts", "Skaitītājs nav reizināts",
                     "Reizinātājs ir nepareizs", "Kļūdas nav"],
         "pareizi": 0,
         "padoms": "Reizināt jāsāk abiem locekļiem."},
        {"jaut": "{20|30} = {20 : 5|30 : 10} = {4|3}. Kur ir kļūda?",
         "opcijas": ["Locekļi dalīti ar dažādiem skaitļiem",
                     "Dalīts ar par lielu skaitli",
                     "Skaitītājs nav dalīts",
                     "Kļūdas nav"],
         "pareizi": 0,
         "padoms": "Dalītājam abās vietās jābūt vienam."},
        {"jaut": "Kāpēc pierakstā raksta arī soli, ne tikai atbildi?",
         "opcijas": ["Lai var atrast, kur radās kļūda",
                     "Lai pieraksts ir garāks",
                     "Lai skolotājs redz darbu",
                     "Tā nav vajadzīgs"],
         "pareizi": 0,
         "padoms": "Solis ir pierādījums."},
        {"jaut": "Kurš pieraksts ir pareizs?",
         "opcijas": ["{1|4} = {1 · 3|4 · 3} = {3|12}",
                     "{1|4} = {1 · 3|4} = {3|4}",
                     "{1|4} = {1|4 · 3} = {1|12}",
                     "{1|4} = {3|12} = {1 · 3|4}"],
         "pareizi": 0,
         "padoms": "Viens skaitlis abās vietās, atbilde beigās."},
        {"jaut": "Saīsinot {45|60}, ko raksta vidū?",
         "opcijas": ["{45 : 15|60 : 15}", "{45 : 15|60}",
                     "{45|60 : 15}", "{45 · 15|60 · 15}"],
         "pareizi": 0,
         "padoms": "Dalītājs pie abiem locekļiem."},
        {"jaut": "Ko pieraksts ar soli ļauj izdarīt ātri?",
         "opcijas": ["Pārbaudīt rezultātu, ejot atpakaļ",
                     "Uzrakstīt vairāk daļu",
                     "Izlaist saīsināšanu",
                     "Neko"],
         "pareizi": 0,
         "padoms": "Reizinājumu var dalīt atpakaļ."},
    ], pamats=4),

    Pasaule("Kā pierakstīt cenas salīdzinājumu?",
            Ievadi("", [
                {"jaut": "Prece atlaidē maksā {3|4} no cenas. Pieraksti to "
                         "ar saucēju 100. Kāds ir skaitītājs?",
                 "atb": ["75"], "padoms": "{3 · 25|4 · 25}."},
                {"jaut": "Cita prece maksā {7|10} no cenas. Pieraksti to ar "
                         "saucēju 100. Kāds ir skaitītājs?",
                 "atb": ["70"], "padoms": "{7 · 10|10 · 10}."},
                {"jaut": "Čekā 45 € no 60 €. Saīsini šo daļu. Atbildi raksti "
                         "kā a/b.",
                 "atb": ["3/4"], "padoms": "{45 : 15|60 : 15}."},
                {"jaut": "Čekā 28 € no 35 €. Saīsini šo daļu. Atbildi raksti "
                         "kā a/b.",
                 "atb": ["4/5"], "padoms": "{28 : 7|35 : 7}."},
            ]),
            pavediens="veikals",
            konteksts="Veikalā rēķinu pārbauda otrs cilvēks, tāpēc pierakstā "
                      "jābūt redzamam katram solim.",
            kapec="Pilns pieraksts ir vienīgais veids, kā parādīt, ka cena "
                  "nav mainīta."),

    Kopsavilkums([
        "Pierakstu paplašināšanu ar reizinātāju pie abiem locekļiem.",
        "Pierakstu saīsināšanu ar dalītāju pie abiem locekļiem.",
        "Atrodu pierakstā vietu, kur pazudis viens no locekļiem.",
        "Skaidroju, kāpēc solis pierakstā ir vajadzīgs.",
    ]),

    Majas([
        "Pieraksti ar pilnu soli: {2|5} ar saucēju 30 un {36|54} saīsinātu.",
        "Atrodi savā burtnīcā pierakstu bez soļa un papildini to.",
        "Uzraksti sabojātu pierakstu draugam un palūdz atrast kļūdu.",
    ]),
]
