# -*- coding: utf-8 -*-
"""1. klase, 3. stunda: «Vai vari pateikt, cik ir, neskaitot?»

Mazu skaitu (līdz 5-6) acs pazīst uzreiz, ja lietas sakārtotas rakstā -
kā kauliņa punkti vai desmitnieka rāmis. Mācās redzēt «4 un vēl 1», nevis
skaitīt pa vienam, un pēc tam pārbauda, saskaitot.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, kaulini, ramis)

TEMA = "Vai vari pateikt, cik ir, neskaitot?"

MERKIS = ("Šodien iemācīsimies pazīt 4, 5 un 6 uzreiz - pēc raksta, "
          "neskaitot pa vienam.")

SATURS = [
    Sakums("Cik punktu uz kauliņa? Atbildi ātri!",
           zimejums=kaulini([5]),
           paraksts="Četri stūri un vidus - tas ir 5.",
           fakti=["Spēlē neviens nepārskaita kauliņa punktus.",
                  "Rakstu acs pazīst uzreiz.",
                  "Pēc tam var pārbaudīt, saskaitot."]),

    Doma("Redzi rakstu, nevis punktus",
         "Sakārtotu skaitu var pazīt, neskaitot - pa daļām.",
         soli=[
             "Kauliņa 4 - četri stūri.",
             "Kauliņa 5 - četri stūri un vidus.",
             "Kauliņa 6 - divas rindas pa trim.",
             "Rāmī: pilna rinda ir 5.",
         ]),

    Slidnis("Kauliņa raksti", [
        {"v": "4", "teksts": "Četri stūri", "zim": kaulini([4])},
        {"v": "5", "teksts": "Četri stūri un vidus", "zim": kaulini([5])},
        {"v": "6", "teksts": "Divas rindas pa trim", "zim": kaulini([6])},
    ]),

    Ievadi("Cik punktu? Ātri!", [
        {"jaut": "Cik punktu?", "zim": kaulini([4]), "atb": ["4"],
         "padoms": "Četri stūri."},
        {"jaut": "Cik punktu?", "zim": kaulini([6]), "atb": ["6"],
         "padoms": "Divas rindas pa trim."},
        {"jaut": "Cik punktu?", "zim": kaulini([3]), "atb": ["3"],
         "padoms": "Slīpa līnija."},
        {"jaut": "Cik ripiņu rāmī?", "zim": ramis(5), "atb": ["5"],
         "padoms": "Pilna augšējā rinda."},
        {"jaut": "Cik ripiņu rāmī?", "zim": ramis(6), "atb": ["6"],
         "padoms": "Pilna rinda un vēl 1."},
        {"jaut": "Cik ripiņu rāmī?", "zim": ramis(4), "atb": ["4"],
         "padoms": "Rindā pietrūkst vienas."},
    ], pamats=4),

    Varianti("Kur ir vairāk?", [
        {"jaut": "Kurš kauliņš rāda vairāk?", "zim": kaulini([4, 6]),
         "opcijas": ["labais", "kreisais"], "jaukt": False, "pareizi": 0,
         "padoms": "6 ir vairāk nekā 4."},
        {"jaut": "Kurš kauliņš rāda vairāk?", "zim": kaulini([5, 3]),
         "opcijas": ["labais", "kreisais"], "jaukt": False, "pareizi": 1,
         "padoms": "5 ir vairāk nekā 3."},
    ]),

    Pasaule("Spēle ar kauliņiem",
            Ievadi("", [
                {"jaut": "Tu uzmeti divus kauliņus. Cik punktu kopā?",
                 "zim": kaulini([2, 3]), "atb": ["5"],
                 "padoms": "2 un vēl 3."},
                {"jaut": "Cik punktu kopā?", "zim": kaulini([4, 1]),
                 "atb": ["5"], "padoms": "4 un vēl 1."},
                {"jaut": "Cik punktu kopā?", "zim": kaulini([3, 3]),
                 "atb": ["6"], "padoms": "3 un vēl 3."},
            ]),
            pavediens="speles",
            konteksts="Galda spēlē jāiet tik lauciņu, cik punktu uzmeti.",
            kapec="Kas pazīst rakstu, spēlē ātrāk un nekļūdās."),

    Kopsavilkums([
        "Pazīstu 4, 5 un 6 uz kauliņa, neskaitot.",
        "Rāmī redzu: pilna rinda ir 5.",
        "Pārbaudu, saskaitot pa vienam.",
    ]),

    Majas([
        "Spēlē ar kādu mājās: parādi kauliņu uz mirkli - cik punktu?",
        "Noliec 5 karotes kā kauliņa pieci.",
        "Atrodi mājās lietas, kas sakārtotas pa 2 vai pa 3.",
    ]),
]
