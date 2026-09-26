# -*- coding: utf-8 -*-
"""1. klase, 147. stunda: «Kā pieskaitīt vienus?»

43 + 5: desmiti paliek, vieniem 3 + 5 = 8 - 48. Simta kvadrātā - soļi pa
labi. Atņem tāpat: 48 − 5 = 43. (Bez pāriešanas pāri desmitam.)
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, simta_kvadrats)

TEMA = "Kā pieskaitīt vienus?"

MERKIS = ("Šodien divciparu skaitlim pieskaitīsim un atņemsim viencipara "
          "skaitli, izmantojot simta kvadrātu.")

SATURS = [
    Sakums("43 + 5 - kur simta kvadrātā?",
           zimejums=simta_kvadrats(41, 50, izcelt=[44, 45, 46, 47, 48]),
           paraksts="No 43 pieci soļi pa labi: 48.",
           fakti=["Desmiti paliek.",
                  "Vieni: 3 + 5 = 8.",
                  "Simta kvadrātā - pa labi."]),

    Doma("Desmiti paliek",
         "Pieskaitot vienus (bez pāriešanas), mainās tikai vienu cipars.",
         soli=[
             "43 + 5: vieni 3 + 5 = 8.",
             "Desmiti paliek 4.",
             "Atbilde: 48.",
         ]),

    Ievadi("Aprēķini", [
        {"jaut": "43 + 5 = ?", "atb": ["48"], "padoms": "3 + 5."},
        {"jaut": "62 + 7 = ?", "atb": ["69"], "padoms": "2 + 7."},
        {"jaut": "86 − 4 = ?", "atb": ["82"], "padoms": "6 − 4."},
        {"jaut": "35 + 4 = ?", "atb": ["39"], "padoms": "5 + 4."},
        {"jaut": "79 − 9 = ?", "atb": ["70"], "padoms": "9 − 9."},
        {"jaut": "51 + 8 = ?", "atb": ["59"], "padoms": "1 + 8."},
    ], pamats=4),

    Varianti("Kurš ir pareizs?", [
        {"jaut": "24 + 3",
         "opcijas": ["27", "54", "21"], "pareizi": 0,
         "padoms": "Vieni: 4 + 3."},
        {"jaut": "68 − 5",
         "opcijas": ["63", "18", "73"], "pareizi": 0,
         "padoms": "Vieni: 8 − 5."},
    ]),

    Pasaule("Klases grāmatu plaukts",
            Ievadi("", [
                {"jaut": "Plauktā 64 grāmatas. Bērni atnesa vēl 5. Cik "
                         "tagad?", "atb": ["69"], "padoms": "4 + 5."},
            ]),
            pavediens="skola",
            konteksts="Klases bibliotēka aug.",
            kapec="Pieskaitot vienus, desmiti nemainās."),

    Kopsavilkums([
        "Pieskaitu vienus divciparu skaitlim.",
        "Atņemu vienus.",
        "Izmantoju simta kvadrātu.",
    ]),

    Majas([
        "Izrēķini 72 + 6, 58 − 3, 41 + 7.",
        "Parādi simta kvadrātā.",
        "Izdomā savu piemēru.",
    ]),
]
