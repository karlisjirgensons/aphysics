# -*- coding: utf-8 -*-
"""1. klase, 51. stunda: «Vai figūra ir simetriska?»

Figūra ir simetriska, ja to var pārlocīt tā, ka abas puses pilnīgi sakrīt;
locījuma līnija ir simetrijas līnija. Mājiņa, sirds un taurenis ir
simetriski, burts F - nav.
"""

from math_saturs import (Doma, Kopsavilkums, Majas, Pasaule, Petijums,
                         Sakums, Varianti, geometrija)

TEMA = "Vai figūra ir simetriska?"

MERKIS = ("Šodien ar locīšanu pārbaudīsim, vai figūra ir simetriska, un "
          "parādīsim locījuma līniju.")


def _fig(punkti, ass=None):
    """Figūra no punktiem; ass - punktēta locījuma līnija (x vērtība)."""
    vardi = ["_%d" % i for i in range(len(punkti))]
    p = [(v, x, y) for v, (x, y) in zip(vardi, punkti)]
    slepti = []
    if ass is not None:
        ys = [y for _, y in punkti]
        p += [("_a", ass, min(ys) - 0.6), ("_b", ass, max(ys) + 0.6)]
        slepti = [("_a", "_b")]
    return geometrija(p, nogriezni=[(vardi[i], vardi[(i + 1) % len(vardi)])
                                    for i in range(len(vardi))],
                      iekrasot=[(vardi, 0)], slepti=slepti)


_MAJA = [(0, 0), (4, 0), (4, 3), (2, 5), (0, 3)]
_KARODZ = [(0, 0), (1, 0), (1, 3), (4, 4), (1, 5), (0, 5)]
_BULTA = [(0, 1), (3, 1), (3, 0), (5, 2), (3, 4), (3, 3), (0, 3)]
_ZVAIGZNE_T = [(0, 0), (2, 1), (4, 0), (3, 2), (4, 4), (2, 3), (0, 4),
               (1, 2)]

SATURS = [
    Sakums("Pārloki mājiņu pa vidu - vai puses sakrīt?",
           zimejums=_fig(_MAJA, ass=2),
           paraksts="Puses sakrīt - mājiņa ir simetriska.",
           fakti=["Simetriska - abas puses kā spoguļattēls.",
                  "Locījuma līnija - simetrijas līnija.",
                  "Pārbauda, pārlokot."]),

    Doma("Pārbaude ar locīšanu",
         "Ja pēc pārlocīšanas nekas neizspraucas, figūra ir simetriska.",
         soli=[
             "Izgriez figūru.",
             "Mēģini pārlocīt tā, lai puses sakrīt.",
             "Sakrīt - simetriska; locījums - simetrijas līnija.",
             "Nekādi nesakrīt - nav simetriska.",
         ]),

    Varianti("Simetriska?", [
        {"jaut": "Vai figūra ir simetriska?", "zim": _fig(_MAJA),
         "opcijas": ["Jā", "Nē"], "jaukt": False, "pareizi": 0,
         "padoms": "Pārloki pa vidu."},
        {"jaut": "Vai figūra ir simetriska?", "zim": _fig(_KARODZ),
         "opcijas": ["Jā", "Nē"], "jaukt": False, "pareizi": 1,
         "padoms": "Karodziņš ir tikai vienā pusē."},
        {"jaut": "Vai bulta ir simetriska?", "zim": _fig(_BULTA),
         "opcijas": ["Jā", "Nē"], "jaukt": False, "pareizi": 0,
         "padoms": "Loki pa garumu - augša uz apakšu."},
        {"jaut": "Vai figūra ir simetriska?", "zim": _fig(_ZVAIGZNE_T),
         "opcijas": ["Jā", "Nē"], "jaukt": False, "pareizi": 0,
         "padoms": "Pa vidu uz augšu."},
    ]),

    Varianti("Burti", [
        {"jaut": "Kurš burts ir simetrisks?",
         "opcijas": ["A", "F", "R"], "pareizi": 0,
         "padoms": "Pārloki pa vidu uz augšu."},
        {"jaut": "Kurš burts nav simetrisks?",
         "opcijas": ["G", "M", "T"], "pareizi": 0,
         "padoms": "M un T pārlokās pa vidu."},
    ]),

    Petijums("Izgriez un pārbaudi", [
        "Izgriez sirdi, trijstūri un sava vārda pirmo burtu.",
        "Mēģini katru pārlocīt tā, lai puses sakrīt.",
        "Uzvelc locījuma līniju ar zīmuli.",
        "Kuras figūras ir simetriskas?",
    ], vajag="papīrs, šķēres, zīmulis"),

    Pasaule("Tauriņa spārni",
            Varianti("", [
                {"jaut": "Kur tauriņam ir simetrijas līnija?",
                 "opcijas": ["pa ķermeni vidū", "pa spārna malu",
                             "tam nav"], "pareizi": 0,
                 "padoms": "Abi spārni vienādi."},
            ]),
            pavediens="daba",
            konteksts="Daudzi dzīvnieki un augi ir simetriski.",
            kapec="Simetriju var atrast visur ap mums."),

    Kopsavilkums([
        "Pārbaudu simetriju, pārlokot.",
        "Parādu simetrijas līniju.",
        "Atšķiru simetriskas un nesimetriskas figūras.",
    ]),

    Majas([
        "Atrodi mājās 3 simetriskas lietas.",
        "Uzraksti lielajiem burtiem savu vārdu - kuri burti simetriski?",
        "Paskaties spogulī - vai tava seja ir simetriska?",
    ]),
]
