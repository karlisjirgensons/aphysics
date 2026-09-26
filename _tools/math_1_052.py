# -*- coding: utf-8 -*-
"""1. klase, 52. stunda: «Kā izgriezt simetrisku rotājumu?»

Simetrisku figūru izgriež, pārlokot papīru un griežot tikai pusi pie
locījuma. Atlokot abas puses vienmēr sakrīt. Rezultātu pārbauda ar
locīšanu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Slidnis, Varianti, geometrija)

TEMA = "Kā izgriezt simetrisku rotājumu?"

MERKIS = ("Šodien izgriezīsim simetrisku rotājumu no pārlocīta papīra un "
          "pārbaudīsim to.")


def _puse(punkti, pilna):
    """Puse figūras pie locījuma (x = 0) vai visa figūra ar spoguļpusi."""
    if pilna:
        punkti = punkti + [(-x, y) for x, y in reversed(punkti)]
    vardi = ["_%d" % i for i in range(len(punkti))]
    ys = [y for _, y in punkti]
    p = [(v, x, y) for v, (x, y) in zip(vardi, punkti)]
    p += [("_a", 0, min(ys) - 0.6), ("_b", 0, max(ys) + 0.6)]
    nogr = [(vardi[i], vardi[i + 1]) for i in range(len(vardi) - 1)]
    if pilna:
        nogr.append((vardi[-1], vardi[0]))
    return geometrija(p, nogriezni=nogr, slepti=[("_a", "_b")],
                      iekrasot=[(vardi, 0)] if pilna else [])


_EGLE = [(0, 6), (2, 3), (1, 3), (3, 0), (0.5, 0), (0.5, -1), (0, -1)]
_SIRDS = [(0, 0), (2.5, 2.5), (3, 4), (2.5, 5), (1.5, 5.2), (0.6, 4.8),
          (0, 4)]

SATURS = [
    Sakums("Kā izgriezt eglīti, kas abās pusēs vienāda?",
           zimejums=_puse(_EGLE, True),
           paraksts="Izgriež tikai pusi - otra rodas pati.",
           fakti=["Papīru pārloka uz pusēm.",
                  "Zīmē pusi figūras pie locījuma.",
                  "Izgriež un atloka - simetrisks rotājums."]),

    Slidnis("Kā tas notiek", [
        {"v": "1", "teksts": "Uzzīmē pusi pie locījuma",
         "zim": _puse(_EGLE, False)},
        {"v": "2", "teksts": "Izgriez un atloki - eglīte!",
         "zim": _puse(_EGLE, True)},
        {"v": "3", "teksts": "Tas pats ar sirdi: puse",
         "zim": _puse(_SIRDS, False)},
        {"v": "4", "teksts": "Atlocīta sirds",
         "zim": _puse(_SIRDS, True)},
    ]),

    Doma("Locīt, zīmēt, griezt",
         "Ko izgriez vienā pusē, tas atlokot parādās arī otrā.",
         soli=[
             "Pārloki papīru uz pusēm.",
             "Pie locījuma uzzīmē pusi figūras.",
             "Izgriez, negriežot pašu locījumu.",
             "Atloki un pārbaudi, pārlokot vēlreiz.",
         ]),

    Varianti("Kas būs, atlokot?", [
        {"jaut": "Ja izgriež pusi eglītes pie locījuma, atlokot būs...",
         "opcijas": ["vesela eglīte", "puse eglītes", "divas eglītes"],
         "pareizi": 0, "padoms": "Otra puse rodas pati."},
        {"jaut": "Ko nedrīkst pārgriezt?",
         "opcijas": ["locījumu", "papīra malu", "zīmējumu"],
         "pareizi": 0, "padoms": "Citādi būs divas puses atsevišķi."},
    ]),

    Ievadi("Saskaiti", [
        {"jaut": "Pusē ir 2 zari. Cik zaru būs atlocītai eglītei?",
         "atb": ["4"], "padoms": "Abās pusēs pa 2."},
        {"jaut": "Pusē izgriezi 3 caurumiņus. Cik būs atlokot?",
         "atb": ["6"], "padoms": "Divreiz vairāk."},
    ]),

    Petijums("Mans rotājums", [
        "Pārloki krāsainu papīru uz pusēm.",
        "Uzzīmē pie locījuma pusi sirds, eglītes vai tauriņa.",
        "Izgriez un atloki.",
        "Pārbaudi: pārloki - vai puses sakrīt?",
    ], vajag="krāsains papīrs, šķēres, zīmulis"),

    Pasaule("Apsveikuma kartīte",
            Ievadi("", [
                {"jaut": "Katrai kartītei vajag 1 sirdi. Klasē 10 bērnu, 4 "
                         "sirdis jau gatavas. Cik vēl jāizgriež?",
                 "atb": ["6"], "padoms": "10 − 4."},
            ]),
            pavediens="skola",
            konteksts="Klase gatavo kartītes ar simetriskām sirdīm.",
            kapec="Locīšana palīdz izgriezt ātri un vienādi."),

    Kopsavilkums([
        "Izgriežu simetrisku figūru no pārlocīta papīra.",
        "Zinu, ka otra puse rodas pati.",
        "Pārbaudu rezultātu ar locīšanu.",
    ]),

    Majas([
        "Izgriez sniegpārsliņu no pārlocīta papīra.",
        "Izgriez tauriņu un izkrāso abas puses vienādi.",
        "Uzdāvini savu rotājumu kādam.",
    ]),
]
