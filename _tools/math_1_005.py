# -*- coding: utf-8 -*-
"""1. klase, 5. stunda: «Kur ir vairāk - pie loga vai pie durvīm?»

Divas grupas salīdzina divējādi: saliek pa pāriem (kam pāra nav, tās ir
vairāk) vai saskaita un salīdzina skaitļus. Vārdi: vairāk, mazāk, tikpat.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, bildes)

TEMA = "Kur ir vairāk - pie loga vai pie durvīm?"

MERKIS = ("Šodien salīdzināsim divas grupas un teiksim: vairāk, mazāk vai "
          "tikpat.")


def _divas(a, na, b, nb, uzraksti=("pie loga", "pie durvīm")):
    return bildes([[(a, na)], [(b, nb)]], uzraksti=list(uzraksti))


SATURS = [
    Sakums("Kur ir vairāk krēslu?",
           zimejums=_divas("kresls", 5, "kresls", 3),
           paraksts="Pa pāriem: pie loga 2 krēsliem pāra nav.",
           fakti=["Saliec pa pāriem - kam pāra nav, to ir vairāk.",
                  "Vai saskaiti abas grupas.",
                  "Ja pāri sanāk visiem - to ir tikpat."]),

    Doma("Pa pāriem vai saskaitot",
         "Kur paliek lietas bez pāra, tur ir vairāk.",
         soli=[
             "Saliec vienu no katras grupas pārī.",
             "Paskaties, kur palika lietas bez pāra.",
             "Vai saskaiti: 5 ir vairāk nekā 3.",
         ],
         pieze="Ja katram ir pāris, abās grupās ir tikpat."),

    Varianti("Vairāk, mazāk vai tikpat?", [
        {"jaut": "Kur ir vairāk?", "zim": _divas("abols", 4, "abols", 6),
         "opcijas": ["pie loga", "pie durvīm", "tikpat"], "jaukt": False,
         "pareizi": 1, "padoms": "Pie durvīm 2 bez pāra."},
        {"jaut": "Kur ir vairāk?", "zim": _divas("bumba", 5, "bumba", 5),
         "opcijas": ["pie loga", "pie durvīm", "tikpat"], "jaukt": False,
         "pareizi": 2, "padoms": "Visām ir pāris."},
        {"jaut": "Kur ir mazāk?", "zim": _divas("soma", 3, "soma", 7),
         "opcijas": ["pie loga", "pie durvīm", "tikpat"], "jaukt": False,
         "pareizi": 0, "padoms": "3 ir mazāk nekā 7."},
        {"jaut": "Kur ir vairāk?", "zim": _divas("puke", 8, "puke", 6),
         "opcijas": ["pie loga", "pie durvīm", "tikpat"], "jaukt": False,
         "pareizi": 0, "padoms": "8 ir vairāk nekā 6."},
    ]),

    Ievadi("Cik bez pāra?", [
        {"jaut": "Cik ābolu paliek bez pāra?",
         "zim": _divas("abols", 6, "abols", 4), "atb": ["2"],
         "padoms": "Saliec pa pāriem."},
        {"jaut": "Cik zīmuļu paliek bez pāra?",
         "zim": _divas("zimulis", 3, "zimulis", 7), "atb": ["4"],
         "padoms": "Apakšā 4 bez pāra."},
        {"jaut": "Cik bumbu jāpieliek augšā, lai būtu tikpat?",
         "zim": _divas("bumba", 2, "bumba", 5), "atb": ["3"],
         "padoms": "Apakšā 3 bez pāra."},
    ]),

    Pasaule("Karotes pie galda",
            Varianti("", [
                {"jaut": "Pie galda sēž 6 bērni, uz galda ir 5 karotes. Vai "
                         "pietiek?",
                 "zim": bildes([[("karote", 5)], [("kresls", 6)]]),
                 "opcijas": ["Nē, pietrūkst 1", "Jā, pietiek",
                             "Paliek 1 lieka"], "jaukt": False,
                 "pareizi": 0, "padoms": "Vienam krēslam karotes nav."},
                {"jaut": "Tagad ir 6 karotes un 6 bērni.",
                 "opcijas": ["Tikpat - pietiek visiem", "Pietrūkst",
                             "Paliek liekas"], "jaukt": False,
                 "pareizi": 0, "padoms": "Katram pa vienai."},
            ]),
            pavediens="virtuve",
            konteksts="Klājot galdu, katram bērnam vajag vienu karoti.",
            kapec="Pa pāriem salīdzina, pat neskaitot."),

    Kopsavilkums([
        "Salīdzinu divas grupas pa pāriem.",
        "Salīdzinu, saskaitot abas.",
        "Lietoju vārdus vairāk, mazāk, tikpat.",
    ]),

    Majas([
        "Salīdzini: kā ir vairāk mājās - krēslu vai cilvēku?",
        "Klājot galdu, noliec katram vienu šķīvi un vienu karoti.",
        "Saliec zeķes pa pāriem - vai kāda palika bez pāra?",
    ]),
]
