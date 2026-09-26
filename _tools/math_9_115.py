# -*- coding: utf-8 -*-
"""9. klase, 115. stunda: «Kurš paņēmiens ir ērtāks?»

Metodes izvēle pēc koeficientiem: ja kāds nezināmais jau ir izteikts vai
tā koeficients ir 1 - ievietošana; ja koeficienti vienādi vai pretēji -
saskaitīšana; aptuvenai atbildei vai ilustrācijai - grafiski.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, paris, restis)

TEMA = "Kurš paņēmiens ir ērtāks?"

MERKIS = ("Izvēlēsimies piemērotāko paņēmienu konkrētai sistēmai un "
          "pamatosim izvēli.")

_T = "text"

SATURS = [
    Sakums("Trīs sistēmas - trīs izvēles",
           zimejums=restis([["sistēma", "ērtāk"],
                            ["y = 3x; 2x + y = 10", "ievietošana"],
                            ["4x + 3y = 18; 2x − 3y = 0", "saskaitīšana"],
                            ["y = 0,5x + 1; y = −x + 4", "grafiski / abas"]]),
           paraksts="Metodi izvēlas pēc koeficientiem.",
           fakti=["Izteikts nezināmais - ievietošana.",
                  "Pretēji koeficienti - saskaitīšana.",
                  "Abas metodes dod vienu atbildi."]),

    Doma("Izvēles noteikumi",
         "Paskaties uz koeficientiem, pirms sāc: laba izvēle ietaupa pusi "
         "rēķinu.",
         soli=[
             "Koeficients 1 vai −1 → izsaki to nezināmo (ievietošana).",
             "Vienādi vai pretēji koeficienti → saskaiti vai atņem.",
             "Lieli vai daļskaitļu koeficienti → vispirms vienkāršo.",
             "Grafiski - ilustrācijai un pārbaudei.",
         ]),

    Slidnis("Viena sistēma - divi ceļi", [
        {"v": "Sistēma", "teksts": "x + y = 6 un 3x − y = 2"},
        {"v": "Ievietošana", "teksts": "y = 6 − x; 3x − 6 + x = 2 ⇒ x = 2, "
                                       "y = 4"},
        {"v": "Saskaitīšana", "teksts": "Saskaita: 4x = 8 ⇒ x = 2, y = 4"},
        {"v": "Secinājums", "teksts": "Te saskaitīšana ir īsāka - pretēji ±y"},
    ]),

    Varianti("Kuru paņēmienu izvēlēties?", [
        {"jaut": "x = 5 − 2y un 3x + 4y = 17",
         "opcijas": ["Ievietošanu", "Saskaitīšanu", "Grafiski",
                     "Nevar atrisināt"],
         "pareizi": 0, "padoms": "x jau izteikts."},
        {"jaut": "7x + 2y = 20 un 3x − 2y = 0",
         "opcijas": ["Saskaitīšanu", "Ievietošanu", "Grafiski",
                     "Nevar atrisināt"],
         "pareizi": 0, "padoms": "±2y."},
        {"jaut": "5x + 3y = 21 un 5x − y = 1",
         "opcijas": ["Atņemšanu (5x)", "Grafiski", "Nevar", "Tikai pārlasi"],
         "pareizi": 0, "padoms": "Vienādi 5x."},
    ]),

    Ievadi("Atrisini ar izvēlēto paņēmienu", [
        {"jaut": "x = 5 − 2y un 3x + 4y = 17", "atb": paris(7, "−1"),
         "tastatura": _T, "vieta": "(x; y)", "padoms": "15 − 6y + 4y = 17."},
        {"jaut": "7x + 2y = 20 un 3x − 2y = 0", "atb": paris(2, 3),
         "tastatura": _T, "vieta": "(x; y)", "padoms": "10x = 20."},
        {"jaut": "5x + 3y = 21 un 5x − y = 1", "atb": paris("1,2", 5),
         "tastatura": _T, "vieta": "(x; y)",
         "padoms": "Atņem: 4y = 20."},
    ]),

    Pasaule("Divu veidu biļetes",
            Ievadi("", [
                {"jaut": "Muzejā pārdotas 120 biļetes: pilnās 8 € un skolēnu "
                         "5 €; ieņēmumi 810 €. x + y = 120, 8x + 5y = 810. "
                         "Pilno biļešu?", "atb": ["70"],
                 "padoms": "Ievietošana: y = 120 − x."},
                {"jaut": "Skolēnu biļešu?", "atb": ["50"],
                 "padoms": "120 − 70."},
            ]),
            pavediens="skola",
            konteksts="Muzeja kase zina kopējo biļešu skaitu un ieņēmumus.",
            kapec="x + y = ... uzreiz ļauj izteikt y."),

    Kopsavilkums([
        "Izvēlos paņēmienu pēc koeficientiem.",
        "Pamatoju izvēli.",
        "Atrisinu ar abām metodēm un salīdzinu.",
    ]),

    Majas([
        "Atrisini divos veidos: 2x + y = 7, x − y = 2.",
        "Kurš veids bija ātrāks? Kāpēc?",
        "Izdomā sistēmu, kurai ērtāka ir ievietošana.",
    ]),
]
