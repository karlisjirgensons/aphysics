# -*- coding: utf-8 -*-
"""1. klase, 166. stunda: «Kā uzbūvēt ēkas modeli?»

Ēkas modeli plāno pirms būvēšanas: cik stāvu, cik kubu katrā stāvā, cik
kopā. Tad uzbūvē un pārbauda plānu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Varianti, kubi)

TEMA = "Kā uzbūvēt ēkas modeli?"

MERKIS = ("Šodien plānosim un veidosim ēkas modeli, iepriekš nosakot "
          "vajadzīgo kubu skaitu.")

_MAJA = kubi([(x, 0, z) for x in range(3) for z in range(2)] +
             [(1, 0, 2)])
_TORNIS = kubi([(0, 0, z) for z in range(4)] + [(1, 0, 0), (2, 0, 0)])

SATURS = [
    Sakums("Cik kubu vajag šai mājai?",
           zimejums=_MAJA,
           paraksts="2 stāvi pa 3 kubiem un 1 kubs virsū: 7.",
           fakti=["Plāno pa stāviem.",
                  "Saskaiti kubus katrā stāvā.",
                  "Saskaiti visus stāvus kopā."]),

    Doma("Plāns pirms būves",
         "Labs plāns pasaka, cik kubu vajag, - tad nekas nepietrūkst.",
         soli=[
             "Cik stāvu būs?",
             "Cik kubu katrā stāvā?",
             "Saskaiti: 3 + 3 + 1 = 7.",
             "Uzbūvē un pārbaudi.",
         ]),

    Ievadi("Cik kubu?", [
        {"jaut": "Cik kubu vajag mājai?", "zim": _MAJA, "atb": ["7"],
         "padoms": "3 + 3 + 1."},
        {"jaut": "Cik kubu vajag tornim ar sētu?", "zim": _TORNIS,
         "atb": ["6"], "padoms": "4 + 2."},
        {"jaut": "Mājai 3 stāvi pa 4 kubiem. Cik kubu?", "atb": ["12"],
         "padoms": "4 + 4 + 4."},
        {"jaut": "Tev ir 10 kubu, māja prasa 7. Cik paliks?", "atb": ["3"],
         "padoms": "10 − 7."},
    ]),

    Varianti("Vai pietiks?", [
        {"jaut": "Tev 8 kubi. Plāns: 2 stāvi pa 5 kubiem.",
         "opcijas": ["nepietiks - vajag 10", "pietiks"], "jaukt": False,
         "pareizi": 0, "padoms": "5 + 5 = 10."},
    ]),

    Petijums("Mans modelis", [
        "Uzzīmē savas mājas plānu: cik stāvu, cik kubu katrā.",
        "Aprēķini, cik kubu vajag.",
        "Paņem tieši tik kubu un uzbūvē.",
        "Vai pietika tieši?",
    ], vajag="kubi (klucīši), lapa"),

    Pasaule("Rotaļlaukuma pilsēta",
            Ievadi("", [
                {"jaut": "Klase būvē 3 mājas pa 7 kubiem. Cik kubu vajag?",
                 "atb": ["21"], "padoms": "7 + 7 + 7."},
            ]),
            pavediens="maja",
            konteksts="Klase būvē klucīšu pilsētu.",
            kapec="Plāns ļauj sadalīt klucīšus visiem."),

    Kopsavilkums([
        "Plānoju modeli pirms būvēšanas.",
        "Aprēķinu vajadzīgo kubu skaitu.",
        "Pārbaudu plānu, uzbūvējot.",
    ]),

    Majas([
        "Uzbūvē mājās torni un saskaiti kubus.",
        "Uzzīmē tā plānu.",
        "Izaicini mājinieku uzbūvēt pēc plāna.",
    ]),
]
