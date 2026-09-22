# -*- coding: utf-8 -*-
"""5. klase, 1. stunda: «Cik tālu sniedzas skaitļi?»

Gada pirmā stunda. Skaitļus līdz miljonam skolēns jau ir redzējis, tāpēc te
nostiprina to, kas lielos skaitļos ir svarīgākais: cipara vērtību nosaka tā
vieta, un pieraksts dalās šķirās pa trim cipariem. Uz šī balstās gan
noapaļošana (14. stunda), gan viss darbs ar lielām vērtībām.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, kolonnas)

TEMA = "Cik tālu sniedzas skaitļi?"

MERKIS = ("Iemācīsimies izlasīt un pierakstīt skaitļus līdz miljardam un "
          "pateikt, ko nozīmē katrs cipars.")

SATURS = [
    Sakums("Cik liela ir starpība starp miljonu un miljardu?",
           zimejums=kolonnas([("miljons", 1000000),
                              ("miljards", 1000000000)]),
           paraksts="Miljona stabiņš ir tik zems, ka to gandrīz neredz.",
           fakti=["Miljons sekunžu ir apmēram 12 dienas.",
                  "Miljards sekunžu ir vairāk nekā 31 gads."]),

    Doma("Cipara vērtību nosaka tā vieta",
         "Viens un tas pats cipars nozīmē dažādas lietas - svarīgi, kurā "
         "vietā tas stāv.",
         soli=[
             "Skaitli sadala pa trim cipariem no labās puses: 1 850 000.",
             "Katru trijnieku sauc par šķiru: vieni, tūkstoši, miljoni, "
             "miljardi.",
             "Šķirā cipari pēc kārtas ir simti, desmiti un vieni.",
             "Lasa pa šķirām: vispirms trijnieks, tad šķiras nosaukums.",
         ],
         pieze="Skaitlī 3 337 ir trīs trijnieki, un katrs nozīmē ko citu: "
               "3 tūkstoši, 3 simti un 3 desmiti. Vietas dēļ pirmais "
               "trijnieks ir tūkstoš reižu lielāks par pēdējo."),

    Paraugs("Kā izlasa 1 907 675?",
            uzd="Izlasi skaitli 1 907 675 un pasaki, ko nozīmē cipars 9.",
            soli=[
                ("1 907 675 → 1 | 907 | 675",
                 "Sadala pa trim cipariem no labās puses. Sanāk trīs šķiras: "
                 "miljoni, tūkstoši un vieni."),
                ("1 miljons 907 tūkstoši 675",
                 "Katru trijnieku nolasa un pasaka tā šķiras nosaukumu. "
                 "Pēdējai šķirai nosaukumu nesaka."),
                ("9 stāv simtu tūkstošu vietā → 900 000",
                 "Cipars 9 ir tūkstošu šķirā simtu vietā, tāpēc tas nozīmē "
                 "deviņus simtus tūkstošu."),
            ],
            atbilde="viens miljons deviņi simti septiņi tūkstoši seši simti "
                    "septiņdesmit pieci; cipars 9 nozīmē 900 000"),

    Ievadi("Ko nozīmē izceltais cipars?", [
        {"jaut": "Skaitlī 45 *6*21 - ko nozīmē cipars 6?",
         "atb": ["600"], "padoms": "Skaiti vietas no labās: vieni, desmiti, "
                                   "simti."},
        {"jaut": "Skaitlī *7* 000 000 - ko nozīmē cipars 7?",
         "atb": ["7000000", "7 000 000"],
         "padoms": "Tas stāv miljonu šķirā vienu vietā."},
        {"jaut": "Skaitlī 3 *4*08 912 - ko nozīmē cipars 4?",
         "atb": ["400000", "400 000"],
         "padoms": "Šķira ir tūkstoši, vieta - simti."},
        {"jaut": "Skaitlī 62 *9*50 - ko nozīmē cipars 9?",
         "atb": ["900"], "padoms": "Vieta ir simti."},
        {"jaut": "Skaitlī 1 *2*34 567 890 - ko nozīmē cipars 2?",
         "atb": ["200000000", "200 000 000"],
         "padoms": "Šķira ir miljoni, vieta - simti."},
        {"jaut": "Skaitlī 80 *5*06 - ko nozīmē cipars 5?",
         "atb": ["500"], "padoms": "Nulles vietu neaizņem velti - tā tur ir, "
                                   "lai pārējie cipari paliktu savās vietās."},
    ], pamats=4,
        ievads="Ieraksti, cik liela vērtība ir izceltajam ciparam."),

    Varianti("Kā šo skaitli izlasa?", [
        {"jaut": "204 060",
         "opcijas": ["divi simti četri tūkstoši sešdesmit",
                     "divdesmit četri tūkstoši sešdesmit",
                     "divi simti četrdesmit tūkstoši seši",
                     "divi miljoni četri tūkstoši sešdesmit"],
         "pareizi": 0,
         "padoms": "Sadali pa trim cipariem: 204 | 060."},
        {"jaut": "Kurš skaitlis ir lielākais?",
         "opcijas": ["999 999", "1 000 001", "1 000 000", "998 888"],
         "pareizi": 1,
         "padoms": "Vispirms salīdzini, cik ciparu ir katrā skaitlī."},
        {"jaut": "Kā pieraksta «trīs miljoni divdesmit tūkstoši piecpadsmit»?",
         "opcijas": ["3 020 015", "3 200 015", "3 020 150", "3 000 215"],
         "pareizi": 0,
         "padoms": "Katrai šķirai jābūt tieši trīs cipariem: 3 | 020 | 015."},
        {"jaut": "Cik ciparu ir mazākajam miljardam?",
         "opcijas": ["10", "9", "7", "12"],
         "pareizi": 0,
         "padoms": "1 000 000 000 - saskaiti ciparus."},
    ], pamats=4,
        ievads="Izvēlies pareizo atbildi."),

    Pasaule("Cik tālu ir Saule?",
            Ievadi("", [
                {"jaut": "Cik miljonu kilometru ir 150 000 000 km?",
                 "atb": ["150"], "padoms": "Miljonu šķira ir pirmie cipari."},
                {"jaut": "Uzraksti ar cipariem: divi simti tūkstoši",
                 "atb": ["200000", "200 000"],
                 "padoms": "Divi simti tūkstošu - tad trīs nulles."},
                {"jaut": "Skaitlī 384 000 - ko nozīmē cipars 8?",
                 "atb": ["80000", "80 000"],
                 "padoms": "Tas stāv tūkstošu šķirā desmitu vietā."},
                {"jaut": "Cik ciparu ir skaitlī 150 000 000?",
                 "atb": ["9"], "padoms": "Saskaiti arī nulles."},
            ]),
            pavediens="kosmoss",
            konteksts="Līdz Saulei ir apmēram 150 000 000 km, līdz Mēnesim - "
                      "384 000 km.",
            kapec="Kosmosā attālumus raksta miljonos, jo citādi cipari "
                  "rindā nesatilpst."),

    Kopsavilkums([
        "Lasu un pierakstu skaitļus līdz miljardam.",
        "Zinu šķiras: vieni, tūkstoši, miljoni, miljardi - katrā pa trim "
        "cipariem.",
        "Pasaku, ko nozīmē katrs cipars pēc tā vietas skaitlī.",
    ]),

    Majas([
        "Atrodi ziņās vienu skaitli, kas lielāks par miljonu, un izlasi to "
        "skaļi.",
        "Uzraksti savu dzimšanas gadu kā šķiru virkni un pasaki, ko nozīmē "
        "katrs cipars.",
        "Padomā: cik sekunžu ir vienā diennaktī? Vai iznāk vairāk vai mazāk "
        "par 100 000?",
    ], ievads="Lielus skaitļus visvieglāk iemācīties tur, kur tie tiešām ir."),
]
