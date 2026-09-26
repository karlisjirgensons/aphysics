# -*- coding: utf-8 -*-
"""9. klase, 130. stunda: «Kas ir aritmētiskā progresija?»

Aritmētiskā progresija: katrs nākamais loceklis ir par vienu un to pašu
skaitli d (diferenci) lielāks. 2025. gada eksāmena 5. uzdevums sākās tieši
tā: a_1 = 3, katrs nākamais par 2 lielāks.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, taisne)

TEMA = "Kas ir aritmētiskā progresija?"

MERKIS = ("Definēsim aritmētisko progresiju un noteiksim tās diferenci.")

SATURS = [
    Sakums("Vienādi soļi pa skaitļu taisni",
           zimejums=taisne(0, 14, 1, atzimes=[(3, "a₁"), (5, "a₂"),
                                               (7, "a₃"), (9, "a₄"),
                                               (11, "a₅")],
                           bultas=[(3, 5, "+2"), (5, 7, "+2"), (7, 9, "+2"),
                                   (9, 11, "+2")]),
           paraksts="Eksāmens 2025: a₁ = 3, katrs nākamais par 2 lielāks.",
           fakti=["Diference d = a_{n+1} − a_n = 2.",
                  "Katrs solis vienāds - tā ir aritmētiskā progresija.",
                  "Eksāmena atbilde: d = 2, a_4 = 9."]),

    Doma("Aritmētiskā progresija",
         "Virkne, kurā a_{n+1} = a_n + d visiem n; d - progresijas diference.",
         soli=[
             "d = a_2 − a_1 = a_3 − a_2 = ...",
             "d > 0 - progresija augoša, d < 0 - dilstoša, d = 0 - konstanta.",
             "Pārbaude: vai VISAS blakus starpības vienādas?",
         ]),

    Slidnis("Progresija vai nē?", [
        {"v": "✔", "teksts": "5, 8, 11, 14: starpības 3, 3, 3 - jā, d = 3"},
        {"v": "✔", "teksts": "20, 15, 10, 5: starpības −5 - jā, d = −5"},
        {"v": "✘", "teksts": "1, 2, 4, 8: starpības 1, 2, 4 - nē"},
        {"v": "✔", "teksts": "7, 7, 7, 7: d = 0 - jā (konstanta)"},
    ]),

    Ievadi("Atrodi d vai locekli", [
        {"jaut": "a_1 = 3, d = 2 (eksāmens). a_4 = ?", "atb": ["9"],
         "padoms": "3, 5, 7, 9."},
        {"jaut": "12, 19, 26, ... d = ?", "atb": ["7"], "padoms": "19 − 12."},
        {"jaut": "40, 34, 28, ... d = ?", "atb": ["−6", "-6"],
         "padoms": "34 − 40."},
        {"jaut": "−5, −2, 1, ... a_5 = ?", "atb": ["7"], "padoms": "d = 3."},
        {"jaut": "a_3 = 10, d = 4. a_1 = ?", "atb": ["2"],
         "padoms": "Atpakaļ: 6, 2."},
    ], pamats=3),

    Varianti("Aritmētiskā progresija?", [
        {"jaut": "2, 6, 10, 14, ...",
         "opcijas": ["Jā, d = 4", "Nē", "Jā, d = 2", "Jā, d = 3"],
         "pareizi": 0, "padoms": "Starpība 4."},
        {"jaut": "1, 4, 9, 16, ...",
         "opcijas": ["Nē", "Jā, d = 3", "Jā, d = 5", "Jā, d = n"],
         "pareizi": 0, "padoms": "Starpības 3, 5, 7."},
        {"jaut": "0,5; 1; 1,5; 2; ...",
         "opcijas": ["Jā, d = 0,5", "Nē", "Jā, d = 2", "Jā, d = 1"],
         "pareizi": 0, "padoms": "+0,5."},
    ]),

    Pasaule("Taksometra skaitītājs",
            Ievadi("", [
                {"jaut": "Iekāpšana 3 €, katrs km +0,80 €. Pēc 1 km: 3,80 €; "
                         "d = ?", "atb": ["0,8"], "padoms": "Maksa par km."},
                {"jaut": "Cik € pēc 5 km?", "atb": ["7"],
                 "padoms": "3 + 5 · 0,8."},
            ]),
            pavediens="celojums",
            konteksts="Skaitītāja rādījumi pēc katra kilometra veido "
                      "aritmētisko progresiju.",
            kapec="Diference ir cena par vienu soli."),

    Kopsavilkums([
        "Definēju aritmētisko progresiju.",
        "Nosaku diferenci d.",
        "Pārbaudu, vai virkne ir progresija.",
    ]),

    Majas([
        "Atrodi d: 17, 13, 9, ...; 2,5; 4; 5,5; ...",
        "Uzraksti progresiju ar a_1 = −4 un d = 3 (5 locekļi).",
        "Atrodi dzīvē vienmērīgi augošu lielumu.",
    ]),
]
