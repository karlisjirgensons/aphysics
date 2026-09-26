# -*- coding: utf-8 -*-
"""3. klase, 62. stunda: «Kā izlasīt četrciparu skaitli?»

Skaitļi aiz simta. Galvenais nav lielums, bet *vietas*: cipara nozīmi nosaka
tas, kur tas stāv. Tieši tāpēc te vispirms parādās vietu tabula un tikai tad
lasīšana - skaitli izlasa, ejot no lielākās vietas uz mazāko.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, Zimejums,
                         restis)

TEMA = "Kā izlasīt četrciparu skaitli?"

MERKIS = ("Lasīsim un rakstīsim trīsciparu un četrciparu skaitļus un "
          "noteiksim to decimālo sastāvu.")

SATURS = [
    Sakums("Cik tālu no Rīgas ir Ēģiptes piramīdas?",
           zimejums=restis([["tūkstoši", "simti", "desmiti", "vieni"],
                            [3, 2, 0, 5]],
                           "3205"),
           paraksts="Katram ciparam sava vieta un sava vērtība.",
           fakti=["Līdz Ēģiptei no Rīgas ir apmēram 3200 km.",
                  "Cipara vērtību nosaka tā vieta, ne pats cipars.",
                  "Četrciparu skaitlī lielākā vieta ir tūkstoši."]),

    Doma("Cipara vērtību nosaka tā vieta",
         "Vietas no labās puses ir vieni, desmiti, simti un tūkstoši - katra "
         "nākamā 10 reizes lielāka.",
         soli=[
             "Saskaiti ciparus - tik vietu skaitlim ir.",
             "Pieraksti skaitli vietu tabulā.",
             "Izlasi no kreisās puses: vispirms tūkstošus, tad simtus.",
             "Ja vietā ir 0, to nenosauc, bet vietu tā aizņem.",
         ],
         pieze="Skaitlī 3205 nulle stāv desmitu vietā. Ja to izņemtu, sanāktu "
               "325 - pavisam cits skaitlis."),

    Slidnis("Kā aug vietas",
            soli=[
                {"v": "5", "teksts": "Pieci vieni.", "josla": 5},
                {"v": "50", "teksts": "Pieci desmiti.", "josla": 20},
                {"v": "500", "teksts": "Pieci simti.", "josla": 55},
                {"v": "5000", "teksts": "Pieci tūkstoši.", "josla": 100},
            ],
            ievads="Cipars ir tas pats, bet vieta - katru reizi citā "
                   "pakāpienā."),

    Paraugs("Kā izlasa 2408?",
            uzd="Izlasi skaitli 2408 un pasaki, ko nozīmē katrs cipars.",
            soli=[
                ("2 | 4 | 0 | 8",
                 "Četras vietas: tūkstoši, simti, desmiti, vieni."),
                ("divi tūkstoši četri simti astoņi",
                 "Desmitu vietā ir nulle, tāpēc to nenosauc."),
                ("2 → 2000, 4 → 400, 8 → 8",
                 "Katra cipara vērtība pēc tā vietas."),
            ],
            atbilde="divi tūkstoši četri simti astoņi"),

    Ievadi("Ko nozīmē cipars?", [
        {"jaut": "Skaitlī 3205 - ko nozīmē cipars 3?", "atb": ["3000"],
         "padoms": "Tas stāv tūkstošu vietā."},
        {"jaut": "Skaitlī 3205 - ko nozīmē cipars 2?", "atb": ["200"],
         "padoms": "Tas stāv simtu vietā."},
        {"jaut": "Skaitlī 1740 - ko nozīmē cipars 7?", "atb": ["700"],
         "padoms": "Simtu vieta."},
        {"jaut": "Skaitlī 1740 - ko nozīmē cipars 4?", "atb": ["40"],
         "padoms": "Desmitu vieta."},
        {"jaut": "Uzraksti ar cipariem: divi tūkstoši seši simti",
         "atb": ["2600"], "padoms": "Desmitu un vienu vietā ir nulles."},
        {"jaut": "Uzraksti ar cipariem: viens tūkstotis piecdesmit",
         "atb": ["1050"], "padoms": "Simtu vietā ir nulle."},
    ], pamats=4),

    Zimejums("Vietu tabula",
             restis([["T", "S", "D", "V"],
                     [1, 7, 4, 0],
                     [2, 0, 0, 8]],
                    "1740 un 2008"),
             paskaidro="Otrajā skaitlī divas nulles tur vietu - bez tām "
                       "sanāktu 28.",
             ievads="T ir tūkstoši, S simti, D desmiti, V vieni."),

    Varianti("Kurš skaitlis tas ir?", [
        {"jaut": "Kā pieraksta «trīs tūkstoši četrdesmit»?",
         "opcijas": ["3040", "3400", "340", "30040"],
         "pareizi": 0, "padoms": "Simtu vietā ir nulle."},
        {"jaut": "Kurš skaitlis ir lielākais?",
         "opcijas": ["4002", "999", "3999", "2500"],
         "pareizi": 0, "padoms": "Vispirms salīdzini ciparu skaitu."},
        {"jaut": "Skaitlī 5060 - ko nozīmē cipars 6?",
         "opcijas": ["60", "600", "6", "6000"],
         "pareizi": 0, "padoms": "Tas stāv desmitu vietā."},
        {"jaut": "Cik ciparu ir mazākajam četrciparu skaitlim?",
         "opcijas": ["4", "3", "5", "1"],
         "pareizi": 0, "padoms": "Mazākais ir 1000."},
    ], pamats=4),

    Pasaule("Cik tālu ir ceļojuma galamērķis?",
            Ievadi("", [
                {"jaut": "Līdz Parīzei no Rīgas ir 1700 km. Ko nozīmē "
                         "cipars 7?",
                 "atb": ["700"], "padoms": "Simtu vieta."},
                {"jaut": "Līdz Romai ir 2100 km. Ko nozīmē cipars 2?",
                 "atb": ["2000"], "padoms": "Tūkstošu vieta."},
                {"jaut": "Uzraksti ar cipariem: divi tūkstoši astoņi simti "
                         "km",
                 "atb": ["2800"], "padoms": "Desmitu un vienu vietā nulles."},
                {"jaut": "Par cik kilometriem Roma ir tālāk nekā Parīze?",
                 "atb": ["400"], "padoms": "2100 − 1700."},
            ]),
            pavediens="celojums",
            konteksts="Attālumus starp pilsētām raksta tūkstošos kilometru - "
                      "tāpēc lielie skaitļi ceļojumā ir katrā solī.",
            kapec="Pareizi izlasīts skaitlis pasaka, vai ceļš ir dienas vai "
                  "nedēļas garš."),

    Kopsavilkums([
        "Lasu un rakstu trīsciparu un četrciparu skaitļus.",
        "Zinu vietas: vieni, desmiti, simti, tūkstoši.",
        "Nosaku, ko nozīmē katrs cipars pēc tā vietas.",
        "Zinu, ka nulle tur vietu, arī ja to nenosauc.",
    ]),

    Majas([
        "Atrodi mājās vai ziņās trīs skaitļus, kas lielāki par 1000.",
        "Izlasi tos skaļi un pasaki, ko nozīmē katrs cipars.",
        "Uzraksti savu dzimšanas gadu vietu tabulā.",
    ]),
]
