# -*- coding: utf-8 -*-
"""1. klase, 50. stunda: «Kā pārlocīt uz pusēm?»

Lokot kvadrātu un riņķi, iegūst divas un četras vienādas daļas. Kvadrātu
var pārlocīt uz pusēm vairākos veidos (vidū vai pa diagonāli); riņķi -
pa jebkuru diametru.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Slidnis, Varianti, geometrija)

TEMA = "Kā pārlocīt uz pusēm?"

MERKIS = ("Šodien pārlocīsim kvadrātu un riņķi divās un četrās vienādās "
          "daļās.")

_KV = [("_A", 0, 0), ("_B", 4, 0), ("_C", 4, 4), ("_D", 0, 4),
       ("_M", 2, 0), ("_N", 2, 4), ("_K", 0, 2), ("_L", 4, 2)]
_KV_MALAS = [("_A", "_B"), ("_B", "_C"), ("_C", "_D"), ("_D", "_A")]


def _kvadrats(loki):
    return geometrija(_KV, nogriezni=_KV_MALAS, slepti=loki,
                      iekrasot=[(["_A", "_B", "_C", "_D"], 0)])


def _rinkis(loki):
    punkti = [("_O", 0, 0), ("_P", -4, 0), ("_Q", 4, 0), ("_R", 0, -4),
              ("_S", 0, 4)]
    return geometrija(punkti, slepti=loki, rinki=[("_O", 4)])


SATURS = [
    Sakums("Kā salocīt salveti tieši uz pusēm?",
           zimejums=_kvadrats([("_M", "_N")]),
           paraksts="Pa vidu - divas vienādas daļas.",
           fakti=["Uz pusēm - divas vienādas daļas.",
                  "Pārloki vēlreiz - četras vienādas daļas.",
                  "Kvadrātu var pārlocīt dažādi."]),

    Slidnis("Locījumi", [
        {"v": "2", "teksts": "Kvadrāts pa vidu - 2 daļas",
         "zim": _kvadrats([("_M", "_N")])},
        {"v": "2", "teksts": "Kvadrāts pa diagonāli - 2 trijstūri",
         "zim": _kvadrats([("_A", "_C")])},
        {"v": "4", "teksts": "Divreiz - 4 kvadrātiņi",
         "zim": _kvadrats([("_M", "_N"), ("_K", "_L")])},
        {"v": "2", "teksts": "Riņķis uz pusēm",
         "zim": _rinkis([("_P", "_Q")])},
        {"v": "4", "teksts": "Riņķis divreiz - 4 daļas",
         "zim": _rinkis([("_P", "_Q"), ("_R", "_S")])},
    ]),

    Doma("Vienādas daļas",
         "Uz pusēm - ja abas daļas pilnīgi sakrīt.",
         soli=[
             "Pārloki tā, lai malas sakrīt.",
             "Nogludini locījumu.",
             "Atloki - locījuma līnija dala figūru.",
             "Pārloki vēlreiz šķērsām - 4 daļas.",
         ]),

    Ievadi("Cik daļu?", [
        {"jaut": "Cik daļu?", "zim": _kvadrats([("_A", "_C")]),
         "atb": ["2"], "padoms": "Saskaiti daļas."},
        {"jaut": "Cik daļu?", "zim": _rinkis([("_P", "_Q"), ("_R", "_S")]),
         "atb": ["4"], "padoms": "Saskaiti daļas."},
        {"jaut": "Pārloka divreiz. Cik daļu būs?", "atb": ["4"],
         "padoms": "Katra puse vēl uz pusēm."},
    ]),

    Varianti("Vai daļas vienādas?", [
        {"jaut": "Kvadrātu pārloka tā, ka malas nesakrīt. Vai daļas "
                 "vienādas?", "opcijas": ["Nē", "Jā"], "jaukt": False,
         "pareizi": 0, "padoms": "Jāsakrīt malām."},
        {"jaut": "Cik veidos kvadrātu var pārlocīt uz pusēm?",
         "opcijas": ["4", "1", "2"], "pareizi": 0,
         "padoms": "Divi pa vidu, divi pa diagonālēm."},
    ]),

    Petijums("Loki pats", [
        "Izgriez papīra kvadrātu un riņķi.",
        "Pārloki katru uz pusēm.",
        "Pārloki vēlreiz - cik daļu?",
        "Atrodi vēl vienu veidu, kā pārlocīt kvadrātu uz pusēm.",
    ], vajag="papīrs, šķēres"),

    Pasaule("Pankūka četriem",
            Ievadi("", [
                {"jaut": "Apaļa pankūka jāsadala 4 draugiem vienādi. Cik "
                         "reizes jāpārgriež pa vidu?", "atb": ["2"],
                 "padoms": "Vienreiz - 2 daļas, divreiz - 4."},
            ]),
            pavediens="virtuve",
            konteksts="Pankūka ir riņķis - to dala kā papīra riņķi.",
            kapec="Vienādas daļas - godīgi visiem."),

    Kopsavilkums([
        "Loku kvadrātu un riņķi uz pusēm.",
        "Iegūstu 2 un 4 vienādas daļas.",
        "Zinu, ka kvadrātu var locīt vairākos veidos.",
    ]),

    Majas([
        "Salaiko salveti 4 vienādās daļās.",
        "Sagriez maizītes šķēli 4 vienādās daļās dažādi.",
        "Vai visas daļas bija vienādas?",
    ]),
]
