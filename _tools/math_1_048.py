# -*- coding: utf-8 -*-
"""1. klase, 48. stunda: «Kā pārbaudīt, vai figūra ir taisnstūris?»

Taisnstūrim visi četri stūri ir taisni. Taisnu stūri pārbauda ar papīra
lapas stūri: ja stūris sakrīt - tas ir taisns. Rūtiņu lapā taisnstūri zīmē
pa rūtiņu līnijām.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Varianti, figura, geometrija)

TEMA = "Kā pārbaudīt, vai figūra ir taisnstūris?"

MERKIS = ("Šodien ar papīra stūri pārbaudīsim taisnos leņķus un "
          "uzzīmēsim taisnstūri rūtiņās.")

_TAISNST = geometrija([("A", 0, 0), ("B", 6, 0), ("C", 6, 3), ("D", 0, 3)],
                      nogriezni=["AB", "BC", "CD", "DA"],
                      taisni=["DAB", "ABC", "BCD", "CDA"],
                      iekrasot=[("ABCD", 0)])
_SLIPS = figura([(0, 0), (5, 0), (6, 3), (1, 3)])
_TRAPECE = figura([(0, 0), (6, 0), (5, 3), (0, 3)])
_KVADR = figura([(0, 0), (3, 0), (3, 3), (0, 3)])

SATURS = [
    Sakums("Vai katrs četrstūris ir taisnstūris?",
           zimejums=_TAISNST,
           paraksts="Taisnstūrim visi 4 stūri ir taisni.",
           fakti=["Taisnu stūri pārbauda ar papīra lapas stūri.",
                  "Ja stūris sakrīt - tas ir taisns.",
                  "Arī kvadrāts ir taisnstūris."]),

    Doma("Pārbaude ar lapas stūri",
         "Taisnstūris ir četrstūris, kuram visi stūri ir taisni.",
         soli=[
             "Pieliec lapas stūri pie figūras stūra.",
             "Vai abas malas sakrīt ar lapas malām?",
             "Pārbaudi visus 4 stūrus.",
             "Visi taisni - taisnstūris.",
         ]),

    Varianti("Vai taisnstūris?", [
        {"jaut": "Vai šī figūra ir taisnstūris?", "zim": _SLIPS,
         "opcijas": ["Nē", "Jā"], "jaukt": False, "pareizi": 0,
         "padoms": "Stūri ir slīpi."},
        {"jaut": "Vai šī figūra ir taisnstūris?", "zim": _KVADR,
         "opcijas": ["Jā", "Nē"], "jaukt": False, "pareizi": 0,
         "padoms": "Visi stūri taisni."},
        {"jaut": "Vai šī figūra ir taisnstūris?", "zim": _TRAPECE,
         "opcijas": ["Nē", "Jā"], "jaukt": False, "pareizi": 0,
         "padoms": "Labajā pusē stūri nav taisni."},
    ]),

    Ievadi("Saskaiti", [
        {"jaut": "Cik taisnu stūru ir taisnstūrim?", "atb": ["4"],
         "padoms": "Visi."},
        {"jaut": "Cik taisnu stūru ir šai figūrai?", "zim": _TRAPECE,
         "atb": ["2"], "padoms": "Pārbaudi kreisos stūrus."},
    ]),

    Petijums("Taisnstūris rūtiņās", [
        "Uzzīmē taisnstūri pa rūtiņu līnijām: 5 rūtiņas garš, 3 augsts.",
        "Pārbaudi visus stūrus ar lapas stūri.",
        "Uzzīmē četrstūri, kas nav taisnstūris.",
    ], vajag="rūtiņu burtnīca, lineāls"),

    Pasaule("Plaukts pie sienas",
            Varianti("", [
                {"jaut": "Plauktam stūris nav taisns. Kas notiks?",
                 "opcijas": ["plaukts būs šķībs", "nekas",
                             "plaukts būs garāks"], "pareizi": 0,
                 "padoms": "Lietas slīdēs."},
            ]),
            pavediens="maja",
            konteksts="Galdnieks pārbauda plaukta stūrus ar leņķmēru.",
            kapec="Taisni stūri - taisns plaukts."),

    Kopsavilkums([
        "Pārbaudu taisnu stūri ar lapas stūri.",
        "Atpazīstu taisnstūri.",
        "Zīmēju taisnstūri rūtiņās.",
    ]),

    Majas([
        "Pārbaudi ar lapas stūri durvju, galda un grāmatas stūrus.",
        "Atrodi kaut ko ar stūri, kas nav taisns.",
        "Uzzīmē 2 dažādus taisnstūrus.",
    ]),
]
