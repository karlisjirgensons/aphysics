# -*- coding: utf-8 -*-
"""7. klase, 145. stunda: «Kā uzdevumu pārtulkot vienādojumā?»

Teksta uzdevumu atrisina trīs soļos: apzīmē nezināmo ar x, izsaka pārējos
lielumus ar x un uzraksta vienādojumu no tā, kas zināms par kopsummu vai
starpību. Stunda trenē tieši tulkošanu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti)

TEMA = "Kā uzdevumu pārtulkot vienādojumā?"

MERKIS = ("Veidosim vienādojumu situācijas aprakstam, apzīmējot "
          "nezināmo ar burtu.")

SATURS = [
    Sakums("Brālis ir 3 gadus vecāks; kopā 27 gadi",
           fakti=["Jaunākais - x, vecākais - x + 3.",
                  "Kopā: x + (x + 3) = 27.",
                  "2x = 24, x = 12: brāļiem 12 un 15 gadi."]),

    Doma("Apzīmē, izsaki, pielīdzini",
         "Teksta uzdevumu pārtulko vienādojumā: vienu nezināmo apzīmē ar x, "
         "pārējos lielumus izsaka ar x un uzraksta vienādību, ko apraksta "
         "teksts (kopā ir ..., par ... vairāk, ... reizes).",
         soli=[
             "Izvēlies, ko apzīmēt ar x (parasti mazāko vai to, ar ko "
             "salīdzina).",
             "Izsaki pārējos lielumus ar x.",
             "Atrodi tekstā vienādību un uzraksti vienādojumu.",
             "Atrisini un atbildi uz jautājumu vārdiem.",
         ]),

    Paraugs("Trīs klases",
            uzd="Trīs klasēs kopā 74 skolēni. B klasē par 4 vairāk nekā A, "
                "C klasē par 2 mazāk nekā A. Cik skolēnu katrā klasē?",
            soli=[
                ("A = x, B = x + 4, C = x − 2", "Izsaka ar x."),
                ("x + (x + 4) + (x − 2) = 74", "Vienādojums."),
                ("3x + 2 = 74, x = 24", "Atrisina."),
                ("24 + 28 + 22 = 74", "Pārbaude."),
            ],
            atbilde="A - 24, B - 28, C - 22 skolēni."),

    Ievadi("Uzraksti un atrisini", [
        {"jaut": "Divu skaitļu summa 50, viens par 8 lielāks. Mazākais?",
         "atb": ["21"], "padoms": "x + x + 8 = 50."},
        {"jaut": "Viens skaitlis 3 reizes lielāks par otru, summa 64. "
                 "Mazākais?",
         "atb": ["16"], "padoms": "x + 3x = 64."},
        {"jaut": "Taisnstūra perimetrs 40 cm, garums par 4 cm lielāks nekā "
                 "platums. Platums (cm)?",
         "atb": ["8"], "padoms": "2(x + x + 4) = 40."},
        {"jaut": "Mamma ir 4 reizes vecāka par dēlu, kopā 50 gadi. Dēla "
                 "vecums?",
         "atb": ["10"], "padoms": "5x = 50."},
    ]),

    Varianti("Kurš vienādojums?", [
        {"jaut": "Pēteris nopirka 3 grāmatas pa x € un pildspalvu par 2 €. "
                 "Samaksāja 26 €.",
         "opcijas": ["3x + 2 = 26", "3(x + 2) = 26", "x + 3 + 2 = 26",
                     "3x = 26 + 2"],
         "pareizi": 0, "padoms": "Pildspalva vienreiz."},
        {"jaut": "Anna ir par 5 gadiem jaunāka nekā Līga (x). Kopā 31.",
         "opcijas": ["x + (x − 5) = 31", "x + (x + 5) = 31", "5x = 31",
                     "x − 5 = 31"],
         "pareizi": 0, "padoms": "Anna - x − 5."},
    ]),

    Pasaule("Koncerta biļetes",
            Ievadi("", [
                {"jaut": "Pārdoti 300 biļešu: parastās pa 20 € un VIP pa 50 €, "
                         "ieņēmumi 7500 €. VIP skaits x: 20(300 − x) + 50x = "
                         "7500. Cik VIP?",
                 "atb": ["50"], "padoms": "6000 + 30x = 7500."},
                {"jaut": "Cik parasto biļešu?",
                 "atb": ["250"], "padoms": "300 − 50."},
                {"jaut": "Ieņēmumi no VIP (€)?",
                 "atb": ["2500"], "padoms": "50 · 50."},
            ]),
            pavediens="veikals",
            konteksts="Pasākumu organizatori no kopējiem ieņēmumiem atjauno, "
                      "cik kādu biļešu pārdots.",
            kapec="Viens nezināmais - otrs izteikts ar to."),

    Kopsavilkums([
        "Apzīmēju nezināmo ar x.",
        "Izsaku pārējos lielumus ar x.",
        "Uzrakstu vienādojumu no teksta vienādības.",
        "Pārbaudu, vai atbilde der situācijai.",
    ]),

    Majas([
        "Divi draugi kopā sakrājuši 90 €, viens divreiz vairāk. Cik katrs?",
        "Izdomā uzdevumu vienādojumam x + 2x + 10 = 70.",
        "Atrisini 3 uzdevumus no mācību grāmatas ar x.",
    ]),
]
