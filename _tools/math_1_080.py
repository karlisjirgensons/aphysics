# -*- coding: utf-8 -*-
"""1. klase, 80. stunda: «Kas notiek, ja pieskaita vairāk?»

Ja pieskaitāmais palielinās par 1, arī summa palielinās par 1:
12 + 3 = 15, 12 + 4 = 16, 12 + 5 = 17. To pēta piemēru virknē.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, restis)

TEMA = "Kas notiek, ja pieskaita vairāk?"

MERKIS = ("Šodien pētīsim, kā mainās summa, ja maina pieskaitāmo skaitli.")

_VIRKNE = restis([["12 + 3", 15], ["12 + 4", 16], ["12 + 5", None]])

SATURS = [
    Sakums("12 + 3, 12 + 4, 12 + 5 - ko tu pamani?",
           zimejums=_VIRKNE,
           paraksts="Pieskaitāmais +1 - arī summa +1.",
           fakti=["Pirmais skaitlis paliek tas pats.",
                  "Pieskaitāmais aug pa 1.",
                  "Summa arī aug pa 1."]),

    Doma("Vairāk klāt - vairāk kopā",
         "Par cik palielina pieskaitāmo, par tik palielinās summa.",
         soli=[
             "Salīdzini divus piemērus.",
             "Par cik atšķiras pieskaitāmie?",
             "Par tik pat atšķiras summas.",
         ]),

    Ievadi("Turpini virkni", [
        {"jaut": "Kas ir «?»", "zim": _VIRKNE, "atb": ["17"],
         "padoms": "16 + 1."},
        {"jaut": "11 + 2 = 13. Cik ir 11 + 3?", "atb": ["14"],
         "padoms": "Par 1 vairāk."},
        {"jaut": "14 + 2 = 16. Cik ir 14 + 4?", "atb": ["18"],
         "padoms": "Par 2 vairāk."},
        {"jaut": "10 + 5 = 15. Cik ir 10 + 4?", "atb": ["14"],
         "padoms": "Par 1 mazāk."},
    ]),

    Varianti("Kā mainās?", [
        {"jaut": "13 + 2 un 13 + 5. Par cik otrā summa lielāka?",
         "opcijas": ["par 3", "par 2", "par 5"], "pareizi": 0,
         "padoms": "5 − 2 = 3."},
        {"jaut": "Ja pieskaita 0, summa...",
         "opcijas": ["nemainās", "palielinās par 1", "kļūst 0"],
         "pareizi": 0, "padoms": "Nekas netika pielikts."},
    ]),

    Pasaule("Uzlīmju albums",
            Ievadi("", [
                {"jaut": "Albumā 12 uzlīmes. Ja pieliek 3 - cik?",
                 "atb": ["15"], "padoms": "12 + 3."},
                {"jaut": "Ja pieliek 6 (par 3 vairāk) - cik?", "atb": ["18"],
                 "padoms": "15 + 3."},
            ]),
            pavediens="speles",
            konteksts="Uzlīmes pienāk dažādos daudzumos.",
            kapec="Paredzi rezultātu bez pārrēķināšanas."),

    Kopsavilkums([
        "Pētu, kā mainās summa.",
        "Zinu: par cik vairāk klāt, par tik vairāk kopā.",
        "Izmantoju to aprēķinos.",
    ]),

    Majas([
        "Uzraksti virkni: 10 + 1, 10 + 2, ... līdz 10 + 9.",
        "Ko pamani summās?",
        "Izdomā virkni ar 13 + ...",
    ]),
]
