# -*- coding: utf-8 -*-
"""1. klase, 101. stunda: «Kuru paņēmienu izvēlēties?»

Katram piemēram savs ērtākais ceļš: 9 + 6 - caur 10; 7 + 7 - dubultais;
15 − 13 - skaitīt uz priekšu; 16 − 3 - kā pirmajā desmitā. Skolēns
izvēlas un pamato.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti)

TEMA = "Kuru paņēmienu izvēlēties?"

MERKIS = ("Šodien izvēlēsimies ērtāko paņēmienu katram piemēram un "
          "paskaidrosim, kāpēc.")

_PANEMIENI = ["caur 10", "dubultais", "skaitīt uz priekšu",
              "kā pirmajā desmitā"]


def _k(piemers, pareizais, padoms):
    return {"jaut": piemers, "opcijas": _PANEMIENI, "jaukt": False,
            "pareizi": _PANEMIENI.index(pareizais), "padoms": padoms}


SATURS = [
    Sakums("Vai visus piemērus rēķina vienādi?",
           fakti=["9 + 6 - caur 10: 9 + 1 + 5.",
                  "7 + 7 - dubultais: 14.",
                  "15 − 13 - skaiti no 13 uz priekšu: 2."]),

    Doma("Izvēlies gudri",
         "Paskaties uz skaitļiem, pirms sāc rēķināt.",
         soli=[
             "Vai skaitļi vienādi vai gandrīz? - dubultais.",
             "Vai viens ir 8 vai 9? - caur 10.",
             "Vai skaitļi ir tuvu viens otram? - skaiti uz priekšu.",
             "Vai vienu pietiek? - kā pirmajā desmitā.",
         ]),

    Varianti("Kurš paņēmiens ērtākais?", [
        _k("9 + 6", "caur 10", "9 + 1 = 10."),
        _k("7 + 7", "dubultais", "Divi vienādi."),
        _k("15 − 13", "skaitīt uz priekšu", "13, 14, 15."),
        _k("16 − 3", "kā pirmajā desmitā", "6 − 3 = 3."),
        _k("8 + 5", "caur 10", "8 + 2 = 10."),
        _k("6 + 7", "dubultais", "6 + 6 un vēl 1."),
    ], pamats=4),

    Ievadi("Izrēķini savā veidā", [
        {"jaut": "9 + 6", "atb": ["15"], "padoms": "Caur 10."},
        {"jaut": "7 + 7", "atb": ["14"], "padoms": "Dubultais."},
        {"jaut": "15 − 13", "atb": ["2"], "padoms": "Uz priekšu."},
        {"jaut": "16 − 3", "atb": ["13"], "padoms": "6 − 3."},
    ]),

    Pasaule("Rēķins galvā veikalā",
            Varianti("", [
                {"jaut": "Siers 9 €, piens 3 €. Kā ātri saskaitīt?",
                 "opcijas": ["caur 10: 9 + 1 + 2", "skaitīt no 1"],
                 "jaukt": False, "pareizi": 0, "padoms": "9 + 3 = 12."},
            ]),
            pavediens="veikals",
            konteksts="Veikalā nav laika rakstīt - rēķina galvā.",
            kapec="Gudrs paņēmiens - ātrs rēķins."),

    Kopsavilkums([
        "Zinu vairākus paņēmienus.",
        "Izvēlos ērtāko konkrētam piemēram.",
        "Paskaidroju savu izvēli.",
    ]),

    Majas([
        "Uzraksti 4 piemērus - katram citu paņēmienu.",
        "Palūdz mājiniekam uzminēt, kuru paņēmienu izvēlējies.",
        "Kurš paņēmiens tev patīk visvairāk?",
    ]),
]
