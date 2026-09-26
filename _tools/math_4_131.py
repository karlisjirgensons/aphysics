# -*- coding: utf-8 -*-
"""4. klase, 131. stunda: «Cik bija sākumā?»

Pretējais uzdevums: zināma daļa, jāatrod veselais. Ja {1|4} ir 6, tad
veselais ir 4 · 6 = 24. Josla ar vienu zināmu gabalu to padara acīmredzamu:
visi gabali ir vienādi.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, restis)

TEMA = "Cik bija sākumā?"

MERKIS = ("Noteiksim veselo, ja zināma pamatdaļas vērtība.")

SATURS = [
    Sakums("Ceturtdaļa tortes - 6 gabali. Cik visa torte?",
           zimejums=restis([["6", "?", "?", "?"]],
                           "1/4 ir 6 - visi gabali vienādi"),
           paraksts="4 · 6 = 24 gabali.",
           fakti=["Ja viena daļa zināma, zināmas visas.",
                  "Veselais = daļas vērtība · saucējs."]),

    Doma("Veselais = pamatdaļa · saucējs",
         "Ja {1|n} no veselā ir a, tad veselais ir n · a.",
         soli=[
             "Uzzīmē joslu no n gabaliem.",
             "Vienā gabalā ieraksti a.",
             "Visi gabali vienādi - veselais n · a.",
             "Pārbaudi: n · a : n = a.",
         ],
         pieze="Tas ir pretēji daļai no skaitļa: tur dala, šeit reizina."),

    Slidnis("Josla aug",
            soli=[
                {"v": "{1|5} no veselā ir 7", "teksts": "Viens gabals zināms.",
                 "josla": 20},
                {"v": "{2|5} no veselā ir 14", "teksts": "Divi gabali.", "josla": 40},
                {"v": "viss veselais ir 35", "teksts": "Viss - 5 · 7.",
                 "josla": 100},
            ]),

    Paraugs("{1|3} ir 9",
            uzd="Trešdaļa klases - 9 skolēni. Cik skolēnu klasē?",
            soli=[
                ("{1|3} klases ir 9", None),
                ("3 · 9 = 27", "Trīs vienādas daļas."),
            ],
            atbilde="27 skolēni"),

    Ievadi("Atrodi veselo", [
        {"jaut": "{1|4} ir 6. Veselais = ?", "atb": ["24"], "padoms": "4 · 6."},
        {"jaut": "{1|5} ir 7. Veselais = ?", "atb": ["35"], "padoms": "5 · 7."},
        {"jaut": "{1|10} ir 12. Veselais = ?", "atb": ["120"],
         "padoms": "10 · 12."},
        {"jaut": "{1|8} ir 25. Veselais = ?", "atb": ["200"],
         "padoms": "8 · 25."},
        {"jaut": "{1|3} ir 150 €. Veselais = ? €", "atb": ["450"],
         "padoms": "3 · 150."},
        {"jaut": "{1|6} ir 10 min. Veselais = ? min", "atb": ["60"],
         "padoms": "6 · 10."},
    ], pamats=4),

    Varianti("Dalīt vai reizināt?", [
        {"jaut": "«{1|4} no 40» - kā rēķina?",
         "opcijas": ["40 : 4", "40 · 4"], "pareizi": 0,
         "padoms": "Daļa no skaitļa - dala."},
        {"jaut": "«{1|4} ir 40, cik veselais?» - kā rēķina?",
         "opcijas": ["40 · 4", "40 : 4"], "pareizi": 0,
         "padoms": "Veselais - reizina."},
        {"jaut": "{1|7} ir 8. Kas ir veselais?",
         "opcijas": ["56", "1", "15", "8"], "pareizi": 0,
         "padoms": "7 · 8."},
    ]),

    Pasaule("Detektīva uzdevumi",
            Ievadi("", [
                {"jaut": "Anna iztērēja {1|5} krājkasītes - 4 €. Cik bija "
                         "krājkasītē?",
                 "atb": ["20"], "padoms": "5 · 4."},
                {"jaut": "Juris nogāja {1|4} ceļa - 300 m. Cik garš viss "
                         "ceļš?",
                 "atb": ["1200"], "padoms": "4 · 300."},
                {"jaut": "{1|10} no ūdens mucā ir 8 l. Cik litru muca?",
                 "atb": ["80"], "padoms": "10 · 8."},
                {"jaut": "Grāmatas {1|6} ir 45 lappuses. Cik lappušu "
                         "grāmatā?",
                 "atb": ["270"], "padoms": "6 · 45."},
            ]),
            pavediens="veikals",
            konteksts="Bieži zinām tikai daļu - cik iztērēts vai noiets - "
                      "un jāatrod, cik bija sākumā.",
            kapec="Veselo atrod, reizinot daļu ar saucēju."),

    Kopsavilkums([
        "Atrodu veselo, ja zināma pamatdaļa.",
        "Reizinu pamatdaļas vērtību ar saucēju.",
        "Atšķiru «daļa no skaitļa» un «skaitlis pēc daļas».",
    ]),

    Majas([
        "Izdomā uzdevumu: {1|4} no kaut kā ir 12. Cik ir viss?",
        "Izmēri {1|10} no sava auguma (aptuveni) un aprēķini visu.",
        "Paskaidro kādam, kad dala un kad reizina.",
    ]),
]
