# -*- coding: utf-8 -*-
"""1. klase, 124. stunda: «Kādus jautājumus var uzdot?»

Par datiem tabulā vai diagrammā var uzdot dažādus jautājumus: cik? kurš
visvairāk? par cik? cik kopā? Skolēns veido savus jautājumus un atbild.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, kolonnas)

TEMA = "Kādus jautājumus var uzdot?"

MERKIS = ("Šodien veidosim savus jautājumus par datiem tabulā vai "
          "diagrammā.")

_LAIKS = kolonnas([("saule", 11), ("mākoņi", 6), ("lietus", 4),
                   ("sniegs", 1)])

SATURS = [
    Sakums("Laikapstākļi mēnesī - ko jautāt?",
           zimejums=_LAIKS,
           paraksts="Cik saulainu dienu? Par cik vairāk nekā lietainu?",
           fakti=["Cik ... ?",
                  "Kurš visvairāk / vismazāk?",
                  "Par cik? Cik kopā?"]),

    Doma("Jautājumu veidi",
         "Labs jautājums ir tāds, uz kuru var atbildēt ar datiem.",
         soli=[
             "«Cik?» - nolasa vienu skaitli.",
             "«Kurš visvairāk?» - salīdzina.",
             "«Par cik?» - atņem.",
             "«Cik kopā?» - saskaita.",
         ]),

    Ievadi("Atbildi uz saviem jautājumiem", [
        {"jaut": "Cik dienu bija saulainas?", "zim": _LAIKS, "atb": ["11"],
         "padoms": "Nolasi."},
        {"jaut": "Par cik saulainu vairāk nekā lietainu?", "zim": _LAIKS,
         "atb": ["7"], "padoms": "11 − 4."},
        {"jaut": "Cik dienu bija mākoņi vai lietus?", "zim": _LAIKS,
         "atb": ["10"], "padoms": "6 + 4."},
    ]),

    Varianti("Vai uz jautājumu var atbildēt?", [
        {"jaut": "«Kurā dienā lija lietus?»", "zim": _LAIKS,
         "opcijas": ["Nē - diagrammā nav datumu", "Jā"], "jaukt": False,
         "pareizi": 0, "padoms": "Ir tikai skaits."},
        {"jaut": "«Kādu laiku bija visbiežāk?»", "zim": _LAIKS,
         "opcijas": ["Jā - saule", "Nē"], "jaukt": False, "pareizi": 0,
         "padoms": "Augstākais stabiņš."},
    ]),

    Pasaule("Klases avīze",
            Varianti("", [
                {"jaut": "Tu raksti par laikapstākļiem avīzē. Kurš "
                         "jautājums interesantākais lasītājiem?",
                 "opcijas": ["Par cik saulainu dienu vairāk nekā lietainu?",
                             "Kā sauc diagrammu?"], "jaukt": False,
                 "pareizi": 0, "padoms": "Ar skaitļiem."},
            ]),
            pavediens="planeta",
            konteksts="Klase visu mēnesi pierakstīja laikapstākļus.",
            kapec="Labi jautājumi dara datus interesantus."),

    Kopsavilkums([
        "Uzdodu dažādus jautājumus par datiem.",
        "Pārbaudu, vai uz tiem var atbildēt.",
        "Atbildu uz saviem jautājumiem.",
    ]),

    Majas([
        "Izdomā 3 jautājumus par diagrammu mājās.",
        "Palūdz mājiniekam atbildēt.",
        "Pārbaudi atbildes.",
    ]),
]
