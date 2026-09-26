# -*- coding: utf-8 -*-
"""8. klase, 26. stunda: «Vai īpašības der arī negatīviem kāpinātājiem?»

Jā - un tieši tāpēc a^−n definēja tā, kā definēja. Stunda pārbauda katru
īpašību ar negatīviem kāpinātājiem un rāda, ka saskaitīt un atņemt veselus
skaitļus kāpinātājos ir tas pats, kas 6. klasē ar negatīviem skaitļiem.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, restis)

TEMA = "Vai īpašības der arī negatīviem kāpinātājiem?"

MERKIS = ("Lietosim pakāpju īpašības izteiksmēs ar veselu kāpinātāju.")

SATURS = [
    Sakums("Pārbaudi ar skaitļiem",
           zimejums=restis([["2⁻³ · 2⁵", "=", "1/8 · 32", "=", "4"],
                            ["2⁻³⁺⁵", "=", "2²", "=", "4"]]),
           paraksts="Abos ceļos - viens rezultāts.",
           fakti=["Reizināšanas īpašība der ar negatīviem kāpinātājiem.",
                  "Kāpinātājus saskaita kā veselus skaitļus.",
                  "Tāpat der dalīšana un kāpināšana."]),

    Doma("Visas īpašības - veseliem kāpinātājiem",
         "Ja a ≠ 0 un m, n ir veseli skaitļi, tad der tās pašas īpašības: "
         "a^m · a^n = a^{m + n}; a^m : a^n = a^{m − n}; (a^m)^n = a^{mn}.",
         soli=[
             "Kāpinātājus saskaiti vai atņem pēc zīmju likuma.",
             "a^m : a^n - atņemot negatīvu, pieskaita: 5 − (−2) = 7.",
             "(a^m)^n - reizinot divus negatīvus, iegūst pozitīvu.",
             "Beigās pieraksti bez negatīviem kāpinātājiem.",
         ]),

    Paraugs("Vienkāršo",
            uzd="Vienkāršo x^−4 · x^7, {a^3|a^−2} un (y^−2)^−3.",
            soli=[
                ("x^{−4 + 7} = x^3", "Saskaita."),
                ("a^{3 − (−2)} = a^5", "Atņem negatīvu."),
                ("y^{(−2) · (−3)} = y^6", "Mīnuss reiz mīnuss."),
            ],
            atbilde="x^3; a^5; y^6"),

    Ievadi("Vienkāršo", [
        {"jaut": "a^−3 · a^8", "atb": ["a^5"], "padoms": "−3 + 8.",
         "tastatura": "text"},
        {"jaut": "b^4 · b^−4", "atb": ["1"], "padoms": "b^0."},
        {"jaut": "{x^2|x^−3}", "atb": ["x^5"], "padoms": "2 − (−3).",
         "tastatura": "text"},
        {"jaut": "(m^−1)^−4", "atb": ["m^4"], "padoms": "(−1) · (−4).",
         "tastatura": "text"},
        {"jaut": "10^−2 · 10^5 - aprēķini", "atb": ["1000"],
         "padoms": "10^3."},
        {"jaut": "{2^−3|2^−5} - aprēķini", "atb": ["4"],
         "padoms": "2^{−3 + 5}."},
    ], pamats=4),

    Varianti("Atrodi kļūdu", [
        {"jaut": "x^−2 · x^−3 = x^6",
         "opcijas": ["Kļūda: x^−5", "Pareizi", "Kļūda: x^1",
                     "Kļūda: x^−6"],
         "pareizi": 0, "padoms": "Saskaita, nereizina."},
        {"jaut": "a^4 : a^−1 = a^3",
         "opcijas": ["Kļūda: a^5", "Pareizi", "Kļūda: a^−4",
                     "Kļūda: a^−3"],
         "pareizi": 0, "padoms": "4 − (−1)."},
        {"jaut": "(z^−3)^2 = z^−1",
         "opcijas": ["Kļūda: z^−6", "Pareizi", "Kļūda: z^6",
                     "Kļūda: z^−5"],
         "pareizi": 0, "padoms": "Reizina."},
    ]),

    Pasaule("Mērvienību pārveidošana",
            Ievadi("", [
                {"jaut": "1 mm = 10^−3 m, 1 km = 10^3 m. Cik mm ir 1 km? "
                         "Atbildi kā 10^?",
                 "atb": ["10^6", "1000000"], "padoms": "10^3 : 10^−3.",
                 "tastatura": "text"},
                {"jaut": "1 mg = 10^−3 g, 1 kg = 10^3 g. Cik mg ir 2 kg?",
                 "atb": ["2000000", "2 000 000"],
                 "padoms": "2 · 10^6."},
                {"jaut": "Tablete satur 5 · 10^−4 kg vielas. Cik mg?",
                 "atb": ["500"], "padoms": "10^−4 kg = 10^2 mg."},
            ]),
            pavediens="tehnika",
            konteksts="Priedēkļi kilo-, mili-, mikro- ir 10 pakāpes, tāpēc "
                      "mērvienības pārveido, saskaitot un atņemot kāpinātājus.",
            kapec="Farmaceitam kļūda par vienu pakāpi nozīmē 10 reizes par "
                  "daudz zāļu."),

    Kopsavilkums([
        "Lietoju pakāpju īpašības ar veseliem kāpinātājiem.",
        "Saskaitu un atņemu negatīvus kāpinātājus pēc zīmju likuma.",
        "Pārveidoju mērvienības ar 10 pakāpēm.",
    ]),

    Majas([
        "Vienkāršo: x^−5 · x^2, {y^−1|y^4}, (a^−2)^3 · a^7.",
        "Pārbaudi vienu no tiem ar x = 2.",
        "Pārveido 3 km uz cm, lietojot 10 pakāpes.",
    ]),
]
