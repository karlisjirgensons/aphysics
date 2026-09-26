# -*- coding: utf-8 -*-
"""2. klase, 39. stunda: «Cik veikli jau proti?»

Saskaitīšanas mikrotemata noslēgums: patstāvīgs treniņš ar pārbaudi. Ir
piemēri bez pārejas un ar to, uzdevumi ar tekstu un «detektīva» uzdevums,
kurā jāatrod cipars, kas paslēpts stabiņā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Kustiba, Majas,
                         Pasaule, Sakums, Varianti, stabins)

TEMA = "Cik veikli jau proti?"

MERKIS = ("Šodien patstāvīgi saskaitīsim divciparu skaitļus un pārbaudīsim "
          "atbildes.")

SATURS = [
    Sakums("Vai vari saskaitīt 5 summas ātrāk nekā minūtē?",
           zimejums=stabins(57, 36, virs="1"),
           fakti=["Novērtē, izrēķini, pārbaudi.",
                  "Ātrums nāk ar treniņu.",
                  "Svarīgāk ir pareizi nekā ātri."]),

    Doma("Mans plāns",
         "Katram piemēram: apmērs, aprēķins, pārbaude.",
         soli=[
             "Apmēram cik sanāks?",
             "Izvēlies paņēmienu un rēķini.",
             "Salīdzini ar apmēru.",
             "Pārbaudi ar atņemšanu.",
         ]),

    Ievadi("Treniņš", [
        {"jaut": "34 + 25 = ?", "atb": ["59"], "padoms": "50 + 9."},
        {"jaut": "47 + 38 = ?", "atb": ["85"], "padoms": "70 + 15."},
        {"jaut": "63 + 29 = ?", "atb": ["92"], "padoms": "63 + 30 − 1."},
        {"jaut": "18 + 56 = ?", "atb": ["74"], "padoms": "60 + 14."},
        {"jaut": "45 + 45 = ?", "atb": ["90"], "padoms": "Dubulti."},
        {"jaut": "76 + 17 = ?", "atb": ["93"], "padoms": "80 + 13."},
        {"jaut": "52 + 39 = ?", "atb": ["91"], "padoms": "52 + 40 − 1."},
        {"jaut": "28 + 64 = ?", "atb": ["92"], "padoms": "80 + 12."},
    ], pamats=6),

    Ievadi("Detektīvs: paslēptais cipars", [
        {"jaut": "3? + 25 = 62. Kāds cipars paslēpts?", "atb": ["7"],
         "padoms": "62 − 25 = 37."},
        {"jaut": "4? + 34 = 80. Kāds cipars?", "atb": ["6"],
         "padoms": "80 − 34 = 46."},
        {"jaut": "?8 + 27 = 45. Kāds cipars?", "atb": ["1"],
         "padoms": "45 − 27 = 18."},
        {"jaut": "56 + 2? = 85. Kāds cipars?", "atb": ["9"],
         "padoms": "85 − 56 = 29."},
    ]),

    Kustiba("Raķete lido uz mērķi", [
        {"jaut": "Raķete pacēlās 38 km, tad vēl 45 km. Cik augstu?",
         "atb": 83, "beigas": 100, "iedala": 10, "mers": "km",
         "objekts": "raķete", "merkis": "38 + 45",
         "padoms": "70 + 13."},
        {"jaut": "Pacēlās 29 km, tad vēl 57 km. Cik augstu?", "atb": 86,
         "beigas": 100, "iedala": 10, "mers": "km", "objekts": "raķete",
         "merkis": "29 + 57", "padoms": "30 + 56."},
    ], ievads="Ieraksti augstumu un palaid raķeti."),

    Varianti("Pārbaudi sevi", [
        {"jaut": "Kura summa ir lielāka par 80?",
         "opcijas": ["46 + 37", "35 + 42", "29 + 49"], "pareizi": 0,
         "padoms": "46 + 37 = 83."},
        {"jaut": "Kura summa ir tieši 70?",
         "opcijas": ["43 + 27", "44 + 36", "38 + 22"], "pareizi": 0,
         "padoms": "3 + 7 = 10."},
    ]),

    Pasaule("Cik punktu komandai?",
            Ievadi("", [
                {"jaut": "Basketbolā pirmajā puslaikā komanda ieguva 37 "
                         "punktus, otrajā - 45. Cik kopā?", "atb": ["82"],
                 "padoms": "70 + 12."},
                {"jaut": "Pretinieki puslaikos ieguva 39 un 44 punktus. Cik "
                         "viņiem kopā?", "atb": ["83"],
                 "padoms": "70 + 13."},
            ]),
            pavediens="sports",
            konteksts="Skolas basketbola turnīrs.",
            kapec="Uzvarētāju nosaka precīza summa."),

    Kopsavilkums([
        "Patstāvīgi saskaitu divciparu skaitļus.",
        "Pārbaudu katru atbildi.",
        "Atrodu paslēptu ciparu, izmantojot atņemšanu.",
    ]),

    Majas([
        "Izrēķini 6 summas no sava uzdevumu krājuma.",
        "Pārbaudi tās ar atņemšanu.",
        "Atzīmē, kuras vēl bija grūtas.",
    ]),
]
