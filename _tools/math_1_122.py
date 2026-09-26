# -*- coding: utf-8 -*-
"""1. klase, 122. stunda: «Kurš stabiņš ir augstākais?»

Stabiņu diagrammā katram lielumam - stabiņš. Augstākais stabiņš - lielākais
lielums. Skaitli nolasa virs stabiņa.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, kolonnas)

TEMA = "Kurš stabiņš ir augstākais?"

MERKIS = ("Šodien lasīsim stabiņu diagrammu un salīdzināsim lielumus.")

_MAJDZ = kolonnas([("kaķis", 7), ("suns", 9), ("zivtiņas", 3),
                   ("trusis", 2)])

SATURS = [
    Sakums("Kāds mājdzīvnieks klasē ir visbiežāk?",
           zimejums=_MAJDZ,
           paraksts="Augstākais stabiņš - suns: 9 bērni.",
           fakti=["Katram dzīvniekam - stabiņš.",
                  "Jo augstāks, jo vairāk.",
                  "Skaitlis virs stabiņa."]),

    Doma("Lasām diagrammu",
         "Diagramma parāda uzreiz, kas lielākais un mazākais.",
         soli=[
             "Izlasi nosaukumus zem stabiņiem.",
             "Atrodi augstāko un zemāko.",
             "Nolasi skaitļus virs tiem.",
         ]),

    Ievadi("Nolasi", [
        {"jaut": "Cik bērniem ir kaķis?", "zim": _MAJDZ, "atb": ["7"],
         "padoms": "Skaitlis virs stabiņa."},
        {"jaut": "Cik bērniem ir zivtiņas?", "zim": _MAJDZ, "atb": ["3"],
         "padoms": "Skaitlis virs stabiņa."},
        {"jaut": "Cik ir augstākā stabiņa skaitlis?", "zim": _MAJDZ,
         "atb": ["9"], "padoms": "Suns."},
    ]),

    Varianti("Kurš?", [
        {"jaut": "Kurš stabiņš zemākais?", "zim": _MAJDZ,
         "opcijas": ["trusis", "zivtiņas", "kaķis", "suns"], "pareizi": 0,
         "padoms": "Mazākais skaitlis."},
        {"jaut": "Kurš ir otrais augstākais?", "zim": _MAJDZ,
         "opcijas": ["kaķis", "suns", "trusis", "zivtiņas"], "pareizi": 0,
         "padoms": "Pēc suņa."},
    ]),

    Pasaule("Mīļākais auglis",
            Varianti("", [
                {"jaut": "Kuru augli klase mīl visvairāk?",
                 "zim": kolonnas([("ābols", 8), ("banāns", 11),
                                  ("apelsīns", 5)]),
                 "opcijas": ["banānu", "ābolu", "apelsīnu"], "pareizi": 0,
                 "padoms": "Augstākais stabiņš."},
            ]),
            pavediens="virtuve",
            konteksts="Klase balsoja par mīļāko augli.",
            kapec="Diagrammā uzvarētāju redz uzreiz."),

    Kopsavilkums([
        "Lasu stabiņu diagrammu.",
        "Atrodu augstāko un zemāko stabiņu.",
        "Nolasu skaitļus.",
    ]),

    Majas([
        "Uzzīmē diagrammu: cik cilvēku ģimenē mīl tēju, kafiju, sulu.",
        "Kurš stabiņš augstākais?",
        "Parādi diagrammu mājiniekiem.",
    ]),
]
