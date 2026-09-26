# -*- coding: utf-8 -*-
"""2. klase, 132. stunda: «Kā izskatās virkne, kas dubultojas?»

Virkne, kurā katrs nākamais ir divreiz lielāks: 1, 2, 4, 8, 16, 32, 64.
Tā aug daudz ātrāk nekā «+2». Šūnu dalīšanās un papīra locīšana ir šādas
virknes piemēri.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, kolonnas)

TEMA = "Kā izskatās virkne, kas dubultojas?"

MERKIS = ("Šodien veidosim virkni, kurā katrs nākamais skaitlis ir divreiz "
          "lielāks, un aprakstīsim to.")

SATURS = [
    Sakums("Cik šūnu būs pēc 6 dalīšanās reizēm, ja sāk ar vienu?",
           zimejums=kolonnas([("0", 1), ("1", 2), ("2", 4), ("3", 8),
                              ("4", 16), ("5", 32), ("6", 64)]),
           paraksts="Katru reizi divreiz vairāk.",
           fakti=["Šūna dalās - no vienas rodas divas.",
                  "1, 2, 4, 8, 16, 32, 64.",
                  "Dubultošanās aug ļoti ātri!"]),

    Doma("Dubultošanās virkne",
         "Katrs nākamais = iepriekšējais + iepriekšējais.",
         soli=[
             "Sāc ar skaitli, piemēram, 3.",
             "Dubulto: 3 + 3 = 6.",
             "Dubulto vēlreiz: 6 + 6 = 12.",
             "Turpini: 24, 48, 96.",
         ],
         pieze="Salīdzini: + 2 virkne 2, 4, 6, 8, 10 aug lēnām; dubultošanās "
               "2, 4, 8, 16, 32 - strauji."),

    Slidnis("Papīra locīšana", [
        {"v": "1", "teksts": "Nesalocīts - 1 slānis."},
        {"v": "2", "teksts": "Pārloka uz pusēm - 2 slāņi."},
        {"v": "4", "teksts": "Vēlreiz - 4 slāņi."},
        {"v": "8", "teksts": "Vēlreiz - 8 slāņi."},
        {"v": "16", "teksts": "Vēlreiz - 16. Grūti salocīt!"},
    ]),

    Ievadi("Turpini", [
        {"jaut": "1, 2, 4, 8, ...", "atb": ["16"], "padoms": "8 + 8."},
        {"jaut": "3, 6, 12, 24, ...", "atb": ["48"], "padoms": "24 + 24."},
        {"jaut": "5, 10, 20, 40, ...", "atb": ["80"], "padoms": "40 + 40."},
        {"jaut": "Atpakaļ: 64, 32, 16, ...", "atb": ["8"],
         "padoms": "Puse no 16."},
        {"jaut": "Cik reizes jādubulto 1, lai iegūtu 32?", "atb": ["5"],
         "padoms": "2, 4, 8, 16, 32."},
        {"jaut": "Atpakaļ: 80, 40, 20, ...", "atb": ["10"],
         "padoms": "Puse no 20."},
    ], pamats=4),

    Varianti("Kura virkne dubultojas?", [
        {"jaut": "Kura?", "opcijas": ["2, 4, 8, 16", "2, 4, 6, 8",
                                      "2, 3, 4, 5"],
         "pareizi": 0, "padoms": "Katrs divreiz lielāks."},
        {"jaut": "Kura virkne aug ātrāk pēc 5 soļiem, sākot no 2?",
         "opcijas": ["dubultojot: 64", "pieskaitot 2: 12"], "jaukt": False,
         "pareizi": 0, "padoms": "2, 4, 8, 16, 32, 64."},
    ]),

    Pasaule("Ziņa sociālajos tīklos",
            Ievadi("", [
                {"jaut": "Tu pastāsti jaunumu 2 draugiem, katrs no viņiem - "
                         "vēl 2, un tā tālāk. 1. kārtā 2 cilvēki, 2. - 4. "
                         "Cik 4. kārtā?", "atb": ["16"],
                 "padoms": "2, 4, 8, 16."},
                {"jaut": "Cik 5. kārtā?", "atb": ["32"], "padoms": "16 + 16."},
            ]),
            pavediens="dati",
            konteksts="Jaunumi izplatās, katram pastāstot diviem.",
            kapec="Dubultošanās izskaidro, kāpēc ziņas izplatās tik ātri."),

    Kopsavilkums([
        "Veidoju virkni, kurā katrs nākamais ir divreiz lielāks.",
        "Turpinu to uz priekšu un atpakaļ.",
        "Zinu, ka dubultošanās aug ļoti ātri.",
    ]),

    Majas([
        "Pārloki papīra lapu uz pusēm, cik reizes vari.",
        "Saskaiti slāņus pēc katras reizes.",
        "Cik reizes izdevās pārlocīt?",
    ]),
]
