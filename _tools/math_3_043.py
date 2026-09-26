# -*- coding: utf-8 -*-
"""3. klase, 43. stunda: «Kur risinājumā ir kļūda?»

Svešu risinājumu lasīt ir grūtāk, nekā rēķināt pašam, un tieši tāpēc tas ir
vērtīgi: jāatrod ne tikai nepareizais skaitlis, bet arī iemesls. Trīs
tipiskākās kļūdas - secība, iekavas un pārrakstīšanās - te ir visas.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kur risinājumā ir kļūda?"

MERKIS = ("Pārbaudīsim dotu risinājumu, atradīsim kļūdu un komentēsim tās "
          "cēloni.")

SATURS = [
    Sakums("Trīs risinājumi, viena kļūda katrā - vai atradīsi?",
           zimejums=restis([["2 + 3 · 4 = 20", "secība"],
                            ["(6 + 2) · 3 = 12", "iekavas"],
                            ["47 + 28 = 65", "pārrakstīšanās"]],
                           "trīs tipiskas kļūdas"),
           paraksts="Katrai kļūdai ir savs cēlonis - un savs labojums.",
           fakti=["Visbiežākā kļūda ir nepareiza darbību secība.",
                  "Otrā biežākā - iekavas, kas aizmirstas vai lieki "
                  "ieliktas."]),

    Doma("Vispirms atrodi kļūdu, tad tās cēloni",
         "Labot bez cēloņa nozīmē to pašu kļūdu atkārtot nākamajā uzdevumā.",
         soli=[
             "Izrēķini uzdevumu pats un salīdzini atbildes.",
             "Ja atbildes atšķiras, meklē pirmo soli, kurā tās šķīrās.",
             "Pasaki, kāpēc tur radās kļūda.",
             "Izlabo risinājumu no šī soļa uz priekšu.",
         ],
         pieze="Ja atšķiras tikai pēdējais solis, kļūda visdrīzāk ir "
               "pārrakstīšanās; ja pirmais - domāšanā."),

    Paraugs("Kur kļūdījās šis skolēns?",
            uzd="Skolēns uzrakstīja: 2 + 3 · 4 = 20. Kur ir kļūda?",
            soli=[
                ("Viņš rēķināja 2 + 3 = 5, tad 5 · 4 = 20",
                 "Atjauno viņa domu gaitu."),
                ("Darbību secība prasa reizināt pirmo",
                 "Reizināšana ir augstākā pakāpienā nekā saskaitīšana."),
                ("3 · 4 = 12; 2 + 12 = 14",
                 "Pareizais risinājums; kļūdas cēlonis - darbību secība."),
            ],
            atbilde="14; kļūda bija darbību secībā"),

    Ievadi("Izlabo kļūdu", [
        {"jaut": "«5 + 2 · 3 = 21» - cik ir pareizi?", "atb": ["11"],
         "padoms": "Vispirms 2 · 3."},
        {"jaut": "«(4 + 6) · 2 = 16» - cik ir pareizi?", "atb": ["20"],
         "padoms": "Vispirms iekavas: 10 · 2."},
        {"jaut": "«20 − 4 · 3 = 48» - cik ir pareizi?", "atb": ["8"],
         "padoms": "Vispirms 4 · 3."},
        {"jaut": "«36 : (2 + 4) = 22» - cik ir pareizi?", "atb": ["6"],
         "padoms": "36 : 6."},
        {"jaut": "«8 · 3 + 2 = 40» - cik ir pareizi?", "atb": ["26"],
         "padoms": "24 + 2."},
        {"jaut": "«(15 − 5) : 5 = 14» - cik ir pareizi?", "atb": ["2"],
         "padoms": "10 : 5."},
    ], pamats=4,
        ievads="Katrā rindā ir nepareizs risinājums. Ieraksti pareizo "
               "atbildi."),

    Zimejums("Kļūda un tās cēlonis",
             restis([["kļūda", "cēlonis"],
                     ["2 + 3 · 4 = 20", "saskaitīja pirms reizināšanas"],
                     ["(6 + 2) · 3 = 12", "reizināja tikai ar 2"],
                     ["47 + 28 = 65", "aizmirsa pāreju desmitā"]],
                    "trīs kļūdas, trīs cēloņi"),
             paskaidro="Katru cēloni var nosaukt vienā teikumā - un tieši "
                       "tas neļauj kļūdu atkārtot.",
             ievads="Šī tabula ir kļūdu vārdnīca."),

    Varianti("Kāds ir kļūdas cēlonis?", [
        {"jaut": "«10 − 6 : 2 = 2» - kāda ir kļūda?",
         "opcijas": ["Atņēma pirms dalīšanas", "Dalīja nepareizi",
                     "Pārrakstījās", "Kļūdas nav"],
         "pareizi": 0, "padoms": "Pareizi ir 10 − 3 = 7."},
        {"jaut": "«3 · (5 + 1) = 16» - kāda ir kļūda?",
         "opcijas": ["Reizināja tikai ar 5", "Saskaitīja nepareizi",
                     "Aizmirsa iekavas", "Kļūdas nav"],
         "pareizi": 0, "padoms": "Pareizi ir 3 · 6 = 18."},
        {"jaut": "«65 − 27 = 42» - kāda ir kļūda?",
         "opcijas": ["Aizmirsa aizņēmumu", "Nepareiza secība",
                     "Aizmirsa iekavas", "Kļūdas nav"],
         "pareizi": 0, "padoms": "Pareizi ir 38."},
        {"jaut": "Kāpēc svarīgi nosaukt cēloni?",
         "opcijas": ["Lai kļūdu neatkārtotu", "Lai darbs būtu garāks",
                     "Tā prasa skolotājs", "Lai atbilde būtu skaistāka"],
         "pareizi": 0, "padoms": "Labojums bez cēloņa ir tikai viens "
                                 "uzdevums."},
    ], pamats=4),

    Pasaule("Kur kļūdījās programma?",
            Ievadi("", [
                {"jaut": "Programma rēķināja 100 − 5 · 8 un rādīja 760. Cik "
                         "ir pareizi?",
                 "atb": ["60"], "padoms": "Vispirms 5 · 8 = 40."},
                {"jaut": "Tā rēķināja (30 + 10) : 8 un rādīja 31. Cik ir "
                         "pareizi?",
                 "atb": ["5"], "padoms": "40 : 8."},
                {"jaut": "Tā rēķināja 6 · (12 − 4) un rādīja 68. Cik ir "
                         "pareizi?",
                 "atb": ["48"], "padoms": "6 · 8."},
                {"jaut": "Tā rēķināja 72 : 8 + 4 un rādīja 6. Cik ir "
                         "pareizi?",
                 "atb": ["13"], "padoms": "9 + 4."},
            ]),
            pavediens="dati",
            konteksts="Programmās kļūdas meklē tieši tā: atrod pirmo soli, "
                      "kurā rezultāts vairs nav tāds, kā gaidīts.",
            kapec="Kļūdas cēlonis ir svarīgāks par pašu kļūdu."),

    Kopsavilkums([
        "Pārbaudu dotu risinājumu un atrodu kļūdu.",
        "Nosaku, kurā solī risinājums aizgāja greizi.",
        "Nosaucu kļūdas cēloni vienā teikumā.",
        "Izlaboju risinājumu no kļūdainā soļa.",
    ]),

    Majas([
        "Atrodi savā burtnīcā vienu izlaboto uzdevumu un pasaki tā cēloni.",
        "Uzraksti risinājumu ar kļūdu un iedod to mājiniekiem atrast.",
        "Izveido savu kļūdu vārdnīcu ar trim ierakstiem.",
    ]),
]
