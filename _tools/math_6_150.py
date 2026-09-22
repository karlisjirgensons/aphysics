# -*- coding: utf-8 -*-
"""6. klase, 150. stunda: «Kāda zīme ir garai izteiksmei?»

Ja reizinātāju ir vairāki, zīmi nosaka viens skaitlis: cik mīnusu ir kopā.
Nepāra skaits dod mīnusu, pāra - plusu. Šis noteikums ļauj pateikt atbildes
zīmi, pat neizrēķinot pašu reizinājumu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kāda zīme ir garai izteiksmei?"

MERKIS = ("Noteiksim reizinājuma zīmi, ja reizinātāju ir vairāki.")

SATURS = [
    Sakums("Skaiti mīnusus, nevis skaitļus",
           zimejums=restis([["1 mīnuss", "2 mīnusi", "3 mīnusi",
                             "4 mīnusi"],
                            ["−", "+", "−", "+"]]),
           paraksts="Nepāra skaits mīnusu dod negatīvu rezultātu, pāra "
                    "skaits - pozitīvu.",
           fakti=["Katrs mīnuss «apgriež» zīmi.",
                  "Divi mīnusi atceļ viens otru.",
                  "Tāpēc svarīgs ir tikai mīnusu skaita pāra vai nepāra "
                  "raksturs."]),

    Doma("Pāra skaits mīnusu dod plusu",
         "Vairāku reizinātāju reizinājuma zīmi nosaka negatīvo reizinātāju "
         "skaits: pāra skaits dod pozitīvu rezultātu, nepāra - negatīvu.",
         soli=[
             "Saskaiti, cik reizinātāju ir negatīvi.",
             "Ja skaits ir pāra, rezultāts būs pozitīvs.",
             "Ja nepāra - negatīvs.",
             "Sareizini visus moduļus.",
             "Pieliec noteikto zīmi.",
         ],
         pieze="Ja kaut viens reizinātājs ir nulle, viss reizinājums ir "
               "nulle - tad zīmi meklēt nevajag. To pārbauda vispirms."),

    Paraugs("Saskaiti mīnusus",
            uzd="Kāda zīme ir reizinājumam (−2) · 3 · (−4) · (−1)?",
            soli=[
                ("Negatīvie reizinātāji: −2; −4; −1",
                 "Trīs mīnusi."),
                ("Trīs ir nepāra skaitlis",
                 "Rezultāts būs negatīvs."),
                ("Moduļi: 2 · 3 · 4 · 1 = 24",
                 "Reizinājums bez zīmēm."),
                ("Rezultāts: −24",
                 "Zīme no mīnusu skaita."),
            ],
            atbilde="−24"),

    Ievadi("Nosaki zīmi un izrēķini", [
        {"jaut": "Cik ir (−2) · 3 · (−4) · (−1)?",
         "atb": ["-24", "−24"], "padoms": "Trīs mīnusi."},
        {"jaut": "Cik ir (−2) · (−3) · (−4)?",
         "atb": ["-24", "−24"], "padoms": "Trīs mīnusi."},
        {"jaut": "Cik ir (−2) · (−3) · 4?",
         "atb": ["24"], "padoms": "Divi mīnusi."},
        {"jaut": "Cik ir (−1) · (−1) · (−1) · (−1)?",
         "atb": ["1"], "padoms": "Četri mīnusi."},
        {"jaut": "Cik ir (−5) · 2 · 0 · (−3)?",
         "atb": ["0"], "padoms": "Viens reizinātājs ir nulle."},
        {"jaut": "Cik mīnusu ir izteiksmē (−1) · (−2) · (−3) · (−4) · (−5)?",
         "atb": ["5"], "padoms": "Visi pieci."},
    ], pamats=4,
        ievads="Vispirms saskaiti mīnusus, tikai tad reizini moduļus."),

    Varianti("Pāra vai nepāra?", [
        {"jaut": "Trīs negatīvi reizinātāji dod...",
         "opcijas": ["negatīvu rezultātu", "pozitīvu rezultātu",
                     "nulli", "nevar zināt"],
         "pareizi": 0,
         "padoms": "Nepāra skaits."},
        {"jaut": "Četri negatīvi reizinātāji dod...",
         "opcijas": ["pozitīvu rezultātu", "negatīvu rezultātu",
                     "nulli", "nevar zināt"],
         "pareizi": 0,
         "padoms": "Pāra skaits."},
        {"jaut": "Ko pārbauda vispirms?",
         "opcijas": ["Vai kāds reizinātājs nav nulle",
                     "Cik ir mīnusu", "Moduļu reizinājumu",
                     "Reizinātāju skaitu"],
         "pareizi": 0,
         "padoms": "Nulle padara visu par nulli."},
        {"jaut": "(−1) desmitajā pakāpē ir...",
         "opcijas": ["1", "−1", "10", "−10"],
         "pareizi": 0,
         "padoms": "Desmit mīnusu - pāra skaits."},
    ], pamats=4),

    Pasaule("Kāds būs gala rezultāts?",
            Ievadi("", [
                {"jaut": "Trīs reizes pēc kārtas summa samazinās divkārt: "
                         "(−1) · (−1) · (−1). Kāda ir zīme? Raksti «pluss» "
                         "vai «mīnuss».",
                 "atb": ["mīnuss", "minuss"], "padoms": "Trīs mīnusi."},
                {"jaut": "Cik ir (−2) · (−2) · (−2)?",
                 "atb": ["-8", "−8"], "padoms": "Trīs mīnusi, moduļi 8."},
                {"jaut": "Cik ir (−2) · (−2) · (−2) · (−2)?",
                 "atb": ["16"], "padoms": "Četri mīnusi."},
                {"jaut": "Cik ir (−3) · 4 · (−5)?",
                 "atb": ["60"], "padoms": "Divi mīnusi, moduļi 60."},
            ]),
            pavediens="dati",
            konteksts="Programmā vairāki koeficienti tiek sareizināti cits "
                      "ar citu - un zīmi var pateikt jau pirms izpildes.",
            kapec="Mīnusu skaits ir vienīgais, kas nosaka zīmi."),

    Zimejums("Mīnusu skaits un zīme",
             restis([["(−2)·3", "(−2)·(−3)", "(−2)·(−3)·(−4)"],
                     ["−6", "6", "−24"]]),
             paskaidro="Viens mīnuss - negatīvs; divi - pozitīvs; trīs - "
                       "atkal negatīvs.",
             ievads="Zīme mainās ar katru jaunu mīnusu."),

    Kopsavilkums([
        "Nosaku reizinājuma zīmi pēc negatīvo reizinātāju skaita.",
        "Zinu, ka pāra skaits mīnusu dod plusu.",
        "Vispirms pārbaudu, vai kāds reizinātājs nav nulle.",
        "Sareizinu moduļus un pielieku zīmi.",
    ]),

    Majas([
        "Nosaki zīmi un izrēķini (−1) · (−2) · 3 · (−4).",
        "Uzraksti reizinājumu ar četriem reizinātājiem, kura rezultāts ir "
        "pozitīvs.",
        "Pieraksti, cik mīnusu tajā ir.",
    ]),
]
