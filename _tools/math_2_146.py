# -*- coding: utf-8 -*-
"""2. klase, 146. stunda: «Kā skaitīt pa 5?»

Skaitīšana pa 5: 5, 10, 15 ... 50 - pirkstu skaitīšana uz rokām un
pulksteņa minūtes. Simta kvadrātā tās ir divas kolonnas. Lēcienu skaits dod
reizinātāju: 7 lēcieni - 7 · 5 = 35.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, laiks, pulkstenis, simta_kvadrats)

TEMA = "Kā skaitīt pa 5?"

MERKIS = ("Šodien skaitīsim pa 5 uz priekšu un izmantosim to reizinājumu "
          "iegūšanai.")

SATURS = [
    Sakums("Cik pirkstu ir 6 bērniem uz rokām?",
           zimejums=simta_kvadrats(1, 60, izcelt=list(range(5, 61, 5))),
           paraksts="Pa 5 - divas kolonnas.",
           fakti=["Katrai rokai 5 pirksti.",
                  "Skaiti pa 5: 5, 10, 15 ...",
                  "Pulkstenī arī minūtes skaita pa 5!"]),

    Doma("Pa 5",
         "Skaitot pa 5, skaitļi beidzas ar 5 vai 0.",
         soli=[
             "Sāc no 5.",
             "Pieskaiti 5: 10, 15, 20 ...",
             "Skaiti lēcienus.",
             "8 lēcieni - 40, jo 8 · 5 = 40.",
         ]),

    Ievadi("Pa 5", [
        {"jaut": "5, 10, 15, 20, ...", "atb": ["25"], "padoms": "+5."},
        {"jaut": "30, 35, 40, ...", "atb": ["45"], "padoms": "+5."},
        {"jaut": "6 lēcieni pa 5 - kur?", "atb": ["30"], "padoms": "6 · 5."},
        {"jaut": "Cik minūšu, ja lielais rādītājs pie 7?", "atb": ["35"],
         "zim": pulkstenis(12, 35), "padoms": "7 · 5."},
        {"jaut": "Atpakaļ: 50, 45, 40, ...", "atb": ["35"], "padoms": "−5."},
        {"jaut": "9 lēcieni pa 5?", "atb": ["45"], "padoms": "9 · 5."},
    ], pamats=4),

    Varianti("Vai pa 5?", [
        {"jaut": "Vai 42 ir virknē pa 5?", "opcijas": ["Nē", "Jā"],
         "jaukt": False, "pareizi": 0, "padoms": "Beidzas ar 2."},
        {"jaut": "Vai 55 ir virknē pa 5?", "opcijas": ["Jā", "Nē"],
         "jaukt": False, "pareizi": 0, "padoms": "Beidzas ar 5."},
    ]),

    Pasaule("Pulkstenis un minūtes",
            Ievadi("", [
                {"jaut": "Cik ir pulkstenis?", "zim": pulkstenis(4, 40),
                 "atb": laiks(4, 40), "padoms": "Lielais pie 8: 8 · 5."},
                {"jaut": "Cik minūšu līdz pieciem?", "atb": ["20"],
                 "padoms": "Pie 12 - 4 iedaļas pa 5."},
            ]),
            pavediens="skola",
            konteksts="Pulksteņa lielais rādītājs skaita pa 5 minūtēm.",
            kapec="Pa 5 - ātrāk nolasīt laiku."),

    Kopsavilkums([
        "Skaitu pa 5 uz priekšu un atpakaļ.",
        "Iegūstu reizinājumus ar 5.",
        "Lasu minūtes pa 5.",
    ]),

    Majas([
        "Skaiti ģimenes pirkstus pa 5.",
        "Nolasi laiku pulkstenī 3 reizes, skaitot pa 5.",
        "Uzraksti virkni pa 5 līdz 100.",
    ]),
]
