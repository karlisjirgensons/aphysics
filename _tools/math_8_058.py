# -*- coding: utf-8 -*-
"""8. klase, 58. stunda: «Kā izvilkt sakni no daļas?»

√{a|b} = {√a|√b}, ja a ≥ 0 un b > 0. Kvadrāts 4 × 4 rūtiņās ar iekrāsotu
3 × 3 daļu rāda, ka laukumam {9|16} mala ir {3|4}. Vienkāršots pieraksts
saucējā sakni neatstāj: {6|√2} = 3√2.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, kvadrats)

TEMA = "Kā izvilkt sakni no daļas?"

MERKIS = ("Lietosim dalījuma saknes īpašību un pierakstīsim rezultātu "
          "vienkāršotā veidā.")

SATURS = [
    Sakums("√{9|16} - cik tas ir?",
           zimejums=kvadrats(4, 4, 3, 3),
           paraksts="Iekrāsotā kvadrāta laukums ir {9|16}, mala - {3|4}.",
           fakti=["√{a|b} = {√a|√b}, ja a ≥ 0 un b > 0.",
                  "√{9|16} = {3|4}, jo {3|4} · {3|4} = {9|16}.",
                  "Vienkāršotā pierakstā saucējā saknes nav."]),

    Doma("Dalījuma sakne",
         "Daļas sakne ir skaitītāja sakne, dalīta ar saucēja sakni.",
         soli=[
             "Sakni velk atsevišķi: √{25|49} = {5|7}.",
             "Decimāldaļu pārveido par daļu: √(0,36) = √{36|100} = {6|10} "
             "= 0,6.",
             "Dalot saknes, apvieno tās: {√72|√2} = √36 = 6.",
             "Ja saucējā paliek sakne, reizina ar to: {3|√3} = {3√3|3} = √3.",
         ],
         pieze="Jauktu skaitli vispirms pārveido par daļu: 2,25 = {9|4}, "
               "tāpēc √(2,25) = {3|2} = 1,5."),

    Paraugs("Trīs gadījumi",
            uzd="Aprēķini √{121|144} un {√50|√2}, vienkāršo {6|√2}.",
            soli=[
                ("√{121|144} = {√121|√144} = {11|12}", "Sakne no skaitītāja "
                                                       "un saucēja."),
                ("{√50|√2} = √25 = 5", "Apvieno zem vienas saknes."),
                ("{6|√2} = {6√2|2} = 3√2", "Skaitītāju un saucēju reizina "
                                            "ar √2."),
            ],
            atbilde="{11|12}; 5; 3√2"),

    Ievadi("Aprēķini", [
        {"jaut": "√{16|25} = ?", "atb": ["{4|5}", "4/5", "0,8"],
         "padoms": "{√16|√25}."},
        {"jaut": "√(0,81) = ?", "atb": ["0,9"], "padoms": "√{81|100}."},
        {"jaut": "{√98|√2} = ?", "atb": ["7"], "padoms": "√49."},
        {"jaut": "{√3|√75} = ?", "atb": ["{1|5}", "1/5", "0,2"],
         "padoms": "√{3|75} = √{1|25}."},
        {"jaut": "√(6,25) = ?", "atb": ["2,5"], "padoms": "√{625|100}."},
        {"jaut": "{10|√5} = a√5. a = ?", "atb": ["2"],
         "padoms": "{10√5|5}."},
    ], pamats=4),

    Varianti("Izvēlies pareizo", [
        {"jaut": "√{1|4} = ?",
         "opcijas": ["{1|2}", "{1|4}", "{1|16}", "2"],
         "pareizi": 0, "padoms": "{1|2} · {1|2} = {1|4}."},
        {"jaut": "{√18|√2} = ?",
         "opcijas": ["3", "9", "√16", "√{9|2}"],
         "pareizi": 0, "padoms": "√9."},
        {"jaut": "Kurā pierakstā saucējā nav saknes?",
         "opcijas": ["{√5|5}", "{1|√5}", "{2|√20}", "{√1|√5}"],
         "pareizi": 0, "padoms": "Visi četri ir vienādi, bet tikai viens "
                                 "vienkāršots."},
    ]),

    Pasaule("Attēla izmērs",
            Ievadi("", [
                {"jaut": "Attēla laukumu samazina 4 reizes, saglabājot formu. "
                         "Cik reizes samazinās platums?",
                 "atb": ["2"], "padoms": "√{1|4} = {1|2}."},
                {"jaut": "Kvadrātveida foto ir 16 cm × 16 cm. Kopijas laukums "
                         "ir {9|16} no oriģināla. Kopijas mala (cm)?",
                 "atb": ["12"], "padoms": "16 · {3|4}."},
                {"jaut": "Kvadrātveida ekrāna laukums ir 0,49 m². Cik m ir "
                         "mala?",
                 "atb": ["0,7"], "padoms": "√{49|100}."},
            ]),
            pavediens="dati",
            konteksts="Mainot attēla izmēru, laukums mainās ar malas "
                      "kvadrātu. Malu iegūst ar sakni no laukumu attiecības.",
            kapec="Tāpēc 4 reizes mazāks attēls ir tikai 2 reizes šaurāks."),

    Kopsavilkums([
        "Izvelku sakni no daļas: no skaitītāja un saucēja atsevišķi.",
        "Dalu saknes, apvienojot tās zem vienas saknes.",
        "Pārnesu sakni no saucēja uz skaitītāju.",
    ]),

    Majas([
        "Aprēķini: √{36|121}, √(0,04), {√200|√8}.",
        "Vienkāršo: {4|√2}, {15|√5}.",
        "Nokopē attēlu ar laukumu {1|9} no oriģināla un nomēri platumu.",
    ]),
]
