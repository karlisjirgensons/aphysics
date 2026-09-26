# -*- coding: utf-8 -*-
"""1. klase, 39. stunda: «Vai aiz «=» vienmēr ir atbilde?»

Zīme «=» nav «un tagad atbilde», bet «abās pusēs tikpat». Tāpēc abās pusēs
var būt izteiksme: 3 + 2 = 4 + 1. To salīdzina kā svarus, kas ir līdzsvarā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, bildes)

TEMA = "Vai aiz «=» vienmēr ir atbilde?"

MERKIS = ("Šodien lasīsim un veidosim vienādības, kurās abās pusēs ir "
          "izteiksme.")

SATURS = [
    Sakums("3 + 2 = 4 + 1 - vai tā drīkst rakstīt?",
           zimejums=bildes([[("ripina", 3), ("ripina*", 2)],
                            [("ripina", 4), ("ripina*", 1)]]),
           paraksts="Abās rindās 5 ripiņas - tikpat.",
           fakti=["«=» nozīmē tikpat, kā svari līdzsvarā.",
                  "Abās pusēs var būt darbība.",
                  "Izrēķini abas puses un salīdzini."]),

    Doma("Svari līdzsvarā",
         "Vienādība ir patiesa, ja abas puses ir vienādi «smagas».",
         soli=[
             "Izrēķini kreiso pusi: 3 + 2 = 5.",
             "Izrēķini labo pusi: 4 + 1 = 5.",
             "Vienādi - svari līdzsvarā.",
         ]),

    Ievadi("Atrodi trūkstošo", [
        {"jaut": "3 + 2 = 4 + ?", "atb": ["1"], "padoms": "Abās pusēs 5."},
        {"jaut": "5 + 5 = 6 + ?", "atb": ["4"], "padoms": "Abās pusēs 10."},
        {"jaut": "2 + 6 = ? + 4", "atb": ["4"], "padoms": "Abās pusēs 8."},
        {"jaut": "9 − 1 = 4 + ?", "atb": ["4"], "padoms": "Abās pusēs 8."},
        {"jaut": "7 + 0 = 5 + ?", "atb": ["2"], "padoms": "Abās pusēs 7."},
        {"jaut": "10 − 3 = ? + 1", "atb": ["6"], "padoms": "Abās pusēs 7."},
    ], pamats=4),

    Varianti("Līdzsvarā?", [
        {"jaut": "1 + 5 = 3 + 3", "opcijas": ["Patiess", "Aplams"],
         "jaukt": False, "pareizi": 0, "padoms": "Abās pusēs 6."},
        {"jaut": "4 + 4 = 5 + 2", "opcijas": ["Patiess", "Aplams"],
         "jaukt": False, "pareizi": 1, "padoms": "8 un 7."},
        {"jaut": "6 − 2 = 2 + 2", "opcijas": ["Patiess", "Aplams"],
         "jaukt": False, "pareizi": 0, "padoms": "Abās pusēs 4."},
    ]),

    Pasaule("Maiņa ar kārtīm",
            Ievadi("", [
                {"jaut": "Tev ir 4 + 3 kārtis, draugam 5 + ?. Cik vajag, lai "
                         "būtu tikpat?", "atb": ["2"], "padoms": "Abās pusēs "
                                                              "7."},
            ]),
            pavediens="speles",
            konteksts="Spēlē abiem jābūt vienādam kāršu skaitam.",
            kapec="«=» nozīmē godīgi - abiem tikpat."),

    Kopsavilkums([
        "Zinu, ka «=» nozīmē tikpat.",
        "Lasu vienādības ar darbību abās pusēs.",
        "Atrodu trūkstošo, lai būtu līdzsvarā.",
    ]),

    Majas([
        "Uzraksti 3 vienādības, kurās abās pusēs ir darbība.",
        "Noliec divās kaudzēs karotes tā, lai 2 + 5 = 3 + 4.",
        "Izskaidro mājiniekam, kāpēc 6 + 1 = 5 + 2.",
    ]),
]
