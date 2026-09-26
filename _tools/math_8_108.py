# -*- coding: utf-8 -*-
"""8. klase, 108. stunda: «Kas ir monoms?»

Temata 8.6. sākums. Monoms - skaitļu, mainīgo un to naturālu pakāpju
reizinājums; koeficients - tā skaitliskais reizinātājs. Summa un dalīšana
ar mainīgo monomu neveido. Monomi jau bija formulās: πr^2, 5t^2, a^3.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, restis)

TEMA = "Kas ir monoms?"

MERKIS = "Noteiksim, vai izteiksme ir monoms, un nosauksim tā koeficientu."

SATURS = [
    Sakums("Kuras izteiksmes ir monomi?",
           zimejums=restis([["3a²b", "monoms"],
                            ["−x", "monoms"],
                            ["7", "monoms"],
                            ["a + b", "nav"],
                            ["x : y", "nav"]]),
           paraksts="Monomā ir tikai reizināšana.",
           fakti=["Monoms - skaitļu un mainīgo pakāpju reizinājums.",
                  "Koeficients - skaitliskais reizinātājs: 3a^2b koeficients "
                  "ir 3.",
                  "Summa vai dalīšana ar mainīgo nav monoms."]),

    Doma("Monoms un koeficients",
         "Monomā skaitļi un burti ir tikai sareizināti.",
         soli=[
             "Pārbaudi, vai ir tikai reizināšana un pakāpes ar naturālu "
             "kāpinātāju.",
             "Skaitlis un viens burts arī ir monomi: 7, x.",
             "−ab koeficients ir −1, ab koeficients ir 1.",
             "{x|2} ir monoms ar koeficientu {1|2}, bet {2|x} - nav.",
         ]),

    Varianti("Monoms vai nē?", [
        {"jaut": "Kura izteiksme ir monoms?",
         "opcijas": ["−5x^2y", "x + 5", "{5|x}", "x − y"],
         "pareizi": 0, "padoms": "Tikai reizināšana."},
        {"jaut": "Kura izteiksme NAV monoms?",
         "opcijas": ["a^2 + 1", "{a|3}", "−a", "0,5ab"],
         "pareizi": 0, "padoms": "Summa."},
        {"jaut": "Monoma −x^3y koeficients ir...",
         "opcijas": ["−1", "1", "3", "−3"],
         "pareizi": 0, "padoms": "−x^3y = −1 · x^3y."},
    ]),

    Ievadi("Nosauc koeficientu", [
        {"jaut": "5a^2b", "atb": ["5"], "padoms": "Skaitlis priekšā."},
        {"jaut": "−x^3", "atb": ["−1", "-1"], "padoms": "−1 · x^3."},
        {"jaut": "{3|4}xy", "atb": ["{3|4}", "3/4", "0,75"],
         "padoms": "Daļa arī ir koeficients."},
        {"jaut": "2a · 3b", "atb": ["6"], "padoms": "Sareizini skaitļus."},
        {"jaut": "−a · (−5b)", "atb": ["5"], "padoms": "Mīnuss reiz mīnuss."},
        {"jaut": "{x|4}", "atb": ["{1|4}", "1/4", "0,25"],
         "padoms": "{x|4} = {1|4} · x."},
    ], pamats=4),

    Pasaule("Formulas ir monomi",
            Ievadi("", [
                {"jaut": "Taisnstūra malas 3a un 2a. Laukums 6a^2 - "
                         "koeficients?",
                 "atb": ["6"], "padoms": "3 · 2."},
                {"jaut": "Kubs ar šķautni 2x: tilpums 8x^3. Koeficients?",
                 "atb": ["8"], "padoms": "2 · 2 · 2."},
                {"jaut": "Riņķa laukums πr^2. Koeficients π līdz simtdaļām?",
                 "atb": ["3,14"], "padoms": "π ≈ 3,14."},
            ]),
            pavediens="tehnika",
            konteksts="Daudzas formulas ir monomi: S = πr^2, V = a^3, "
                      "s = 5t^2.",
            kapec="Koeficients parāda, cik reižu lielums pieaug."),

    Kopsavilkums([
        "Nosaku, vai izteiksme ir monoms.",
        "Nosaucu monoma koeficientu, arī −1 un daļu.",
        "Atrodu monomus pazīstamās formulās.",
    ]),

    Majas([
        "Uzraksti 5 monomus un 3 izteiksmes, kas nav monomi.",
        "Atrodi fizikas vai ģeometrijas formulā monomu un nosauc "
        "koeficientu.",
        "Paskaidro, kāpēc {x|2} ir monoms, bet {2|x} - nav.",
    ]),
]
