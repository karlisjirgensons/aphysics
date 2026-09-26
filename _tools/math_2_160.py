# -*- coding: utf-8 -*-
"""2. klase, 160. stunda: «Reizes vai vienības?»

Nostiprina 133. stundas atšķirību ar visiem reizinātājiem: «par 4 vairāk»
(+ 4) un «4 reizes vairāk» (· 4). Shematiskā zīmējumā «par» pieliek gabalu,
«reizes» atkārto visu sloksni.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, sloksnes)

TEMA = "Reizes vai vienības?"

MERKIS = ("Šodien nošķirsim «par tik lielāks» no «tik reižu lielāks», "
          "attēlojot abus shematiskā zīmējumā.")

SATURS = [
    Sakums("Annai 5 €. Brālim «par 3 vairāk» vai «3 reizes vairāk»?",
           zimejums=sloksnes([("Anna", 5, "5"), ("par 3", 8, "8"),
                              ("3 reizes", 15, "15")]),
           paraksts="5 + 3 = 8, bet 5 · 3 = 15.",
           fakti=["«Par» - vienības: saskaiti vai atņem.",
                  "«Reizes» - reizini vai dali.",
                  "Zīmējums rāda atšķirību."]),

    Doma("Par vai reizes",
         "«Par N» maina par N vienībām; «N reizes» - atkārto N reizes.",
         soli=[
             "Par N lielāks: + N.",
             "Par N mazāks: − N.",
             "N reizes lielāks: · N.",
             "N reizes mazāks: : N.",
         ]),

    Slidnis("No 4", [
        {"v": "4", "teksts": "Dotais.", "zim": sloksnes([("dotais", 4, "4")])},
        {"v": "par 5 vairāk", "teksts": "4 + 5 = 9.",
         "zim": sloksnes([("dotais", 4, "4"), ("par 5", 9, "9")])},
        {"v": "5 reizes vairāk", "teksts": "4 · 5 = 20.",
         "zim": sloksnes([("dotais", 4, "4"), ("5 reizes", 20, "20")])},
    ]),

    Varianti("Kura darbība?", [
        {"jaut": "Par 4 lielāks nekā 6", "opcijas": ["6 + 4", "6 · 4"],
         "jaukt": False, "pareizi": 0, "padoms": "«Par»."},
        {"jaut": "4 reizes lielāks nekā 6", "opcijas": ["6 + 4", "6 · 4"],
         "jaukt": False, "pareizi": 1, "padoms": "«Reizes»."},
        {"jaut": "3 reizes mazāks nekā 21", "opcijas": ["21 − 3", "21 : 3"],
         "jaukt": False, "pareizi": 1, "padoms": "«Reizes mazāks»."},
        {"jaut": "Par 5 mazāks nekā 20", "opcijas": ["20 − 5", "20 : 5"],
         "jaukt": False, "pareizi": 0, "padoms": "«Par mazāks»."},
    ]),

    Ievadi("Aprēķini", [
        {"jaut": "Par 4 lielāks nekā 6?", "atb": ["10"], "padoms": "6 + 4."},
        {"jaut": "4 reizes lielāks nekā 6?", "atb": ["24"],
         "padoms": "6 · 4."},
        {"jaut": "3 reizes mazāks nekā 21?", "atb": ["7"],
         "padoms": "21 : 3."},
        {"jaut": "Par 5 mazāks nekā 20?", "atb": ["15"], "padoms": "20 − 5."},
        {"jaut": "5 reizes mazāks nekā 20?", "atb": ["4"],
         "padoms": "20 : 5."},
        {"jaut": "Par 3 lielāks nekā 9?", "atb": ["12"], "padoms": "9 + 3."},
    ], pamats=4),

    Pasaule("Suņu barība",
            Ievadi("", [
                {"jaut": "Kucēns apēd 2 paciņas dienā, liels suns - 4 reizes "
                         "vairāk. Cik paciņu suns?", "atb": ["8"],
                 "padoms": "2 · 4."},
                {"jaut": "Kaķis apēd par 1 paciņu vairāk nekā kucēns. Cik?",
                 "atb": ["3"], "padoms": "2 + 1."},
            ]),
            pavediens="daba",
            konteksts="Patversmē dzīvniekiem dod dažādu barības daudzumu.",
            kapec="Viens vārds - «par» vai «reizes» - maina daudzumu."),

    Kopsavilkums([
        "Atšķiru «par tik» no «tik reižu».",
        "Attēloju abus shematiskā zīmējumā.",
        "Izvēlos pareizo darbību.",
    ]),

    Majas([
        "Izdomā 4 teikumus: par 3 vairāk, 3 reizes vairāk, par 2 mazāk, "
        "2 reizes mazāk.",
        "Lai mājinieks pasaka darbību.",
        "Uzzīmē vienu ar sloksnēm.",
    ]),
]
