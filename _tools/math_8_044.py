# -*- coding: utf-8 -*-
"""8. klase, 44. stunda: «Kad daļu var pierakstīt kā decimāldaļu?»

Katru daļu var izdalīt, bet dažreiz dalīšana beidzas ({3|8} = 0,375), dažreiz
- nekad ({1|3} = 0,333...). Stunda atklāj likumu: nesaīsināmas daļas saucējā
drīkst būt tikai 2 un 5, jo tie ir 10 reizinātāji.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Slidnis, Varianti, restis)

TEMA = "Kad daļu var pierakstīt kā decimāldaļu?"

MERKIS = ("Pārveidosim parasto daļu par galīgu vai periodisku decimāldaļu.")

SATURS = [
    Sakums("{3|8} un {1|3} - kurš dalījums beidzas?",
           zimejums=restis([["3/8", "0,375", "galīga"],
                            ["1/3", "0,333...", "bezgalīga"],
                            ["7/20", "0,35", "galīga"]]),
           paraksts="Dažas daļas «beidzas», citas - nekad.",
           fakti=["8 = 2³, 20 = 2² · 5 - tikai divnieki un pieci.",
                  "3 nav 10 reizinātājs - dalīšana nebeidzas.",
                  "Saucējs izšķir visu."]),

    Doma("Galīga vai periodiska?",
         "Nesaīsināmu daļu var pierakstīt kā galīgu decimāldaļu tikai tad, ja "
         "tās saucējs sadalās pirmreizinātājos tikai ar 2 un 5.",
         soli=[
             "Saīsini daļu.",
             "Sadali saucēju pirmreizinātājos.",
             "Tikai 2 un 5 - galīga decimāldaļa.",
             "Ir cits pirmreizinātājs (3, 7, 11...) - bezgalīga periodiska.",
         ],
         pieze="Iemesls: galīga decimāldaļa ir daļa ar saucēju 10, 100, 1000... "
               "un 10 = 2 · 5."),

    Slidnis("Dala 1 : 7 stūrī", [
        {"v": "0,1", "teksts": "10 : 7 = 1, atlikums 3"},
        {"v": "0,14", "teksts": "30 : 7 = 4, atlikums 2"},
        {"v": "0,142", "teksts": "20 : 7 = 2, atlikums 6"},
        {"v": "0,142857", "teksts": "Atlikumi 4, 5, 1..."},
        {"v": "0,142857142857...", "teksts": "Atlikums 1 atkārtojas - cipari "
                                             "arī"},
    ], ievads="Atlikumu var būt tikai 6 dažādi - tāpēc cipari atkārtojas."),

    Paraugs("Pārveido ar saucēju 10, 100, 1000",
            uzd="Pārveido {7|25} un {3|40} decimāldaļās.",
            soli=[
                ("{7|25} = {28|100} = 0,28", "· 4."),
                ("{3|40} = {75|1000} = 0,075", "· 25."),
            ],
            atbilde="0,28; 0,075"),

    Ievadi("Pārveido decimāldaļā", [
        {"jaut": "{3|8}", "atb": ["0,375", "0.375"],
         "padoms": "{375|1000}."},
        {"jaut": "{9|20}", "atb": ["0,45", "0.45"], "padoms": "{45|100}."},
        {"jaut": "{11|50}", "atb": ["0,22", "0.22"], "padoms": "{22|100}."},
        {"jaut": "{2|3} - pirmie trīs cipari aiz komata",
         "atb": ["0,666", "0.666", "0,667"], "padoms": "0,666..."},
        {"jaut": "{21|28} - saīsini un pārveido",
         "atb": ["0,75", "0.75"], "padoms": "{3|4}."},
        {"jaut": "{5|16}", "atb": ["0,3125", "0.3125"],
         "padoms": "16 = 2^4."},
    ], pamats=4),

    Varianti("Galīga vai bezgalīga?", [
        {"jaut": "{7|40}",
         "opcijas": ["Galīga", "Bezgalīga periodiska"],
         "pareizi": 0, "padoms": "40 = 2^3 · 5.", "jaukt": False},
        {"jaut": "{5|12}",
         "opcijas": ["Galīga", "Bezgalīga periodiska"],
         "pareizi": 1, "padoms": "12 = 2^2 · 3.", "jaukt": False},
        {"jaut": "{6|15}",
         "opcijas": ["Galīga", "Bezgalīga periodiska"],
         "pareizi": 0, "padoms": "Saīsini: {2|5}.", "jaukt": False},
        {"jaut": "{1|11}",
         "opcijas": ["Galīga", "Bezgalīga periodiska"],
         "pareizi": 1, "padoms": "11 ir pirmskaitlis.", "jaukt": False},
    ]),

    Pasaule("Receptes pārrēķins",
            Ievadi("", [
                {"jaut": "Receptē {3|4} glāzes cukura, glāze 200 g. Cik "
                         "gramu?",
                 "atb": ["150"], "padoms": "0,75 · 200."},
                {"jaut": "Recepte 3 porcijām, vajag 1 porciju: {1|3} no "
                         "300 g miltu. Cik gramu?",
                 "atb": ["100"], "padoms": "Precīzi, nevis 0,33 · 300."},
                {"jaut": "{1|3} no 250 g sviesta līdz veseliem gramiem?",
                 "atb": ["83"], "padoms": "83,333..."},
            ]),
            pavediens="virtuve",
            konteksts="Virtuves svari rāda decimāldaļas, bet receptes - "
                      "parastas daļas. Dažas pārveidojas precīzi, citas - nē.",
            kapec="{1|3} precīzi var izrēķināt tikai tad, ja skaitlis dalās "
                  "ar 3."),

    Kopsavilkums([
        "Pārveidoju daļu par decimāldaļu.",
        "Pēc saucēja nosaku, vai decimāldaļa būs galīga.",
        "Paskaidroju, kāpēc dalīšana atkārtojas.",
    ]),

    Majas([
        "Pārveido decimāldaļās: {7|8}, {13|20}, {5|6}.",
        "Nosaki bez dalīšanas, kuras no {1|6}, {3|16}, {7|35} ir galīgas.",
        "Izdali 1 : 13 un atrodi, pēc cik cipariem sākas atkārtojums.",
    ]),
]
