# -*- coding: utf-8 -*-
"""1. klase, 16. stunda: «Vai uz mērķi ir tikai viens ceļš?»

Uz vienu mērķi ved vairāki ceļi. Ja soļus tikai samaina vietām (→→↑↑ vai
↑↑→→), ceļš ir tikpat garš; apkārtceļš ir garāks. Salīdzina ceļus pēc soļu
skaita.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, celjs)

TEMA = "Vai uz mērķi ir tikai viens ceļš?"

MERKIS = ("Šodien atradīsim vairākus ceļus uz vienu mērķi un salīdzināsim "
          "tos.")


def _l(soli="", skersli=()):
    return celjs(5, 4, (0, 3), (3, 1), soli, skersli=skersli)


SATURS = [
    Sakums("Pa kuru ceļu iet - un vai tas ir svarīgi?",
           zimejums=_l("→→→↑↑"),
           paraksts="→→→↑↑ - pieci soļi.",
           fakti=["Uz mērķi var aiziet pa dažādiem ceļiem.",
                  "Samainot soļus vietām, ceļš ir tikpat garš.",
                  "Apkārtceļš ir garāks."]),

    Slidnis("Trīs ceļi uz vienu ābolu", [
        {"v": "→→→↑↑", "teksts": "5 soļi", "zim": _l("→→→↑↑")},
        {"v": "↑↑→→→", "teksts": "Arī 5 soļi - soļi samainīti",
         "zim": _l("↑↑→→→")},
        {"v": "↑↑↑→→→↓", "teksts": "7 soļi - apkārtceļš",
         "zim": _l("↑↑↑→→→↓")},
    ]),

    Doma("Salīdzini ceļus",
         "Garākais ceļš ir tas, kurā vairāk bultiņu.",
         soli=[
             "Saskaiti katra ceļa bultiņas.",
             "Mazāk bultiņu - īsāks ceļš.",
             "Ja soļi tikai samainīti vietām, ceļi ir vienādi gari.",
         ]),

    Ievadi("Cik soļu?", [
        {"jaut": "Cik soļu ir ceļā ↑↑→→→?", "zim": _l("↑↑→→→"),
         "atb": ["5"], "padoms": "Saskaiti bultiņas."},
        {"jaut": "Cik soļu ir apkārtceļā?", "zim": _l("↑↑↑→→→↓"),
         "atb": ["7"], "padoms": "Saskaiti bultiņas."},
        {"jaut": "Par cik soļiem apkārtceļš ir garāks nekā 5 soļi?",
         "atb": ["2"], "padoms": "7 un 5."},
    ]),

    Varianti("Kurš ceļš?", [
        {"jaut": "Vai →↑→↑→ nonāk tajā pašā vietā kā →→→↑↑?",
         "opcijas": ["Jā", "Nē"], "jaukt": False, "pareizi": 0,
         "padoms": "Arī 3 pa labi un 2 uz augšu."},
        {"jaut": "Pelēkā rūtiņa ir siena. Kurš ceļš der?",
         "zim": _l("", skersli=[(3, 3), (2, 2)]),
         "opcijas": ["↑↑→→→", "→→→↑↑", "→→↑↑→"], "pareizi": 0,
         "padoms": "Apej pelēkās rūtiņas."},
    ]),

    Pasaule("Uz rotaļu laukumu",
            Varianti("", [
                {"jaut": "Ceļš gar parku ir 6 soļi, pāri ielai - 4 soļi, "
                         "bet tur nav gājēju pārejas. Kuru izvēlēties?",
                 "opcijas": ["gar parku - tas ir drošs",
                             "pāri ielai - tas īsāks"],
                 "jaukt": False, "pareizi": 0,
                 "padoms": "Īsākais ne vienmēr ir labākais."},
            ]),
            pavediens="celojums",
            konteksts="Uz rotaļu laukumu var aiziet pa diviem ceļiem.",
            kapec="Salīdzinām ceļus - un izvēlamies ne tikai pēc garuma."),

    Kopsavilkums([
        "Atrodu vairākus ceļus uz vienu mērķi.",
        "Salīdzinu ceļus pēc soļu skaita.",
        "Zinu, ka, samainot soļus vietām, garums nemainās.",
    ]),

    Majas([
        "Atrodi divus ceļus no savas istabas līdz durvīm. Kurš īsāks?",
        "Saskaiti soļus abos ceļos.",
        "Uzzīmē rūtiņās labirintu un divus ceļus caur to.",
    ]),
]
