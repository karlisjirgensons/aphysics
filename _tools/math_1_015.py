# -*- coding: utf-8 -*-
"""1. klase, 15. stunda: «Kā ar bultiņām pastāstīt ceļu?»

Pārvietošanos pa rūtiņu laukumu pieraksta ar bultiņām: katra bultiņa ir
viens solis vienā rūtiņā. «→→↑» nozīmē: divi soļi pa labi, viens uz augšu.
Tā ir pirmā «programma».
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Varianti, celjs)

TEMA = "Kā ar bultiņām pastāstīt ceļu?"

MERKIS = ("Šodien pierakstīsim ceļu ar bultiņām un iesim pa bultiņām.")


def _l(soli="", merkis=(3, 0), sakums=(0, 3), **kw):
    return celjs(5, 4, sakums, merkis, soli, **kw)


SATURS = [
    Sakums("Kā ripiņa var tikt līdz ābolam?",
           zimejums=_l("→→→↑↑↑"),
           paraksts="Trīs soļi pa labi, trīs uz augšu: →→→↑↑↑.",
           fakti=["Viena bultiņa - viens solis.",
                  "Bultiņa rāda virzienu.",
                  "Bultiņu virkne ir ceļa pieraksts."]),

    Doma("Bultiņu valoda",
         "→ pa labi, ← pa kreisi, ↑ uz augšu, ↓ uz leju - katra bultiņa ir "
         "viena rūtiņa.",
         soli=[
             "Novieto pirkstu uz ripiņas.",
             "Par katru bultiņu pārvieto pirkstu vienu rūtiņu.",
             "Kur apstājies - tur ceļš beidzas.",
         ]),

    Varianti("Kurš pieraksts der?", [
        {"jaut": "Kā pierakstīt šo ceļu?", "zim": _l("→→↑↑"),
         "opcijas": ["→→↑↑", "↑↑→→→", "→↑→"], "pareizi": 0,
         "padoms": "Vispirms pa labi, tad uz augšu."},
        {"jaut": "Kā pierakstīt šo ceļu?", "zim": _l("↑↑↑→→→"),
         "opcijas": ["↑↑↑→→→", "→→→↑↑↑", "↑→↑→"], "pareizi": 0,
         "padoms": "Vispirms uz augšu."},
        {"jaut": "Kurš ceļš ved līdz ābolam?", "zim": _l(),
         "opcijas": ["→→→↑↑↑", "→→↑↑", "↑↑↑→→"], "pareizi": 0,
         "padoms": "Ābols ir 3 pa labi un 3 uz augšu."},
    ]),

    Ievadi("Saskaiti soļus", [
        {"jaut": "Cik soļu ir ceļā →→↑↑?", "zim": _l("→→↑↑"),
         "atb": ["4"], "padoms": "Saskaiti bultiņas."},
        {"jaut": "Cik soļu pa labi jāiet līdz ābolam?", "zim": _l(),
         "atb": ["3"], "padoms": "Skaiti rūtiņas pa labi."},
        {"jaut": "Cik soļu uz augšu?", "zim": _l(), "atb": ["3"],
         "padoms": "Skaiti rūtiņas uz augšu."},
    ]),

    Petijums("Robots klasē", [
        "Viens ir «robots», otrs - «programmētājs».",
        "Programmētājs uzraksta 3-5 bultiņas uz lapiņas.",
        "Robots iet pa klasi tieši pēc bultiņām.",
        "Vai robots nonāca tur, kur bija domāts?",
    ], vajag="lapiņa, zīmulis"),

    Pasaule("Ceļš līdz skolai",
            Varianti("", [
                {"jaut": "Ripiņa ir mājās, ābols - skola. Pelēkā rūtiņa ir "
                         "māja, tur iet nevar. Kurš ceļš der?",
                 "zim": _l("→→→↑↑↑", skersli=[(1, 1)]),
                 "opcijas": ["→→→↑↑↑", "↑↑→→→↑", "→↑↑↑→→"], "pareizi": 0,
                 "padoms": "Pārbaudi, vai ceļš neiet caur pelēko."},
            ]),
            pavediens="celojums",
            konteksts="Ceļu uz skolu var pastāstīt ar bultiņām kā kartē.",
            kapec="Bultiņas ir īss ceļa pieraksts - tā strādā arī roboti."),

    Kopsavilkums([
        "Pierakstu ceļu ar bultiņām.",
        "Eju pa rūtiņām pēc bultiņām.",
        "Saskaitu ceļa soļus.",
    ]),

    Majas([
        "Uzraksti bultiņas ceļam no tavas istabas līdz virtuvei.",
        "Paslēp mantu un uzraksti bultiņas, kā to atrast.",
        "Uzzīmē rūtiņās savu ceļu un pieraksti to.",
    ]),
]
