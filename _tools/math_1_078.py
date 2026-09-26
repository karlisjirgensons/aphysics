# -*- coding: utf-8 -*-
"""1. klase, 78. stunda: «Kas kopīgs 6 + 3 un 16 + 3?»

16 + 3: desmits paliek, vieniem pieskaita tāpat kā 6 + 3. Tāpēc no zināmās
summas pirmajā desmitā uzreiz iegūst summu otrajā: 6 + 3 = 9, 16 + 3 = 19.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, ramis)

TEMA = "Kas kopīgs 6 + 3 un 16 + 3?"

MERKIS = ("Šodien pieskaitīsim divciparu skaitlim viencipara skaitli, "
          "izmantojot to, ko zinām pirmajā desmitā.")

SATURS = [
    Sakums("6 + 3 = 9. Cik ir 16 + 3?",
           zimejums=ramis(19, 2, otra=3),
           paraksts="Pilns desmits paliek; 6 + 3 = 9, tātad 16 + 3 = 19.",
           fakti=["16 = 10 + 6.",
                  "Desmits nemainās - mainās tikai vieni.",
                  "16 + 3 = 10 + 9 = 19."]),

    Slidnis("Tas pats otrajā desmitā", [
        {"v": "6 + 3 = 9", "teksts": "Pirmajā desmitā",
         "zim": ramis(9, 1, otra=3)},
        {"v": "16 + 3 = 19", "teksts": "Pilns desmits un tas pats",
         "zim": ramis(19, 2, otra=3)},
    ]),

    Doma("Desmits paliek",
         "Pieskaitot vienus, desmits nemainās: saskaiti tikai vienus.",
         soli=[
             "Sadali: 16 = 10 + 6.",
             "Saskaiti vienus: 6 + 3 = 9.",
             "Pieliec desmitu: 10 + 9 = 19.",
         ]),

    Ievadi("Pāri", [
        {"jaut": "4 + 5 = 9. Cik ir 14 + 5?", "atb": ["19"],
         "padoms": "Desmits un 9."},
        {"jaut": "2 + 6 = 8. Cik ir 12 + 6?", "atb": ["18"],
         "padoms": "Desmits un 8."},
        {"jaut": "13 + 4 = ?", "atb": ["17"], "padoms": "3 + 4 = 7."},
        {"jaut": "15 + 2 = ?", "atb": ["17"], "padoms": "5 + 2 = 7."},
        {"jaut": "11 + 8 = ?", "atb": ["19"], "padoms": "1 + 8 = 9."},
        {"jaut": "17 + 3 = ?", "atb": ["20"], "padoms": "7 + 3 = 10."},
    ], pamats=4),

    Varianti("Kurš pāris der?", [
        {"jaut": "Kurš piemērs palīdz izrēķināt 14 + 3?",
         "opcijas": ["4 + 3", "1 + 3", "14 + 4"], "pareizi": 0,
         "padoms": "Vieni: 4 un 3."},
        {"jaut": "Kas kopīgs 5 + 2 un 15 + 2?",
         "opcijas": ["vieni sanāk 7", "abi ir 7", "nekas"],
         "pareizi": 0, "padoms": "5 + 2 = 7, 15 + 2 = 17."},
    ]),

    Pasaule("Sporta tērps",
            Ievadi("", [
                {"jaut": "Kreklam numurs 12. Brālim par 5 lielāks. Kāds?",
                 "atb": ["17"], "padoms": "2 + 5 = 7."},
                {"jaut": "Māsai numurs 11, draudzenei - par 7 lielāks.",
                 "atb": ["18"], "padoms": "1 + 7 = 8."},
            ]),
            pavediens="sports",
            konteksts="Komandā katram spēlētājam savs numurs.",
            kapec="Zinot 2 + 5, zini arī 12 + 5."),

    Kopsavilkums([
        "Pieskaitu vienus divciparu skaitlim.",
        "Izmantoju summas no pirmā desmita.",
        "Zinu, ka desmits paliek tas pats.",
    ]),

    Majas([
        "Uzraksti 3 pārus kā 3 + 4 un 13 + 4.",
        "Izrēķini 12 + 7 un 2 + 7.",
        "Paskaidro mājiniekam, kas tiem kopīgs.",
    ]),
]
