# -*- coding: utf-8 -*-
"""6. klase, 74. stunda: «Cik liels ir šis trauks?»

Novērtēšanas stunda, kurā jāizmanto arī acs, ne tikai lineāls. Trauka
tilpumu var novērtēt, salīdzinot to ar zināmu mēru - un tikai tad pārbaudīt
ar mērījumu. Atšķirība starp abiem ir pati mācība.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti)

TEMA = "Cik liels ir šis trauks?"

MERKIS = ("Novērtēsim tilpuma aptuveno vērtību un salīdzināsim to ar "
          "precīzo.")

SATURS = [
    Sakums("Acs melo mazāk, nekā domā",
           fakti=["Puslitra pudele ir apmēram 10 cm x 6 cm x 8 cm.",
                  "Novērtē, salīdzinot ar zināmu mēru - pudeli vai spaini.",
                  "Pēc novērtējuma vienmēr seko mērījums."]),

    Doma("Salīdzini ar zināmu mēru",
         "Tilpumu novērtē, salīdzinot trauku ar zināmu mēru vai noapaļojot "
         "izmērus līdz ērtiem skaitļiem.",
         soli=[
             "Izvēlies zināmu mēru: puslitru, litru vai spaini.",
             "Novērtē, cik tādu mēru ietilptu traukā.",
             "Pieraksti novērtējumu.",
             "Izmēri izmērus un aprēķini precīzo tilpumu.",
             "Salīdzini abus un pieraksti starpību.",
         ],
         pieze="Novērtējot noapaļo visus trīs izmērus: 19 x 11 x 9 cm ir "
               "apmēram 20 x 10 x 10 = 2000 cm³, tātad ap 2 litriem. Precīzi "
               "sanāk 1881 cm³ - novērtējums bija tuvu."),

    Paraugs("Novērtē un tad izmēri",
            uzd="Kaste ir 19 cm x 11 cm x 9 cm. Cik apmēram litru tajā "
                "ietilpst?",
            soli=[
                ("Noapaļo: 20 x 10 x 10",
                 "Ērti skaitļi."),
                ("20 · 10 · 10 = 2000 cm³",
                 "Novērtējums."),
                ("2000 cm³ = 2 l",
                 "Apmēram divas litra pudeles."),
                ("Precīzi: 19 · 11 · 9 = 1881 cm³",
                 "Starpība mazāka par 0,12 l."),
            ],
            atbilde="apmēram 2 l, precīzi 1,881 l"),

    Ievadi("Novērtē tilpumu", [
        {"jaut": "Kaste 19 x 11 x 9 cm. Cik apmēram cm³? Noapaļo līdz "
                 "tūkstošiem.",
         "atb": ["2000", "2 000"], "padoms": "20 · 10 · 10."},
        {"jaut": "Cik apmēram litru tas ir?",
         "atb": ["2"], "padoms": "2000 cm³."},
        {"jaut": "Kaste 29 x 21 x 10 cm. Cik apmēram cm³?",
         "atb": ["6000", "6 000"], "padoms": "30 · 20 · 10."},
        {"jaut": "Kaste 9 x 9 x 11 cm. Cik apmēram cm³?",
         "atb": ["1000", "1 000"], "padoms": "10 · 10 · 10."},
        {"jaut": "Precīzs tilpums ir 1881 cm³, novērtējums 2000 cm³. Kāda ir "
                 "starpība cm³?",
         "atb": ["119"], "padoms": "2000 − 1881."},
        {"jaut": "Kaste 51 x 19 x 21 cm. Cik apmēram litru?",
         "atb": ["20"], "padoms": "50 · 20 · 20 = 20 000 cm³."},
    ], pamats=4),

    Petijums("Novērtē un pārbaudi trīs traukus",
             vajag="trīs mājas trauki, lineāls, mērglāze",
             soli=[
                 "Katram traukam vispirms pieraksti savu minējumu litros.",
                 "Izmēri izmērus un aprēķini precīzo tilpumu.",
                 "Pārbaudi ar ūdeni un mērglāzi.",
                 "Pieraksti, kurā gadījumā minējums bija vistuvāk.",
             ],
             secinajums="Minējums parasti ir tuvāks tad, kad trauku salīdzina "
                        "ar zināmu mēru, nevis min brīvi."),

    Varianti("Cik liels tas ir?", [
        {"jaut": "Kāds ir parastas ūdens pudeles tilpums?",
         "opcijas": ["Apmēram 0,5 l", "Apmēram 5 l",
                     "Apmēram 50 l", "Apmēram 0,05 l"],
         "pareizi": 0,
         "padoms": "500 cm³."},
        {"jaut": "Kāds ir spaiņa tilpums?",
         "opcijas": ["Apmēram 10 l", "Apmēram 1 l",
                     "Apmēram 100 l", "Apmēram 0,1 l"],
         "pareizi": 0,
         "padoms": "10 dm³."},
        {"jaut": "Kāpēc novērtējot noapaļo visus trīs izmērus?",
         "opcijas": ["Lai rēķinu varētu izdarīt galvā",
                     "Lai atbilde būtu precīzāka",
                     "Tā prasa likums", "Nav iemesla"],
         "pareizi": 0,
         "padoms": "Novērtējums ir galvas rēķins."},
        {"jaut": "Ja visi trīs izmēri noapaļoti uz augšu, novērtējums būs...",
         "opcijas": ["lielāks par precīzo", "mazāks par precīzo",
                     "tieši tāds pats", "nejaušs"],
         "pareizi": 0,
         "padoms": "Visi trīs reizinātāji lielāki."},
    ], pamats=4),

    Pasaule("Vai soma ietilps bagāžā?",
            Ievadi("", [
                {"jaut": "Soma 55 x 40 x 20 cm. Cik apmēram cm³? Noapaļo "
                         "līdz desmitiem tūkstošu.",
                 "atb": ["40000", "40 000"], "padoms": "50 · 40 · 20."},
                {"jaut": "Precīzi: cik cm³ ir 55 x 40 x 20?",
                 "atb": ["44000", "44 000"], "padoms": "2200 · 20."},
                {"jaut": "Cik litru tas ir?",
                 "atb": ["44"], "padoms": "44 000 : 1000."},
                {"jaut": "Atļautais bagāžas tilpums ir 40 l. Vai soma der? "
                         "Raksti «jā» vai «nē».",
                 "atb": ["nē", "ne"], "padoms": "44 ir vairāk par 40."},
            ]),
            pavediens="celojums",
            konteksts="Lidostā bagāžas izmērus pārbauda ar rāmi - tilpums "
                      "jāzina jau mājās.",
            kapec="Novērtējums pasaka atbildi ātrāk nekā precīzs rēķins."),

    Kopsavilkums([
        "Novērtēju trauka tilpumu, salīdzinot to ar zināmu mēru.",
        "Noapaļoju izmērus un rēķinu novērtējumu galvā.",
        "Aprēķinu precīzo tilpumu un salīdzinu ar novērtējumu.",
        "Pasaku, uz kuru pusi novērtējums kļūdījās un kāpēc.",
    ]),

    Majas([
        "Novērtē trīs mājas trauku tilpumu un pieraksti minējumus.",
        "Izmēri vienu no tiem un aprēķini precīzo tilpumu.",
        "Pieraksti, cik liela bija starpība.",
    ]),
]
