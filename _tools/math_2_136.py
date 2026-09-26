# -*- coding: utf-8 -*-
"""2. klase, 136. stunda: «Kurus skaitļus var salikt no trim vienādiem?»

Tas pats, kas ar dubultiem, tikai trīs saskaitāmie: 3 = 1 + 1 + 1,
6 = 2 + 2 + 2, 9 = 3 + 3 + 3 ... Skaitļi, ko var salikt no trim vienādiem,
ir reizinājumi ar 3. Ne katru skaitli tā var - 10 nevar.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, bildes)

TEMA = "Kurus skaitļus var salikt no trim vienādiem?"

MERKIS = ("Šodien meklēsim skaitļus, ko var uzrakstīt kā trīs vienādu "
          "skaitļu summu.")

SATURS = [
    Sakums("Vai 12 konfektes var sadalīt 3 draugiem vienādi? Un 10?",
           zimejums=bildes([[("ripina", 4)], [("ripina", 4)],
                            [("ripina", 4)]]),
           paraksts="12 = 4 + 4 + 4.",
           fakti=["12 var: pa 4 katram.",
                  "10 nevar: 3 + 3 + 3 = 9, 4 + 4 + 4 = 12.",
                  "Trīs vienādi: 3, 6, 9, 12, 15 ..."]),

    Doma("Trīs vienādi saskaitāmie",
         "Skaitlis der, ja to var sadalīt trīs vienādās kaudzītēs bez "
         "atlikuma.",
         soli=[
             "Liec pa vienam pārmaiņus trīs kaudzītēs.",
             "Ja beigās kaudzītes vienādas - der.",
             "Pieraksti: 12 = 4 + 4 + 4.",
             "Tādi skaitļi: 3, 6, 9, 12, 15, 18, 21 ...",
         ]),

    Ievadi("Atrodi saskaitāmo", [
        {"jaut": "? + ? + ? = 9 (visi vienādi)", "atb": ["3"],
         "padoms": "3 + 3 + 3."},
        {"jaut": "? + ? + ? = 15", "atb": ["5"], "padoms": "5 + 5 + 5."},
        {"jaut": "? + ? + ? = 21", "atb": ["7"], "padoms": "7 + 7 + 7."},
        {"jaut": "? + ? + ? = 30", "atb": ["10"], "padoms": "10 + 10 + 10."},
        {"jaut": "6 + 6 + 6 = ?", "atb": ["18"], "padoms": "12 + 6."},
        {"jaut": "8 + 8 + 8 = ?", "atb": ["24"], "padoms": "16 + 8."},
    ], pamats=4),

    Varianti("Der vai neder?", [
        {"jaut": "Vai 14 ir trīs vienādu skaitļu summa?",
         "opcijas": ["Nē", "Jā"], "jaukt": False, "pareizi": 0,
         "padoms": "4 + 4 + 4 = 12, 5 + 5 + 5 = 15."},
        {"jaut": "Vai 18 ir trīs vienādu skaitļu summa?",
         "opcijas": ["Jā, 6 + 6 + 6", "Nē"], "jaukt": False, "pareizi": 0,
         "padoms": "6 + 6 + 6."},
        {"jaut": "Kurš skaitlis der?", "opcijas": ["27", "25", "26"],
         "pareizi": 0, "padoms": "9 + 9 + 9."},
        {"jaut": "Kurš skaitlis neder?", "opcijas": ["20", "21", "24"],
         "pareizi": 0, "padoms": "6 + 6 + 6 = 18, 7 + 7 + 7 = 21."},
    ]),

    Pasaule("Trīsriteņi",
            Ievadi("", [
                {"jaut": "Parkā trīsriteņiem kopā 15 riteņi. Cik trīsriteņu?",
                 "atb": ["5"], "padoms": "5 + 5 + 5... jeb pa 3."},
                {"jaut": "Cik riteņu ir 6 trīsriteņiem?", "atb": ["18"],
                 "padoms": "3 + 3 + 3 + 3 + 3 + 3."},
            ]),
            pavediens="sports",
            konteksts="Bērnu parkā iznomā trīsriteņus.",
            kapec="Pa 3 - nākamais solis pēc «pa 2»."),

    Kopsavilkums([
        "Meklēju skaitļus, kas ir trīs vienādu skaitļu summa.",
        "Pierakstu tos kā summu.",
        "Zinu, ka ne katrs skaitlis der.",
    ]),

    Majas([
        "Sadali 15 karotes 3 vienādās kaudzītēs.",
        "Pamēģini ar 16 - kas notiek?",
        "Uzraksti visus derīgos skaitļus līdz 30.",
    ]),
]
