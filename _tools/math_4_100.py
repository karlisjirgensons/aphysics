# -*- coding: utf-8 -*-
"""4. klase, 100. stunda: «Kāpēc lielāks saucējs dod mazāku daļu?»

Pamatdaļas ({1|n}) salīdzināšana - lielākais pārsteigums skolēniem: 8 > 4,
bet {1|8} < {1|4}. Jo vairāk cilvēku dala picu, jo mazāks katra gabals.
Stunda to rāda ar joslām, dzīves piemēriem un slīdni.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, dala)

TEMA = "Kāpēc lielāks saucējs dod mazāku daļu?"

MERKIS = ("Salīdzināsim pamatdaļas, izmantojot piemērus no dzīves un "
          "modeļus.")

SATURS = [
    Sakums("Labāk {1|4} vai {1|8} tortes?",
           zimejums=dala(4, 1, "1/4") + dala(8, 1, "1/8"),
           paraksts="Ceturtdaļa ir divreiz lielāka nekā astotdaļa.",
           fakti=["8 > 4, bet {1|8} < {1|4}.",
                  "Vairāk ēdāju - mazāks katra gabals."]),

    Doma("Vairāk daļu - mazāks katrs gabals",
         "Pamatdaļa {1|n} ir viena no n vienādām daļām; jo lielāks n, jo "
         "mazāka katra daļa.",
         soli=[
             "Pamatdaļai skaitītājs ir 1: {1|2}, {1|3}, {1|10}.",
             "Salīdzini saucējus.",
             "Lielāks saucējs - veselais sadalīts vairāk gabalos.",
             "Tātad lielāks saucējs - mazāka pamatdaļa.",
         ],
         pieze="{1|2} > {1|3} > {1|4} > {1|5} > ... > {1|100}."),

    Slidnis("Tā pati pica - vairāk ēdāju",
            soli=[
                {"v": "{1|2}", "zim": dala(2, 1), "teksts": "2 ēdāji."},
                {"v": "{1|3}", "zim": dala(3, 1), "teksts": "3 ēdāji."},
                {"v": "{1|4}", "zim": dala(4, 1), "teksts": "4 ēdāji."},
                {"v": "{1|6}", "zim": dala(6, 1), "teksts": "6 ēdāji."},
                {"v": "{1|10}", "zim": dala(10, 1), "teksts": "10 ēdāji - "
                 "gabals pavisam mazs."},
            ],
            ievads="Skaties, kā sarūk viena gabala josla."),

    Paraugs("{1|5} vai {1|3}?",
            uzd="Salīdzini {1|5} un {1|3} un paskaidro.",
            soli=[
                ("5 > 3", "Saucēji."),
                ("{1|5} < {1|3}", "Vairāk daļu - mazāka katra."),
            ],
            atbilde="{1|5} < {1|3}"),

    Varianti("Kura lielāka?", [
        {"jaut": "{1|6} ☐ {1|9}", "opcijas": [">", "<", "="], "pareizi": 0,
         "padoms": "6 daļas ir lielākas nekā 9 daļas."},
        {"jaut": "{1|12} ☐ {1|2}", "opcijas": ["<", ">", "="], "pareizi": 0,
         "padoms": "12 gabali ir mazāki."},
        {"jaut": "Kura pamatdaļa ir mazākā?",
         "opcijas": ["{1|20}", "{1|2}", "{1|10}", "{1|5}"], "pareizi": 0,
         "padoms": "Lielākais saucējs."},
        {"jaut": "Kura ir lielākā?",
         "opcijas": ["{1|3}", "{1|4}", "{1|7}", "{1|30}"], "pareizi": 0,
         "padoms": "Mazākais saucējs."},
    ], pamats=4),

    Ievadi("Cik reižu?", [
        {"jaut": "Cik astotdaļu ir vienā ceturtdaļā?", "atb": ["2"],
         "padoms": "8 : 4."},
        {"jaut": "Cik sestdaļu ir vienā trešdaļā?", "atb": ["2"],
         "padoms": "6 : 3."},
        {"jaut": "Cik desmitdaļu ir pusē?", "atb": ["5"],
         "padoms": "10 : 2."},
        {"jaut": "Cik divpadsmitdaļu ir vienā ceturtdaļā?", "atb": ["3"],
         "padoms": "12 : 4."},
    ]),

    Pasaule("Laimests jāsadala",
            Ievadi("", [
                {"jaut": "Balva 120 € sadalīta 4 uzvarētājiem. Cik katram?",
                 "atb": ["30"], "padoms": "{1|4} no 120."},
                {"jaut": "Ja uzvarētāju būtu 6, cik katram?", "atb": ["20"],
                 "padoms": "{1|6} no 120."},
                {"jaut": "Par cik € mazāk katram, ja uzvarētāju 6, nevis 4?",
                 "atb": ["10"], "padoms": "30 − 20."},
                {"jaut": "Cik € katram, ja uzvarētāju 10?", "atb": ["12"],
                 "padoms": "120 : 10."},
            ]),
            pavediens="veikals",
            konteksts="Kad balvu dala vairāk cilvēku, katrs saņem mazāk - "
                      "tieši tā strādā lielāks saucējs.",
            kapec="Pamatdaļas salīdzināšana ir godīgas dalīšanas "
                  "matemātika."),

    Kopsavilkums([
        "Salīdzinu pamatdaļas.",
        "Zinu, ka lielāks saucējs dod mazāku pamatdaļu.",
        "Paskaidroju to ar picas vai balvas piemēru.",
    ]),

    Majas([
        "Sagriez papīra sloksnītes 2, 4 un 8 daļās un salīdzini gabalus.",
        "Sakārto: {1|5}, {1|2}, {1|9}, {1|3}.",
        "Paskaidro mājiniekiem, kāpēc {1|8} < {1|4}.",
    ]),
]
