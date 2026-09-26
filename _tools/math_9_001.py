# -*- coding: utf-8 -*-
"""9. klase, 1. stunda: «Kad nogriežņi ir proporcionāli?»

Gada pirmā stunda sākas ar papīra lapu: A4 pārlocīta uz pusēm ir A5, un
forma nemainās, jo malas ir proporcionālas. No tā izaug viss 9.1. temats -
proporcionāli nogriežņi, viduslīnija un līdzīgi trijstūri.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, geometrija)

TEMA = "Kad nogriežņi ir proporcionāli?"

MERKIS = ("Noteiksim, vai nogriežņi ir proporcionāli, un pierakstīsim to "
          "attiecību.")

SATURS = [
    Sakums("Kāpēc A5 lapa izskatās kā mazā A4?",
           zimejums=geometrija([("A", 0, 0), ("B", 21, 0), ("C", 21, 29.7),
                                ("D", 0, 29.7), ("_E", 0, 14.85),
                                ("_F", 21, 14.85)],
                               nogriezni=["AB", "BC", "CD", "DA", ("_E", "_F")],
                               iekrasot=[("A B _F _E".split(), 1)],
                               malas=[("AB", "21 cm")],
                               uzraksti=[(27, 22.3, "29,7 cm"),
                                         (10.5, 7.4, "A5"),
                                         (10.5, 22.3, "A5")]),
           paraksts="Pārlocītai lapai garums un platums mainās vienādi.",
           fakti=["A4: 29,7 : 21 ≈ 1,41. A5: 21 : 14,85 ≈ 1,41.",
                  "Vienāda attiecība - vienāda forma.",
                  "Tāpēc kopētājs var A4 samazināt uz A5 bez kropļojuma."]),

    Doma("Proporcionāli nogriežņi",
         "Nogriežņi AB un CD ir proporcionāli nogriežņiem A_1B_1 un C_1D_1, "
         "ja {AB|A_1B_1} = {CD|C_1D_1}.",
         soli=[
             "Izmēri visus nogriežņus vienās mērvienībās.",
             "Aprēķini abas attiecības.",
             "Ja attiecības ir vienādas - nogriežņi ir proporcionāli.",
             "Nezināmo proporcijā atrod ar krustenisko reizināšanu.",
         ],
         pieze="Attiecība ir skaitlis bez mērvienības: 6 cm : 4 cm = 1,5."),

    Paraugs("Vai tie ir proporcionāli?",
            uzd="AB = 6 cm, CD = 9 cm, A_1B_1 = 4 cm, C_1D_1 = 6 cm. Vai AB "
                "un CD ir proporcionāli A_1B_1 un C_1D_1?",
            soli=[
                ("{AB|A_1B_1} = {6|4} = 1,5", "Pirmā attiecība."),
                ("{CD|C_1D_1} = {9|6} = 1,5", "Otrā attiecība."),
                ("1,5 = 1,5", "Attiecības vienādas."),
            ],
            atbilde="jā, nogriežņi ir proporcionāli"),

    Ievadi("Atrodi nezināmo nogriezni", [
        {"jaut": "{4|6} = {x|9}. x = ?", "atb": ["6"],
         "padoms": "x = 4 · 9 : 6."},
        {"jaut": "{5|x} = {15|12}. x = ?", "atb": ["4"],
         "padoms": "x = 5 · 12 : 15."},
        {"jaut": "{AB|CD} = {2|3}, CD = 12 cm. AB = ? cm", "atb": ["8"],
         "padoms": "AB = 12 · 2 : 3."},
        {"jaut": "{x|7} = {10|14}. x = ?", "atb": ["5"],
         "padoms": "Abas puses vienādojot: 14x = 70."},
        {"jaut": "{2,5|x} = {5|8}. x = ?", "atb": ["4"],
         "padoms": "x = 2,5 · 8 : 5."},
        {"jaut": "{9|12} = {x|20}. x = ?", "atb": ["15"],
         "padoms": "{9|12} = 0,75; 0,75 · 20."},
    ], pamats=4),

    Varianti("Proporcionāli vai nē?", [
        {"jaut": "3 cm un 5 cm pret 6 cm un 10 cm",
         "opcijas": ["Jā, attiecība 2", "Nē", "Tikai viens pāris",
                     "Nevar noteikt"],
         "pareizi": 0, "padoms": "6 : 3 un 10 : 5."},
        {"jaut": "4 cm un 6 cm pret 6 cm un 8 cm",
         "opcijas": ["Nē", "Jā, attiecība 1,5", "Jā, attiecība 2",
                     "Jā, jo abiem pieskaitīja 2"],
         "pareizi": 0, "padoms": "6 : 4 = 1,5, bet 8 : 6 ≈ 1,33."},
        {"jaut": "2 dm un 30 cm pret 4 cm un 6 cm",
         "opcijas": ["Jā, attiecība 5", "Nē, mērvienības atšķiras",
                     "Nē", "Jā, attiecība 2"],
         "pareizi": 0, "padoms": "2 dm = 20 cm; 20 : 4 un 30 : 6."},
        {"jaut": "Kura proporcija ir pareizi pierakstīta?",
         "opcijas": ["{AB|A_1B_1} = {CD|C_1D_1}", "{AB|C_1D_1} = {CD|A_1B_1}",
                     "AB · CD = A_1B_1 · C_1D_1", "AB + CD = A_1B_1 + C_1D_1"],
         "pareizi": 0, "padoms": "Atbilstošais pret atbilstošo."},
    ]),

    Pasaule("Foto palielināšana",
            Ievadi("", [
                {"jaut": "Foto ir 10 cm × 15 cm. To palielina tā, ka platums "
                         "ir 20 cm. Kāds būs augstums (cm)?",
                 "atb": ["30"], "padoms": "Attiecība 2 : 1 abām malām."},
                {"jaut": "Plakāts no tā paša foto ir 60 cm plats. Augstums "
                         "(cm)?",
                 "atb": ["90"], "padoms": "60 : 10 = 6 reizes."},
                {"jaut": "Telefona ekrāns rāda 6 cm platu attēlu. Augstums "
                         "(cm)?",
                 "atb": ["9"], "padoms": "{6|10} = {x|15}."},
            ]),
            pavediens="dati",
            konteksts="Attēlu mainot, abas malas jāmaina vienādā attiecībā - "
                      "citādi seja kļūst plata vai izstiepta.",
            kapec="Proporcionālas malas saglabā attēla formu."),

    Kopsavilkums([
        "Pierakstu nogriežņu attiecību.",
        "Pārbaudu, vai divi nogriežņu pāri ir proporcionāli.",
        "Atrodu nezināmo nogriezni no proporcijas.",
    ]),

    Majas([
        "Izmēri A4 lapu un grāmatas vāku. Vai to malas ir proporcionālas?",
        "Atrodi x: {x|8} = {15|24}; {12|x} = {4|7}.",
        "Uzraksti trīs nogriežņu pārus, kas ir proporcionāli ar attiecību 3.",
    ]),
]
