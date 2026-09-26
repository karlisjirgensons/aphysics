# -*- coding: utf-8 -*-
"""1. klase, 165. stunda: «Vai no visām pusēm izskatās vienādi?»

Telpisku figūru apraksta no dažādām pusēm: priekšā, no augšas, no sāna.
L būve no priekšas izskatās kā L, no augšas - kā rinda. Skats atšķiras,
būve - tā pati.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Varianti, figura, kubi)

TEMA = "Vai no visām pusēm izskatās vienādi?"

MERKIS = ("Šodien aprakstīsim telpisku figūru no dažādām pusēm un "
          "saskatīsim, ka skats var atšķirties.")

_BUVE = kubi([(0, 0, 0), (1, 0, 0), (2, 0, 0), (0, 0, 1)])
_PRIEKSA = figura([(0, 0), (3, 0), (3, 1), (1, 1), (1, 2), (0, 2)])
_AUGSA = figura([(0, 0), (3, 0), (3, 1), (0, 1)])
_SANS = figura([(0, 0), (1, 0), (1, 2), (0, 2)])

SATURS = [
    Sakums("Kā šī būve izskatās no augšas?",
           zimejums=_BUVE,
           paraksts="No priekšas - L, no augšas - 3 kvadrāti rindā.",
           fakti=["Skats no priekšas.",
                  "Skats no augšas.",
                  "Skats no sāna."]),

    Doma("Trīs skati",
         "Viena būve - dažādi skati: katrs rāda tikai vienu pusi.",
         soli=[
             "Paskaties tieši no priekšas - ko redzi?",
             "Tad tieši no augšas.",
             "Tad no sāna.",
         ]),

    Varianti("Kurš skats?", [
        {"jaut": "Kā būve izskatās no priekšas?", "zim": _PRIEKSA,
         "opcijas": ["tieši tā", "nē"], "jaukt": False, "pareizi": 0,
         "padoms": "L forma."},
        {"jaut": "Kā būve izskatās no augšas?", "zim": _AUGSA,
         "opcijas": ["tieši tā", "nē"], "jaukt": False, "pareizi": 0,
         "padoms": "Virsū tikai vienā vietā - no augšas redz 3 kvadrātus."},
        {"jaut": "No labā sāna redz...", "zim": _SANS,
         "opcijas": ["2 kvadrātus stateniski", "1 kvadrātu", "3 rindā"],
         "pareizi": 0,
         "padoms": "No sāna redz arī kreiso kubu ar kubu virsū."},
    ]),

    Ievadi("Saskaiti", [
        {"jaut": "Cik kvadrātu redz no priekšas?", "zim": _BUVE,
         "atb": ["4"], "padoms": "3 un 1."},
        {"jaut": "Cik kvadrātu redz no augšas?", "zim": _BUVE,
         "atb": ["3"], "padoms": "Augšējais kubs virs apakšējā."},
    ]),

    Petijums("Apskati no visām pusēm", [
        "Uzbūvē figūru no 4 kubiem.",
        "Uzzīmē skatu no priekšas.",
        "Uzzīmē skatu no augšas.",
        "Vai pāris uzmin būvi pēc taviem zīmējumiem?",
    ], vajag="4 kubi, rūtiņu lapa"),

    Pasaule("Māja no augšas",
            Varianti("", [
                {"jaut": "Putns redz māju no augšas. Ko tas redz?",
                 "opcijas": ["jumtu", "durvis", "logus"], "pareizi": 0,
                 "padoms": "No augšas - jumts."},
            ]),
            pavediens="daba",
            konteksts="Putns lido pāri pilsētai.",
            kapec="Karte ir skats no augšas."),

    Kopsavilkums([
        "Aprakstu figūru no dažādām pusēm.",
        "Zinu, ka skati atšķiras.",
        "Zīmēju skatu no priekšas un augšas.",
    ]),

    Majas([
        "Apskati krēslu no priekšas, sāna un augšas.",
        "Uzzīmē trīs skatus.",
        "Kurš skats visinteresantākais?",
    ]),
]
