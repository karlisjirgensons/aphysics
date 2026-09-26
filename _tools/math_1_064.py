# -*- coding: utf-8 -*-
"""1. klase, 64. stunda: «Kur skaitlis stāv uz skaitļu taisnes?»

Uz taisnes no 0 līdz 100 iedaļas ir pa 10. Skaitlis, kas stāv tālāk pa
labi, ir lielāks. 45 stāv pusceļā starp 40 un 50.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, taisne)

TEMA = "Kur skaitlis stāv uz skaitļu taisnes?"

MERKIS = ("Šodien atliksim skaitļus uz skaitļu taisnes un pamatosim, kurš "
          "ir lielāks.")


def _t(atzimes):
    return taisne(0, 100, 10, [(v, u) for v, u in atzimes])


SATURS = [
    Sakums("Kur uz taisnes ir 45?",
           zimejums=_t([(45, "45")]),
           paraksts="Pusceļā starp 40 un 50.",
           fakti=["Iedaļas pa 10: 0, 10, 20 ... 100.",
                  "Pa labi - lielāks.",
                  "45 ir tieši vidū starp 40 un 50."]),

    Doma("Vieta uz taisnes",
         "Atrodi desmitu, tad paej vēl vienus.",
         soli=[
             "Atrodi iedaļu ar desmitiem: 40.",
             "Līdz nākamajai iedaļai ir 10 soļu.",
             "Paej tik soļu, cik vienu: 45 - pusceļā.",
         ]),

    Ievadi("Kurš skaitlis atzīmēts?", [
        {"jaut": "Kurš skaitlis atzīmēts ar «?»?", "zim": _t([(70, "?")]),
         "atb": ["70"], "padoms": "Saskaiti iedaļas pa 10."},
        {"jaut": "Kurš skaitlis atzīmēts ar «?»?", "zim": _t([(30, "?")]),
         "atb": ["30"], "padoms": "Trešā iedaļa pēc 0."},
        {"jaut": "Kurš skaitlis atzīmēts ar «?»? (pusceļā)",
         "zim": _t([(25, "?")]), "atb": ["25"],
         "padoms": "Pusceļā starp 20 un 30."},
        {"jaut": "Kurš desmits ir tuvāk 68 - 60 vai 70?", "atb": ["70"],
         "padoms": "No 68 līdz 70 - 2 soļi."},
    ]),

    Varianti("Kurš lielāks?", [
        {"jaut": "Kurš lielāks: A vai B?",
         "zim": _t([(30, "A"), (80, "B")]),
         "opcijas": ["B", "A"], "jaukt": False, "pareizi": 0,
         "padoms": "Pa labi - lielāks."},
        {"jaut": "Kurš tuvāk nullei: 15 vai 51?",
         "opcijas": ["15", "51"], "jaukt": False, "pareizi": 0,
         "padoms": "Mazākais ir tuvāk 0."},
    ]),

    Pasaule("Ceļš uz skolu",
            Ievadi("", [
                {"jaut": "Ceļš līdz skolai 100 m. Tu esi pie 60 m atzīmes. "
                         "Cik m vēl?", "zim": _t([(60, "tu")]),
                 "atb": ["40"], "padoms": "No 60 līdz 100."},
            ]),
            pavediens="celojums",
            konteksts="Ceļu var iedomāties kā skaitļu taisni.",
            kapec="Taisnē redz, cik noiets un cik atlicis."),

    Kopsavilkums([
        "Atlieku skaitļus uz skaitļu taisnes.",
        "Zinu: pa labi - lielāks.",
        "Atrodu tuvāko desmitu.",
    ]),

    Majas([
        "Uzzīmē taisni no 0 līdz 100 pa 10 un atzīmē savu vecumu.",
        "Atzīmē 50 un 55.",
        "Kurš desmits ir tuvāk 38?",
    ]),
]
