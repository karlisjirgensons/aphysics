# -*- coding: utf-8 -*-
"""9. klase, 124. stunda: «Kas ir skaitļu virkne?»

Virkne ir sanumurēts skaitļu saraksts: a_1, a_2, a_3, ... Stunda sākas ar
kvadrātiem no sērkociņiem - katrs nākamais skaitlis ir vienas figūras
sērkociņu skaits, un numurs pasaka, kura tā figūra.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, restis)

TEMA = "Kas ir skaitļu virkne?"

MERKIS = ("Nosauksim virknes locekļus un noteiksim to kārtas numuru.")

SATURS = [
    Sakums("Cik sērkociņu vajag n kvadrātiem rindā?",
           zimejums=restis([["kvadrāti", "1", "2", "3", "4", "5"],
                            ["sērkociņi", "4", "7", "10", "13", None]]),
           paraksts="4, 7, 10, 13, ... - tā ir skaitļu virkne.",
           fakti=["Katram skaitlim ir sava vieta - numurs.",
                  "a_1 = 4, a_2 = 7, a_3 = 10.",
                  "Nākamais: a_5 = 16."]),

    Doma("Skaitļu virkne",
         "Skaitļu virkne ir skaitļi, kas sanumurēti ar naturāliem skaitļiem: "
         "a_1, a_2, a_3, ..., a_n, ...",
         soli=[
             "a_n - virknes n-tais loceklis.",
             "n - locekļa kārtas numurs (1, 2, 3, ...).",
             "Virkne var būt galīga vai bezgalīga.",
             "Secība ir svarīga: 1, 2, 3 un 3, 2, 1 ir dažādas virknes.",
         ]),

    Varianti("Nosauc locekli", [
        {"jaut": "Virkne 5, 9, 13, 17, 21. a_3 = ?",
         "opcijas": ["13", "9", "3", "17"],
         "pareizi": 0, "padoms": "Trešais skaitlis."},
        {"jaut": "Tai pašai virknei: kurš ir loceklis 21?",
         "opcijas": ["a_5", "a_{21}", "a_4", "a_6"],
         "pareizi": 0, "padoms": "Piektā vietā."},
        {"jaut": "Virkne 2, 4, 8, 16, ... Nākamais loceklis?",
         "opcijas": ["32", "20", "24", "18"],
         "pareizi": 0, "padoms": "Divkāršo."},
        {"jaut": "Kurš apgalvojums ir patiess?",
         "opcijas": ["a_n ir loceklis ar numuru n", "n ir locekļa vērtība",
                     "a_1 vienmēr ir 1", "Virknei jābūt augošai"],
         "pareizi": 0, "padoms": "Indekss - numurs."},
    ]),

    Ievadi("Turpini virkni", [
        {"jaut": "3, 8, 13, 18, ... a_5 = ?", "atb": ["23"],
         "padoms": "+5."},
        {"jaut": "100, 90, 80, ... a_6 = ?", "atb": ["50"],
         "padoms": "−10."},
        {"jaut": "1, 4, 9, 16, ... a_6 = ?", "atb": ["36"],
         "padoms": "Kvadrāti."},
        {"jaut": "1, 1, 2, 3, 5, 8, ... a_7 = ?", "atb": ["13"],
         "padoms": "Divu iepriekšējo summa."},
        {"jaut": "Sērkociņu virkne: a_5 = ?", "atb": ["16"],
         "padoms": "+3."},
    ], pamats=3),

    Pasaule("Fibonači un saulespuķe",
            Ievadi("", [
                {"jaut": "Saulespuķes sēklu spirāļu skaits ir Fibonači virknē: "
                         "..., 21, 34, 55, ... Nākamais?", "atb": ["89"],
                 "padoms": "34 + 55."},
                {"jaut": "Un vēl nākamais?", "atb": ["144"],
                 "padoms": "55 + 89."},
            ]),
            pavediens="daba",
            konteksts="Saulespuķē sēklas sakārtojas spirālēs, un to skaits "
                      "bieži ir Fibonači skaitlis.",
            kapec="Virknes apraksta arī dabu."),

    Kopsavilkums([
        "Zinu, kas ir skaitļu virkne un tās loceklis.",
        "Pierakstu locekli ar indeksu a_n.",
        "Turpinu virkni pēc likumsakarības.",
    ]),

    Majas([
        "Atrodi 3 virknes ikdienā (cenas, laiki, skaiti).",
        "Uzraksti Fibonači virknes pirmos 12 locekļus.",
        "Saskaiti saulespuķes vai čiekura spirāles, ja vari.",
    ]),
]
