# -*- coding: utf-8 -*-
"""6. klase, 172. stunda: «Ko gaida 7. klasē?»

Gada pēdējā stunda. Atskats uz to, kas šogad iemācīts, un skats uz priekšu:
nākamgad skaitļiem pievienosies burti, un lielākā daļa likumu paliks tie
paši. Stunda beidzas ar pašvērtējumu, ne ar pārbaudi.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         restis)

TEMA = "Ko gaida 7. klasē?"

MERKIS = ("Apkoposim gada laikā apgūto un ieskatīsimies, kas gaida nākamajā "
          "klasē.")

SATURS = [
    Sakums("Skaitļiem pievienosies burti",
           zimejums=restis([["6. klasē", "7. klasē"],
                            ["3 + (−5)", "a + (−b)"]]),
           paraksts="Likumi paliek tie paši - mainās tikai tas, ka skaitļa "
                    "vietā var būt burts.",
           fakti=["Zīmju likums 7. klasē nemainās.",
                  "Daļu un procentu likumi arī paliek.",
                  "Jaunais būs vienādojumi un izteiksmes ar burtiem."]),

    Doma("Viss šogad mācītais paliek spēkā",
         "Septītajā klasē skaitļu vietā parādās burti, bet visi darbību "
         "likumi ir tie paši, ko apguvi šogad.",
         soli=[
             "Atkārto zīmju likumu visām četrām darbībām.",
             "Atkārto daļu un decimāldaļu pārveidošanu.",
             "Atkārto procentus un attiecību.",
             "Atkārto darbību secību un iekavas.",
             "Pieraksti, kura no šīm vietām tev vēl ir nedroša.",
         ],
         pieze="Vienādojumi, ko risināsi 7. klasē, ir tie paši «atrodi "
               "trūkstošo skaitli» uzdevumi, tikai ar burtu un garāku "
               "pierakstu."),

    Paraugs("No skaitļiem uz burtiem",
            uzd="Kā šī gada zināšanas noderēs 7. klasē?",
            soli=[
                ("3 + (−5) = −2",
                 "Šogad: skaitļi."),
                ("a + (−b) = a − b",
                 "Nākamgad: tas pats likums ar burtiem."),
                ("x + 5 = −3, tātad x = −8",
                 "Tas pats «kurš skaitlis trūkst»."),
                ("Likums nemainās, mainās pieraksts",
                 "Tāpēc šis gads ir pamats nākamajam."),
            ],
            atbilde="likumi paliek, pieraksts kļūst vispārīgāks"),

    Ievadi("Pārbaudi visu gadu", [
        {"jaut": "Cik ir −7 + 12?",
         "atb": ["5"], "padoms": "Zīmju likums."},
        {"jaut": "Cik ir {2|3} · {3|4}? Atbildi raksti kā a/b.",
         "atb": ["1/2", "6/12"], "padoms": "Saīsina."},
        {"jaut": "Cik ir 25 % no 80?",
         "atb": ["20"], "padoms": "80 : 4."},
        {"jaut": "Cik ir 0,4 · 0,5?",
         "atb": ["0,2", "0.2"], "padoms": "Divi cipari aiz komata."},
        {"jaut": "Kuba ar šķautni 3 cm tilpums cm³?",
         "atb": ["27"], "padoms": "3 · 3 · 3."},
        {"jaut": "x + 5 = −3. Kāds ir x?",
         "atb": ["-8", "−8"], "padoms": "−3 − 5."},
    ], pamats=4,
        ievads="Seši uzdevumi no sešiem dažādiem gada tematiem."),

    Petijums("Uzraksti vēstuli sev",
             vajag="burtnīca",
             soli=[
                 "Pieraksti trīs lietas, ko šogad iemācījies vislabāk.",
                 "Pieraksti divas, kuras vēl ir nedrošas.",
                 "Katrai nedrošajai pieraksti vienu uzdevumu, ko atkārtot.",
                 "Pieraksti vienu lietu, ko gribētu iemācīties 7. klasē.",
                 "Ieliec lapu burtnīcā un izlasi to septembrī.",
             ],
             secinajums="Vasarā aizmirstas tieši tās vietas, kas jau maijā "
                        "bija nedrošas - tāpēc tās ir vērts pierakstīt."),

    Varianti("Kas mainīsies?", [
        {"jaut": "Kas 7. klasē paliks tas pats?",
         "opcijas": ["Zīmju likums", "Skaitļu vietā burti",
                     "Vienādojumi", "Jaunas darbības"],
         "pareizi": 0,
         "padoms": "Likumi nemainās."},
        {"jaut": "Kas būs jauns?",
         "opcijas": ["Izteiksmes ar burtiem", "Daļu saskaitīšana",
                     "Procenti", "Darbību secība"],
         "pareizi": 0,
         "padoms": "Pārējais jau ir zināms."},
        {"jaut": "Vienādojums ir līdzīgs uzdevumam...",
         "opcijas": ["«kurš skaitlis trūkst»", "«cik procenti»",
                     "«cik reižu ietilpst»", "«kāds ir laukums»"],
         "pareizi": 0,
         "padoms": "Nezināmais kļūst par burtu."},
        {"jaut": "Kāpēc vērts pierakstīt nedrošās vietas?",
         "opcijas": ["Jo vasarā tās aizmirstas visvairāk",
                     "Jo skolotājs prasa",
                     "Jo tā ir ātrāk", "Nav vērts"],
         "pareizi": 0,
         "padoms": "Nedrošais pazūd pirmais."},
    ], pamats=4),

    Pasaule("Kur matemātika noderēja šogad?",
            Ievadi("", [
                {"jaut": "Veikalā: cena 60 €, atlaide 25 %. Cik eiro maksā?",
                 "atb": ["45"], "padoms": "75 % no 60."},
                {"jaut": "Virtuvē: recepte 4 porcijām, vajag 6. Cik reižu "
                         "jāpalielina? Atbildi raksti kā a/b vai decimāldaļu.",
                 "atb": ["1,5", "1.5", "3/2"], "padoms": "6 : 4."},
                {"jaut": "Kartē: mērogs 1 : 1000, attālums 7 cm. Cik metru "
                         "dabā?",
                 "atb": ["70"], "padoms": "7000 cm."},
                {"jaut": "Laika ziņas: no −6 °C uz 4 °C. Par cik grādiem?",
                 "atb": ["10"], "padoms": "6 + 4."},
            ]),
            pavediens="celojums",
            konteksts="Viss gads vienā rindā: procenti, proporcijas, mērogs "
                      "un negatīvi skaitļi - visi no ikdienas.",
            kapec="Matemātika šogad bija par to, kā izlasīt pasauli "
                  "skaitļos."),

    Kopsavilkums([
        "Apkopoju, ko esmu iemācījies 6. klasē.",
        "Zinu, kuras vietas man vēl jāatkārto.",
        "Saprotu, ka 7. klasē likumi paliks tie paši.",
        "Zinu, ka vienādojums ir «kurš skaitlis trūkst» ar burtu.",
    ]),

    Majas([
        "Pieraksti trīs lietas, ko šogad iemācījies vislabāk.",
        "Pieraksti divas, kuras atkārtosi vasarā.",
        "Atrodi vienu vietu mājās vai ceļā, kur šogad noderēja matemātika.",
    ]),
]
