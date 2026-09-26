# -*- coding: utf-8 -*-
"""1. klase, 99. stunda: «Kas mainās, ja atņem vairāk?»

No viena skaitļa atņem arvien lielākus skaitļus: 15 − 5 = 10, 15 − 6 = 9,
15 − 7 = 8. Par cik vairāk atņem, par tik mazāk paliek.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, restis)

TEMA = "Kas mainās, ja atņem vairāk?"

MERKIS = ("Šodien veidosim piemērus, atņemot no viena skaitļa dažādus "
          "skaitļus, un spriedīsim par izmaiņām.")

_VIRKNE = restis([["15 − 5", 10], ["15 − 6", 9], ["15 − 7", 8],
                  ["15 − 8", None]])

SATURS = [
    Sakums("15 − 5, 15 − 6, 15 − 7 - ko tu pamani?",
           zimejums=_VIRKNE,
           paraksts="Atņem par 1 vairāk - paliek par 1 mazāk.",
           fakti=["Pirmais skaitlis nemainās.",
                  "Atņemamais aug.",
                  "Starpība samazinās."]),

    Doma("Vairāk prom - mazāk paliek",
         "Par cik palielina atņemamo, par tik samazinās starpība.",
         soli=[
             "Salīdzini atņemamos.",
             "Par cik tie atšķiras?",
             "Par tik atšķiras starpības - otrādi.",
         ]),

    Ievadi("Paredzi", [
        {"jaut": "Kas ir «?»", "zim": _VIRKNE, "atb": ["7"],
         "padoms": "8 − 1."},
        {"jaut": "18 − 8 = 10. Cik ir 18 − 9?", "atb": ["9"],
         "padoms": "Par 1 mazāk."},
        {"jaut": "16 − 6 = 10. Cik ir 16 − 8?", "atb": ["8"],
         "padoms": "Par 2 mazāk."},
        {"jaut": "14 − 4 = 10. Cik ir 14 − 3?", "atb": ["11"],
         "padoms": "Atņem mazāk - paliek vairāk."},
    ]),

    Varianti("Kā mainās?", [
        {"jaut": "13 − 3 un 13 − 5. Kur paliek vairāk?",
         "opcijas": ["13 − 3", "13 − 5"], "jaukt": False, "pareizi": 0,
         "padoms": "Mazāk atņem - vairāk paliek."},
    ]),

    Pasaule("Cepumi kastē",
            Ievadi("", [
                {"jaut": "Kastē 17 cepumu. Ja apēd 7, paliek 10. Cik paliek, "
                         "ja apēd 9?", "atb": ["8"], "padoms": "Par 2 mazāk."},
            ]),
            pavediens="virtuve",
            konteksts="Cepumu kastē vienmēr tas pats skaits.",
            kapec="Vari paredzēt, nepārrēķinot."),

    Kopsavilkums([
        "Veidoju piemērus ar vienu sākuma skaitli.",
        "Pamanu: vairāk atņem - mazāk paliek.",
        "Paredzu rezultātu.",
    ]),

    Majas([
        "Uzraksti virkni 20 − 1, 20 − 2, ... 20 − 9.",
        "Ko pamani?",
        "Izskaidro mājiniekam.",
    ]),
]
