# -*- coding: utf-8 -*-
"""4. klase, 73. stunda: «Cik ir desmittūkstotis?»

Reizināšana ar desmitiem ātri aizved pāri 10 000. Desmittūkstotis ir jauna
šķira - piektais cipars no labās. Lielus skaitļus lasa pa trim cipariem,
atdalot ar atstarpi: 45 300 - četrdesmit pieci tūkstoši trīs simti.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis, taisne)

TEMA = "Cik ir desmittūkstotis?"

MERKIS = ("Lietosim jēdzienu desmittūkstotis un lasīsim lielus skaitļus.")

SATURS = [
    Sakums("Cik skatītāju ietilpst stadionā?",
           zimejums=restis([["DT", "T", "S", "D", "V"],
                            [1, 0, 0, 0, 0],
                            [4, 5, 3, 0, 0]],
                           "10 000 un 45 300"),
           paraksts="Piektais cipars no labās - desmittūkstoši.",
           fakti=["Skonto stadionā Rīgā ir ap 10 000 sēdvietu.",
                  "Lielākajos pasaules stadionos - vairāk nekā 90 000."]),

    Doma("Desmit tūkstoši ir desmittūkstotis",
         "10 · 1000 = 10 000; lielus skaitļus lasa, sadalot pa trim cipariem "
         "no labās.",
         soli=[
             "Atdali trīs ciparus no labās ar atstarpi: 45 300.",
             "Kreisā daļa (45) ir tūkstoši.",
             "Lasi: «četrdesmit pieci tūkstoši trīs simti».",
             "Šķiru tabulā 4 ir desmittūkstoši, 5 - tūkstoši.",
         ],
         pieze="Atstarpe palīdz: 45300 grūti izlasīt, 45 300 - viegli."),

    Zimejums("Taisne līdz 100 000",
             taisne(0, 100000, 10000, [(45300, "45 300")]),
             paskaidro="Katra iedaļa ir desmittūkstotis.",
             ievads="Ar soli 10 000 taisne sniedzas līdz simt tūkstošiem."),

    Paraugs("Izlasi 70 080",
            uzd="Kā izlasīt 70 080?",
            soli=[
                ("70 | 080", "Atdala trīs ciparus."),
                ("70 tūkstoši", None),
                ("80", "Simtu nav."),
            ],
            atbilde="septiņdesmit tūkstoši astoņdesmit"),

    Ievadi("Lasi un raksti", [
        {"jaut": "Raksti ar cipariem: divdesmit tūkstoši", "atb": ["20000",
         "20 000"], "padoms": "20 un trīs nulles."},
        {"jaut": "Raksti: trīsdesmit pieci tūkstoši divi simti",
         "atb": ["35200", "35 200"], "padoms": "35 | 200."},
        {"jaut": "Cik tūkstošu ir 48 000?", "atb": ["48"],
         "padoms": "Kreisā daļa."},
        {"jaut": "Cik desmittūkstošu ir 60 000?", "atb": ["6"],
         "padoms": "60 000 : 10 000."},
        {"jaut": "10 000 · 3 = ?", "atb": ["30000", "30 000"],
         "padoms": "3 desmittūkstoši."},
        {"jaut": "Raksti: deviņdesmit deviņi tūkstoši deviņi simti deviņdesmit "
                 "deviņi", "atb": ["99999", "99 999"],
         "padoms": "Lielākais piecciparu skaitlis."},
    ], pamats=4),

    Varianti("Kā izlasa?", [
        {"jaut": "12 500",
         "opcijas": ["divpadsmit tūkstoši pieci simti",
                     "simts divdesmit pieci", "divpadsmit simti pieci",
                     "viens tūkstotis divi simti piecdesmit"],
         "pareizi": 0, "padoms": "12 | 500."},
        {"jaut": "Cik ciparu ir desmittūkstotim?",
         "opcijas": ["5", "4", "6", "10"], "pareizi": 0,
         "padoms": "10 000."},
        {"jaut": "Kurš lielāks: 9999 vai 10 000?",
         "opcijas": ["10 000", "9999", "vienādi"], "pareizi": 0,
         "padoms": "Piecciparu > četrciparu."},
        {"jaut": "Cik ir 1000 · 10?",
         "opcijas": ["10 000", "1000", "100 000", "1010"], "pareizi": 0,
         "padoms": "Viena nulle klāt."},
    ], pamats=4),

    Pasaule("Stadionu salīdzinājums",
            Ievadi("", [
                {"jaut": "Stadionā A ir 10 000 vietu, B - 4 reizes vairāk. "
                         "Cik vietu B?",
                 "atb": ["40000", "40 000"], "padoms": "10 000 · 4."},
                {"jaut": "Par cik vietām B lielāks nekā A?",
                 "atb": ["30000", "30 000"], "padoms": "40 000 − 10 000."},
                {"jaut": "Arēnā 12 500 vietu. Cik pilnu tūkstošu vietu tas "
                         "ir?",
                 "atb": ["12"], "padoms": "12 | 500."},
                {"jaut": "Koncertā 45 300 cilvēku. Cik tūkstošu?",
                 "atb": ["45"], "padoms": "45 | 300 - pilnie tūkstoši."},
            ]),
            pavediens="sports",
            konteksts="Stadionu ietilpība - skaitļi, kuros desmittūkstoši "
                      "ir ikdiena.",
            kapec="Lielu skaitli var izlasīt tikai tad, ja zina šķiras."),

    Kopsavilkums([
        "Zinu, ka 10 000 ir desmittūkstotis.",
        "Lasu lielus skaitļus, atdalot pa trim cipariem.",
        "Rakstu lielus skaitļus ar atstarpi.",
    ]),

    Majas([
        "Atrodi internetā savas pilsētas iedzīvotāju skaitu un izlasi to.",
        "Uzraksti ar cipariem 3 lielus skaitļus, ko dzirdi ziņās.",
        "Izrēķini, cik ir 10 000 · 5 un 10 000 · 10.",
    ]),
]
