# -*- coding: utf-8 -*-
"""7. klase, 122. stunda: «Kā pārveidot garāku izteiksmi?»

Garāku izteiksmi vienkāršo soļos: vispirms iekavas (arī ar mīnusu), tad
līdzīgo saskaitāmo savilkšana. Katru soli pieraksta atsevišķā rindā - tā
kļūdu var atrast un pārbaudīt.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti)

TEMA = "Kā pārveidot garāku izteiksmi?"

MERKIS = ("Vienkāršosim izteiksmi vairākos soļos un pierakstīsim katru "
          "soli.")

SATURS = [
    Sakums("Garš pieraksts - īss rezultāts",
           fakti=["3(2x − 1) − 2(x − 4) + x izskatās sarežģīti.",
                  "Pēc trim soļiem: 5x + 5.",
                  "Soļi - kā kāpnes: katrs vienkāršs."]),

    Doma("Soļi: iekavas → līdzīgie → pārbaude",
         "Garāku izteiksmi vienkāršo, katru pārveidojumu pierakstot jaunā "
         "rindā ar vienādības zīmi: vispirms atver visas iekavas, tad savelk "
         "līdzīgos saskaitāmos.",
         soli=[
             "1. solis: atver visas iekavas (ievēro zīmes).",
             "2. solis: sagrupē līdzīgos (pasvītro).",
             "3. solis: savelc.",
             "Pārbaude: ievieto x = 1 sākumā un beigās.",
         ],
         pieze="Neraksti visu vienā rindā galvā - katrs solis uz papīra "
               "samazina kļūdu iespēju."),

    Paraugs("Trīs soļi",
            uzd="Vienkāršo: 3(2x − 1) − 2(x − 4) + x.",
            soli=[
                ("= 6x − 3 − 2x + 8 + x", "Atver iekavas."),
                ("= (6x − 2x + x) + (−3 + 8)", "Grupē."),
                ("= 5x + 5", "Savelk."),
                ("Pārbaude x = 1: 3 · 1 − 2 · (−3) + 1 = 10; 5 + 5 = 10",
                 "Sakrīt."),
            ],
            atbilde="5x + 5"),

    Ievadi("Vienkāršo", [
        {"jaut": "2(a + 3) + 3(a − 1) = ?",
         "atb": ["5a + 3", "5a+3"], "padoms": "2a + 6 + 3a − 3.",
         "tastatura": "text"},
        {"jaut": "4(x − 2) − (x + 1) = ?",
         "atb": ["3x − 9", "3x-9"], "padoms": "4x − 8 − x − 1.",
         "tastatura": "text"},
        {"jaut": "5 − 2(3 − y) = ?",
         "atb": ["2y − 1", "2y-1", "-1+2y"], "padoms": "5 − 6 + 2y.",
         "tastatura": "text"},
        {"jaut": "−(m − 4) + 3(m + 2) − 2m = ?",
         "atb": ["10"], "padoms": "−m + 4 + 3m + 6 − 2m.",
         "tastatura": "text"},
        {"jaut": "0,5(2x + 8) − 3(x − 1) = ?",
         "atb": ["−2x + 7", "-2x+7", "7-2x"], "padoms": "x + 4 − 3x + 3.",
         "tastatura": "text"},
        {"jaut": "Vērtība 3(2x − 1) − 2(x − 4) + x, ja x = 3?",
         "atb": ["20"], "padoms": "Vienkāršotā: 5 · 3 + 5."},
    ], pamats=4),

    Varianti("Vienkāršošanas priekšrocība", [
        {"jaut": "Kāpēc izteiksmi vienkāršo pirms aprēķina?",
         "opcijas": ["Mazāk darbību - mazāk kļūdu",
                     "Tā ir skaistāk", "Rezultāts mainās",
                     "Tā prasa skolotājs"],
         "pareizi": 0, "padoms": "5x + 5 ir vieglāk nekā oriģināls."},
        {"jaut": "−(m − 4) + 3(m + 2) − 2m = 10. Ko tas nozīmē?",
         "opcijas": ["Vērtība ir 10 jebkuram m",
                     "m = 10", "Kļūda", "m = 0"],
         "pareizi": 0, "padoms": "m pazuda."},
    ]),

    Pasaule("Ģimenes mobilie tarifi",
            Ievadi("", [
                {"jaut": "3 telefoni pa (t + 2) € un 2 planšetes pa (t − 1) €. "
                         "Vienkāršo: 3(t + 2) + 2(t − 1) = ?t + ? Raksti "
                         "koeficientu pie t.",
                 "atb": ["5"], "padoms": "3t + 2t."},
                {"jaut": "Un brīvo locekli?",
                 "atb": ["4"], "padoms": "6 − 2."},
                {"jaut": "Cik € mēnesī, ja t = 9?",
                 "atb": ["49"], "padoms": "45 + 4."},
            ]),
            pavediens="dati",
            konteksts="Ģimenes plānā vairākas ierīces ar dažādām cenām - "
                      "vienkāršota izteiksme parāda kopsummu.",
            kapec="5t + 4 ir vienkāršāk nekā 3(t + 2) + 2(t − 1)."),

    Kopsavilkums([
        "Vienkāršoju izteiksmi soļos.",
        "Katru soli pierakstu jaunā rindā.",
        "Vispirms atveru iekavas, tad savelku.",
        "Pārbaudu ar x = 1.",
    ]),

    Majas([
        "Vienkāršo: 2(3a − 1) − 4(a − 2) − (a + 3).",
        "Pārbaudi ar a = 2.",
        "Izdomā izteiksmi, kas vienkāršojas līdz skaitlim.",
    ]),
]
