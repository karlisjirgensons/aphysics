# -*- coding: utf-8 -*-
"""7. klase, 133. stunda: «Kā vienādojumu atrisināt spriežot?»

Vienkāršu vienādojumu var atrisināt, spriežot par darbību komponentiem:
nezināmais saskaitāmais = summa − zināmais saskaitāmais; nezināmais
reizinātājs = reizinājums : zināmais. «Ejot atpakaļ» no ārējās darbības uz
iekšējo, atrisina arī vairāku soļu vienādojumus.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kā vienādojumu atrisināt spriežot?"

MERKIS = ("Atrisināsim vienkāršu vienādojumu, spriežot par sakarībām starp "
          "lielumiem.")

SATURS = [
    Sakums("Burvja triks atpakaļgaitā",
           zimejums=restis([["uz priekšu", "atpakaļ"],
                            ["x", "7"],
                            ["· 3 → 3x", ": 3 ← 21"],
                            ["+ 5 → 3x + 5", "− 5 ← 26"],
                            ["= 26", "26"]]),
           paraksts="3x + 5 = 26: ej atpakaļ - x = 7.",
           fakti=["Pēdējā darbība bija + 5 - to atceļ pirmo.",
                  "Tad atceļ · 3.",
                  "Tā ir spriešana, nevis minēšana."]),

    Doma("Atceļ darbības otrādā secībā",
         "Spriežot vienādojumu atrisina, katru darbību ar nezināmo atceļot "
         "ar pretējo darbību otrādā secībā: vispirms pēdējo izpildīto.",
         soli=[
             "Nezināmais saskaitāmais: summa − zināmais.",
             "Nezināmais mazināmais: starpība + mazinātājs.",
             "Nezināmais reizinātājs: reizinājums : zināmais.",
             "Nezināmais dalāmais: dalījums · dalītājs.",
         ],
         pieze="Vairāku soļu vienādojumā vispirms «atraisa» ārējo darbību: "
               "3x + 5 = 26 - sākumā 3x ir nezināmais saskaitāmais."),

    Paraugs("Spriežot",
            uzd="Atrisini 4(x − 2) = 20.",
            soli=[
                ("x − 2 ir nezināmais reizinātājs: 20 : 4 = 5", "x − 2 = 5."),
                ("x ir nezināmais mazināmais: 5 + 2 = 7", "x = 7."),
                ("Pārbaude: 4(7 − 2) = 20", "Pareizi."),
            ],
            atbilde="x = 7"),

    Ievadi("Atrisini spriežot", [
        {"jaut": "x + 17 = 42",
         "atb": ["25"], "padoms": "42 − 17."},
        {"jaut": "56 − x = 20",
         "atb": ["36"], "padoms": "Nezināmais mazinātājs: 56 − 20."},
        {"jaut": "{x|4} = 9",
         "atb": ["36"], "padoms": "9 · 4."},
        {"jaut": "2x + 7 = 31",
         "atb": ["12"], "padoms": "2x = 24."},
        {"jaut": "{x + 3|5} = 4",
         "atb": ["17"], "padoms": "x + 3 = 20."},
        {"jaut": "3(x + 4) = 27",
         "atb": ["5"], "padoms": "x + 4 = 9."},
    ], pamats=4),

    Varianti("Kura darbība pirmā?", [
        {"jaut": "5x − 3 = 22. Ko atceļ vispirms?",
         "opcijas": ["− 3 (pieskaita 3)", "· 5 (dala ar 5)",
                     "Neko", "Abas reizē"],
         "pareizi": 0, "padoms": "Pēdējā izpildītā."},
        {"jaut": "{x − 1|3} = 4. Ko atceļ vispirms?",
         "opcijas": [": 3 (reizina ar 3)", "− 1", "Neko", "Abas reizē"],
         "pareizi": 0, "padoms": "Dalīšana notika pēdējā."},
    ]),

    Pasaule("Cik bija sākumā?",
            Ievadi("", [
                {"jaut": "Maks iztērēja pusi kabatas naudas un vēl 4 €; "
                         "palika 11 €. Cik bija sākumā? ({x|2} − 4 = 11)",
                 "atb": ["30"], "padoms": "{x|2} = 15."},
                {"jaut": "Temperatūra dubultojās un pazeminājās par 3 grādiem "
                         "līdz 9 °C. Kāda bija sākumā?",
                 "atb": ["6"], "padoms": "2x − 3 = 9."},
                {"jaut": "Skaitli reizināja ar 3, pieskaitīja 8 un ieguva 50. "
                         "Skaitlis?",
                 "atb": ["14"], "padoms": "3x = 42."},
            ]),
            pavediens="veikals",
            konteksts="Uzdevumi «cik bija sākumā?» risināmi atpakaļgaitā - "
                      "tāpat kā vienādojumi.",
            kapec="Spriešana ir metode, ne minēšana."),

    Kopsavilkums([
        "Atrisinu vienādojumu, atceļot darbības otrādā secībā.",
        "Lietoju komponentu sakarības.",
        "Vispirms atceļu pēdējo izpildīto darbību.",
        "Pārbaudu sakni.",
    ]),

    Majas([
        "Atrisini spriežot: 6(x − 5) = 42; {x|3} + 4 = 10.",
        "Izdomā «iedomājies skaitli» triku un atrisini to atpakaļ.",
        "Uzraksti 2 «cik bija sākumā?» uzdevumus.",
    ]),
]
