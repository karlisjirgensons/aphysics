# -*- coding: utf-8 -*-
"""4. klase, 115. stunda: «Vai rezultāts ir īsta vai neīsta daļa?»

Vesela skaitļa un daļas reizinājums var būt īsta vai neīsta daļa, un to
var paredzēt: ja reizinājums k · a ir mazāks par saucēju, rezultāts ir
mazāks par 1. Skolēns pamato, nevis tikai izrēķina.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, restis)

TEMA = "Vai rezultāts ir īsta vai neīsta daļa?"

MERKIS = ("Noteiksim, vai reizinājums ir īsta vai neīsta daļa, un "
          "pamatosim atbildi.")

SATURS = [
    Sakums("Vai reizinājums pārsniegs 1?",
           zimejums=restis([["reizinājums", "skaitītājs", "daļa"],
                            ["2 · 1/5", "2 < 5", "īsta"],
                            ["5 · 1/5", "5 = 5", "vienāda ar 1"],
                            ["3 · 2/5", "6 > 5", "neīsta"]],
                           "salīdzini ar saucēju"),
           fakti=["Skaitītāju izrēķina, reizinot.",
                  "Tad salīdzina ar saucēju - kā 97. stundā."]),

    Doma("Salīdzini k · a ar saucēju",
         "Reizinājums k · {a|n} ir īsta daļa, ja k · a < n, un neīsta, ja "
         "k · a ≥ n.",
         soli=[
             "Sareizini skaitli ar skaitītāju: k · a.",
             "Salīdzini ar saucēju n.",
             "k · a < n → īsta daļa, mazāka par 1.",
             "k · a ≥ n → neīsta daļa, 1 vai vairāk.",
         ],
         pieze="Robeža: k · a = n dod tieši 1."),

    Paraugs("4 · {2|7}",
            uzd="Vai 4 · {2|7} ir īsta vai neīsta daļa?",
            soli=[
                ("4 · 2 = 8", None),
                ("8 > 7", "Skaitītājs lielāks par saucēju."),
                ("{8|7} - neīsta", "Mazliet vairāk par 1."),
            ],
            atbilde="neīsta daļa"),

    Varianti("Īsta vai neīsta?", [
        {"jaut": "2 · {3|8}", "opcijas": ["īsta", "neīsta"], "pareizi": 0,
         "padoms": "6 < 8."},
        {"jaut": "3 · {3|8}", "opcijas": ["neīsta", "īsta"], "pareizi": 0,
         "padoms": "9 > 8."},
        {"jaut": "4 · {1|4}", "opcijas": ["neīsta (= 1)", "īsta"],
         "pareizi": 0, "padoms": "4 = 4."},
        {"jaut": "5 · {1|6}", "opcijas": ["īsta", "neīsta"], "pareizi": 0,
         "padoms": "5 < 6."},
        {"jaut": "Lielākais k, lai k · {2|9} būtu īsta daļa?",
         "opcijas": ["4", "5", "9", "3"], "pareizi": 0,
         "padoms": "4 · 2 = 8 < 9, 5 · 2 = 10 > 9."},
        {"jaut": "Kurš reizinājums ir tieši 1?",
         "opcijas": ["3 · {2|6}", "2 · {2|6}", "4 · {2|6}", "6 · {2|6}"],
         "pareizi": 0, "padoms": "3 · 2 = 6."},
    ], pamats=4),

    Ievadi("Atrodi skaitli", [
        {"jaut": "Mazākais k, lai k · {1|5} būtu neīsta daļa?", "atb": ["5"],
         "padoms": "k · 1 ≥ 5."},
        {"jaut": "Lielākais k, lai k · {3|10} būtu īsta?", "atb": ["3"],
         "padoms": "3 · 3 = 9 < 10."},
        {"jaut": "Kāds k, lai k · {2|8} = 1?", "atb": ["4"],
         "padoms": "k · 2 = 8."},
        {"jaut": "Cik veselo ir 7 · {3|7}?", "atb": ["3"],
         "padoms": "{21|7} = 3."},
    ]),

    Pasaule("Vai pietiks krāsas?",
            Ievadi("", [
                {"jaut": "Vienam sienas gabalam vajag {2|5} bundžas. Ir 1 "
                         "bundža. Cik gabalus var nokrāsot (vesels skaitlis)?",
                 "atb": ["2"], "padoms": "2 · {2|5} = {4|5} < 1, bet "
                 "3 · {2|5} = {6|5} > 1."},
                {"jaut": "Cik bundžas vajag 5 gabaliem? Raksti daļu.",
                 "atb": ["10/5", "2"], "vieta": "piem., 1/2",
                 "padoms": "5 · 2."},
                {"jaut": "Cik veselas bundžas tas ir?", "atb": ["2"],
                 "padoms": "{10|5} = 2."},
                {"jaut": "Vai 3 gabaliem pietiks ar 1 bundžu? Raksti «jā» "
                         "vai «nē».",
                 "atb": ["nē", "ne"], "tastatura": "text",
                 "padoms": "{6|5} > 1."},
            ]),
            pavediens="maja",
            konteksts="Remontā materiālu pērk veselās bundžās - un jāzina, "
                      "vai reizinājums pārsniegs 1.",
            kapec="Īsta daļa - pietiek; neīsta - jāpērk vēl."),

    Kopsavilkums([
        "Paredzu, vai reizinājums būs īsta vai neīsta daļa.",
        "Salīdzinu k · a ar saucēju.",
        "Pamatoju atbildi.",
    ]),

    Majas([
        "Atrodi visus k, kuriem k · {3|12} ir īsta daļa.",
        "Izdomā remonta uzdevumu ar krāsas bundžām.",
        "Paskaidro, kad reizinājums ir tieši 1.",
    ]),
]
