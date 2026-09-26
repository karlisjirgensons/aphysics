# -*- coding: utf-8 -*-
"""1. klase, 36. stunda: «Cik palika somā?»

Situācijas «pienāk» un «aiziet»: skolēns izlemj, vai darbība ir «+» vai
«−», pieraksta to un aprēķina. Atbildi pasaka teikumā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, bildes)

TEMA = "Cik palika somā?"

MERKIS = ("Šodien risināsim stāstus par to, kas pienāk un kas aiziet, un "
          "pierakstīsim tos ar darbību.")

SATURS = [
    Sakums("Somā 7 grāmatas, 3 izņēma. Cik palika?",
           zimejums=bildes([[("gramata", 4), ("gramata*", 3)]]),
           paraksts="Oranžās izņēma: 7 − 3 = 4.",
           fakti=["Izņēma, atdeva, apēda - «−».",
                  "Ielika, atnāca, nopirka - «+».",
                  "Atbildi pasaki teikumā."]),

    Paraugs("Stāsts par somu",
            uzd="Somā ir 7 grāmatas. Toms izņēma 3. Cik grāmatu palika "
                "somā?",
            soli=[
                ("7 − 3", "Izņēma - kļūst mazāk."),
                ("7 − 3 = 4", "Skaiti atpakaļ 3."),
            ],
            atbilde="somā palika 4 grāmatas."),

    Doma("Stāsts → darbība → atbilde",
         "Vispirms izlem, vai kļūst vairāk vai mazāk.",
         soli=[
             "Cik bija sākumā?",
             "Kas notika: klāt vai prom?",
             "Uzraksti darbību un aprēķini.",
             "Atbildi teikumā.",
         ]),

    Ievadi("Aprēķini", [
        {"jaut": "Somā 5 zīmuļi. Ieliek vēl 3. Cik tagad?", "atb": ["8"],
         "padoms": "5 + 3."},
        {"jaut": "Maisā 9 konfektes. Apēda 4. Cik palika?", "atb": ["5"],
         "padoms": "9 − 4."},
        {"jaut": "Plauktā 6 bumbas. Paņēma 6. Cik palika?", "atb": ["0"],
         "padoms": "Visas paņēma."},
        {"jaut": "Garāžā 2 mašīnas. Atbrauca vēl 5. Cik tagad?",
         "atb": ["7"], "padoms": "2 + 5."},
        {"jaut": "Kokā 8 putni. Aizlidoja 5. Cik palika?", "atb": ["3"],
         "padoms": "8 − 5."},
        {"jaut": "Vāzē 4 puķes. Ieliek vēl 6. Cik tagad?", "atb": ["10"],
         "padoms": "4 + 6."},
    ], pamats=4),

    Varianti("Kura darbība?", [
        {"jaut": "Ievai bija 6 uzlīmes, 2 viņa uzdāvināja.",
         "opcijas": ["6 − 2", "6 + 2"], "jaukt": False, "pareizi": 0,
         "padoms": "Uzdāvināja - palika mazāk."},
        {"jaut": "Mārim bija 3 marķieri, nopirka vēl 4.",
         "opcijas": ["3 + 4", "4 − 3"], "jaukt": False, "pareizi": 0,
         "padoms": "Nopirka - vairāk."},
    ]),

    Pasaule("Skolas soma",
            Ievadi("", [
                {"jaut": "Rītā somā bija 4 burtnīcas. Skolā iedeva vēl 2. "
                         "Cik tagad?", "atb": ["6"], "padoms": "4 + 2."},
                {"jaut": "1 burtnīcu atstāja skolā. Cik atnesa mājās?",
                 "atb": ["5"], "padoms": "6 − 1."},
            ]),
            pavediens="skola",
            konteksts="Pa dienu somā lietas nāk klāt un aiziet.",
            kapec="Katrs solis - viena darbība."),

    Kopsavilkums([
        "Izlemju, vai stāstā ir «+» vai «−».",
        "Pierakstu darbību un aprēķinu.",
        "Atbildu teikumā.",
    ]),

    Majas([
        "Saskaiti grāmatas savā somā. Izņem dažas - cik palika?",
        "Izdomā stāstu par «palika» un izrēķini.",
        "Pastāsti mājiniekam stāstu un atbildi teikumā.",
    ]),
]
