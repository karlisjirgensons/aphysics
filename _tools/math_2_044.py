# -*- coding: utf-8 -*-
"""2. klase, 44. stunda: «Cik pietrūkst līdz 100?»

Papildināšana līdz apaļam skaitlim: vispirms līdz tuvākajam desmitam, tad
līdz 100. 100 − 37 = 3 + 60 = 63. Tas ir galvenais atlikuma paņēmiens -
tā to rēķina pārdevējs, kas atdod naudu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Kustiba, Majas,
                         Pasaule, Sakums, Varianti, simta_kvadrats, taisne)

TEMA = "Cik pietrūkst līdz 100?"

MERKIS = ("Šodien aprēķināsim, cik pietrūkst līdz pilnam simtam vai "
          "desmitam.")

SATURS = [
    Sakums("Uzlīmju albumā ir 100 vietu. Tev ir 37 uzlīmes. Cik vēl "
           "vajag?",
           zimejums=taisne(30, 100, 10, bultas=[(37, 40, "+3"),
                                                (40, 100, "+60")]),
           paraksts="3 līdz 40 un 60 līdz 100.",
           fakti=["Vispirms papildini līdz desmitam.",
                  "Tad pa desmitiem līdz 100.",
                  "3 + 60 = 63."]),

    Doma("Papildināšana",
         "Cik pietrūkst - to atrod ar lēcieniem līdz apaļam skaitlim.",
         soli=[
             "No 37 līdz 40 - 3.",
             "No 40 līdz 100 - 6 desmiti, tas ir 60.",
             "Saskaiti lēcienus: 3 + 60 = 63.",
             "Pārbaude: 37 + 63 = 100.",
         ],
         pieze="Desmita draugi palīdz: 7 + 3 = 10, tāpēc 37 + 3 = 40."),

    Ievadi("Līdz desmitam", [
        {"jaut": "46 + ? = 50", "atb": ["4"], "padoms": "6 + 4 = 10."},
        {"jaut": "83 + ? = 90", "atb": ["7"], "padoms": "3 + 7 = 10."},
        {"jaut": "29 + ? = 30", "atb": ["1"], "padoms": "9 + 1."},
        {"jaut": "55 + ? = 60", "atb": ["5"], "padoms": "5 + 5."},
    ]),

    Ievadi("Līdz simtam", [
        {"jaut": "Cik pietrūkst līdz 100 no 70?", "atb": ["30"],
         "padoms": "3 desmiti."},
        {"jaut": "Cik pietrūkst līdz 100 no 64?", "atb": ["36"],
         "padoms": "6 + 30."},
        {"jaut": "Cik pietrūkst līdz 100 no 18?", "atb": ["82"],
         "padoms": "2 + 80."},
        {"jaut": "Cik pietrūkst līdz 100 no 91?", "atb": ["9"],
         "padoms": "91 + 9."},
        {"jaut": "Cik pietrūkst līdz 100 no 45?", "atb": ["55"],
         "padoms": "5 + 50."},
        {"jaut": "Cik pietrūkst līdz 100 no 33?", "atb": ["67"],
         "padoms": "7 + 60."},
    ], pamats=4),

    Kustiba("Aizbrauc līdz 100", [
        {"jaut": "Mašīna ir pie 72 km. Cik km vēl jābrauc līdz 100 km "
                 "atzīmei?", "atb": 28, "beigas": 40, "iedala": 5,
         "mers": "km", "objekts": "mašīna", "merkis": "100",
         "padoms": "8 + 20."},
        {"jaut": "Mašīna ir pie 86 km. Cik vēl līdz 100?", "atb": 14,
         "beigas": 40, "iedala": 5, "mers": "km", "objekts": "mašīna",
         "merkis": "100", "padoms": "4 + 10."},
    ], ievads="Ieraksti, cik km vēl jābrauc."),

    Varianti("Simta kvadrātā", [
        {"jaut": "Cik tukšu rūtiņu līdz 100, ja iekrāsotas 1-58?",
         "zim": simta_kvadrats(51, 100, izcelt=list(range(51, 59))),
         "opcijas": ["42", "58", "52"], "pareizi": 0,
         "padoms": "2 + 40."},
    ]),

    Pasaule("Cik atdos atpakaļ?",
            Ievadi("", [
                {"jaut": "Samaksāji ar 100 € banknoti par 64 € kurpēm. Cik "
                         "atdos?", "atb": ["36"], "mers": "€",
                 "padoms": "64 + 6 = 70, + 30 = 100."},
                {"jaut": "Samaksāji 1 € (100 c) par 45 c bulciņu. Cik "
                         "centu atdos?", "atb": ["55"], "mers": "c",
                 "padoms": "45 + 5 = 50, + 50 = 100."},
            ]),
            pavediens="veikals",
            konteksts="Pārdevējs atlikumu skaita, papildinot līdz "
                      "samaksātajam.",
            kapec="Tā atlikumu rēķina visā pasaulē."),

    Kopsavilkums([
        "Papildinu skaitli līdz tuvākajam desmitam.",
        "Aprēķinu, cik pietrūkst līdz 100.",
        "Pārbaudu ar saskaitīšanu.",
    ]),

    Majas([
        "Ar mājinieku spēlē «līdz 100»: viens saka skaitli, otrs - cik "
        "pietrūkst.",
        "Izrēķini: 100 − 27, 100 − 81, 100 − 49.",
        "Kurš bija ātrākais?",
    ]),
]
