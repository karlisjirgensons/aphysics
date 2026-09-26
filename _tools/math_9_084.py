# -*- coding: utf-8 -*-
"""9. klase, 84. stunda: «Kā pārveidot vienādojumu?»

Reti vienādojums ir dots formā ax^2 + bx + c = 0. Ekvivalenti pārveidojumi
- atvērt iekavas, pārnest locekļus, reizināt ar saucēju, dalīt ar kopīgu
skaitli - saknes nemaina; tiem jānoved līdz standartformai.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Slidnis, Varianti, restis)

TEMA = "Kā pārveidot vienādojumu?"

MERKIS = ("Veiksim ekvivalentus pārveidojumus, lai iegūtu kvadrātvienādojumu "
          "standartformā.")

_T = "text"

SATURS = [
    Sakums("(x + 1)(x − 2) = 4 - kas ir a, b, c?",
           zimejums=restis([["(x + 1)(x − 2) = 4"], ["x² − x − 2 = 4"],
                            ["x² − x − 6 = 0"]]),
           paraksts="Tikai pēc pārveidojumiem: a = 1, b = −1, c = −6.",
           fakti=["Labajā pusē jābūt 0.",
                  "Iekavas atver, līdzīgos savelk.",
                  "Pārveidojumi saknes nemaina."]),

    Doma("Ekvivalenti pārveidojumi",
         "Vienādojuma saknes nemainās, ja abām pusēm pieskaita vienu skaitli "
         "vai tās reizina (dala) ar skaitli, kas nav 0.",
         soli=[
             "Atver iekavas.",
             "Pārnes visu uz kreiso pusi (zīme mainās).",
             "Savelc līdzīgos locekļus; sakārto x^2, x, skaitlis.",
             "Ja visi koeficienti dalās - izdali (vieglāk rēķināt).",
             "Ja a < 0 - var reizināt ar −1.",
         ]),

    Slidnis("Piemērs soli pa solim", [
        {"v": "Dots", "teksts": "2x(x − 3) = x^2 − 9"},
        {"v": "1", "teksts": "2x^2 − 6x = x^2 − 9"},
        {"v": "2", "teksts": "2x^2 − 6x − x^2 + 9 = 0"},
        {"v": "3", "teksts": "x^2 − 6x + 9 = 0: a = 1, b = −6, c = 9"},
    ]),

    Paraugs("Ar daļām",
            uzd="Pārveido: {x^2|2} − {x|3} = 1.",
            soli=[
                ("· 6: 3x^2 − 2x = 6", "Reizina ar kopsaucēju 6."),
                ("3x^2 − 2x − 6 = 0", "Pārnes 6."),
            ],
            atbilde="a = 3, b = −2, c = −6"),

    Ievadi("Pārveido un nosauc c (a > 0)", [
        {"jaut": "x^2 = 3x + 10 ⇒ x^2 − 3x + ? = 0", "atb": ["−10", "-10"],
         "padoms": "Pārnes 10."},
        {"jaut": "(x − 2)^2 = 5 ⇒ x^2 − 4x + ? = 0", "atb": ["−1", "-1"],
         "padoms": "4 − 5."},
        {"jaut": "x(x + 4) = 2x + 3 ⇒ x^2 + ?x − 3 = 0", "atb": ["2"],
         "padoms": "4x − 2x."},
        {"jaut": "6x^2 − 12x + 18 = 0 : 6 ⇒ x^2 − 2x + ? = 0", "atb": ["3"],
         "padoms": "18 : 6."},
        {"jaut": "−x^2 + 5x − 4 = 0 · (−1) ⇒ x^2 − 5x + ? = 0", "atb": ["4"],
         "padoms": "Zīmes mainās."},
    ], pamats=3),

    Varianti("Vai pārveidojums ir ekvivalents?", [
        {"jaut": "x^2 = 4x ⇒ x = 4 (dalīts ar x)",
         "opcijas": ["Nē - pazūd sakne 0", "Jā", "Jā, ja x > 0",
                     "Nē - rodas lieka sakne"],
         "pareizi": 0, "padoms": "Ar x dalīt nedrīkst."},
        {"jaut": "2x^2 − 8 = 0 ⇒ x^2 − 4 = 0",
         "opcijas": ["Jā - dalīts ar 2", "Nē", "Jā, bet saknes mainās",
                     "Nē, jādala ar 8"],
         "pareizi": 0, "padoms": "Skaitlis ≠ 0."},
    ]),

    Pasaule("Taisnstūra dārzs",
            Ievadi("", [
                {"jaut": "Dārzs x m plats un par 5 m garāks; laukums 84 m². "
                         "x(x + 5) = 84 ⇒ x^2 + 5x − ? = 0",
                 "atb": ["84"], "padoms": "Pārnes 84."},
                {"jaut": "Pārbaudi x = 7: 7 · 12 = ?", "atb": ["84"],
                 "padoms": "Der!"},
            ]),
            pavediens="maja",
            konteksts="Situācijas uzdevums gandrīz vienmēr dod vienādojumu, "
                      "ko vēl jāpārveido.",
            kapec="Standartforma ir sākums jebkurai metodei."),

    Kopsavilkums([
        "Pārveidoju vienādojumu standartformā.",
        "Lietoju tikai ekvivalentus pārveidojumus.",
        "Nosaucu a, b, c pēc pārveidošanas.",
    ]),

    Majas([
        "Pārveido: (2x − 1)^2 = x + 5; {x^2|3} + x = 2.",
        "Kāpēc nedrīkst dalīt ar izteiksmi, kurā ir x?",
        "Izdomā situāciju, kas dod vienādojumu x(x + 3) = 40.",
    ]),
]
