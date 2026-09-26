# -*- coding: utf-8 -*-
"""2. klase, 124. stunda: «Kā pieraksta dalīšanu?»

Dalīšanu pieraksta ar zīmi «:» - 12 : 2 = 6. Tai ir divas nozīmes, ko jau
iepazina: sadalīt 2 vienādās daļās (cik katrā?) un sadalīt pa 2 (cik
daļu?). Abas pieraksta vienādi.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, bildes)

TEMA = "Kā pieraksta dalīšanu?"

MERKIS = ("Šodien lasīsim un pierakstīsim dalīšanu ar zīmi «:» un "
          "paskaidrosim abas dalīšanas nozīmes.")

_DIVAS = ["uz pusēm - cik katrā", "pa 2 - cik daļu"]

SATURS = [
    Sakums("Kā ar zīmēm pierakstīt «12 konfektes sadala 2 bērniem»?",
           zimejums=bildes([[("ripina", 6)], [("ripina", 6)]]),
           paraksts="12 : 2 = 6 - katram 6.",
           fakti=["Dalīšanas zīme ir kols «:».",
                  "12 : 2 lasa «divpadsmit dalīts ar divi».",
                  "Tas pats pieraksts der arī «pa 2»."]),

    Doma("Dalīšana",
         "12 : 2 ir tas pats skaitlis abās dalīšanas nozīmēs.",
         soli=[
             "Uz pusēm: 12 sadala 2 daļās - katrā 6.",
             "Pa 2: 12 sadala pa 2 - 6 daļas.",
             "Abos pieraksta 12 : 2 = 6.",
             "Rezultātu sauc par dalījumu.",
         ]),

    Varianti("Kura nozīme?", [
        {"jaut": "«10 āboli 2 grozos vienādi.» 10 : 2", "opcijas": _DIVAS,
         "jaukt": False, "pareizi": 0, "padoms": "Grozu skaits zināms."},
        {"jaut": "«10 āboli pa 2 maisiņos.» 10 : 2", "opcijas": _DIVAS,
         "jaukt": False, "pareizi": 1, "padoms": "Maisiņu skaits nezināms."},
        {"jaut": "Kā lasa 18 : 2?",
         "opcijas": ["astoņpadsmit dalīts ar divi",
                     "astoņpadsmit reiz divi", "astoņpadsmit mīnus divi"],
         "pareizi": 0, "padoms": "«:» - dalīts ar."},
        {"jaut": "Kurš ir dalīšanas pieraksts?",
         "opcijas": ["14 : 2", "14 · 2", "14 + 2"], "pareizi": 0,
         "padoms": "Kols."},
    ]),

    Ievadi("Aprēķini", [
        {"jaut": "8 : 2 = ?", "atb": ["4"], "padoms": "4 + 4 = 8."},
        {"jaut": "16 : 2 = ?", "atb": ["8"], "padoms": "8 + 8."},
        {"jaut": "20 : 2 = ?", "atb": ["10"], "padoms": "10 + 10."},
        {"jaut": "14 : 2 = ?", "atb": ["7"], "padoms": "7 + 7."},
        {"jaut": "6 : 2 = ?", "atb": ["3"], "padoms": "3 + 3."},
        {"jaut": "18 : 2 = ?", "atb": ["9"], "padoms": "9 + 9."},
    ], pamats=4),

    Pasaule("Galda spēle diviem",
            Ievadi("", [
                {"jaut": "Spēlē 16 kārtis sadala 2 spēlētājiem vienādi. "
                         "16 : 2 = ?", "atb": ["8"], "padoms": "8 + 8."},
                {"jaut": "Kārtis liek pa 2 kaudzītēs. Cik kaudzīšu no 16?",
                 "atb": ["8"], "padoms": "Arī 16 : 2."},
            ]),
            pavediens="speles",
            konteksts="Kāršu spēlē kārtis izdala godīgi.",
            kapec="Viens pieraksts - divas situācijas."),

    Kopsavilkums([
        "Pierakstu dalīšanu ar zīmi «:».",
        "Zinu abas dalīšanas nozīmes.",
        "Aprēķinu dalījumu ar 2.",
    ]),

    Majas([
        "Sadali 12 karotes 2 kaudzītēs un pieraksti ar «:».",
        "Sadali tās pašas pa 2 un pieraksti.",
        "Vai pieraksti sakrīt?",
    ]),
]
