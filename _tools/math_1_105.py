# -*- coding: utf-8 -*-
"""1. klase, 105. stunda: «Cik veikli jau proti?»

Patstāvīgs darbs ar jauktiem piemēriem 20 apjomā: saskaitīšana un
atņemšana, ar un bez pāriešanas, nezināmais. Katrs pats pārbauda atbildes.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         ramis)

TEMA = "Cik veikli jau proti?"

MERKIS = ("Šodien patstāvīgi risināsim jauktus piemērus 20 apjomā un paši "
          "pārbaudīsim atbildes.")

SATURS = [
    Sakums("Jaukti piemēri - vai zini, kuru paņēmienu ņemt?",
           zimejums=ramis(14, 2, otra=6),
           paraksts="8 + 6: caur 10 - 14.",
           fakti=["Paskaties uz skaitļiem.",
                  "Izvēlies paņēmienu.",
                  "Pārbaudi ar pretējo darbību."]),

    Doma("Patstāvīgi",
         "Risini, pārbaudi, un tikai tad skaties padomu.",
         soli=[
             "Izrēķini.",
             "Pārbaudi: + ar −, − ar +.",
             "Ja nesakrīt - rēķini vēlreiz.",
         ]),

    Ievadi("1. daļa: saskaiti", [
        {"jaut": "8 + 6", "atb": ["14"], "padoms": "Caur 10."},
        {"jaut": "13 + 5", "atb": ["18"], "padoms": "3 + 5."},
        {"jaut": "9 + 9", "atb": ["18"], "padoms": "Dubultais."},
        {"jaut": "7 + 4", "atb": ["11"], "padoms": "7 + 3 + 1."},
        {"jaut": "6 + 5 + 4", "atb": ["15"], "padoms": "6 + 4 = 10."},
        {"jaut": "12 + 8", "atb": ["20"], "padoms": "2 + 8 = 10."},
    ], pamats=4),

    Ievadi("2. daļa: atņem", [
        {"jaut": "17 − 9", "atb": ["8"], "padoms": "17 − 7 − 2."},
        {"jaut": "19 − 6", "atb": ["13"], "padoms": "9 − 6."},
        {"jaut": "14 − 11", "atb": ["3"], "padoms": "Uz priekšu."},
        {"jaut": "12 − 7", "atb": ["5"], "padoms": "12 − 2 − 5."},
        {"jaut": "20 − 5", "atb": ["15"], "padoms": "Desmits un 5."},
        {"jaut": "11 − 8", "atb": ["3"], "padoms": "8 + 3 = 11."},
    ], pamats=4),

    Ievadi("3. daļa: atrodi ?", [
        {"jaut": "9 + ? = 16", "atb": ["7"], "padoms": "16 − 9."},
        {"jaut": "? − 5 = 8", "atb": ["13"], "padoms": "8 + 5."},
        {"jaut": "15 − ? = 9", "atb": ["6"], "padoms": "15 − 9."},
    ]),

    Pasaule("Sporta diena",
            Ievadi("", [
                {"jaut": "Mūsu komanda: 8 un 7 punkti divās kārtās. Cik "
                         "kopā?", "atb": ["15"], "padoms": "8 + 2 + 5."},
                {"jaut": "Pretiniekiem 19. Par cik viņi vairāk?",
                 "atb": ["4"], "padoms": "19 − 15."},
            ]),
            pavediens="sports",
            konteksts="Sporta dienā skaita punktus.",
            kapec="Veikls rēķins - ātrs rezultāts."),

    Kopsavilkums([
        "Risinu jauktus piemērus 20 apjomā.",
        "Pats pārbaudu atbildes.",
        "Zinu, kas vēl jātrenē.",
    ]),

    Majas([
        "Izrēķini 10 piemērus un pārbaudi.",
        "Pieraksti, kuri bija grūtākie.",
        "Trenē tos vēlreiz rīt.",
    ]),
]
