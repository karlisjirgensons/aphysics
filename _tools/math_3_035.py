# -*- coding: utf-8 -*-
"""3. klase, 35. stunda: «Cik veikli rēķinu galvā?»

Galvas rēķini 20 apjomā un tabula - tas ir pamats, uz kura stāv viss pārējais.
Šī stunda tos trenē ar ātrumu, bet uzsvars ir uz *paņēmienu*: ātrums nāk no
tā, ka skaitli sadala ērtāk, nevis no tā, ka skolēns steidzas.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, taisne)

TEMA = "Cik veikli rēķinu galvā?"

MERKIS = ("Veikli saskaitīsim un atņemsim 20 apjomā un reizināsim tabulas "
          "apjomā, izmantojot ērtus paņēmienus.")

SATURS = [
    Sakums("Kāpēc 8 + 7 ir vieglāk skaitīt caur desmit?",
           zimejums=taisne(0, 20, 5, [(15, "15")],
                           bultas=[(8, 10, "+2"), (10, 15, "+5")]),
           paraksts="8 + 7 ir 8 + 2 + 5 - vispirms līdz desmit.",
           fakti=["Desmit ir atbalsta punkts - pie tā skaitļi ir vienkārši.",
                  "Tāpēc summu sadala divās daļās: līdz 10 un pāri 10."]),

    Doma("Ātrums nāk no ērta sadalījuma",
         "Skaitli sadala tā, lai pa ceļam būtu apaļš desmits - tad rēķins "
         "notiek divos vienkāršos soļos.",
         soli=[
             "Paskaties, cik trūkst līdz tuvākajam desmitam.",
             "Pieskaiti tieši tik daudz.",
             "Pieskaiti atlikušo daļu.",
             "Atņemot dari to pašu otrādi: vispirms līdz desmitam.",
         ],
         pieze="Tas pats paņēmiens strādā arī ar lieliem skaitļiem: "
               "58 + 7 ir 58 + 2 + 5 = 65."),

    Paraugs("Cik ir 13 − 8?",
            uzd="Izrēķini 13 − 8, izmantojot desmitu kā atbalstu.",
            soli=[
                ("13 − 3 = 10",
                 "Vispirms nokāp līdz apaļam desmitam."),
                ("8 − 3 = 5",
                 "Tik daudz vēl jāatņem."),
                ("10 − 5 = 5",
                 "Otrais solis; atbilde ir 5."),
            ],
            atbilde="5"),

    Ievadi("Galvas rēķini", [
        {"jaut": "8 + 7 = ?", "atb": ["15"], "padoms": "8 + 2 + 5."},
        {"jaut": "15 − 9 = ?", "atb": ["6"], "padoms": "15 − 5 − 4."},
        {"jaut": "6 + 9 = ?", "atb": ["15"], "padoms": "6 + 4 + 5."},
        {"jaut": "17 − 8 = ?", "atb": ["9"], "padoms": "17 − 7 − 1."},
        {"jaut": "7 · 8 = ?", "atb": ["56"], "padoms": "49 + 7."},
        {"jaut": "54 : 6 = ?", "atb": ["9"], "padoms": "6 · 9 = 54."},
        {"jaut": "9 + 8 = ?", "atb": ["17"], "padoms": "9 + 1 + 7."},
        {"jaut": "14 − 6 = ?", "atb": ["8"], "padoms": "14 − 4 − 2."},
    ], pamats=6,
        ievads="Rēķini galvā un centies atbildēt bez pauzes."),

    Zimejums("Atbalsts uz skaitļu taisnes",
             taisne(0, 20, 5, [(9, "9"), (17, "17")],
                    bultas=[(9, 10, "+1"), (10, 17, "+7")]),
             paskaidro="Pirmais lēciens ir īss - tikai līdz desmitam; otrais "
                       "jau ir viegls.",
             ievads="Tā izskatās 9 + 8."),

    Varianti("Kurš paņēmiens ir ērtākais?", [
        {"jaut": "Kā ērtāk rēķināt 9 + 6?",
         "opcijas": ["9 + 1 + 5", "9 + 6 pa vienam", "6 + 6 + 3",
                     "10 + 6"],
         "pareizi": 0, "padoms": "Vispirms līdz desmitam."},
        {"jaut": "Kā ērtāk rēķināt 16 − 7?",
         "opcijas": ["16 − 6 − 1", "16 − 7 pa vienam", "16 − 10 + 3",
                     "7 − 16"],
         "pareizi": 0, "padoms": "Vispirms nokāp līdz desmitam."},
        {"jaut": "Kā ērtāk rēķināt 19 + 5?",
         "opcijas": ["20 + 5 − 1", "19 + 1 + 5 − 1", "19 + 5 pa vienam",
                     "20 + 4 + 1"],
         "pareizi": 0, "padoms": "19 ir gandrīz 20."},
        {"jaut": "Kāpēc ātrums nav galvenais?",
         "opcijas": ["Steidzoties rodas kļūdas",
                     "Ātrums nav vajadzīgs vispār",
                     "Skolotājs neliek laiku", "Lēni ir vienmēr labāk"],
         "pareizi": 0, "padoms": "Ātrums nāk no paņēmiena, ne no steigas."},
    ], pamats=4),

    Pasaule("Cik punktu ieguva komanda?",
            Ievadi("", [
                {"jaut": "Komanda guva 8 punktus pirmajā puslaikā un 7 "
                         "otrajā. Cik kopā?",
                 "atb": ["15"], "padoms": "8 + 2 + 5."},
                {"jaut": "Pretinieki guva 9 punktus. Par cik vairāk guva "
                         "pirmā komanda?",
                 "atb": ["6"], "padoms": "15 − 9."},
                {"jaut": "Nākamajā spēlē komanda guva 6 reizes pa 3 punktiem. "
                         "Cik punktu?",
                 "atb": ["18"], "padoms": "6 · 3."},
                {"jaut": "Cik punktu komanda guva abās spēlēs kopā?",
                 "atb": ["33"], "padoms": "15 + 18."},
            ]),
            pavediens="sports",
            konteksts="Spēles laikā rezultātu skaita galvā - tablo tikai "
                      "pārbauda to, ko skatītāji jau zina.",
            kapec="Veikls galvas rēķins ļauj sekot spēlei, nevis skaitļiem."),

    Kopsavilkums([
        "Veikli saskaitu un atņemu 20 apjomā.",
        "Izmantoju desmitu kā atbalsta punktu.",
        "Veikli reizinu un dalu tabulas apjomā.",
        "Zinu, ka ātrums nāk no ērta sadalījuma, ne no steigas.",
    ]),

    Majas([
        "Izrēķini galvā desmit piemērus ar pāreju pāri desmitam.",
        "Palūdz mājiniekiem pajautāt piecus tabulas reizinājumus.",
        "Atrodi piemēru, kurā desmita atbalsts nepalīdz, un pastāsti, "
        "kāpēc.",
    ]),
]
