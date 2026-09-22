# -*- coding: utf-8 -*-
"""6. klase, 49. stunda: «Kā dalīt decimāldaļu ar veselu skaitli?»

Jauns mikrotemats. Dalīšana ar veselu skaitli ir vienīgā no decimāldaļu
darbībām, kurā nekas nav jāpārveido - komats paliek vietā. Tieši tāpēc ar to
sākas, un tieši tāpēc te vingrina pārbaudi.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kā dalīt decimāldaļu ar veselu skaitli?"

MERKIS = ("Iemācīsimies dalīt decimāldaļu ar veselu skaitli un pārbaudīt "
          "rezultātu ar reizināšanu.")

SATURS = [
    Sakums("Komats paliek tieši tur, kur bija",
           zimejums=restis([["7", ",", "5", ":", "3"],
                            ["2", ",", "5", "", ""]]),
           paraksts="7,5 : 3 = 2,5. Komats dalījumā ir tieši virs komata "
                    "dalāmajā.",
           fakti=["Dalot ar veselu skaitli, komatu nekur nepārceļ.",
                  "Rēķina kā veselus skaitļus un komatu liek vietā.",
                  "Ja dalīšana nebeidzas, dalāmajam pieraksta nulles."]),

    Doma("Komats dalījumā stāv virs komata dalāmajā",
         "Decimāldaļu ar veselu skaitli dala tāpat kā veselus skaitļus, un "
         "komatu dalījumā liek tad, kad dalāmajā tiek pāriets pāri komatam.",
         soli=[
             "Dali veselo daļu kā parasti.",
             "Kad dalāmajā sasniedz komatu, liec komatu arī dalījumā.",
             "Turpini dalīt ciparus aiz komata.",
             "Ja atlikums nav nulle, pieraksti dalāmajam nulli un turpini.",
             "Pārbaudi ar reizināšanu.",
         ],
         pieze="0,6 : 4 = 0,15 - te veselā daļa ir nulle, tāpēc dalījums "
               "sākas ar «0,». Tas nav kļūda, bet gaidāms rezultāts: "
               "dalījums ir mazāks par dalāmo."),

    Paraugs("Dali un pārbaudi",
            uzd="Cik ir 9,6 : 4?",
            soli=[
                ("9 : 4 = 2, atlikums 1",
                 "Vispirms veselā daļa."),
                ("Pāriet pāri komatam - liec komatu dalījumā",
                 "Dalījums sākas ar «2,»."),
                ("16 : 4 = 4",
                 "Atlikums 1 un nākamais cipars 6 dod 16."),
                ("9,6 : 4 = 2,4",
                 "Dalīšana beidzas bez atlikuma."),
                ("Pārbaude: 2,4 · 4 = 9,6",
                 "Atgriežas dalāmais."),
            ],
            atbilde="2,4"),

    Ievadi("Dali ar veselu skaitli", [
        {"jaut": "Cik ir 7,5 : 3?",
         "atb": ["2,5", "2.5"], "padoms": "75 : 3 = 25; komats vietā."},
        {"jaut": "Cik ir 8,4 : 4?",
         "atb": ["2,1", "2.1"], "padoms": "84 : 4 = 21."},
        {"jaut": "Cik ir 0,6 : 4?",
         "atb": ["0,15", "0.15"], "padoms": "Pieraksta nulli: 60 : 4 = 15."},
        {"jaut": "Cik ir 12,6 : 6?",
         "atb": ["2,1", "2.1"], "padoms": "126 : 6 = 21."},
        {"jaut": "Cik ir 5,04 : 4?",
         "atb": ["1,26", "1.26"], "padoms": "504 : 4 = 126."},
        {"jaut": "Cik ir 3 : 8?",
         "atb": ["0,375", "0.375"], "padoms": "3,000 : 8."},
    ], pamats=4,
        ievads="Pēc katras atbildes pārbaudi ar reizināšanu."),

    Varianti("Kur liek komatu?", [
        {"jaut": "Kad dalījumā liek komatu?",
         "opcijas": ["Kad dalāmajā tiek pāriets pāri komatam",
                     "Beigās", "Sākumā", "Nekad"],
         "pareizi": 0,
         "padoms": "Komats dalījumā stāv virs komata dalāmajā."},
        {"jaut": "Ko darīt, ja atlikums nav nulle?",
         "opcijas": ["Pierakstīt dalāmajam nulli un turpināt",
                     "Noapaļot uzreiz", "Pārtraukt dalīšanu",
                     "Mainīt dalītāju"],
         "pareizi": 0,
         "padoms": "3 : 8 = 0,375 - tieši tā tas notiek."},
        {"jaut": "0,6 : 4 rezultāts ir...",
         "opcijas": ["mazāks par 0,6", "lielāks par 0,6",
                     "vienāds ar 0,6", "vesels skaitlis"],
         "pareizi": 0,
         "padoms": "Dalītājs ir lielāks par 1."},
        {"jaut": "Kā pārbaudīt 9,6 : 4 = 2,4?",
         "opcijas": ["2,4 · 4", "9,6 · 4", "2,4 : 4", "9,6 + 2,4"],
         "pareizi": 0,
         "padoms": "Rezultāts reiz dalītājs."},
    ], pamats=4),

    Pasaule("Cik maksā viens gabals?",
            Ievadi("", [
                {"jaut": "4 burtnīcas maksā 5,2 €. Cik eiro maksā viena?",
                 "atb": ["1,3", "1.3"], "padoms": "52 : 4 = 13."},
                {"jaut": "6 maizes maksā 4,5 €. Cik eiro maksā viena?",
                 "atb": ["0,75", "0.75"], "padoms": "450 : 6 = 75."},
                {"jaut": "8 skolēni sadala 6 l sulas. Cik litru katram?",
                 "atb": ["0,75", "0.75"], "padoms": "6,00 : 8."},
                {"jaut": "5 detaļas sver 12,5 kg. Cik kg sver viena?",
                 "atb": ["2,5", "2.5"], "padoms": "125 : 5 = 25."},
            ]),
            pavediens="veikals",
            konteksts="Cenu par vienu gabalu veikalā neraksta - to izrēķina "
                      "pats, dalot ar gabalu skaitu.",
            kapec="Dalot ar veselu skaitli, komats paliek savā vietā."),

    Zimejums("Kad dalīšana neapstājas uzreiz",
             restis([["3", ",", "0", "0", "0", ":", "8"],
                     ["0", ",", "3", "7", "5", "", ""]]),
             paskaidro="3 : 8 = 0,375. Dalāmajam pieraksta nulles, līdz "
                       "atlikums kļūst par nulli.",
             ievads="Vesels skaitlis arī ir decimāldaļa: 3 = 3,000."),

    Kopsavilkums([
        "Dalu decimāldaļu ar veselu skaitli, neaiztiekot komatu.",
        "Lieku komatu dalījumā tur, kur dalāmajā to pāriet.",
        "Pierakstu nulles, ja dalīšana neapstājas.",
        "Pārbaudu rezultātu ar reizināšanu.",
    ]),

    Majas([
        "Izrēķini 14,4 : 6 un 7 : 4 ar pārbaudi.",
        "Atrodi mājās iepakojumu un izrēķini cenu par vienu vienību.",
        "Pieraksti, kurā solī tev bija jāpieraksta nulle.",
    ]),
]
