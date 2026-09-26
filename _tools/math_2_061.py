# -*- coding: utf-8 -*-
"""2. klase, 61. stunda: «Cikos jāsāk?»

Apgrieztais laika uzdevums: zināms ilgums un viens no galiem. Beigas =
sākums + ilgums; sākums = beigas − ilgums. Tas ir tas pats, ko atrast
paslēpto skaitli, tikai pulkstenī.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, laiks, pulkstenis)

TEMA = "Cikos jāsāk?"

MERKIS = ("Šodien aprēķināsim sākuma vai beigu laiku, ja zināms, cik ilgi "
          "notikums turpinās.")

SATURS = [
    Sakums("Pīrāgs cepas 40 minūtes. Ciemiņi nāks 17:00. Cikos jāliek "
           "krāsnī?",
           zimejums=pulkstenis(4, 20),
           paraksts="16:20 - tieši 40 minūtes pirms 17:00.",
           fakti=["No beigām atpakaļ atņem ilgumu.",
                  "17:00 − 40 min = 16:20.",
                  "Sākumam pieskaitot ilgumu, sanāk beigas."]),

    Doma("Uz priekšu un atpakaļ",
         "Beigas = sākums + ilgums; sākums = beigas − ilgums.",
         soli=[
             "Ja zini sākumu - pieskaiti ilgumu.",
             "Ja zini beigas - atņem ilgumu.",
             "Pāri pilnai stundai ej pa soļiem: līdz :00, tad tālāk.",
             "Pārbaudi ar pretējo darbību.",
         ]),

    Paraugs("Cikos beigsies ekskursija?",
            uzd="Ekskursija sākas 10:40 un ilgst 1 h 30 min.",
            soli=[("10:40 + 1 h = 11:40", "Vispirms stunda."),
                  ("11:40 + 20 min = 12:00", "Līdz pilnai stundai."),
                  ("12:00 + 10 min = 12:10", "Atlikušās minūtes.")],
            atbilde="12:10"),

    Ievadi("Aprēķini laiku", [
        {"jaut": "Sākums 9:00, ilgums 45 min. Beigas?", "atb": laiks(9, 45),
         "padoms": "9:00 + 45 min."},
        {"jaut": "Sākums 14:30, ilgums 2 h. Beigas?", "atb": laiks(16, 30),
         "padoms": "14 + 2."},
        {"jaut": "Beigas 12:00, ilgums 30 min. Sākums?",
         "atb": laiks(11, 30), "padoms": "12:00 − 30 min."},
        {"jaut": "Sākums 8:50, ilgums 20 min. Beigas?", "atb": laiks(9, 10),
         "padoms": "8:50 + 10 = 9:00, + 10."},
        {"jaut": "Beigas 18:15, ilgums 1 h. Sākums?", "atb": laiks(17, 15),
         "padoms": "18 − 1."},
        {"jaut": "Beigas 10:10, ilgums 25 min. Sākums?",
         "atb": laiks(9, 45), "padoms": "10:10 − 10 = 10:00, − 15."},
    ], pamats=4),

    Varianti("Kura darbība?", [
        {"jaut": "Zini, kad filma beidzas un cik ilga. Kā atrast sākumu?",
         "opcijas": ["beigas − ilgums", "beigas + ilgums",
                     "sākums + ilgums"], "pareizi": 0,
         "padoms": "Ej atpakaļ."},
        {"jaut": "Treniņš sākas 16:45 un ilgst 1 h. Kad beidzas?",
         "opcijas": ["17:45", "16:45", "15:45"], "pareizi": 0,
         "padoms": "Pieskaiti stundu."},
    ]),

    Pasaule("Cikos celties?",
            Ievadi("", [
                {"jaut": "Skola sākas 8:30. Ceļš ilgst 20 min. Cikos jāiziet?",
                 "atb": laiks(8, 10), "padoms": "8:30 − 20 min."},
                {"jaut": "Pirms iziešanas vajag 40 min brokastīm un "
                         "apģērbšanai. Cikos celties?", "atb": laiks(7, 30),
                 "padoms": "8:10 − 10 = 8:00, − 30."},
            ]),
            pavediens="skola",
            konteksts="Rīts ir virkne darbu, un katram vajag laiku.",
            kapec="Rēķinot atpakaļ, nekad nenokavē."),

    Kopsavilkums([
        "Aprēķinu beigu laiku, pieskaitot ilgumu.",
        "Aprēķinu sākuma laiku, atņemot ilgumu.",
        "Eju pāri pilnai stundai pa soļiem.",
    ]),

    Majas([
        "Aprēķini, cikos jāceļas, lai nenokavētu skolu.",
        "Ja pusdienas gatavojas 1 h 15 min, cikos jāsāk, lai ēstu 14:00?",
        "Pārbaudi ar mājinieku.",
    ]),
]
