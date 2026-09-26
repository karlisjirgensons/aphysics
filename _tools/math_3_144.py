# -*- coding: utf-8 -*-
"""3. klase, 144. stunda: «Kā pieraksta atņemšanu stabiņā?»

Pieraksts ar aizņēmumu: kur liek svītru, kur raksta jauno ciparu un kā to
atzīmē, lai nepazustu. Grūtākais gadījums ir aizņemšanās caur nulli, un to
stunda parāda atsevišķi.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kā pieraksta atņemšanu stabiņā?"

MERKIS = ("Veidosim atņemšanas pierakstu stabiņā un aprēķināsim starpību.")

SATURS = [
    Sakums("Kā atzīmēt aizņēmumu, lai to neaizmirstu?",
           zimejums=restis([["3", "12", ""],
                            ["4", "2", "5"],
                            ["− 1", "8", "3"],
                            ["2", "4", "2"]],
                           "aizņēmumu raksta virs cipara"),
           paraksts="Pārsvītroto ciparu aizstāj jaunais, uzrakstīts virs tā.",
           fakti=["Aizņēmumu pieraksta virs cipara, lai to neaizmirstu.",
                  "Atņemšanu sāk no vieniem."]),

    Doma("Pārsvītro un uzraksti jauno ciparu",
       "Aizņemoties pārsvītro ciparu, no kura ņem, un virs tā uzraksti par "
       "vienu mazāku; vietai, kur trūka, pieraksti 10.",
         soli=[
             "Uzraksti skaitļus vienu zem otra, vietas pret vietām.",
             "Sāc no vieniem.",
             "Ja atņemt nevar, aizņemies un atzīmē to virs cipariem.",
             "Turpini ar desmitiem un simtiem.",
         ],
         pieze="Ja aizņemas caur nulli, jāiet vēl vienu vietu tālāk: no 802 "
               "vispirms simtu pārvērš desmitos, tad desmitu - vienos."),

    Paraugs("Kā atņemt 802 − 347?",
            uzd="Izrēķini stabiņā 802 − 347.",
            soli=[
                ("Vieni: 2 − 7 nesanāk",
                 "Desmitu vietā ir 0, tāpēc jāiet tālāk."),
                ("8 simti → 7 simti un 10 desmiti",
                 "Vispirms aizņemas no simtiem."),
                ("10 desmiti → 9 desmiti un 12 vieni",
                 "Tad no desmitiem."),
                ("12 − 7 = 5; 9 − 4 = 5; 7 − 3 = 4",
                 "Atbilde ir 455."),
            ],
            atbilde="455"),

    Ievadi("Atņem stabiņā", [
        {"jaut": "802 − 347 = ?", "atb": ["455"], "padoms": "Aizņemas caur "
                                                            "nulli."},
        {"jaut": "600 − 234 = ?", "atb": ["366"], "padoms": "Aizņemas caur "
                                                            "nulli."},
        {"jaut": "701 − 158 = ?", "atb": ["543"], "padoms": "Divi soļi."},
        {"jaut": "500 − 176 = ?", "atb": ["324"], "padoms": "Aizņemas caur "
                                                            "nulli."},
        {"jaut": "904 − 267 = ?", "atb": ["637"], "padoms": "Divi soļi."},
        {"jaut": "300 − 145 = ?", "atb": ["155"], "padoms": "Aizņemas caur "
                                                            "nulli."},
    ], pamats=4,
        ievads="Uzraksti katru piemēru burtnīcā stabiņā un ieraksti atbildi."),

    Zimejums("Aizņemšanās caur nulli",
             restis([["7", "9", "12"],
                     ["8", "0", "2"],
                     ["− 3", "4", "7"],
                     ["4", "5", "5"]],
                    "802 − 347"),
             paskaidro="Nulle nevar aizdot, tāpēc vispirms tā pati aizņemas "
                       "no simtiem.",
             ievads="Grūtākais atņemšanas gadījums."),

    Varianti("Kā pareizi pierakstīt?", [
        {"jaut": "No kuras vietas sāk atņemt stabiņā?",
         "opcijas": ["No vieniem", "No simtiem", "No desmitiem",
                     "Vienalga"],
         "pareizi": 0, "padoms": "Tikai tā zina, vai vajadzīgs aizņēmums."},
        {"jaut": "Ko dara, ja desmitu vietā ir nulle?",
         "opcijas": ["Aizņemas no simtiem", "Raksta nulli",
                     "Izlaiž vietu", "Atņem otrādi"],
         "pareizi": 0, "padoms": "Nulle pati aizņemas tālāk."},
        {"jaut": "Cik ir 400 − 128?",
         "opcijas": ["272", "282", "372", "262"],
         "pareizi": 0, "padoms": "Aizņemas caur nulli."},
        {"jaut": "Kur pieraksta aizņēmumu?",
         "opcijas": ["Virs cipara", "Zem svītras", "Blakus atbildei",
                     "Nekur"],
         "pareizi": 0, "padoms": "Lai to neaizmirstu."},
    ], pamats=4),

    Pasaule("Cik punktu atpaliek komanda?",
            Ievadi("", [
                {"jaut": "Līderim 802 punkti, otrajai komandai 347. Cik "
                         "punktu starpība?",
                 "atb": ["455"], "padoms": "802 − 347."},
                {"jaut": "Trešajai komandai 268 punkti. Cik tā atpaliek no "
                         "otrās?",
                 "atb": ["79"], "padoms": "347 − 268."},
                {"jaut": "Cik punktu ir otrajai un trešajai komandai kopā?",
                 "atb": ["615"], "padoms": "347 + 268."},
                {"jaut": "Par cik tas ir mazāk nekā līderim?",
                 "atb": ["187"], "padoms": "802 − 615."},
            ]),
            pavediens="sports",
            konteksts="Tabulā starpības rēķina katru kārtu - un punktu "
                      "skaits reti ir apaļš.",
            kapec="Viena aizmirsta aizņēmuma dēļ komanda tabulā pārlec citai "
                  "pāri."),

    Kopsavilkums([
        "Veidoju atņemšanas pierakstu stabiņā.",
        "Atzīmēju aizņēmumu virs cipariem.",
        "Atņemu arī tad, kad jāaizņemas caur nulli.",
        "Aprēķinu starpību un pārbaudu to.",
    ]),

    Majas([
        "Izrēķini stabiņā 700 − 356 un 905 − 478.",
        "Atzīmē katrā aizņēmumus.",
        "Pārbaudi abas atbildes ar saskaitīšanu.",
    ]),
]
