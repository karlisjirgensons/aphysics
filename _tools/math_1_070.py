# -*- coding: utf-8 -*-
"""1. klase, 70. stunda: «Pēc kāda likuma virkne aug?»

Skaitļu virknes likumu atrod, skatoties, par cik katrs nākamais atšķiras
no iepriekšējā: 1; 3; 5; 7 - katru reizi +2. Likumu pasaka vārdos un ar
to turpina virkni.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, taisne)

TEMA = "Pēc kāda likuma virkne aug?"

MERKIS = ("Šodien turpināsim skaitļu virknes un vārdos pateiksim to "
          "likumu.")

SATURS = [
    Sakums("1; 3; 5; 7 - kāds būs nākamais?",
           zimejums=taisne(0, 10, 1, [(1, "1"), (3, "3"), (5, "5"),
                                      (7, "7")],
                           bultas=[(1, 3, "+2"), (3, 5, "+2"),
                                   (5, 7, "+2")]),
           paraksts="Katrs lēciens +2 - nākamais būs 9.",
           fakti=["Paskaties, par cik mainās katrs solis.",
                  "Ja visur vienādi - tas ir likums.",
                  "Pasaki likumu vārdos: «katru reizi par 2 vairāk»."]),

    Doma("Atrodi likumu",
         "Likums - tas, kas notiek ar katru nākamo skaitli.",
         soli=[
             "Atņem blakus skaitļus: 3 − 1 = 2.",
             "Pārbaudi, vai tā visur.",
             "Pasaki likumu vārdos.",
             "Turpini virkni ar likumu.",
         ]),

    Ievadi("Turpini virkni", [
        {"jaut": "1; 3; 5; 7; ...", "atb": ["9"], "padoms": "+2."},
        {"jaut": "3; 6; 9; 12; ...", "atb": ["15"], "padoms": "+3."},
        {"jaut": "20; 18; 16; 14; ...", "atb": ["12"], "padoms": "−2."},
        {"jaut": "4; 14; 24; 34; ...", "atb": ["44"], "padoms": "+10."},
        {"jaut": "50; 45; 40; 35; ...", "atb": ["30"], "padoms": "−5."},
        {"jaut": "0; 4; 8; 12; ...", "atb": ["16"], "padoms": "+4."},
    ], pamats=4),

    Varianti("Kāds ir likums?", [
        {"jaut": "2; 5; 8; 11",
         "opcijas": ["katru reizi par 3 vairāk", "katru reizi par 2 vairāk",
                     "katru reizi par 3 mazāk"], "pareizi": 0,
         "padoms": "5 − 2 = 3."},
        {"jaut": "90; 80; 70; 60",
         "opcijas": ["katru reizi par 10 mazāk",
                     "katru reizi par 10 vairāk", "katru reizi par 1 mazāk"],
         "pareizi": 0, "padoms": "Samazinās."},
    ]),

    Pasaule("Krājkasīte",
            Ievadi("", [
                {"jaut": "Katru nedēļu Rūta ieliek krājkasītē 5 €. Pēc 1. "
                         "nedēļas 5 €, pēc 2. - 10 €. Cik pēc 4. nedēļas?",
                 "atb": ["20"], "padoms": "5; 10; 15; 20."},
                {"jaut": "Pēc cik nedēļām būs 30 €?", "atb": ["6"],
                 "padoms": "Skaiti pa 5 līdz 30."},
            ]),
            pavediens="veikals",
            konteksts="Rūta krāj naudu velosipēdam.",
            kapec="Likums ļauj paredzēt, cik būs vēlāk."),

    Kopsavilkums([
        "Atrodu virknes likumu.",
        "Pasaku to vārdos.",
        "Turpinu virkni.",
    ]),

    Majas([
        "Izdomā virkni ar likumu «+3» un palūdz kādam turpināt.",
        "Uzraksti virkni, kas samazinās pa 10.",
        "Atrodi mājās numurus, kas iet ar likumu (mājas, lappuses).",
    ]),
]
