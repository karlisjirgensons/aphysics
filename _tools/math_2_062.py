# -*- coding: utf-8 -*-
"""2. klase, 62. stunda: «Cik minūšu ir stundā un pusstundā?»

1 h = 60 min, pusstunda - 30 min, ceturtdaļstunda - 15 min. Pulksteņa
ciparnīca pati rāda šīs daļas: lielais rādītājs pie 3 - ceturtdaļa, pie 6 -
puse. Ar šīm vienībām pārveido un rēķina.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, pulkstenis)

TEMA = "Cik minūšu ir stundā un pusstundā?"

MERKIS = ("Šodien sadalīsim stundu minūtēs un veiksim vienkāršus aprēķinus "
          "ar laika mērvienībām.")

SATURS = [
    Sakums("Cik minūšu ir «pusstundā» un «ceturtdaļstundā»?",
           zimejums=pulkstenis(12, 30),
           paraksts="Lielais rādītājs noiet pusi apļa - 30 minūtes.",
           fakti=["1 stunda = 60 minūtes.",
                  "Pusstunda = 30 minūtes.",
                  "Ceturtdaļstunda = 15 minūtes."]),

    Doma("Stundas daļas",
         "Stunda ir viss aplis; puse apļa ir 30 min, ceturtdaļa - 15 min.",
         soli=[
             "60 min = 1 h.",
             "30 + 30 = 60: divas pusstundas ir stunda.",
             "15 + 15 + 15 + 15 = 60: četras ceturtdaļstundas.",
             "1 h 15 min = 60 + 15 = 75 min.",
         ]),

    Slidnis("Ceturtdaļa pēc ceturtdaļas", [
        {"v": "15 min", "teksts": "Ceturtdaļstunda.",
         "zim": pulkstenis(12, 15)},
        {"v": "30 min", "teksts": "Pusstunda.", "zim": pulkstenis(12, 30)},
        {"v": "45 min", "teksts": "Trīs ceturtdaļas.",
         "zim": pulkstenis(12, 45)},
        {"v": "60 min", "teksts": "Pilna stunda.", "zim": pulkstenis(1, 0)},
    ]),

    Ievadi("Pārveido", [
        {"jaut": "Cik minūšu ir 2 stundās?", "atb": ["120"], "mers": "min",
         "padoms": "60 + 60."},
        {"jaut": "Cik minūšu ir 1 h 30 min?", "atb": ["90"], "mers": "min",
         "padoms": "60 + 30."},
        {"jaut": "Cik minūšu ir divās ceturtdaļstundās?", "atb": ["30"],
         "mers": "min", "padoms": "15 + 15."},
        {"jaut": "80 min = 1 h un cik min?", "atb": ["20"], "mers": "min",
         "padoms": "80 − 60."},
        {"jaut": "Cik minūšu ir 3 ceturtdaļstundās?", "atb": ["45"],
         "mers": "min", "padoms": "15 + 15 + 15."},
        {"jaut": "100 min = 1 h un cik min?", "atb": ["40"], "mers": "min",
         "padoms": "100 − 60."},
    ], pamats=4),

    Varianti("Salīdzini", [
        {"jaut": "Kas ir ilgāk?", "opcijas": ["pusstunda", "20 minūtes"],
         "jaukt": False, "pareizi": 0, "padoms": "30 min."},
        {"jaut": "Kas ir ilgāk?", "opcijas": ["70 minūtes", "1 stunda"],
         "jaukt": False, "pareizi": 0, "padoms": "1 h = 60 min."},
        {"jaut": "Kas ir ilgāk?", "opcijas": ["ceturtdaļstunda",
                                              "20 minūtes"],
         "jaukt": False, "pareizi": 1, "padoms": "15 min."},
        {"jaut": "Kas ir tikpat ilgi kā 1 h?",
         "opcijas": ["divas pusstundas", "trīs ceturtdaļstundas",
                     "50 minūtes"], "pareizi": 0, "padoms": "30 + 30."},
    ]),

    Pasaule("Vai pietiks laika multfilmai?",
            Ievadi("", [
                {"jaut": "Tev ir 1 h brīva laika. Multfilma ilgst 45 min. "
                         "Cik minūšu paliks?", "atb": ["15"], "mers": "min",
                 "padoms": "60 − 45."},
                {"jaut": "Vai pietiks vēl pusstundas spēlei? Raksti, cik "
                         "minūšu pietrūkst.", "atb": ["15"], "mers": "min",
                 "padoms": "30 − 15."},
            ]),
            pavediens="maja",
            konteksts="Vakarā ir stunda brīva laika.",
            kapec="Laika rēķini palīdz izvēlēties, ko paspēt."),

    Kopsavilkums([
        "Zinu, ka 1 h = 60 min, pusstunda = 30 min.",
        "Ceturtdaļstunda = 15 min.",
        "Pārveidoju stundas minūtēs un otrādi.",
    ]),

    Majas([
        "Izmēri, vai mājasdarbi aizņem vairāk vai mazāk par pusstundu.",
        "Cik ceturtdaļstundu ilgst tava mīļākā pārraide?",
        "Pieraksti un salīdzini.",
    ]),
]
