# -*- coding: utf-8 -*-
"""9. klase, 83. stunda: «Kas ir kvadrāttrinoms?»

Kvadrāttrinoms ax^2 + bx + c. Pilnā kvadrāta atdalīšana: x^2 + 6x + 5 =
(x + 3)^2 − 4. No šī pieraksta redz virsotni (−3; −4) un saknes - un no tā
pēc divām stundām izaugs sakņu formula.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Slidnis, Varianti, binoma_kvadrats, parabola)

TEMA = "Kas ir kvadrāttrinoms?"

MERKIS = ("Pierakstīsim kvadrāttrinomu kā binoma kvadrāta un skaitļa summu.")

_T = "text"

SATURS = [
    Sakums("x² + 6x + 5 = (x + 3)² − ?",
           zimejums=binoma_kvadrats(4, 1.8, ("x", "3")),
           paraksts="Kvadrātam (x + 3)² vajag + 9; mums ir tikai + 5.",
           fakti=["x^2 + 6x + 9 = (x + 3)^2.",
                  "x^2 + 6x + 5 = (x + 3)^2 − 4.",
                  "To sauc par pilnā kvadrāta atdalīšanu."]),

    Doma("Pilnā kvadrāta atdalīšana",
         "x^2 + bx + c = (x + {b|2})^2 − ({b|2})^2 + c.",
         soli=[
             "Paņem pusi no b - tas iet iekavās.",
             "Pieskaiti un atņem ({b|2})^2.",
             "Pirmie trīs locekļi = binoma kvadrāts.",
             "Pārējos savelc vienā skaitlī.",
         ]),

    Slidnis("x² − 8x + 12 pa soļiem", [
        {"v": "1", "teksts": "Puse no −8 ir −4"},
        {"v": "2", "teksts": "x^2 − 8x + 16 − 16 + 12"},
        {"v": "3", "teksts": "(x − 4)^2 − 4"},
        {"v": "4", "teksts": "Virsotne (4; −4); saknes: (x − 4)^2 = 4 ⇒ "
                             "x = 2 vai x = 6",
         "zim": parabola(1, -8, 12, -1, 8, -5, 6,
                         punkti=[(4, -4, "(4; −4)")])},
    ]),

    Paraugs("Atrisini ar pilno kvadrātu",
            uzd="Atrisini x^2 + 6x + 5 = 0.",
            soli=[
                ("(x + 3)^2 − 4 = 0", "Atdala kvadrātu."),
                ("(x + 3)^2 = 4 ⇒ x + 3 = ±2", "Izvelk sakni."),
                ("x = −1 vai x = −5", "Saknes."),
            ],
            atbilde="−5; −1"),

    Ievadi("Atdali pilno kvadrātu", [
        {"jaut": "x^2 + 4x + 7 = (x + 2)^2 + ?", "atb": ["3"],
         "padoms": "7 − 4."},
        {"jaut": "x^2 − 10x + 20 = (x − 5)^2 + ?", "atb": ["−5", "-5"],
         "padoms": "20 − 25."},
        {"jaut": "x^2 + 2x = (x + 1)^2 + ?", "atb": ["−1", "-1"],
         "padoms": "0 − 1."},
        {"jaut": "x^2 − 6x + 1 = (x − ?)^2 − 8", "atb": ["3"],
         "padoms": "Puse no 6."},
        {"jaut": "x^2 + 5x + 4 = (x + 2,5)^2 + ? (decimāldaļa)",
         "atb": ["−2,25", "-2,25"], "padoms": "4 − 6,25."},
    ], pamats=3),

    Varianti("Ko rāda pieraksts (x − m)^2 + n?", [
        {"jaut": "(x − 2)^2 + 3. Mazākā vērtība?",
         "opcijas": ["3, ja x = 2", "2, ja x = 3", "−3", "0"],
         "pareizi": 0, "padoms": "Kvadrāts ≥ 0."},
        {"jaut": "(x + 1)^2 + 5 = 0. Cik sakņu?",
         "opcijas": ["0", "1", "2", "Nevar zināt"],
         "pareizi": 0, "padoms": "Kreisā puse ≥ 5."},
        {"jaut": "Parabolas y = (x − 3)^2 − 7 virsotne?",
         "opcijas": ["(3; −7)", "(−3; −7)", "(3; 7)", "(−7; 3)"],
         "pareizi": 0, "padoms": "Iekavās −3 → x = 3."},
    ]),

    Pasaule("Mazākās izmaksas",
            Ievadi("", [
                {"jaut": "Ražošanas izmaksas: C = x^2 − 20x + 150 (x - simti "
                         "preču). C = (x − 10)^2 + ? ", "atb": ["50"],
                 "padoms": "150 − 100."},
                {"jaut": "Pie kāda x izmaksas mazākās?", "atb": ["10"],
                 "padoms": "Kad kvadrāts = 0."},
                {"jaut": "Mazākās izmaksas?", "atb": ["50"],
                 "padoms": "0 + 50."},
            ]),
            pavediens="veikals",
            konteksts="Uzņēmums meklē ražošanas apjomu, kurā vienas partijas "
                      "izmaksas ir mazākās.",
            kapec="Pilnais kvadrāts uzreiz parāda minimumu."),

    Kopsavilkums([
        "Atdalu pilno kvadrātu kvadrāttrinomā.",
        "Nolasu virsotni un mazāko vērtību.",
        "Atrisinu vienādojumu ar pilnā kvadrāta metodi.",
    ]),

    Majas([
        "Atdali pilno kvadrātu: x^2 + 12x + 30; x^2 − 3x + 2.",
        "Atrisini x^2 − 4x − 5 = 0 ar pilno kvadrātu.",
        "Pārbaudi atbildi, sadalot reizinātājos.",
    ]),
]
