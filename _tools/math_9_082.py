# -*- coding: utf-8 -*-
"""9. klase, 82. stunda: «Ko rāda grafiks?»

Vienādojuma ax^2 + bx + c = 0 saknes ir parabolas y = ax^2 + bx + c
krustpunkti ar x asi. Divi, viens vai neviens krustpunkts - tikpat sakņu.
Slīdnis bīda parabolu augšup, un krustpunkti «saplūst» un pazūd.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, parabola)

TEMA = "Ko rāda grafiks?"

MERKIS = ("Noteiksim sakņu skaitu no atbilstošās funkcijas grafika.")

SATURS = [
    Sakums("Saknes - tur, kur parabola šķērso x asi",
           zimejums=parabola(1, -2, -3, -3, 5, -5, 6,
                             punkti=[(-1, 0, "−1"), (3, 0, "3")]),
           paraksts="x² − 2x − 3 = 0: saknes −1 un 3.",
           fakti=["Uz x ass y = 0 - tieši to prasa vienādojums.",
                  "Krustpunktu skaits = sakņu skaits.",
                  "Grafiks parāda arī aptuvenas saknes."]),

    Slidnis("Bīdi parabolu augšup", [
        {"v": "c = −3", "teksts": "Divi krustpunkti - 2 saknes",
         "zim": parabola(1, -2, -3, -3, 5, -5, 6)},
        {"v": "c = 1", "teksts": "Pieskaras x asij - 1 sakne (x = 1)",
         "zim": parabola(1, -2, 1, -3, 5, -5, 6)},
        {"v": "c = 3", "teksts": "Nav kopīgu punktu - 0 sakņu",
         "zim": parabola(1, -2, 3, -3, 5, -5, 6)},
    ]),

    Doma("Grafiskā interpretācija",
         "Vienādojuma ax^2 + bx + c = 0 saknes ir funkcijas "
         "y = ax^2 + bx + c grafika krustpunktu ar x asi abscises.",
         soli=[
             "Uzzīmē vai aplūko parabolu.",
             "Saskaiti krustpunktus ar x asi: 2, 1 vai 0.",
             "Nolasi abscises - tās ir saknes (vai tuvinājumi).",
             "Pārbaudi, ievietojot vienādojumā.",
         ]),

    Varianti("Cik sakņu?", [
        {"jaut": "Parabola ar virsotni (2; −4), zari uz augšu.",
         "opcijas": ["2", "1", "0", "Nevar zināt"],
         "pareizi": 0, "padoms": "Virsotne zem ass, zari augšup."},
        {"jaut": "Parabola ar virsotni (−1; 3), zari uz augšu.",
         "opcijas": ["0", "1", "2", "Nevar zināt"],
         "pareizi": 0, "padoms": "Visa virs ass."},
        {"jaut": "Parabola ar virsotni (5; 0).",
         "opcijas": ["1", "0", "2", "Nevar zināt"],
         "pareizi": 0, "padoms": "Virsotne uz ass."},
        {"jaut": "Parabola ar virsotni (0; 4), zari uz leju.",
         "opcijas": ["2", "0", "1", "Nevar zināt"],
         "pareizi": 0, "padoms": "Virs ass, bet iet lejup."},
    ]),

    Ievadi("Nolasi saknes no grafika (sākuma zīmējums)", [
        {"jaut": "Mazākā sakne?", "atb": ["−1", "-1"],
         "padoms": "Kreisais krustpunkts."},
        {"jaut": "Lielākā sakne?", "atb": ["3"],
         "padoms": "Labais krustpunkts."},
        {"jaut": "Pārbaude: 3^2 − 2 · 3 − 3 = ?", "atb": ["0"],
         "padoms": "9 − 6 − 3."},
    ]),

    Pasaule("Basketbola metiens",
            Ievadi("", [
                {"jaut": "Bumbas augstums pēc t sekundēm: grafiks krusto "
                         "laika asi punktos 0 un 1,6. Cik s bumba lido?",
                 "atb": ["1,6"], "padoms": "No 0 līdz 1,6."},
                {"jaut": "Virsotne ir vidū starp krustpunktiem. Pēc cik s "
                         "bumba ir visaugstāk?", "atb": ["0,8"],
                 "padoms": "1,6 : 2."},
            ]),
            pavediens="sports",
            konteksts="Sporta analītiķi video izseko bumbu un iegūst tās "
                      "trajektoriju - parabolu.",
            kapec="Krustpunkti ar asi ir brīži, kad bumba ir zemē.",
            zimejums=parabola(-5, 8, 0, -1, 2, -1, 4, uzraksts="h(t)",
                              asis=("t", "h"),
                              punkti=[(0, 0, "0"), (1.6, 0, "1,6")])),

    Kopsavilkums([
        "Saistu saknes ar parabolas krustpunktiem ar x asi.",
        "Nosaku sakņu skaitu no grafika.",
        "Nolasu saknes no grafika un pārbaudu.",
    ]),

    Majas([
        "Uzzīmē y = x^2 − 4 un nolasi saknes.",
        "Uzzīmē y = x^2 + 1. Cik sakņu ir x^2 + 1 = 0?",
        "Atrodi parabolu, kurai saknes ir 0 un 6.",
    ]),
]
