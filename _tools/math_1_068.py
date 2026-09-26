# -*- coding: utf-8 -*-
"""1. klase, 68. stunda: «Cik apmēram ir?»

Lielu skaitu novērtē aptuveni: saskaita vienu grupu (piemēram, vienu
rindu) un iedomājas, cik tādu grupu ir. Tad pārbauda, saskaitot pa 10.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, bildes)

TEMA = "Cik apmēram ir?"

MERKIS = ("Šodien novērtēsim, cik apmēram ir priekšmetu, un pārbaudīsim, "
          "saskaitot.")

_ZVAIGZNES = bildes([[("zvaigzne", 10)]] * 3 + [[("zvaigzne", 8)]])

SATURS = [
    Sakums("Cik zvaigžņu? Mini, pirms skaiti!",
           zimejums=_ZVAIGZNES,
           paraksts="Rindā apmēram 10, rindu 4 - apmēram 40.",
           fakti=["Aplēse - ātrs, gudrs minējums.",
                  "Saskaiti vienu rindu un rindas.",
                  "Pārbaudi, skaitot pa 10."]),

    Doma("Gudra aplēse",
         "Saskaiti mazu daļu un iedomājies, cik tādu daļu ir.",
         soli=[
             "Saskaiti vienu rindu vai grupu.",
             "Saskaiti, cik tādu grupu.",
             "Nosauc aplēsi: «apmēram 40».",
             "Pārbaudi - saskaiti pa 10.",
         ]),

    Ievadi("Novērtē un pārbaudi", [
        {"jaut": "Cik zvaigžņu ir īstenībā?", "zim": _ZVAIGZNES,
         "atb": ["38"], "padoms": "3 pilnas rindas un 8."},
        {"jaut": "Cik ābolu?", "zim": bildes([[("abols", 10)]] * 2 +
                                             [[("abols", 5)]]),
         "atb": ["25"], "padoms": "2 rindas pa 10 un 5."},
    ]),

    Varianti("Kura aplēse labāka?", [
        {"jaut": "Burkā ir 47 konfektes. Kura aplēse vistuvāk?",
         "opcijas": ["apmēram 50", "apmēram 10", "apmēram 100"],
         "pareizi": 0, "padoms": "47 ir tuvu 50."},
        {"jaut": "Klasē ir 23 bērni. Kura aplēse vistuvāk?",
         "opcijas": ["apmēram 20", "apmēram 50", "apmēram 5"],
         "pareizi": 0, "padoms": "23 ir tuvu 20."},
        {"jaut": "Grāmatā 96 lappuses.",
         "opcijas": ["apmēram 100", "apmēram 60", "apmēram 10"],
         "pareizi": 0, "padoms": "Gandrīz 100."},
    ]),

    Pasaule("Putni uz vada",
            Varianti("", [
                {"jaut": "Uz vada sēž putni. Vienā metrā apmēram 10, vads 5 m. "
                         "Cik apmēram putnu?",
                 "opcijas": ["apmēram 50", "apmēram 10", "apmēram 100"],
                 "pareizi": 0, "padoms": "10, 20, 30, 40, 50."},
            ]),
            pavediens="daba",
            konteksts="Rudenī bezdelīgas pulcējas uz vadiem.",
            kapec="Kustīgus putnus nevar saskaitīt precīzi - aplēse der."),

    Kopsavilkums([
        "Novērtēju lielu skaitu aptuveni.",
        "Lietoju vienu grupu aplēsei.",
        "Pārbaudu, skaitot pa 10.",
    ]),

    Majas([
        "Novērtē, cik zirņu ir saujā, tad saskaiti.",
        "Novērtē, cik grāmatu ir plauktā.",
        "Cik tuvu biji?",
    ]),
]
