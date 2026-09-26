# -*- coding: utf-8 -*-
"""1. klase, 46. stunda: «Cik gara ir lauzta līnija?»

Lauztas līnijas garums ir visu posmu garumu summa: 2 cm + 3 cm = 5 cm.
Katru posmu izmēra atsevišķi, pieraksta ar mērvienību un saskaita.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, linijas)


def _lauzta(punkti, garumi):
    """Lauzta līnija rūtiņās ar posmu garumiem pie katra posma."""
    nogr = [(punkti[i][0], punkti[i][1], punkti[i + 1][0], punkti[i + 1][1])
            for i in range(len(punkti) - 1)]
    uzr = [((a + c) / 2.0, (b + d) / 2.0 + 0.7, "%d cm" % g)
           for (a, b, c, d), g in zip(nogr, garumi)]
    return linijas(nogr, uzraksti=uzr, punkti=punkti, platums=12,
                   augstums=6)


TEMA = "Cik gara ir lauzta līnija?"

MERKIS = ("Šodien izmērīsim lauztas līnijas posmus un saskaitīsim to "
          "garumus.")

_L1 = _lauzta([(1, 1), (4, 4), (9, 1)], [2, 3])

SATURS = [
    Sakums("Kā izmērīt līniju, kas nav taisna?",
           zimejums=_L1,
           paraksts="2 cm + 3 cm = 5 cm.",
           fakti=["Lauzta līnija sastāv no taisniem posmiem.",
                  "Katru posmu izmēra atsevišķi.",
                  "Garumus saskaita."]),

    Paraugs("Lauztas līnijas garums",
            uzd="Lauztai līnijai ir divi posmi: 2 cm un 3 cm. Cik gara ir "
                "visa līnija?",
            soli=[
                ("2 cm + 3 cm", "Posmu garumu summa."),
                ("2 cm + 3 cm = 5 cm", "Saskaita skaitļus, mērvienība "
                                      "paliek."),
            ],
            atbilde="līnija ir 5 cm gara."),

    Doma("Posmi kopā",
         "Visa līnija ir tik gara, cik visi posmi kopā.",
         soli=[
             "Saskaiti posmus.",
             "Izmēri katru posmu no punkta līdz punktam.",
             "Saskaiti garumus un pieliec «cm».",
         ]),

    Ievadi("Aprēķini garumu", [
        {"jaut": "Cik cm gara ir līnija?",
         "zim": _lauzta([(1, 1), (5, 5), (9, 1)], [4, 4]), "atb": ["8"],
         "padoms": "4 + 4."},
        {"jaut": "Cik cm gara ir līnija?",
         "zim": _lauzta([(0, 1), (3, 5), (6, 1), (10, 4)], [3, 3, 2]),
         "atb": ["8"], "padoms": "3 + 3 + 2."},
        {"jaut": "1 cm + 6 cm = ? cm", "atb": ["7"], "padoms": "1 + 6."},
        {"jaut": "Līnija 9 cm, viens posms 5 cm. Cik garš otrs?",
         "atb": ["4"], "padoms": "5 + ? = 9."},
    ]),

    Varianti("Kurš pieraksts pareizs?", [
        {"jaut": "Posmi 4 cm un 5 cm.",
         "opcijas": ["4 cm + 5 cm = 9 cm", "4 + 5 = 9 cm cm",
                     "4 cm + 5 cm = 10 cm"], "pareizi": 0,
         "padoms": "Mērvienība katram skaitlim vienreiz."},
    ]),

    Pasaule("Skudras ceļš",
            Ievadi("", [
                {"jaut": "Skudra rāpo pa lauztu ceļu: 3 cm, 2 cm, 4 cm. Cik "
                         "cm tā norāpoja?", "atb": ["9"],
                 "padoms": "3 + 2 + 4."},
                {"jaut": "Taisni būtu 6 cm. Par cik cm ceļš garāks?",
                 "atb": ["3"], "padoms": "9 − 6."},
            ]),
            pavediens="daba",
            konteksts="Skudra neiet taisni - tā apiet akmentiņus.",
            kapec="Lauzts ceļš ir garāks par taisnu."),

    Kopsavilkums([
        "Mēru lauztas līnijas posmus.",
        "Saskaitu garumus: 2 cm + 3 cm = 5 cm.",
        "Zinu, ka lauzta līnija garāka par taisnu.",
    ]),

    Majas([
        "Uzzīmē lauztu līniju ar 3 posmiem un aprēķini garumu.",
        "Ar diegu izmēri lauztu ceļu un salīdzini ar lineālu.",
        "Izdomā skudras ceļu 10 cm garumā.",
    ]),
]
