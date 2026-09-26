# -*- coding: utf-8 -*-
"""2. klase, 126. stunda: «Kā reizināšana palīdz dalīt?»

Reizināšana un dalīšana ir pretējas: 2 · 5 = 10, tāpēc 10 : 2 = 5 un
10 : 5 = 2. Katram reizinājumam ir divi dalījumi - trīs skaitļi veido
«ģimeni». Dalot jautā: ar ko jāreizina 2, lai iegūtu 10?
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, rutinas)

TEMA = "Kā reizināšana palīdz dalīt?"

MERKIS = ("Šodien paskaidrosim sakarību starp reizināšanu un dalīšanu "
          "(2 · 5 = 10 un 10 : 2 = 5).")

SATURS = [
    Sakums("Ja zini 2 · 5 = 10, vai zini arī 10 : 2?",
           zimejums=rutinas(5, 2),
           paraksts="2 rindas pa 5 = 10. 10 : 2 = 5.",
           fakti=["Viens attēls - trīs skaitļi: 2, 5, 10.",
                  "2 · 5 = 10 un 5 · 2 = 10.",
                  "10 : 2 = 5 un 10 : 5 = 2."]),

    Doma("Pretējās darbības",
         "Dalīšanu pārbauda un atrod ar reizināšanu.",
         soli=[
             "Dalīšana 14 : 2 = ?",
             "Pajautā: ar ko jāreizina 2, lai būtu 14?",
             "2 · 7 = 14.",
             "Tātad 14 : 2 = 7.",
         ]),

    Slidnis("Skaitļu ģimene 2, 6, 12", [
        {"v": "6 · 2 = 12", "teksts": "6 kolonnas pa 2 rūtiņām.",
         "zim": rutinas(6, 2)},
        {"v": "12 : 2 = 6", "teksts": "12 divās rindās - katrā 6.",
         "zim": rutinas(6, 2)},
        {"v": "12 : 6 = 2", "teksts": "12 sešās kolonnās - katrā 2.",
         "zim": rutinas(6, 2)},
    ]),

    Ievadi("Ģimenes", [
        {"jaut": "2 · 7 = 14, tātad 14 : 2 = ?", "atb": ["7"],
         "padoms": "Tie paši skaitļi."},
        {"jaut": "2 · 9 = 18, tātad 18 : 9 = ?", "atb": ["2"],
         "padoms": "Tie paši skaitļi."},
        {"jaut": "16 : 2 = ?, jo 2 · ? = 16", "atb": ["8"],
         "padoms": "2 · 8."},
        {"jaut": "20 : 2 = ?", "atb": ["10"], "padoms": "2 · 10 = 20."},
        {"jaut": "12 : 6 = ?", "atb": ["2"], "padoms": "6 · 2 = 12."},
        {"jaut": "10 : 5 = ?", "atb": ["2"], "padoms": "5 · 2 = 10."},
    ], pamats=4),

    Varianti("Kurš dalījums?", [
        {"jaut": "Zināms 2 · 4 = 8. Kurš dalījums pareizs?",
         "opcijas": ["8 : 2 = 4", "8 : 4 = 4", "4 : 2 = 8"], "pareizi": 0,
         "padoms": "Tie paši trīs skaitļi."},
        {"jaut": "Kā pārbaudīt 18 : 2 = 9?",
         "opcijas": ["2 · 9 = 18", "18 + 2", "9 − 2"], "pareizi": 0,
         "padoms": "Ar reizināšanu."},
    ]),

    Pasaule("Galda klāšana",
            Ievadi("", [
                {"jaut": "Uz galda 14 dakšiņas - katram viesim 2. Cik viesu? "
                         "14 : 2 = ?", "atb": ["7"], "padoms": "2 · 7 = 14."},
            ]),
            pavediens="virtuve",
            konteksts="Svētku galdā katram viesim ir nazis un dakšiņa.",
            kapec="Reizināšanas tabula palīdz dalīt."),

    Kopsavilkums([
        "Zinu, ka dalīšana ir pretēja reizināšanai.",
        "Atrodu dalījumu ar reizināšanu.",
        "Pārbaudu dalīšanu ar reizināšanu.",
    ]),

    Majas([
        "Uzraksti 3 skaitļu ģimenes ar 2.",
        "Katrai - 2 reizinājumi un 2 dalījumi.",
        "Paskaidro mājiniekam.",
    ]),
]
