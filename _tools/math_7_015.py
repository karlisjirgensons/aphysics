# -*- coding: utf-8 -*-
"""7. klase, 15. stunda: «Kā varbūtību aprēķina teorētiski?»

Ja visi iznākumi ir vienādi iespējami, varbūtību var aprēķināt bez
eksperimenta: labvēlīgo iznākumu skaitu dala ar visu iznākumu skaitu.
Stunda iemāca formulu P(A) = {m|n} un to, kad tā der.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Simulacija, Varianti, Zimejums,
                         restis)

TEMA = "Kā varbūtību aprēķina teorētiski?"

MERKIS = ("Iemācīsimies aprēķināt notikuma varbūtību un pierakstīt to kā "
          "daļu vai procentos.")

SATURS = [
    Sakums("Cik liela iespēja, ka izlozē būsi pirmais?",
           fakti=["Klasē ir 25 skolēni, izlozē vienu.",
                  "Katram ir vienādas izredzes - 1 no 25.",
                  "P = {1|25} = 0,04 = 4 %."]),

    Doma("P(A) = labvēlīgie : visi",
         "Ja visi n iznākumi ir vienādi iespējami un notikumam A ir labvēlīgi "
         "m no tiem, tad notikuma A varbūtība ir P(A) = {m|n}.",
         soli=[
             "Uzskaiti visus iznākumus (n) - pārbaudi, vai tie vienādi "
             "iespējami.",
             "Saskaiti labvēlīgos (m) - tos, kuros A notiek.",
             "Uzraksti daļu {m|n} un saīsini.",
             "Ja vajag, pārveido decimāldaļā vai procentos.",
         ],
         pieze="Burts P nāk no latīņu «probabilitas». Formula neder, ja "
               "iznākumi nav vienādi iespējami, piemēram, pogai."),

    Paraugs("Kauliņš",
            uzd="Met vienu kauliņu. Kāda ir varbūtība, ka uzkritīs pāra "
                "skaitlis, kas lielāks nekā 2?",
            soli=[
                ("Visi iznākumi: 1; 2; 3; 4; 5; 6 - n = 6",
                 "Godīgam kauliņam vienādi iespējami."),
                ("Labvēlīgie: 4; 6 - m = 2", "Pāra un lielāki nekā 2."),
                ("P(A) = {2|6} = {1|3}", "Saīsina."),
                ("{1|3} ≈ 0,33 ≈ 33 %", "Noapaļo, tāpēc «≈»."),
            ],
            atbilde="P(A) = {1|3} ≈ 33 %"),

    Zimejums("Divi kauliņi - 36 iznākumi",
             restis([["+", "1", "2", "3", "4", "5", "6"],
                     ["1", "2", "3", "4", "5", "6", "7"],
                     ["2", "3", "4", "5", "6", "7", "8"],
                     ["3", "4", "5", "6", "7", "8", "9"],
                     ["4", "5", "6", "7", "8", "9", "10"],
                     ["5", "6", "7", "8", "9", "10", "11"],
                     ["6", "7", "8", "9", "10", "11", "12"]]),
             ievads="Summu tabula: katra rūtiņa ir viens vienādi iespējams "
                    "iznākums.",
             paskaidro="Summa 7 ir 6 rūtiņās: P = {6|36} = {1|6}. Summa 12 - "
                       "tikai vienā: P = {1|36}."),

    Ievadi("Aprēķini varbūtību (daļā)", [
        {"jaut": "Maisā 3 sarkanas un 5 zilas bumbiņas. P(sarkana) = ?",
         "atb": ["{3|8}", "3/8"], "padoms": "3 no 8. Raksti 3/8.",
         "vieta": "piemēram, 2/5"},
        {"jaut": "Met kauliņu. P(skaitlis dalās ar 3) = ?",
         "atb": ["{1|3}", "1/3", "2/6"], "padoms": "3 un 6 - 2 no 6.",
         "vieta": "piemēram, 2/5"},
        {"jaut": "Met divus kauliņus. P(summa ir 12) = ?",
         "atb": ["{1|36}", "1/36"], "padoms": "Tikai 6 + 6.",
         "vieta": "piemēram, 2/5"},
        {"jaut": "Izvēlas nejaušu mēneša dienu 30 dienu mēnesī. "
                 "P(diena ir 13.) = ?",
         "atb": ["{1|30}", "1/30"], "padoms": "1 no 30.",
         "vieta": "piemēram, 2/5"},
        {"jaut": "Met divus kauliņus. P(summa ir 10) = ?",
         "atb": ["{1|12}", "1/12", "3/36"], "padoms": "4+6, 5+5, 6+4.",
         "vieta": "piemēram, 2/5"},
        {"jaut": "No burtiem vārdā «VARBŪTĪBA» izvelk vienu kartīti. "
                 "P(burts B) = ?",
         "atb": ["{2|9}", "2/9"], "padoms": "9 kartītes, B divas.",
         "vieta": "piemēram, 2/5"},
    ], pamats=4, ievads="Daļu ieraksti ar slīpsvītru: 3/8."),

    Simulacija("Pārbaudi ar eksperimentu",
               ["2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"],
               [5], "summa ir 7", teorija="{1|6} ≈ 0,17",
               svari=[1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1],
               ievads="Divu kauliņu summa: katrai summai tik «vietu», cik "
                      "rūtiņu tabulā."),

    Varianti("Vai formula der?", [
        {"jaut": "Futbola spēlē: uzvara, neizšķirts, zaudējums. Vai "
                 "P(uzvara) = {1|3}?",
         "opcijas": ["Nē - iznākumi nav vienādi iespējami",
                     "Jā - ir trīs iznākumi",
                     "Jā, bet tikai finālā",
                     "Nē - varbūtība ir {1|2}"],
         "pareizi": 0,
         "padoms": "Spēcīga komanda uzvar biežāk."},
        {"jaut": "Maisā 2 sarkanas, 2 zilas. Kāda varbūtība izvilkt "
                 "zaļu?",
         "opcijas": ["0", "{1|3}", "{1|4}", "{1|2}"],
         "pareizi": 0,
         "padoms": "Zaļu nav."},
    ]),

    Pasaule("Konkursa balvu izloze",
            Ievadi("", [
                {"jaut": "Izlozē piedalās 400 kuponi, balvu ir 10. Tev ir 1 "
                         "kupons. Varbūtība laimēt procentos (tikai "
                         "skaitli)?",
                 "atb": ["2,5"], "padoms": "10 : 400 = 0,025."},
                {"jaut": "Tev ir 4 kuponi. Varbūtība, ka kāds laimēs, ir "
                         "aptuveni cik procentu (tikai skaitli)?",
                 "atb": ["10"], "padoms": "Aptuveni 4 · 2,5 %."},
                {"jaut": "Cik kuponu vajag, lai varbūtība būtu apmēram "
                         "50 %?",
                 "atb": ["20"], "padoms": "50 : 2,5."},
            ]),
            pavediens="speles",
            konteksts="Veikala izlozes noteikumos parasti ir rakstīts gan "
                      "kuponu, gan balvu skaits.",
            kapec="Ar formulu var novērtēt izredzes pirms piedalīšanās."),

    Kopsavilkums([
        "Aprēķinu P(A) = {m|n}.",
        "Pārbaudu, vai iznākumi ir vienādi iespējami.",
        "Lietoju tabulu diviem kauliņiem.",
        "Pierakstu varbūtību kā daļu, decimāldaļu un procentos.",
    ]),

    Majas([
        "Uzraksti 3 notikumus ar kauliņu, kuru varbūtība ir {1|2}.",
        "Kāda ir varbūtība, ka nejauši izvēlēts klasesbiedrs ir dzimis "
        "vasarā?",
        "Aprēķini P(summa ir 8) diviem kauliņiem.",
    ]),
]
