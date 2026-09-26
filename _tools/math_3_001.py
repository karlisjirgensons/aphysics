# -*- coding: utf-8 -*-
"""3. klase, 1. stunda: «Ko jau proti no reizināšanas tabulas?»

Gada pirmā stunda. Reizināšanas tabula nav jāsāk no nulles - ar 2, 3, 4 un 5
skolēns rēķina jau kopš otrās klases. Tāpēc stunda vispirms parāda, cik daudz
jau ir padarīts, un tikai tad nosauc to gabalu, kas vēl paliek: reizinājumus
ar 6, 7, 8 un 9. No šīs kartes aug viss temats.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Ko jau proti no reizināšanas tabulas?"

MERKIS = ("Atkārtosim reizināšanu un dalīšanu ar 2, 3, 4 un 5 un atzīmēsim, "
          "kuri reizinājumi vēl jāiemācās.")

SATURS = [
    Sakums("Cik daudz no tabulas tu jau zini?",
           zimejums=restis([[2, 4, 6, 8, 10],
                            [3, 6, 9, 12, 15],
                            [4, 8, 12, 16, 20],
                            [5, 10, 15, 20, 25]],
                           "reizinājumi ar 2, 3, 4 un 5"),
           paraksts="Šos četrus stāvus tu jau esi uzkāpis pagājušajā gadā.",
           fakti=["Visā reizināšanas tabulā ir 100 reizinājumu.",
                  "Ar 2, 3, 4 un 5 tu proti jau 40 no tiem.",
                  "Šogad jāpieliek tikai 6, 7, 8, 9 un 10."]),

    Doma("Reizināšana ir vienādu grupu saskaitīšana",
         "5 · 4 nozīmē: pieci gabali, katrā četri - un tā ir īsa pieraksta "
         "forma summai 4 + 4 + 4 + 4 + 4.",
         soli=[
             "Pasaki, cik ir grupu - tas ir pirmais skaitlis.",
             "Pasaki, cik ir katrā grupā - tas ir otrais skaitlis.",
             "Saskaiti visu kopā vai atceries reizinājumu no tabulas.",
             "Pārbaudi: vai atbilde ir lielāka par katru no skaitļiem?",
         ],
         pieze="Tāpēc tabulu māca no galvas: skaitīt 4 + 4 + 4 + 4 + 4 var "
               "vienmēr, bet *atcerēties* 20 ir daudz ātrāk."),

    Paraugs("Cik riteņu ir piecos trīsriteņos?",
            uzd="Skolas pagalmā stāv 5 trīsriteņi. Cik riteņu ir pavisam?",
            soli=[
                ("5 trīsriteņi, katram 3 riteņi",
                 "Vispirms saprot, kas ir grupa un kas ir grupas lielums."),
                ("3 + 3 + 3 + 3 + 3",
                 "Tā izskatās šis pats rēķins ar saskaitīšanu."),
                ("5 · 3 = 15",
                 "Reizināšana pasaka to pašu īsāk."),
            ],
            atbilde="15 riteņu"),

    Ievadi("Atceries tabulu", [
        {"jaut": "4 · 5 = ?", "atb": ["20"],
         "padoms": "Četras piecnieku grupas: 5, 10, 15, 20."},
        {"jaut": "3 · 8 = ?", "atb": ["24"],
         "padoms": "Skaiti pa trim: 3, 6, 9, 12, 15, 18, 21, 24."},
        {"jaut": "2 · 9 = ?", "atb": ["18"],
         "padoms": "Divkārši deviņus: 9 + 9."},
        {"jaut": "5 · 7 = ?", "atb": ["35"],
         "padoms": "Skaiti pa pieciem septiņas reizes."},
        {"jaut": "24 : 4 = ?", "atb": ["6"],
         "padoms": "Kurš skaitlis, reizināts ar 4, dod 24?"},
        {"jaut": "35 : 5 = ?", "atb": ["7"],
         "padoms": "Kurš skaitlis, reizināts ar 5, dod 35?"},
    ], pamats=4,
        ievads="Ieraksti atbildi un spied «Pārbaudīt»."),

    Zimejums("Kas vēl nav apgūts",
             restis([["6 ·", "?", "?", "?", "?"],
                     ["7 ·", "?", "?", "?", "?"],
                     ["8 ·", "?", "?", "?", "?"],
                     ["9 ·", "?", "?", "?", "?"]],
                    "šos stāvus celsim šogad"),
             paskaidro="Katrā rindā ir tikai daži reizinājumi, ko tu vēl "
                       "nezini - pārējos jau proti no otras puses.",
             ievads="Šī ir tabulas otra puse - tā, kuru sāksim nākamajā "
                    "stundā."),

    Varianti("Kurš pieraksts ir pareizs?", [
        {"jaut": "Kā pierakstīt «trīs grupas pa sešiem»?",
         "opcijas": ["3 · 6", "6 : 3", "3 + 6", "6 − 3"],
         "pareizi": 0,
         "padoms": "Vispirms grupu skaits, tad grupas lielums."},
        {"jaut": "Kurš rēķins ir tas pats, kas 4 + 4 + 4?",
         "opcijas": ["3 · 4", "4 · 4", "3 + 4", "12 : 4"],
         "pareizi": 0,
         "padoms": "Saskaiti, cik reižu četrinieks parādās."},
        {"jaut": "Kurš rezultāts *nevar* būt pareizs reizinājumam 5 · 6?",
         "opcijas": ["11", "30", "2 · 15", "6 · 5"],
         "pareizi": 0,
         "padoms": "Reizinājums ir daudz lielāks par summu 5 + 6."},
        {"jaut": "Ko nozīmē 20 : 5?",
         "opcijas": ["20 sadala 5 vienādās daļās", "20 pieskaita 5",
                     "20 reizina ar 5", "no 20 atņem 5"],
         "pareizi": 0,
         "padoms": "Dalīšana ir sadalīšana vienādās daļās."},
    ], pamats=4),

    Pasaule("Cik kāju ir uz pļavas?",
            Ievadi("", [
                {"jaut": "Vienai vabolei ir 6 kājas. Cik kāju ir 2 vabolēm?",
                 "atb": ["12"], "padoms": "6 + 6."},
                {"jaut": "Zirneklim ir 8 kājas. Cik kāju ir 2 zirnekļiem?",
                 "atb": ["16"], "padoms": "8 + 8."},
                {"jaut": "Cik kāju ir 5 putniem, ja katram ir 2 kājas?",
                 "atb": ["10"], "padoms": "5 · 2."},
                {"jaut": "Uz zieda sēž 4 bites. Cik kāju ir kopā, ja katrai "
                         "ir 6?",
                 "atb": ["24"], "padoms": "6 + 6 + 6 + 6 jeb 4 · 6."},
            ]),
            pavediens="daba",
            konteksts="Kukaiņiem ir 6 kājas, zirnekļiem 8, putniem 2 - "
                      "dabā vienādas grupas ir gandrīz visur.",
            kapec="Kad grupas ir vienādas, nekad nav jāskaita pa vienam."),

    Kopsavilkums([
        "Zinu, ka reizināšana ir vienādu grupu saskaitīšana.",
        "Veikli rēķinu reizinājumus ar 2, 3, 4 un 5.",
        "Atrodu dalījumu, domājot par atbilstošo reizinājumu.",
        "Zinu, kuri reizinājumi man vēl jāiemācās.",
    ]),

    Majas([
        "Saskaiti, cik kāju ir visiem dzīvniekiem, kas dzīvo jūsu mājās.",
        "Atrodi virtuvē kaut ko, kas stāv vienādās grupās, un pieraksti "
        "reizinājumu.",
        "Pasaki skaļi visu piecnieku rindu: 5, 10, 15, ... līdz 50.",
    ], ievads="Reizināšanu visvieglāk atcerēties tur, kur grupas var "
              "aptaustīt."),
]
