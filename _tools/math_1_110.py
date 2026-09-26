# -*- coding: utf-8 -*-
"""1. klase, 110. stunda: «Ko nozīmē «tikpat un vēl»?»

«Tikpat un vēl 2» - otrai rindai noliek tikpat, cik pirmajā, un vēl 2.
Tas ir tas pats, kas «par 2 vairāk»: 6 + 2 = 8.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, bildes)

TEMA = "Ko nozīmē «tikpat un vēl»?"

MERKIS = ("Šodien modelēsim «tikpat un vēl» un pierakstīsim to ar darbību.")

SATURS = [
    Sakums("Annai 6 pogas, Jānim tikpat un vēl 2. Cik Jānim?",
           zimejums=bildes([[("ripina", 6)], [("ripina", 6),
                                                ("ripina*", 2)]],
                           uzraksti=["Anna", "Jānis"]),
           paraksts="Tikpat (6) un vēl 2 (oranžās): 6 + 2 = 8.",
           fakti=["«Tikpat» - tas pats skaits.",
                  "«Un vēl 2» - pieliek 2.",
                  "Tas ir «par 2 vairāk»."]),

    Slidnis("Kā modelē", [
        {"v": "tikpat", "teksts": "Noliec tikpat, cik Annai",
         "zim": bildes([[("ripina", 6)], [("ripina", 6)]],
                       uzraksti=["Anna", "Jānis"])},
        {"v": "un vēl 2", "teksts": "Pieliec vēl 2",
         "zim": bildes([[("ripina", 6)], [("ripina", 6), ("ripina*", 2)]],
                       uzraksti=["Anna", "Jānis"])},
    ]),

    Doma("Tikpat un vēl",
         "«Tikpat un vēl n» = pirmais skaitlis + n.",
         soli=[
             "Noliec tikpat.",
             "Pieliec vēl.",
             "Pieraksti: 6 + 2 = 8.",
         ],
         pieze="«Tikpat bez 2» - atņem: 6 − 2 = 4."),

    Ievadi("Aprēķini", [
        {"jaut": "Ievai 7 uzlīmes, Laurai tikpat un vēl 3. Cik Laurai?",
         "atb": ["10"], "padoms": "7 + 3."},
        {"jaut": "Grozā 9 āboli, otrā tikpat un vēl 4. Cik otrā?",
         "atb": ["13"], "padoms": "9 + 4."},
        {"jaut": "Plauktā 12 grāmatas, otrā tikpat bez 5. Cik otrā?",
         "atb": ["7"], "padoms": "12 − 5."},
        {"jaut": "Tev 8 konfektes, draugam tikpat un vēl 8. Cik draugam?",
         "atb": ["16"], "padoms": "8 + 8."},
    ]),

    Pasaule("Pusdienu galdi",
            Ievadi("", [
                {"jaut": "Pie galda 6 bērni. Pie otra tikpat un vēl 2. Cik "
                         "krēslu vajag otrajam galdam?", "atb": ["8"],
                 "padoms": "6 + 2."},
            ]),
            pavediens="skola",
            konteksts="Ēdnīcā bērni sēž pie diviem galdiem.",
            kapec="«Tikpat un vēl» palīdz saplānot krēslus."),

    Kopsavilkums([
        "Modelēju «tikpat un vēl».",
        "Pierakstu to ar «+».",
        "Zinu, ka «tikpat bez» ir «−».",
    ]),

    Majas([
        "Noliec 5 karotes un otrā rindā tikpat un vēl 3.",
        "Pieraksti ar darbību.",
        "Izdomā stāstu ar «tikpat un vēl».",
    ]),
]
