# -*- coding: utf-8 -*-
"""8. klase, 76. stunda: «Kas raksturo taisnu prizmu?»

Taisnai prizmai pamati ir vienādi daudzstūri paralēlās plaknēs, sānu
skaldnes - taisnstūri. n-stūra prizmai: 2n virsotnes, 3n šķautnes,
n + 2 skaldnes. Izklājumu zīmē prizmas_izklajums (pamats 3, 4, 5).
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, Zimejums, kermenis, prizmas_izklajums)

TEMA = "Kas raksturo taisnu prizmu?"

MERKIS = ("Raksturosim taisnas prizmas pamatus un sānu skaldnes un zīmēsim "
          "tās izklājumu.")

SATURS = [
    Sakums("No kā sastāv prizma?",
           zimejums=kermenis("prizma"),
           paraksts="Trijstūra prizma: 2 pamati un 3 sānu skaldnes.",
           fakti=["Pamati ir vienādi daudzstūri paralēlās plaknēs.",
                  "Taisnai prizmai sānu skaldnes ir taisnstūri.",
                  "Sānu šķautnes garums ir prizmas augstums h."]),

    Doma("n-stūra prizma",
         "Prizmu nosauc pēc pamata: trijstūra, četrstūra, sešstūra prizma.",
         soli=[
             "n-stūra prizmai ir 2 pamati un n sānu skaldnes.",
             "Virsotņu 2n, šķautņu 3n, skaldņu n + 2.",
             "Izklājums: n taisnstūri rindā un divi pamati.",
             "Kvadrs un kubs ir četrstūra prizmas.",
         ]),

    Zimejums("Trijstūra prizmas izklājums",
             prizmas_izklajums(3, 4, 5, 6),
             paskaidro="Sānu taisnstūri 3 × 6, 4 × 6 un 5 × 6; pamati - "
                       "trijstūri ar malām 3, 4 un 5. Salokot trijstūra "
                       "malas sakrīt ar taisnstūru malām."),

    Ievadi("Saskaiti", [
        {"jaut": "Cik sānu skaldņu ir sešstūra prizmai?", "atb": ["6"],
         "padoms": "n = 6."},
        {"jaut": "Cik virsotņu ir sešstūra prizmai?", "atb": ["12"],
         "padoms": "2n."},
        {"jaut": "Cik šķautņu ir piecstūra prizmai?", "atb": ["15"],
         "padoms": "3n."},
        {"jaut": "Cik skaldņu kopā ir četrstūra prizmai?", "atb": ["6"],
         "padoms": "n + 2."},
        {"jaut": "Prizmai ir 24 šķautnes. Cik stūru ir pamatam?",
         "atb": ["8"], "padoms": "3n = 24."},
        {"jaut": "Prizmai ir 10 virsotnes. Cik tai skaldņu?", "atb": ["7"],
         "padoms": "2n = 10, n + 2."},
    ], pamats=4),

    Varianti("Spried", [
        {"jaut": "Kāda forma ir taisnas prizmas sānu skaldnēm?",
         "opcijas": ["Taisnstūri", "Trijstūri", "Vienmēr kvadrāti",
                     "Trapeces"],
         "pareizi": 0, "padoms": "Sānu šķautnes ir perpendikulāras "
                                 "pamatam."},
        {"jaut": "Kurš ķermenis NAV prizma?",
         "opcijas": ["Piramīda", "Kubs", "Kvadrs", "Trijstūra prizma"],
         "pareizi": 0, "padoms": "Piramīdai ir viens pamats."},
        {"jaut": "Trijstūra prizmas izklājumā ir...",
         "opcijas": ["3 taisnstūri un 2 trijstūri",
                     "2 taisnstūri un 3 trijstūri", "5 taisnstūri",
                     "4 trijstūri"],
         "pareizi": 0, "padoms": "Skaties zīmējumu."},
    ]),

    Pasaule("Telts",
            Ievadi("", [
                {"jaut": "Telts ir guļus trijstūra prizma. Cik taisnstūra "
                         "skaldņu tai ir (ar grīdu)?",
                 "atb": ["3"], "padoms": "Grīda un divi jumta slīpumi."},
                {"jaut": "Cik auduma gabalu vajag, ja katra skaldne ir savs "
                         "gabals?",
                 "atb": ["5"], "padoms": "3 taisnstūri + 2 gali."},
                {"jaut": "Karkasa stieņi iet pa visām šķautnēm. Cik stieņu?",
                 "atb": ["9"], "padoms": "3n, n = 3."},
            ]),
            pavediens="celojums",
            konteksts="Klasiska telts: grīda un jumta slīpumi ir taisnstūri, "
                      "abi gali - trijstūri.",
            kapec="Izklājums rāda, kādi gabali jāizgriež šuvējam."),

    Kopsavilkums([
        "Raksturoju taisnas prizmas pamatus un sānu skaldnes.",
        "Saskaitu n-stūra prizmas virsotnes, šķautnes un skaldnes.",
        "Zīmēju trijstūra prizmas izklājumu.",
    ]),

    Majas([
        "No kartona izgriez izklājumu (3, 4, 5 un 6 cm) un saloki prizmu.",
        "Atrodi mājās trīs priekšmetus prizmas formā.",
        "Uzzīmē sešstūra prizmas izklājumu.",
    ]),
]
