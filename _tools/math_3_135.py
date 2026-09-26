# -*- coding: utf-8 -*-
"""3. klase, 135. stunda: «Kā saskaitīt simtus?»

Saskaitīšana 1000 apjomā sākas ar vieglāko: pilni simti un desmiti. Tur
rēķins ir tas pats, kas ar vieniem - 3 + 4 = 7, tāpēc 300 + 400 = 700. Šī
analoģija ir visas mutvārdu saskaitīšanas pamats.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, Zimejums,
                         restis)

TEMA = "Kā saskaitīt simtus?"

MERKIS = ("Saskaitīsim pilnus simtus un desmitus, saskatot analoģiju ar "
          "vieniem.")

SATURS = [
    Sakums("Ja 3 + 4 = 7, tad cik ir 300 + 400?",
           zimejums=restis([[3, "+", 4, "=", 7],
                            [30, "+", 40, "=", 70],
                            [300, "+", 400, "=", 700]],
                           "viens rēķins, trīs vietas"),
           paraksts="Cipari tie paši - atšķiras tikai vienības nosaukums.",
           fakti=["Simtus saskaita tāpat kā vienus.",
                  "3 simti plus 4 simti ir 7 simti."]),

    Doma("Saskaiti vienādas vienības",
         "300 + 400 ir 3 simti plus 4 simti - un tas ir tas pats, kas 3 + 4, "
         "tikai simtos.",
         soli=[
             "Nosauc, cik vienību ir katrā skaitlī: 3 simti un 4 simti.",
             "Saskaiti tās kā parastus skaitļus.",
             "Pieraksti rezultātu tajā pašā vienībā.",
             "Pārbaudi: vai nulles ir tikpat, cik sākumā?",
         ],
         pieze="Saskaitīt var tikai vienādas vienības: 300 + 40 nav 7 "
               "nekā - tur ir 3 simti un 4 desmiti, tātad 340."),

    Slidnis("Viens rēķins, trīs līmeņi",
            soli=[
                {"v": "3 + 4 = 7", "teksts": "Vieni.", "josla": 20},
                {"v": "30 + 40 = 70", "teksts": "Desmiti.", "josla": 50},
                {"v": "300 + 400 = 700", "teksts": "Simti.", "josla": 100},
            ],
            ievads="Cipari tie paši, vienības dažādas."),

    Paraugs("Cik ir 500 + 300?",
            uzd="Izrēķini 500 + 300.",
            soli=[
                ("5 simti + 3 simti",
                 "Nosauc vienības."),
                ("5 + 3 = 8",
                 "Saskaita kā vienus."),
                ("8 simti = 800",
                 "Pieraksta rezultātu simtos."),
            ],
            atbilde="800"),

    Ievadi("Saskaiti simtus un desmitus", [
        {"jaut": "300 + 400 = ?", "atb": ["700"], "padoms": "3 + 4 simti."},
        {"jaut": "500 + 300 = ?", "atb": ["800"], "padoms": "5 + 3 simti."},
        {"jaut": "60 + 70 = ?", "atb": ["130"], "padoms": "6 + 7 desmiti."},
        {"jaut": "800 − 500 = ?", "atb": ["300"], "padoms": "8 − 5 simti."},
        {"jaut": "400 + 250 = ?", "atb": ["650"],
         "padoms": "400 + 200 un vēl 50."},
        {"jaut": "600 + 90 = ?", "atb": ["690"],
         "padoms": "Simti un desmiti atsevišķi."},
    ], pamats=4),

    Zimejums("Kad simtu sanāk vairāk par desmit",
             restis([[600, "+", 700, "=", 1300]],
                    "6 + 7 = 13 simti"),
             paskaidro="Trīspadsmit simti ir viens tūkstotis un trīs simti.",
             ievads="Arī te rēķins ir tas pats."),

    Varianti("Cik sanāk?", [
        {"jaut": "Cik ir 200 + 600?",
         "opcijas": ["800", "8", "80", "260"],
         "pareizi": 0, "padoms": "2 + 6 simti."},
        {"jaut": "Cik ir 90 + 80?",
         "opcijas": ["170", "17", "1700", "98"],
         "pareizi": 0, "padoms": "9 + 8 desmiti."},
        {"jaut": "Cik ir 700 + 500?",
         "opcijas": ["1200", "120", "12", "750"],
         "pareizi": 0, "padoms": "12 simti."},
        {"jaut": "Cik ir 300 + 40?",
         "opcijas": ["340", "700", "70", "304"],
         "pareizi": 0, "padoms": "Dažādas vienības - tās nesaskaita kopā."},
    ], pamats=4),

    Pasaule("Cik kilometru ir ceļā?",
            Ievadi("", [
                {"jaut": "Pirmajā dienā 300 km, otrajā 400 km. Cik kopā?",
                 "atb": ["700"], "padoms": "3 + 4 simti."},
                {"jaut": "Trešajā dienā 250 km. Cik kopā trīs dienās?",
                 "atb": ["950"], "padoms": "700 + 250."},
                {"jaut": "Viss ceļš ir 1200 km. Cik atlicis?",
                 "atb": ["250"], "padoms": "1200 − 950."},
                {"jaut": "Cik kilometru vidēji nobrauca dienā?",
                 "atb": ["400"], "padoms": "1200 : 3."},
            ]),
            pavediens="celojums",
            konteksts="Ceļojumā dienas attālumi parasti ir apaļi simti - "
                      "tāpēc tos var saskaitīt galvā.",
            kapec="Apaļi skaitļi ļauj plānot, neapstājoties pie kalkulatora."),

    Kopsavilkums([
        "Saskaitu pilnus simtus un desmitus.",
        "Saskatu analoģiju ar vienu saskaitīšanu.",
        "Zinu, ka saskaitīt var tikai vienādas vienības.",
        "Rēķinu arī tad, kad simtu sanāk vairāk par desmit.",
    ]),

    Majas([
        "Izrēķini 400 + 500, 70 + 60 un 800 + 300.",
        "Atrodi trīs apaļus simtus mājas dokumentos vai ziņās.",
        "Saskaiti divus no tiem galvā.",
    ]),
]
