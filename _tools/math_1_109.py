# -*- coding: utf-8 -*-
"""1. klase, 109. stunda: «Kurš skaitlis ir par 4 lielāks?»

«Par 4 lielāks nekā 9» - pieskaita: 9 + 4 = 13. «Par 4 mazāks nekā 13» -
atņem: 13 − 4 = 9. Sloksnē: pieliek vai nogriež 4 rūtiņas.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, sloksnes)

TEMA = "Kurš skaitlis ir par 4 lielāks?"

MERKIS = ("Šodien aprēķināsim skaitli, kas ir par doto lielāks vai mazāks "
          "nekā zināmais.")

SATURS = [
    Sakums("Kurš skaitlis ir par 4 lielāks nekā 9?",
           zimejums=sloksnes([("9", 9), ("?", 13, "?")]),
           paraksts="Pieliek 4 rūtiņas: 9 + 4 = 13.",
           fakti=["«Par tik lielāks» - pieskaiti.",
                  "«Par tik mazāks» - atņem.",
                  "Sloksnē - pieliec vai nogriez."]),

    Doma("Lielāks vai mazāks",
         "«Par 4 lielāks» - tikpat un vēl 4; «par 4 mazāks» - bez 4.",
         soli=[
             "Izlasi: lielāks vai mazāks?",
             "Lielāks - «+», mazāks - «−».",
             "Aprēķini.",
         ]),

    Ievadi("Aprēķini", [
        {"jaut": "Par 4 lielāks nekā 9?", "atb": ["13"], "padoms": "9 + 4."},
        {"jaut": "Par 4 mazāks nekā 13?", "atb": ["9"], "padoms": "13 − 4."},
        {"jaut": "Par 6 lielāks nekā 8?", "atb": ["14"], "padoms": "8 + 6."},
        {"jaut": "Par 5 mazāks nekā 12?", "atb": ["7"], "padoms": "12 − 5."},
        {"jaut": "Par 10 lielāks nekā 7?", "atb": ["17"], "padoms": "7 + 10."},
        {"jaut": "Par 3 mazāks nekā 20?", "atb": ["17"], "padoms": "20 − 3."},
    ], pamats=4),

    Varianti("Kura darbība?", [
        {"jaut": "Par 7 lielāks nekā 6",
         "opcijas": ["6 + 7", "6 − 7", "7 − 6"], "pareizi": 0,
         "padoms": "Lielāks - pieskaiti."},
        {"jaut": "Par 8 mazāks nekā 15",
         "opcijas": ["15 − 8", "15 + 8", "8 − 15"], "pareizi": 0,
         "padoms": "Mazāks - atņem."},
    ]),

    Pasaule("Brāļa gadi",
            Ievadi("", [
                {"jaut": "Tev 7 gadi, brālis par 5 gadiem vecāks. Cik "
                         "brālim?", "atb": ["12"], "padoms": "7 + 5."},
                {"jaut": "Māsa par 3 gadiem jaunāka nekā tu. Cik māsai?",
                 "atb": ["4"], "padoms": "7 − 3."},
            ]),
            pavediens="maja",
            konteksts="Ģimenē visi ir dažāda vecuma.",
            kapec="«Vecāks par» - pieskaita, «jaunāks par» - atņem."),

    Kopsavilkums([
        "Atrodu skaitli, kas par tik lielāks.",
        "Atrodu skaitli, kas par tik mazāks.",
        "Izvēlos pareizo darbību.",
    ]),

    Majas([
        "Kurš skaitlis ir par 6 lielāks nekā tavs vecums?",
        "Par 3 mazāks nekā tavs mājas numurs?",
        "Izdomā 2 šādus jautājumus mājiniekam.",
    ]),
]
