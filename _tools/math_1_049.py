# -*- coding: utf-8 -*-
"""1. klase, 49. stunda: «Kuras malas ir vienādas?»

Taisnstūrim pretējās malas ir vienāda garuma - to pierāda, pārlokot: malas
sakrīt. Kvadrātam vienādas ir visas četras malas.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Varianti, geometrija)

TEMA = "Kuras malas ir vienādas?"

MERKIS = ("Šodien ar locīšanu pārbaudīsim, kuras taisnstūra un kvadrāta "
          "malas ir vienādas.")


def _ts(a, b, malas):
    return geometrija([("A", 0, 0), ("B", a, 0), ("C", a, b), ("D", 0, b)],
                      nogriezni=["AB", "BC", "CD", "DA"],
                      malas=malas, iekrasot=[("ABCD", 0)])


_TS = _ts(6, 3, [("AB", "6 cm"), ("BC", "3 cm")])

SATURS = [
    Sakums("Pārloki taisnstūri - kas sakrīt?",
           zimejums=_TS,
           paraksts="Augšējā mala sakrīt ar apakšējo: abas 6 cm.",
           fakti=["Taisnstūrim pretējās malas ir vienādas.",
                  "Kvadrātam visas 4 malas vienādas.",
                  "Pārbauda, pārlokot vai izmērot."]),

    Doma("Pretējās malas",
         "Pārlokot taisnstūri uz pusēm, pretējās malas sakrīt - tās ir "
         "vienāda garuma.",
         soli=[
             "Pārloki tā, lai augšējā mala uzguļ uz apakšējās.",
             "Tās sakrīt - vienādas.",
             "Pārloki otrādi - sakrīt sānu malas.",
         ]),

    Ievadi("Cik gara mala?", [
        {"jaut": "Cik cm ir augšējā mala CD?", "zim": _TS, "atb": ["6"],
         "padoms": "Pretī AB."},
        {"jaut": "Cik cm ir kreisā mala AD?", "zim": _TS, "atb": ["3"],
         "padoms": "Pretī BC."},
        {"jaut": "Kvadrāta mala 4 cm. Cik cm ir katra cita mala?",
         "zim": _ts(4, 4, [("AB", "4 cm")]), "atb": ["4"],
         "padoms": "Visas vienādas."},
        {"jaut": "Taisnstūrim 2 malas pa 5 cm, 2 malas pa 2 cm. Cik cm "
                 "visas kopā?", "atb": ["14"], "padoms": "5 + 5 + 2 + 2."},
    ]),

    Varianti("Taisnstūris vai kvadrāts?", [
        {"jaut": "Visas malas 3 cm, stūri taisni.",
         "opcijas": ["kvadrāts", "taisnstūris, bet ne kvadrāts"],
         "jaukt": False, "pareizi": 0, "padoms": "Visas vienādas."},
        {"jaut": "Malas 5 cm, 2 cm, 5 cm, 2 cm, stūri taisni.",
         "opcijas": ["kvadrāts", "taisnstūris, bet ne kvadrāts"],
         "jaukt": False, "pareizi": 1, "padoms": "Ne visas vienādas."},
    ]),

    Petijums("Loki un mēri", [
        "Izgriez papīra taisnstūri.",
        "Pārloki: augšā uz leju. Vai malas sakrīt?",
        "Pārloki: pa kreisi uz labo. Vai sakrīt?",
        "Izmēri visas 4 malas ar lineālu.",
    ], vajag="papīrs, šķēres, lineāls"),

    Pasaule("Rāmītis bildei",
            Ievadi("", [
                {"jaut": "Rāmītim jāizgriež 4 līstes: 2 pa 8 cm un 2 pa 6 cm. "
                         "Cik cm līstes kopā?", "atb": ["28"],
                 "padoms": "8 + 8 + 6 + 6."},
            ]),
            pavediens="maja",
            konteksts="Taisnstūra rāmītim pretējās līstes ir vienādas.",
            kapec="Zinot vienu malu, zini arī pretējo."),

    Kopsavilkums([
        "Zinu, ka taisnstūrim pretējās malas ir vienādas.",
        "Zinu, ka kvadrātam visas malas ir vienādas.",
        "Pārbaudu, pārlokot vai izmērot.",
    ]),

    Majas([
        "Izmēri grāmatas vāku: vai pretējās malas vienādas?",
        "Pārloki salveti un pārbaudi malas.",
        "Atrodi mājās kvadrātu.",
    ]),
]
