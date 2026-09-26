# -*- coding: utf-8 -*-
"""1. klase, 37. stunda: «Vai pieraksts ir patiess?»

Vienādība ir patiesa, ja abās «=» pusēs ir viens un tas pats skaitlis.
Šaubu gadījumā to modelē ar ripiņām. «=» nav «atbilde nāk», bet «tikpat».
"""

from math_saturs import (Doma, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, bildes)

TEMA = "Vai pieraksts ir patiess?"

MERKIS = ("Šodien noteiksim, vai vienādība ir patiesa vai aplama, un "
          "paskaidrosim, kāpēc.")


def _pa(jaut, patiess, padoms, zim=None):
    k = {"jaut": jaut, "opcijas": ["Patiess", "Aplams"], "jaukt": False,
         "pareizi": 0 if patiess else 1, "padoms": padoms}
    if zim:
        k["zim"] = zim
    return k


SATURS = [
    Sakums("3 + 4 = 8 - vai tā ir taisnība?",
           zimejums=bildes([[("ripina", 3), ("ripina*", 4)]]),
           paraksts="Ripiņu ir 7, nevis 8 - pieraksts ir aplams.",
           fakti=["«=» nozīmē: abās pusēs tikpat.",
                  "Ja abās pusēs vienāds skaitlis - patiess.",
                  "Ja nē - aplams."]),

    Doma("Pārbaudi abas puses",
         "Izrēķini katru pusi atsevišķi un salīdzini.",
         soli=[
             "Izrēķini kreiso pusi.",
             "Izrēķini labo pusi.",
             "Vienādi? - patiess. Dažādi? - aplams.",
             "Šaubies? Noliec ripiņas.",
         ]),

    Varianti("Patiess vai aplams?", [
        _pa("3 + 4 = 7", True, "3 un 4 ir 7."),
        _pa("5 + 2 = 8", False, "5 un 2 ir 7."),
        _pa("9 − 3 = 6", True, "3 + 6 = 9."),
        _pa("6 − 1 = 7", False, "Atņemot kļūst mazāk."),
        _pa("10 = 4 + 6", True, "Desmita draugi."),
        _pa("2 + 2 = 5", False, "Divreiz 2 ir 4."),
    ], pamats=4),

    Varianti("Pārbaudi ar zīmējumu", [
        _pa("4 + 2 = 6", True, "Saskaiti ripiņas.",
            bildes([[("ripina", 4), ("ripina*", 2)]])),
        _pa("5 + 3 = 9", False, "Saskaiti ripiņas.",
            bildes([[("ripina", 5), ("ripina*", 3)]])),
    ]),

    Pasaule("Kase veikalā",
            Varianti("", [
                _pa("Maize maksā 2 €, piens 3 €. Čekā: 2 + 3 = 6. Vai "
                    "pareizi?", False, "2 + 3 = 5."),
                _pa("Ābols 1 €, bumbieris 1 €. Čekā: 1 + 1 = 2.", True,
                    "1 un 1 ir 2."),
            ]),
            pavediens="veikals",
            konteksts="Pārbaudi čeku: vai kase saskaitīja pareizi?",
            kapec="Kļūdu čekā pamana tas, kurš pārbauda."),

    Kopsavilkums([
        "Zinu, ka «=» nozīmē tikpat.",
        "Pārbaudu, vai vienādība ir patiesa.",
        "Paskaidroju ar ripiņām.",
    ]),

    Majas([
        "Uzraksti 3 patiesas un 1 aplamu vienādību. Lai kāds atrod aplamo.",
        "Pārbaudi ar karotēm: 4 + 3 = 7?",
        "Paskaidro mājiniekam, ko nozīmē «=».",
    ]),
]
