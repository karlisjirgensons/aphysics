# -*- coding: utf-8 -*-
"""6. klase, 101. stunda: «Kas ir skaitļa modulis?»

Modulis ir attālums, un tieši tā to arī jāsaprot: cik tālu skaitlis ir no
nulles, nemaz nejautājot, kurā pusē. No šīs vienas idejas izriet viss - arī
tas, kāpēc pretējiem skaitļiem moduļi sakrīt.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, Zimejums,
                         taisne)

TEMA = "Kas ir skaitļa modulis?"

MERKIS = ("Skaidrosim moduli kā attālumu līdz nullei un noteiksim pretēju "
          "skaitļu moduļus.")

SATURS = [
    Sakums("Cik tālu, nevis kurā pusē",
           zimejums=taisne(-6, 6, 2, [(-4, "4 soļi"), (4, "4 soļi")]),
           paraksts="Abi skaitļi ir četrus soļus no nulles, tāpēc abu "
                    "modulis ir 4.",
           fakti=["Modulis ir attālums no skaitļa līdz nullei.",
                  "Attālums nekad nav negatīvs.",
                  "Pretējiem skaitļiem moduļi ir vienādi."]),

    Doma("Modulis ir attālums, tāpēc tas nav negatīvs",
         "Skaitļa modulis ir tā attālums līdz nullei uz skaitļu taisnes; "
         "pozitīvam skaitlim tas ir pats skaitlis, negatīvam - tā pretējais.",
         soli=[
             "Paskaties uz skaitļa zīmi.",
             "Ja skaitlis ir pozitīvs vai nulle, modulis ir pats skaitlis.",
             "Ja negatīvs, modulis ir tā pretējais skaitlis.",
             "Pieraksti rezultātu - tas nekad nav mazāks par nulli.",
             "Pārbaudi uz taisnes: cik soļu līdz nullei?",
         ],
         pieze="Nullei modulis ir nulle - attālums no nulles līdz nullei "
               "ir nekāds. Tas ir vienīgais skaitlis, kura modulis ir nulle."),

    Slidnis("Modulis nekad nav negatīvs",
            [{"v": "skaitlis −5", "teksts": "modulis 5", "josla": 100},
             {"v": "skaitlis −2", "teksts": "modulis 2", "josla": 40},
             {"v": "skaitlis 0", "teksts": "modulis 0", "josla": 0},
             {"v": "skaitlis 3", "teksts": "modulis 3", "josla": 60},
             {"v": "skaitlis 5", "teksts": "modulis 5", "josla": 100}],
            ievads="Spied soli pa solim: skaitlis iet no −5 līdz 5, bet "
                   "modulis vispirms sarūk līdz nullei un tad atkal aug."),

    Paraugs("Atrodi moduļus",
            uzd="Kāds ir skaitļu −4; 7 un 0 modulis?",
            soli=[
                ("−4 ir 4 soļus no nulles",
                 "Modulis ir 4."),
                ("7 ir 7 soļus no nulles",
                 "Modulis ir 7."),
                ("0 ir nulles attālumā no nulles",
                 "Modulis ir 0."),
                ("Neviens no moduļiem nav negatīvs",
                 "Attālums nevar būt negatīvs."),
            ],
            atbilde="4; 7 un 0"),

    Ievadi("Atrodi moduli", [
        {"jaut": "Kāds ir skaitļa −4 modulis?",
         "atb": ["4"], "padoms": "Attālums līdz nullei."},
        {"jaut": "Kāds ir skaitļa 7 modulis?",
         "atb": ["7"], "padoms": "Pozitīvam skaitlim modulis ir pats "
                                 "skaitlis."},
        {"jaut": "Kāds ir skaitļa 0 modulis?",
         "atb": ["0"], "padoms": "Attālums ir nekāds."},
        {"jaut": "Kāds ir skaitļa −2,5 modulis?",
         "atb": ["2,5", "2.5"], "padoms": "Arī daļskaitļiem."},
        {"jaut": "Kuriem diviem skaitļiem modulis ir 6? Ieraksti negatīvo.",
         "atb": ["-6", "−6"], "padoms": "6 un −6."},
        {"jaut": "Kāds ir skaitļa −{3|4} modulis? Atbildi raksti kā a/b.",
         "atb": ["3/4"], "padoms": "Maina zīmi."},
    ], pamats=4),

    Varianti("Ko pasaka modulis?", [
        {"jaut": "Modulis ir...",
         "opcijas": ["attālums līdz nullei", "skaitļa zīme",
                     "pretējais skaitlis", "skaitļa puse"],
         "pareizi": 0,
         "padoms": "Attālums, ne virziens."},
        {"jaut": "Vai modulis var būt negatīvs?",
         "opcijas": ["Nē, nekad", "Jā, negatīviem skaitļiem",
                     "Jā, dažreiz", "Tikai nullei"],
         "pareizi": 0,
         "padoms": "Attālums nav negatīvs."},
        {"jaut": "Kuriem skaitļiem moduļi ir vienādi?",
         "opcijas": ["Pretējiem skaitļiem", "Visiem pozitīvajiem",
                     "Visiem negatīvajiem", "Nevienam"],
         "pareizi": 0,
         "padoms": "Vienāds attālums no nulles."},
        {"jaut": "Cik skaitļiem modulis ir 0?",
         "opcijas": ["Vienam", "Diviem", "Nevienam", "Bezgalīgi daudz"],
         "pareizi": 0,
         "padoms": "Tikai pašai nullei."},
    ], pamats=4),

    Pasaule("Cik tālu no jūras līmeņa?",
            Ievadi("", [
                {"jaut": "Zemūdene ir −120 m dziļumā. Cik metru tā ir no "
                         "jūras līmeņa?",
                 "atb": ["120"], "padoms": "Attālums, ne zīme."},
                {"jaut": "Lidmašīna ir 120 m virs jūras līmeņa. Cik metru tā "
                         "ir no jūras līmeņa?",
                 "atb": ["120"], "padoms": "Tas pats attālums."},
                {"jaut": "Kura atrodas tālāk no jūras līmeņa: −80 m vai "
                         "50 m? Ieraksti moduli lielākajam attālumam.",
                 "atb": ["80"], "padoms": "Salīdzina moduļus."},
                {"jaut": "Zemūdene no −120 m pacēlās līdz −40 m. Par cik "
                         "metriem?",
                 "atb": ["80"], "padoms": "120 − 40."},
            ]),
            pavediens="planeta",
            konteksts="Dziļumu un augstumu mēra no viena un tā paša jūras "
                      "līmeņa - tikai dažādos virzienos.",
            kapec="Modulis pasaka attālumu neatkarīgi no virziena."),

    Zimejums("Vienāds modulis, dažādas zīmes",
             taisne(-8, 8, 4, [(-6, "−6"), (6, "6")]),
             paskaidro="Abiem skaitļiem modulis ir 6. Tas ir vienīgais, kas "
                       "tiem kopīgs.",
             ievads="Modulis nešķiro virzienus."),

    Kopsavilkums([
        "Skaidroju moduli kā attālumu līdz nullei.",
        "Nosaku pozitīvu, negatīvu un nulles moduli.",
        "Zinu, ka pretējiem skaitļiem moduļi ir vienādi.",
        "Zinu, ka modulis nekad nav negatīvs.",
    ]),

    Majas([
        "Atrodi moduļus skaitļiem −12; 5; 0 un −0,5.",
        "Uzraksti divus skaitļus, kuru modulis ir 9.",
        "Paskaidro kādam mājās, kāpēc modulis nevar būt negatīvs.",
    ]),
]
