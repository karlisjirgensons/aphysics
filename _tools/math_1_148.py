# -*- coding: utf-8 -*-
"""1. klase, 148. stunda: «Cik apmēram sanāks?»

Pirms precīza aprēķina novērtē: 38 + 21 - apmēram 40 + 20 = 60. Pēc
aprēķina (59) salīdzina ar aplēsi. Ja atšķiras daudz - kļūda.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, taisne)

TEMA = "Cik apmēram sanāks?"

MERKIS = ("Šodien noteiksim aptuveno rezultātu un pēc tam pārbaudīsim to ar "
          "aprēķinu.")

SATURS = [
    Sakums("38 + 21 - apmēram cik?",
           zimejums=taisne(0, 100, 10, [(38, "38"), (40, "")]),
           paraksts="38 ir tuvu 40, 21 - tuvu 20: apmēram 60.",
           fakti=["Noapaļo uz tuvāko desmitu.",
                  "Saskaiti desmitus.",
                  "Precīzi: 38 + 21 = 59 - tuvu 60."]),

    Doma("Aplēse un pārbaude",
         "Aplēse pasaka, kādam jābūt rezultātam apmēram.",
         soli=[
             "Katru skaitli nomaini ar tuvāko desmitu.",
             "Saskaiti desmitus - aplēse.",
             "Izrēķini precīzi un salīdzini.",
         ]),

    Ievadi("Tuvākais desmits", [
        {"jaut": "Tuvākais desmits skaitlim 38?", "atb": ["40"],
         "padoms": "38 ir tuvāk 40."},
        {"jaut": "Tuvākais desmits skaitlim 21?", "atb": ["20"],
         "padoms": "21 ir tuvāk 20."},
        {"jaut": "Aplēse: 38 + 21 ≈ ?", "atb": ["60"], "padoms": "40 + 20."},
        {"jaut": "Aplēse: 49 + 32 ≈ ?", "atb": ["80"], "padoms": "50 + 30."},
    ]),

    Varianti("Vai ticams?", [
        {"jaut": "Juris: 29 + 41 = 97. Aplēse 30 + 40 = 70. Vai ticams?",
         "opcijas": ["Nē - jābūt ap 70", "Jā"], "jaukt": False,
         "pareizi": 0, "padoms": "97 ir tālu no 70."},
        {"jaut": "Ieva: 52 + 19 = 71. Aplēse 50 + 20 = 70.",
         "opcijas": ["ticams", "neticams"], "jaukt": False, "pareizi": 0,
         "padoms": "71 ir tuvu 70."},
    ]),

    Pasaule("Iepirkumi",
            Varianti("", [
                {"jaut": "Grāmata 39 €, rotaļlieta 18 €. Makā 50 €. Vai "
                         "pietiks?", "opcijas": ["Nē - apmēram 60 €", "Jā"],
                 "jaukt": False, "pareizi": 0, "padoms": "40 + 20 = 60."},
            ]),
            pavediens="veikals",
            konteksts="Pie kases ātri jānovērtē summa.",
            kapec="Aplēse palīdz izlemt bez papīra."),

    Kopsavilkums([
        "Noapaļoju līdz tuvākajam desmitam.",
        "Novērtēju rezultātu.",
        "Pārbaudu precīzu aprēķinu ar aplēsi.",
    ]),

    Majas([
        "Veikalā novērtē divu preču summu.",
        "Pārbaudi pie kases.",
        "Cik tuvu biji?",
    ]),
]
