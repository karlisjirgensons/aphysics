# -*- coding: utf-8 -*-
"""1. klase, 27. stunda: «Kas notiek, ja tas pats iznāk otrreiz?»

Datus ieraksta tabulā tādā secībā, kā tie iegūti; ja iznākums atkārtojas,
to atzīmē (ar ķeksīti). Tā redz, kas iznāk bieži un kas vēl nav iznācis.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Varianti, restis)

TEMA = "Kas notiek, ja tas pats iznāk otrreiz?"

MERKIS = ("Šodien ierakstīsim datus tabulā pēc kārtas un atzīmēsim tos, kas "
          "atkārtojas.")

_TABULA = restis([["V", "O", "✓"], [3, 2, ""], [1, 4, ""], [3, 2, "✓"],
                  [4, 1, ""], [1, 4, "✓"]])

SATURS = [
    Sakums("3 un 2 iznāca vēlreiz - ko darīt?",
           zimejums=_TABULA,
           paraksts="Atkārtojumu atzīmē ar ķeksīti.",
           fakti=["Pieraksti visu pēc kārtas.",
                  "Ja tas pats iznāk vēlreiz - pieliec ķeksīti.",
                  "Tā redz, kas iznāk bieži."]),

    Doma("Atkārtojums",
         "Arī atkārtots iznākums ir dati - to nemet ārā, bet atzīmē.",
         soli=[
             "Ieraksti iznākumu jaunā rindā.",
             "Paskaties augstāk: vai tāds jau bija?",
             "Ja bija - pieliec ✓.",
         ]),

    Ievadi("Nolasi tabulu", [
        {"jaut": "Cik reizes izbēra?", "zim": _TABULA, "atb": ["5"],
         "padoms": "Saskaiti rindas."},
        {"jaut": "Cik atkārtojumu (✓)?", "zim": _TABULA, "atb": ["2"],
         "padoms": "Saskaiti ķeksīšus."},
        {"jaut": "Cik reizes iznāca 3 un 2?", "zim": _TABULA, "atb": ["2"],
         "padoms": "Meklē rindas ar 3 un 2."},
        {"jaut": "Cik dažādu iznākumu bija?", "zim": _TABULA, "atb": ["3"],
         "padoms": "3+2, 1+4, 4+1."},
    ]),

    Varianti("Kurš iznākums vēl nav bijis?", [
        {"jaut": "Kurš no šiem vēl nav bijis tabulā?", "zim": _TABULA,
         "opcijas": ["2 un 3", "3 un 2", "1 un 4"], "pareizi": 0,
         "padoms": "2 violetas, 3 oranžas - meklē."},
    ]),

    Petijums("Izber un atzīmē", [
        "Izber 5 ripiņas 8 reizes.",
        "Katru reizi ieraksti rindā V un O.",
        "Ja tāds jau bija - pieliec ✓.",
        "Kurš iznākums bija visbiežāk?",
    ], vajag="5 divpusējas ripiņas, tabula"),

    Pasaule("Kas nāk uz skolu?",
            Ievadi("", [
                {"jaut": "Skolotāja pierakstīja, kā bērni nāk: kājām, kājām, "
                         "ar autobusu, kājām, ar auto. Cik reizes «kājām»?",
                 "atb": ["3"], "padoms": "Saskaiti vārdu «kājām»."},
                {"jaut": "Cik dažādu veidu bija?", "atb": ["3"],
                 "padoms": "Kājām, autobuss, auto."},
            ]),
            pavediens="skola",
            konteksts="Rītā skolotāja pieraksta, kā katrs atnāca.",
            kapec="Atkārtojumi parāda, kas ir visbiežāk."),

    Kopsavilkums([
        "Ierakstu datus pēc kārtas.",
        "Atzīmēju atkārtotos iznākumus.",
        "Nolasu, kas bija visbiežāk.",
    ]),

    Majas([
        "Met kauliņu 10 reizes un pieraksti; atzīmē atkārtojumus.",
        "Kurš skaitlis iznāca visbiežāk?",
        "Vai kāds skaitlis neiznāca ne reizi?",
    ]),
]
