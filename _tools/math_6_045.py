# -*- coding: utf-8 -*-
"""6. klase, 45. stunda: «Kas notiek, reizinot ar 0,1?»

Otrs virziens. Reizināšana ar 0,1 ir pirmais gadījums, kad reizinot skaitlis
sarūk - un tas nav pretrunā ar iepriekšējo stundu, jo 0,1 ir mazāks par 1.
Abas stundas kopā dod vienu likumu ar diviem virzieniem.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti)

TEMA = "Kas notiek, reizinot ar 0,1?"

MERKIS = ("Formulēsim algoritmu reizināšanai ar 0,1; 0,01 un 0,001.")

SATURS = [
    Sakums("Reizinot ar 0,1, skaitlis sarūk",
           fakti=["0,1 ir tas pats, kas {1|10} - tātad desmitā daļa.",
                  "45 · 0,1 = 4,5 - komats pārceļas pa kreisi.",
                  "Ciparu skaits aiz komata pasaka soļu skaitu."]),

    Doma("Komats ceļo pa kreisi",
         "Reizinot ar 0,1; 0,01 vai 0,001, komatu pārceļ par tik vietām pa "
         "kreisi, cik ciparu ir aiz komata reizinātājā.",
         soli=[
             "Saskaiti ciparus aiz komata reizinātājā.",
             "Pārcel komatu par tik vietām pa kreisi.",
             "Ja ciparu nepietiek, priekšā pieraksti nulles.",
             "Pārbaudi: skaitlim jākļūst mazākam.",
         ],
         pieze="Reizināt ar 0,1 ir tas pats, kas dalīt ar 10. Tieši tāpēc "
               "šie algoritmi nav četri dažādi - tie ir divi, katrs ar "
               "diviem pierakstiem."),

    Slidnis("Katrs solis - desmit reižu mazāk",
            [{"v": "450 · 1", "teksts": "= 450", "josla": 100},
             {"v": "450 · 0,1", "teksts": "= 45", "josla": 70},
             {"v": "450 · 0,01", "teksts": "= 4,5", "josla": 45},
             {"v": "450 · 0,001", "teksts": "= 0,45", "josla": 20}],
            ievads="Spied soli pa solim: cipari 4, 5 un 0 nemainās - mainās "
                   "tikai komata vieta."),

    Paraugs("Reizini ar 0,01",
            uzd="Cik ir 27,5 · 0,01?",
            soli=[
                ("0,01 - divi cipari aiz komata",
                 "Tik vietas komats pārceļas."),
                ("27,5 → 2,75 → 0,275",
                 "Divi soļi pa kreisi."),
                ("Pārbaude: 27,5 ir apmēram 28; simtā daļa no 28 ir 0,28",
                 "0,275 ir ticams."),
            ],
            atbilde="0,275"),

    Ievadi("Pārcel komatu pa kreisi", [
        {"jaut": "Cik ir 45 · 0,1?",
         "atb": ["4,5", "4.5"], "padoms": "Viena vieta pa kreisi."},
        {"jaut": "Cik ir 3,6 · 0,1?",
         "atb": ["0,36", "0.36"], "padoms": "Viena vieta pa kreisi."},
        {"jaut": "Cik ir 250 · 0,01?",
         "atb": ["2,5", "2.5"], "padoms": "Divas vietas pa kreisi."},
        {"jaut": "Cik ir 7 · 0,001?",
         "atb": ["0,007", "0.007"], "padoms": "Trīs vietas; nulles priekšā."},
        {"jaut": "Cik ir 0,8 · 0,1?",
         "atb": ["0,08", "0.08"], "padoms": "Viena vieta pa kreisi."},
        {"jaut": "Cik ir 1240 · 0,001?",
         "atb": ["1,24", "1.24"], "padoms": "Trīs vietas pa kreisi."},
    ], pamats=4,
        ievads="Ciparu skaits aiz komata reizinātājā ir soļu skaits."),

    Varianti("Uz kuru pusi?", [
        {"jaut": "Reizinot ar 0,001, komats pārceļas...",
         "opcijas": ["par trim vietām pa kreisi",
                     "par trim vietām pa labi",
                     "par vienu vietu pa kreisi", "nekur"],
         "pareizi": 0,
         "padoms": "Trīs cipari aiz komata."},
        {"jaut": "Reizināt ar 0,1 ir tas pats, kas...",
         "opcijas": ["dalīt ar 10", "reizināt ar 10",
                     "dalīt ar 0,1", "atņemt 0,1"],
         "pareizi": 0,
         "padoms": "0,1 = {1|10}."},
        {"jaut": "Cik ir 0,05 · 0,1?",
         "opcijas": ["0,005", "0,5", "0,05", "5"],
         "pareizi": 0,
         "padoms": "Viena vieta pa kreisi."},
        {"jaut": "Kāpēc skaitlis kļūst mazāks?",
         "opcijas": ["Jo reizinātājs ir mazāks par 1",
                     "Jo komats pazūd", "Jo cipari mainās",
                     "Tas nekļūst mazāks"],
         "pareizi": 0,
         "padoms": "Robeža ir vieninieks."},
    ], pamats=4),

    Pasaule("Cik sver viena daļiņa?",
            Ievadi("", [
                {"jaut": "1000 graudu sver 24 g. Cik gramu sver viens "
                         "grauds?",
                 "atb": ["0,024", "0.024"], "padoms": "24 · 0,001."},
                {"jaut": "100 lapas sver 45 g. Cik gramu sver viena lapa?",
                 "atb": ["0,45", "0.45"], "padoms": "45 · 0,01."},
                {"jaut": "10 skrūves sver 8,5 g. Cik gramu sver viena?",
                 "atb": ["0,85", "0.85"], "padoms": "8,5 · 0,1."},
                {"jaut": "1000 pilieni ir 50 ml. Cik ml ir viens piliens?",
                 "atb": ["0,05", "0.05"], "padoms": "50 · 0,001."},
            ]),
            pavediens="daba",
            konteksts="Vienas sēklas masu nemēra - nosver tūkstoti un "
                      "pārceļ komatu.",
            kapec="Reizināšana ar 0,001 ir ātrākais ceļš no daudziem uz "
                  "vienu."),

    Kopsavilkums([
        "Reizinu ar 0,1; 0,01 un 0,001, pārceļot komatu pa kreisi.",
        "Zinu, ka soļu skaits ir ciparu skaits aiz komata reizinātājā.",
        "Pierakstu nulles priekšā, ja ciparu nepietiek.",
        "Saistu reizināšanu ar 0,1 ar dalīšanu ar 10.",
    ]),

    Majas([
        "Izrēķini 620 · 0,01 un 4,5 · 0,001.",
        "Pārvērt savu augumu no centimetriem metros, izmantojot 0,01.",
        "Pieraksti, kāpēc reizināšana ar 0,1 nav pretrunā ar iepriekšējo "
        "stundu.",
    ]),
]
