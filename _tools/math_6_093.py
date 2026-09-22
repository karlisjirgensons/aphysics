# -*- coding: utf-8 -*-
"""6. klase, 93. stunda: «Procenti vai reizes?»

Divas valodas par vienu un to pašu: «par 50 % vairāk» un «pusotru reizi
vairāk». Skolēni tās mēdz sajaukt, jo abās ir skaitlis un vārds «vairāk».
Stunda tās nostāda blakus un liek pārtulkot vienu otrā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, Zimejums,
                         restis)

TEMA = "Procenti vai reizes?"

MERKIS = ("Risināsim uzdevumus, kuros apvienoti procenti un sakarības «tik "
          "reižu vairāk».")

SATURS = [
    Sakums("«Par 50 % vairāk» nav «50 reizes vairāk»",
           zimejums=restis([["+50 %", "+100 %", "+200 %"],
                            ["1,5 reizes", "2 reizes", "3 reizes"]]),
           paraksts="Procentu pieaugums un reizinātājs ir viens un tas pats "
                    "skaitlis divās valodās.",
           fakti=["Par 100 % vairāk nozīmē divas reizes vairāk.",
                  "Par 50 % vairāk nozīmē pusotru reizi vairāk.",
                  "Reizinātājs ir 1 plus procentu daļa."]),

    Doma("Reizinātājs ir 1 plus procenti",
         "«Par p procentiem vairāk» nozīmē reizināt ar (1 + p simtdaļām), "
         "bet «par p procentiem mazāk» - ar (1 − p simtdaļām).",
         soli=[
             "Izlasi, vai runa ir par pieaugumu vai samazinājumu.",
             "Pārvērt procentus decimāldaļā.",
             "Pieskaiti vai atņem to no vieninieka.",
             "Reizini sākotnējo skaitli ar iegūto reizinātāju.",
             "Pārbaudi ar otru ceļu: aprēķini izmaiņu un pieskaiti.",
         ],
         pieze="«Trīs reizes vairāk» nav «par 300 % vairāk», bet «par 200 % "
               "vairāk»: sākotnējais skaitlis jau ir 100 %, un tam pieskaita "
               "vēl 200 %."),

    Slidnis("Procenti un reizes blakus",
            [{"v": "+25 %", "teksts": "reizinātājs 1,25", "josla": 25},
             {"v": "+50 %", "teksts": "reizinātājs 1,5", "josla": 50},
             {"v": "+100 %", "teksts": "reizinātājs 2", "josla": 75},
             {"v": "+200 %", "teksts": "reizinātājs 3", "josla": 100}],
            ievads="Spied soli pa solim: procentu pieaugums un reizinātājs "
                   "aug kopā, bet ar dažādiem skaitļiem."),

    Paraugs("Pārtulko abās valodās",
            uzd="Cena bija 40 €, tā pieauga par 50 %. Cik tā maksā tagad? "
                "Cik reižu tā pieauga?",
            soli=[
                ("50 % no 40 ir 20 €",
                 "Pieaugums eiro."),
                ("40 + 20 = 60 €",
                 "Jaunā cena."),
                ("Reizinātājs: 1 + 0,5 = 1,5",
                 "Otrs ceļš."),
                ("40 · 1,5 = 60 €",
                 "Tā pati atbilde."),
                ("Cena pieauga pusotru reizi",
                 "Nevis 50 reizes."),
            ],
            atbilde="60 €, pieaugums 1,5 reizes"),

    Ievadi("Pārtulko un izrēķini", [
        {"jaut": "Skaitlis 40 pieaug par 50 %. Cik tas ir?",
         "atb": ["60"], "padoms": "40 · 1,5."},
        {"jaut": "Skaitlis 40 pieaug par 100 %. Cik tas ir?",
         "atb": ["80"], "padoms": "40 · 2."},
        {"jaut": "Skaitlis 40 samazinās par 25 %. Cik tas ir?",
         "atb": ["30"], "padoms": "40 · 0,75."},
        {"jaut": "Skaitlis pieaug 3 reizes. Par cik procentiem tas pieaug?",
         "atb": ["200"], "padoms": "300 % − 100 %."},
        {"jaut": "Skaitlis 60 pieaug par 20 %. Cik tas ir?",
         "atb": ["72"], "padoms": "60 · 1,2."},
        {"jaut": "Skaitlis 50 samazinās par 40 %. Cik tas ir?",
         "atb": ["30"], "padoms": "50 · 0,6."},
    ], pamats=4,
        ievads="Reizinātājs ir 1 plus vai mīnus procentu daļa."),

    Varianti("Cik reižu vai cik procentu?", [
        {"jaut": "«Par 100 % vairāk» nozīmē...",
         "opcijas": ["divas reizes vairāk", "simt reizes vairāk",
                     "par 100 vairāk", "tikpat"],
         "pareizi": 0,
         "padoms": "100 % pieskaita sākotnējiem 100 %."},
        {"jaut": "«Divas reizes mazāk» nozīmē...",
         "opcijas": ["par 50 % mazāk", "par 200 % mazāk",
                     "par 2 % mazāk", "par 100 % mazāk"],
         "pareizi": 0,
         "padoms": "Paliek puse."},
        {"jaut": "Reizinātājs pieaugumam par 30 % ir...",
         "opcijas": ["1,3", "0,3", "30", "0,7"],
         "pareizi": 0,
         "padoms": "1 + 0,3."},
        {"jaut": "Reizinātājs samazinājumam par 30 % ir...",
         "opcijas": ["0,7", "1,3", "0,3", "70"],
         "pareizi": 0,
         "padoms": "1 − 0,3."},
    ], pamats=4),

    Pasaule("Kā mainījās rezultāts?",
            Ievadi("", [
                {"jaut": "Pērn komandā bija 20 dalībnieku, tagad par 25 % "
                         "vairāk. Cik ir tagad?",
                 "atb": ["25"], "padoms": "20 · 1,25."},
                {"jaut": "Citā komandā bija 40, tagad par 25 % mazāk. Cik "
                         "ir tagad?",
                 "atb": ["30"], "padoms": "40 · 0,75."},
                {"jaut": "Trešajā komandā skaits dubultojās no 15. Par cik "
                         "procentiem tas pieauga?",
                 "atb": ["100"], "padoms": "Divas reizes."},
                {"jaut": "Cik dalībnieku ir trešajā komandā tagad?",
                 "atb": ["30"], "padoms": "15 · 2."},
            ]),
            pavediens="sports",
            konteksts="Sacensību pārskatā vienu un to pašu izmaiņu raksta "
                      "gan procentos, gan reizēs.",
            kapec="Abas valodas apraksta vienu skaitli - reizinātāju."),

    Zimejums("Divas valodas, viena tabula",
             restis([["−50 %", "−25 %", "+25 %", "+100 %"],
                     ["0,5", "0,75", "1,25", "2"]]),
             paskaidro="Apakšējā rindā ir reizinātājs. Ar to pietiek, lai "
                       "izrēķinātu jauno vērtību vienā darbībā.",
             ievads="Tabulu var lasīt abos virzienos."),

    Kopsavilkums([
        "Pārtulkoju procentu izmaiņu reizinātājā un otrādi.",
        "Zinu, ka «par 100 % vairāk» ir divas reizes vairāk.",
        "Rēķinu jauno vērtību vienā darbībā.",
        "Pārbaudu rezultātu otrā ceļā.",
    ]),

    Majas([
        "Pieraksti reizinātājus pieaugumam par 10 %, 40 % un 75 %.",
        "Atrodi ziņās izmaiņu procentos un pieraksti to reizēs.",
        "Paskaidro, kāpēc «trīs reizes vairāk» ir «par 200 % vairāk».",
    ]),
]
