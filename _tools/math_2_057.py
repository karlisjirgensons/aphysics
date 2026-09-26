# -*- coding: utf-8 -*-
"""2. klase, 57. stunda: «Cik ilgi tu skrien 100 metrus?»

Īsu notikumu mēra ar hronometru minūtēs un sekundēs. 1 minūtē ir 60
sekunžu, tāpēc 75 sekundes ir 1 minūte un 15 sekundes. Sportā uzvar mazākais
laiks - tas ir otrādi nekā tāllēkšanā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Varianti, restis)

TEMA = "Cik ilgi tu skrien 100 metrus?"

MERKIS = ("Šodien ar hronometru mērīsim reāla notikuma ilgumu un "
          "pierakstīsim to minūtēs un sekundēs.")

_SKREJIENS = restis([["vārds", "laiks"], ["Kārlis", "19 s"],
                     ["Dace", "21 s"], ["Rihards", "18 s"],
                     ["Ance", "20 s"]])

SATURS = [
    Sakums("Ātrākais cilvēks noskrien 100 m mazāk nekā 10 sekundēs. Un "
           "tu?",
           zimejums=_SKREJIENS,
           paraksts="2. klases skrējiens - apmēram 20 sekundes.",
           fakti=["Sekunde - apmēram tik ilgi, cik pasaki «viens-divi».",
                  "1 minūte = 60 sekundes.",
                  "Skrējienā uzvar mazākais laiks."]),

    Doma("Minūtes un sekundes",
         "1 min = 60 s; ilgāku laiku pieraksta minūtēs un sekundēs.",
         soli=[
             "Hronometru ieslēdz startā un aptur finišā.",
             "Līdz 60 sekundēm raksta: 45 s.",
             "Vairāk nekā 60 s: 75 s = 60 s + 15 s = 1 min 15 s.",
             "Salīdzinot - mazāks laiks nozīmē ātrāk.",
         ]),

    Ievadi("Rēķini ar sekundēm", [
        {"jaut": "Par cik sekundēm Rihards bija ātrāks nekā Dace?",
         "zim": _SKREJIENS, "atb": ["3"], "mers": "s", "padoms": "21 − 18."},
        {"jaut": "Cik sekunžu ir 1 min 20 s?", "atb": ["80"], "mers": "s",
         "padoms": "60 + 20."},
        {"jaut": "90 s = 1 min un cik sekundes?", "atb": ["30"], "mers": "s",
         "padoms": "90 − 60."},
        {"jaut": "Cik sekunžu ir pusminūtē?", "atb": ["30"], "mers": "s",
         "padoms": "Puse no 60."},
        {"jaut": "Cik sekunžu ir 1 min 45 s?", "atb": ["105"],
         "mers": "s", "padoms": "60 + 45."},
        {"jaut": "Kārlis nākamreiz skrēja par 2 s ātrāk. Kāds laiks?",
         "zim": _SKREJIENS, "atb": ["17"], "mers": "s",
         "padoms": "19 − 2."},
    ], pamats=4),

    Varianti("Kurš uzvar?", [
        {"jaut": "Kurš skrēja visātrāk?", "zim": _SKREJIENS,
         "opcijas": ["Rihards", "Dace", "Kārlis"], "pareizi": 0,
         "padoms": "Mazākais laiks."},
        {"jaut": "Kurš bija ceturtais?", "zim": _SKREJIENS,
         "opcijas": ["Dace", "Ance", "Kārlis"], "pareizi": 0,
         "padoms": "18, 19, 20, 21."},
    ]),

    Petijums("Mēri ar hronometru", [
        "Pārī: viens skrien 30 m, otrs mēra ar hronometru.",
        "Pieraksti laiku sekundēs.",
        "Apmainieties lomām.",
        "Kurš bija ātrāks? Par cik sekundēm?",
    ], vajag="hronometrs vai telefons, 30 m celiņš"),

    Pasaule("Cik ilgi vārīt olu?",
            Ievadi("", [
                {"jaut": "Mīksta ola vārās 4 minūtes. Pagāja 3 minūtes. "
                         "Cik sekunžu vēl?", "atb": ["60"], "mers": "s",
                 "padoms": "Vēl 1 minūte."},
                {"jaut": "Pagāja 3 min 30 s. Cik sekunžu vēl?",
                 "atb": ["30"], "mers": "s", "padoms": "Puse minūtes."},
            ]),
            pavediens="virtuve",
            konteksts="Virtuves taimeris skaita sekundes.",
            kapec="Pāris lieku minūšu - un ola jau cieta."),

    Kopsavilkums([
        "Mēru ilgumu ar hronometru.",
        "Zinu, ka 1 min = 60 s.",
        "Pārveidoju sekundes minūtēs un sekundēs.",
    ]),

    Majas([
        "Izmēri, cik ilgi tu tīri zobus.",
        "Izmēri, cik ilgi uzvelc apavus.",
        "Kas notiek ilgāk? Par cik sekundēm?",
    ]),
]
