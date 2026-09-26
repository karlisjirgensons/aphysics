# -*- coding: utf-8 -*-
"""3. klase, 82. stunda: «Ko rāda saucējs un ko skaitītājs?»

Pieraksts jau ir; tagad jāsaprot, ko katrs skaitlis dara. Galvenā doma ir
tā, ka abi skaitļi atbild uz dažādiem jautājumiem: saucējs - «cik daļās
sadalīts», skaitītājs - «cik daļu paņemts».
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, Zimejums,
                         dala)

TEMA = "Ko rāda saucējs un ko skaitītājs?"

MERKIS = ("Skaidrosim, ka saucējs rāda dalījumu skaitu, bet skaitītājs - "
          "ņemto daļu skaitu.")

SATURS = [
    Sakums("Kurš skaitlis daļā ir svarīgāks?",
           zimejums=dala(4, 3, "3/4", "saucējs 4, skaitītājs 3"),
           paraksts="Saucējs sadala, skaitītājs skaita.",
           fakti=["Saucējs pasaka, cik vienādās daļās sadalīts veselais.",
                  "Skaitītājs pasaka, cik šādu daļu ir ņemts."]),

    Doma("Saucējs sadala, skaitītājs skaita",
         "Vispirms strādā saucējs - tas sadala veselo; tikai tad skaitītājs "
         "saskaita, cik daļu paņemtas.",
         soli=[
             "Paskaties uz saucēju - tas pasaka, cik liela ir viena daļa.",
             "Paskaties uz skaitītāju - tas pasaka, cik tādu daļu ņem.",
             "Jo lielāks saucējs, jo mazāka katra daļa.",
             "Jo lielāks skaitītājs, jo vairāk daļu ņemts.",
         ],
         pieze="Tāpēc {1|8} ir mazāks par {1|4}, bet {3|8} ir lielāks par "
               "{1|8} - saucējs un skaitītājs strādā pretējos virzienos."),

    Slidnis("Kas notiek, mainot skaitītāju",
            soli=[
                {"v": "{1|8}", "teksts": "Viena astotdaļa.", "josla": 12},
                {"v": "{3|8}", "teksts": "Trīs astotdaļas.", "josla": 37},
                {"v": "{5|8}", "teksts": "Piecas astotdaļas.", "josla": 62},
                {"v": "{8|8}", "teksts": "Astoņas astotdaļas - viss vesels.",
                 "josla": 100},
            ],
            ievads="Saucējs paliek 8, mainās tikai skaitītājs."),

    Paraugs("Ko nozīmē katrs skaitlis?",
            uzd="Paskaidro, ko nozīmē skaitļi daļā {3|4}.",
            soli=[
                ("Saucējs 4",
                 "Veselais sadalīts četrās vienādās daļās."),
                ("Skaitītājs 3",
                 "No šīm četrām daļām paņemtas trīs."),
                ("{3|4} ir trīs ceturtdaļas",
                 "Vēl viena ceturtdaļa pietrūkst līdz veselajam."),
            ],
            atbilde="trīs no četrām vienādām daļām"),

    Ievadi("Saucējs un skaitītājs", [
        {"jaut": "Daļā {5|9} - cik vienādās daļās sadalīts veselais?",
         "atb": ["9"], "padoms": "To pasaka saucējs."},
        {"jaut": "Daļā {5|9} - cik daļu ir ņemts?", "atb": ["5"],
         "padoms": "To pasaka skaitītājs."},
        {"jaut": "Cik daļu pietrūkst līdz veselajam daļā {5|9}?",
         "atb": ["4"], "padoms": "9 − 5."},
        {"jaut": "Cik astotdaļu ir vienā veselajā?", "atb": ["8"],
         "padoms": "Tik, cik pasaka saucējs."},
        {"jaut": "Cik daļu pietrūkst līdz veselajam daļā {2|7}?",
         "atb": ["5"], "padoms": "7 − 2."},
        {"jaut": "Daļā {4|4} - cik tas ir veselo?", "atb": ["1"],
         "padoms": "Visas daļas ir ņemtas."},
    ], pamats=4),

    Zimejums("Tas pats skaitītājs, cits saucējs",
             dala(3, 1, "1/3", "viena trešdaļa"),
             paskaidro="Salīdzini ar {1|8}: skaitītājs abām ir 1, bet "
                       "trešdaļa ir daudz lielāka par astotdaļu.",
             ievads="Saucējs nosaka daļas lielumu."),

    Varianti("Kurš skaitlis ko dara?", [
        {"jaut": "Ko rāda saucējs?",
         "opcijas": ["Cik vienādās daļās sadalīts veselais",
                     "Cik daļu ņemts", "Cik daļu palicis",
                     "Cik liela ir figūra"],
         "pareizi": 0, "padoms": "Saucējs sadala."},
        {"jaut": "Kura daļa ir lielāka?",
         "opcijas": ["{1|3}", "{1|8}", "{1|10}", "Visas vienādas"],
         "pareizi": 0, "padoms": "Mazāks saucējs - lielāka daļa."},
        {"jaut": "Kura daļa ir lielāka?",
         "opcijas": ["{5|8}", "{3|8}", "{1|8}", "Visas vienādas"],
         "pareizi": 0, "padoms": "Saucējs viens, skatās skaitītāju."},
        {"jaut": "Cik daļu pietrūkst līdz veselajam daļā {7|10}?",
         "opcijas": ["3", "7", "10", "17"],
         "pareizi": 0, "padoms": "10 − 7."},
    ], pamats=4),

    Pasaule("Cik distances ir noskrietas?",
            Ievadi("", [
                {"jaut": "Distanci sadala 8 posmos. Skrējējs pabeidzis 3. "
                         "Cik posmu vēl atlicis?",
                 "atb": ["5"], "padoms": "8 − 3."},
                {"jaut": "Cik posmu ir {3|4} no 8 posmiem?",
                 "atb": ["6"], "padoms": "8 : 4 = 2; 3 · 2."},
                {"jaut": "Distance ir 800 m, viens posms ir {1|8}. Cik metru "
                         "ir viens posms?",
                 "atb": ["100"], "padoms": "800 : 8."},
                {"jaut": "Cik metru ir 3 posmi?", "atb": ["300"],
                 "padoms": "3 · 100."},
            ]),
            pavediens="sports",
            konteksts="Garās distances sadala posmos, un skrējējs zina, cik "
                      "daļu jau aiz muguras.",
            kapec="Daļa pasaka progresu labāk nekā metri: {3|4} ir "
                  "saprotams uzreiz."),

    Kopsavilkums([
        "Zinu, ka saucējs rāda dalījumu skaitu.",
        "Zinu, ka skaitītājs rāda ņemto daļu skaitu.",
        "Zinu, ka lielāks saucējs dod mazāku daļu.",
        "Aprēķinu, cik daļu pietrūkst līdz veselajam.",
    ]),

    Majas([
        "Uzzīmē {3|5} un paskaidro, ko nozīmē katrs skaitlis.",
        "Atrodi divas daļas ar vienādu skaitītāju un salīdzini tās.",
        "Pastāsti mājiniekiem, kāpēc {1|8} ir mazāks par {1|4}.",
    ]),
]
