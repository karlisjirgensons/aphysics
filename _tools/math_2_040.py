# -*- coding: utf-8 -*-
"""2. klase, 40. stunda: «Kā atņemt bez desmita sadalīšanas?»

Atņemšana pa daļām: desmitus no desmitiem, vienus no vieniem. Šodien vieni
vienmēr pietiek (58 − 23), tāpēc nekas nav jāsadala - tas nāks nākamajā
stundā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, desmiti)

TEMA = "Kā atņemt bez desmita sadalīšanas?"

MERKIS = ("Šodien atņemsim divciparu skaitli, kad vienus var atņemt no "
          "vieniem.")

SATURS = [
    Sakums("Veikalā bija 58 baloni, pārdeva 23. Cik palika?",
           zimejums=desmiti(5, 8),
           paraksts="5 desmiti un 8 vieni.",
           fakti=["Atņem 2 desmitus: paliek 3 desmiti.",
                  "Atņem 3 vienus: paliek 5 vieni.",
                  "Palika 35 baloni."]),

    Doma("Katrs no sava",
         "Desmitus atņem no desmitiem, vienus - no vieniem.",
         soli=[
             "58 = 50 + 8, 23 = 20 + 3.",
             "Desmiti: 50 − 20 = 30.",
             "Vieni: 8 − 3 = 5.",
             "Kopā: 30 + 5 = 35.",
         ]),

    Slidnis("58 − 23 ar kubiņiem", [
        {"v": "58", "teksts": "5 stieņi, 8 kubiņi.", "zim": desmiti(5, 8)},
        {"v": "− 20", "teksts": "Noņem 2 stieņus: 38.", "zim": desmiti(3, 8)},
        {"v": "− 3", "teksts": "Noņem 3 kubiņus: 35.", "zim": desmiti(3, 5)},
    ]),

    Paraugs("Cik ir 76 − 42?",
            uzd="Atņem pa daļām.",
            soli=[("70 − 40 = 30", "Desmiti."), ("6 − 2 = 4", "Vieni."),
                  ("30 + 4 = 34", "Kopā.")],
            atbilde="34"),

    Ievadi("Atņem", [
        {"jaut": "47 − 23 = ?", "atb": ["24"], "padoms": "20 + 4."},
        {"jaut": "89 − 56 = ?", "atb": ["33"], "padoms": "30 + 3."},
        {"jaut": "65 − 30 = ?", "atb": ["35"], "padoms": "Tikai desmiti."},
        {"jaut": "98 − 45 = ?", "atb": ["53"], "padoms": "50 + 3."},
        {"jaut": "74 − 72 = ?", "atb": ["2"], "padoms": "0 desmiti, 2 vieni."},
        {"jaut": "59 − 17 = ?", "atb": ["42"], "padoms": "40 + 2."},
    ], pamats=4),

    Varianti("Vai vieni pietiek?", [
        {"jaut": "68 − 25", "opcijas": ["pietiek", "nepietiek"],
         "jaukt": False, "pareizi": 0, "padoms": "8 ir vairāk nekā 5."},
        {"jaut": "63 − 28", "opcijas": ["pietiek", "nepietiek"],
         "jaukt": False, "pareizi": 1, "padoms": "No 3 nevar atņemt 8."},
    ]),

    Pasaule("Cik vietu vēl brīvas?",
            Ievadi("", [
                {"jaut": "Kinozālē ir 96 vietas, pārdotas 54 biļetes. Cik "
                         "vietu vēl brīvas?", "atb": ["42"],
                 "padoms": "90 − 50, 6 − 4."},
                {"jaut": "Vēl nopirka 21 biļeti. Cik vietu brīvas tagad?",
                 "atb": ["21"], "padoms": "42 − 21."},
            ]),
            pavediens="skola",
            konteksts="Skola iet uz kino, un kasiere skaita brīvās vietas.",
            kapec="Atņemšana pasaka, cik vēl var pārdot."),

    Kopsavilkums([
        "Atņemu desmitus no desmitiem un vienus no vieniem.",
        "Pamanu, vai vieni pietiek.",
        "Saliku rezultātu kopā.",
    ]),

    Majas([
        "Izrēķini: 87 − 34, 69 − 45, 55 − 22.",
        "Paskaidro mājiniekam katru soli.",
        "Izdomā uzdevumu par naudu ar atņemšanu.",
    ]),
]
