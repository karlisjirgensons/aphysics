# -*- coding: utf-8 -*-
"""2. klase, 5. stunda: «Kuri skaitļi der šai grupai?»

Grupēšana pāriet uz skaitļiem. Pazīmes ir tās, ko redz pierakstā (pēdējais
cipars, ciparu skaits) un ko saka salīdzinājums (mazāks nekā 20). Simta
kvadrātā grupa kļūst redzama kā raksts - kolonna vai rinda.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, simta_kvadrats)

TEMA = "Kuri skaitļi der šai grupai?"

MERKIS = ("Šodien atlasīsim skaitļus pēc pazīmes: pēc pēdējā cipara, pēc "
          "ciparu skaita un pēc lieluma.")

SATURS = [
    Sakums("Kuri skaitļi slēpjas vienā kolonnā?",
           zimejums=simta_kvadrats(1, 50, izcelt=[5, 15, 25, 35, 45]),
           paraksts="Visi iekrāsotie beidzas ar 5.",
           fakti=["Skaitļiem arī ir pazīmes - tāpat kā priekšmetiem.",
                  "Simta kvadrātā viena kolonna - viens pēdējais cipars."]),

    Doma("Skaitļa pazīmes",
         "Pazīmi var nolasīt no cipariem vai pateikt ar salīdzinājumu.",
         soli=[
             "Pēdējais cipars: beidzas ar 5, beidzas ar 0.",
             "Ciparu skaits: viencipara (0-9) vai divciparu (10-99).",
             "Lielums: mazāks nekā 20, lielāks nekā 50.",
             "Skaitlis der grupai, ja tam ir grupas pazīme.",
         ]),

    Slidnis("Grupas simta kvadrātā", [
        {"v": "beidzas ar 5", "teksts": "Viena kolonna.",
         "zim": simta_kvadrats(1, 50, izcelt=[5, 15, 25, 35, 45])},
        {"v": "viencipara", "teksts": "Pirmās rindas sākums: 1-9.",
         "zim": simta_kvadrats(1, 50, izcelt=list(range(1, 10)))},
        {"v": "mazāki nekā 20", "teksts": "Divas pirmās rindas bez 20.",
         "zim": simta_kvadrats(1, 50, izcelt=list(range(1, 20)))},
        {"v": "sākas ar 3", "teksts": "Rinda no 30 līdz 39.",
         "zim": simta_kvadrats(1, 50, izcelt=list(range(30, 40)))},
    ], ievads="Katrai pazīmei - savs raksts."),

    Ievadi("Cik der?", [
        {"jaut": "Cik skaitļu beidzas ar 5: 15, 52, 45, 5, 50, 95?",
         "atb": ["4"], "padoms": "15, 45, 5, 95."},
        {"jaut": "Cik viencipara skaitļu: 7, 17, 3, 30, 9, 90?",
         "atb": ["3"], "padoms": "7, 3, 9."},
        {"jaut": "Cik skaitļu ir mazāki nekā 20: 19, 21, 12, 20, 2?",
         "atb": ["3"], "padoms": "20 nav mazāks nekā 20."},
        {"jaut": "Cik divciparu skaitļu beidzas ar 0 līdz 100 (bez 100)?",
         "atb": ["9"], "padoms": "10, 20, ..., 90."},
        {"jaut": "Kurš ir lielākais divciparu skaitlis, kas beidzas ar 5?",
         "atb": ["95"], "padoms": "Iedomājies kolonnu līdz 100."},
        {"jaut": "Kurš ir mazākais divciparu skaitlis?", "atb": ["10"],
         "padoms": "9 vēl ir viencipara."},
    ], pamats=4),

    Varianti("Kura pazīme der visiem?", [
        {"jaut": "Grupa: 30, 31, 35, 38.",
         "opcijas": ["sākas ar 3", "beidzas ar 5", "viencipara"],
         "pareizi": 0, "padoms": "Paskaties pirmo ciparu."},
        {"jaut": "Grupa: 4, 14, 44, 94.",
         "opcijas": ["beidzas ar 4", "mazāki nekā 20", "sākas ar 4"],
         "pareizi": 0, "padoms": "94 nav mazāks nekā 20."},
    ]),

    Pasaule("Kuras mājas ir ielas vienā pusē?",
            Varianti("", [
                {"jaut": "Pastniece nes vēstules mājām 3, 8, 15, 22, 27. "
                         "Kuras ir ielas kreisajā pusē?",
                 "opcijas": ["3, 15, 27", "8, 22", "3, 8, 15"],
                 "pareizi": 0, "padoms": "Kreisajā pusē: 1, 3, 5, 7..."},
                {"jaut": "Kura māja ir labajā pusē?",
                 "opcijas": ["22", "15", "27"], "pareizi": 0,
                 "padoms": "Labajā pusē: 2, 4, 6..."},
            ]),
            pavediens="maja",
            konteksts="Ielas kreisajā pusē mājām ir numuri 1, 3, 5, 7..., "
                      "labajā - 2, 4, 6, 8...",
            kapec="Pēc numura pazīmes pastniece zina, uz kuru pusi iet."),

    Kopsavilkums([
        "Atlasu skaitļus pēc pēdējā cipara.",
        "Atšķiru viencipara un divciparu skaitļus.",
        "Atlasu skaitļus, kas mazāki vai lielāki nekā dotais.",
    ]),

    Majas([
        "Atrodi 5 numurus uz mājām, mašīnām vai grāmatām.",
        "Sadali tos: viencipara un divciparu.",
        "Kuriem numuriem ir kopīgs pēdējais cipars?",
    ]),
]
