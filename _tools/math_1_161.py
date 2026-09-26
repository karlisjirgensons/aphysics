# -*- coding: utf-8 -*-
"""1. klase, 161. stunda: «Kā uzzīmēt otru pusi?»

Rūtiņu lapā dota puse figūras un simetrijas līnija. Otru pusi zīmē,
skaitot rūtiņas no līnijas: katrs punkts ir tikpat tālu otrā pusē.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Slidnis, Varianti, geometrija)

TEMA = "Kā uzzīmēt otru pusi?"

MERKIS = ("Šodien uzzīmēsim rūtiņu lapā simetriskas figūras otru pusi pēc "
          "dotās.")

_PUSE = [(0, 0), (2, 0), (2, 2), (3, 3), (1, 5), (0, 5)]


def _zim(pilna):
    punkti = list(_PUSE)
    if pilna:
        punkti = punkti + [(-x, y) for x, y in reversed(punkti)]
    vardi = ["_%d" % i for i in range(len(punkti))]
    p = [(v, x, y) for v, (x, y) in zip(vardi, punkti)]
    p += [("_a", 0, -0.7), ("_b", 0, 5.7)]
    nogr = [(vardi[i], vardi[i + 1]) for i in range(len(vardi) - 1)]
    if pilna:
        nogr.append((vardi[-1], vardi[0]))
    return geometrija(p, nogriezni=nogr, slepti=[("_a", "_b")],
                      iekrasot=[(vardi, 0)] if pilna else [])


SATURS = [
    Sakums("Puse figūras - kā uzzīmēt otru?",
           zimejums=_zim(False),
           paraksts="Katrs stūris - tikpat rūtiņu otrā pusē līnijai.",
           fakti=["Simetrijas līnija ir kā spogulis.",
                  "Skaiti rūtiņas no līnijas.",
                  "Otrā pusē - tikpat tālu."]),

    Slidnis("Spoguļojam", [
        {"v": "puse", "teksts": "Dotā puse", "zim": _zim(False)},
        {"v": "visa", "teksts": "Otra puse spogulī", "zim": _zim(True)},
    ]),

    Doma("Rūtiņu spogulis",
         "Punkts 2 rūtiņas pa labi no līnijas - otrā pusē 2 rūtiņas pa "
         "kreisi.",
         soli=[
             "Atrodi stūri dotajā pusē.",
             "Saskaiti rūtiņas līdz līnijai.",
             "Tikpat rūtiņu otrā pusē - atzīmē punktu.",
             "Savieno punktus.",
         ]),

    Ievadi("Cik rūtiņu?", [
        {"jaut": "Stūris ir 3 rūtiņas pa labi no līnijas. Cik rūtiņas pa "
                 "kreisi būs spoguļstūris?", "atb": ["3"],
         "padoms": "Tikpat."},
        {"jaut": "Cik stūru būs visai figūrai, ja pusei ir 4 stūri ārpus "
                 "līnijas?", "atb": ["8"], "padoms": "4 + 4."},
    ]),

    Varianti("Pareizi?", [
        {"jaut": "Maija otrā pusē uzzīmēja stūri 2 rūtiņas no līnijas, bet "
                 "dotajā tas ir 3 rūtiņas.",
         "opcijas": ["kļūda", "pareizi"], "jaukt": False, "pareizi": 0,
         "padoms": "Jābūt tikpat."},
    ]),

    Petijums("Zīmē pats", [
        "Novelc rūtiņu lapā stateniski līniju.",
        "Pa labi uzzīmē pusi mājiņas.",
        "Pa kreisi uzzīmē otru pusi, skaitot rūtiņas.",
        "Pārbaudi ar spoguli uz līnijas.",
    ], vajag="rūtiņu burtnīca, spogulis"),

    Pasaule("Kartīte draugam",
            Varianti("", [
                {"jaut": "Kartītei vajag simetrisku sirdi. Kā zīmēt ātrāk?",
                 "opcijas": ["pusi un otru pa rūtiņām",
                             "visu no brīvas rokas"], "jaukt": False,
                 "pareizi": 0, "padoms": "Rūtiņas palīdz."},
            ]),
            pavediens="skola",
            konteksts="Klase gatavo kartītes.",
            kapec="Skaitot rūtiņas, puses sanāk vienādas."),

    Kopsavilkums([
        "Zīmēju otru pusi pēc dotās.",
        "Skaitu rūtiņas no simetrijas līnijas.",
        "Pārbaudu ar spoguli.",
    ]),

    Majas([
        "Uzzīmē pusi tauriņa un palūdz mājiniekam pabeigt.",
        "Pārbaudi ar spoguli.",
        "Izkrāso simetriski.",
    ]),
]
