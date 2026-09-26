# -*- coding: utf-8 -*-
"""4. klase, 52. stunda: «Kādas malas ir taisnstūrim?»

Taisnstūris apvieno abas jaunās idejas: pretējās malas paralēlas, blakus
malas perpendikulāras. Kvadrāts ir taisnstūris ar vienādām malām. Stunda
pieraksta šīs īpašības ar ∥ un ⊥ un pārbauda, vai citiem četrstūriem tās ir.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, figura)

TEMA = "Kādas malas ir taisnstūrim?"

MERKIS = ("Paskaidrosim, ka taisnstūra pretējās malas ir paralēlas, bet "
          "blakus malas - perpendikulāras.")

SATURS = [
    Sakums("Kāpēc ekrāni ir taisnstūri?",
           zimejums=figura([(1, 1), (11, 1), (11, 6), (1, 6)],
                           uzraksti=[(0.4, 0.4, "A"), (11.6, 0.4, "B"),
                                     (11.6, 6.6, "C"), (0.4, 6.6, "D")],
                           platums=12, augstums=7),
           paraksts="AB ∥ DC, AD ∥ BC; AB ⊥ BC.",
           fakti=["Taisnstūrus viegli salikt blakus bez spraugām.",
                  "Tāpēc ekrāni, flīzes un grāmatas ir taisnstūri."]),

    Doma("Pretējās malas ∥, blakus malas ⊥",
         "Taisnstūrim pretējās malas ir paralēlas un vienādi garas, bet blakus "
         "malas ir perpendikulāras.",
         soli=[
             "Pretējās malas: AB un DC, AD un BC.",
             "Pretējās malas ir paralēlas: AB ∥ DC, AD ∥ BC.",
             "Blakus malas krustojas taisnā leņķī: AB ⊥ BC.",
             "Kvadrāts ir taisnstūris, kuram visas malas vienādas.",
         ],
         pieze="Ja četrstūrim ir 4 taisni leņķi, tas ir taisnstūris - "
               "pretējās malas tad paralēlas pašas no sevis."),

    Paraugs("Taisnstūra malu pāri",
            uzd="Taisnstūrī ABCD nosauc visus paralēlo un perpendikulāro malu "
                "pārus.",
            soli=[
                ("AB ∥ DC, AD ∥ BC", "2 paralēlu malu pāri."),
                ("AB ⊥ BC, BC ⊥ CD, CD ⊥ DA, DA ⊥ AB",
                 "4 perpendikulāru malu pāri - katrā virsotnē viens."),
            ],
            atbilde="2 paralēli, 4 perpendikulāri pāri"),

    Zimejums("Vai šim četrstūrim ir paralēlas malas?",
             figura([(1, 1), (11, 1), (8, 5), (3, 5)],
                    uzraksti=[(6, 0.4, "AB"), (5.5, 5.6, "DC")],
                    platums=12, augstums=6),
             paskaidro="AB ∥ DC, bet sānu malas nav paralēlas un stūri nav "
                       "taisni - tā ir trapece, nevis taisnstūris.",
             ievads="Ne katrs četrstūris ar paralēlām malām ir taisnstūris."),

    Varianti("Taisnstūris vai nav?", [
        {"jaut": "Četrstūrim 4 taisni leņķi. Tas ir...",
         "opcijas": ["taisnstūris", "trapece", "nevar zināt"], "pareizi": 0,
         "padoms": "Tā ir taisnstūra pazīme."},
        {"jaut": "Vai kvadrāts ir taisnstūris?",
         "opcijas": ["jā", "nē"], "pareizi": 0,
         "padoms": "4 taisni leņķi - jā, vēl arī vienādas malas."},
        {"jaut": "Vai taisnstūris vienmēr ir kvadrāts?",
         "opcijas": ["nē", "jā"], "pareizi": 0,
         "padoms": "Malas var būt dažādas."},
        {"jaut": "Taisnstūrī AB ∥ ...",
         "opcijas": ["DC", "BC", "AD", "AC"], "pareizi": 0,
         "padoms": "Pretējā mala."},
        {"jaut": "Taisnstūrī AD ⊥ ...",
         "opcijas": ["AB", "BC", "AD", "neviena"], "pareizi": 0,
         "padoms": "Blakus mala virsotnē A."},
    ], pamats=3),

    Ievadi("Malu garumi", [
        {"jaut": "Taisnstūrī AB = 8 cm. Cik garš ir DC?", "atb": ["8"],
         "padoms": "Pretējās malas vienādas."},
        {"jaut": "Taisnstūra malas 8 cm un 5 cm. Cik ir perimetrs?",
         "atb": ["26"], "padoms": "8 + 5 + 8 + 5."},
        {"jaut": "Kvadrāta mala 7 cm. Perimetrs?", "atb": ["28"],
         "padoms": "4 · 7."},
        {"jaut": "Taisnstūra perimetrs 30 cm, viena mala 10 cm. Otra mala?",
         "atb": ["5"], "padoms": "30 : 2 = 15; 15 − 10."},
    ]),

    Pasaule("Futbola laukums",
            Ievadi("", [
                {"jaut": "Laukums ir taisnstūris 105 m × 68 m. Cik metru ir "
                         "otrā garā mala?",
                 "atb": ["105"], "padoms": "Pretējās malas vienādas."},
                {"jaut": "Cik metru ir apkārt laukumam (perimetrs)?",
                 "atb": ["346"], "padoms": "105 + 68 + 105 + 68."},
                {"jaut": "Cik taisnu leņķu ir laukuma stūros?",
                 "atb": ["4"], "padoms": "Tas ir taisnstūris."},
                {"jaut": "Futbolists 3 reizes aprisina laukumam apkārt. Cik "
                         "metru?",
                 "atb": ["1038"], "padoms": "346 · 3."},
            ]),
            pavediens="sports",
            konteksts="Oficiālais futbola laukums ir taisnstūris; tā līnijas "
                      "velk ar auklu un uzstūri.",
            kapec="Ja stūri nav taisni, laukums ir greizs un noteikumi "
                  "negodīgi."),

    Kopsavilkums([
        "Zinu, ka taisnstūra pretējās malas ir paralēlas un vienādas.",
        "Zinu, ka blakus malas ir perpendikulāras.",
        "Atšķiru taisnstūri no citiem četrstūriem.",
        "Zinu, ka kvadrāts ir īpašs taisnstūris.",
    ]),

    Majas([
        "Izmēri divas taisnstūrveida lietas mājās un pārbaudi pretējās malas.",
        "Uzzīmē četrstūri ar vienu paralēlu malu pāri, kas nav taisnstūris.",
        "Izrēķini sava galda perimetru.",
    ]),
]
