# -*- coding: utf-8 -*-
"""6. klase, 77. stunda: «Kas notiek, ja šķautni palielina divas reizes?»

Viens no tiem jautājumiem, kuros intuīcija gandrīz vienmēr kļūdās: šķautne
aug divas reizes, virsma - četras, tilpums - astoņas. Tāpēc stunda sākas ar
minējumu un tikai tad ar rēķinu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Kustiba, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti)

TEMA = "Kas notiek, ja šķautni palielina divas reizes?"

MERKIS = ("Pētīsim un skaidrosim, kā mainās kuba virsmas laukums un tilpums, "
          "mainot šķautni.")

SATURS = [
    Sakums("Divreiz garāks nenozīmē divreiz lielāks",
           fakti=["Šķautne aug 2 reizes - virsma aug 4 reizes.",
                  "Tas pats kubs tilpumā kļūst 8 reizes lielāks.",
                  "Reizinātājs ir kvadrātā virsmai un kubā tilpumam."]),

    Doma("Divas reizes, četras reizes, astoņas reizes",
         "Ja kuba šķautni palielina n reižu, virsma pieaug n kvadrātā "
         "reižu, bet tilpums - n trešajā pakāpē reižu.",
         soli=[
             "Pieraksti, cik reižu mainās šķautne.",
             "Virsmai kāpini šo skaitli kvadrātā.",
             "Tilpumam kāpini to trešajā pakāpē.",
             "Reizini sākotnējo virsmu un tilpumu ar šiem skaitļiem.",
             "Pārbaudi ar tiešu aprēķinu.",
         ],
         pieze="Kāpēc? Virsmā ir divi izmēri, tāpēc reizinātājs parādās "
               "divreiz; tilpumā - trīs izmēri, tāpēc trīsreiz. Tas ir tas "
               "pats iemesls, kāpēc mērvienībās ir divnieks un trijnieks."),

    Slidnis("Kubs aug",
            [{"v": "šķautne 2 cm", "teksts": "virsma 24 cm², tilpums 8 cm³",
              "josla": 8},
             {"v": "šķautne 4 cm", "teksts": "virsma 96 cm², tilpums 64 cm³",
              "josla": 30},
             {"v": "šķautne 6 cm",
              "teksts": "virsma 216 cm², tilpums 216 cm³", "josla": 60},
             {"v": "šķautne 8 cm",
              "teksts": "virsma 384 cm², tilpums 512 cm³", "josla": 100}],
            ievads="Spied soli pa solim: šķautne aug vienmērīgi, tilpums - "
                   "daudz straujāk nekā virsma."),

    Paraugs("Palielini šķautni divas reizes",
            uzd="Kuba šķautne ir 3 cm. Kā mainīsies virsma un tilpums, ja "
                "šķautni palielinās līdz 6 cm?",
            soli=[
                ("Sākumā: virsma 6 · 9 = 54 cm², tilpums 27 cm³",
                 "Šķautne 3 cm."),
                ("Pēc tam: virsma 6 · 36 = 216 cm², tilpums 216 cm³",
                 "Šķautne 6 cm."),
                ("216 : 54 = 4",
                 "Virsma pieauga 4 reizes."),
                ("216 : 27 = 8",
                 "Tilpums pieauga 8 reizes."),
            ],
            atbilde="virsma 4 reizes, tilpums 8 reizes"),

    Ievadi("Cik reižu pieaug?", [
        {"jaut": "Šķautni palielina 2 reizes. Cik reižu pieaug virsma?",
         "atb": ["4"], "padoms": "2 · 2."},
        {"jaut": "Cik reižu pieaug tilpums?",
         "atb": ["8"], "padoms": "2 · 2 · 2."},
        {"jaut": "Šķautni palielina 3 reizes. Cik reižu pieaug virsma?",
         "atb": ["9"], "padoms": "3 · 3."},
        {"jaut": "Cik reižu pieaug tilpums?",
         "atb": ["27"], "padoms": "3 · 3 · 3."},
        {"jaut": "Kuba tilpums bija 5 cm³. Cik cm³ tas būs, palielinot "
                 "šķautni 2 reizes?",
         "atb": ["40"], "padoms": "5 · 8."},
        {"jaut": "Šķautni samazina 2 reizes. Cik reižu samazinās tilpums?",
         "atb": ["8"], "padoms": "Tas pats likums otrā virzienā."},
    ], pamats=4),

    Pasaule("Cik liela būs jaunā tvertne?",
            Kustiba("", [
                {"jaut": "Tvertnes tilpums ir 10 l. Cik litru būs, "
                         "palielinot visus izmērus 2 reizes?",
                 "atb": 80, "beigas": 300, "iedala": 50, "mers": "litri",
                 "merkis": "jaunais tilpums", "objekts": "Tvertne",
                 "padoms": "10 · 8."},
                {"jaut": "Cik litru būs, palielinot izmērus 3 reizes?",
                 "atb": 270, "beigas": 300, "iedala": 50, "mers": "litri",
                 "merkis": "jaunais tilpums", "objekts": "Tvertne",
                 "padoms": "10 · 27."},
                {"jaut": "Tvertne 20 l. Cik litru būs, samazinot izmērus "
                         "2 reizes?",
                 "atb": 2.5, "beigas": 300, "iedala": 50, "mers": "litri",
                 "merkis": "jaunais tilpums", "objekts": "Tvertne",
                 "padoms": "20 : 8."},
                {"jaut": "Tvertne 8 l. Cik litru būs, palielinot izmērus "
                         "2 reizes?",
                 "atb": 64, "beigas": 300, "iedala": 50, "mers": "litri",
                 "merkis": "jaunais tilpums", "objekts": "Tvertne",
                 "padoms": "8 · 8."},
            ]),
            pavediens="planeta",
            konteksts="Divreiz lielāka ūdens tvertne dārzā nozīmē astoņas "
                      "reizes vairāk ūdens - tāpēc vieta jāplāno iepriekš.",
            kapec="Tilpums aug daudz straujāk, nekā izskatās."),

    Varianti("Cik reižu?", [
        {"jaut": "Šķautni palielina 2 reizes. Tilpums pieaug...",
         "opcijas": ["8 reizes", "2 reizes", "4 reizes", "6 reizes"],
         "pareizi": 0,
         "padoms": "Trīs izmēri."},
        {"jaut": "Šķautni palielina 4 reizes. Virsma pieaug...",
         "opcijas": ["16 reizes", "4 reizes", "64 reizes", "8 reizes"],
         "pareizi": 0,
         "padoms": "4 · 4."},
        {"jaut": "Kāpēc virsma aug lēnāk nekā tilpums?",
         "opcijas": ["Jo virsmā ir divi izmēri, tilpumā trīs",
                     "Jo virsma ir mazāka",
                     "Jo tilpums ir lielāks", "Tā nav"],
         "pareizi": 0,
         "padoms": "Reizinātājs parādās divreiz vai trīsreiz."},
        {"jaut": "Šķautni samazina 3 reizes. Virsma samazinās...",
         "opcijas": ["9 reizes", "3 reizes", "27 reizes", "6 reizes"],
         "pareizi": 0,
         "padoms": "3 · 3."},
    ], pamats=4),

    Kopsavilkums([
        "Zinu, kā mainās virsma un tilpums, mainot šķautni.",
        "Lietoju reizinātāju kvadrātā virsmai un trešajā pakāpē tilpumam.",
        "Pamatoju likumu ar izmēru skaitu.",
        "Pārbaudu secinājumu ar tiešu aprēķinu.",
    ]),

    Majas([
        "Aprēķini kuba ar šķautni 2 cm un 4 cm virsmu un tilpumu.",
        "Pieraksti, cik reižu katrs pieauga.",
        "Paskaidro kādam mājās, kāpēc divreiz lielāka kaste ietilpina "
        "astoņas reizes vairāk.",
    ]),
]
