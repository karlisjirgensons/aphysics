# -*- coding: utf-8 -*-
"""4. klase, 111. stunda: «Kā aug daļu virkne?»

Mikrotemata noslēgums. Virkne {1|8}, {3|8}, {5|8}, ... aug par {2|8} ik
solī. Skolēns turpina virkni un formulē likumsakarību vārdiem - tā ir
algebriskās domāšanas sēkla ar daļām.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, taisne)

TEMA = "Kā aug daļu virkne?"

MERKIS = ("Turpināsim skaitļu virkni, ko veido daļas, un formulēsim "
          "likumsakarību.")

SATURS = [
    Sakums("Kas nāks pēc {5|8}?",
           zimejums=taisne(0, 1, 1, [(1 / 8.0, "1/8"), (3 / 8.0, "3/8"),
                                     (5 / 8.0, "5/8"), (7 / 8.0, "?")],
                           sikas=8),
           paraksts="Katrs solis - vēl divas astotdaļas.",
           fakti=["Virkne aug vienādos soļos.",
                  "Solis ir {2|8}."]),

    Doma("Atrodi soli - un turpini",
         "Daļu virknē ar vienādu saucēju solis ir skaitītāju starpība; "
         "katram nākamajam loceklim pieskaita soli.",
         soli=[
             "Salīdzini divus blakus locekļus: {3|8} − {1|8} = {2|8}.",
             "Pārbaudi ar nākamo pāri: {5|8} − {3|8} = {2|8}.",
             "Pieskaiti soli: {5|8} + {2|8} = {7|8}.",
             "Formulē: «katrs nākamais ir par {2|8} lielāks».",
         ],
         pieze="Virkne var arī samazināties: {9|10}, {7|10}, {5|10}, ... - "
               "solis «mīnus {2|10}»."),

    Paraugs("Turpini virkni",
            uzd="Turpini: {2|12}, {5|12}, {8|12}, ...",
            soli=[
                ("{5|12} − {2|12} = {3|12}", "Solis."),
                ("{8|12} + {3|12} = {11|12}", "Nākamais."),
                ("{11|12} + {3|12} = {14|12}", "Vēl nākamais - neīsta."),
            ],
            atbilde="{11|12}, {14|12}"),

    Slidnis("Virkne aug",
            soli=[
                {"v": "{1|6}", "teksts": "1. loceklis.", "josla": 17},
                {"v": "{2|6}", "teksts": "+ {1|6}.", "josla": 33},
                {"v": "{3|6}", "teksts": "+ {1|6}.", "josla": 50},
                {"v": "{4|6}", "teksts": "+ {1|6}.", "josla": 67},
                {"v": "{5|6}", "teksts": "+ {1|6}.", "josla": 83},
                {"v": "{6|6} = 1", "teksts": "Sasniegts veselais!",
                 "josla": 100},
            ]),

    Ievadi("Nākamais loceklis", [
        {"jaut": "{1|8}, {3|8}, {5|8}, ?", "atb": ["7/8"],
         "vieta": "piem., 1/2", "padoms": "+ {2|8}."},
        {"jaut": "{9|10}, {7|10}, {5|10}, ?", "atb": ["3/10"],
         "vieta": "piem., 1/2", "padoms": "− {2|10}."},
        {"jaut": "{1|5}, {4|5}, {7|5}, ?", "atb": ["10/5"],
         "vieta": "piem., 1/2", "padoms": "+ {3|5}."},
        {"jaut": "Cik locekļu virknē {1|4}, {2|4}, ... līdz {12|4}?",
         "atb": ["12"], "padoms": "Skaitītāji 1 līdz 12."},
    ]),

    Varianti("Kāda likumsakarība?", [
        {"jaut": "{2|7}, {4|7}, {6|7}, ...",
         "opcijas": ["katru reizi + {2|7}", "katru reizi + {1|7}",
                     "katru reizi · 2"], "pareizi": 0,
         "padoms": "4 − 2 = 2."},
        {"jaut": "{11|12}, {8|12}, {5|12}, ...",
         "opcijas": ["katru reizi − {3|12}", "katru reizi + {3|12}",
                     "katru reizi − {1|12}"], "pareizi": 0,
         "padoms": "11 − 8 = 3."},
        {"jaut": "Kāds būs 10. loceklis virknē {1|9}, {2|9}, {3|9}, ...?",
         "opcijas": ["{10|9}", "{10|90}", "{1|10}", "{9|10}"],
         "pareizi": 0, "padoms": "Skaitītājs = numurs."},
    ]),

    Pasaule("Mēness fāzes",
            Ievadi("", [
                {"jaut": "Mēness apgaismotā daļa pieaug: {1|8}, {2|8}, {3|8}. "
                         "Kāda būs nākamā?",
                 "atb": ["4/8"], "vieta": "piem., 1/2", "padoms": "+ {1|8}."},
                {"jaut": "Pēc cik soļiem no {1|8} būs pilnmēness ({8|8})?",
                 "atb": ["7"], "padoms": "8 − 1."},
                {"jaut": "Ja katrs solis ir apmēram 2 dienas, cik dienu līdz "
                         "pilnmēnesim?",
                 "atb": ["14"], "padoms": "7 · 2."},
                {"jaut": "Pēc pilnmēness daļa sarūk par {1|8}. Kāda būs pēc "
                         "{8|8}?",
                 "atb": ["7/8"], "vieta": "piem., 1/2", "padoms": "8 − 1."},
            ]),
            pavediens="kosmoss",
            konteksts="Mēness apgaismotā daļa katru nakti mainās - no jauna "
                      "mēness līdz pilnmēnesim apmēram 15 dienās.",
            kapec="Daļu virkne apraksta dabas ciklus."),

    Kopsavilkums([
        "Turpinu daļu virkni.",
        "Atrodu soli kā skaitītāju starpību.",
        "Formulēju likumsakarību vārdiem.",
    ]),

    Majas([
        "Nedēļu vēro Mēnesi un zīmē, kāda daļa apgaismota.",
        "Izdomā daļu virkni, kas samazinās, un palūdz kādu to turpināt.",
        "Uzraksti virkni no {1|10} līdz 1 ar soli {1|10}.",
    ]),
]
