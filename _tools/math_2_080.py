# -*- coding: utf-8 -*-
"""2. klase, 80. stunda: «Cik dažādas izteiksmes var izveidot?»

Kombinatorikas sākums: no trim skaitļiem un zīmēm «+» un «−» veido visas
izteiksmes. Kārtīgi uzskaitot (vispirms «+ +», tad «+ −», «− +», «− −»),
neviens gadījums nepazūd.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Sakums, Varianti, restis)

TEMA = "Cik dažādas izteiksmes var izveidot?"

MERKIS = ("Šodien no trim dotiem skaitļiem un zīmēm «+» un «−» veidosim "
          "visas iespējamās izteiksmes.")

_VISAS = restis([["zīmes", "izteiksme", "vērtība"],
                 ["+ +", "30 + 10 + 5", 45],
                 ["+ −", "30 + 10 − 5", 35],
                 ["− +", "30 − 10 + 5", 25],
                 ["− −", "30 − 10 − 5", 15]])

SATURS = [
    Sakums("Starp 30, 10 un 5 jāieliek divas zīmes. Cik dažādu rezultātu?",
           zimejums=_VISAS,
           paraksts="Četras iespējas - četri rezultāti.",
           fakti=["Katrā vietā var būt «+» vai «−».",
                  "Divas vietas - 4 iespējas.",
                  "Kārtīga tabula palīdz nevienu neaizmirst."]),

    Doma("Sistemātiski",
         "Visas iespējas atrod, ja tās uzskaita pēc kārtības.",
         soli=[
             "Pirmajā vietā «+»: otrajā «+» vai «−».",
             "Pirmajā vietā «−»: otrajā «+» vai «−».",
             "Katrai izteiksmei aprēķini vērtību.",
             "Pārbaudi, vai nav divu vienādu.",
         ]),

    Ievadi("Skaitļi 20, 8, 2", [
        {"jaut": "20 + 8 + 2 = ?", "atb": ["30"], "padoms": "28 + 2."},
        {"jaut": "20 + 8 − 2 = ?", "atb": ["26"], "padoms": "28 − 2."},
        {"jaut": "20 − 8 + 2 = ?", "atb": ["14"], "padoms": "12 + 2."},
        {"jaut": "20 − 8 − 2 = ?", "atb": ["10"], "padoms": "12 − 2."},
    ]),

    Varianti("Atrodi izteiksmi", [
        {"jaut": "Skaitļi 50, 20, 10. Kura izteiksme dod 40?",
         "opcijas": ["50 − 20 + 10", "50 + 20 − 10", "50 − 20 − 10"],
         "pareizi": 0, "padoms": "30 + 10."},
        {"jaut": "Skaitļi 50, 20, 10. Kura dod 20?",
         "opcijas": ["50 − 20 − 10", "50 − 20 + 10", "50 + 20 + 10"],
         "pareizi": 0, "padoms": "30 − 10."},
        {"jaut": "Cik izteiksmju var izveidot no trim skaitļiem un divām "
                 "vietām zīmēm «+» vai «−» (skaitļu secība nemainās)?",
         "opcijas": ["4", "2", "6"], "pareizi": 0,
         "padoms": "+ +, + −, − +, − −."},
        {"jaut": "Skaitļi 40, 15, 5. Kura dod lielāko vērtību?",
         "opcijas": ["40 + 15 + 5", "40 + 15 − 5", "40 − 15 + 5"],
         "pareizi": 0, "padoms": "Visu saskaitot."},
    ]),

    Pasaule("Kombinācijas slēdzene",
            Ievadi("", [
                {"jaut": "Slēdzenes kods ir izteiksmes 60, 25, 5 vērtība, "
                         "kur zīmes ir «−» un «+». 60 − 25 + 5 = ?",
                 "atb": ["40"], "padoms": "35 + 5."},
                {"jaut": "Ja zīmes nezina, cik kodi jāizmēģina?",
                 "atb": ["4"], "padoms": "+ +, + −, − +, − −."},
            ]),
            pavediens="kodi",
            konteksts="Dārgumu lādei ir slēdzene ar skaitļu kodu.",
            kapec="Kas uzskaita visas iespējas, atver slēdzeni droši."),

    Kopsavilkums([
        "Veidoju visas izteiksmes no dotajiem skaitļiem un zīmēm.",
        "Uzskaitu iespējas pēc kārtības.",
        "Aprēķinu katras izteiksmes vērtību.",
    ]),

    Majas([
        "Izvēlies trīs skaitļus līdz 50.",
        "Uzraksti visas 4 izteiksmes ar «+» un «−».",
        "Kura vērtība lielākā, kura mazākā?",
    ]),
]
