# -*- coding: utf-8 -*-
"""4. klase, 5. stunda: «Kur noder mērvienības?»

Atkārtojuma mikrotemata noslēgums. Skaitlis bez mērvienības neko nepasaka -
«5» var būt 5 centi vai 5 kilometri. Stundā pārvērš lielākas vienības
mazākās (1 € = 100 ct, 1 km = 1000 m, 1 kg = 1000 g, 1 h = 60 min) un
rēķina ar tām, jo tieši tur rodas lielākā daļa kļūdu sadzīves uzdevumos.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         restis)

TEMA = "Kur noder mērvienības?"

MERKIS = ("Pārveidosim naudas, garuma, masas, tilpuma un laika mērvienības "
          "un rēķināsim ar tām sadzīves uzdevumos.")

SATURS = [
    Sakums("Kāpēc raķete var pazust mērvienību dēļ?",
           zimejums=restis([["lielā vienība", "mazā vienība"],
                            ["1 €", "100 ct"],
                            ["1 km", "1000 m"],
                            ["1 kg", "1000 g"],
                            ["1 h", "60 min"]],
                           "pāri, kas jāzina no galvas"),
           fakti=["1999. gadā NASA zaudēja Marsa zondi mērvienību kļūdas dēļ.",
                  "Viena komanda rēķināja mārciņās, otra - ņūtonos.",
                  "Pirms rēķina vienmēr pārbaudi mērvienības."]),

    Doma("Pirms rēķināt, pārvērt visu vienās mērvienībās",
         "Ja divi lielumi doti dažādās vienībās, vispirms izsaki abus vienā - "
         "tad saskaiti vai atņem.",
         soli=[
             "Atrodi, kādas mērvienības uzdevumā ir.",
             "Izvēlies mazāko no tām.",
             "Pārvērt lielāko vienību mazākajā: 2 m = 200 cm.",
             "Rēķini un pieraksti atbildi ar mērvienību.",
         ],
         pieze="1 l = 1000 ml, 1 m = 100 cm, 1 cm = 10 mm, 1 min = 60 s."),

    Paraugs("Cik ilgi ceļā?",
            uzd="Vilciens izbrauc 8 h 45 min un brauc 1 h 30 min. Cikos tas "
                "pienāk?",
            soli=[
                ("8 h + 1 h = 9 h",
                 "Vispirms saskaita stundas."),
                ("45 min + 30 min = 75 min",
                 "Tad minūtes."),
                ("75 min = 1 h 15 min",
                 "60 minūtes ir viena stunda."),
                ("9 h + 1 h 15 min = 10 h 15 min", None),
            ],
            atbilde="plkst. 10.15"),

    Ievadi("Pārvērt", [
        {"jaut": "3 € = ? ct", "atb": ["300"], "padoms": "1 € = 100 ct."},
        {"jaut": "2 km = ? m", "atb": ["2000"], "padoms": "1 km = 1000 m."},
        {"jaut": "4 kg = ? g", "atb": ["4000"], "padoms": "1 kg = 1000 g."},
        {"jaut": "2 h = ? min", "atb": ["120"], "padoms": "1 h = 60 min."},
        {"jaut": "5 m 20 cm = ? cm", "atb": ["520"],
         "padoms": "500 cm + 20 cm."},
        {"jaut": "1 l 250 ml = ? ml", "atb": ["1250"],
         "padoms": "1000 ml + 250 ml."},
    ], pamats=4,
        ievads="Ieraksti tikai skaitli - mērvienība jau ir dota."),

    Zimejums("Kāpnes starp vienībām",
             restis([["mm", "cm", "m", "km"],
                     ["· 10", "· 100", "· 1000", ""]],
                    "cik mazo ir vienā lielajā"),
             paskaidro="1 cm = 10 mm, 1 m = 100 cm, 1 km = 1000 m. Uz leju - "
                       "reizina, uz augšu - dala.",
             ievads="Garuma vienības ir kāpnes: katrs pakāpiens ir citāds."),

    Varianti("Kas nav pareizi?", [
        {"jaut": "Kura vienādība ir aplama?",
         "opcijas": ["1 h = 100 min", "1 km = 1000 m", "1 € = 100 ct",
                     "1 kg = 1000 g"], "pareizi": 0,
         "padoms": "Stundā ir 60 minūtes."},
        {"jaut": "Kas ir smagāks: 1 kg vai 900 g?",
         "opcijas": ["1 kg", "900 g", "vienādi"], "pareizi": 0,
         "padoms": "1 kg = 1000 g."},
        {"jaut": "Kas ir garāks: 3 m vai 250 cm?",
         "opcijas": ["3 m", "250 cm", "vienādi"], "pareizi": 0,
         "padoms": "3 m = 300 cm."},
        {"jaut": "Ar ko mēra ūdeni krūzē?",
         "opcijas": ["ml", "km", "kg", "min"], "pareizi": 0,
         "padoms": "Tilpumu mēra litros un mililitros."},
    ], pamats=4),

    Pasaule("Iepakojam ceļojumam",
            Ievadi("", [
                {"jaut": "Mugursomā ir 2 kg 300 g lietu un ūdens pudele "
                         "500 g. Cik gramu kopā?",
                 "atb": ["2800"], "padoms": "2300 + 500."},
                {"jaut": "Pārgājiens ir 5 km. Nogājām 3 km 400 m. Cik "
                         "metru vēl atlicis?",
                 "atb": ["1600"], "padoms": "5000 − 3400."},
                {"jaut": "Maizītes maksā 1 € 20 ct un 85 ct. Cik centu "
                         "kopā?",
                 "atb": ["205"], "padoms": "120 + 85."},
                {"jaut": "Ceļā pavadījām 1 h 40 min. Cik minūšu tas ir?",
                 "atb": ["100"], "padoms": "60 + 40."},
            ]),
            pavediens="celojums",
            konteksts="Pārgājienā viss ir mērvienībās: somas svars, "
                      "attālums, laiks un nauda.",
            kapec="Kas pārvērš vienības pirms rēķina, tas nesajauc 3 km ar "
                  "3 m."),

    Petijums("Mērvienības mūsu klasē",
             soli=[
                 "Ar mērlenti izmēri tāfeles garumu metros un centimetros.",
                 "Uzraksti to tikai centimetros.",
                 "Nosver savu somu uz svariem un pieraksti gramos.",
                 "Salīdzini ar klasesbiedru: kuram soma smagāka un par cik?",
             ],
             vajag="mērlente, svari",
             secinajums="Kad abi lielumi ir vienās vienībās, salīdzināt un "
                        "rēķināt ir viegli."),

    Kopsavilkums([
        "Zinu, cik mazo vienību ir vienā lielajā.",
        "Pārvēršu lielākas mērvienības mazākās.",
        "Pirms rēķina pārbaudu, vai vienības ir vienādas.",
        "Rakstu atbildi ar mērvienību.",
    ]),

    Majas([
        "Atrodi virtuvē trīs iepakojumus un pieraksti, kādās vienībās uz tiem "
        "ir masa vai tilpums.",
        "Izrēķini, cik minūšu tu pavadi ceļā uz skolu nedēļā.",
        "Pārbaudi, cik centu ir tavā krājkasītē vai makā.",
    ]),
]
