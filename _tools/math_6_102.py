# -*- coding: utf-8 -*-
"""6. klase, 102. stunda: «Kurš skaitlis ir lielāks?»

Salīdzināšana ir vienkārša, ja atceras vienu likumu: uz skaitļu taisnes
lielākais ir tas, kurš ir vairāk pa labi. Grūtība rodas tikai tad, kad abi
skaitļi ir negatīvi - tur intuīcija velk uz pretējo pusi.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, taisne)

TEMA = "Kurš skaitlis ir lielāks?"

MERKIS = ("Mācīsimies salīdzināt pozitīvus un negatīvus skaitļus un sakārtot "
          "tos augošā secībā.")

SATURS = [
    Sakums("−2 ir lielāks nekā −7",
           zimejums=taisne(-8, 2, 2, [(-7, "−7"), (-2, "−2")]),
           paraksts="−2 ir vairāk pa labi, tāpēc tas ir lielāks - lai gan "
                    "septiņi izskatās «vairāk» nekā divi.",
           fakti=["Lielāks ir tas skaitlis, kurš uz taisnes ir vairāk pa "
                  "labi.",
                  "Jebkurš pozitīvs skaitlis ir lielāks par jebkuru "
                  "negatīvu.",
                  "Negatīviem skaitļiem lielāks modulis nozīmē mazāku "
                  "skaitli."]),

    Doma("Pa labi - lielāks",
         "Salīdzinot skaitļus, izšķir to vieta uz skaitļu taisnes: kurš ir "
         "vairāk pa labi, tas ir lielāks.",
         soli=[
             "Paskaties uz abu skaitļu zīmēm.",
             "Ja zīmes ir dažādas, pozitīvais ir lielāks.",
             "Ja abi ir pozitīvi, lielāks ir tas, kuram lielāks modulis.",
             "Ja abi ir negatīvi, lielāks ir tas, kuram *mazāks* modulis.",
             "Pārbaudi uz skaitļu taisnes.",
         ],
         pieze="Nulle ir robeža: tā ir lielāka par visiem negatīvajiem un "
               "mazāka par visiem pozitīvajiem. Tāpēc, sakārtojot skaitļus, "
               "to ērti likt par atskaites punktu."),

    Paraugs("Sakārto augošā secībā",
            uzd="Sakārto augošā secībā: 3; −7; 0; −2; 1,5.",
            soli=[
                ("Negatīvie: −7 un −2",
                 "Tie ir pa kreisi no nulles."),
                ("−7 < −2, jo −7 ir tālāk pa kreisi",
                 "Lielāks modulis - mazāks skaitlis."),
                ("Tad nulle",
                 "Robeža."),
                ("Pozitīvie: 1,5 un 3",
                 "Parastā secība."),
                ("−7 < −2 < 0 < 1,5 < 3",
                 "Visa rinda."),
            ],
            atbilde="−7; −2; 0; 1,5; 3"),

    Ievadi("Kurš ir lielāks?", [
        {"jaut": "Kurš ir lielāks: −2 vai −7? Ieraksti lielāko.",
         "atb": ["-2", "−2"], "padoms": "Vairāk pa labi."},
        {"jaut": "Kurš ir lielāks: −5 vai 1? Ieraksti lielāko.",
         "atb": ["1"], "padoms": "Pozitīvs pret negatīvu."},
        {"jaut": "Kurš ir lielāks: −0,5 vai −1? Ieraksti lielāko.",
         "atb": ["-0,5", "−0,5", "-0.5"], "padoms": "Mazāks modulis."},
        {"jaut": "Kurš ir mazākais no skaitļiem 3; −7; 0; −2?",
         "atb": ["-7", "−7"], "padoms": "Vistālāk pa kreisi."},
        {"jaut": "Kurš ir lielākais no skaitļiem −8; −3; −15?",
         "atb": ["-3", "−3"], "padoms": "Mazākais modulis."},
        {"jaut": "Kurš skaitlis ir lielāks: 0 vai −0,1? Ieraksti lielāko.",
         "atb": ["0"], "padoms": "Nulle ir lielāka par visiem negatīvajiem."},
    ], pamats=4),

    Varianti("Kurš apgalvojums ir patiess?", [
        {"jaut": "Jebkurš pozitīvs skaitlis ir...",
         "opcijas": ["lielāks par jebkuru negatīvu",
                     "mazāks par jebkuru negatīvu",
                     "vienāds ar nulli", "lielāks par nulli tikai dažreiz"],
         "pareizi": 0,
         "padoms": "Pozitīvie ir pa labi no nulles."},
        {"jaut": "Ja diviem negatīviem skaitļiem salīdzina moduļus, lielāks "
                 "ir...",
         "opcijas": ["tas, kuram modulis mazāks",
                     "tas, kuram modulis lielāks",
                     "abi vienādi", "nevar salīdzināt"],
         "pareizi": 0,
         "padoms": "−2 ir lielāks nekā −7."},
        {"jaut": "Nulle ir...",
         "opcijas": ["lielāka par visiem negatīvajiem",
                     "mazāka par visiem negatīvajiem",
                     "lielākais skaitlis", "mazākais skaitlis"],
         "pareizi": 0,
         "padoms": "Tā ir robeža."},
        {"jaut": "Kurš skaitlis ir vislielākais: −1; −0,5; −0,1?",
         "opcijas": ["−0,1", "−1", "−0,5", "Visi vienādi"],
         "pareizi": 0,
         "padoms": "Vistuvāk nullei."},
    ], pamats=4),

    Pasaule("Kura nakts bija aukstāka?",
            Ievadi("", [
                {"jaut": "Pirmajā naktī −7 °C, otrajā −12 °C. Kura bija "
                         "aukstāka? Ieraksti temperatūru.",
                 "atb": ["-12", "−12"], "padoms": "Mazāks skaitlis."},
                {"jaut": "Par cik grādiem aukstāka?",
                 "atb": ["5"], "padoms": "12 − 7."},
                {"jaut": "Trešajā naktī −3 °C. Kura bija vissiltākā? Ieraksti "
                         "temperatūru.",
                 "atb": ["-3", "−3"], "padoms": "Lielākais skaitlis."},
                {"jaut": "Sakārto augošā secībā un ieraksti pirmo: −7; −12; "
                         "−3.",
                 "atb": ["-12", "−12"], "padoms": "Mazākais ir pirmais."},
            ]),
            pavediens="planeta",
            konteksts="Laika ziņās aukstākā nakts ir tā, kurai temperatūra "
                      "ir mazākais skaitlis - nevis lielākais modulis.",
            kapec="Salīdzināšana ar zīmi ir citāda nekā bez tās."),

    Zimejums("Visi skaitļi vienā rindā",
             taisne(-8, 4, 2, [(-7, "−7"), (-2, "−2"), (0, "0"),
                               (1.5, "1,5"), (3, "3")]),
             paskaidro="Secība uz taisnes no kreisās uz labo ir tieši augošā "
                       "secība.",
             ievads="Sakārtot skaitļus nozīmē tos salikt uz taisnes."),

    Kopsavilkums([
        "Salīdzinu pozitīvus un negatīvus skaitļus.",
        "Zinu, ka lielāks ir tas skaitlis, kurš ir vairāk pa labi.",
        "Salīdzinu divus negatīvus skaitļus pēc to moduļa.",
        "Sakārtoju skaitļus augošā secībā.",
    ]),

    Majas([
        "Sakārto augošā secībā: −4; 2; −9; 0; −0,5.",
        "Atrodi nedēļas laika ziņās aukstāko un siltāko dienu.",
        "Paskaidro kādam mājās, kāpēc −2 ir lielāks nekā −7.",
    ]),
]
