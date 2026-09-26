# -*- coding: utf-8 -*-
"""7. klase, 35. stunda: «Cik kopīgu punktu var būt divām taisnēm?»

Divām dažādām taisnēm plaknē var būt viens kopīgs punkts (tās krustojas)
vai neviena (tās ir paralēlas). Divi kopīgi punkti nozīmē, ka taisnes
sakrīt - jo caur diviem punktiem iet tikai viena taisne.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, geometrija)

TEMA = "Cik kopīgu punktu var būt divām taisnēm?"

MERKIS = ("Secināsim, kā var būt novietotas divas taisnes plaknē, un "
          "pamatosim to.")

SATURS = [
    Sakums("Sliedes un krustojums",
           zimejums=geometrija([("_1", 0, 0), ("_2", 10, 0), ("_3", 0, 2),
                                ("_4", 10, 2), ("_5", 2, -1.5),
                                ("_6", 8, 3.5)],
                               taisnes=[("_1", "_2"), ("_3", "_4"),
                                        ("_5", "_6")]),
           paraksts="Sliedes nekrustojas; ceļš krusto abas sliedes.",
           fakti=["Sliedes ir paralēlas - kopīgu punktu nav.",
                  "Ceļš krusto katru sliedi tieši vienā punktā."]),

    Doma("Krustojas vai paralēlas",
         "Divām dažādām taisnēm plaknē ir vai nu tieši viens kopīgs punkts "
         "(tās krustojas), vai neviena (tās ir paralēlas: a ∥ b).",
         soli=[
             "Pieņem, ka taisnēm ir divi kopīgi punkti A un B.",
             "Caur A un B iet tikai viena taisne (pamatīpašība).",
             "Tātad abas taisnes ir viena un tā pati - pretruna.",
             "Secinājums: dažādām taisnēm ir ne vairāk kā viens kopīgs "
             "punkts.",
         ],
         pieze="Šis ir pierādījums «no pretējā»: pieņem pretējo un nonāk "
               "pie pretrunas."),

    Paraugs("Cik krustpunktu?",
            uzd="Plaknē ir 4 taisnes, nekādas divas nav paralēlas un nekādas "
                "trīs neiet caur vienu punktu. Cik krustpunktu?",
            soli=[
                ("Katrs taišņu pāris dod 1 krustpunktu", "Nav paralēlu."),
                ("Pāru skaits: 4 · 3 : 2 = 6", "Kā rokasspiedieni."),
                ("Visi krustpunkti dažādi", "Nekādas trīs caur vienu punktu."),
            ],
            atbilde="6 krustpunkti"),

    Varianti("Novietojums", [
        {"jaut": "Taisnēm a un b ir kopīgi punkti M un N (M ≠ N). Ko var "
                 "secināt?",
         "opcijas": ["a un b sakrīt", "a ∥ b", "a ⊥ b",
                     "Tās krustojas vienā punktā"],
         "pareizi": 0,
         "padoms": "Caur diviem punktiem - viena taisne."},
        {"jaut": "a ∥ b un b ∥ c. Kā novietotas a un c?",
         "opcijas": ["a ∥ c (vai sakrīt)", "a ⊥ c", "Krustojas",
                     "Nevar zināt"],
         "pareizi": 0,
         "padoms": "Divas taisnes, kas paralēlas trešajai."},
        {"jaut": "Cik krustpunktu var būt 3 taisnēm plaknē visvairāk?",
         "opcijas": ["3", "1", "6", "2"],
         "pareizi": 0,
         "padoms": "3 · 2 : 2."},
        {"jaut": "Cik krustpunktu ir 3 paralēlām taisnēm?",
         "opcijas": ["0", "3", "1", "Bezgalīgi daudz"],
         "pareizi": 0,
         "padoms": "Paralēlas nekrustojas."},
    ], pamats=4),

    Ievadi("Saskaiti krustpunktus", [
        {"jaut": "5 taisnes, nekādas divas nav paralēlas, nekādas trīs "
                 "neiet caur vienu punktu. Cik krustpunktu?",
         "atb": ["10"], "padoms": "5 · 4 : 2."},
        {"jaut": "3 taisnes, no tām 2 paralēlas. Cik krustpunktu?",
         "atb": ["2"], "padoms": "Trešā krusto abas."},
        {"jaut": "4 taisnes: 2 paralēlas vienā virzienā, 2 - citā. Cik "
                 "krustpunktu?",
         "atb": ["4"], "padoms": "Kā rūtiņu režģis 2 × 2."},
        {"jaut": "3 taisnes iet caur vienu punktu. Cik krustpunktu?",
         "atb": ["1"], "padoms": "Visas krustojas tajā pašā punktā."},
    ]),

    Pasaule("Ielu krustojumi",
            Ievadi("", [
                {"jaut": "Rajonā 5 ielas vienā virzienā un 4 tām "
                         "perpendikulāri. Cik krustojumu?",
                 "atb": ["20"], "padoms": "5 · 4."},
                {"jaut": "Katrā krustojumā vajag 4 luksoforus. Cik "
                         "luksoforu?",
                 "atb": ["80"], "padoms": "20 · 4."},
                {"jaut": "Pilsēta pievieno vienu diagonālu ielu, kas "
                         "krusto visas 9 ielas dažādos punktos. Cik "
                         "krustojumu tagad?",
                 "atb": ["29"], "padoms": "20 + 9."},
            ]),
            pavediens="celojums",
            konteksts="Pilsētas plānotāji skaita krustojumus, lai "
                      "saplānotu luksoforus un gājēju pārejas.",
            kapec="Paralēlas ielas nekrustojas - tās neskaita."),

    Zimejums("Režģis: 3 un 2 paralēlas ielas",
             geometrija([("_a1", 0, 0), ("_a2", 8, 0), ("_b1", 0, 2),
                         ("_b2", 8, 2), ("_c1", 0, 4), ("_c2", 8, 4),
                         ("_d1", 2, -1), ("_d2", 2, 5), ("_e1", 6, -1),
                         ("_e2", 6, 5)],
                        taisnes=[("_a1", "_a2"), ("_b1", "_b2"),
                                 ("_c1", "_c2"), ("_d1", "_d2"),
                                 ("_e1", "_e2")]),
             paskaidro="3 · 2 = 6 krustpunkti."),

    Kopsavilkums([
        "Zinu, ka dažādām taisnēm ir 0 vai 1 kopīgs punkts.",
        "Pamatoju to ar pierādījumu no pretējā.",
        "Saskaitu krustpunktus, izmantojot pārus.",
        "Ņemu vērā paralēlas taisnes.",
    ]),

    Majas([
        "Uzzīmē 4 taisnes ar 0, 1, 3, 4, 5 un 6 krustpunktiem.",
        "Saskaiti krustojumus sava rajona kartē.",
        "Paskaidro, kāpēc divām taisnēm nevar būt 2 krustpunkti.",
    ]),
]
