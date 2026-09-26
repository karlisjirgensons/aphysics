# -*- coding: utf-8 -*-
"""2. klase, 32. stunda: «Kā saskaitīt pa desmitiem?»

Divciparu skaitlis ir desmiti un vieni: 47 = 10 + 10 + 10 + 10 + 5 + 1 + 1.
Skaitot pa 10 un pa 5 saskaita naudu - 10 centu un 5 centu monētas. Te
sākas pāreja no 20 uz 100.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, desmiti, monetas)

TEMA = "Kā saskaitīt pa desmitiem?"

MERKIS = ("Šodien saskaitīsim, skaitot pa 10 un pa 5, un izmantosim to, "
          "rēķinot naudu.")

SATURS = [
    Sakums("Cik centu ir makā?",
           zimejums=monetas(["10 c", "10 c", "10 c", "10 c", "5 c", "1 c",
                             "1 c"]),
           paraksts="10, 20, 30, 40, 45, 46, 47.",
           fakti=["Vispirms skaiti lielās monētas.",
                  "Pa 10: 10, 20, 30, 40.",
                  "Tad pa 5 un pa 1: 45, 46, 47."]),

    Doma("Desmiti un vieni",
         "Divciparu skaitļa pirmais cipars pasaka desmitus, otrais - vienus.",
         soli=[
             "47 = 4 desmiti un 7 vieni.",
             "Pieskaitot 10, mainās tikai desmiti: 47 + 10 = 57.",
             "Pieskaitot 20, desmiti palielinās par 2: 47 + 20 = 67.",
             "Vieni paliek tie paši.",
         ]),

    Slidnis("Pa desmitiem uz augšu", [
        {"v": "23", "teksts": "2 desmiti un 3 vieni.",
         "zim": desmiti(2, 3)},
        {"v": "33", "teksts": "+10 - vēl viens stienis.",
         "zim": desmiti(3, 3)},
        {"v": "43", "teksts": "+10.", "zim": desmiti(4, 3)},
        {"v": "53", "teksts": "+10 - vieni nemainās.",
         "zim": desmiti(5, 3)},
    ]),

    Ievadi("Pa desmitiem", [
        {"jaut": "36 + 10 = ?", "atb": ["46"], "padoms": "Desmiti +1."},
        {"jaut": "52 + 30 = ?", "atb": ["82"], "padoms": "5 + 3 desmiti."},
        {"jaut": "78 − 20 = ?", "atb": ["58"], "padoms": "7 − 2 desmiti."},
        {"jaut": "Cik ir?", "zim": desmiti(6, 4), "atb": ["64"],
         "padoms": "Stieņi - desmiti, kubiņi - vieni."},
        {"jaut": "45 + 40 = ?", "atb": ["85"], "padoms": "4 + 4 desmiti."},
        {"jaut": "91 − 50 = ?", "atb": ["41"], "padoms": "9 − 5 desmiti."},
    ], pamats=4),

    Ievadi("Saskaiti naudu", [
        {"jaut": "Cik centu?", "zim": monetas(["10 c", "10 c", "10 c",
                                               "5 c", "1 c"]),
         "atb": ["36"], "mers": "c", "padoms": "30 + 5 + 1."},
        {"jaut": "Cik centu?", "zim": monetas(["20 c", "20 c", "10 c",
                                               "5 c", "2 c"]),
         "atb": ["57"], "mers": "c", "padoms": "20, 40, 50, 55, 57."},
    ]),

    Varianti("Kā izskatās skaitlis?", [
        {"jaut": "Kurā skaitlī ir 7 desmiti un 2 vieni?",
         "opcijas": ["72", "27", "79"], "pareizi": 0,
         "padoms": "Desmiti pirmajā vietā."},
        {"jaut": "Kas ir 58 − 10?", "opcijas": ["48", "57", "68"],
         "pareizi": 0, "padoms": "Viens desmits mazāk."},
    ]),

    Pasaule("Vai pietiks saldējumam?",
            Varianti("", [
                {"jaut": "Makā: 10 c, 10 c, 10 c, 10 c, 5 c. Saldējums maksā "
                         "50 c. Vai pietiks?",
                 "opcijas": ["Nē, ir 45 c", "Jā, ir 50 c"], "jaukt": False,
                 "pareizi": 0, "padoms": "10, 20, 30, 40, 45."},
                {"jaut": "Cik vēl vajag?", "opcijas": ["5 c", "10 c",
                                                        "1 c"],
                 "pareizi": 0, "padoms": "50 − 45."},
            ]),
            pavediens="veikals",
            konteksts="Ēdnīcā saldējums maksā 50 centu.",
            kapec="Skaitot pa 10, naudu saskaita ātri."),

    Kopsavilkums([
        "Saskaitu, skaitot pa 10 un pa 5.",
        "Zinu, ka divciparu skaitlis ir desmiti un vieni.",
        "Pieskaitu un atņemu veselus desmitus.",
    ]),

    Majas([
        "Saskaiti monētas makā vai krājkasītē, skaitot pa 10 un pa 5.",
        "Pieraksti summu.",
        "Cik pietrūkst līdz 1 € (100 c)?",
    ]),
]
