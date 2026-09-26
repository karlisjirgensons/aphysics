# -*- coding: utf-8 -*-
"""1. klase, 157. stunda: «Kādas figūras rodas?»

Daudzstūri pārgriež ar taisnu līniju un nosauc jaunās figūras: kvadrāts
pa diagonāli - divi trijstūri; taisnstūris pa vidu - divi taisnstūri;
trijstūris no virsotnes - divi trijstūri, šķērsām - trijstūris un
četrstūris.
"""

from math_saturs import (Doma, Kopsavilkums, Majas, Pasaule, Petijums,
                         Sakums, Varianti, geometrija)

TEMA = "Kādas figūras rodas?"

MERKIS = ("Šodien sadalīsim daudzstūri ar taisnu līniju un nosauksim, kādas "
          "figūras izveidojas.")


def _griez(punkti, dalas):
    """Figūra, sagriezta daļās: katra daļa savā krāsā."""
    return geometrija([("_" + k, x, y) for k, (x, y) in punkti.items()],
                      nogriezni=[("_" + d[i], "_" + d[(i + 1) % len(d)])
                                 for d in dalas for i in range(len(d))],
                      iekrasot=[(["_" + c for c in d], i % 2)
                                for i, d in enumerate(dalas)])


_KV = _griez({"A": (0, 0), "B": (4, 0), "C": (4, 4), "D": (0, 4)},
             ["ABC", "ACD"])
_TRIJ = _griez({"A": (0, 0), "B": (6, 0), "C": (3, 5), "M": (1.5, 2.5),
                "N": (4.5, 2.5)}, ["MNC", "ABNM"])
_TRIJ2 = _griez({"A": (0, 0), "B": (6, 0), "C": (3, 5), "M": (3, 0)},
                ["AMC", "MBC"])

SATURS = [
    Sakums("Pārgriez kvadrātu pa diagonāli - kas iznāk?",
           zimejums=_KV,
           paraksts="Divi trijstūri.",
           fakti=["Taisns griezums rada jaunas figūras.",
                  "Saskaiti katras daļas stūrus.",
                  "Nosauc figūras."]),

    Doma("Griezums",
         "Jaunās figūras nosauc pēc stūru skaita.",
         soli=[
             "Iedomājies vai novelc griezuma līniju.",
             "Aplūko katru daļu atsevišķi.",
             "Saskaiti stūrus un nosauc.",
         ]),

    Varianti("Kas iznāca?", [
        {"jaut": "Kādas figūras?", "zim": _KV,
         "opcijas": ["2 trijstūri", "2 kvadrāti", "trijstūris un kvadrāts"],
         "pareizi": 0, "padoms": "Katrā daļā 3 stūri."},
        {"jaut": "Kādas figūras?", "zim": _TRIJ,
         "opcijas": ["trijstūris un četrstūris", "2 trijstūri",
                     "2 četrstūri"], "pareizi": 0,
         "padoms": "Augšā 3 stūri, apakšā 4."},
        {"jaut": "Kādas figūras?", "zim": _TRIJ2,
         "opcijas": ["2 trijstūri", "trijstūris un četrstūris",
                     "2 kvadrāti"], "pareizi": 0,
         "padoms": "Griezums no virsotnes."},
    ]),

    Petijums("Griez un nosauc", [
        "Izgriez papīra kvadrātu, taisnstūri un trijstūri.",
        "Katru pārgriez ar vienu taisnu griezumu.",
        "Nosauc jaunās figūras.",
        "Vai var iegūt piecstūri? Pamēģini!",
    ], vajag="papīrs, šķēres, lineāls"),

    Pasaule("Sviestmaizes",
            Varianti("", [
                {"jaut": "Kvadrātveida sviestmaizi pārgriež pa diagonāli. "
                         "Kādas figūras uz šķīvja?",
                 "opcijas": ["trijstūri", "apļi", "piecstūri"],
                 "pareizi": 0, "padoms": "Diagonāle - trijstūri."},
            ]),
            pavediens="virtuve",
            konteksts="Svētkiem sviestmaizes griež skaisti.",
            kapec="Griezums rada jaunas figūras."),

    Kopsavilkums([
        "Sadalu figūru ar taisnu līniju.",
        "Nosaucu jaunās figūras.",
        "Saskaitu to stūrus.",
    ]),

    Majas([
        "Pārgriez papīra taisnstūri dažādi.",
        "Kādas figūras ieguvi?",
        "Uzzīmē tās burtnīcā.",
    ]),
]
