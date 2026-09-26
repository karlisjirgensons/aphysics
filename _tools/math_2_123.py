# -*- coding: utf-8 -*-
"""2. klase, 123. stunda: «Kā pieraksta reizināšanu?»

Vienādu saskaitāmo summu īsi pieraksta ar reizināšanas zīmi «·»:
2 + 2 + 2 + 2 + 2 = 5 · 2 - «pieci reiz divi». Latvijā reizināšanas zīme
ir punkts vidū, nevis «x». Pirmais skaitlis pasaka, cik reižu, otrais - cik
katrā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, bildes)

TEMA = "Kā pieraksta reizināšanu?"

MERKIS = ("Šodien lasīsim un pierakstīsim reizināšanu ar zīmi «·» un "
          "paskaidrosim, ko tā nozīmē.")


def _pari(n):
    """n pāri - katrs pāris savā rindā."""
    return bildes([[("ripina", 2)]] * n)


SATURS = [
    Sakums("Kā īsāk uzrakstīt 2 + 2 + 2 + 2 + 2?",
           zimejums=_pari(5),
           paraksts="5 rindas pa 2: 5 · 2 = 10.",
           fakti=["Vienādu skaitļu summu raksta ar reizināšanu.",
                  "5 · 2 lasa: «pieci reiz divi».",
                  "Latvijā reizināšanas zīme ir punkts «·»."]),

    Doma("Reizināšana",
         "Reizināšana ir vienādu saskaitāmo summas īss pieraksts.",
         soli=[
             "Saskaiti, cik reižu atkārtojas skaitlis: 5 reizes.",
             "Kāds skaitlis atkārtojas: 2.",
             "Pieraksti: 5 · 2.",
             "Rezultāts - reizinājums: 5 · 2 = 10.",
         ]),

    Slidnis("No summas uz reizinājumu", [
        {"v": "2 + 2 + 2", "teksts": "Trīs reizes pa 2.", "zim": _pari(3)},
        {"v": "3 · 2", "teksts": "«Trīs reiz divi».", "zim": _pari(3)},
        {"v": "3 · 2 = 6", "teksts": "Reizinājums ir 6.", "zim": _pari(3)},
    ]),

    Varianti("Pieraksti ar reizināšanu", [
        {"jaut": "2 + 2 + 2 + 2", "opcijas": ["4 · 2", "2 · 2", "4 + 2"],
         "pareizi": 0, "padoms": "Četras reizes pa 2."},
        {"jaut": "2 + 2 + 2 + 2 + 2 + 2 + 2", "opcijas": ["7 · 2", "2 · 2",
                                                           "7 + 2"],
         "pareizi": 0, "padoms": "Saskaiti divniekus."},
        {"jaut": "Kā lasa 6 · 2?", "opcijas": ["seši reiz divi",
                                               "seši plus divi",
                                               "seši dalīts ar divi"],
         "pareizi": 0, "padoms": "«·» - reiz."},
        {"jaut": "Kurš ir reizināšanas pieraksts?",
         "opcijas": ["8 · 2", "8 : 2", "8 − 2"], "pareizi": 0,
         "padoms": "Punkts vidū."},
    ]),

    Ievadi("Aprēķini", [
        {"jaut": "4 · 2 = ?", "zim": _pari(4), "atb": ["8"],
         "padoms": "2 + 2 + 2 + 2."},
        {"jaut": "6 · 2 = ?", "zim": _pari(6), "atb": ["12"],
         "padoms": "Skaiti pa 2."},
        {"jaut": "8 · 2 = ?", "atb": ["16"], "padoms": "8 reizes pa 2."},
        {"jaut": "10 · 2 = ?", "atb": ["20"], "padoms": "10 + 10."},
    ]),

    Pasaule("Velosipēdu stāvvieta",
            Ievadi("", [
                {"jaut": "Stāvvietā 7 velosipēdi, katram 2 riteņi. Uzraksti "
                         "kā reizinājumu un aprēķini: 7 · 2 = ?",
                 "atb": ["14"], "padoms": "7 reizes pa 2."},
            ]),
            pavediens="celojums",
            konteksts="Pie skolas ir velosipēdu stāvvieta.",
            kapec="Reizināšana ir īsāka nekā garš saskaitījums."),

    Kopsavilkums([
        "Pierakstu vienādu saskaitāmo summu ar reizināšanu.",
        "Lasu «·» kā «reiz».",
        "Aprēķinu reizinājumu ar 2.",
    ]),

    Majas([
        "Atrodi mājās lietas pa 2 un pieraksti ar «·».",
        "Piemēram: 3 pāri zeķu - 3 · 2 = 6.",
        "Izdomā 3 šādus piemērus.",
    ]),
]
