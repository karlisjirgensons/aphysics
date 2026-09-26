# -*- coding: utf-8 -*-
"""7. klase, 11. stunda: «Cik dažādus kodus var izveidot?»

Reizināšanas likums: ja pirmo izvēli var izdarīt a veidos un pēc tam otro -
b veidos, tad abas kopā - a · b veidos. Ar to skaita PIN kodus, paroles un
auto numurus, un saprot, kāpēc gara parole ir drošāka.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti)

TEMA = "Cik dažādus kodus var izveidot?"

MERKIS = ("Iemācīsimies lietot reizināšanas likumu, lai saskaitītu kodu "
          "un paroļu skaitu.")

SATURS = [
    Sakums("Kāpēc bankas karte bloķējas pēc 3 kļūdām?",
           fakti=["Četrciparu PIN kodu ir 10 000.",
                  "Ar 3 mēģinājumiem var uzminēt tikai 3 no tiem.",
                  "Izredzes zaglim: 3 no 10 000 - 0,03 %."]),

    Doma("Izvēļu skaitus sareizina",
         "Reizināšanas likums: ja darbība sastāv no soļiem un pirmo var "
         "izdarīt a veidos, otro - b veidos, trešo - c veidos, tad visu "
         "darbību var izdarīt a · b · c veidos.",
         soli=[
             "Sadali kodu pa vietām (soļiem).",
             "Katrai vietai nosaki, cik izvēļu ir.",
             "Ja simboli nedrīkst atkārtoties, katrā nākamajā vietā izvēļu "
             "ir par vienu mazāk.",
             "Sareizini visus izvēļu skaitus.",
         ],
         pieze="Tas pats iespēju koks, tikai tik liels, ka to vairs "
               "nezīmē - to aprēķina."),

    Paraugs("PIN kods bez atkārtojumiem",
            uzd="Cik ir četrciparu PIN kodu (cipari 0-9), kuros neviens "
                "cipars neatkārtojas?",
            soli=[
                ("1. vieta: 10 izvēles", "Jebkurš cipars."),
                ("2. vieta: 9 izvēles", "Visi, izņemot pirmo."),
                ("3. vieta: 8; 4. vieta: 7", "Katru reizi par vienu mazāk."),
                ("10 · 9 · 8 · 7 = 5040", "Reizināšanas likums."),
            ],
            atbilde="5040 kodu"),

    Slidnis("Ar katru simbolu - daudz vairāk paroļu", [
        {"v": "1 burts", "teksts": "26 paroles", "josla": 3},
        {"v": "2 burti", "teksts": "26 · 26 = 676 paroles", "josla": 12},
        {"v": "3 burti", "teksts": "676 · 26 = 17 576 paroles", "josla": 30},
        {"v": "4 burti", "teksts": "17 576 · 26 = 456 976 paroles",
         "josla": 55},
        {"v": "5 burti", "teksts": "456 976 · 26 = 11 881 376 paroles",
         "josla": 100},
    ], ievads="Parole no mazajiem angļu alfabēta burtiem (26)."),

    Ievadi("Saskaiti kodus", [
        {"jaut": "Cik ir trīsciparu kodu no cipariem 0-9?",
         "atb": ["1000"], "padoms": "10 · 10 · 10."},
        {"jaut": "Cik ir trīsciparu kodu, kuros cipari neatkārtojas?",
         "atb": ["720"], "padoms": "10 · 9 · 8."},
        {"jaut": "Kods: burts (A, B vai C) un cipars (0-9). Cik kodu?",
         "atb": ["30"], "padoms": "3 · 10."},
        {"jaut": "Cik ir trīsciparu skaitļu (pirmais cipars nav 0)?",
         "atb": ["900"], "padoms": "9 · 10 · 10."},
        {"jaut": "Cik trīsciparu skaitļu var uzrakstīt tikai ar "
                 "nepāra cipariem?",
         "atb": ["125"], "padoms": "5 · 5 · 5."},
        {"jaut": "Karodziņam ir 3 horizontālas joslas no 5 krāsām, "
                 "blakus joslas dažādās krāsās. Cik karodziņu?",
         "atb": ["80"], "padoms": "5 · 4 · 4 - vidējā nav kā augšējā, "
                                 "apakšējā nav kā vidējā."},
    ], pamats=4),

    Varianti("Kurš ir drošāks?", [
        {"jaut": "Kura parole ir grūtāk uzminama pilnā pārlasē?",
         "opcijas": ["6 simboli no 62 (burti un cipari)",
                     "6 cipari", "8 cipari", "4 burti no 26"],
         "pareizi": 0,
         "padoms": "62⁶ ≈ 57 miljardi, 10⁸ = 100 miljoni."},
        {"jaut": "Ja PIN kodam pievieno vienu ciparu, kodu skaits...",
         "opcijas": ["palielinās 10 reizes", "palielinās par 10",
                     "divkāršojas", "nemainās"],
         "pareizi": 0,
         "padoms": "Vēl viens reizinātājs 10."},
        {"jaut": "Cik veidos var sakārtot rindā 4 grāmatas?",
         "opcijas": ["24", "16", "4", "10"],
         "pareizi": 0,
         "padoms": "4 · 3 · 2 · 1."},
    ]),

    Pasaule("Auto numura zīmes",
            Ievadi("", [
                {"jaut": "Numurs: 2 burti (no 24) un 4 cipari. Cik "
                         "numuru ar vienādiem burtiem, piemēram, «AA», var "
                         "izveidot? (4 cipari - jebkuri)",
                 "atb": ["240000", "240 000"],
                 "padoms": "24 burtu pāri «AA», «BB» ... · 10 000."},
                {"jaut": "Cik numuru ar jebkuriem 2 burtiem un 4 cipariem?",
                 "atb": ["5760000", "5 760 000"],
                 "padoms": "24 · 24 · 10 000."},
                {"jaut": "Latvijā ir ap 800 000 automašīnu. Vai šādu "
                         "numuru pietiek? Raksti «jā» vai «nē».",
                 "atb": ["jā", "ja"], "padoms": "5 760 000 > 800 000."},
            ]),
            pavediens="kodi",
            konteksts="Numuru sistēmu izvēlas tā, lai kodu pietiktu visām "
                      "valsts automašīnām uz ilgiem gadiem.",
            kapec="Reizināšanas likums pasaka, cik ilgi sistēma kalpos."),

    Kopsavilkums([
        "Lietoju reizināšanas likumu: a · b · c.",
        "Ņemu vērā, vai simboli drīkst atkārtoties.",
        "Zinu, ka katrs jauns simbols kodu skaitu sareizina.",
        "Salīdzinu paroļu drošību ar aprēķinu.",
    ]),

    Majas([
        "Cik ir sešciparu PIN kodu? Cik no tiem bez atkārtojumiem?",
        "Aprēķini, cik paroļu ar 4 simboliem ir no 36 simboliem (burti "
        "un cipari).",
        "Izdomā savu kodu sistēmu un saskaiti kodus.",
    ]),
]
