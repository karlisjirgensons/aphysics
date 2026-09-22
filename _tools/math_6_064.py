# -*- coding: utf-8 -*-
"""6. klase, 64. stunda: «Kas kopīgs piramīdai un konusam?»

Mikrotemata noslēgums. Četri ķermeņi tiek salikti vienā tabulā, un izrādās,
ka tie veido divus pārus: viens ar plakanām skaldnēm, otrs ar apaļu pamatu,
bet abos pāros ir «stabs» un «smaile».
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, kermenis,
                         restis)

TEMA = "Kas kopīgs piramīdai un konusam?"

MERKIS = ("Salīdzināsim daudzskaldni, piramīdu, cilindru un konusu pēc to "
          "elementiem.")

SATURS = [
    Sakums("Divi pāri, nevis četri svešinieki",
           zimejums=kermenis("piramida"),
           paraksts="Piramīdai visas sānu skaldnes satiekas vienā virsotnē - "
                    "tieši tāpat kā konusam.",
           fakti=["Prizma un cilindrs ir «stabi»: divi vienādi pamati.",
                  "Piramīda un konuss ir «smailes»: viens pamats un "
                  "virsotne.",
                  "Atšķiras tikai tas, vai pamats ir daudzstūris vai aplis."]),

    Doma("Stabs vai smaile, plakans vai apaļš",
         "Telpiskos ķermeņus šķiro pēc divām pazīmēm: vai tiem ir divi "
         "vienādi pamati vai viena virsotne, un vai pamats ir daudzstūris "
         "vai aplis.",
         soli=[
             "Paskaties, cik pamatu ir ķermenim.",
             "Ja divi vienādi - tas ir stabs: prizma vai cilindrs.",
             "Ja viens pamats un virsotne - tā ir smaile: piramīda vai "
             "konuss.",
             "Paskaties uz pamatu: daudzstūris vai aplis.",
             "Nosauc ķermeni un pieraksti tā elementus.",
         ],
         pieze="Cilindram un konusam nav ne šķautņu, ne virsotņu parastajā "
               "nozīmē - tiem ir līknes virsmas. Tāpēc tos nesauc par "
               "daudzskaldņiem."),

    Zimejums("Četri ķermeņi vienā tabulā",
             restis([["", "daudzstūris", "aplis"],
                     ["stabs", "prizma", "cilindrs"],
                     ["smaile", "piramīda", "konuss"]]),
             paskaidro="Rinda pasaka formu, kolonna - pamatu. Katram "
                       "ķermenim ir sava vieta.",
             ievads="Divas pazīmes sadala visus četrus ķermeņus."),

    Paraugs("Salīdzini piramīdu un konusu",
            uzd="Kas piramīdai un konusam ir kopīgs un kas - atšķirīgs?",
            soli=[
                ("Abiem ir viens pamats",
                 "Tāpēc abi ir «smailes»."),
                ("Abiem ir viena virsotne",
                 "Visas sānu virsmas tajā satiekas."),
                ("Piramīdas pamats ir daudzstūris, konusa - aplis",
                 "Tā ir galvenā atšķirība."),
                ("Piramīdai ir šķautnes, konusam - nav",
                 "Konusa sānu virsma ir līkne."),
            ],
            atbilde="kopīgs - viens pamats un virsotne; atšķirīgs - pamata "
                    "forma"),

    Ievadi("Nosaki ķermeni un tā elementus", [
        {"jaut": "Cik pamatu ir cilindram?",
         "atb": ["2"], "padoms": "Apakšā un augšā.",
         "zim": kermenis("cilindrs")},
        {"jaut": "Cik virsotņu ir konusam?",
         "atb": ["1"], "padoms": "Viena smaile.",
         "zim": kermenis("konuss")},
        {"jaut": "Cik skaldņu ir trīsstūra piramīdai?",
         "atb": ["4"], "padoms": "Pamats un trīs sānu skaldnes."},
        {"jaut": "Cik skaldņu ir trīsstūra prizmai?",
         "atb": ["5"], "padoms": "Divi pamati un trīs sāni.",
         "zim": kermenis("prizma")},
        {"jaut": "Cik šķautņu ir cilindram?",
         "atb": ["0"], "padoms": "Tam nav plakanu skaldņu robežu."},
        {"jaut": "Cik virsotņu ir piecstūra piramīdai?",
         "atb": ["6"], "padoms": "5 pamatā un 1 augšā."},
    ], pamats=4),

    Varianti("Kurš ķermenis tas ir?", [
        {"jaut": "Divi vienādi apļveida pamati - kurš ķermenis?",
         "opcijas": ["Cilindrs", "Konuss", "Prizma", "Piramīda"],
         "pareizi": 0,
         "padoms": "Stabs ar apaļu pamatu."},
        {"jaut": "Viens daudzstūra pamats un virsotne - kurš ķermenis?",
         "opcijas": ["Piramīda", "Konuss", "Prizma", "Cilindrs"],
         "pareizi": 0,
         "padoms": "Smaile ar plakanu pamatu."},
        {"jaut": "Kurš ķermenis nav daudzskaldnis?",
         "opcijas": ["Konuss", "Kubs", "Prizma", "Piramīda"],
         "pareizi": 0,
         "padoms": "Tam ir līknes virsma."},
        {"jaut": "Kas kopīgs prizmai un cilindram?",
         "opcijas": ["Divi vienādi pamati", "Viena virsotne",
                     "Trīsstūra skaldnes", "Nekas"],
         "pareizi": 0,
         "padoms": "Abi ir «stabi»."},
    ], pamats=4),

    Pasaule("Kāda forma der kādam mērķim?",
            Ievadi("", [
                {"jaut": "Cik pamatu ir dzēriena bundžai?",
                 "atb": ["2"], "padoms": "Tā ir cilindrs."},
                {"jaut": "Cik skaldņu ir saldējuma tūtai, ja to uzskata par "
                         "konusu?",
                 "atb": ["1"], "padoms": "Tikai pamats ir plakans."},
                {"jaut": "Cik skaldņu ir jumta formas piramīdai ar kvadrāta "
                         "pamatu?",
                 "atb": ["5"], "padoms": "Pamats un četri sāni."},
                {"jaut": "Cik virsotņu ir kartona kastei?",
                 "atb": ["8"], "padoms": "Tas ir kvadrs."},
            ]),
            pavediens="maja",
            konteksts="Iepakojuma formu izvēlas pēc satura: šķidrumam der "
                      "cilindrs, salokāmām lietām - kvadrs.",
            kapec="Ķermeņa elementi nosaka, kā to var izgatavot un salikt."),

    Kopsavilkums([
        "Salīdzinu prizmu, piramīdu, cilindru un konusu.",
        "Šķiroju tos pēc pamatu skaita un pamata formas.",
        "Zinu, kuri ķermeņi ir daudzskaldņi un kuri nav.",
        "Nosaucu katra ķermeņa elementus.",
    ]),

    Majas([
        "Atrodi mājās vienu ķermeni no katras tabulas rūtiņas.",
        "Uzzīmē konusu un piramīdu blakus un apzīmē to kopīgo daļu.",
        "Pieraksti, kāpēc bumba neietilpst šajā tabulā.",
    ]),
]
