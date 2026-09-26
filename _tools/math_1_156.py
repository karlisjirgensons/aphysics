# -*- coding: utf-8 -*-
"""1. klase, 156. stunda: «Kā sadalīt vienādās daļās?»

Taisnstūri un riņķi sadala divās un četrās vienādās daļās dažādi:
taisnstūri - pa vidu garumā, platumā vai pa diagonāli; riņķi - pa
diametriem. Salīdzina risinājumus: vai daļas tiešām vienādas?
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Slidnis, Varianti, geometrija)

TEMA = "Kā sadalīt vienādās daļās?"

MERKIS = ("Šodien sadalīsim taisnstūri un riņķi divās un četrās vienādās "
          "daļās un salīdzināsim risinājumus.")

_P = [("_A", 0, 0), ("_B", 6, 0), ("_C", 6, 4), ("_D", 0, 4),
      ("_M", 3, 0), ("_N", 3, 4), ("_K", 0, 2), ("_L", 6, 2),
      ("_X", 2, 0), ("_Y", 2, 4)]
_MALAS = [("_A", "_B"), ("_B", "_C"), ("_C", "_D"), ("_D", "_A")]


def _ts(linijas):
    return geometrija(_P, nogriezni=_MALAS + linijas,
                      iekrasot=[(["_A", "_B", "_C", "_D"], 0)])


def _r(linijas):
    return geometrija([("_O", 0, 0), ("_P", -4, 0), ("_Q", 4, 0),
                       ("_R", 0, -4), ("_S", 0, 4)],
                      nogriezni=linijas, rinki=[("_O", 4)])


SATURS = [
    Sakums("Kā taisnstūri sadalīt 2 vienādās daļās?",
           zimejums=_ts([("_M", "_N")]),
           paraksts="Pa vidu - divi vienādi taisnstūri.",
           fakti=["Vienādas daļas - sakrīt, ja pārloka.",
                  "Var dalīt dažādos veidos.",
                  "Pārbaudi, pārlokot."]),

    Slidnis("Dažādi veidi", [
        {"v": "2", "teksts": "Pa vidu stateniski", "zim": _ts([("_M", "_N")])},
        {"v": "2", "teksts": "Pa vidu guļus", "zim": _ts([("_K", "_L")])},
        {"v": "2", "teksts": "Pa diagonāli", "zim": _ts([("_A", "_C")])},
        {"v": "4", "teksts": "Abas vidus līnijas",
         "zim": _ts([("_M", "_N"), ("_K", "_L")])},
        {"v": "4", "teksts": "Riņķis pa diametriem",
         "zim": _r([("_P", "_Q"), ("_R", "_S")])},
    ]),

    Doma("Vienādas daļas",
         "Daļas ir vienādas, ja vienu var uzlikt otrai un tās sakrīt.",
         soli=[
             "Atrodi figūras vidu.",
             "Velc līniju caur vidu.",
             "Pārbaudi, pārlokot vai izgriežot.",
         ]),

    Varianti("Vai vienādas?", [
        {"jaut": "Vai daļas vienādas?", "zim": _ts([("_X", "_Y")]),
         "opcijas": ["Nē", "Jā"], "jaukt": False, "pareizi": 0,
         "padoms": "Līnija nav vidū."},
        {"jaut": "Vai daļas vienādas?", "zim": _ts([("_A", "_C")]),
         "opcijas": ["Jā", "Nē"], "jaukt": False, "pareizi": 0,
         "padoms": "Divi vienādi trijstūri."},
    ]),

    Ievadi("Cik daļu?", [
        {"jaut": "Cik daļu?", "zim": _ts([("_M", "_N"), ("_K", "_L")]),
         "atb": ["4"], "padoms": "Saskaiti."},
        {"jaut": "Cik daļu?", "zim": _r([("_P", "_Q")]), "atb": ["2"],
         "padoms": "Saskaiti."},
    ]),

    Petijums("Dali un salīdzini", [
        "Izgriez 3 vienādus papīra taisnstūrus.",
        "Katru sadali 2 vienādās daļās citādi.",
        "Pārbaudi, izgriežot un uzliekot daļas vienu uz otras.",
        "Salīdzini ar klasesbiedru veidiem.",
    ], vajag="papīrs, šķēres, lineāls"),

    Pasaule("Šokolādes tāfelīte",
            Varianti("", [
                {"jaut": "Tāfelīti jāsadala 4 draugiem vienādi. Kā?",
                 "zim": _ts([("_M", "_N"), ("_K", "_L")]),
                 "opcijas": ["pa abām vidus līnijām", "pa vienai malai",
                             "kā sanāk"], "pareizi": 0,
                 "padoms": "4 vienādas daļas."},
            ]),
            pavediens="virtuve",
            konteksts="Draugi dala šokolādi.",
            kapec="Vienādas daļas - godīgi."),

    Kopsavilkums([
        "Dalu taisnstūri un riņķi 2 un 4 vienādās daļās.",
        "Atrodu vairākus veidus.",
        "Pārbaudu, vai daļas vienādas.",
    ]),

    Majas([
        "Sagriez maizītes šķēli 4 vienādās daļās 2 veidos.",
        "Sadali papīra riņķi 4 daļās.",
        "Vai visas daļas vienādas?",
    ]),
]
