# -*- coding: utf-8 -*-
"""4. klase, 107. stunda: «Cik pietrūkst līdz veselam?»

Papildinājums līdz vienam: {3|8} + ? = 1 → ? = {5|8}. Tas ir 16. stundas
«nezināmais saskaitāmais», tikai ar daļām; 1 raksta kā {8|8}. Šo prasmi
ikdienā lieto ar laiku (līdz pilnai stundai) un naudu (līdz eiro).
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Kustiba, Majas,
                         Paraugs, Pasaule, Sakums, Varianti, dala)

TEMA = "Cik pietrūkst līdz veselam?"

MERKIS = ("Noteiksim dotās daļas papildinājumu līdz vienam.")

SATURS = [
    Sakums("Cik vēl jāizlasa?",
           zimejums=dala(8, 3, "izlasīti 3/8, trūkst 5/8"),
           paraksts="Grāmata ir 1 = {8|8}.",
           fakti=["Iekrāsotais un neiekrāsotais kopā ir veselais.",
                  "{3|8} + {5|8} = {8|8} = 1."]),

    Doma("Papildinājums = 1 − daļa",
         "Lai atrastu, cik trūkst līdz 1, uzraksti 1 kā {n|n} un atņem doto "
         "daļu.",
         soli=[
             "Uzraksti 1 ar to pašu saucēju: 1 = {8|8}.",
             "Atņem: {8|8} − {3|8} = {5|8}.",
             "Pārbaude: {3|8} + {5|8} = 1.",
             "Skaitītājs papildinājumam = saucējs − skaitītājs.",
         ],
         pieze="Tas ir iekrāsotā un tukšā gabalu skaits joslā."),

    Paraugs("Līdz pilnai stundai",
            uzd="Pagājušas {7|12} stundas. Kāda daļa stundas vēl atlikusi?",
            soli=[
                ("1 = {12|12}", None),
                ("{12|12} − {7|12} = {5|12}", None),
                ("{7|12} + {5|12} = 1", "Pārbaude."),
            ],
            atbilde="{5|12} stundas"),

    Kustiba("Aizved līdz veselajam", [
        {"jaut": "Gliemezis nogājis {3|10} ceļa (3 iedaļas no 10). Cik "
                 "desmitdaļu vēl jāiet?",
         "atb": 7, "beigas": 10, "iedala": 1, "mers": "desmitdaļas",
         "merkis": "trūkst", "objekts": "Gliemezis",
         "padoms": "10 − 3.",
         "stasts": "Skaitļu taisne rāda atlikušo ceļu desmitdaļās."},
        {"jaut": "Nogājis {6|10}. Cik vēl?", "atb": 4, "beigas": 10,
         "iedala": 1, "mers": "desmitdaļas", "merkis": "trūkst",
         "objekts": "Gliemezis", "padoms": "10 − 6."},
        {"jaut": "Nogājis {9|10}. Cik vēl?", "atb": 1, "beigas": 10,
         "iedala": 1, "mers": "desmitdaļas", "merkis": "trūkst",
         "objekts": "Gliemezis", "padoms": "10 − 9."},
        {"jaut": "Nogājis {5|10}. Cik vēl?", "atb": 5, "beigas": 10,
         "iedala": 1, "mers": "desmitdaļas", "merkis": "trūkst",
         "objekts": "Gliemezis", "padoms": "Puse palikusi."},
    ], pamats=2),

    Ievadi("Cik trūkst?", [
        {"jaut": "{3|8} + ? = 1", "atb": ["5/8"], "vieta": "piem., 1/2",
         "padoms": "8 − 3."},
        {"jaut": "{2|5} + ? = 1", "atb": ["3/5"], "vieta": "piem., 1/2",
         "padoms": "5 − 2."},
        {"jaut": "? + {9|11} = 1", "atb": ["2/11"], "vieta": "piem., 1/2",
         "padoms": "11 − 9."},
        {"jaut": "1 − {1|4} = ?", "atb": ["3/4"], "vieta": "piem., 1/2",
         "padoms": "4 − 1."},
    ]),

    Varianti("Pāri, kas dod 1", [
        {"jaut": "Kurš pāris dod 1?",
         "opcijas": ["{2|7} un {5|7}", "{2|7} un {4|7}", "{1|2} un {1|3}",
                     "{3|7} un {3|7}"], "pareizi": 0,
         "padoms": "2 + 5 = 7."},
        {"jaut": "Papildinājums {1|2} līdz 1 ir...",
         "opcijas": ["{1|2}", "{2|2}", "0", "{1|4}"], "pareizi": 0,
         "padoms": "Puse un puse."},
        {"jaut": "Ja papildinājums ir {1|10}, kāda ir daļa?",
         "opcijas": ["{9|10}", "{1|10}", "{10|9}", "{8|10}"], "pareizi": 0,
         "padoms": "10 − 1."},
    ]),

    Pasaule("Līdz pilnai stundai",
            Ievadi("", [
                {"jaut": "Pagājušas 45 minūtes = {3|4} stundas. Kāda daļa "
                         "stundas atlikusi?",
                 "atb": ["1/4"], "vieta": "piem., 1/2", "padoms": "4 − 3."},
                {"jaut": "Cik minūšu tas ir?", "atb": ["15"],
                 "padoms": "60 : 4."},
                {"jaut": "Pagājušas {5|6} stundas. Cik minūšu atlicis līdz "
                         "pilnai stundai?",
                 "atb": ["10"], "padoms": "{1|6} no 60."},
                {"jaut": "Pagājušas {7|10} stundas. Cik minūšu atlicis?",
                 "atb": ["18"], "padoms": "{3|10} no 60 = 18."},
            ]),
            pavediens="skola",
            konteksts="Stunda ir veselais - un pulkstenis rāda, kāda daļa "
                      "vēl atlikusi līdz starpbrīdim.",
            kapec="Papildinājums līdz 1 pasaka, cik vēl jāgaida."),

    Kopsavilkums([
        "Atrodu papildinājumu līdz 1.",
        "Rakstu 1 kā {n|n}.",
        "Pārbaudu: daļa + papildinājums = 1.",
    ]),

    Majas([
        "Pavēro pulksteni un pasaki, kāda daļa stundas vēl atlikusi.",
        "Atrodi 4 daļu pārus ar saucēju 9, kas kopā dod 1.",
        "Izrēķini, kāda daļa gada vēl atlikusi (pēc mēnešiem: {?|12}).",
    ]),
]
