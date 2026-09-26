# -*- coding: utf-8 -*-
"""9. klase, 47. stunda: «Kāds ir 45° leņķa sinuss?»

Kvadrāta diagonāle sadala to divos vienādsānu taisnleņķa trijstūros ar
katetēm 1 un hipotenūzu √2. No tā: sin 45° = cos 45° = {√2|2}, tg 45° = 1.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, geometrija, taisnlenka)

TEMA = "Kāds ir 45° leņķa sinuss?"

MERKIS = ("Iegūsim 45° leņķa vērtības no vienādsānu taisnleņķa trijstūra.")

SATURS = [
    Sakums("Kvadrāta diagonāle un 45°",
           zimejums=geometrija([("A", 0, 0), ("B", 1, 0), ("C", 1, 1),
                                ("D", 0, 1)],
                               nogriezni=["AB", "BC", "CD", "DA"],
                               izcelti=["AC"], iekrasot=[("ABC", 1)],
                               lenki=[("BAC", "45°")],
                               malas=[("AB", "1"), ("BC", "1"),
                                      ("AC", "√2")]),
           paraksts="Diagonāle dala taisno leņķi uz pusēm.",
           fakti=["Katetes vienādas: 1 un 1.",
                  "Hipotenūza: √(1 + 1) = √2.",
                  "sin 45° = {1|√2} = {√2|2} ≈ 0,707."]),

    Doma("45°",
         "sin 45° = cos 45° = {√2|2}, tg 45° = 1.",
         soli=[
             "Vienādsānu taisnleņķa trijstūrī abi šaurie leņķi 45°.",
             "Katete a, hipotenūza a√2.",
             "{1|√2} = {√2|2} - saucēju atbrīvo no saknes.",
         ],
         pieze="Kvadrāta diagonāle d = a√2 - tā pati sakarība."),

    Paraugs("Kvadrāta diagonāle",
            uzd="Kvadrāta mala 6 cm. Atrodi diagonāli.",
            soli=[
                ("cos 45° = {6|d}", "Trijstūris ar hipotenūzu d."),
                ("d = {6|cos 45°} = 6 : {√2|2} = 6√2", "Aprēķins."),
                ("d ≈ 8,49 cm", "√2 ≈ 1,414."),
            ],
            atbilde="6√2 ≈ 8,49 cm"),

    Ievadi("Aprēķini", [
        {"jaut": "Katete 5, leņķis 45°. Otra katete?", "atb": ["5"],
         "padoms": "tg 45° = 1."},
        {"jaut": "Katete 3. Hipotenūza = 3√?", "atb": ["2"],
         "padoms": "a√2."},
        {"jaut": "Hipotenūza 4√2. Katete?", "atb": ["4"],
         "padoms": "4√2 · {√2|2} = 4."},
        {"jaut": "Kvadrāta diagonāle 10. Mala ≈ ? (līdz simtdaļām)",
         "atb": ["7,07"], "padoms": "10 : 1,414."},
        {"jaut": "sin 45° · cos 45° = ? (decimāldaļa)", "atb": ["0,5"],
         "padoms": "{2|4}."},
    ], pamats=3),

    Varianti("Izvēlies", [
        {"jaut": "cos 45° = ?",
         "opcijas": ["{√2|2}", "{1|2}", "1", "√2"],
         "pareizi": 0, "padoms": "Tāds pats kā sin 45°."},
        {"jaut": "Kvadrāta ar malu a diagonāle ir",
         "opcijas": ["a√2", "2a", "a√3", "{a|2}"],
         "pareizi": 0, "padoms": "Pitagors: a^2 + a^2."},
        {"jaut": "Kurā leņķī tg α = 1?",
         "opcijas": ["45°", "30°", "60°", "90°"],
         "pareizi": 0, "padoms": "Katetes vienādas."},
    ]),

    Pasaule("Futbola laukuma diagonāle",
            Ievadi("", [
                {"jaut": "Kvadrātveida treniņlaukums 40 m × 40 m. Skrējiens "
                         "pa diagonāli ≈ ? m (līdz veseliem)",
                 "atb": ["57"], "padoms": "40 · 1,414 = 56,6."},
                {"jaut": "Cik m ietaupa, skrienot pa diagonāli, nevis gar "
                         "divām malām? (līdz veseliem)",
                 "atb": ["23"], "padoms": "80 − 56,6."},
            ]),
            pavediens="sports",
            konteksts="Treneris liek skriet pa kvadrātveida laukuma "
                      "diagonāli; tās virziens ar malu veido 45°.",
            kapec="Diagonāle = mala · √2.",
            zimejums=taisnlenka(4, 4, ("40 m", "40 m", "?"), "45°")),

    Kopsavilkums([
        "Iegūstu 45° vērtības no kvadrāta.",
        "Zinu: sin 45° = cos 45° = {√2|2}, tg 45° = 1.",
        "Aprēķinu kvadrāta diagonāli.",
    ]),

    Majas([
        "Izmēri grāmatas kvadrātveida vāka diagonāli un pārbaudi a√2.",
        "Aprēķini: sin^2 45° + cos^2 45°.",
        "Paskaidro, kāpēc {1|√2} = {√2|2}.",
    ]),
]
