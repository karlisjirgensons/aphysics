# -*- coding: utf-8 -*-
"""1. klase, 128. stunda: «Cik maksā?»

Cenas zīmē raksta eiro un centos: 2 € 50 c. Monētas: 1, 2, 5, 10, 20, 50
centi, 1 un 2 eiro; banknotes no 5 €. Cenas salīdzina - vispirms eiro, tad
centus.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, monetas)

TEMA = "Cik maksā?"

MERKIS = ("Šodien nolasīsim preču cenas eiro un centos un salīdzināsim "
          "tās.")

SATURS = [
    Sakums("Kādas monētas un naudas zīmes ir Latvijā?",
           zimejums=monetas(["1 c", "2 c", "5 c", "10 c", "20 c", "50 c",
                             "1 €", "2 €"]),
           paraksts="Centi: 1, 2, 5, 10, 20, 50. Eiro monētas: 1 € un 2 €.",
           fakti=["100 centi = 1 eiro.",
                  "Cenu raksta: 2 € 50 c.",
                  "Salīdzina vispirms eiro, tad centus."]),

    Doma("Nolasi cenu",
         "Cenā pirms € ir eiro, pēc tam - centi.",
         soli=[
             "2 € 50 c - divi eiro un piecdesmit centi.",
             "Cenas salīdzina pēc eiro.",
             "Ja eiro vienādi - pēc centiem.",
         ]),

    Ievadi("Cik naudas?", [
        {"jaut": "Cik centu?", "zim": monetas(["20 c", "20 c", "5 c"]),
         "atb": ["45"], "padoms": "20 + 20 + 5."},
        {"jaut": "Cik centu?", "zim": monetas(["50 c", "10 c", "2 c"]),
         "atb": ["62"], "padoms": "50 + 10 + 2."},
        {"jaut": "Cik eiro?", "zim": monetas(["5 €", "2 €", "1 €"]),
         "atb": ["8"], "padoms": "5 + 2 + 1."},
        {"jaut": "Cik eiro?", "zim": monetas(["10 €", "5 €", "2 €"]),
         "atb": ["17"], "padoms": "10 + 5 + 2."},
    ]),

    Varianti("Kurš dārgāks?", [
        {"jaut": "Maize 1 € 20 c vai piens 99 c?",
         "opcijas": ["maize", "piens"], "jaukt": False, "pareizi": 0,
         "padoms": "1 € ir vairāk nekā 99 c."},
        {"jaut": "Sula 2 € 40 c vai kefīrs 2 € 15 c?",
         "opcijas": ["sula", "kefīrs"], "jaukt": False, "pareizi": 0,
         "padoms": "Eiro vienādi, 40 > 15."},
    ]),

    Pasaule("Veikala plaukts",
            Ievadi("", [
                {"jaut": "Ābols 35 c, banāns 25 c. Par cik centiem ābols "
                         "dārgāks?", "atb": ["10"], "padoms": "35 − 25."},
            ]),
            pavediens="veikals",
            konteksts="Pie katras preces ir cenu zīme.",
            kapec="Cenu salīdzināšana palīdz izvēlēties."),

    Kopsavilkums([
        "Pazīstu monētas un naudaszīmes.",
        "Nolasu cenu eiro un centos.",
        "Salīdzinu cenas.",
    ]),

    Majas([
        "Atrodi mājās 3 čekus vai cenu zīmes un izlasi cenas.",
        "Saskaiti monētas makā.",
        "Kura prece bija visdārgākā?",
    ]),
]
