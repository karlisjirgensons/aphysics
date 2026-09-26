# -*- coding: utf-8 -*-
"""1. klase, 133. stunda: «Kura summa ir lielāka?»

Naudas summas salīdzina ar «<», «>», «=». Ja mērvienības atšķiras
(1 € un 90 c), vispirms pārvērš centos: 1 € = 100 c > 90 c.
"""

from math_saturs import (Doma, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, monetas)

TEMA = "Kura summa ir lielāka?"

MERKIS = ("Šodien salīdzināsim naudas summas eiro un centos, pierakstot «<», "
          "«>» vai «=».")


def _z(a, b, zime, padoms):
    return {"jaut": "%s ? %s" % (a, b), "opcijas": ["<", ">", "="],
            "jaukt": False, "pareizi": ["<", ">", "="].index(zime),
            "padoms": padoms}


SATURS = [
    Sakums("1 € vai 90 c - kas vairāk?",
           zimejums=monetas(["1 €", "50 c", "20 c", "20 c"]),
           paraksts="1 € = 100 c; 50 + 20 + 20 = 90 c. 1 € > 90 c.",
           fakti=["Vispirms vienādas mērvienības.",
                  "1 € = 100 c.",
                  "Tad salīdzini skaitļus."]),

    Doma("Salīdzini naudu",
         "Pārvērš abas summas centos vai eiro, tad liek zīmi.",
         soli=[
             "Vai mērvienības vienādas?",
             "Ja nē - 1 € = 100 c.",
             "Salīdzini un liec <, >, =.",
         ]),

    Varianti("Liec zīmi", [
        _z("1 €", "90 c", ">", "100 c > 90 c."),
        _z("50 c", "5 c", ">", "50 > 5."),
        _z("100 c", "1 €", "=", "Tas pats."),
        _z("2 € 20 c", "2 € 50 c", "<", "Eiro vienādi, 20 < 50."),
        _z("20 c + 20 c", "50 c", "<", "40 c < 50 c."),
        _z("3 €", "2 € 99 c", ">", "3 € = 2 € 100 c."),
    ], pamats=4),

    Varianti("Kam vairāk?", [
        {"jaut": "Annai 3 monētas pa 20 c. Jānim 1 monēta 50 c.",
         "opcijas": ["Annai", "Jānim", "vienādi"], "pareizi": 0,
         "padoms": "60 c > 50 c."},
        {"jaut": "Mārai 2 € un 1 €. Pēterim 5 €.",
         "opcijas": ["Pēterim", "Mārai", "vienādi"], "pareizi": 0,
         "padoms": "3 € < 5 €."},
    ]),

    Pasaule("Lētākais piedāvājums",
            Varianti("", [
                {"jaut": "Vienā veikalā bulciņa 95 c, otrā 1 € 5 c. Kur "
                         "lētāk?", "opcijas": ["pirmajā", "otrajā"],
                 "jaukt": False, "pareizi": 0, "padoms": "95 c < 105 c."},
            ]),
            pavediens="veikals",
            konteksts="Dažādos veikalos cenas atšķiras.",
            kapec="Salīdzinot cenas, ietaupa."),

    Kopsavilkums([
        "Salīdzinu naudas summas.",
        "Pārvēršu eiro centos.",
        "Lietoju <, >, =.",
    ]),

    Majas([
        "Salīdzini divu preču cenas veikalā.",
        "Pieraksti ar zīmi.",
        "Cik ietaupītu, ja pirktu lētāko?",
    ]),
]
