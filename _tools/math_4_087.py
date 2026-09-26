# -*- coding: utf-8 -*-
"""4. klase, 87. stunda: «Cik reižu viens lielums ietilpst otrā?»

Dalīšana kā «cik reižu ietilpst» - ar lielumiem, ne tikai skaitļiem:
cik 250 ml glāžu ir 2 litros, cik 45 minūšu stundu ir 6 stundās. Pirms
dalīšanas abi lielumi jāizsaka vienās vienībās, un atlikums dzīvē nozīmē
«vēl nepilns».
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, restis)

TEMA = "Cik reižu viens lielums ietilpst otrā?"

MERKIS = ("Noteiksim, cik reižu viena lieluma vērtība ietilpst otrā, un "
          "paskaidrosim atlikuma nozīmi.")

SATURS = [
    Sakums("Cik glāžu sulas ir 2 litru pakā?",
           zimejums=restis([["2 l", "=", "2000 ml"],
                            ["2000 : 250", "=", "8"]],
                           "8 glāzes pa 250 ml"),
           paraksts="Vispirms litrus pārvērš mililitros.",
           fakti=["Vienā glāzē parasti 250 ml.",
                  "Dalīt var tikai vienādās vienībās."]),

    Doma("Vienādas vienības, tad dali",
         "Lai uzzinātu, cik reižu mazākais lielums ietilpst lielākajā, abus "
         "izsaka vienās vienībās un dala.",
         soli=[
             "Izsaki abus vienās vienībās: 2 l = 2000 ml.",
             "Dali: 2000 : 250 = 8.",
             "Ja paliek atlikums, tas ir «vēl nepilns» gabals.",
             "Atbildē pasaki, ko nozīmē dalījums un ko - atlikums.",
         ],
         pieze="6 h : 45 min → 360 min : 45 min = 8 - astoņas mācību stundas."),

    Paraugs("Lente dāvanām",
            uzd="No 5 m lentes griež gabalus pa 35 cm. Cik gabalu sanāk un "
                "cik paliek?",
            soli=[
                ("5 m = 500 cm", None),
                ("500 : 35 = 14 (atl. 10)", "35 · 14 = 490."),
                ("14 gabali, 10 cm paliek", "Atlikums ir par īsu gabalam."),
            ],
            atbilde="14 gabali, paliek 10 cm"),

    Ievadi("Cik reižu ietilpst?", [
        {"jaut": "Cik 250 ml glāžu ir 3 l?", "atb": ["12"],
         "padoms": "3000 : 250."},
        {"jaut": "Cik 45 minūšu stundu ir 6 h?", "atb": ["8"],
         "padoms": "360 : 45."},
        {"jaut": "Cik 25 cm gabalu no 4 m?", "atb": ["16"],
         "padoms": "400 : 25."},
        {"jaut": "Cik 15 minūšu intervālu ir 2 h?", "atb": ["8"],
         "padoms": "120 : 15."},
        {"jaut": "No 3 m lentes griež pa 40 cm. Cik gabalu?", "atb": ["7"],
         "padoms": "300 : 40 = 7 (atl. 20)."},
        {"jaut": "Cik cm paliek pāri?", "atb": ["20"],
         "padoms": "300 − 280."},
    ], pamats=4),

    Varianti("Ko nozīmē atlikums?", [
        {"jaut": "1 kg miltu, cepumiem vajag 150 g. 1000 : 150 = 6 (atl. "
                 "100). Ko nozīmē 100?",
         "opcijas": ["100 g miltu paliek", "100 cepumi",
                     "vajag vēl 100 kg"], "pareizi": 0,
         "padoms": "Nepietiek vēl vienai porcijai."},
        {"jaut": "Pirms dalīšanas 2 l un 250 ml jāizsaka...",
         "opcijas": ["abi mililitros", "abi litros ar komatu",
                     "nav jāmaina"], "pareizi": 0,
         "padoms": "Vienādās vienībās."},
        {"jaut": "Cik reižu 20 minūtes ietilpst 1 stundā?",
         "opcijas": ["3", "20", "60", "2"], "pareizi": 0,
         "padoms": "60 : 20."},
    ]),

    Pasaule("Ballītes sagatavošana",
            Ievadi("", [
                {"jaut": "Limonāde 6 l, glāzē 250 ml. Cik glāžu?",
                 "atb": ["24"], "padoms": "6000 : 250."},
                {"jaut": "Pica 1200 g, gabals 150 g. Cik gabalu?",
                 "atb": ["8"], "padoms": "1200 : 150."},
                {"jaut": "Ballīte 3 h, spēle 25 min. Cik pilnu spēļu?",
                 "atb": ["7"], "padoms": "180 : 25 = 7 (atl. 5)."},
                {"jaut": "Cik minūšu paliek pēc 7 spēlēm?",
                 "atb": ["5"], "padoms": "180 − 175."},
            ]),
            pavediens="virtuve",
            konteksts="Plānojot ballīti, jāzina, cik porciju sanāk no "
                      "lielā iepakojuma.",
            kapec="Cik reižu ietilpst - viens no biežākajiem dzīves "
                  "jautājumiem."),

    Kopsavilkums([
        "Nosaku, cik reižu viens lielums ietilpst otrā.",
        "Pirms dalīšanas izsaku lielumus vienās vienībās.",
        "Paskaidroju atlikuma nozīmi.",
    ]),

    Majas([
        "Izrēķini, cik 200 ml tasīšu tējas ir 1,5 l tējkannā (1500 ml).",
        "Izmēri auklu un izrēķini, cik 30 cm gabalu var nogriezt.",
        "Izdomā uzdevumu, kurā atlikums nozīmē «vēl nepilns».",
    ]),
]
