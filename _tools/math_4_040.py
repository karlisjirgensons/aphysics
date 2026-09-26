# -*- coding: utf-8 -*-
"""4. klase, 40. stunda: «Cik apmēram būs reizinājums?»

Pirms stabiņa - aptuvenā vērtība: noapaļo trīsciparu reizinātāju līdz
simtiem un sareizini galvā. Tā pasaka, cik ciparu būs atbildē un kur tā
aptuveni stāv. Pēc stabiņa - pārbaude.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Kustiba, Majas,
                         Paraugs, Pasaule, Sakums, Varianti, kolonnas)

TEMA = "Cik apmēram būs reizinājums?"

MERKIS = ("Noteiksim reizinājuma aptuveno vērtību pirms aprēķina un "
          "pārbaudīsim pieņēmumu.")

SATURS = [
    Sakums("Vai 6 skūteri pa 389 € maksā vairāk par 2000 €?",
           zimejums=kolonnas([("aptuveni", 2400), ("precīzi", 2334),
                              ("robeža", 2000)], " €"),
           paraksts="389 ≈ 400, 400 · 6 = 2400.",
           fakti=["Atbildi var novērtēt vēl pirms rēķina.",
                  "Aptuveni: vairāk par 2000 - un tas ir pareizi."]),

    Doma("Noapaļo, sareizini galvā, tad rēķini precīzi",
         "Aptuvenā vērtība pasaka, ap kuru skaitli jābūt precīzajai atbildei.",
         soli=[
             "Noapaļo trīsciparu reizinātāju līdz simtiem.",
             "Sareizini galvā: 400 · 6 = 2400.",
             "Izrēķini precīzi stabiņā.",
             "Salīdzini: vai precīzā atbilde ir tuvu?",
         ],
         pieze="Ja noapaļoji uz augšu, precīzā atbilde būs nedaudz mazāka, "
               "ja uz leju - nedaudz lielāka."),

    Paraugs("Novērtē 612 · 7",
            uzd="Novērtē un izrēķini 612 · 7.",
            soli=[
                ("612 ≈ 600", None),
                ("600 · 7 = 4200", "Aptuveni."),
                ("612 · 7 = 4284", "Precīzi."),
                ("4284 ≈ 4200", "Tuvu - pārbaude izturēta."),
            ],
            atbilde="4284"),

    Kustiba("Kur apstāsies reizinājums?", [
        {"jaut": "Aptuveni: 389 · 6 ≈ 400 · 6. Aizved līdz aptuvenajai "
                 "vērtībai.",
         "atb": 2400, "beigas": 5000, "iedala": 500,
         "merkis": "≈ 2400", "objekts": "Skūteris",
         "padoms": "4 simti · 6 = 24 simti.",
         "stasts": "Skūteris brauc līdz aptuvenajai vērtībai."},
        {"jaut": "Aptuveni: 712 · 5 ≈ 700 · 5. Kur?",
         "atb": 3500, "beigas": 5000, "iedala": 500,
         "merkis": "≈ 3500", "objekts": "Skūteris",
         "padoms": "7 simti · 5."},
        {"jaut": "Aptuveni: 198 · 9 ≈ 200 · 9. Kur?",
         "atb": 1800, "beigas": 5000, "iedala": 500,
         "merkis": "≈ 1800", "objekts": "Skūteris",
         "padoms": "2 simti · 9."},
        {"jaut": "Aptuveni: 505 · 8 ≈ 500 · 8. Kur?",
         "atb": 4000, "beigas": 5000, "iedala": 500,
         "merkis": "≈ 4000", "objekts": "Skūteris",
         "padoms": "5 simti · 8."},
    ], pamats=2),

    Ievadi("Aptuveni līdz simtiem", [
        {"jaut": "294 · 3 ≈ ?", "atb": ["900"], "padoms": "300 · 3."},
        {"jaut": "812 · 4 ≈ ?", "atb": ["3200"], "padoms": "800 · 4."},
        {"jaut": "651 · 5 ≈ ?", "atb": ["3500"], "padoms": "700 · 5."},
        {"jaut": "149 · 6 ≈ ?", "atb": ["600"], "padoms": "100 · 6."},
    ]),

    Varianti("Vai ticams?", [
        {"jaut": "419 · 5 = 2095. Ticams?",
         "opcijas": ["jā", "nē"], "pareizi": 0,
         "padoms": "400 · 5 = 2000."},
        {"jaut": "703 · 6 = 4818. Ticams?",
         "opcijas": ["nē", "jā"], "pareizi": 0,
         "padoms": "700 · 6 = 4200; pareizi 4218."},
        {"jaut": "288 · 3 = 564. Ticams?",
         "opcijas": ["nē", "jā"], "pareizi": 0,
         "padoms": "300 · 3 = 900; pareizi 864."},
        {"jaut": "Cik ciparu būs reizinājumā 897 · 9?",
         "opcijas": ["4", "3", "5", "2"], "pareizi": 0,
         "padoms": "900 · 9 = 8100."},
    ], pamats=4),

    Pasaule("Skūteru nomas punkts",
            Ievadi("", [
                {"jaut": "Elektroskūteris maksā 389 €. Cik maksā 6 skūteri "
                         "precīzi?",
                 "atb": ["2334"], "padoms": "389 · 6."},
                {"jaut": "Ķiveres pa 42 € - cik par 6 ķiverēm?",
                 "atb": ["252"], "padoms": "42 · 6."},
                {"jaut": "Aptuveni: vai 2334 + 252 ir mazāk par 3000 €? "
                         "Raksti «jā» vai «nē».",
                 "atb": ["jā", "ja"], "tastatura": "text",
                 "padoms": "2300 + 300 = 2600."},
                {"jaut": "Precīzi: cik maksā viss pirkums?",
                 "atb": ["2586"], "padoms": "2334 + 252."},
            ]),
            pavediens="tehnika",
            konteksts="Nomas punkts pērk skūterus un ķiveres - vispirms "
                      "novērtē, vai budžets pietiks.",
            kapec="Aptuvenais rēķins galvā pasaka, vai vērts rēķināt "
                  "precīzi."),

    Kopsavilkums([
        "Novērtēju reizinājumu, noapaļojot līdz simtiem.",
        "Salīdzinu precīzo atbildi ar aptuveno.",
        "Pamanu, ja atbildē ir par daudz vai par maz ciparu.",
    ]),

    Majas([
        "Novērtē, cik maksā 4 lietas, ko gribētu nopirkt, un tad izrēķini "
        "precīzi.",
        "Novērtē, cik lappušu izlasīsi 7 dienās, ja dienā lasi ap 30.",
        "Izdomā aplamu reizinājumu, ko var atmaskot ar aptuveno vērtību.",
    ]),
]
