# -*- coding: utf-8 -*-
"""1. klase, 136. stunda: «Kā skaitīt pa 5 minūtēm?»

Starp diviem cipariem ciparnīcā ir 5 minūtes. Garais rādītājs uz 1 - 5
min, uz 3 - 15 min, uz 6 - 30 min. Skaitīšana pa 5 no 69. stundas
tagad noder pulkstenī.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, pulkstenis)

TEMA = "Kā skaitīt pa 5 minūtēm?"

MERKIS = ("Šodien noteiksim laiku ar 5 minūšu precizitāti, skaitot pa 5.")

SATURS = [
    Sakums("Garais rādītājs uz 3 - cik minūšu?",
           zimejums=pulkstenis(4, 15),
           paraksts="5, 10, 15 - 4:15.",
           fakti=["Starp cipariem - 5 minūtes.",
                  "Skaiti pa 5 no 12.",
                  "Uz 6 - 30 minūtes."]),

    Doma("Minūtes pa 5",
         "Garo rādītāju skaiti pa 5, sākot no 12.",
         soli=[
             "Nolasi stundu pēc īsā (pēdējais cipars, kam tas pagājis garām).",
             "Garo skaiti pa 5: 5, 10, 15...",
             "Pieraksti: stundas:minūtes.",
         ]),

    Ievadi("Cik minūšu?", [
        {"jaut": "Garais uz 2. Cik minūšu?", "atb": ["10"],
         "padoms": "5, 10."},
        {"jaut": "Garais uz 4. Cik minūšu?", "atb": ["20"],
         "padoms": "5, 10, 15, 20."},
        {"jaut": "Garais uz 9. Cik minūšu?", "atb": ["45"],
         "padoms": "Pa 5 līdz 9."},
        {"jaut": "Garais uz 11. Cik minūšu?", "atb": ["55"],
         "padoms": "Pirms 60."},
    ]),

    Ievadi("Cik pulkstenis? (kā 4:15)", [
        {"jaut": "Cik rāda?", "zim": pulkstenis(2, 20),
         "atb": ["2:20", "2,20"], "tastatura": "text",
         "padoms": "Garais uz 4 - 20 min."},
        {"jaut": "Cik rāda?", "zim": pulkstenis(7, 45),
         "atb": ["7:45", "7,45"], "tastatura": "text",
         "padoms": "Garais uz 9 - 45 min."},
        {"jaut": "Cik rāda?", "zim": pulkstenis(9, 5),
         "atb": ["9:05", "9,05"], "tastatura": "text",
         "padoms": "Garais uz 1 - 5 min."},
    ]),

    Varianti("Kurš pulkstenis?", [
        {"jaut": "Kurš laiks attēlā?", "zim": pulkstenis(11, 50),
         "opcijas": ["11:50", "10:50", "11:10"], "pareizi": 0,
         "padoms": "Īsais gandrīz pie 12, garais uz 10."},
    ]),

    Pasaule("Autobuss",
            Ievadi("", [
                {"jaut": "Autobuss atiet 8:25. Pulkstenis rāda 8:15. Cik "
                         "minūšu vēl?", "atb": ["10"], "padoms": "15 līdz 25."},
            ]),
            pavediens="celojums",
            konteksts="Autobusa sarakstā laiks ir minūtēs.",
            kapec="Minūtes izšķir, vai paspēsi."),

    Kopsavilkums([
        "Skaitu minūtes pa 5.",
        "Nolasu laiku ar 5 minūšu precizitāti.",
        "Pierakstu laiku ar cipariem.",
    ]),

    Majas([
        "Nolasi mājas pulksteni 3 reizes dienā.",
        "Pieraksti laikus.",
        "Salīdzini ar digitālo pulksteni.",
    ]),
]
