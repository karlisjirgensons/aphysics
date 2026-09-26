# -*- coding: utf-8 -*-
"""9. klase, 48. stunda: «Kā izveidot atgādni?»

Īpašo leņķu tabula nav jāiekaļ: to var atjaunot no diviem trijstūriem
(1, 1, √2 un 1, √3, 2) vai no «sakņu kāpnēm» √1/2, √2/2, √3/2. Stundā
skolēns uzbūvē tabulu pats un pārbauda to ar kalkulatoru.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, restis, taisnlenka)

TEMA = "Kā izveidot atgādni?"

MERKIS = "Veidosim pārskatu par īpašo leņķu vērtībām un pārbaudīsim to."

_TABULA = restis([["", "30°", "45°", "60°"],
                  ["sin", "1/2", "√2/2", "√3/2"],
                  ["cos", "√3/2", "√2/2", "1/2"],
                  ["tg", "√3/3", "1", "√3"]])

SATURS = [
    Sakums("Viena tabula - deviņas vērtības",
           zimejums=_TABULA,
           paraksts="Eksāmena formulu lapā šīs tabulas nav.",
           fakti=["sin rindā saknes aug: √1, √2, √3 - viss dalīts ar 2.",
                  "cos rinda ir sin rinda pretējā secībā.",
                  "tg = sin : cos."]),

    Slidnis("Atjauno tabulu no trijstūriem", [
        {"v": "45°", "teksts": "Katetes 1 un 1, hipotenūza √2",
         "zim": taisnlenka(1, 1, ("1", "1", "√2"), "45°")},
        {"v": "30°", "teksts": "Katetes 1 un √3, hipotenūza 2",
         "zim": taisnlenka(1.732, 1, ("1", "√3", "2"), "30°")},
        {"v": "60°", "teksts": "Tas pats trijstūris, otrs leņķis",
         "zim": taisnlenka(1, 1.732, ("√3", "1", "2"), "60°")},
    ], ievads="Divi trijstūri - visa tabula."),

    Doma("Sakņu kāpnes",
         "sin 30°, sin 45°, sin 60° = {√1|2}, {√2|2}, {√3|2}.",
         soli=[
             "Uzraksti sin rindu: zem saknes 1, 2, 3; saucējs 2.",
             "cos rindu uzraksti pretējā secībā.",
             "tg = sin : cos (tg 30° = {1|√3} = {√3|3}).",
             "Pārbaudi ar kalkulatoru (tuvinātas vērtības).",
         ]),

    Varianti("Sameklē tabulā", [
        {"jaut": "cos 60° = ?",
         "opcijas": ["{1|2}", "{√3|2}", "{√2|2}", "1"],
         "pareizi": 0, "padoms": "cos rinda."},
        {"jaut": "Kurā leņķī sin α = cos α?",
         "opcijas": ["45°", "30°", "60°", "Nevienā"],
         "pareizi": 0, "padoms": "Vidējā kolonna."},
        {"jaut": "{√3|2} ≈ ?",
         "opcijas": ["0,866", "0,707", "0,5", "1,732"],
         "pareizi": 0, "padoms": "1,732 : 2."},
        {"jaut": "tg 30° · tg 60° = ?",
         "opcijas": ["1", "√3", "3", "{1|3}"],
         "pareizi": 0, "padoms": "{√3|3} · √3 = {3|3}."},
    ]),

    Ievadi("Pārbaudi ar kalkulatoru (līdz tūkstošdaļām)", [
        {"jaut": "{√2|2} ≈ ?", "atb": ["0,707"], "padoms": "1,4142 : 2."},
        {"jaut": "{√3|3} ≈ ?", "atb": ["0,577"], "padoms": "1,7321 : 3."},
        {"jaut": "sin 60° − cos 30° = ?", "atb": ["0"],
         "padoms": "Vienādas vērtības."},
        {"jaut": "sin^2 30° + cos^2 30° = ?", "atb": ["1"],
         "padoms": "{1|4} + {3|4}."},
    ]),

    Pasaule("Spēle «Trīs leņķi»",
            Varianti("", [
                {"jaut": "Kartīte: «pretkatete ir puse no hipotenūzas». Kāds "
                         "leņķis?",
                 "opcijas": ["30°", "45°", "60°", "90°"],
                 "pareizi": 0, "padoms": "sin α = {1|2}."},
                {"jaut": "Kartīte: «katetes vienādas». Leņķis?",
                 "opcijas": ["45°", "30°", "60°", "0°"],
                 "pareizi": 0, "padoms": "tg α = 1."},
                {"jaut": "Kartīte: «piekatete ir puse no hipotenūzas».",
                 "opcijas": ["60°", "30°", "45°", "90°"],
                 "pareizi": 0, "padoms": "cos α = {1|2}."},
            ]),
            pavediens="speles",
            konteksts="Spēlē ar draugu: viens velk kartīti ar aprakstu, otrs "
                      "ātri nosauc leņķi.",
            kapec="Atkārtojot spēlē, tabula paliek atmiņā."),

    Kopsavilkums([
        "Atjaunoju īpašo leņķu tabulu no diviem trijstūriem.",
        "Lietoju «sakņu kāpnes».",
        "Pārbaudu vērtības ar kalkulatoru.",
    ]),

    Majas([
        "Uzraksti tabulu no atmiņas uz kartītes.",
        "Izveido 6 spēles kartītes un izspēlē ar kādu mājās.",
        "Aprēķini: 2sin 30° + √2 · cos 45° + tg 45°.",
    ]),
]
