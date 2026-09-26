# -*- coding: utf-8 -*-
"""2. klase, 51. stunda: «Cik centu ir 0,05 € un 0,50 €?»

Cenu zīmēs naudu raksta ar komatu: 0,50 € ir 50 centu, 0,05 € - 5 centi.
Skolēns decimāldaļas vēl nemācās; te tikai lasa pierakstu - pirms komata
eiro, pēc komata centi (divi cipari).
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, monetas, restis)

TEMA = "Cik centu ir 0,05 € un 0,50 €?"

MERKIS = ("Šodien lasīsim un salīdzināsim naudas summas, kas pierakstītas "
          "ar komatu.")

SATURS = [
    Sakums("Kas ir dārgāks - 0,05 € vai 0,50 €?",
           zimejums=monetas(["5 c", "50 c"]),
           paraksts="5 centi un 50 centi.",
           fakti=["Pirms komata - eiro, pēc komata - centi.",
                  "0,05 € = 5 c, 0,50 € = 50 c.",
                  "1 € = 100 c."]),

    Doma("Naudas pieraksts ar komatu",
         "Pēc komata vienmēr ir divi cipari - tie ir centi.",
         soli=[
             "2,35 €: 2 eiro un 35 centi.",
             "0,50 €: 0 eiro un 50 centi.",
             "0,05 €: 0 eiro un 5 centi - nulle priekšā!",
             "Salīdzina vispirms eiro, tad centus.",
         ]),

    Ievadi("Cik centu?", [
        {"jaut": "0,20 € = ? c", "atb": ["20"], "padoms": "Pēc komata 20."},
        {"jaut": "0,02 € = ? c", "atb": ["2"], "padoms": "Pēc komata 02."},
        {"jaut": "0,75 € = ? c", "atb": ["75"], "padoms": "Pēc komata 75."},
        {"jaut": "1,00 € = ? c", "atb": ["100"], "padoms": "1 € = 100 c."},
        {"jaut": "Cik eiro ir 3,40 €? (tikai veselie)", "atb": ["3"],
         "padoms": "Pirms komata."},
        {"jaut": "Cik centu ir 3,40 € pēc komata?", "atb": ["40"],
         "padoms": "Pēc komata."},
    ], pamats=4),

    Varianti("Kas dārgāks?", [
        {"jaut": "Kura cena lielāka?", "opcijas": ["0,50 €", "0,05 €"],
         "jaukt": False, "pareizi": 0, "padoms": "50 c un 5 c."},
        {"jaut": "Kura cena lielāka?", "opcijas": ["1,10 €", "0,99 €"],
         "jaukt": False, "pareizi": 0, "padoms": "1 eiro ir vairāk nekā 0."},
        {"jaut": "Kā pierakstīt 8 centus?",
         "opcijas": ["0,08 €", "0,8 €", "8,00 €"], "pareizi": 0,
         "padoms": "Divi cipari pēc komata."},
        {"jaut": "Kura cena lielāka?", "opcijas": ["2,30 €", "2,03 €"],
         "jaukt": False, "pareizi": 0, "padoms": "30 c un 3 c."},
    ]),

    Pasaule("Cenas kioskā",
            Varianti("", [
                {"jaut": "Kas ir vislētākais?",
                 "opcijas": ["konfekte", "bulciņa", "sula"], "pareizi": 0,
                 "padoms": "Mazākais skaitlis."},
                {"jaut": "Tev ir 50 c monēta. Ko vari nopirkt?",
                 "opcijas": ["konfekti un bulciņu", "tikai sulu",
                             "neko"], "pareizi": 0,
                 "padoms": "5 c + 45 c = 50 c."},
            ]),
            pavediens="veikals",
            zimejums=restis([["prece", "cena"], ["konfekte", "0,05 €"],
                             ["bulciņa", "0,45 €"], ["sula", "0,80 €"]]),
            konteksts="Skolas kioskā cenas raksta ar komatu.",
            kapec="Cenu zīmes jālasa pareizi, lai pietiktu naudas."),

    Kopsavilkums([
        "Lasu naudas summas ar komatu.",
        "Pārvēršu tās centos.",
        "Salīdzinu cenas.",
    ]),

    Majas([
        "Atrodi mājās 3 čekus vai cenu zīmes.",
        "Pieraksti katru cenu eiro un centos.",
        "Kura prece bija visdārgākā?",
    ]),
]
