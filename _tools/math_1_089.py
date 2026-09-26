# -*- coding: utf-8 -*-
"""1. klase, 89. stunda: «Vai būs vairāk nekā 10?»

Bez precīza aprēķina var spriest: ja otrais saskaitāmais ir lielāks nekā
tas, kas trūkst līdz 10, summa būs vairāk nekā 10. Tāpat ar 15. Pēc tam
pārbauda.
"""

from math_saturs import (Doma, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, ramis)

TEMA = "Vai būs vairāk nekā 10?"

MERKIS = ("Šodien bez precīza aprēķina noteiksim, vai summa būs lielāka "
          "nekā 10 vai 15, un pārbaudīsim.")


def _k(a, b, robeza):
    s = a + b
    return {"jaut": "%d + %d - vairāk nekā %d?" % (a, b, robeza),
            "opcijas": ["vairāk", "tieši tik", "mazāk"], "jaukt": False,
            "pareizi": 0 if s > robeza else 1 if s == robeza else 2,
            "padoms": "Cik trūkst %d līdz %d? Salīdzini ar %d." % (
                a, robeza, b)}


SATURS = [
    Sakums("7 + 5 - vairāk vai mazāk nekā 10? Neskaiti!",
           zimejums=ramis(7),
           paraksts="7 līdz 10 trūkst 3. 5 > 3 - būs vairāk.",
           fakti=["Cik trūkst līdz 10?",
                  "Salīdzini ar otro skaitli.",
                  "Pēc tam pārbaudi."]),

    Doma("Spried, neskaitot",
         "Ja otrais skaitlis ir lielāks nekā trūkstošais, summa pārsniedz "
         "robežu.",
         soli=[
             "Cik pirmajam trūkst līdz 10?",
             "Otrais lielāks? - Vairāk nekā 10.",
             "Vienāds? - Tieši 10. Mazāks? - Mazāk.",
         ]),

    Varianti("Vairāk nekā 10?", [
        _k(7, 5, 10), _k(6, 3, 10), _k(8, 2, 10), _k(4, 9, 10),
        _k(5, 4, 10), _k(9, 3, 10),
    ], pamats=4),

    Varianti("Vairāk nekā 15?", [
        _k(9, 7, 15), _k(8, 6, 15), _k(12, 3, 15), _k(11, 6, 15),
    ]),

    Pasaule("Vai pietiks ar 10 €?",
            Varianti("", [
                {"jaut": "Pirkums: 6 € un 5 €. Vai pietiek ar 10 €?",
                 "opcijas": ["Nē - vairāk nekā 10", "Jā"], "jaukt": False,
                 "pareizi": 0, "padoms": "6 līdz 10 trūkst 4, bet 5 > 4."},
                {"jaut": "Pirkums: 3 € un 6 €?",
                 "opcijas": ["Jā - mazāk nekā 10", "Nē"], "jaukt": False,
                 "pareizi": 0, "padoms": "3 līdz 10 trūkst 7, 6 < 7."},
            ]),
            pavediens="veikals",
            konteksts="Pie kases ātri jāizlemj, vai nauda pietiek.",
            kapec="Spriest var ātrāk, nekā rēķināt."),

    Kopsavilkums([
        "Spriežu, vai summa būs vairāk nekā 10 vai 15.",
        "Izmantoju «cik trūkst līdz».",
        "Pārbaudu ar aprēķinu.",
    ]),

    Majas([
        "Veikalā pamēģini uzminēt, vai pirkums pārsniedz 10 €.",
        "Pārbaudi pie kases.",
        "Izdomā 3 piemērus, kuros tieši 10.",
    ]),
]
