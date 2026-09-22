# -*- coding: utf-8 -*-
"""5. klase, 139. stunda: «Kā atņemt, ja ciparu skaits atšķiras?»

Atņemot 3,6 - 1,57, mazināmajam trūkst simtdaļu, un tieši tur skolēns
apstājas. Risinājums ir 133. stundas paplašināšana: 3,6 = 3,60, un tālāk
viss notiek kā parasti. Tāpēc šī stunda ir vairāk par pierakstu nekā par
atņemšanu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kā atņemt, ja ciparu skaits atšķiras?"

MERKIS = ("Iemācīsimies aprēķināt starpību, lietojot decimāldaļas "
          "paplašināšanu.")

SATURS = [
    Sakums("Trūkst vienas šķiras",
           zimejums=restis([["3", ",", "6", "0"],
                            ["1", ",", "5", "7"]],
                           virsraksts="3,6 pārrakstīts kā 3,60"),
           paraksts="Bez nulles simtdaļu kolonna paliktu tukša.",
           fakti=["3,6 ir viens cipars aiz komata, 1,57 - divi.",
                  "Atņemt var tikai vienas šķiras ciparus.",
                  "Tāpēc 3,6 pārraksta kā 3,60."]),

    Doma("Vispirms izlīdzini, tad atņem",
         "Ja atņemamajiem skaitļiem aiz komata ir dažāds ciparu skaits, "
         "īsāko paplašina ar nullēm un tikai tad atņem kolonnā.",
         soli=[
             "Saskaiti ciparus aiz komata abiem skaitļiem.",
             "Īsākajam pieraksti nulles beigās.",
             "Uzraksti kolonnā ar komatu zem komata.",
             "Atņem pa kolonnām no labās uz kreiso.",
             "Atbildē komatu liec zem komata.",
         ],
         pieze="Nulle beigās neko nemaina: 3,6 = 3,60. Bet bez tās simtdaļu "
               "kolonnā nav no kā atņemt 7, un skolēns vai nu apstājas, vai "
               "raksta 7 atbildē - abas reizes nepareizi."),

    Paraugs("3,6 - 1,57",
            uzd="Aprēķini starpību.",
            soli=[
                ("3,6 = 3,60",
                 "Paplašina līdz simtdaļām."),
                ("Komats zem komata",
                 "Kolonnas sakrīt."),
                ("0 - 7 neiznāk; aizņemas no desmitdaļām",
                 "10 - 7 = 3 simtdaļas."),
                ("5 - 5 = 0 desmitdaļas",
                 "Pēc aizņemšanās palika 5."),
                ("3 - 1 = 2; atbilde 2,03",
                 "Veselie."),
            ],
            atbilde="3,6 - 1,57 = 2,03"),

    Ievadi("Atņem decimāldaļas", [
        {"jaut": "3,6 - 1,57 = ? Ieraksti skaitli.",
         "atb": ["2,03"], "padoms": "3,60 - 1,57."},
        {"jaut": "5,4 - 2,25 = ?",
         "atb": ["3,15"], "padoms": "5,40 - 2,25."},
        {"jaut": "7 - 2,35 = ?",
         "atb": ["4,65"], "padoms": "7,00 - 2,35."},
        {"jaut": "4,5 - 1,8 = ?",
         "atb": ["2,7"], "padoms": "45 - 18 desmitdaļas."},
        {"jaut": "10 - 3,7 = ?",
         "atb": ["6,3"], "padoms": "10,0 - 3,7."},
        {"jaut": "6,05 - 2,5 = ?",
         "atb": ["3,55"], "padoms": "6,05 - 2,50."},
        {"jaut": "8,2 - 5,45 = ?",
         "atb": ["2,75"], "padoms": "8,20 - 5,45."},
        {"jaut": "1 - 0,25 = ?",
         "atb": ["0,75"], "padoms": "1,00 - 0,25."},
    ], pamats=4,
        ievads="Vispirms nulles, tad kolonna, tad atņemšana."),

    Zimejums("Izlīdzināts pieraksts",
             restis([["3", ",", "6", "0"],
                     ["1", ",", "5", "7"],
                     ["2", ",", "0", "3"]],
                    virsraksts="Starpība apakšējā rindā"),
             paskaidro="Ar nulli simtdaļu kolonnā ir no kā atņemt, un "
                       "atbilde iznāk 2,03, nevis 2,3 vai 2,13.",
             ievads="Viena nulle izšķir visu rēķinu."),

    Varianti("Kur pazūd šķira?", [
        {"jaut": "Ko dara, ja ciparu skaits aiz komata atšķiras?",
         "opcijas": ["Īsāko paplašina ar nullēm", "Atmet lieko ciparu",
                     "Saskaita ciparus", "Neko"],
         "pareizi": 0,
         "padoms": "3,6 = 3,60."},
        {"jaut": "3,6 - 1,57 ir...",
         "opcijas": ["2,03", "2,13", "2,3", "1,03"],
         "pareizi": 0,
         "padoms": "3,60 - 1,57."},
        {"jaut": "Kā uzraksta 7, lai atņemtu 2,35?",
         "opcijas": ["7,00", "7,0", "0,7", "70"],
         "pareizi": 0,
         "padoms": "Divi cipari aiz komata."},
        {"jaut": "1 - 0,25 ir...",
         "opcijas": ["0,75", "0,25", "1,25", "0,85"],
         "pareizi": 0,
         "padoms": "1,00 - 0,25."},
        {"jaut": "Vai nulle beigās maina skaitļa vērtību?",
         "opcijas": ["Nemaina", "Palielina", "Samazina", "To nevar zināt"],
         "pareizi": 0,
         "padoms": "3,6 = 3,60."},
        {"jaut": "10 - 3,7 ir...",
         "opcijas": ["6,3", "7,3", "6,7", "13,7"],
         "pareizi": 0,
         "padoms": "10,0 - 3,7."},
    ], pamats=4),

    Pasaule("Cik naudas palika?",
            Ievadi("", [
                {"jaut": "Bija 3,6 €, iztērēti 1,57 €. Cik eiro palika?",
                 "atb": ["2,03"], "padoms": "3,60 - 1,57."},
                {"jaut": "Bija 10 €, iztērēti 3,7 €. Cik eiro palika?",
                 "atb": ["6,3"], "padoms": "10,0 - 3,7."},
                {"jaut": "Bija 5 €, iztērēti 2,35 €. Cik eiro palika?",
                 "atb": ["2,65"], "padoms": "5,00 - 2,35."},
                {"jaut": "Bija 8,2 m dēļa, nogriezti 5,45 m. Cik metru "
                         "palika?",
                 "atb": ["2,75"], "padoms": "8,20 - 5,45."},
            ]),
            pavediens="maja",
            konteksts="Naudas atlikumu un materiāla atlikumu rēķina ar vienu "
                      "un to pašu atņemšanu.",
            kapec="Nulle beigās ir vienīgais, kas atšķir pareizu rēķinu no "
                  "greiza."),

    Kopsavilkums([
        "Izlīdzinu ciparu skaitu aiz komata ar nullēm.",
        "Atņemu decimāldaļas kolonnā ar komatu zem komata.",
        "Aizņemos no augstākās šķiras, kad vajag.",
        "Pierakstu atbildi ar komatu pareizajā vietā.",
    ]),

    Majas([
        "Izrēķini 9,4 - 3,68; 6 - 1,25; 12,5 - 7,85.",
        "Pieraksti, kur katrā piemērā vajadzēja pielikt nulli.",
        "Pārbaudi vienu atbildi ar saskaitīšanu.",
    ]),
]
