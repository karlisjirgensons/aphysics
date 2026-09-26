# -*- coding: utf-8 -*-
"""1. klase, 85. stunda: «Kad rodas jauns desmits?»

8 + 5: violetās 8 aizpilda pirmo rāmi gandrīz līdz galam, oranžās
aizpilda atlikušās 2 rūtiņas un 3 nonāk otrajā rāmī. Kad pirmais rāmis
pilns, rodas jauns desmits: 8 + 5 = 13.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Slidnis, Varianti, ramis)

TEMA = "Kad rodas jauns desmits?"

MERKIS = ("Šodien ar klucīšiem un rāmi redzēsim, kā, saskaitot divus "
          "viencipara skaitļus, rodas pilns desmits.")

SATURS = [
    Sakums("8 + 5 - kāpēc pietrūkst vietas vienā rāmī?",
           zimejums=ramis(13, 2, otra=5),
           paraksts="Pirmais rāmis pilns - desmits; vēl 3.",
           fakti=["Rāmī ietilpst tieši 10.",
                  "Kad tas pilns - rodas desmits.",
                  "Pārējie iet otrajā rāmī."]),

    Slidnis("8 + 5 soli pa solim", [
        {"v": "8", "teksts": "8 violetas ripiņas", "zim": ramis(8, 2)},
        {"v": "8 + 2", "teksts": "2 oranžās aizpilda rāmi: 10",
         "zim": ramis(10, 2, otra=2)},
        {"v": "10 + 3", "teksts": "Vēl 3 otrajā rāmī: 13",
         "zim": ramis(13, 2, otra=5)},
    ]),

    Doma("Jauns desmits",
         "Ja summa ir vairāk nekā 10, pirmais rāmis kļūst pilns un veidojas "
         "desmits.",
         soli=[
             "Noliec pirmo skaitli rāmī.",
             "Liec otro, līdz rāmis pilns.",
             "Atlikušās liec otrajā rāmī.",
             "Nolasi: desmits un vēl ...",
         ]),

    Ievadi("Cik kopā?", [
        {"jaut": "9 + 4 = ?", "zim": ramis(13, 2, otra=4), "atb": ["13"],
         "padoms": "Desmits un 3."},
        {"jaut": "7 + 5 = ?", "zim": ramis(12, 2, otra=5), "atb": ["12"],
         "padoms": "Desmits un 2."},
        {"jaut": "6 + 6 = ?", "zim": ramis(12, 2, otra=6), "atb": ["12"],
         "padoms": "Desmits un 2."},
        {"jaut": "8 + 7 = ?", "zim": ramis(15, 2, otra=7), "atb": ["15"],
         "padoms": "Desmits un 5."},
    ]),

    Varianti("Vai rodas jauns desmits?", [
        {"jaut": "5 + 4", "opcijas": ["Nē", "Jā"], "jaukt": False,
         "pareizi": 0, "padoms": "9 - rāmis nav pilns."},
        {"jaut": "6 + 7", "opcijas": ["Jā", "Nē"], "jaukt": False,
         "pareizi": 0, "padoms": "13 - vairāk nekā 10."},
        {"jaut": "3 + 7", "opcijas": ["Jā - tieši 10", "Nē"],
         "jaukt": False, "pareizi": 0, "padoms": "Rāmis tieši pilns."},
    ]),

    Petijums("Klucīši", [
        "Saspraud 8 violetus klucīšus.",
        "Pievieno oranžos, līdz ir 10 - cik vajadzēja?",
        "Vēl 3 oranžos liec atsevišķi.",
        "Cik kopā?",
    ], vajag="saspraužami klucīši, desmitnieka rāmis"),

    Pasaule("Olas kastēs",
            Ievadi("", [
                {"jaut": "Kastē (10 vietas) 9 olas. Atnesa vēl 3. Cik olu "
                         "kopā?", "atb": ["12"], "padoms": "Kaste pilna un 2."},
                {"jaut": "Cik olu būs otrajā kastē?", "atb": ["2"],
                 "padoms": "Pirmajā ietilpst tikai 1."},
            ]),
            pavediens="virtuve",
            konteksts="Olas liek kastēs pa 10.",
            kapec="Pilna kaste - viens desmits."),

    Kopsavilkums([
        "Redzu, kā rodas jauns desmits.",
        "Aizpildu rāmi un lieku pārējos otrā.",
        "Saskaitu ar desmita pāriešanu.",
    ]),

    Majas([
        "Ar pogām un olu kastēm parādi 7 + 6.",
        "Cik vajadzēja, lai kaste būtu pilna?",
        "Pieraksti: 7 + 6 = 13.",
    ]),
]
