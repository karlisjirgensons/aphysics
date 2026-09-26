# -*- coding: utf-8 -*-
"""2. klase, 139. stunda: «Cik rūtiņu ir taisnstūrī?»

Taisnstūrī rūtiņas var saskaitīt pa rindām (3 rindas pa 5) vai pa kolonnām
(5 kolonnas pa 3) - abos gadījumos 15. Tā reizinājums kļūst par laukumu, ko
2.6. tematā skaitīja pa vienai.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, rutinas)

TEMA = "Cik rūtiņu ir taisnstūrī?"

MERKIS = ("Šodien noteiksim rūtiņu skaitu taisnstūrī, skaitot pa rindām vai "
          "kolonnām, un pierakstīsim reizinājumu.")

SATURS = [
    Sakums("Cik šokolādes gabaliņu ir tāfelītē, nesaskaitot katru?",
           zimejums=rutinas(5, 3),
           paraksts="3 rindas pa 5 - 3 · 5 = 15.",
           fakti=["Saskaiti rindu garumu un rindu skaitu.",
                  "Pa rindām: 5 + 5 + 5.",
                  "Pa kolonnām: 3 + 3 + 3 + 3 + 3."]),

    Doma("Rindas un kolonnas",
         "Rūtiņu skaits = rindu skaits · rūtiņas vienā rindā.",
         soli=[
             "Saskaiti rūtiņas vienā rindā.",
             "Saskaiti rindas.",
             "Pieraksti reizinājumu: 3 · 5.",
             "Aprēķini: 15.",
         ]),

    Slidnis("3 rindas pa 5", [
        {"v": "1 · 5 = 5", "teksts": "Viena rinda.",
         "zim": rutinas(5, 3, 5, 1)},
        {"v": "2 · 5 = 10", "teksts": "Divas rindas.",
         "zim": rutinas(5, 3, 5, 2)},
        {"v": "3 · 5 = 15", "teksts": "Trīs rindas.",
         "zim": rutinas(5, 3, 5, 3)},
    ]),

    Ievadi("Cik rūtiņu?", [
        {"jaut": "Cik rūtiņu?", "zim": rutinas(4, 3), "atb": ["12"],
         "padoms": "3 rindas pa 4."},
        {"jaut": "Cik rūtiņu?", "zim": rutinas(6, 3), "atb": ["18"],
         "padoms": "3 rindas pa 6."},
        {"jaut": "Cik rūtiņu?", "zim": rutinas(3, 3), "atb": ["9"],
         "padoms": "3 · 3."},
        {"jaut": "Cik rūtiņu?", "zim": rutinas(7, 3), "atb": ["21"],
         "padoms": "3 · 7."},
        {"jaut": "Cik rūtiņu?", "zim": rutinas(8, 3), "atb": ["24"],
         "padoms": "3 · 8."},
        {"jaut": "Cik rūtiņu?", "zim": rutinas(9, 3), "atb": ["27"],
         "padoms": "3 · 9."},
    ], pamats=4),

    Varianti("Kurš reizinājums?", [
        {"jaut": "Kurš reizinājums der šim taisnstūrim?",
         "zim": rutinas(4, 3), "opcijas": ["3 · 4", "3 · 3", "4 · 4"],
         "pareizi": 0, "padoms": "3 rindas, 4 kolonnas."},
        {"jaut": "Kurš vēl der?", "zim": rutinas(4, 3),
         "opcijas": ["4 · 3", "4 + 3", "3 + 3"], "pareizi": 0,
         "padoms": "4 kolonnas pa 3."},
    ]),

    Pasaule("Olu kaste",
            Ievadi("", [
                {"jaut": "Olu kastē 3 rindas pa 6 olām. Cik olu?",
                 "zim": rutinas(6, 3), "atb": ["18"], "padoms": "3 · 6."},
                {"jaut": "Mazā kastē 2 rindas pa 3. Cik olu?",
                 "zim": rutinas(3, 2), "atb": ["6"], "padoms": "2 · 3."},
            ]),
            pavediens="veikals",
            konteksts="Olas pārdod kastēs ar rindām.",
            kapec="Rindas un kolonnas ļauj saskaitīt ātri."),

    Kopsavilkums([
        "Saskaitu rūtiņas taisnstūrī pa rindām un kolonnām.",
        "Pierakstu reizinājumu.",
        "Zinu, ka abi veidi dod vienu skaitli.",
    ]),

    Majas([
        "Atrodi mājās kaut ko rindās: flīzes, olu kasti, logu rūtis.",
        "Pieraksti reizinājumu.",
        "Aprēķini, cik to ir kopā.",
    ]),
]
