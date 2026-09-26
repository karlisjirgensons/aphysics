# -*- coding: utf-8 -*-
"""8. klase, 62. stunda: «Kā pierakstīt algoritmu?»

Bloka un temata noslēgums pirms PD3: visas darbības ar saknēm saliek vienā
algoritmā, kas der jebkurai saknei - daļa, iznešana, sakne no saucēja,
līdzīgo savilkšana. Slīdnis izpilda algoritmu √360 soli pa solim.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Slidnis, Varianti, restis)

TEMA = "Kā pierakstīt algoritmu?"

MERKIS = ("Formulēsim un pierakstīsim algoritmu darbību izpildei ar "
          "kvadrātsaknēm.")

SATURS = [
    Sakums("Kā vienkāršot jebkuru sakni?",
           zimejums=restis([["1.", "Sadali reizinātājos"],
                            ["2.", "Atrodi pārus"],
                            ["3.", "Iznes pārus"],
                            ["4.", "Pārbaudi"]]),
           paraksts="Četri soļi, kas der katrai saknei.",
           fakti=["Algoritms - soļi, kas der katram gadījumam.",
                  "Soļu secība ir svarīga.",
                  "Katru soli var pārbaudīt."]),

    Doma("Saknes vienkāršošanas algoritms",
         "Vienkāršotā saknē nav pilna kvadrāta reizinātāja, daļas un saknes "
         "saucējā.",
         soli=[
             "Ja zem saknes ir daļa, velc sakni no skaitītāja un saucēja.",
             "Zemsaknes skaitli sadali pirmreizinātājos: 72 = 2 · 2 · 2 · 3 · 3.",
             "No katra vienādu reizinātāju pāra iznes vienu: 2 · 3√2 = 6√2.",
             "Ja saucējā paliek sakne, reizini skaitītāju un saucēju ar to.",
             "Savelc līdzīgās saknes.",
         ]),

    Slidnis("√360 soli pa solim", [
        {"v": "√360", "teksts": "360 = 2 · 2 · 2 · 3 · 3 · 5"},
        {"v": "Pāri", "teksts": "(2 · 2) un (3 · 3) - pilni kvadrāti"},
        {"v": "2 · 3√(2 · 5)", "teksts": "No katra pāra iznes vienu "
                                        "reizinātāju"},
        {"v": "6√10", "teksts": "Pārbaude: 36 · 10 = 360"},
    ]),

    Paraugs("Algoritms ar daļu",
            uzd="Vienkāršo √{8|9} + √{1|2}.",
            soli=[
                ("√{8|9} = {√8|3} = {2√2|3}", "Daļas sakne, tad iznes."),
                ("√{1|2} = {1|√2} = {√2|2}", "Sakni no saucēja pārnes."),
                ("{2√2|3} + {√2|2} = {4√2|6} + {3√2|6}", "Kopsaucējs 6."),
                ("= {7√2|6}", "Savelk līdzīgās saknes."),
            ],
            atbilde="{7√2|6}"),

    Varianti("Pārbaudi soļus", [
        {"jaut": "Kurš pieraksts ir pilnīgi vienkāršots?",
         "opcijas": ["3√5", "√45", "{3|√5}", "2√20"],
         "pareizi": 0, "padoms": "Pārējos var vēl vienkāršot."},
        {"jaut": "Kur ir kļūda: √48 = √(4 · 12) = 2√12?",
         "opcijas": ["Nav iznests viss: 12 = 4 · 3", "4 nav pilns kvadrāts",
                     "Jābūt 4√12", "Kļūdas nav"],
         "pareizi": 0, "padoms": "√48 = 4√3."},
        {"jaut": "Kas jādara ar {6|√3}?",
         "opcijas": ["Reizināt ar {√3|√3}", "Dalīt ar 3", "Kāpināt kvadrātā",
                     "Neko"],
         "pareizi": 0, "padoms": "{6√3|3} = 2√3."},
    ]),

    Ievadi("Izpildi algoritmu", [
        {"jaut": "√128 = ?√2", "atb": ["8"], "padoms": "128 = 64 · 2."},
        {"jaut": "√{27|4} = {a√3|2}. a = ?", "atb": ["3"],
         "padoms": "√27 = 3√3."},
        {"jaut": "{12|√6} = a√6. a = ?", "atb": ["2"],
         "padoms": "{12√6|6}."},
        {"jaut": "√8 + √{1|2} = {a√2|2}. a = ?", "atb": ["5"],
         "padoms": "{4√2|2} + {√2|2}."},
    ]),

    Pasaule("Programma, kas vienkāršo",
            Ievadi("", [
                {"jaut": "Programma vienkāršo √500: meklē lielāko k, kam k^2 "
                         "dala 500. Kāds ir k?",
                 "atb": ["10"], "padoms": "500 = 100 · 5."},
                {"jaut": "Līdz kuram lielākajam k jāpārbauda, ja k^2 ≤ 500?",
                 "atb": ["22"], "padoms": "22^2 = 484, 23^2 = 529."},
                {"jaut": "√500 = ?√5", "atb": ["10"], "padoms": "k = 10."},
            ]),
            pavediens="dati",
            konteksts="Datorprogramma neko neredz «uz aci» - tai vajag "
                      "precīzus soļus, kas der jebkuram skaitlim.",
            kapec="Labu algoritmu bez minēšanas var izpildīt gan dators, "
                  "gan cilvēks."),

    Kopsavilkums([
        "Pierakstu saknes vienkāršošanas algoritmu.",
        "Izpildu to soli pa solim un pārbaudu katru soli.",
        "Atrodu kļūdu cita risinājumā.",
    ]),

    Majas([
        "Pieraksti algoritmu un izpildi to: √288, √{50|9}, {10|√2}.",
        "Izveido plakātu «Kā vienkāršot sakni» ar vienu piemēru.",
        "Pārbaudi savus rezultātus ar kalkulatoru.",
    ]),
]
