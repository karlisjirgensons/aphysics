# -*- coding: utf-8 -*-
"""1. klase, 23. stunda: «Cik pietrūkst līdz 10?»

Desmitnieka rāmis (2 × 5): tukšās rūtiņas uzreiz rāda, cik pietrūkst līdz
10, un pilnā augšējā rinda - cik ir vairāk nekā 5. Šie «desmita draugi»
vēlāk noderēs saskaitīšanā ar pāriešanu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, ramis)

TEMA = "Cik pietrūkst līdz 10?"

MERKIS = ("Šodien rāmī redzēsim, cik pietrūkst līdz 10 un cik ir vairāk "
          "nekā 5.")

SATURS = [
    Sakums("Rāmī 7 ripiņas - cik rūtiņu tukšas?",
           zimejums=ramis(7),
           paraksts="7 ripiņas un 3 tukšas rūtiņas: 7 + 3 = 10.",
           fakti=["Rāmī ir 10 rūtiņas: 2 rindas pa 5.",
                  "Tukšās rūtiņas - cik pietrūkst līdz 10.",
                  "Pilna augšējā rinda ir 5."]),

    Slidnis("Desmita draugi", [
        {"v": "9 + 1", "teksts": "Pietrūkst 1", "zim": ramis(9)},
        {"v": "8 + 2", "teksts": "Pietrūkst 2", "zim": ramis(8)},
        {"v": "7 + 3", "teksts": "Pietrūkst 3", "zim": ramis(7)},
        {"v": "6 + 4", "teksts": "Pietrūkst 4", "zim": ramis(6)},
        {"v": "5 + 5", "teksts": "Pietrūkst 5", "zim": ramis(5)},
    ]),

    Doma("Rāmis pasaka divas lietas",
         "Tukšās rūtiņas - cik līdz 10; ripiņas apakšējā rindā - cik vairāk "
         "nekā 5.",
         soli=[
             "Saskaiti tukšās rūtiņas - tik pietrūkst līdz 10.",
             "Augšējā rinda pilna? Tad ir vismaz 5.",
             "Ripiņas apakšā - cik vēl virs 5.",
         ]),

    Ievadi("Cik pietrūkst līdz 10?", [
        {"jaut": "Cik pietrūkst līdz 10?", "zim": ramis(6), "atb": ["4"],
         "padoms": "Saskaiti tukšās rūtiņas."},
        {"jaut": "Cik pietrūkst līdz 10?", "zim": ramis(8), "atb": ["2"],
         "padoms": "Saskaiti tukšās rūtiņas."},
        {"jaut": "Cik pietrūkst līdz 10?", "zim": ramis(3), "atb": ["7"],
         "padoms": "Visa apakšējā rinda un vēl 2."},
        {"jaut": "Par cik 8 ir vairāk nekā 5?", "zim": ramis(8),
         "atb": ["3"], "padoms": "Ripiņas apakšējā rindā."},
        {"jaut": "Par cik 9 ir vairāk nekā 5?", "zim": ramis(9),
         "atb": ["4"], "padoms": "Ripiņas apakšējā rindā."},
        {"jaut": "Cik pietrūkst līdz 10, ja ir 1?", "atb": ["9"],
         "padoms": "1 + ? = 10."},
    ], pamats=4),

    Pasaule("Olu kaste",
            Ievadi("", [
                {"jaut": "Kastē ir vieta 10 olām. Tajā ir 6 olas. Cik vēl "
                         "var ielikt?", "zim": ramis(6), "atb": ["4"],
                 "padoms": "Tukšās vietas."},
                {"jaut": "Mamma izņēma 3 olas no pilnas kastes. Cik palika?",
                 "zim": ramis(7), "atb": ["7"], "padoms": "10 bez 3."},
            ]),
            pavediens="virtuve",
            konteksts="Olu kaste - 2 rindas pa 5, gluži kā rāmis.",
            kapec="Tukšās vietas uzreiz pasaka, cik pietrūkst."),

    Kopsavilkums([
        "Zinu desmita draugus: 9 un 1, 8 un 2, 7 un 3, 6 un 4, 5 un 5.",
        "Rāmī redzu, cik pietrūkst līdz 10.",
        "Redzu, par cik skaitlis lielāks nekā 5.",
    ]),

    Majas([
        "Atrodi mājās olu kasti un saskaiti tukšās vietas.",
        "Uzzīmē rāmi ar 4 ripiņām. Cik pietrūkst līdz 10?",
        "Spēlē ar kādu: tu saki skaitli, viņš - desmita draugu.",
    ]),
]
