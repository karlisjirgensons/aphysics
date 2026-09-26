# -*- coding: utf-8 -*-
"""2. klase, 130. stunda: «Kas notiek, skaitot pa 2?»

Skaitot pa 2 no pāra skaitļa, visi ir pāra; no nepāra - visi nepāra.
Virkni var skaitīt arī atpakaļ. Tas ir tas pats «+2» lēciens uz skaitļu
taisnes.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Kustiba, Majas, Pasaule,
                         Sakums, Varianti, taisne)

TEMA = "Kas notiek, skaitot pa 2?"

MERKIS = ("Šodien skaitīsim pa 2 uz priekšu un atpakaļ, sākot no jebkura "
          "skaitļa, un veidosim virkni.")

SATURS = [
    Sakums("Varde lec pa 2 no 3. Vai tā kādreiz nonāks uz 10?",
           zimejums=taisne(0, 14, 1, bultas=[(3, 5, "+2"), (5, 7, "+2"),
                                              (7, 9, "+2"), (9, 11, "+2")]),
           paraksts="3, 5, 7, 9, 11 - visi nepāra.",
           fakti=["No nepāra skaitļa pa 2 - tikai nepāra.",
                  "10 ir pāra - varde to pārlēks.",
                  "No pāra skaitļa pa 2 - tikai pāra."]),

    Doma("Virkne pa 2",
         "Skaitot pa 2, paritāte nemainās: pāra paliek pāra.",
         soli=[
             "Sāc no dotā skaitļa.",
             "Uz priekšu - pieskaiti 2, atpakaļ - atņem 2.",
             "Vieni mainās: 1, 3, 5, 7, 9 vai 0, 2, 4, 6, 8.",
             "Desmits mainās, kad vieni pārlec pāri 9.",
         ]),

    Ievadi("Turpini virkni", [
        {"jaut": "31, 33, 35, 37, ...", "atb": ["39"], "padoms": "+2."},
        {"jaut": "48, 50, 52, 54, ...", "atb": ["56"], "padoms": "+2."},
        {"jaut": "Atpakaļ: 70, 68, 66, ...", "atb": ["64"], "padoms": "−2."},
        {"jaut": "Atpakaļ: 23, 21, 19, ...", "atb": ["17"], "padoms": "−2."},
        {"jaut": "87, 89, 91, ...", "atb": ["93"], "padoms": "Pāri 90."},
        {"jaut": "Atpakaļ: 102, 100, 98, ...", "atb": ["96"],
         "padoms": "−2."},
    ], pamats=4),

    Kustiba("Varde lec pa 2", [
        {"jaut": "Varde sāk pie 4 un lec 5 reizes pa 2. Kur tā būs?",
         "atb": 14, "beigas": 20, "iedala": 2, "objekts": "varde",
         "merkis": "5 lēcieni", "padoms": "6, 8, 10, 12, 14."},
        {"jaut": "Varde sāk pie 19 un lec 4 reizes atpakaļ pa 2. Kur?",
         "atb": 11, "beigas": 20, "iedala": 2, "objekts": "varde",
         "merkis": "4 lēcieni", "padoms": "17, 15, 13, 11."},
    ]),

    Varianti("Vai būs virknē?", [
        {"jaut": "Virkne 1, 3, 5 ... Vai tajā būs 20?",
         "opcijas": ["Nē - 20 ir pāra", "Jā"], "jaukt": False,
         "pareizi": 0, "padoms": "Visi nepāra."},
        {"jaut": "Virkne 2, 4, 6 ... Vai tajā būs 50?",
         "opcijas": ["Jā - 50 ir pāra", "Nē"], "jaukt": False,
         "pareizi": 0, "padoms": "Visi pāra."},
    ]),

    Pasaule("Kāpnes uz torni",
            Ievadi("", [
                {"jaut": "Kāp pa 2 pakāpieniem. Pēc 10 soļiem esi uz kura "
                         "pakāpiena?", "atb": ["20"],
                 "padoms": "2, 4 ... 20."},
                {"jaut": "Tornī 30 pakāpienu. Cik soļu pa 2 vēl?", "atb": ["5"],
                 "padoms": "22, 24, 26, 28, 30."},
            ]),
            pavediens="sports",
            konteksts="Uz skatu torni kāpj pa diviem pakāpieniem.",
            kapec="Pa 2 - ātrāk nekā pa vienam."),

    Kopsavilkums([
        "Skaitu pa 2 uz priekšu un atpakaļ.",
        "Zinu, ka pa 2 pāra paliek pāra, nepāra - nepāra.",
        "Turpinu virkni no jebkura skaitļa.",
    ]),

    Majas([
        "Skaiti pa 2 no 1 līdz 31 skaļi.",
        "Skaiti pa 2 atpakaļ no 40 līdz 20.",
        "Kāp pa kāpnēm pa 2 pakāpieniem un skaiti.",
    ]),
]
