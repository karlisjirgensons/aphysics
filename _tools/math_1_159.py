# -*- coding: utf-8 -*-
"""1. klase, 159. stunda: «Cik locījuma līniju ir kvadrātam?»

Kvadrātam ir 4 simetrijas līnijas (2 pa vidu, 2 pa diagonālēm),
taisnstūrim - 2, vienādmalu trijstūrim - 3, riņķim - bezgalīgi daudz.
Tās atrod, locot.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Slidnis, Varianti, geometrija)

TEMA = "Cik locījuma līniju ir kvadrātam?"

MERKIS = ("Šodien atradīsim figūrai visas simetrijas līnijas un "
          "pārliecināsimies, ka to var būt vairākas.")

_KP = [("_A", 0, 0), ("_B", 4, 0), ("_C", 4, 4), ("_D", 0, 4),
       ("_M", 2, 0), ("_N", 2, 4), ("_K", 0, 2), ("_L", 4, 2)]
_KM = [("_A", "_B"), ("_B", "_C"), ("_C", "_D"), ("_D", "_A")]


def _kv(loki):
    return geometrija(_KP, nogriezni=_KM, slepti=loki,
                      iekrasot=[(["_A", "_B", "_C", "_D"], 0)])


def _ts(loki):
    p = [("_A", 0, 0), ("_B", 6, 0), ("_C", 6, 3), ("_D", 0, 3),
         ("_M", 3, 0), ("_N", 3, 3), ("_K", 0, 1.5), ("_L", 6, 1.5)]
    return geometrija(p, nogriezni=_KM, slepti=loki,
                      iekrasot=[(["_A", "_B", "_C", "_D"], 0)])


SATURS = [
    Sakums("Cik veidos kvadrātu var pārlocīt, lai puses sakrīt?",
           zimejums=_kv([("_M", "_N"), ("_K", "_L"), ("_A", "_C"),
                         ("_B", "_D")]),
           paraksts="4 locījuma līnijas: 2 pa vidu un 2 pa diagonālēm.",
           fakti=["Kvadrātam - 4 simetrijas līnijas.",
                  "Taisnstūrim - tikai 2.",
                  "Riņķim - ļoti daudz."]),

    Slidnis("Kvadrāta locījumi", [
        {"v": "1", "teksts": "Pa vidu stateniski",
         "zim": _kv([("_M", "_N")])},
        {"v": "2", "teksts": "Pa vidu guļus", "zim": _kv([("_K", "_L")])},
        {"v": "3", "teksts": "Pa diagonāli", "zim": _kv([("_A", "_C")])},
        {"v": "4", "teksts": "Pa otru diagonāli",
         "zim": _kv([("_B", "_D")])},
    ]),

    Doma("Visas simetrijas līnijas",
         "Meklē visus veidus, kā pārlocīt, lai puses sakrīt.",
         soli=[
             "Pamēģini pa vidu stateniski un guļus.",
             "Pamēģini pa diagonālēm.",
             "Saskaiti, cik līniju derēja.",
         ]),

    Ievadi("Cik līniju?", [
        {"jaut": "Cik simetrijas līniju taisnstūrim?",
         "zim": _ts([("_M", "_N"), ("_K", "_L")]), "atb": ["2"],
         "padoms": "Diagonāles neder."},
        {"jaut": "Cik simetrijas līniju kvadrātam?", "atb": ["4"],
         "padoms": "2 + 2."},
        {"jaut": "Cik simetrijas līniju vienādmalu trijstūrim?",
         "atb": ["3"], "padoms": "No katra stūra."},
    ]),

    Varianti("Vai tā ir simetrijas līnija?", [
        {"jaut": "Taisnstūris, pārlocīts pa diagonāli.",
         "zim": _ts([("_A", "_C")]),
         "opcijas": ["Nē - puses nesakrīt", "Jā"], "jaukt": False,
         "pareizi": 0, "padoms": "Pamēģini ar papīru!"},
    ]),

    Petijums("Loki un skaiti", [
        "Izgriez kvadrātu, taisnstūri un riņķi.",
        "Atrodi katrai visas locījuma līnijas.",
        "Uzvelc tās ar zīmuli.",
        "Ieraksti tabulā: figūra - līniju skaits.",
    ], vajag="papīrs, šķēres, zīmulis"),

    Pasaule("Salvetes locīšana",
            Ievadi("", [
                {"jaut": "Kvadrātveida salveti var salocīt uz pusēm cik "
                         "dažādos veidos?", "atb": ["4"],
                 "padoms": "Tik, cik simetrijas līniju."},
            ]),
            pavediens="virtuve",
            konteksts="Svētku galdam salvetes loka dažādi.",
            kapec="Katra simetrijas līnija - cits locījums."),

    Kopsavilkums([
        "Atrodu visas simetrijas līnijas.",
        "Zinu: kvadrātam 4, taisnstūrim 2.",
        "Pārbaudu, locot.",
    ]),

    Majas([
        "Cik locījuma līniju ir tavai salvetei?",
        "Atrodi figūru ar tieši 1 simetrijas līniju.",
        "Uzzīmē to.",
    ]),
]
