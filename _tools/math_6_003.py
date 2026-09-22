# -*- coding: utf-8 -*-
"""6. klase, 3. stunda: «Kā attiecību pieraksta?»

Trīs pieraksti vienai un tai pašai lietai: ar vārdu «pret», ar kolu un ar
daļsvītru. Pēdējais ir svarīgākais - tieši tas attiecību savieno ar daļām,
kuras skolēns jau prot, un vēlāk ļauj attiecību saīsināt.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti)

TEMA = "Kā attiecību pieraksta?"

MERKIS = ("Iemācīsimies vienu un to pašu attiecību pierakstīt ar vārdu "
          "«pret», ar kolu un ar daļsvītru.")

SATURS = [
    Sakums("Trīs pieraksti, viena doma",
           fakti=["«divi pret trīs» - tā saka.",
                  "2 : 3 - tā raksta receptē un uz iepakojuma.",
                  "{2|3} - tā raksta, kad attiecību grib rēķināt."]),

    Doma("Attiecība ir dalījums",
         "Pieraksts a : b nozīmē to pašu, ko daļa {a|b} - cik reižu pirmais "
         "ir lielāks vai mazāks par otro.",
         soli=[
             "Uzraksti attiecību ar vārdu «pret» - tā to izlasa.",
             "To pašu uzraksti ar kolu: pirmais skaitlis, kols, otrais.",
             "To pašu uzraksti kā daļu: pirmais skaitītājā, otrais saucējā.",
             "Pārbaudi, vai secība visos trijos pierakstos ir viena un tā "
             "pati.",
         ],
         pieze="Tāpēc attiecību drīkst saīsināt tāpat kā daļu: 4 : 6 ir tas "
               "pats, kas 2 : 3, jo {4|6} = {2|3}."),

    Paraugs("Pieraksti vienu attiecību trīs veidos",
            uzd="Klasē ir 12 meitenes un 16 zēni. Kāda ir meiteņu attiecība "
                "pret zēniem?",
            soli=[
                ("12 pret 16",
                 "Vispirms - tieši tā, kā teikumā."),
                ("12 : 16",
                 "Tas pats ar kolu."),
                ("{12|16} = {3|4}",
                 "Kā daļu var saīsināt: abus dala ar 4."),
                ("Atbilde: 3 : 4",
                 "Saīsinātais pieraksts stāsta to pašu, tikai īsāk."),
            ],
            atbilde="12 : 16 = 3 : 4"),

    Ievadi("Saīsini attiecību", [
        {"jaut": "Uzraksti attiecību 4 : 6 saīsinātā veidā. (piemēram 1:2)",
         "atb": ["2:3"], "padoms": "Abus dali ar 2."},
        {"jaut": "Saīsini 10 : 15.", "atb": ["2:3"], "padoms": "Abus dali "
                                                               "ar 5."},
        {"jaut": "Saīsini 20 : 5.", "atb": ["4:1"], "padoms": "Abus dali "
                                                              "ar 5."},
        {"jaut": "Saīsini 100 : 40.", "atb": ["5:2"], "padoms": "Abus dali "
                                                                "ar 20."},
        {"jaut": "Saīsini 9 : 12.", "atb": ["3:4"], "padoms": "Abus dali "
                                                              "ar 3."},
        {"jaut": "Saīsini 24 : 36.", "atb": ["2:3"], "padoms": "Abus dali "
                                                               "ar 12."},
    ], pamats=4,
        ievads="Atbildi raksti ar kolu, piemēram 2:3."),

    Varianti("Kurš pieraksts ir tas pats?", [
        {"jaut": "Kurš pieraksts nozīmē to pašu, ko «3 pret 5»?",
         "opcijas": ["3 : 5", "5 : 3", "3 + 5", "5 − 3"],
         "pareizi": 0,
         "padoms": "Secība nemainās."},
        {"jaut": "Attiecību 6 : 8 var saīsināt līdz...",
         "opcijas": ["3 : 4", "2 : 3", "6 : 8 nevar saīsināt", "1 : 2"],
         "pareizi": 0,
         "padoms": "Abus dali ar 2."},
        {"jaut": "Kāpēc attiecību drīkst saīsināt?",
         "opcijas": ["Tā ir daļa, un daļas pamatīpašība to atļauj",
                     "Jo skaitļi kļūst mazāki",
                     "Tā ir atsevišķa kārtula tikai attiecībām",
                     "Drīkst tikai tad, ja abi ir pāra"],
         "pareizi": 0,
         "padoms": "5. klasē to pašu darīja ar daļām."},
        {"jaut": "Klasē 12 meitenes un 16 zēni. Kāda ir zēnu attiecība pret "
                 "meitenēm?",
         "opcijas": ["4 : 3", "3 : 4", "12 : 16", "16 : 28"],
         "pareizi": 0,
         "padoms": "Tagad pirmais nosauktais ir zēni."},
    ], pamats=4),

    Pasaule("Kā pierakstīt maisījumu?",
            Ievadi("", [
                {"jaut": "Javā 2 maisi cementa un 8 maisi smilšu. Pieraksti "
                         "saīsinātu attiecību. (piemēram 1:2)",
                 "atb": ["1:4"], "padoms": "Abus dali ar 2."},
                {"jaut": "Krāsā 6 l krāsas un 4 l ūdens. Saīsināta "
                         "attiecība?",
                 "atb": ["3:2"], "padoms": "Abus dali ar 2."},
                {"jaut": "Dārzā 15 kvadrātmetri dobju un 5 celiņu. Saīsināta "
                         "attiecība?",
                 "atb": ["3:1"], "padoms": "Abus dali ar 5."},
                {"jaut": "Sienā 9 kvadrātmetri loga un 27 sienas. Saīsināta "
                         "attiecība?",
                 "atb": ["1:3"], "padoms": "Abus dali ar 9."},
            ]),
            pavediens="maja",
            konteksts="Veikalā materiālu attiecību raksta ar kolu, receptē - "
                      "ar vārdiem, bet rēķinā tā kļūst par daļu.",
            kapec="Saīsināta attiecība ir vieglāk lasāma un nemaina nozīmi."),

    Kopsavilkums([
        "Pierakstu attiecību ar vārdu «pret», ar kolu un ar daļsvītru.",
        "Zinu, ka attiecība ir dalījums, tāpēc to drīkst saīsināt.",
        "Saīsinu attiecību, dalot abus skaitļus ar vienu un to pašu.",
        "Ievēroju secību arī tad, kad pieraksts mainās.",
    ]),

    Majas([
        "Saskaiti mājās divas lietas (piemēram, karotes un dakšiņas) un "
        "pieraksti to attiecību trīs veidos.",
        "Saīsini to, ja var.",
        "Atrodi iepakojumu, uz kura attiecība jau ir saīsināta.",
    ]),
]
