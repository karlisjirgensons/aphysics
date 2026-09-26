# -*- coding: utf-8 -*-
"""7. klase, 71. stunda: «Vai no šiem nogriežņiem var izveidot trijstūri?»

Ne katri trīs nogriežņi veido trijstūri: ja divi īsākie kopā nav garāki par
garāko, tie «nesatiekas». Tā ir trijstūra nevienādība - katra mala ir
īsāka par abu pārējo summu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         geometrija)

TEMA = "Vai no šiem nogriežņiem var izveidot trijstūri?"

MERKIS = ("Lietosim trijstūra nevienādību, lai noteiktu, vai trijstūris "
          "eksistē.")

SATURS = [
    Sakums("3 cm, 4 cm un 9 cm - trijstūris nesanāk",
           zimejums=geometrija([("A", 0, 0), ("B", 9, 0), ("_C", 3, 0.01),
                                ("_D", 5, 0.01)],
                               nogriezni=["AB"],
                               izcelti=[("A", "_C"), ("B", "_D")],
                               malas=[("AB", "9 cm")]),
           paraksts="3 + 4 = 7 < 9: īsie nogriežņi nesatiekas.",
           fakti=["Pamēģini ar salmiņiem - galiem jāsaskaras.",
                  "Ja divi īsākie kopā ir par īsu, trijstūra nav.",
                  "Ja tieši vienādi - «trijstūris» saplok nogrieznī."]),

    Doma("Katra mala < pārējo divu summa",
         "Trijstūra nevienādība: jebkurā trijstūrī katra mala ir īsāka par "
         "abu pārējo malu summu. No trim nogriežņiem trijstūri var izveidot "
         "tad un tikai tad, ja garākais ir īsāks par abu pārējo summu.",
         soli=[
             "Atrodi garāko nogriezni.",
             "Saskaiti abus pārējos.",
             "Ja summa > garākais - trijstūris ir.",
             "Ja summa ≤ garākais - trijstūra nav.",
         ],
         pieze="Pietiek pārbaudīt tikai garāko malu - pārējās nevienādības "
               "tad izpildās pašas."),

    Paraugs("Pārbaudi",
            uzd="Vai var izveidot trijstūri no 5 cm, 7 cm un 11 cm?",
            soli=[
                ("Garākais: 11 cm", "Atrod."),
                ("5 + 7 = 12 (cm)", "Pārējo summa."),
                ("12 > 11", "Nevienādība izpildās."),
            ],
            atbilde="Var."),

    Varianti("Trijstūris vai nē?", [
        {"jaut": "2 cm, 3 cm, 4 cm",
         "opcijas": ["Var", "Nevar"], "pareizi": 0, "jaukt": False,
         "padoms": "2 + 3 = 5 > 4."},
        {"jaut": "1 cm, 2 cm, 3 cm",
         "opcijas": ["Var", "Nevar"], "pareizi": 1, "jaukt": False,
         "padoms": "1 + 2 = 3 - nav lielāks."},
        {"jaut": "6 cm, 6 cm, 11 cm",
         "opcijas": ["Var", "Nevar"], "pareizi": 0, "jaukt": False,
         "padoms": "12 > 11."},
        {"jaut": "4 cm, 10 cm, 5 cm",
         "opcijas": ["Var", "Nevar"], "pareizi": 1, "jaukt": False,
         "padoms": "4 + 5 = 9 < 10."},
    ], pamats=4),

    Petijums("Salmiņu eksperiments",
             ["Sagriez salmiņus: 4, 5, 6, 9, 10 un 12 cm.",
              "Izvēlies trīs un mēģini salikt trijstūri.",
              "Pieraksti tabulā: garumi un «sanāk / nesanāk».",
              "Katrai trijotnei aprēķini: divu īsāko summa un garākais."],
             vajag="salmiņi vai papīra strēmeles, lineāls, šķēres",
             secinajums="Trijstūris sanāk tieši tad, kad divu īsāko summa ir "
                         "lielāka par garāko."),

    Ievadi("Aprēķini", [
        {"jaut": "Malas 8 cm un 3 cm. Vai trešā var būt 12 cm? Raksti «jā» "
                 "vai «nē».",
         "atb": ["nē", "ne"], "padoms": "8 + 3 = 11 < 12."},
        {"jaut": "Malas 8 cm un 3 cm. Vai trešā var būt 10 cm?",
         "atb": ["jā", "ja"], "padoms": "8 + 3 = 11 > 10."},
        {"jaut": "Cik no trijotnēm (2; 3; 6), (3; 4; 5), (5; 5; 10), "
                 "(7; 8; 9) veido trijstūri?",
         "atb": ["2"], "padoms": "(3; 4; 5) un (7; 8; 9)."},
        {"jaut": "Mazākais vesels garums x, lai 5 cm, 9 cm un x cm (x - "
                 "garākā mala) veidotu trijstūri, ja x ≥ 9?",
         "atb": ["9"], "padoms": "9 < 14."},
    ]),

    Pasaule("Stūrgaldam trīs dēļi",
            Ievadi("", [
                {"jaut": "Galdnieka dēļi: 60 cm, 80 cm un 150 cm. Vai "
                         "var izveidot trīsstūra rāmi? Raksti «jā» vai «nē».",
                 "atb": ["nē", "ne"], "padoms": "60 + 80 = 140 < 150."},
                {"jaut": "Cik cm jānozāģē garākajam dēlim, lai tas būtu "
                         "tieši vienāds ar pārējo summu (vēl nav rāmis)?",
                 "atb": ["10"], "padoms": "150 − 140."},
                {"jaut": "Lielākais vesels garums (cm) garākajam dēlim, lai "
                         "rāmis sanāktu?",
                 "atb": ["139"], "padoms": "Mazāk par 140."},
            ]),
            pavediens="maja",
            konteksts="Pirms zāģēšanas galdnieks pārbauda nevienādību - tas "
                      "ir lētāk nekā bojāts dēlis.",
            kapec="Trijstūra nevienādība ir būvniecības noteikums."),

    Kopsavilkums([
        "Zinu trijstūra nevienādību.",
        "Pārbaudu, vai no trim nogriežņiem var izveidot trijstūri.",
        "Salīdzinu garāko malu ar pārējo summu.",
        "Zinu, ka vienādības gadījumā trijstūris saplok.",
    ]),

    Majas([
        "Izmēri 3 zīmuļus un pārbaudi, vai no tiem sanāk trijstūris.",
        "Izdomā 3 trijotnes: divas der, viena neder.",
        "Paskaidro, kāpēc taisns ceļš ir īsāks par apkārtceļu.",
    ]),
]
