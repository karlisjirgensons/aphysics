# -*- coding: utf-8 -*-
"""9. klase, 106. stunda: «Kā atrast naturālos atrisinājumus?»

Ja nezināmie ir skaiti (monētas, biļetes, cilvēki), der tikai naturāli
skaitļi, un atrisinājumu ir galīgs skaits. Tos atrod ar pilno pārlasi:
izmēģina katru iespējamo x un pārbauda, vai y ir vesels.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, plakne, restis)

TEMA = "Kā atrast naturālos atrisinājumus?"

MERKIS = ("Lietosim pilno pārlasi, lai atrastu vienādojuma naturālos "
          "atrisinājumus.")

SATURS = [
    Sakums("3x + 5y = 40 - cik naturālu pāru?",
           zimejums=plakne(grafiki=[(-0.6, 8, "3x + 5y = 40")],
                           punkti=[(5, 5, "(5; 5)"), (10, 2, "(10; 2)")],
                           no_x=0, lidz_x=14, no_y=0, lidz_y=9),
           paraksts="Tikai divos taisnes punktos abas koordinātas naturālas.",
           fakti=["Taisnei bezgalīgi daudz punktu.",
                  "Naturālu - tikai daži (te - divi).",
                  "Tos atrod ar pilno pārlasi."]),

    Doma("Pilnā pārlase",
         "Izsaki y ar x un pārbaudi visas x vērtības, pie kurām y vēl ir "
         "pozitīvs; der tās, kur y ir naturāls.",
         soli=[
             "Izsaki: y = {40 − 3x|5}.",
             "Nosaki robežas: 40 − 3x > 0 ⇒ x ≤ 13.",
             "Pārbaudi x = 1, 2, ..., 13 - vai 40 − 3x dalās ar 5?",
             "Pieraksti visus derīgos pārus.",
         ],
         pieze="Saīsinājums: 40 − 3x dalās ar 5 tikai tad, ja 3x dalās ar 5 - "
               "tātad x = 5, 10."),

    Slidnis("Pārlase tabulā", [
        {"v": "x = 1-4", "teksts": "y = 7,4; 6,8; 6,2; 5,6 - nav veseli",
         "zim": restis([["x", "1", "2", "3", "4"],
                        ["y", "7,4", "6,8", "6,2", "5,6"]])},
        {"v": "x = 5", "teksts": "y = 5 ✔",
         "zim": restis([["x", "5"], ["y", "5"]])},
        {"v": "x = 6-9", "teksts": "y = 4,4; 3,8; 3,2; 2,6 - nav",
         "zim": restis([["x", "6", "7", "8", "9"],
                        ["y", "4,4", "3,8", "3,2", "2,6"]])},
        {"v": "x = 10", "teksts": "y = 2 ✔; tālāk y < 2 un nav vesels",
         "zim": restis([["x", "10", "11", "12", "13"],
                        ["y", "2", "1,4", "0,8", "0,2"]])},
    ]),

    Ievadi("Pārlase", [
        {"jaut": "x + y = 5, x, y ∈ ℕ. Cik pāru?", "atb": ["4"],
         "padoms": "(1; 4), (2; 3), (3; 2), (4; 1)."},
        {"jaut": "2x + y = 9, x, y ∈ ℕ. Cik pāru?", "atb": ["4"],
         "padoms": "x = 1, 2, 3, 4."},
        {"jaut": "2x + 3y = 20, x, y ∈ ℕ. Cik pāru?", "atb": ["3"],
         "padoms": "(7; 2), (4; 4), (1; 6)."},
        {"jaut": "5x + 2y = 21: pāris ar mazāko x ir (1; ?)", "atb": ["8"],
         "padoms": "2y = 16."},
    ]),

    Varianti("Naturāls atrisinājums?", [
        {"jaut": "4x + 6y = 15",
         "opcijas": ["Nav - kreisā puse pāra, labā nepāra", "(3; 0,5)",
                     "(0; 2,5)", "(1; 2)"],
         "pareizi": 0, "padoms": "4x + 6y vienmēr pāra."},
        {"jaut": "x + 2y = 7 - kurš pāris der?",
         "opcijas": ["(3; 2)", "(2; 3)", "(4; 2)", "(7; 1)"],
         "pareizi": 0, "padoms": "3 + 4 = 7."},
    ]),

    Pasaule("Piegāde ar mazām un lielām kastēm",
            Ievadi("", [
                {"jaut": "Jānosūta 50 grāmatas kastēs pa 6 un pa 8, visas "
                         "kastes pilnas: 6x + 8y = 50. Mazākais kastu skaits?",
                 "atb": ["7"], "padoms": "(3; 4): 3 + 4 = 7."},
                {"jaut": "Cik ir derīgu variantu (x, y ∈ ℕ)?", "atb": ["2"],
                 "padoms": "(3; 4) un (7; 1)."},
            ]),
            pavediens="veikals",
            konteksts="Interneta veikals izvēlas kastes tā, lai tās būtu "
                      "pilnas un to būtu maz.",
            kapec="Pārlase atrod visus variantus un labāko no tiem."),

    Kopsavilkums([
        "Atrodu naturālos atrisinājumus ar pārlasi.",
        "Ierobežoju pārlasi ar nevienādību.",
        "Izmantoju dalāmību, lai pārlasi saīsinātu.",
    ]),

    Majas([
        "Atrodi visus naturālos atrisinājumus: 5x + 3y = 34.",
        "Cik veidos 1 € samaksāt ar 10 un 20 centu monētām?",
        "Pamato, kāpēc 6x + 9y = 20 nav veselu atrisinājumu.",
    ]),
]
