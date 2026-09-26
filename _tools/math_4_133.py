# -*- coding: utf-8 -*-
"""4. klase, 133. stunda: «Kāds ir skaitlis, ja zināma tā ceturtdaļa?»

Divi paņēmieni vienam uzdevumam: reizināšana (veselais = 4 · ceturtdaļa)
un saskaitīšana (četras vienādas daļas: a + a + a + a). Skolēns lieto abus
un pārliecinās, ka rezultāts sakrīt - un kāpēc.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, restis)

TEMA = "Kāds ir skaitlis, ja zināma tā ceturtdaļa?"

MERKIS = ("Noteiksim skaitli, ja zināma pamatdaļas vērtība, ar diviem "
          "paņēmieniem.")

SATURS = [
    Sakums("Ceturtdaļa ir 35. Kāds ir skaitlis?",
           zimejums=restis([["1. paņēmiens", "35 · 4 = 140"],
                            ["2. paņēmiens", "35 + 35 + 35 + 35 = 140"]],
                           "divi ceļi, viena atbilde"),
           fakti=["Reizināšana ir ātrāka.",
                  "Saskaitīšana parāda, kāpēc tā ir."]),

    Doma("Reizini vai saskaiti vienādus gabalus",
         "Ja {1|n} skaitļa ir a, skaitlis ir n · a jeb n reizes a pēc kārtas "
         "saskaitīts.",
         soli=[
             "1. paņēmiens: a · n.",
             "2. paņēmiens: a + a + ... (n reizes).",
             "Abi dod vienu rezultātu, jo reizināšana ir saskaitīšana.",
             "Pārbaudi ar dalīšanu: skaitlis : n = a.",
         ],
         pieze="Ja n liels (piemēram, 12), otrais paņēmiens ir garš - tad "
               "reizini."),

    Paraugs("{1|4} ir 35",
            uzd="Skaitļa ceturtdaļa ir 35. Atrodi skaitli divos veidos.",
            soli=[
                ("35 · 4 = 140", "Reizināšana."),
                ("35 + 35 + 35 + 35 = 140", "Saskaitīšana."),
                ("140 : 4 = 35", "Pārbaude."),
            ],
            atbilde="140"),

    Ievadi("Atrodi skaitli", [
        {"jaut": "{1|4} skaitļa ir 35. Skaitlis = ?", "atb": ["140"],
         "padoms": "35 · 4."},
        {"jaut": "{1|4} skaitļa ir 125. Skaitlis = ?", "atb": ["500"],
         "padoms": "125 · 4."},
        {"jaut": "{1|2} skaitļa ir 480. Skaitlis = ?", "atb": ["960"],
         "padoms": "480 + 480."},
        {"jaut": "{1|3} skaitļa ir 333. Skaitlis = ?", "atb": ["999"],
         "padoms": "333 · 3."},
        {"jaut": "{1|5} skaitļa ir 200. Skaitlis = ?", "atb": ["1000"],
         "padoms": "200 · 5."},
        {"jaut": "{1|4} skaitļa ir 2500. Skaitlis = ?", "atb": ["10000",
         "10 000"], "padoms": "2500 · 4."},
    ], pamats=4),

    Varianti("Kurš paņēmiens?", [
        {"jaut": "{1|2} skaitļa ir 45. Ērtāk...",
         "opcijas": ["45 + 45", "45 · 45", "45 : 2"], "pareizi": 0,
         "padoms": "Tikai divas daļas."},
        {"jaut": "{1|12} skaitļa ir 15. Ērtāk...",
         "opcijas": ["15 · 12", "15 + 15 + ... (12 reizes)", "15 : 12"],
         "pareizi": 0, "padoms": "12 saskaitāmie ir daudz."},
        {"jaut": "Vai abi paņēmieni vienmēr dod vienu rezultātu?",
         "opcijas": ["jā", "nē"], "pareizi": 0,
         "padoms": "Reizināšana ir vienādu saskaitāmo summa."},
    ]),

    Pasaule("Dzīvnieku svars",
            Ievadi("", [
                {"jaut": "Kucēns sver {1|4} no pieauguša suņa - 8 kg. Cik "
                         "sver pieaudzis?",
                 "atb": ["32"], "padoms": "8 · 4."},
                {"jaut": "Kumeļš sver {1|4} no zirga - 125 kg. Cik sver "
                         "zirgs?",
                 "atb": ["500"], "padoms": "125 · 4."},
                {"jaut": "Zilonēns sver {1|4} no ziloņmātes - 1200 kg. Cik "
                         "sver ziloņmāte?",
                 "atb": ["4800"], "padoms": "1200 · 4."},
                {"jaut": "Par cik kg zirgs smagāks nekā kumeļš?",
                 "atb": ["375"], "padoms": "500 − 125."},
            ]),
            pavediens="daba",
            konteksts="Dzīvnieku mazuļi bieži sver ap ceturtdaļu no "
                      "pieaugušā - un no tā var novērtēt pieaugušo.",
            kapec="Zinot daļu, var atrast visu - arī dabā."),

    Kopsavilkums([
        "Atrodu skaitli pēc tā ceturtdaļas (vai citas pamatdaļas).",
        "Lietoju reizināšanu un saskaitīšanu.",
        "Paskaidroju, kāpēc abi paņēmieni dod vienu atbildi.",
    ]),

    Majas([
        "Atrodi skaitli, kura ceturtdaļa ir tavs vecums.",
        "Izrēķini abos veidos: {1|3} skaitļa ir 250.",
        "Izdomā uzdevumu par dzīvnieku mazuli.",
    ]),
]
