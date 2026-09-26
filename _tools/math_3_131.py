# -*- coding: utf-8 -*-
"""3. klase, 131. stunda: «Kā sakārtot skaitļus?»

Sakārtošana ir salīdzināšana, atkārtota daudzas reizes. Šeit svarīga ir arī
kārtības *nosaukšana*: augoša un dilstoša secība, un prasme pateikt, pēc kāda
noteikuma saraksts ir sakārtots.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         restis)

TEMA = "Kā sakārtot skaitļus?"

MERKIS = ("Sakārtosim skaitļus augošā un dilstošā secībā un skaidrosim savu "
          "kārtību.")

SATURS = [
    Sakums("Kā sakārtot piecus skaitļus pēc kārtas?",
           zimejums=restis([[307, 370, 703, 730],
                            ["augošā secībā", "", "", ""]],
                           "no mazākā uz lielāko"),
           paraksts="Augošā secībā katrs nākamais ir lielāks par iepriekšējo.",
           fakti=["Augošā secībā skaitļi aug no mazākā uz lielāko.",
                  "Dilstošā secībā - otrādi."]),

    Doma("Atrodi mazāko, tad nākamo mazāko",
         "Sakārtot nozīmē atkārtot vienu darbību: atrast mazāko no "
         "atlikušajiem.",
         soli=[
             "Atrodi mazāko skaitli un pieraksti to pirmo.",
             "Izsvītro to no saraksta.",
             "Atrodi mazāko no atlikušajiem.",
             "Atkārto, līdz saraksts ir tukšs.",
         ],
         pieze="Dilstošai secībai tas pats, tikai katru reizi meklē "
               "*lielāko*. Sakārtotu sarakstu var vienkārši izlasīt "
               "atpakaļ."),

    Paraugs("Sakārto augošā secībā",
            uzd="Sakārto augošā secībā: 703, 307, 730, 370.",
            soli=[
                ("Mazākais ir 307",
                 "Simti: 3, 3, 7, 7; no trīssimtniekiem mazākais ir 307."),
                ("Nākamais ir 370",
                 "Otrs trīssimtnieks."),
                ("Tad 703 un 730",
                 "Septiņsimtnieki tādā pašā kārtībā."),
            ],
            atbilde="307, 370, 703, 730"),

    Petijums("Sakārto kartītes",
             vajag="astoņas kartītes ar trīsciparu skaitļiem",
             soli=[
                 "Uzraksti uz kartītēm astoņus dažādus skaitļus.",
                 "Sajauc tās un noliec uz galda.",
                 "Sakārto augošā secībā, katru reizi meklējot mazāko.",
                 "Pārlasi sarakstu atpakaļ - tā ir dilstošā secība.",
             ],
             secinajums="Viens sakārtojums dod abas secības - to tikai lasa "
                        "no dažādiem galiem."),

    Ievadi("Sakārto skaitļus", [
        {"jaut": "Kurš no šiem ir mazākais: 703, 307, 730, 370? Ieraksti to.",
         "atb": ["307"], "padoms": "Vismazākie simti un desmiti."},
        {"jaut": "Kurš ir lielākais: 703, 307, 730, 370? Ieraksti to.",
         "atb": ["730"], "padoms": "Septiņi simti un trīs desmiti."},
        {"jaut": "Kurš skaitlis ir otrais augošā secībā?", "atb": ["370"],
         "padoms": "Pēc 307."},
        {"jaut": "Par cik lielākais ir lielāks par mazāko?", "atb": ["423"],
         "padoms": "730 − 307."},
        {"jaut": "Kurš skaitlis ir starp 450 un 470?", "atb": ["460"],
         "padoms": "Pa vidu."},
        {"jaut": "Kurš skaitlis ir tieši pirms 600?", "atb": ["599"],
         "padoms": "600 − 1."},
    ], pamats=4),

    Zimejums("Augošā un dilstošā secība",
             restis([["augošā", 307, 370, 703, 730],
                     ["dilstošā", 730, 703, 370, 307]],
                    "viens saraksts, divi virzieni"),
             paskaidro="Dilstošā secība ir tā pati rinda, izlasīta no otra "
                       "gala.",
             ievads="Salīdzini abas rindas."),

    Varianti("Kāda ir kārtība?", [
        {"jaut": "Kurš saraksts ir augošā secībā?",
         "opcijas": ["120, 210, 201", "500, 400, 300",
                     "700, 707, 770", "999, 99, 9"],
         "pareizi": 2, "padoms": "Katrs nākamais lielāks."},
        {"jaut": "Kāda secība ir 900, 800, 700?",
         "opcijas": ["Dilstoša", "Augoša", "Nekāda", "Jaukta"],
         "pareizi": 0, "padoms": "Katrs nākamais mazāks."},
        {"jaut": "Kurš skaitlis trūkst: 310, 320, ?, 340",
         "opcijas": ["330", "325", "350", "300"],
         "pareizi": 0, "padoms": "Solis ir 10."},
        {"jaut": "Kā sakārtot dilstošā secībā?",
         "opcijas": ["Katru reizi meklējot lielāko",
                     "Katru reizi meklējot mazāko",
                     "Pēc ciparu summas", "Nejauši"],
         "pareizi": 0, "padoms": "Otrādi nekā augošajai."},
    ], pamats=4),

    Pasaule("Kurā secībā planētas?",
            Ievadi("", [
                {"jaut": "Attālumi miljonos km: 58, 108, 150, 228. Kurš ir "
                         "mazākais? Ieraksti to.",
                 "atb": ["58"], "padoms": "Divi cipari."},
                {"jaut": "Kurš ir lielākais?", "atb": ["228"],
                 "padoms": "Divi simti."},
                {"jaut": "Par cik miljoniem 228 ir lielāks par 58?",
                 "atb": ["170"], "padoms": "228 − 58."},
                {"jaut": "Cik ir 150 un 108 summa?", "atb": ["258"],
                 "padoms": "150 + 108."},
            ]),
            pavediens="kosmoss",
            konteksts="Planētas no Saules sakārtotas tieši augošā secībā pēc "
                      "attāluma - Merkurs, Venera, Zeme, Marss.",
            kapec="Sakārtots saraksts ļauj uzreiz redzēt, kas ir tuvāk un kas "
                  "tālāk."),

    Kopsavilkums([
        "Sakārtoju skaitļus augošā secībā.",
        "Sakārtoju skaitļus dilstošā secībā.",
        "Skaidroju savu kārtību ar salīdzināšanu.",
        "Atrodu trūkstošo skaitli sakārtotā rindā.",
    ]),

    Majas([
        "Uzraksti piecus trīsciparu skaitļus un sakārto tos abās secībās.",
        "Atrodi mājās piecas cenas un sakārto tās augošā secībā.",
        "Izdomā rindu ar soli 25 un uzraksti piecus tās locekļus.",
    ]),
]
