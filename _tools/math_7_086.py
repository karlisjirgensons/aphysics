# -*- coding: utf-8 -*-
"""7. klase, 86. stunda: «Kas ir vienādsānu un vienādmalu trijstūris?»

Pēc malām trijstūri iedala daudzmalu (visas malas dažādas), vienādsānu
(divas vienādas) un vienādmalu (visas trīs vienādas). Vienādmalu trijstūris
ir vienādsānu trijstūra īpašs gadījums - tā ir apakškopa.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, geometrija,
                         venna)

TEMA = "Kas ir vienādsānu un vienādmalu trijstūris?"

MERKIS = ("Definēsim un klasificēsim trijstūrus pēc malu garumiem.")

_VS = geometrija([("A", 0, 0), ("C", 4, 0), ("B", 2, 4.5)],
                 nogriezni=["AB", "BC", "CA"],
                 svitras=[("AB", 1), ("BC", 1)],
                 malas=[("AC", "pamats")])

SATURS = [
    Sakums("Ceļa zīme «Dodiet ceļu» ir vienādmalu trijstūris",
           zimejums=_VS,
           paraksts="Vienādsānu: sānu malas AB = BC, AC - pamats.",
           fakti=["Brīdinājuma zīmes ir vienādmalu trijstūri.",
                  "Jumta frontons parasti ir vienādsānu trijstūris.",
                  "Pēc malām - trīs veidi."]),

    Doma("Klasifikācija pēc malām",
         "Trijstūri, kuram divas malas ir vienādas, sauc par vienādsānu; "
         "vienādās malas ir sānu malas, trešā - pamats. Trijstūri, kuram visas "
         "malas ir vienādas, sauc par vienādmalu. Ja visas malas dažādas - "
         "daudzmalu trijstūris.",
         soli=[
             "Salīdzini malas pa pāriem.",
             "Trīs vienādas - vienādmalu.",
             "Tieši vai vismaz divas vienādas - vienādsānu.",
             "Visas dažādas - daudzmalu.",
         ],
         pieze="Katrs vienādmalu trijstūris ir arī vienādsānu (jebkuras "
               "divas malas ir vienādas), bet ne otrādi."),

    Zimejums("Kopu diagramma",
             venna(["5; 5; 8"], [], ["6; 6; 6"],
                   ("vienādsānu", "vienādmalu")),
             paskaidro="Vienādmalu trijstūri ⊂ vienādsānu trijstūri."),

    Paraugs("Aprēķini perimetru",
            uzd="Vienādsānu trijstūra pamats 6 cm, sānu mala 2 reizes garāka. "
                "Aprēķini perimetru.",
            soli=[
                ("Sānu mala: 2 · 6 = 12 (cm)", "Divas tādas."),
                ("P = 12 + 12 + 6", "Summa."),
                ("P = 30 (cm)", "Atbilde."),
                ("Pārbaude: 12 + 6 > 12", "Trijstūris eksistē."),
            ],
            atbilde="P = 30 cm"),

    Varianti("Kāds trijstūris?", [
        {"jaut": "Malas 7, 7, 7 cm",
         "opcijas": ["Vienādmalu (arī vienādsānu)", "Tikai daudzmalu",
                     "Tikai vienādsānu, ne vienādmalu", "Nav trijstūris"],
         "pareizi": 0, "padoms": "Visas vienādas."},
        {"jaut": "Malas 5, 8, 5 cm",
         "opcijas": ["Vienādsānu", "Vienādmalu", "Daudzmalu",
                     "Nav trijstūris"],
         "pareizi": 0, "padoms": "Divas vienādas."},
        {"jaut": "Malas 3, 4, 5 cm",
         "opcijas": ["Daudzmalu", "Vienādsānu", "Vienādmalu",
                     "Nav trijstūris"],
         "pareizi": 0, "padoms": "Visas dažādas."},
        {"jaut": "Malas 2, 2, 5 cm",
         "opcijas": ["Nav trijstūris", "Vienādsānu", "Vienādmalu",
                     "Daudzmalu"],
         "pareizi": 0, "padoms": "2 + 2 < 5."},
    ], pamats=4),

    Ievadi("Aprēķini", [
        {"jaut": "Vienādmalu trijstūra perimetrs 27 cm. Mala (cm)?",
         "atb": ["9"], "padoms": "27 : 3."},
        {"jaut": "Vienādsānu trijstūrim sānu mala 8 cm, P = 22 cm. Pamats "
                 "(cm)?",
         "atb": ["6"], "padoms": "22 − 16."},
        {"jaut": "Vienādsānu trijstūrim pamats 10 cm, P = 36 cm. Sānu mala "
                 "(cm)?",
         "atb": ["13"], "padoms": "(36 − 10) : 2."},
        {"jaut": "No 60 cm stieples izliec vienādmalu trijstūri. Mala (cm)?",
         "atb": ["20"], "padoms": "60 : 3."},
    ]),

    Pasaule("Ceļa zīmes",
            Ievadi("", [
                {"jaut": "Brīdinājuma zīme ir vienādmalu trijstūris ar malu "
                         "90 cm. Cik cm apmales līmlentes vajag?",
                 "atb": ["270"], "padoms": "3 · 90."},
                {"jaut": "Mazākā zīme ir ar malu 60 cm. Par cik cm īsāks "
                         "perimetrs?",
                 "atb": ["90"], "padoms": "270 − 180."},
                {"jaut": "Cik zīmju ar malu 60 cm var aplīmēt ar 36 m "
                         "līmlentes?",
                 "atb": ["20"], "padoms": "3600 : 180."},
            ]),
            pavediens="celojums",
            konteksts="Ceļa zīmju izmērus nosaka standarts - un tie ir "
                      "vienādmalu trijstūri.",
            kapec="Vienāda forma - vienāds aprēķins."),

    Kopsavilkums([
        "Klasificēju trijstūrus pēc malām.",
        "Nosaucu sānu malas un pamatu.",
        "Zinu, ka vienādmalu trijstūri ir vienādsānu apakškopa.",
        "Aprēķinu perimetru un malas.",
    ]),

    Majas([
        "Atrodi 3 vienādsānu trijstūrus apkārtnē.",
        "Izdomā vienādsānu trijstūri ar perimetru 20 cm (3 variantus).",
        "Pārbaudi katram trijstūra nevienādību.",
    ]),
]
