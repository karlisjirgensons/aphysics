# -*- coding: utf-8 -*-
"""1. klase, 111. stunda: «Kā uzzīmēt divus nogriežņus?»

Uzzīmē nogriezni un otru - par doto skaitli garāku vai īsāku: 6 cm un
6 + 3 = 9 cm. Abus sāk no vienas vietas, lai starpību redz.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Varianti, lineals)

TEMA = "Kā uzzīmēt divus nogriežņus?"

MERKIS = ("Šodien uzzīmēsim divus nogriežņus tā, lai viens būtu par doto "
          "skaitli garāks nekā otrs.")

SATURS = [
    Sakums("Pirmais 6 cm, otrais par 3 cm garāks. Cik garš otrais?",
           zimejums=lineals(10, [(0, 6, "6 cm"), (0, 9, "9 cm")]),
           paraksts="6 + 3 = 9 cm.",
           fakti=["Vispirms aprēķini otra garumu.",
                  "Zīmē abus no vienas vietas.",
                  "Pārbaudi starpību ar lineālu."]),

    Doma("Plāns zīmēšanai",
         "Aprēķini, zīmē, pārbaudi.",
         soli=[
             "Garāks par n - pieskaiti; īsāks - atņem.",
             "Uzzīmē pirmo nogriezni.",
             "Zem tā - otru, sākot tajā pašā vietā.",
             "Izmēri starpību.",
         ]),

    Ievadi("Aprēķini garumu", [
        {"jaut": "Pirmais 5 cm, otrais par 4 cm garāks. Otrais (cm)?",
         "atb": ["9"], "padoms": "5 + 4."},
        {"jaut": "Pirmais 12 cm, otrais par 5 cm īsāks. Otrais (cm)?",
         "atb": ["7"], "padoms": "12 − 5."},
        {"jaut": "Par cik cm atšķiras?",
         "zim": lineals(20, [(0, 14, "14 cm"), (0, 8, "8 cm")]),
         "atb": ["6"], "padoms": "14 − 8."},
    ]),

    Varianti("Vai uzzīmēts pareizi?", [
        {"jaut": "Vajag: otrais par 2 cm garāks nekā 7 cm.",
         "zim": lineals(10, [(0, 7, ""), (0, 9, "")]),
         "opcijas": ["Jā", "Nē"], "jaukt": False, "pareizi": 0,
         "padoms": "7 un 9."},
        {"jaut": "Vajag: otrais par 3 cm īsāks nekā 8 cm.",
         "zim": lineals(10, [(0, 8, ""), (0, 4, "")]),
         "opcijas": ["Nē - jābūt 5 cm", "Jā"], "jaukt": False, "pareizi": 0,
         "padoms": "8 − 3 = 5."},
    ]),

    Petijums("Zīmē burtnīcā", [
        "Uzzīmē nogriezni 8 cm.",
        "Zem tā - par 4 cm garāku.",
        "Vēl zemāk - par 3 cm īsāku nekā pirmais.",
        "Pieraksti visus garumus.",
    ], vajag="lineāls, zīmulis, burtnīca"),

    Pasaule("Lentes dāvanām",
            Ievadi("", [
                {"jaut": "Mazajai kastei lente 9 cm, lielajai par 8 cm garāka. "
                         "Cik cm lielajai?", "atb": ["17"], "padoms": "9 + 8."},
            ]),
            pavediens="maja",
            konteksts="Dāvanu kastēm vajag dažāda garuma lentes.",
            kapec="Aprēķini pirms griez - lente nepietrūks."),

    Kopsavilkums([
        "Aprēķinu otrā nogriežņa garumu.",
        "Zīmēju abus no vienas vietas.",
        "Pārbaudu starpību.",
    ]),

    Majas([
        "Uzzīmē 2 nogriežņus: 6 cm un par 5 cm garāku.",
        "Uzzīmē 15 cm un par 7 cm īsāku.",
        "Izmēri un pārbaudi.",
    ]),
]
