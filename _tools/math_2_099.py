# -*- coding: utf-8 -*-
"""2. klase, 99. stunda: «Kas ir taisnstūru skaldnis un kas - piramīda?»

Trīs telpiskās figūras: kubs (6 vienādas kvadrātu skaldnes), taisnstūru
skaldnis (6 taisnstūru skaldnes - kā kaste) un piramīda (pamats un
trijstūru skaldnes, kas satiekas virsotnē). Tās atpazīst un raksturo.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, kermenis, restis)

TEMA = "Kas ir taisnstūru skaldnis un kas - piramīda?"

MERKIS = ("Šodien atpazīsim un raksturosim kubu, taisnstūru skaldni un "
          "piramīdu.")

SATURS = [
    Sakums("Kādas formas ir Ēģiptes piramīdas un kurpju kaste?",
           zimejums=kermenis("piramida"),
           paraksts="Piramīda - skaldnes satiekas vienā virsotnē.",
           fakti=["Heopsa piramīda ir vairāk nekā 4000 gadu veca.",
                  "Kurpju kaste ir taisnstūru skaldnis.",
                  "Kauliņš ir kubs."]),

    Doma("Trīs telpiskās figūras",
         "Tās atšķir pēc skaldņu formas.",
         soli=[
             "Kubs: 6 vienādi kvadrāti.",
             "Taisnstūru skaldnis: 6 taisnstūri, pretējie - vienādi.",
             "Piramīda: pamats un trijstūri, kas satiekas augšā.",
             "Kubs ir īpašs taisnstūru skaldnis.",
         ]),

    Slidnis("Iepazīsti", [
        {"v": "kubs", "teksts": "6 skaldnes, 8 virsotnes, 12 šķautnes.",
         "zim": kermenis("kubs")},
        {"v": "taisnstūru skaldnis", "teksts": "Arī 6, 8 un 12 - kā kaste.",
         "zim": kermenis("kvadrs")},
        {"v": "piramīda", "teksts": "Ar kvadrāta pamatu: 5 skaldnes, "
                                    "5 virsotnes, 8 šķautnes.",
         "zim": kermenis("piramida")},
    ]),

    Varianti("Kas tas ir?", [
        {"jaut": "Kas tā par figūru?", "zim": kermenis("kvadrs"),
         "opcijas": ["taisnstūru skaldnis", "piramīda", "lode"],
         "pareizi": 0, "padoms": "Kā kaste."},
        {"jaut": "Kas tā par figūru?", "zim": kermenis("piramida"),
         "opcijas": ["piramīda", "kubs", "cilindrs"], "pareizi": 0,
         "padoms": "Skaldnes satiekas augšā."},
        {"jaut": "Kurš priekšmets ir taisnstūru skaldnis?",
         "opcijas": ["ķieģelis", "bumba", "konuss"], "pareizi": 0,
         "padoms": "Taisnstūru skaldnes."},
        {"jaut": "Kurai figūrai visas skaldnes ir vienādi kvadrāti?",
         "opcijas": ["kubam", "piramīdai", "taisnstūru skaldnim"],
         "pareizi": 0, "padoms": "Kā kauliņam."},
    ]),

    Ievadi("Saskaiti", [
        {"jaut": "Cik skaldņu piramīdai ar kvadrāta pamatu?",
         "zim": kermenis("piramida"), "atb": ["5"],
         "padoms": "Pamats un 4 trijstūri."},
        {"jaut": "Cik trijstūra skaldņu tai ir?", "zim": kermenis("piramida"),
         "atb": ["4"], "padoms": "Visas, izņemot pamatu."},
        {"jaut": "Cik virsotņu taisnstūru skaldnim?",
         "zim": kermenis("kvadrs"), "atb": ["8"], "padoms": "Tāpat kā kubam."},
        {"jaut": "Cik skaldņu kopā kubam un piramīdai?", "atb": ["11"],
         "padoms": "6 + 5."},
    ]),

    Pasaule("Iepakojumu veikals",
            Varianti("", [
                {"jaut": "Kādas formas kaste ir vieglāk sakraujama plauktā?",
                 "opcijas": ["taisnstūru skaldnis", "piramīda", "lode"],
                 "pareizi": 0, "padoms": "Plakanas skaldnes, taisni stūri."},
                {"jaut": "Tējas maisiņi dažreiz ir piramīdas. Cik stūru tai "
                         "ar trijstūra pamatu?",
                 "opcijas": ["4", "5", "8"], "pareizi": 0,
                 "padoms": "3 pamatā un 1 augšā."},
            ]),
            zimejums=restis([["figūra", "skaldnes", "virsotnes"],
                             ["kubs", 6, 8], ["piramīda", 5, 5]]),
            pavediens="tehnika",
            konteksts="Iepakojuma forma ietekmē, cik daudz ietilpst mašīnā.",
            kapec="Taisnstūru skaldņus var sakraut bez spraugām."),

    Kopsavilkums([
        "Atpazīstu kubu, taisnstūru skaldni un piramīdu.",
        "Raksturoju tos pēc skaldnēm, virsotnēm un šķautnēm.",
        "Atrodu tos apkārtnē.",
    ]),

    Majas([
        "Atrodi mājās taisnstūru skaldni un kubu.",
        "Saskaiti to skaldnes un virsotnes.",
        "No papīra saloki piramīdu - cik skaldņu tai sanāca?",
    ]),
]
