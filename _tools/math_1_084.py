# -*- coding: utf-8 -*-
"""1. klase, 84. stunda: «Kā pārbaudīt, vai sanāca pareizi?»

Saskaitīšanu pārbauda divējādi: ar citu paņēmienu (samaina saskaitāmos)
vai ar pretējo darbību - atņemšanu: ja 13 + 5 = 18, tad 18 − 5 = 13.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, majina)

TEMA = "Kā pārbaudīt, vai sanāca pareizi?"

MERKIS = ("Šodien pārbaudīsim saskaitīšanas rezultātu ar citu paņēmienu vai "
          "ar atņemšanu.")

SATURS = [
    Sakums("13 + 5 = 18. Kā pārliecināties?",
           zimejums=majina(18, [(13, 5)]),
           paraksts="18 − 5 = 13 - pareizi!",
           fakti=["Pārbaudi ar atņemšanu.",
                  "Vai samaini saskaitāmos.",
                  "Ja sakrīt - pareizi."]),

    Doma("Pretējā darbība",
         "No summas atņem vienu saskaitāmo - jāpaliek otram.",
         soli=[
             "Izrēķini summu.",
             "Atņem no summas otro saskaitāmo.",
             "Sanāca pirmais? Pareizi!",
         ]),

    Ievadi("Pārbaudi ar atņemšanu", [
        {"jaut": "14 + 4 = 18. Pārbaude: 18 − 4 = ?", "atb": ["14"],
         "padoms": "Jāsanāk 14."},
        {"jaut": "12 + 7 = 19. Pārbaude: 19 − 7 = ?", "atb": ["12"],
         "padoms": "Jāsanāk 12."},
        {"jaut": "11 + 5 = 16. Pārbaude: 16 − 5 = ?", "atb": ["11"],
         "padoms": "Jāsanāk 11."},
    ]),

    Varianti("Vai pareizi?", [
        {"jaut": "Toms: 15 + 3 = 17. Pārbaude 17 − 3 = 14. Vai pareizi?",
         "opcijas": ["Nē, 14 nav 15", "Jā"], "jaukt": False, "pareizi": 0,
         "padoms": "Pārbaude nesakrīt."},
        {"jaut": "Anna: 13 + 6 = 19. Pārbaude 19 − 6 = 13. Vai pareizi?",
         "opcijas": ["Jā", "Nē"], "jaukt": False, "pareizi": 0,
         "padoms": "Sakrīt."},
        {"jaut": "Kāda ir pareizā summa 15 + 3?",
         "opcijas": ["18", "17", "19"], "pareizi": 0,
         "padoms": "5 + 3 = 8."},
    ]),

    Pasaule("Čeka pārbaude",
            Ievadi("", [
                {"jaut": "Čekā: 12 € + 6 € = 18 €. Pārbaude: 18 − 6 = ?",
                 "atb": ["12"], "padoms": "Jāsanāk 12 - pareizi."},
            ]),
            pavediens="veikals",
            konteksts="Mamma pārbauda čeku pēc iepirkšanās.",
            kapec="Pārbaude pasargā no kļūdām."),

    Kopsavilkums([
        "Pārbaudu summu ar atņemšanu.",
        "Pārbaudu, samainot saskaitāmos.",
        "Atrodu kļūdu, ja pārbaude nesakrīt.",
    ]),

    Majas([
        "Izrēķini 3 summas un pārbaudi katru.",
        "Pārbaudi mājinieka rēķinu.",
        "Kurš pārbaudes veids tev patīk labāk?",
    ]),
]
