# -*- coding: utf-8 -*-
"""1. klase, 132. stunda: «Vai pietiks naudas?»

Pirms pirkuma novērtē: saskaita cenas (vai noapaļo tās uz augšu) un
salīdzina ar naudu makā. Pamato atbildi.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, monetas)

TEMA = "Vai pietiks naudas?"

MERKIS = ("Šodien novērtēsim, vai dotā summa pietiek pirkumam, un pamatosim "
          "atbildi.")

SATURS = [
    Sakums("Makā 20 €. Bumba 12 €, pumpis 7 €. Vai pietiks?",
           zimejums=monetas(["10 €", "10 €"]),
           paraksts="12 + 7 = 19 - pietiek, paliek 1 €.",
           fakti=["Saskaiti cenas.",
                  "Salīdzini ar naudu makā.",
                  "Ja summa mazāka vai vienāda - pietiek."]),

    Doma("Novērtē un pamato",
         "Pietiek, ja pirkuma summa nav lielāka par naudu makā.",
         soli=[
             "Saskaiti vai novērtē cenas.",
             "Salīdzini ar naudu: ≤ - pietiek, > - nepietiek.",
             "Pasaki, cik paliks vai cik pietrūkst.",
         ]),

    Varianti("Pietiek?", [
        {"jaut": "Makā 10 €. Pirkums: 6 € + 5 €.",
         "opcijas": ["nepietiek - trūkst 1 €", "pietiek"], "jaukt": False,
         "pareizi": 0, "padoms": "11 > 10."},
        {"jaut": "Makā 15 €. Pirkums: 8 € + 7 €.",
         "opcijas": ["pietiek - tieši", "nepietiek"], "jaukt": False,
         "pareizi": 0, "padoms": "15 = 15."},
        {"jaut": "Makā 1 €. Pirkums: 60 c + 30 c.",
         "opcijas": ["pietiek - paliek 10 c", "nepietiek"], "jaukt": False,
         "pareizi": 0, "padoms": "90 c < 100 c."},
    ]),

    Ievadi("Cik paliks vai trūks?", [
        {"jaut": "Makā 20 €, pirkums 12 € + 7 €. Cik paliks?",
         "atb": ["1"], "padoms": "20 − 19."},
        {"jaut": "Makā 10 €, pirkums 6 € + 5 €. Cik trūkst?",
         "atb": ["1"], "padoms": "11 − 10."},
        {"jaut": "Makā 18 €, pirkums 9 € + 4 €. Cik paliks?",
         "atb": ["5"], "padoms": "18 − 13."},
    ]),

    Pasaule("Dāvana mammai",
            Varianti("", [
                {"jaut": "Tev krājkasītē 14 €. Puķes 8 €, kartīte 3 €, "
                         "šokolāde 4 €. Vai vari nopirkt visu?",
                 "opcijas": ["Nē - vajag 15 €", "Jā"], "jaukt": False,
                 "pareizi": 0, "padoms": "8 + 3 + 4 = 15."},
                {"jaut": "Bez šokolādes?",
                 "opcijas": ["Jā - 11 €", "Nē"], "jaukt": False,
                 "pareizi": 0, "padoms": "8 + 3 = 11."},
            ]),
            pavediens="veikals",
            konteksts="Tu krāj naudu dāvanai.",
            kapec="Plāno pirms ej uz veikalu."),

    Kopsavilkums([
        "Novērtēju, vai naudas pietiek.",
        "Aprēķinu, cik paliks vai pietrūks.",
        "Pamatoju atbildi.",
    ]),

    Majas([
        "Izdomā, ko nopirktu par 20 €.",
        "Saskaiti cenas no reklāmas.",
        "Vai pietiek?",
    ]),
]
