# -*- coding: utf-8 -*-
"""1. klase, 88. stunda: «Cik dažādi var izveidot 15?»

15 kā divu saskaitāmo summu var izveidot daudzos veidos. Kārtīgi -
pēc pirmā saskaitāmā: 6 + 9, 7 + 8, 8 + 7, 9 + 6 (ja abi viencipara),
vai no 0 + 15 līdz 15 + 0.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, restis)

TEMA = "Cik dažādi var izveidot 15?"

MERKIS = ("Šodien izveidosim 15 kā divu saskaitāmo summu visos iespējamos "
          "veidos.")

_TABULA = restis([[6, 9], [7, 8], [8, 7], [9, 6]])

SATURS = [
    Sakums("15 no diviem viencipara skaitļiem - kādi pāri?",
           zimejums=_TABULA,
           paraksts="6 + 9, 7 + 8, 8 + 7, 9 + 6.",
           fakti=["Kārto pēc pirmā saskaitāmā.",
                  "Pirmais aug par 1, otrais samazinās par 1.",
                  "Tā neviens pāris nepazūd."]),

    Doma("Visi veidi pēc kārtas",
         "Ja pirmais saskaitāmais palielinās par 1, otrais samazinās par 1 - "
         "summa paliek 15.",
         soli=[
             "Sāc ar mazāko iespējamo pirmo skaitli.",
             "Katrā rindā pirmais +1, otrais −1.",
             "Beidz, kad pirmais kļūst par lielu.",
         ]),

    Ievadi("Aizpildi", [
        {"jaut": "6 + ? = 15", "atb": ["9"], "padoms": "No 6 līdz 15."},
        {"jaut": "? + 8 = 15", "atb": ["7"], "padoms": "7 + 8."},
        {"jaut": "10 + ? = 15", "atb": ["5"], "padoms": "Desmits un 5."},
        {"jaut": "Cik pāru ar diviem viencipara skaitļiem dod 15?",
         "zim": _TABULA, "atb": ["4"], "padoms": "Saskaiti rindas."},
        {"jaut": "Cik pāru dod 12, ja abi viencipara? (3+9 ... 9+3)",
         "atb": ["7"], "padoms": "3, 4, 5, 6, 7, 8, 9."},
        {"jaut": "0 + ? = 15", "atb": ["15"], "padoms": "Nekas un 15."},
    ], pamats=4),

    Varianti("Vai dod 15?", [
        {"jaut": "7 + 9", "opcijas": ["Nē", "Jā"], "jaukt": False,
         "pareizi": 0, "padoms": "16."},
        {"jaut": "11 + 4", "opcijas": ["Jā", "Nē"], "jaukt": False,
         "pareizi": 0, "padoms": "1 + 4 = 5."},
        {"jaut": "8 + 8", "opcijas": ["Nē", "Jā"], "jaukt": False,
         "pareizi": 0, "padoms": "16."},
    ]),

    Pasaule("Spēles punkti",
            Ievadi("", [
                {"jaut": "Divos metienos jāsavāc tieši 15 punktu. Pirmajā - "
                         "9. Cik vajag otrajā?", "atb": ["6"],
                 "padoms": "9 + ? = 15."},
            ]),
            pavediens="speles",
            konteksts="Spēlē uzvar, kas divos metienos savāc tieši 15.",
            kapec="Zinot visus pārus, zini, ko vajag."),

    Kopsavilkums([
        "Veidoju 15 kā summu dažādos veidos.",
        "Kārtoju pārus, lai neko neaizmirstu.",
        "Atrodu trūkstošo saskaitāmo.",
    ]),

    Majas([
        "Uzraksti visus veidus, kā izveidot 13 ar viencipara skaitļiem.",
        "Cik to ir?",
        "Pārbaudi ar kauliņiem vai kārtīm.",
    ]),
]
