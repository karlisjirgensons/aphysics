# -*- coding: utf-8 -*-
"""1. klase, 164. stunda: «Cik dažādas figūras no četriem kubiem?»

No 4 kubiem, saliekot ar veselām skaldnēm, var uzbūvēt dažādas figūras:
rindu, L, T, kvadrātu, Z un telpiskas. Spriež, kuras ir «tās pašas»
(pagrieztas) un kuras atšķiras.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Slidnis, Varianti, kubi)

TEMA = "Cik dažādas figūras no četriem kubiem?"

MERKIS = ("Šodien veidosim no četriem kubiem dažādas figūras un "
          "spriedīsim, cik to ir.")

_RINDA = kubi([(0, 0, 0), (1, 0, 0), (2, 0, 0), (3, 0, 0)])
_L = kubi([(0, 0, 0), (1, 0, 0), (2, 0, 0), (0, 0, 1)])
_T = kubi([(0, 0, 0), (1, 0, 0), (2, 0, 0), (1, 0, 1)])
_KV = kubi([(0, 0, 0), (1, 0, 0), (0, 0, 1), (1, 0, 1)])
_Z = kubi([(0, 0, 0), (1, 0, 0), (1, 0, 1), (2, 0, 1)])
_TELP = kubi([(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)])

SATURS = [
    Sakums("No 4 kubiem - cik dažādu figūru?",
           zimejums=_L,
           paraksts="L figūra: 3 rindā un 1 virsū.",
           fakti=["Kubus liek ar veselām skaldnēm.",
                  "Pagriezta figūra ir tā pati.",
                  "Ir arī telpiskas figūras."]),

    Slidnis("Figūras no 4 kubiem", [
        {"v": "rinda", "teksts": "4 rindā", "zim": _RINDA},
        {"v": "L", "teksts": "3 rindā un 1 galā", "zim": _L},
        {"v": "T", "teksts": "3 rindā un 1 vidū", "zim": _T},
        {"v": "kvadrāts", "teksts": "2 un 2", "zim": _KV},
        {"v": "Z", "teksts": "Pakāpiens", "zim": _Z},
        {"v": "telpiska", "teksts": "Stūrītis", "zim": _TELP},
    ]),

    Doma("Vai tā pati figūra?",
         "Ja figūru var pagriezt tā, lai tā sakrīt ar citu, - tā ir tā pati.",
         soli=[
             "Uzbūvē figūru.",
             "Pagriez to dažādi.",
             "Salīdzini ar jau atrastajām.",
         ]),

    Ievadi("Saskaiti", [
        {"jaut": "Cik kubu ir katrā figūrā?", "zim": _T, "atb": ["4"],
         "padoms": "Saskaiti."},
        {"jaut": "Cik kubu ir apakšējā rindā T figūrā?", "zim": _T,
         "atb": ["3"], "padoms": "Apakšā."},
    ]),

    Varianti("Tā pati vai cita?", [
        {"jaut": "L figūra, apgriezta otrādi. Tā pati?",
         "opcijas": ["tā pati", "cita"], "jaukt": False, "pareizi": 0,
         "padoms": "Pagriez - sakrīt."},
        {"jaut": "Rinda un kvadrāts - tā pati?",
         "opcijas": ["cita", "tā pati"], "jaukt": False, "pareizi": 0,
         "padoms": "Nekādi nesakrīt."},
    ]),

    Petijums("Būvē un skaiti", [
        "Paņem 4 kubus.",
        "Uzbūvē pēc iespējas vairāk dažādu figūru.",
        "Katru uzzīmē.",
        "Salīdzini ar pāri - vai atradāt vienādi daudz?",
    ], vajag="4 kubi (klucīši)"),

    Pasaule("Spēle ar klucīšiem",
            Varianti("", [
                {"jaut": "Spēlē ar krītošiem klucīšiem ir figūras no 4 "
                         "kvadrātiem. Kura ir rinda?",
                 "zim": _RINDA, "opcijas": ["šī", "neviena"],
                 "jaukt": False, "pareizi": 0, "padoms": "4 rindā."},
            ]),
            pavediens="speles",
            konteksts="Datorspēlēs figūras veidotas no 4 kvadrātiem.",
            kapec="Pazīstot figūras, spēlē gudrāk."),

    Kopsavilkums([
        "Veidoju figūras no 4 kubiem.",
        "Nosaku, vai figūras ir vienādas.",
        "Spriežu, cik figūru var izveidot.",
    ]),

    Majas([
        "Uzbūvē figūras no 4 grāmatām vai kastītēm.",
        "Uzzīmē tās.",
        "Cik dažādas atradi?",
    ]),
]
