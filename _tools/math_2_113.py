# -*- coding: utf-8 -*-
"""2. klase, 113. stunda: «Cik rūtiņu ietilpst figūrā?»

Laukums ir tas, cik vietas figūra aizņem - cik vienādu kvadrātu (rūtiņu)
to noklāj. Taisnstūrim rūtiņas skaita pa rindām: 3 rindas pa 5 = 5 + 5 +
5 = 15 rūtiņas. Perimetrs ir apmale, laukums - iekšpuse.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, figura, rutinas)

TEMA = "Cik rūtiņu ietilpst figūrā?"

MERKIS = ("Šodien noteiksim taisnstūra laukumu rūtiņās, noklājot to ar "
          "vienādiem kvadrātiem.")

SATURS = [
    Sakums("Cik flīžu vajag vannas istabas grīdai?",
           zimejums=rutinas(5, 3, 5, 3),
           paraksts="3 rindas pa 5 flīzēm - 15.",
           fakti=["Laukums - cik vietas figūra aizņem.",
                  "To mēra ar vienādiem kvadrātiem - rūtiņām.",
                  "Perimetrs ir apmale, laukums - iekšpuse."]),

    Doma("Laukums rūtiņās",
         "Laukums ir rūtiņu skaits, kas noklāj figūru bez spraugām.",
         soli=[
             "Saskaiti rūtiņas vienā rindā.",
             "Saskaiti rindas.",
             "Saskaiti visas rindas kopā: 5 + 5 + 5 = 15.",
             "Atbilde rūtiņās.",
         ]),

    Slidnis("Rinda pēc rindas", [
        {"v": "5", "teksts": "Viena rinda.", "zim": rutinas(5, 3, 5, 1)},
        {"v": "10", "teksts": "Divas rindas: 5 + 5.",
         "zim": rutinas(5, 3, 5, 2)},
        {"v": "15", "teksts": "Trīs rindas: 5 + 5 + 5.",
         "zim": rutinas(5, 3, 5, 3)},
    ]),

    Ievadi("Cik rūtiņu?", [
        {"jaut": "Cik rūtiņu laukums?", "zim": rutinas(4, 4, 4, 4),
         "atb": ["16"], "mers": "rūtiņas", "padoms": "4 + 4 + 4 + 4."},
        {"jaut": "Cik rūtiņu laukums?", "zim": rutinas(6, 2, 6, 2),
         "atb": ["12"], "mers": "rūtiņas", "padoms": "6 + 6."},
        {"jaut": "Cik rūtiņu laukums?",
         "zim": figura([(0, 0), (4, 0), (4, 2), (2, 2), (2, 4), (0, 4)]),
         "atb": ["12"], "mers": "rūtiņas", "padoms": "8 apakšā un 4 augšā."},
        {"jaut": "Taisnstūris - 3 rindas pa 7 rūtiņām. Laukums?",
         "atb": ["21"], "mers": "rūtiņas", "padoms": "7 + 7 + 7."},
    ]),

    Varianti("Perimetrs vai laukums?", [
        {"jaut": "Cik flīžu vajag grīdai?",
         "opcijas": ["laukums", "perimetrs"], "jaukt": False, "pareizi": 0,
         "padoms": "Grīdu noklāj."},
        {"jaut": "Cik līstes vajag gar sienām?",
         "opcijas": ["laukums", "perimetrs"], "jaukt": False, "pareizi": 1,
         "padoms": "Gar malu."},
        {"jaut": "Cik zāles sēklu vajag zālienam?",
         "opcijas": ["laukums", "perimetrs"], "jaukt": False, "pareizi": 0,
         "padoms": "Viss laukums jāapsēj."},
        {"jaut": "Cik lentes ap dāvanas kastes vāku?",
         "opcijas": ["laukums", "perimetrs"], "jaukt": False, "pareizi": 1,
         "padoms": "Apkārt."},
    ]),

    Pasaule("Šokolādes tāfelīte",
            Ievadi("", [
                {"jaut": "Šokolādē 4 rindas pa 6 gabaliņiem. Cik gabaliņu?",
                 "zim": rutinas(6, 4, 6, 4), "atb": ["24"],
                 "padoms": "6 + 6 + 6 + 6."},
                {"jaut": "Apēda vienu rindu. Cik palika?", "atb": ["18"],
                 "padoms": "24 − 6."},
            ]),
            pavediens="virtuve",
            konteksts="Šokolādes tāfelīte ir sadalīta rūtiņās.",
            kapec="Rūtiņas ļauj ātri saskaitīt laukumu."),

    Kopsavilkums([
        "Zinu, ka laukums ir tas, cik vietas figūra aizņem.",
        "Saskaitu rūtiņas pa rindām.",
        "Atšķiru laukumu no perimetra.",
    ]),

    Majas([
        "Atrodi mājās flīzes un saskaiti, cik tās ir vienā sienā.",
        "Uzzīmē rūtiņu lapā taisnstūri ar laukumu 12 rūtiņas.",
        "Vai var uzzīmēt citu taisnstūri ar tādu pašu laukumu?",
    ]),
]
