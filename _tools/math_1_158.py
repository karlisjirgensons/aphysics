# -*- coding: utf-8 -*-
"""1. klase, 158. stunda: «Vai figūras ir vienādas?»

Divas figūras ir vienādas, ja vienu var uzlikt otrai un tās pilnīgi sakrīt
(drīkst pagriezt vai apgriezt). Rūtiņu lapā vienādu figūru zīmē, skaitot
rūtiņas katrā malā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Varianti, figura)

TEMA = "Vai figūras ir vienādas?"

MERKIS = ("Šodien pārliecināsimies par figūru vienādību, tās savietojot, un "
          "uzzīmēsim vienādu figūru rūtiņās.")

_L = figura([(0, 0), (3, 0), (3, 1), (1, 1), (1, 3), (0, 3)])
_L_GRIEZTS = figura([(0, 0), (1, 0), (1, 2), (3, 2), (3, 3), (0, 3)])
_L_LIELS = figura([(0, 0), (4, 0), (4, 1), (1, 1), (1, 4), (0, 4)])

SATURS = [
    Sakums("Vai šīs divas L figūras ir vienādas?",
           zimejums=_L,
           paraksts="Ja pagriež un tās sakrīt - vienādas.",
           fakti=["Vienādas - pilnīgi sakrīt.",
                  "Drīkst pagriezt vai apgriezt.",
                  "Pārbauda, izgriežot un uzliekot."]),

    Doma("Vienādas figūras",
         "Vienādām figūrām ir vienādas malas un stūri - atšķirties drīkst "
         "tikai novietojums.",
         soli=[
             "Saskaiti rūtiņas katrā malā.",
             "Salīdzini ar otru figūru.",
             "Ja visas malas sakrīt - vienādas.",
         ]),

    Varianti("Vienādas?", [
        {"jaut": "Vai šī figūra vienāda ar sākuma L?", "zim": _L_GRIEZTS,
         "opcijas": ["Jā - tikai pagriezta", "Nē"], "jaukt": False,
         "pareizi": 0, "padoms": "Malas 3, 1, 2, 2, 1, 3 rūtiņas."},
        {"jaut": "Vai šī figūra vienāda ar sākuma L?", "zim": _L_LIELS,
         "opcijas": ["Nē - lielāka", "Jā"], "jaukt": False, "pareizi": 0,
         "padoms": "Malas garākas."},
    ]),

    Ievadi("Saskaiti rūtiņas", [
        {"jaut": "Cik rūtiņu aizņem sākuma L?", "zim": _L, "atb": ["5"],
         "padoms": "3 apakšā un 2 augšā."},
        {"jaut": "Cik rūtiņu aizņem lielais L?", "zim": _L_LIELS,
         "atb": ["7"], "padoms": "4 un 3."},
    ]),

    Petijums("Uzzīmē vienādu", [
        "Uzzīmē rūtiņās jebkuru figūru.",
        "Blakus uzzīmē vienādu - skaiti rūtiņas.",
        "Izgriez abas un uzliec vienu uz otras.",
        "Vai sakrīt?",
    ], vajag="rūtiņu lapa, šķēres"),

    Pasaule("Puzle",
            Varianti("", [
                {"jaut": "Puzlē caurums L formā. Kura detaļa derēs?",
                 "zim": _L_GRIEZTS,
                 "opcijas": ["šī - pagriezta der", "neder"], "jaukt": False,
                 "pareizi": 0, "padoms": "Vienāda figūra."},
            ]),
            pavediens="speles",
            konteksts="Puzles detaļai jābūt tieši tādai kā caurumam.",
            kapec="Vienādas figūras - ieder vieta."),

    Kopsavilkums([
        "Pārbaudu vienādību, savietojot.",
        "Zinu, ka drīkst pagriezt.",
        "Zīmēju vienādu figūru rūtiņās.",
    ]),

    Majas([
        "Atrodi mājās 2 vienādas lietas.",
        "Uzzīmē rūtiņās 2 vienādas figūras dažādi pagrieztas.",
        "Salīdzini, izgriežot.",
    ]),
]
