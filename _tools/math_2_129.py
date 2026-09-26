# -*- coding: utf-8 -*-
"""2. klase, 129. stunda: «Kuri skaitļi dalās ar 2?»

Pāra skaitļi dalās ar 2 bez atlikuma un beidzas ar 0, 2, 4, 6, 8; nepāra -
ar 1, 3, 5, 7, 9. Simta kvadrātā pāra skaitļi ir piecas kolonnas pārmaiņus -
tas ir tas pats raksts, ko 2.1. tematā redzēja mājas numuros.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, simta_kvadrats)

TEMA = "Kuri skaitļi dalās ar 2?"

MERKIS = ("Šodien nosauksim pāra un nepāra skaitļus un raksturosim to vietu "
          "simta kvadrātā.")

_PARA = ["pāra", "nepāra"]

SATURS = [
    Sakums("Kāpēc ielas vienā pusē ir tikai pāra numuri?",
           zimejums=simta_kvadrats(1, 50, izcelt=list(range(2, 51, 2))),
           paraksts="Pāra skaitļi - katra otrā kolonna.",
           fakti=["Pāra skaitlis dalās ar 2 bez atlikuma.",
                  "Tas beidzas ar 0, 2, 4, 6 vai 8.",
                  "Pārējie ir nepāra skaitļi."]),

    Doma("Pāra un nepāra",
         "Pāra skaitli var sadalīt divās vienādās daļās, nepāra - nevar.",
         soli=[
             "Paskaties uz pēdējo ciparu.",
             "0, 2, 4, 6, 8 - pāra skaitlis.",
             "1, 3, 5, 7, 9 - nepāra skaitlis.",
             "Simta kvadrātā - kolonnas pārmaiņus.",
         ]),

    Varianti("Pāra vai nepāra?", [
        {"jaut": "34", "opcijas": _PARA, "jaukt": False, "pareizi": 0,
         "padoms": "Beidzas ar 4."},
        {"jaut": "57", "opcijas": _PARA, "jaukt": False, "pareizi": 1,
         "padoms": "Beidzas ar 7."},
        {"jaut": "90", "opcijas": _PARA, "jaukt": False, "pareizi": 0,
         "padoms": "Beidzas ar 0."},
        {"jaut": "71", "opcijas": _PARA, "jaukt": False, "pareizi": 1,
         "padoms": "Beidzas ar 1."},
        {"jaut": "0", "opcijas": _PARA, "jaukt": False, "pareizi": 0,
         "padoms": "0 : 2 = 0 bez atlikuma."},
        {"jaut": "99", "opcijas": _PARA, "jaukt": False, "pareizi": 1,
         "padoms": "Beidzas ar 9."},
    ], pamats=4),

    Ievadi("Saskaiti", [
        {"jaut": "Cik pāra skaitļu no 1 līdz 20?", "atb": ["10"],
         "padoms": "2, 4 ... 20.",
         "zim": simta_kvadrats(1, 20, izcelt=list(range(2, 21, 2)))},
        {"jaut": "Kurš ir lielākais divciparu pāra skaitlis?", "atb": ["98"],
         "padoms": "99 ir nepāra."},
        {"jaut": "Kurš ir mazākais divciparu nepāra skaitlis?",
         "atb": ["11"], "padoms": "10 ir pāra."},
        {"jaut": "Nākamais pāra skaitlis pēc 46?", "atb": ["48"],
         "padoms": "+ 2."},
    ]),

    Pasaule("Mājas numurs",
            Varianti("", [
                {"jaut": "Tavas mājas numurs ir 37. Kurā ielas pusē tā ir, "
                         "ja pāra numuri ir labajā pusē?",
                 "opcijas": ["kreisajā", "labajā"], "jaukt": False,
                 "pareizi": 0, "padoms": "37 ir nepāra."},
                {"jaut": "Kurš būs kaimiņš tajā pašā pusē?",
                 "opcijas": ["35 vai 39", "36 vai 38", "38"],
                 "pareizi": 0, "padoms": "Arī nepāra: ± 2."},
            ]),
            pavediens="maja",
            konteksts="Latvijā ielas vienā pusē ir pāra, otrā - nepāra "
                      "numuri.",
            kapec="Pēc numura uzreiz zina, uz kuru pusi iet."),

    Kopsavilkums([
        "Atšķiru pāra un nepāra skaitļus pēc pēdējā cipara.",
        "Zinu, ka pāra skaitļi dalās ar 2.",
        "Redzu to rakstu simta kvadrātā.",
    ]),

    Majas([
        "Paskaties uz māju numuriem savā ielā.",
        "Vai vienā pusē ir tikai pāra numuri?",
        "Uzraksti 5 pāra un 5 nepāra skaitļus līdz 100.",
    ]),
]
