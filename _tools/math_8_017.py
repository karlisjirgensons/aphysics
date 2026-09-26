# -*- coding: utf-8 -*-
"""8. klase, 17. stunda: «Kad izteiksme ir pakāpe?»

Temata sākums. Pakāpe ir vienādu reizinātāju reizinājuma saīsināts
pieraksts. Galvenais jautājums - kas tieši tiek kāpināts: −3^2 un (−3)^2
izskatās līdzīgi, bet pēdējā darbība tajās ir dažāda.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Slidnis, Varianti, kolonnas)

TEMA = "Kad izteiksme ir pakāpe?"

MERKIS = ("Atkārtosim, kas ir pakāpe, un noteiksim, vai izteiksme ir pakāpe, "
          "pēc pēdējās darbības.")

SATURS = [
    Sakums("Rīsu grauds uz šaha galdiņa",
           zimejums=kolonnas([("1.", 1), ("2.", 2), ("3.", 4), ("4.", 8),
                              ("5.", 16), ("6.", 32)]),
           paraksts="Uz katra nākamā lauciņa - divreiz vairāk graudu.",
           fakti=["Uz 64. lauciņa būtu 2⁶³ graudu.",
                  "Tā ir visas pasaules rīsu raža vairākos simtos gadu.",
                  "Pakāpe ir īss pieraksts ļoti gariem reizinājumiem."]),

    Doma("Pakāpe - vienādu reizinātāju reizinājums",
         "a^n = a · a · ... · a (n reizinātāji). Skaitli a sauc par pakāpes "
         "bāzi, n - par kāpinātāju.",
         soli=[
             "Bāze - tas, ko reizina; kāpinātājs - cik reizes.",
             "a^1 = a; a^2 - «a kvadrātā»; a^3 - «a kubā».",
             "Izteiksme ir pakāpe, ja tās pēdējā darbība ir kāpināšana.",
             "−3^2 = −(3 · 3) = −9: kāpina tikai 3.",
             "(−3)^2 = (−3) · (−3) = 9: kāpina visu iekavās.",
         ],
         pieze="Kalkulatorā un izklājlapā pakāpi raksta ar ^ zīmi: 2^10."),

    Slidnis("Kas tiek kāpināts?", [
        {"v": "2 · 3^2", "teksts": "Vispirms 3^2 = 9, tad · 2 = 18. Pēdējā - "
                                   "reizināšana: nav pakāpe"},
        {"v": "(2 · 3)^2", "teksts": "Vispirms 6, tad 6^2 = 36. Pēdējā - "
                                     "kāpināšana: pakāpe"},
        {"v": "−5^2", "teksts": "5^2 = 25, tad pretējais: −25. Nav pakāpe"},
        {"v": "(−5)^2", "teksts": "(−5) · (−5) = 25. Pakāpe ar bāzi −5"},
    ], ievads="Darbību secība: kāpināšana notiek pirms reizināšanas."),

    Paraugs("Aprēķini un nosaki",
            uzd="Aprēķini 5^3, (−2)^4, −2^4 un (0,3)^2.",
            soli=[
                ("5^3 = 5 · 5 · 5 = 125", "Trīs reizinātāji."),
                ("(−2)^4 = 16", "Pāra skaits mīnusu."),
                ("−2^4 = −16", "Kāpina tikai 2."),
                ("(0,3)^2 = 0,09", "0,3 · 0,3 - divi cipari aiz komata."),
            ],
            atbilde="125; 16; −16; 0,09"),

    Ievadi("Aprēķini", [
        {"jaut": "2^5", "atb": ["32"], "padoms": "2 · 2 · 2 · 2 · 2."},
        {"jaut": "(−3)^3", "atb": ["−27", "-27"], "padoms": "Trīs mīnusi."},
        {"jaut": "−3^2", "atb": ["−9", "-9"], "padoms": "Kāpina tikai 3."},
        {"jaut": "(0,2)^3", "atb": ["0,008", "0.008"],
         "padoms": "3 cipari aiz komata."},
        {"jaut": "({2|3})^2 - atbildi raksti kā a/b",
         "atb": ["{4|9}", "4/9"], "padoms": "{2 · 2|3 · 3}."},
        {"jaut": "10^6", "atb": ["1000000", "1 000 000"],
         "padoms": "6 nulles."},
    ], pamats=4),

    Varianti("Vai tā ir pakāpe?", [
        {"jaut": "3x^2",
         "opcijas": ["Nē - pēdējā darbība ir reizināšana",
                     "Jā, bāze 3x", "Jā, bāze 3", "Jā, bāze x"],
         "pareizi": 0, "padoms": "Kāpina tikai x."},
        {"jaut": "(a + b)^3",
         "opcijas": ["Jā, bāze a + b", "Nē - tā ir summa",
                     "Jā, bāze b", "Nē - trūkst reizināšanas"],
         "pareizi": 0, "padoms": "Iekavas kāpina kopā."},
        {"jaut": "x · x · x · x",
         "opcijas": ["x^4", "4x", "x + 4", "x^3"],
         "pareizi": 0, "padoms": "Četri reizinātāji."},
        {"jaut": "a^2 + a^2",
         "opcijas": ["2a^2 - nav pakāpe", "a^4", "(2a)^2", "a^2"],
         "pareizi": 0, "padoms": "Divi vienādi saskaitāmie."},
    ]),

    Pasaule("Cik datu ietilpst?",
            Ievadi("", [
                {"jaut": "Viens baits ir 8 biti jeb 2^3. Cik dažādu vērtību "
                         "var pierakstīt ar 8 bitiem (2^8)?",
                 "atb": ["256"], "padoms": "2^4 · 2^4 = 16 · 16."},
                {"jaut": "Kilobaits ir 2^10 baitu. Cik tas ir?",
                 "atb": ["1024"], "padoms": "2^5 = 32; 32 · 32."},
                {"jaut": "PIN kods no 4 cipariem: 10^4 variantu. Cik?",
                 "atb": ["10000", "10 000"], "padoms": "10 · 10 · 10 · 10."},
            ]),
            pavediens="kodi",
            konteksts="Datori skaita divnieka pakāpēs, tāpēc atmiņas izmēri ir "
                      "256, 512, 1024 - nevis apaļi simti.",
            kapec="Katrs papildu bits divkāršo iespēju skaitu."),

    Kopsavilkums([
        "Nosaucu pakāpes bāzi un kāpinātāju.",
        "Atšķiru −a^2 no (−a)^2.",
        "Nosaku, vai izteiksme ir pakāpe, pēc pēdējās darbības.",
        "Aprēķinu pakāpes vērtību.",
    ]),

    Majas([
        "Aprēķini 2^1 līdz 2^12 un pieraksti tabulā.",
        "Atrodi, kurā tabulas vietā parādās 1024.",
        "Uzraksti trīs izteiksmes, kas izskatās pēc pakāpes, bet nav.",
    ]),
]
