# -*- coding: utf-8 -*-
"""6. klase, 41. stunda: «Cik ciparu būs aiz komata?»

Viens noteikums, kas atbrīvo no domāšanas par komatu visā turpmākajā
rēķināšanā. Svarīgi, lai skolēns to nevis iegaumē, bet atklāj pats -
saskaitot ciparus vairākos piemēros.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti)

TEMA = "Cik ciparu būs aiz komata?"

MERKIS = ("Secināsim, cik ciparu reizinājumā ir aiz komata, un pamatosim "
          "šo likumu.")

SATURS = [
    Sakums("Komata vietu var pateikt, vēl nerēķinot",
           fakti=["0,4 · 0,7 = 0,28 - viens un viens cipars dod divus.",
                  "0,25 · 0,4 = 0,100 - divi un viens cipars dod trīs.",
                  "Ciparu skaits aiz komata vienmēr ir abu summa."]),

    Doma("Saskaiti ciparus aiz komata",
         "Reizinājumā aiz komata ir tik ciparu, cik tie kopā ir abos "
         "reizinātājos - jo saucēji sareizinās.",
         soli=[
             "Saskaiti ciparus aiz komata pirmajā reizinātājā.",
             "Saskaiti tos otrajā.",
             "Saskaiti abus skaitļus - tik ciparu būs rezultātā.",
             "Sareizini skaitļus bez komata.",
             "Atskaiti no labās puses tik ciparu, cik ieguvi, un liec "
             "komatu.",
         ],
         pieze="Kāpēc tā? 0,4 = {4|10} un 0,7 = {7|10}; to reizinājums ir "
               "{28|100}. Saucējs kļūst 100, tāpēc aiz komata ir divi "
               "cipari."),

    Paraugs("Vispirms cipari, tad rēķins",
            uzd="Cik ir 1,25 · 0,4?",
            soli=[
                ("1,25 - divi cipari; 0,4 - viens",
                 "Kopā trīs cipari aiz komata."),
                ("125 · 4 = 500",
                 "Reizina bez komata."),
                ("0,500",
                 "Atskaita trīs ciparus no labās puses."),
                ("= 0,5",
                 "Nulles beigās drīkst nerakstīt."),
            ],
            atbilde="0,5"),

    Ievadi("Cik ciparu un cik iznāk?", [
        {"jaut": "Cik ciparu aiz komata būs reizinājumā 0,3 · 0,2?",
         "atb": ["2"], "padoms": "1 + 1."},
        {"jaut": "Cik ir 0,3 · 0,2?",
         "atb": ["0,06", "0.06"], "padoms": "3 · 2 = 6; divi cipari."},
        {"jaut": "Cik ciparu aiz komata būs reizinājumā 2,5 · 0,04?",
         "atb": ["3"], "padoms": "1 + 2."},
        {"jaut": "Cik ir 2,5 · 0,04?",
         "atb": ["0,1", "0.1", "0,100"], "padoms": "25 · 4 = 100."},
        {"jaut": "Cik ir 1,2 · 0,5?",
         "atb": ["0,6", "0.6"], "padoms": "12 · 5 = 60; divi cipari."},
        {"jaut": "Cik ir 0,05 · 0,05?",
         "atb": ["0,0025", "0.0025"], "padoms": "5 · 5 = 25; četri cipari."},
    ], pamats=4,
        ievads="Vispirms pasaki ciparu skaitu, tikai tad rēķini."),

    Petijums("Atklāj likumu pats",
             vajag="burtnīca un kalkulators",
             soli=[
                 "Izrēķini ar kalkulatoru 0,2 · 0,3; 0,25 · 0,2; 1,5 · 0,04.",
                 "Pieraksti katram reizinātājam ciparu skaitu aiz komata.",
                 "Pieraksti rezultāta ciparu skaitu aiz komata.",
                 "Salīdzini visas trīs rindas un formulē likumu.",
             ],
             secinajums="Rezultāta ciparu skaits aiz komata ir abu "
                        "reizinātāju ciparu skaitu summa - vienmēr."),

    Varianti("Kur pazuda komats?", [
        {"jaut": "0,6 · 0,5 skolēns ieguva 3. Kas nav labi?",
         "opcijas": ["Aizmirsts komats: jābūt 0,30",
                     "Nepareizi sareizināts", "Jābūt 30",
                     "Viss ir pareizi"],
         "pareizi": 0,
         "padoms": "Divi cipari aiz komata."},
        {"jaut": "Cik ciparu aiz komata ir 0,125 · 0,8 reizinājumā?",
         "opcijas": ["4", "2", "3", "1"],
         "pareizi": 0,
         "padoms": "3 + 1."},
        {"jaut": "1,5 · 2 rezultātā aiz komata ir...",
         "opcijas": ["viens cipars", "divi cipari", "neviena",
                     "trīs cipari"],
         "pareizi": 0,
         "padoms": "2 ir vesels skaitlis - nulle ciparu."},
        {"jaut": "Kāpēc likums strādā?",
         "opcijas": ["Jo saucēji 10, 100 un 1000 sareizinās",
                     "Jo tā ir pieņemts",
                     "Jo komats vienmēr ir vidū",
                     "Tas strādā tikai dažreiz"],
         "pareizi": 0,
         "padoms": "Decimāldaļa ir daļa ar saucēju 10, 100 vai 1000."},
    ], pamats=4),

    Pasaule("Cik maksā viena detaļa?",
            Ievadi("", [
                {"jaut": "Detaļas masa ir 0,25 kg. Cik kg sver 12 detaļas?",
                 "atb": ["3"], "padoms": "12 · 25 = 300; divi cipari."},
                {"jaut": "Viens metrs stieples sver 0,08 kg. Cik kg sver "
                         "2,5 m?",
                 "atb": ["0,2", "0.2"], "padoms": "8 · 25 = 200; trīs "
                                                  "cipari."},
                {"jaut": "Skrūve maksā 0,15 €. Cik eiro maksā 20 skrūves?",
                 "atb": ["3"], "padoms": "15 · 20 = 300."},
                {"jaut": "Lentes metrs maksā 1,2 €. Cik eiro maksā 0,5 m?",
                 "atb": ["0,6", "0.6"], "padoms": "12 · 5 = 60; divi "
                                                  "cipari."},
            ]),
            pavediens="tehnika",
            konteksts="Darbnīcā masas un cenas ir decimāldaļas, tāpēc komata "
                      "vieta nosaka, vai kļūda ir desmitkārtīga.",
            kapec="Ciparu skaitīšana ir ātrākā pārbaude, kāda vien ir."),

    Kopsavilkums([
        "Nosaku ciparu skaitu aiz komata pirms reizināšanas.",
        "Reizinu skaitļus bez komata un ieliku komatu beigās.",
        "Pamatoju likumu ar parasto daļu saucējiem.",
        "Pamanu kļūdu, kurā komats ir nepareizā vietā.",
    ]),

    Majas([
        "Izrēķini 0,45 · 0,2 un pieraksti, cik ciparu aiz komata gaidīji.",
        "Atrodi reizinājumu, kura rezultātā aiz komata ir četri cipari.",
        "Pārbaudi trīs savus rēķinus ar kalkulatoru.",
    ]),
]
