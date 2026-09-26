# -*- coding: utf-8 -*-
"""1. klase, 79. stunda: «Cik ātri zini summas 10 apjomā?»

Veiklības atkārtojums pirms desmita pāriešanas: summas un starpības 10
apjomā. Katrs pastāsta savu atcerēšanās paņēmienu - dubultie, desmita
draugi, +1, skaitļu ģimenes.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, ramis)

TEMA = "Cik ātri zini summas 10 apjomā?"

MERKIS = ("Šodien veikli saskaitīsim un atņemsim 10 apjomā un pastāstīsim, "
          "kā atceramies.")

SATURS = [
    Sakums("Kā atcerēties 7 + 3 uzreiz?",
           zimejums=ramis(10, otra=3),
           paraksts="Desmita draugi: 7 un 3.",
           fakti=["Desmita draugi: 9+1, 8+2, 7+3, 6+4, 5+5.",
                  "Dubultie: 2+2, 3+3, 4+4, 5+5.",
                  "Ģimene: ja 7 + 3 = 10, tad 10 − 3 = 7."]),

    Doma("Atcerēšanās paņēmieni",
         "Kas zina paņēmienu, tam nav jāskaita pa vienam.",
         soli=[
             "Desmita draugi - uz 10.",
             "Dubultie un «dubultais + 1».",
             "No summas - atņemšana.",
         ]),

    Ievadi("Ātrā sērija", [
        {"jaut": "6 + 4", "atb": ["10"], "padoms": "Desmita draugi."},
        {"jaut": "3 + 3", "atb": ["6"], "padoms": "Dubultais."},
        {"jaut": "4 + 5", "atb": ["9"], "padoms": "4 + 4 + 1."},
        {"jaut": "10 − 8", "atb": ["2"], "padoms": "8 + 2 = 10."},
        {"jaut": "9 − 5", "atb": ["4"], "padoms": "5 + 4 = 9."},
        {"jaut": "7 − 0", "atb": ["7"], "padoms": "Neko neatņem."},
        {"jaut": "8 − 4", "atb": ["4"], "padoms": "4 + 4."},
        {"jaut": "2 + 7", "atb": ["9"], "padoms": "7 un 2."},
    ], pamats=6),

    Varianti("Kā tu atceries?", [
        {"jaut": "4 + 5 = 9 - kurš paņēmiens?",
         "opcijas": ["4 + 4 un vēl 1", "desmita draugi", "+ 0"],
         "pareizi": 0, "padoms": "Dubultais un viens."},
        {"jaut": "10 − 6 = 4 - kurš paņēmiens?",
         "opcijas": ["desmita draugi 6 un 4", "dubultais", "+ 1"],
         "pareizi": 0, "padoms": "6 + 4 = 10."},
    ]),

    Pasaule("Kauliņu spēle",
            Ievadi("", [
                {"jaut": "Uzmeti 5 un 5. Cik kopā?", "atb": ["10"],
                 "padoms": "Dubultais."},
                {"jaut": "Uzmeti 6 un 3. Cik kopā?", "atb": ["9"],
                 "padoms": "No 6: 7, 8, 9."},
            ]),
            pavediens="speles",
            konteksts="Kauliņu spēlē summas jāzina ātri.",
            kapec="Kas atceras, spēlē ātrāk."),

    Kopsavilkums([
        "Zinu summas 10 apjomā no galvas.",
        "Lietoju desmita draugus un dubultos.",
        "Pastāstu savu paņēmienu.",
    ]),

    Majas([
        "Katru dienu nosauc desmita draugus 3 reizes.",
        "Spēlē kauliņus ar kādu mājās.",
        "Kurus piemērus vēl atceries lēni?",
    ]),
]
