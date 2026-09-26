# -*- coding: utf-8 -*-
"""1. klase, 152. stunda: «Kas figūrai ir svarīgs?»

Figūras būtiskās īpašības - malu un stūru skaits (un vai malas taisnas);
nebūtiskās - krāsa, lielums, novietojums. Trijstūris paliek trijstūris,
arī ja ir liels, oranžs un apgriezts.
"""

from math_saturs import (Doma, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, geometrija)

TEMA = "Kas figūrai ir svarīgs?"

MERKIS = ("Šodien noteiksim, kas figūrai ir būtisks (malu skaits) un kas nav "
          "(krāsa, lielums).")


def _fig(punkti, krasa=0):
    vardi = ["_%d" % i for i in range(len(punkti))]
    return geometrija([(v, x, y) for v, (x, y) in zip(vardi, punkti)],
                      nogriezni=[(vardi[i], vardi[(i + 1) % len(vardi)])
                                 for i in range(len(vardi))],
                      iekrasot=[(vardi, krasa)])


_TRIJ_A = _fig([(0, 0), (6, 0), (2, 4)])
_TRIJ_B = _fig([(0, 3), (3, 0), (4, 5)], 1)

SATURS = [
    Sakums("Vai abi ir trijstūri?",
           zimejums=_TRIJ_B,
           paraksts="Oranžs, apgriezts - bet 3 malas: trijstūris.",
           fakti=["Svarīgi: cik malu un stūru.",
                  "Nav svarīgi: krāsa, lielums.",
                  "Nav svarīgi: kā figūra pagriezta."]),

    Doma("Būtisks un nebūtisks",
         "Figūras vārdu nosaka malu skaits, nevis krāsa vai lielums.",
         soli=[
             "Saskaiti malas un stūrus.",
             "Pārbaudi, vai malas taisnas.",
             "Krāsu un lielumu neskaties.",
         ]),

    Varianti("Kā sauc?", [
        {"jaut": "Kā sauc šo figūru?", "zim": _TRIJ_A,
         "opcijas": ["trijstūris", "četrstūris", "aplis"], "pareizi": 0,
         "padoms": "3 malas."},
        {"jaut": "Kā sauc šo oranžo figūru?", "zim": _TRIJ_B,
         "opcijas": ["trijstūris", "oranžstūris", "četrstūris"],
         "pareizi": 0, "padoms": "Krāsa nav svarīga."},
        {"jaut": "Kā sauc šo figūru?",
         "zim": _fig([(0, 0), (2, 0), (3, 2), (1, 4), (-1, 2)], 1),
         "opcijas": ["piecstūris", "četrstūris", "sešstūris"],
         "pareizi": 0, "padoms": "5 malas."},
    ]),

    Varianti("Svarīgs vai nē?", [
        {"jaut": "Lai figūra būtu kvadrāts, svarīga ir...",
         "opcijas": ["4 vienādas malas un taisni stūri", "zila krāsa",
                     "liels izmērs"], "pareizi": 0,
         "padoms": "Krāsa nemaina figūru."},
        {"jaut": "Ja trijstūri pagriež otrādi, tas ir...",
         "opcijas": ["joprojām trijstūris", "cita figūra"],
         "jaukt": False, "pareizi": 0, "padoms": "Malas tās pašas."},
    ]),

    Pasaule("Ceļa zīmes",
            Varianti("", [
                {"jaut": "Brīdinājuma zīmes ir trijstūri - lielas un mazas. "
                         "Kas tām kopīgs?",
                 "opcijas": ["3 malas", "vienāds lielums",
                             "viena krāsa visur"], "pareizi": 0,
                 "padoms": "Forma, nevis lielums."},
            ]),
            pavediens="celojums",
            konteksts="Ceļa zīmes pazīst pēc formas.",
            kapec="Forma - būtiska īpašība."),

    Kopsavilkums([
        "Zinu, ka svarīgs ir malu skaits.",
        "Zinu, ka krāsa un lielums nav svarīgi.",
        "Pazīstu figūru jebkurā novietojumā.",
    ]),

    Majas([
        "Atrodi mājās 2 dažādas krāsas un lieluma trijstūrus.",
        "Kas tiem kopīgs?",
        "Uzzīmē apgrieztu kvadrātu.",
    ]),
]
