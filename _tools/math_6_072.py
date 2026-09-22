# -*- coding: utf-8 -*-
"""6. klase, 72. stunda: «Cik kubikcentimetru ir kubikdecimetrā?»

Praktiska stunda ar taustāmu rezultātu. Kubs ar malu 1 dm ir tik liels, ka
to var paņemt rokās - un tikai tad skaitlis 1000 pārstāj būt abstrakts.
Pārveidošanas likums izaug no modeļa, ne otrādi.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         restis)

TEMA = "Cik kubikcentimetru ir kubikdecimetrā?"

MERKIS = ("Praktiski izveidosim 1 dm³ modeli un noteiksim sakarību starp "
          "tilpuma mērvienībām.")

SATURS = [
    Sakums("Tūkstotis mazu kubiņu vienā",
           zimejums=restis([["1 dm³", "1000 cm³"],
                            ["1 m³", "1000 dm³"]]),
           paraksts="Katrs solis uz mazāku tilpuma vienību ir reizināšana "
                    "ar 1000.",
           fakti=["1 dm = 10 cm, tāpēc 1 dm³ = 10 · 10 · 10 = 1000 cm³.",
                  "Garumam reizinātājs ir 10, laukumam 100, tilpumam 1000.",
                  "Reizinātājs vienmēr ir garuma reizinātājs pakāpē."]),

    Doma("Reizinātājs kļūst trešajā pakāpē",
         "Pārejot uz mazāku tilpuma mērvienību, reizina ar garuma "
         "reizinātāju trešajā pakāpē: 10 kļūst par 1000.",
         soli=[
             "Pieraksti, cik reižu atšķiras garuma vienības.",
             "Kāpini šo skaitli trešajā pakāpē.",
             "Ja pāriet uz mazāku vienību - reizini.",
             "Ja uz lielāku - dali.",
             "Pārbaudi ar modeli: cik mazo kubu ietilpst lielajā?",
         ],
         pieze="1 m = 100 cm, tāpēc 1 m³ = 100 · 100 · 100 = 1 000 000 cm³. "
               "Sešas nulles nav pārrakstīšanās - tas ir reizinātājs "
               "trešajā pakāpē."),

    Paraugs("Cik kubikcentimetru ir 2,5 dm³?",
            uzd="Pārveido 2,5 dm³ kubikcentimetros.",
            soli=[
                ("1 dm = 10 cm",
                 "Garuma reizinātājs."),
                ("1 dm³ = 10 · 10 · 10 = 1000 cm³",
                 "Tilpuma reizinātājs ir trešajā pakāpē."),
                ("2,5 · 1000 = 2500 cm³",
                 "Reizina ar reizinātāju."),
                ("Pārbaude: 2500 : 1000 = 2,5",
                 "Atpakaļceļš dod sākotnējo."),
            ],
            atbilde="2500 cm³"),

    Petijums("Uzbūvē 1 dm³ modeli",
             vajag="kartons, lineāls, šķēres, līmlente",
             soli=[
                 "Uzzīmē izklājumu kubam ar šķautni 10 cm.",
                 "Izgriez un salīmē kubu.",
                 "Aprēķini, cik 1 cm³ kubiņu tajā ietilptu.",
                 "Ielej tajā ūdeni un pārbaudi, cik litru tas ir.",
             ],
             secinajums="Kubā ietilpst 1000 kubikcentimetru un tieši viens "
                        "litrs ūdens - tā ir viena un tā pati sakarība."),

    Ievadi("Pārveido tilpuma vienības", [
        {"jaut": "Cik cm³ ir 1 dm³?",
         "atb": ["1000", "1 000"], "padoms": "10 · 10 · 10."},
        {"jaut": "Cik dm³ ir 1 m³?",
         "atb": ["1000", "1 000"], "padoms": "10 · 10 · 10."},
        {"jaut": "Cik cm³ ir 3 dm³?",
         "atb": ["3000", "3 000"], "padoms": "3 · 1000."},
        {"jaut": "Cik dm³ ir 5000 cm³?",
         "atb": ["5"], "padoms": "5000 : 1000."},
        {"jaut": "Cik cm³ ir 1 m³?",
         "atb": ["1000000", "1 000 000"], "padoms": "100 · 100 · 100."},
        {"jaut": "Cik dm³ ir 0,25 m³?",
         "atb": ["250"], "padoms": "0,25 · 1000."},
    ], pamats=4),

    Varianti("Ar ko reizina?", [
        {"jaut": "Pārejot no dm³ uz cm³, reizina ar...",
         "opcijas": ["1000", "100", "10", "10 000"],
         "pareizi": 0,
         "padoms": "10 trešajā pakāpē."},
        {"jaut": "Pārejot no m³ uz dm³, reizina ar...",
         "opcijas": ["1000", "100", "10", "1 000 000"],
         "pareizi": 0,
         "padoms": "1 m = 10 dm."},
        {"jaut": "Kāpēc tilpuma reizinātājs ir lielāks nekā laukuma?",
         "opcijas": ["Jo tilpumam ir trīs izmēri",
                     "Jo tilpums ir liels",
                     "Jo tā ir pieņemts", "Tas nav lielāks"],
         "pareizi": 0,
         "padoms": "Reizina trīs izmērus."},
        {"jaut": "Kubam ar šķautni 10 cm tilpums ir...",
         "opcijas": ["1000 cm³", "100 cm³", "30 cm³", "10 000 cm³"],
         "pareizi": 0,
         "padoms": "10 · 10 · 10."},
    ], pamats=4),

    Pasaule("Cik ūdens ietilpst akvārijā?",
            Ievadi("", [
                {"jaut": "Akvārijs 40 x 20 x 25 cm. Cik cm³ ir tilpums?",
                 "atb": ["20000", "20 000"], "padoms": "800 · 25."},
                {"jaut": "Cik dm³ tas ir?",
                 "atb": ["20"], "padoms": "20 000 : 1000."},
                {"jaut": "Mazāks akvārijs 30 x 20 x 20 cm. Cik cm³ ir "
                         "tilpums?",
                 "atb": ["12000", "12 000"], "padoms": "600 · 20."},
                {"jaut": "Cik dm³ tas ir?",
                 "atb": ["12"], "padoms": "12 000 : 1000."},
            ]),
            pavediens="daba",
            konteksts="Akvārija izmērus raksta centimetros, bet ūdeni "
                      "pērk litros - starp tiem ir tūkstotis.",
            kapec="Viena nulle par maz nozīmē desmitkārtīgu kļūdu."),

    Zimejums("Tilpuma kāpnes",
             restis([["1 m³", "1 dm³", "1 cm³"],
                     ["1000 dm³", "1000 cm³", "1000 mm³"]]),
             paskaidro="Katrs pakāpiens uz leju ir reizināšana ar 1000, "
                       "nevis ar 10 vai 100.",
             ievads="Tilpuma kāpnēs solis ir vislielākais."),

    Kopsavilkums([
        "Praktiski izveidoju 1 dm³ modeli.",
        "Zinu, ka 1 dm³ = 1000 cm³ un 1 m³ = 1000 dm³.",
        "Pārveidoju tilpuma mērvienības abos virzienos.",
        "Pamatoju reizinātāju ar trim izmēriem.",
    ]),

    Majas([
        "Atrodi mājās trauku, kura tilpums ir apmēram 1 dm³.",
        "Pārveido 0,5 m³ kubikdecimetros un kubikcentimetros.",
        "Pieraksti, cik cm³ ir tavai pildspalvu kārbiņai.",
    ]),
]
