# -*- coding: utf-8 -*-
"""8. klase, 21. stunda: «Kā kāpina reizinājumu un daļu?»

(ab)^n = a^n b^n: katru reizinātāju kāpina atsevišķi. Kvadrāta laukums ar
malu 3a to parāda redzami - 9 mazi kvadrātiņi. Daļai tas pats: kāpina gan
skaitītāju, gan saucēju.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, kvadrats)

TEMA = "Kā kāpina reizinājumu un daļu?"

MERKIS = ("Kāpināsim reizinājumu un daļu un pierakstīsim rezultātu "
          "vienkāršotā veidā.")

SATURS = [
    Sakums("Kvadrāts ar malu 3a",
           zimejums=kvadrats(3, 3, paraksts="(3a)² = 9a²"),
           paraksts="Katrs mazais kvadrātiņš ir a². Kopā - deviņi.",
           fakti=["(3a)² = 3² · a² = 9a².",
                  "Kāpina katru reizinātāju.",
                  "3a² ir cits - tur kāpina tikai a."]),

    Doma("Reizinājuma un daļas kāpināšana",
         "Kāpinot reizinājumu, kāpina katru reizinātāju: (ab)^n = a^n b^n. "
         "Kāpinot daļu, kāpina skaitītāju un saucēju: ({a|b})^n = "
         "{a^n|b^n}.",
         soli=[
             "Nosaki visus reizinātājus iekavās (arī skaitli un mīnusu).",
             "Katru kāpini ar iekavu kāpinātāju.",
             "Ja reizinātājs jau ir pakāpe - reizini kāpinātājus.",
             "Pēc tam aprēķini skaitlisko koeficientu.",
         ],
         pieze="Summai tā nedrīkst: (a + b)^2 nav a^2 + b^2. Pārbaude: "
               "(1 + 2)^2 = 9, bet 1 + 4 = 5."),

    Paraugs("Viss uzreiz",
            uzd="Vienkāršo (−2x^3y)^4.",
            soli=[
                ("(−2)^4 = 16", "Pāra kāpinātājs - pluss."),
                ("(x^3)^4 = x^{12}", "Kāpinātāji reizinās."),
                ("y^4", "y kāpina tāpat."),
                ("16x^{12}y^4", "Kopā."),
            ],
            atbilde="16x^{12}y^4"),

    Ievadi("Kāpini", [
        {"jaut": "(2a)^3", "atb": ["8a^3"], "padoms": "2^3 · a^3.",
         "tastatura": "text"},
        {"jaut": "(xy)^5", "atb": ["x^5y^5"], "padoms": "Katru.",
         "tastatura": "text"},
        {"jaut": "(−3b^2)^2", "atb": ["9b^4"], "padoms": "9 · b^4.",
         "tastatura": "text"},
        {"jaut": "({2|5})^3 - atbildi raksti kā a/b",
         "atb": ["{8|125}", "8/125"], "padoms": "{2^3|5^3}."},
        {"jaut": "(10a^2)^3", "atb": ["1000a^6"], "padoms": "10^3 · a^6.",
         "tastatura": "text"},
        {"jaut": "(−a^3)^3", "atb": ["−a^9", "-a^9"], "padoms": "Nepāra.",
         "tastatura": "text"},
    ], pamats=4),

    Varianti("Pareizi vai nē?", [
        {"jaut": "(3x)^2 = 3x^2",
         "opcijas": ["Kļūda: 9x^2", "Pareizi", "Kļūda: 6x^2",
                     "Kļūda: 9x"],
         "pareizi": 0, "padoms": "Kāpina arī 3."},
        {"jaut": "(a + b)^2 = a^2 + b^2",
         "opcijas": ["Kļūda - tā ir summa, ne reizinājums", "Pareizi",
                     "Pareizi tikai pozitīviem", "Kļūda: 2a + 2b"],
         "pareizi": 0, "padoms": "Pārbaudi ar a = 1, b = 2."},
        {"jaut": "({x|3})^2 = {x^2|3}",
         "opcijas": ["Kļūda: {x^2|9}", "Pareizi", "Kļūda: {2x|6}",
                     "Kļūda: {x|9}"],
         "pareizi": 0, "padoms": "Kāpina arī saucēju."},
    ]),

    Pasaule("Fotogrāfijas palielināšana",
            Ievadi("", [
                {"jaut": "Fotogrāfijas malas palielina 3 reizes. Cik reižu "
                         "palielinās laukums?",
                 "atb": ["9"], "padoms": "(3a)(3b) = 9ab."},
                {"jaut": "Bilde 10 × 15 cm (150 cm²). Kāds laukums pēc "
                         "palielināšanas 3 reizes?",
                 "atb": ["1350"], "padoms": "150 · 9."},
                {"jaut": "Kuba malu palielina 2 reizes. Cik reižu palielinās "
                         "tilpums?",
                 "atb": ["8"], "padoms": "(2a)^3."},
            ]),
            pavediens="tehnika",
            konteksts="Divreiz lielāka pica nav divreiz vairāk picas - "
                      "laukums aug kvadrātā.",
            kapec="Tāpēc lielais iepakojums bieži ir izdevīgāks."),

    Kopsavilkums([
        "Kāpinu reizinājumu: katru reizinātāju.",
        "Kāpinu daļu: skaitītāju un saucēju.",
        "Nosaku zīmi, kāpinot negatīvu reizinātāju.",
        "Zinu, ka summu tā kāpināt nedrīkst.",
    ]),

    Majas([
        "Vienkāršo: (4y)^2, (−2a^2b)^3, ({3|x})^2.",
        "Pārbaudi (a + b)^2 ≠ a^2 + b^2 ar diviem skaitļu pāriem.",
        "Atrodi veikalā divus picas izmērus un salīdzini laukumus.",
    ]),
]
