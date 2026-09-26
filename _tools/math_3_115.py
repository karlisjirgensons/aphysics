# -*- coding: utf-8 -*-
"""3. klase, 115. stunda: «Kā pateikt laukuma aprēķinu ar vārdiem?»

Tāpat kā perimetram 53. stundā - vispirms vārdi, tad burti. Laukuma sakarība
te iegūst arī savu mērvienību: kvadrātcentimetrs, kas ir rūtiņa ar malu 1 cm.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, figura)

TEMA = "Kā pateikt laukuma aprēķinu ar vārdiem?"

MERKIS = ("Formulēsim vārdisku taisnstūra laukuma aprēķināšanas sakarību.")

SATURS = [
    Sakums("Kā vienā teikumā pateikt jebkura taisnstūra laukumu?",
           zimejums=figura([(0, 0), (6, 0), (6, 4), (0, 4)],
                           [(3, -0.7, "a"), (6.8, 2, "b")],
                           "S = a · b"),
           paraksts="Laukumu apzīmē ar burtu S.",
           fakti=["Laukums ir garuma un platuma reizinājums.",
                  "Laukumu mēra kvadrātcentimetros: 1 cm² ir rūtiņa ar malu "
                  "1 cm."]),

    Doma("Laukums ir garuma un platuma reizinājums",
         "S = a · b - šis teikums der jebkuram taisnstūrim.",
         soli=[
             "Izmēri garumu un platumu vienādās mērvienībās.",
             "Reizini abus skaitļus.",
             "Pieraksti rezultātu ar mērvienību: cm² vai m².",
             "Pārbaudi ar rūtiņu skaitīšanu.",
         ],
         pieze="Mērvienībai jābūt vienādai abiem mērījumiem: ja viens ir "
               "metros, bet otrs centimetros, vispirms jāpārvērš."),

    Paraugs("Cik liels ir laukums?",
            uzd="Taisnstūra malas ir 6 cm un 4 cm. Aprēķini laukumu.",
            soli=[
                ("S = a · b",
                 "Vispirms pieraksta sakarību."),
                ("S = 6 · 4",
                 "Ieliek dotos skaitļus."),
                ("S = 24 cm²",
                 "Atbildi raksta ar mērvienību."),
            ],
            atbilde="24 cm²"),

    Ievadi("Aprēķini laukumu", [
        {"jaut": "Taisnstūris 6 cm un 4 cm. Cik ir laukums kvadrātcentimetros?",
         "atb": ["24"], "padoms": "6 · 4."},
        {"jaut": "Taisnstūris 9 cm un 5 cm. Cik ir laukums?", "atb": ["45"],
         "padoms": "9 · 5."},
        {"jaut": "Kvadrāts ar malu 7 cm. Cik ir laukums?", "atb": ["49"],
         "padoms": "7 · 7."},
        {"jaut": "Laukums 56 cm², viena mala 8 cm. Cik ir otra?",
         "atb": ["7"], "padoms": "56 : 8."},
        {"jaut": "Taisnstūris 12 cm un 3 cm. Cik ir laukums?", "atb": ["36"],
         "padoms": "12 · 3."},
        {"jaut": "Laukums 63 cm², viena mala 9 cm. Cik ir otra?",
         "atb": ["7"], "padoms": "63 : 9."},
    ], pamats=4),

    Zimejums("Kvadrāta laukums",
             figura([(0, 0), (5, 0), (5, 5), (0, 5)],
                    [(2.5, -0.7, "a"), (5.8, 2.5, "a")],
                    "S = a · a"),
             paskaidro="Kvadrātam abas malas ir vienādas, tāpēc laukums ir "
                       "malas reizinājums ar sevi.",
             ievads="Īpašais gadījums."),

    Varianti("Kurš teikums ir pareizs?", [
        {"jaut": "Kurš teikums pareizi apraksta laukumu?",
         "opcijas": ["Garuma un platuma reizinājums",
                     "Garuma un platuma summa",
                     "Divas reizes malu summa", "Lielākā mala"],
         "pareizi": 0, "padoms": "Perimetrs ir summa."},
        {"jaut": "Kurā mērvienībā mēra laukumu?",
         "opcijas": ["cm²", "cm", "cm³", "kg"],
         "pareizi": 0, "padoms": "Kvadrātcentimetri."},
        {"jaut": "Kvadrāta mala ir 9 cm. Cik ir laukums?",
         "opcijas": ["81 cm²", "36 cm²", "18 cm²", "9 cm²"],
         "pareizi": 0, "padoms": "9 · 9."},
        {"jaut": "Ko nozīmē 1 cm²?",
         "opcijas": ["Kvadrāts ar malu 1 cm", "Līnija 1 cm gara",
                     "Kubs ar malu 1 cm", "Riņķis ar rādiusu 1 cm"],
         "pareizi": 0, "padoms": "Tā ir viena rūtiņa."},
    ], pamats=4),

    Pasaule("Cik krāsas vajag sienai?",
            Ievadi("", [
                {"jaut": "Siena 5 m un 3 m. Cik kvadrātmetru ir laukums?",
                 "atb": ["15"], "padoms": "5 · 3."},
                {"jaut": "Logs aizņem 2 m². Cik kvadrātmetru jākrāso?",
                 "atb": ["13"], "padoms": "15 − 2."},
                {"jaut": "Viena banka krāsas pietiek 7 m². Cik banku vajag?",
                 "atb": ["2"], "padoms": "13 : 7 ar atlikumu."},
                {"jaut": "Cik kvadrātmetru krāsas paliks pāri?",
                 "atb": ["1"], "padoms": "14 − 13."},
            ]),
            pavediens="maja",
            konteksts="Krāsu pērk pēc laukuma, un uz bankas vienmēr rakstīts, "
                      "cik kvadrātmetru tā noklāj.",
            kapec="Logu un durvju laukumu no sienas atņem - citādi krāsas "
                  "pērk par daudz."),

    Kopsavilkums([
        "Formulēju laukuma aprēķinu vārdiski.",
        "Zinu, ka laukums ir garuma un platuma reizinājums.",
        "Rakstu laukumu ar mērvienību cm² vai m².",
        "Atrodu trūkstošo malu, ja zināms laukums.",
    ]),

    Majas([
        "Izrēķini sava galda virsmas laukumu.",
        "Izrēķini istabas grīdas laukumu kvadrātmetros.",
        "Atrodi mājās virsmu, kuras laukums ir apmēram 1 m².",
    ]),
]
