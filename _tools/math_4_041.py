# -*- coding: utf-8 -*-
"""4. klase, 41. stunda: «Vai izdosies arī ar četrciparu skaitli?»

Mikrotemata noslēgums - patstāvīgs solis: stabiņam pieliek vēl vienu šķiru.
Nekas jauns nav jāmācās, tāpēc skolēns pats pārnes metodi un pārbauda to ar
aptuveno vērtību. Visi rezultāti paliek 10 000 apjomā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, restis)

TEMA = "Vai izdosies arī ar četrciparu skaitli?"

MERKIS = ("Patstāvīgi reizināsim četrciparu skaitli ar viencipara skaitli un "
          "pārbaudīsim rezultātu.")

SATURS = [
    Sakums("Vai stabiņam ir robežas?",
           zimejums=restis([["", "1", "2", "3", "4"],
                            ["·", "", "", "", "3"],
                            ["", "3", "7", "0", "2"]],
                           "1234 · 3"),
           paraksts="Vēl viena šķira - tas pats stabiņš.",
           fakti=["Stabiņš strādā ar jebkuru ciparu skaitu.",
                  "Aptuvenā vērtība: 1000 · 3 = 3000 - tātad četri cipari."]),

    Doma("Tā pati metode - vēl viens solis",
         "Četrciparu skaitli reizina tāpat kā trīsciparu: vieni, desmiti, "
         "simti, tūkstoši - katrā solī pārnesto pieskaita.",
         soli=[
             "Novērtē: noapaļo līdz tūkstošiem.",
             "Reizini stabiņā no vieniem.",
             "Tūkstošos arī pieskaiti pārnesto.",
             "Salīdzini ar novērtējumu.",
         ],
         pieze="1234 · 3: 4 · 3 = 12, 3 · 3 + 1 = 10, 2 · 3 + 1 = 7, "
               "1 · 3 = 3 → 3702."),

    Paraugs("2047 · 4",
            uzd="Sareizini 2047 · 4 un pārbaudi.",
            soli=[
                ("7 · 4 = 28", "Raksta 8, 2 prātā."),
                ("4 · 4 + 2 = 18", "Raksta 8, 1 prātā."),
                ("0 · 4 + 1 = 1", "Raksta 1."),
                ("2 · 4 = 8", "Raksta 8."),
                ("2047 · 4 = 8188", "Aptuveni 2000 · 4 = 8000 - tuvu."),
            ],
            atbilde="8188"),

    Ievadi("Pamēģini pats", [
        {"jaut": "1234 · 3 = ?", "atb": ["3702"], "padoms": "12, 10, 7, 3."},
        {"jaut": "2105 · 4 = ?", "atb": ["8420"], "padoms": "20, 2, 4, 8."},
        {"jaut": "1506 · 6 = ?", "atb": ["9036"], "padoms": "36, 3, 30, 9."},
        {"jaut": "3125 · 2 = ?", "atb": ["6250"], "padoms": "10, 5, 2, 6."},
        {"jaut": "1111 · 9 = ?", "atb": ["9999"], "padoms": "9 katrā šķirā."},
        {"jaut": "1250 · 8 = ?", "atb": ["10000", "10 000"],
         "padoms": "125 · 8 = 1000."},
    ], pamats=4),

    Varianti("Pārbaudi ar novērtējumu", [
        {"jaut": "2350 · 3 = 7050. Ticams?",
         "opcijas": ["jā", "nē"], "pareizi": 0,
         "padoms": "2000 · 3 = 6000, 2400 · 3 = 7200."},
        {"jaut": "1809 · 5 = 5045. Ticams?",
         "opcijas": ["nē", "jā"], "pareizi": 0,
         "padoms": "2000 · 5 = 10 000; pareizi 9045."},
        {"jaut": "Kurš reizinājums ir mazāks par 10 000?",
         "opcijas": ["2400 · 4", "2600 · 4", "3000 · 4", "5000 · 2"],
         "pareizi": 0, "padoms": "2400 · 4 = 9600."},
    ]),

    Pasaule("Kosmosa raķetes degviela",
            Ievadi("", [
                {"jaut": "Raķetes pakāpe sadedzina 1350 kg degvielas minūtē. "
                         "Cik 6 minūtēs?",
                 "atb": ["8100"], "padoms": "1350 · 6."},
                {"jaut": "Satelīts sver 1215 kg. Cik sver 4 satelīti?",
                 "atb": ["4860"], "padoms": "1215 · 4."},
                {"jaut": "Raķete vienā startā paceļ 2475 kg. Cik kg tā "
                         "pacels 3 startos?",
                 "atb": ["7425"], "padoms": "2475 · 3."},
                {"jaut": "Cik kg vēl var pacelt, ja limits 3 startos ir "
                         "7500 kg?",
                 "atb": ["75"], "padoms": "7500 − 7425."},
            ]),
            pavediens="kosmoss",
            konteksts="Raķetes rēķina ar tūkstošiem kilogramu - un katrs "
                      "kilograms ir svarīgs.",
            kapec="Metode, kas strādā ar trim cipariem, strādā arī ar četriem."),

    Kopsavilkums([
        "Reizinu četrciparu skaitli ar viencipara skaitli.",
        "Pārnesu metodi uz jaunu situāciju pats.",
        "Pārbaudu ar novērtējumu.",
    ]),

    Majas([
        "Izrēķini, cik dienu ir 4 gados (365 · 4 + 1).",
        "Sareizini savu dzimšanas gadu ar 2 un pārbaudi ar kalkulatoru.",
        "Izdomā četrciparu reizinājumu, kura rezultāts ir tieši 10 000.",
    ]),
]
