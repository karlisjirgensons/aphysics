# -*- coding: utf-8 -*-
"""2. klase, 117. stunda: «Kurus skaitļus var salikt no diviem vienādiem?»

Reizināšanas ar 2 sākums: skaitļus no 2 līdz 20 pieraksta kā divu skaitļu
summu un izceļ tos, kurus var uzrakstīt kā divu vienādu skaitļu summu -
dubultus. Tie ir 2, 4, 6 ... 20, un tieši tos vēlāk sauks par pāra
skaitļiem.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, bildes, simta_kvadrats)

TEMA = "Kurus skaitļus var salikt no diviem vienādiem?"

MERKIS = ("Šodien pierakstīsim skaitļus no 2 līdz 20 kā divu skaitļu summu "
          "un izcelsim vienādu skaitļu summas.")

SATURS = [
    Sakums("Kāpēc zeķes pērk pa pāriem, bet 7 zeķes pāros nesadalās?",
           zimejums=bildes([[("ripina", 4)], [("ripina", 3)]]),
           paraksts="7 = 4 + 3 - nav divu vienādu.",
           fakti=["8 = 4 + 4 - divi vienādi.",
                  "7 nevar uzrakstīt kā divus vienādus.",
                  "Dubulti: 1 + 1, 2 + 2, 3 + 3 ..."]),

    Doma("Dubulti",
         "Skaitlis, ko var uzrakstīt kā divu vienādu skaitļu summu, ir "
         "dubults.",
         soli=[
             "Sadali skaitli divās kaudzītēs.",
             "Ja kaudzītes vienādas - tas ir dubults.",
             "Dubulti līdz 20: 2, 4, 6, 8, 10, 12, 14, 16, 18, 20.",
             "Tie ir katrs otrais skaitlis.",
         ]),

    Slidnis("Dubultu virkne", [
        {"v": "1 + 1 = 2", "teksts": "Mazākais dubults.", "zim": bildes([["ripina"],
                                                         ["ripina"]])},
        {"v": "3 + 3 = 6", "teksts": "Divas rindas pa 3.",
         "zim": bildes([[("ripina", 3)], [("ripina", 3)]])},
        {"v": "6 + 6 = 12", "teksts": "Divas rindas pa 6.",
         "zim": bildes([[("ripina", 6)], [("ripina", 6)]])},
        {"v": "10 + 10 = 20", "teksts": "Lielākais dubults līdz 20.",
         "zim": bildes([[("ripina", 10)], [("ripina", 10)]])},
    ]),

    Ievadi("Dubulti", [
        {"jaut": "7 + 7 = ?", "atb": ["14"], "padoms": "7 + 3 + 4."},
        {"jaut": "? + ? = 16 (abi vienādi)", "atb": ["8"],
         "padoms": "8 + 8."},
        {"jaut": "9 + 9 = ?", "atb": ["18"], "padoms": "9 + 1 + 8."},
        {"jaut": "? + ? = 10 (abi vienādi)", "atb": ["5"],
         "padoms": "5 + 5."},
        {"jaut": "? + ? = 20 (abi vienādi)", "atb": ["10"],
         "padoms": "10 + 10."},
        {"jaut": "Cik dubultu ir no 2 līdz 20?", "atb": ["10"],
         "padoms": "2, 4, 6 ... 20.",
         "zim": simta_kvadrats(1, 20, izcelt=list(range(2, 21, 2)))},
    ], pamats=4),

    Varianti("Vai tas ir dubults?", [
        {"jaut": "12", "opcijas": ["Jā, 6 + 6", "Nē"], "jaukt": False,
         "pareizi": 0, "padoms": "Sadali uz pusēm."},
        {"jaut": "15", "opcijas": ["Jā", "Nē, 7 + 8"], "jaukt": False,
         "pareizi": 1, "padoms": "7 + 7 = 14, 8 + 8 = 16."},
        {"jaut": "18", "opcijas": ["Jā, 9 + 9", "Nē"], "jaukt": False,
         "pareizi": 0, "padoms": "9 + 9."},
        {"jaut": "11", "opcijas": ["Jā", "Nē, 5 + 6"], "jaukt": False,
         "pareizi": 1, "padoms": "5 + 5 = 10, 6 + 6 = 12."},
    ]),

    Pasaule("Zeķu pāri veļasgrozā",
            Ievadi("", [
                {"jaut": "Pēc mazgāšanas ir 14 zeķes. Cik pāru?", "atb": ["7"],
                 "padoms": "7 + 7 = 14."},
                {"jaut": "Vēl atrada 1 zeķi. Cik zeķu paliks bez pāra?",
                 "atb": ["1"], "padoms": "15 = 7 + 7 + 1."},
            ]),
            pavediens="maja",
            konteksts="Pēc veļas mazgāšanas zeķes jāsaliek pa pāriem.",
            kapec="Dubulti - pāri, kas sanāk bez atlikuma."),

    Kopsavilkums([
        "Pierakstu skaitli kā divu skaitļu summu.",
        "Atrodu dubultus - divu vienādu skaitļu summas.",
        "Zinu dubultus līdz 20.",
    ]),

    Majas([
        "Saskaiti mājās apavus pa pāriem.",
        "Vai kāds palika bez pāra?",
        "Uzraksti visus dubultus no 2 līdz 20.",
    ]),
]
