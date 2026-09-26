# -*- coding: utf-8 -*-
"""1. klase, 31. stunda: «Skaitīt klāt vai atcerēties?»

Trīs saskaitīšanas paņēmieni: saliek kopā un izskaita visu; skaita uz
priekšu no pirmā; izmanto skaitļa sastāvu, ko jau zina. Salīdzina, kurš
ātrāks.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, bildes, majina, taisne)

TEMA = "Skaitīt klāt vai atcerēties?"

MERKIS = ("Šodien salīdzināsim trīs veidus, kā saskaitīt, un izvēlēsimies "
          "ātrāko.")

SATURS = [
    Sakums("6 + 3 - kā tu to izrēķini?",
           zimejums=bildes([[("ripina", 6), ("ripina*", 3)]]),
           paraksts="Var skaitīt visus, var skaitīt no 6, var atcerēties.",
           fakti=["Izskaitīt visu - drošs, bet lēns.",
                  "Skaitīt no lielākā - ātrāk.",
                  "Atcerēties sastāvu - visātrāk."]),

    Slidnis("Trīs veidi", [
        {"v": "1", "teksts": "Izskaiti visus: 1, 2, 3 ... 9",
         "zim": bildes([[("ripina", 6), ("ripina*", 3)]])},
        {"v": "2", "teksts": "No 6 uz priekšu: 7, 8, 9",
         "zim": taisne(0, 10, 1, [(9, "9")],
                       bultas=[(6, 7, ""), (7, 8, ""), (8, 9, "")])},
        {"v": "3", "teksts": "Atceros: 9 = 6 + 3",
         "zim": majina(9, [(6, 3)])},
    ]),

    Doma("Izvēlies ātrāko",
         "Ja sastāvu zini no galvas - atceries; ja nē - skaiti no lielākā.",
         soli=[
             "Vai zinu šo summu? Tad saku uzreiz.",
             "Ja nē - sāku ar lielāko skaitli.",
             "Skaitu uz priekšu tik soļu, cik mazākais.",
         ]),

    Ievadi("Saskaiti", [
        {"jaut": "6 + 3 = ?", "atb": ["9"], "padoms": "No 6: 7, 8, 9."},
        {"jaut": "5 + 4 = ?", "atb": ["9"], "padoms": "No 5: 6, 7, 8, 9."},
        {"jaut": "2 + 6 = ?", "atb": ["8"], "padoms": "No 6: 7, 8."},
        {"jaut": "7 + 3 = ?", "atb": ["10"], "padoms": "Desmita draugi."},
        {"jaut": "4 + 4 = ?", "atb": ["8"], "padoms": "Divreiz 4."},
        {"jaut": "1 + 5 = ?", "atb": ["6"], "padoms": "Pēc 5."},
    ], pamats=4),

    Varianti("Kurš veids te ātrākais?", [
        {"jaut": "8 + 1", "opcijas": ["skaitīt no 8 vienu soli",
                                      "izskaitīt visus 9"],
         "jaukt": False, "pareizi": 0, "padoms": "Tikai viens solis."},
        {"jaut": "5 + 5", "opcijas": ["atcerēties: 10",
                                      "izskaitīt visus"],
         "jaukt": False, "pareizi": 0, "padoms": "Divas rokas!"},
    ]),

    Pasaule("Punkti spēlē",
            Ievadi("", [
                {"jaut": "Tev bija 7 punkti, uzmeti 2. Cik tagad?",
                 "atb": ["9"], "padoms": "No 7: 8, 9."},
                {"jaut": "Tev bija 4, uzmeti 5. Cik tagad?", "atb": ["9"],
                 "padoms": "No 5 uz priekšu 4."},
            ]),
            pavediens="speles",
            konteksts="Galda spēlē punkti jāsaskaita ātri, kamēr citi gaida.",
            kapec="Ātrs paņēmiens - ātrāka spēle."),

    Kopsavilkums([
        "Zinu trīs saskaitīšanas veidus.",
        "Skaitu uz priekšu no lielākā.",
        "Izvēlos ātrāko veidu.",
    ]),

    Majas([
        "Izrēķini 3 + 6 trīs veidos.",
        "Kuras summas tu jau zini no galvas? Pieraksti.",
        "Spēlē ar kauliņiem un saskaiti ātri.",
    ]),
]
