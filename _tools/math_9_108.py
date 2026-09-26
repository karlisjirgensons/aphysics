# -*- coding: utf-8 -*-
"""9. klase, 108. stunda: «Kas ir vienādojumu sistēma?»

Divi vienādojumi, kuriem jāizpildās VIENLAIKUS. Katram ir bezgalīgi daudz
atrisinājumu, bet kopīgs parasti tikai viens pāris - divu taisnu
krustpunkts. Figūriekava sistēmas pierakstā nozīmē «un».
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, paris, plakne, restis)

TEMA = "Kas ir vienādojumu sistēma?"

MERKIS = ("Skaidrosim, ka sistēmas atrisinājums ir abu vienādojumu "
          "kopīgais atrisinājums.")

_T = "text"

SATURS = [
    Sakums("Divi fakti - viens pāris",
           zimejums=restis([["x + y = 7", "(1; 6)", "(2; 5)", "(3; 4)",
                             "(4; 3)"],
                            ["x − y = 1", "(2; 1)", "(3; 2)", "(4; 3)",
                             "(5; 4)"]]),
           paraksts="Abās rindās ir tikai (4; 3).",
           fakti=["Katram vienādojumam - daudz pāru.",
                  "Sistēmai - tikai kopīgie.",
                  "Te kopīgs ir viens: x = 4, y = 3."]),

    Doma("Vienādojumu sistēma",
         "Sistēmas atrisinājums ir skaitļu pāris, kas ir atrisinājums katram "
         "sistēmas vienādojumam.",
         soli=[
             "Sistēmu raksta ar figūriekavu - «un».",
             "Pāris der, ja pārbaude izdodas ABOS vienādojumos.",
             "Grafiski - taisnu krustpunkts.",
             "Atrisināt sistēmu - atrast visus kopīgos pārus.",
         ]),

    Paraugs("Pārbaude",
            uzd="Vai (2; −1) ir sistēmas 3x + y = 5 un x − 2y = 4 "
                "atrisinājums?",
            soli=[
                ("3 · 2 + (−1) = 5 ✔", "Pirmais vienādojums."),
                ("2 − 2 · (−1) = 4 ✔", "Otrais vienādojums."),
            ],
            atbilde="jā - der abos"),

    Varianti("Sistēmas atrisinājums?", [
        {"jaut": "(3; 1) sistēmai x + y = 4, x − y = 2",
         "opcijas": ["Jā", "Nē"], "jaukt": False,
         "pareizi": 0, "padoms": "4 = 4 un 2 = 2."},
        {"jaut": "(1; 3) sistēmai x + y = 4, x − y = 2",
         "opcijas": ["Jā", "Nē"], "jaukt": False,
         "pareizi": 1, "padoms": "Otrajā: −2 ≠ 2."},
        {"jaut": "(0; 5) sistēmai 2x + y = 5, y = 5",
         "opcijas": ["Jā", "Nē"], "jaukt": False,
         "pareizi": 0, "padoms": "5 = 5 abos."},
    ]),

    Ievadi("Atrodi kopīgo pāri", [
        {"jaut": "x + y = 10 un x − y = 2", "atb": paris(6, 4),
         "tastatura": _T, "vieta": "(x; y)", "padoms": "6 + 4, 6 − 4."},
        {"jaut": "x + y = 5 un y = 2x − 1", "atb": paris(2, 3),
         "tastatura": _T, "vieta": "(x; y)", "padoms": "Izmēģini x = 2."},
        {"jaut": "x = 3 un x + 2y = 11", "atb": paris(3, 4),
         "tastatura": _T, "vieta": "(x; y)", "padoms": "3 + 2y = 11."},
    ]),

    Pasaule("Dzimšanas dienas konfektes",
            Ievadi("", [
                {"jaut": "Maisiņā 20 konfektes: šokolādes x un karameles y; "
                         "šokolādes par 6 vairāk. x + y = 20, x − y = 6. "
                         "Cik šokolādes?", "atb": ["13"],
                 "padoms": "13 + 7 = 20, 13 − 7 = 6."},
                {"jaut": "Cik karameļu?", "atb": ["7"], "padoms": "20 − 13."},
            ]),
            pavediens="virtuve",
            konteksts="Divi fakti par vienu maisiņu - tā ir sistēma.",
            kapec="Tikai viens pāris der abiem faktiem.",
            zimejums=plakne(grafiki=[(-1, 20, "x + y = 20"),
                                     (1, -6, "x − y = 6")],
                            punkti=[(13, 7, "(13; 7)")],
                            no_x=0, lidz_x=20, no_y=0, lidz_y=20, solis=2,
                            solis_y=2)),

    Kopsavilkums([
        "Zinu, ka sistēmas atrisinājums der visos vienādojumos.",
        "Pārbaudu pāri abos vienādojumos.",
        "Atrodu kopīgo pāri vienkāršā sistēmā.",
    ]),

    Majas([
        "Pārbaudi, vai (5; 2) ir sistēmas 2x − 3y = 4, x + y = 7 atrisinājums.",
        "Izdomā sistēmu ar atrisinājumu (1; −2).",
        "Uzraksti sistēmu par savu ģimeni (vecumi, skaiti).",
    ]),
]
