# -*- coding: utf-8 -*-
"""1. klase, 134. stunda: «Kā uzbūvēt savu pulksteni?»

Pulksteņa modeli izgatavo no papīra šķīvja: 12 cipari vienādos
attālumos (sākot ar 12, 3, 6, 9), divi rādītāji - īsais stundu un garais
minūšu. Ar to rāda pilnas stundas.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Varianti, pulkstenis)

TEMA = "Kā uzbūvēt savu pulksteni?"

MERKIS = ("Šodien pēc norādēm izveidosim pulksteņa modeli un rādīsim ar to "
          "pilnas stundas.")

SATURS = [
    Sakums("Kā uztaisīt pulksteni no papīra šķīvja?",
           zimejums=pulkstenis(12),
           paraksts="Vispirms 12, 3, 6, 9 - tad pārējie cipari.",
           fakti=["12 cipari pa apli.",
                  "Īsais rādītājs - stundas.",
                  "Garais rādītājs - minūtes."]),

    Petijums("Pulksteņa modelis", [
        "Uz papīra šķīvja augšā uzraksti 12, apakšā 6.",
        "Pa labi 3, pa kreisi 9.",
        "Starp tiem ieraksti pārējos ciparus pa diviem.",
        "Izgriez divus rādītājus - īsu un garu - un piesprauž vidū.",
    ], vajag="papīra šķīvis, kartons, spraudīte, flomāsteri"),

    Doma("Pilnas stundas",
         "Pilnā stundā garais rādītājs rāda uz 12, īsais - uz stundu.",
         soli=[
             "Pagriez garo uz 12.",
             "Īso pagriez uz stundas ciparu.",
             "Nolasi: pulksten ...",
         ]),

    Ievadi("Cik pulkstenis?", [
        {"jaut": "Cik stundas?", "zim": pulkstenis(9), "atb": ["9"],
         "padoms": "Īsais uz 9."},
        {"jaut": "Cik stundas?", "zim": pulkstenis(6), "atb": ["6"],
         "padoms": "Īsais uz 6."},
        {"jaut": "Cik stundas?", "zim": pulkstenis(11), "atb": ["11"],
         "padoms": "Īsais uz 11."},
        {"jaut": "Cik stundas?", "zim": pulkstenis(2), "atb": ["2"],
         "padoms": "Īsais uz 2."},
    ]),

    Varianti("Kurš pulkstenis?", [
        {"jaut": "Kas rāda pulksten 4?", "zim": pulkstenis(4),
         "opcijas": ["šis rāda 4", "šis rāda 12"], "jaukt": False,
         "pareizi": 0, "padoms": "Īsais uz 4."},
        {"jaut": "Kurš rādītājs garāks?",
         "opcijas": ["minūšu", "stundu"], "jaukt": False, "pareizi": 0,
         "padoms": "Garais - minūtes."},
    ]),

    Pasaule("Modinātājs",
            Ievadi("", [
                {"jaut": "Modinātājs zvana pulksten 7. Tu piecēlies stundu "
                         "vēlāk. Cik pulkstenis?", "atb": ["8"],
                 "padoms": "7 + 1."},
            ]),
            pavediens="maja",
            konteksts="Rītā modinātājs zvana vienmēr vienā laikā.",
            kapec="Pulkstenis palīdz nenokavēt."),

    Kopsavilkums([
        "Izveidoju pulksteņa modeli.",
        "Rādu pilnas stundas.",
        "Zinu, kurš rādītājs ko rāda.",
    ]),

    Majas([
        "Parādi ar savu pulksteni, kad ceļies un kad ej gulēt.",
        "Salīdzini ar īsto pulksteni.",
        "Iemāci mājiniekam savu pulksteni.",
    ]),
]
