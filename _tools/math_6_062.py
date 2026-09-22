# -*- coding: utf-8 -*-
"""6. klase, 62. stunda: «Kā ķermenis izskatās no dažādām pusēm?»

Skati ir tas, ko redz inženieris rasējumā: trīs plakani attēli, no kuriem
var atjaunot visu ķermeni. Stunda iet abos virzienos - no ķermeņa uz skatiem
un no skatiem atpakaļ uz ķermeni.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         restis)

TEMA = "Kā ķermenis izskatās no dažādām pusēm?"

MERKIS = ("Mācīsimies zīmēt un raksturot telpiska ķermeņa skatus dažādās "
          "plaknēs.")

SATURS = [
    Sakums("Rasējumā nav neviena telpiska attēla",
           zimejums=restis([["priekša", "sāns", "augša"]]),
           paraksts="Trīs plakani skati - un detaļu var izgatavot, to nekad "
                    "neredzot dabā.",
           fakti=["Skats ir tas, ko redz, skatoties taisni no vienas puses.",
                  "Trīs skati parasti apraksta ķermeni pilnībā.",
                  "Rūpnīcā strādā tieši pēc skatiem, ne pēc telpiska "
                  "zīmējuma."]),

    Doma("Skaties taisni, nevis pa diagonāli",
         "Skats ir ķermeņa attēls uz plaknes, kad skatās perpendikulāri no "
         "priekšas, no sāna vai no augšas.",
         soli=[
             "Novieto ķermeni tā, lai viena skaldne būtu tieši pretī.",
             "Uzzīmē tikai to, ko redzi, bez dziļuma.",
             "Pagriez ķermeni par 90 grādiem un zīmē sānu skatu.",
             "Paskaties no augšas un zīmē trešo skatu.",
             "Pārbaudi: vai skatu izmēri savstarpēji sakrīt?",
         ],
         pieze="Kvadram 4 x 3 x 2 priekšas skats ir 4 x 3, sāna skats - "
               "2 x 3, augšas skats - 4 x 2. Katrs izmērs parādās tieši "
               "divos skatos - tā tos arī pārbauda."),

    Paraugs("Trīs skati kvadram",
            uzd="Kvadrs ir 5 cm plats, 3 cm augsts un 2 cm dziļš. Kādi ir "
                "tā trīs skati?",
            soli=[
                ("Priekšas skats: taisnstūris 5 x 3",
                 "Platums un augstums."),
                ("Sāna skats: taisnstūris 2 x 3",
                 "Dziļums un augstums."),
                ("Augšas skats: taisnstūris 5 x 2",
                 "Platums un dziļums."),
                ("Katrs izmērs parādās divos skatos",
                 "Tā pārbauda, vai nekas nav sajaukts."),
            ],
            atbilde="5 x 3, 2 x 3 un 5 x 2"),

    Ievadi("Nosaki skatu izmērus", [
        {"jaut": "Kvadrs 6 x 4 x 3 (platums x augstums x dziļums). Cik plats "
                 "ir priekšas skats?",
         "atb": ["6"], "padoms": "Platums."},
        {"jaut": "Cik augsts ir priekšas skats?",
         "atb": ["4"], "padoms": "Augstums."},
        {"jaut": "Cik plats ir sāna skats?",
         "atb": ["3"], "padoms": "Dziļums."},
        {"jaut": "Cik augsts ir augšas skats?",
         "atb": ["3"], "padoms": "Augšas skatā redz platumu un dziļumu."},
        {"jaut": "Kuba ar šķautni 5 cm visi trīs skati ir vienādi. Cik cm "
                 "gara ir katra skata mala?",
         "atb": ["5"], "padoms": "Kubam visas šķautnes vienādas."},
        {"jaut": "Cik dažādu skatu izmēru ir kvadram 4 x 4 x 7?",
         "atb": ["2"], "padoms": "4 x 4 un 4 x 7."},
    ], pamats=4),

    Petijums("Uzzīmē sava priekšmeta skatus",
             vajag="kastes formas priekšmets, lineāls, rūtiņu lapa",
             soli=[
                 "Izmēri priekšmeta platumu, augstumu un dziļumu.",
                 "Uzzīmē priekšas skatu rūtiņu lapā.",
                 "Uzzīmē sāna un augšas skatu blakus.",
                 "Iedod skatus soļabiedram un palūdz nosaukt izmērus.",
             ],
             secinajums="Ja soļabiedrs no skatiem atjaunoja visus trīs "
                        "izmērus, rasējums ir pilnīgs."),

    Varianti("Ko rāda katrs skats?", [
        {"jaut": "Ko redz augšas skatā?",
         "opcijas": ["Platumu un dziļumu", "Platumu un augstumu",
                     "Dziļumu un augstumu", "Tikai augstumu"],
         "pareizi": 0,
         "padoms": "Skatoties no augšas, augstums pazūd."},
        {"jaut": "Cik skatu parasti pietiek, lai aprakstītu kvadru?",
         "opcijas": ["Trīs", "Viens", "Seši", "Divi"],
         "pareizi": 0,
         "padoms": "Priekša, sāns un augša."},
        {"jaut": "Kuba visi trīs skati ir...",
         "opcijas": ["vienādi kvadrāti", "dažādi taisnstūri",
                     "trīsstūri", "apļi"],
         "pareizi": 0,
         "padoms": "Visas šķautnes vienādas."},
        {"jaut": "Cilindra skats no augšas ir...",
         "opcijas": ["aplis", "taisnstūris", "trīsstūris", "kvadrāts"],
         "pareizi": 0,
         "padoms": "No sāna tas ir taisnstūris."},
    ], pamats=4),

    Pasaule("Kā pasūtīt mēbeli pēc rasējuma?",
            Ievadi("", [
                {"jaut": "Plaukta priekšas skats ir 80 x 200 cm. Cik cm "
                         "plats ir plaukts?",
                 "atb": ["80"], "padoms": "Pirmais skaitlis."},
                {"jaut": "Sāna skats ir 40 x 200 cm. Cik cm dziļš ir "
                         "plaukts?",
                 "atb": ["40"], "padoms": "Sāna skatā redz dziļumu."},
                {"jaut": "Cik cm augsts ir plaukts?",
                 "atb": ["200"], "padoms": "Augstums abos skatos sakrīt."},
                {"jaut": "Kādi ir augšas skata izmēri centimetros? Raksti "
                         "mazāko skaitli.",
                 "atb": ["40"], "padoms": "80 x 40."},
            ]),
            pavediens="maja",
            konteksts="Mēbeļu veikalā izmērus raksta tieši trīs skaitļos - "
                      "tas ir tas pats, kas trīs skati.",
            kapec="No trim skatiem var pateikt, vai mēbele ietilps istabā."),

    Zimejums("Divi skati vienam kvadram",
             restis([["5 x 3", "2 x 3", "5 x 2"]],
                    "priekša / sāns / augša"),
             paskaidro="Katrs izmērs parādās divos skatos: 5 - priekšā un "
                       "augšā, 3 - priekšā un sānos, 2 - sānos un augšā.",
             ievads="Tā pārbauda, vai skati ir savstarpēji saskaņoti."),

    Kopsavilkums([
        "Zīmēju telpiska ķermeņa skatus no priekšas, sāna un augšas.",
        "Zinu, kurus izmērus rāda katrs skats.",
        "Pārbaudu skatus savstarpēji: katrs izmērs parādās divos.",
        "No skatiem atjaunoju ķermeņa izmērus.",
    ]),

    Majas([
        "Uzzīmē trīs skatus savai pildspalvu kārbiņai.",
        "Atrodi mājās priekšmetu, kuram divi skati ir vienādi.",
        "Pieraksti, kāds ir cilindra skats no sāna.",
    ]),
]
