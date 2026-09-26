# -*- coding: utf-8 -*-
"""1. klase, 47. stunda: «Cik tev šķiet - un cik ir?»

Vispirms novērtē garumu pēc acumēra, tad izmēra un salīdzina. Vārdi:
«apmēram», «gandrīz», «nedaudz vairāk nekā». Laba aplēse ir tuvu īstajam.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Varianti, lineals)

TEMA = "Cik tev šķiet - un cik ir?"

MERKIS = ("Šodien vispirms novērtēsim garumu pēc acumēra un tad "
          "pārbaudīsim, izmērot.")

SATURS = [
    Sakums("Cik garš ir tavs zīmulis? Mini, pirms mēri!",
           zimejums=lineals(20, [(0, 13, "gandrīz 13 cm")]),
           paraksts="Apmēram 13 cm - gandrīz, bet ne pilnīgi.",
           fakti=["Aplēse - gudrs minējums pirms mērīšanas.",
                  "«Apmēram» - tuvu, bet ne precīzi.",
                  "Tad izmēri un salīdzini."]),

    Doma("Novērtē un pārbaudi",
         "Salīdzini ar kaut ko, ko zini: īkšķis ir apmēram 1 cm plats, "
         "skolas lineāls - 20 cm garš.",
         soli=[
             "Paskaties uz priekšmetu un nosauc aplēsi.",
             "Izmēri ar lineālu.",
             "Par cik aplēse atšķiras?",
         ]),

    Ievadi("Cik tuvu biji?", [
        {"jaut": "Tu minēji 8 cm, izmērīji 10 cm. Par cik kļūdījies?",
         "atb": ["2"], "padoms": "10 − 8."},
        {"jaut": "Tu minēji 12 cm, izmērīji 11 cm. Par cik kļūdījies?",
         "atb": ["1"], "padoms": "12 − 11."},
        {"jaut": "Cik cm apmēram? (vesels)", "zim": lineals(10, [(0, 6, "")]),
         "atb": ["6"], "padoms": "Gals pie 6."},
    ]),

    Varianti("Kura aplēse ticamāka?", [
        {"jaut": "Karotes garums",
         "opcijas": ["apmēram 15 cm", "apmēram 2 cm", "apmēram 100 cm"],
         "pareizi": 0, "padoms": "Garāka par plaukstu."},
        {"jaut": "Dzēšgumijas garums",
         "opcijas": ["apmēram 3 cm", "apmēram 30 cm", "apmēram 1 cm"],
         "pareizi": 0, "padoms": "Mazāka par pirkstu."},
        {"jaut": "Grāmatas garums",
         "opcijas": ["apmēram 20 cm", "apmēram 5 cm", "apmēram 90 cm"],
         "pareizi": 0, "padoms": "Apmēram kā skolas lineāls."},
    ]),

    Petijums("Mini un mēri", [
        "Izvēlies 4 priekšmetus uz sola.",
        "Katram uzraksti aplēsi centimetros.",
        "Izmēri un ieraksti īsto garumu blakus.",
        "Kura aplēse bija vistuvāk?",
    ], vajag="lineāls, lapa tabulai"),

    Pasaule("Vai kaste pietiks?",
            Varianti("", [
                {"jaut": "Tev jāiesaiņo lelle apmēram 25 cm gara. Kaste - "
                         "apmēram 20 cm. Vai ietilps?",
                 "opcijas": ["Nē, kaste par īsu", "Jā", "Nevar zināt"],
                 "pareizi": 0, "padoms": "25 ir vairāk nekā 20."},
            ]),
            pavediens="maja",
            konteksts="Dāvanu jāiesaiņo kastē.",
            kapec="Aplēse palīdz izlemt ātri, bez lineāla."),

    Kopsavilkums([
        "Novērtēju garumu pēc acumēra.",
        "Pārbaudu, izmērot.",
        "Lietoju vārdus apmēram un gandrīz.",
    ]),

    Majas([
        "Uzmini, cik cm gara ir tava pēda, un izmēri.",
        "Uzmini durvju roktura garumu un pārbaudi.",
        "Kura aplēse bija labākā?",
    ]),
]
