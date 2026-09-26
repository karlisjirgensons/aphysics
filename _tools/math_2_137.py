# -*- coding: utf-8 -*-
"""2. klase, 137. stunda: «Ko nozīmē reizināt ar 3?»

Reizināt ar 3 nozīmē: tikpat, tikpat un vēl tikpat. 4 · 3 = 4 + 4 + 4 -
trīs grupas pa 4 vai četras grupas pa 3. Modelē ar priekšmetiem un
pieraksta reizinājumu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, bildes)

TEMA = "Ko nozīmē reizināt ar 3?"

MERKIS = ("Šodien modelēsim ar priekšmetiem doto daudzumu un 3 reizes "
          "lielāku daudzumu un pierakstīsim reizinājumu.")


def _grupas(n, katra, ikona="abols"):
    return bildes([[(ikona, katra)]] * n)


SATURS = [
    Sakums("Cik ābolu 3 groziņos, ja katrā ir 4?",
           zimejums=_grupas(3, 4),
           paraksts="4 + 4 + 4 = 3 · 4 = 12.",
           fakti=["3 grozi pa 4 āboliem.",
                  "Trīs reizes pa 4 - reizināšana.",
                  "3 reizes vairāk - tikpat trīs reizes."]),

    Doma("Reizināt ar 3",
         "Reizināt ar 3 - saskaitīt trīs vienādus skaitļus.",
         soli=[
             "Nosaki, cik ir vienā grupā: 4.",
             "Grupu skaits: 3.",
             "Saskaiti: 4 + 4 + 4 = 12.",
             "Pieraksti: 3 · 4 = 12 vai 4 · 3 = 12.",
         ]),

    Slidnis("Trīs reizes vairāk", [
        {"v": "5", "teksts": "Viena grupa.", "zim": _grupas(1, 5, "zvaigzne")},
        {"v": "5 + 5", "teksts": "Divas grupas.",
         "zim": _grupas(2, 5, "zvaigzne")},
        {"v": "3 · 5 = 15", "teksts": "Trīs grupas - 15.",
         "zim": _grupas(3, 5, "zvaigzne")},
    ]),

    Ievadi("Reizini ar 3", [
        {"jaut": "Cik ir? Pieraksti kā reizinājumu un aprēķini.",
         "zim": _grupas(3, 2, "bumba"), "atb": ["6"], "padoms": "2 + 2 + 2."},
        {"jaut": "Cik zivju?", "zim": _grupas(3, 6, "zivs"), "atb": ["18"],
         "padoms": "6 + 6 + 6."},
        {"jaut": "3 · 7 = ?", "atb": ["21"], "padoms": "7 + 7 + 7."},
        {"jaut": "3 · 9 = ?", "atb": ["27"], "padoms": "9 + 9 + 9."},
        {"jaut": "3 · 10 = ?", "atb": ["30"], "padoms": "10 + 10 + 10."},
        {"jaut": "3 reizes vairāk nekā 8?", "atb": ["24"],
         "padoms": "8 + 8 + 8."},
    ], pamats=4),

    Varianti("Kurš pieraksts?", [
        {"jaut": "Kurš pieraksts atbilst 6 + 6 + 6?",
         "opcijas": ["3 · 6", "6 · 6", "3 + 6"], "pareizi": 0,
         "padoms": "Trīs reizes pa 6."},
        {"jaut": "Kas ir 3 reizes vairāk nekā 5?",
         "opcijas": ["15", "8", "53"], "pareizi": 0,
         "padoms": "5 + 5 + 5."},
    ]),

    Pasaule("Ģimenes brokastis",
            Ievadi("", [
                {"jaut": "Ģimenē 3 cilvēki, katrs apēd 2 olas. Cik olu "
                         "vajag?", "atb": ["6"], "padoms": "3 · 2."},
                {"jaut": "Katrs izdzer 3 krūzes tējas dienā. Cik krūzes "
                         "visi kopā?", "atb": ["9"], "padoms": "3 · 3."},
            ]),
            pavediens="virtuve",
            konteksts="Svētdienas brokastīm gatavo visai ģimenei.",
            kapec="Reizinot ātri zina, cik produktu vajag."),

    Kopsavilkums([
        "Modelēju reizināšanu ar 3 ar priekšmetiem.",
        "Pierakstu to kā reizinājumu.",
        "Aprēķinu, saskaitot trīs vienādus skaitļus.",
    ]),

    Majas([
        "Noliec 3 šķīvjus un uz katra 4 cepumus.",
        "Uzraksti reizinājumu un aprēķini.",
        "Izdomā vēl 2 piemērus ar 3 grupām.",
    ]),
]
