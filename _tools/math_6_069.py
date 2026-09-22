# -*- coding: utf-8 -*-
"""6. klase, 69. stunda: «Kā pārveidot laukuma mērvienības?»

Mikrotemata noslēgums. Laukuma mērvienības pārveido citādi nekā garuma, un
tieši tur rodas kļūda: 1 m nav 100 cm² ziņā. Kvadrāta zīmējums to izskaidro
ātrāk nekā jebkurš likums.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, kvadrats,
                         restis)

TEMA = "Kā pārveidot laukuma mērvienības?"

MERKIS = ("Iemācīsimies izteikt lielākas laukuma mērvienības mazākās un "
          "otrādi.")

SATURS = [
    Sakums("Kāpēc 1 m² nav 100 cm²?",
           zimejums=kvadrats(10, 10, 10, 10, paraksts="100 rūtiņas"),
           paraksts="Ja malu sadala 10 daļās, rūtiņu sanāk 10 · 10 = 100. "
                    "Tāpēc 1 dm² = 100 cm².",
           fakti=["Garuma vienības aug 10 reižu, laukuma - 100 reižu.",
                  "1 m² = 10 000 cm², jo 100 · 100.",
                  "Reizinātājs vienmēr ir garuma reizinātājs kvadrātā."]),

    Doma("Reizinātājs kļūst kvadrātā",
         "Pārejot uz mazāku laukuma mērvienību, reizina ar garuma "
         "reizinātāju kvadrātā: 10 kļūst par 100, bet 100 - par 10 000.",
         soli=[
             "Pieraksti, cik reižu atšķiras garuma vienības.",
             "Kāpini šo skaitli kvadrātā.",
             "Ja pāriet uz mazāku vienību - reizini ar to.",
             "Ja uz lielāku - dali.",
             "Pārbaudi ar zīmējumu: cik mazu kvadrātu ietilpst lielajā?",
         ],
         pieze="1 m = 100 cm, tāpēc 1 m² = 100 · 100 = 10 000 cm². Tā pati "
               "kārtība: 1 km² = 1 000 000 m², jo 1000 · 1000."),

    Zimejums("Mērvienību kāpnes",
             restis([["1 m²", "1 dm²", "1 cm²"],
                     ["100 dm²", "100 cm²", "100 mm²"]]),
             paskaidro="Katrs solis uz mazāku vienību ir reizināšana ar 100, "
                       "nevis ar 10.",
             ievads="Laukuma kāpnēs katrs pakāpiens ir simtreiz."),

    Paraugs("Pārveido laukuma vienības",
            uzd="Cik kvadrātcentimetru ir 2,5 m²?",
            soli=[
                ("1 m = 100 cm",
                 "Garuma reizinātājs."),
                ("1 m² = 100 · 100 = 10 000 cm²",
                 "Laukuma reizinātājs ir kvadrātā."),
                ("2,5 · 10 000 = 25 000 cm²",
                 "Reizina ar reizinātāju."),
                ("Pārbaude: 25 000 : 10 000 = 2,5",
                 "Atpakaļceļš dod sākotnējo."),
            ],
            atbilde="25 000 cm²"),

    Ievadi("Pārveido mērvienības", [
        {"jaut": "Cik cm² ir 1 dm²?",
         "atb": ["100"], "padoms": "10 · 10."},
        {"jaut": "Cik cm² ir 1 m²?",
         "atb": ["10000", "10 000"], "padoms": "100 · 100."},
        {"jaut": "Cik dm² ir 1 m²?",
         "atb": ["100"], "padoms": "10 · 10."},
        {"jaut": "Cik cm² ir 3 dm²?",
         "atb": ["300"], "padoms": "3 · 100."},
        {"jaut": "Cik m² ir 50 000 cm²?",
         "atb": ["5"], "padoms": "50 000 : 10 000."},
        {"jaut": "Cik mm² ir 2 cm²?",
         "atb": ["200"], "padoms": "10 · 10 = 100; 2 · 100."},
    ], pamats=4),

    Varianti("Ar ko reizina?", [
        {"jaut": "Pārejot no m² uz cm², reizina ar...",
         "opcijas": ["10 000", "100", "1000", "10"],
         "pareizi": 0,
         "padoms": "100 · 100."},
        {"jaut": "Pārejot no cm² uz mm², reizina ar...",
         "opcijas": ["100", "10", "1000", "10 000"],
         "pareizi": 0,
         "padoms": "10 · 10."},
        {"jaut": "Kāpēc laukuma reizinātājs ir lielāks nekā garuma?",
         "opcijas": ["Jo laukumam ir divi izmēri",
                     "Jo laukums ir lielāks",
                     "Jo tā ir pieņemts", "Tas nav lielāks"],
         "pareizi": 0,
         "padoms": "Reizina gan garumu, gan platumu."},
        {"jaut": "Cik m² ir 1 km²?",
         "opcijas": ["1 000 000", "1000", "10 000", "100"],
         "pareizi": 0,
         "padoms": "1000 · 1000."},
    ], pamats=4),

    Pasaule("Cik materiāla vajag grīdai?",
            Ievadi("", [
                {"jaut": "Istaba ir 4 m x 3 m. Cik m² ir grīda?",
                 "atb": ["12"], "padoms": "4 · 3."},
                {"jaut": "Cik cm² tas ir?",
                 "atb": ["120000", "120 000"], "padoms": "12 · 10 000."},
                {"jaut": "Viena flīze ir 30 cm x 30 cm. Cik cm² ir viena "
                         "flīze?",
                 "atb": ["900"], "padoms": "30 · 30."},
                {"jaut": "Cik flīžu vajag visai grīdai?",
                 "atb": ["134", "133"], "padoms": "120 000 : 900 ir mazliet "
                                                  "vairāk par 133."},
            ]),
            pavediens="maja",
            konteksts="Grīdu mēra kvadrātmetros, bet flīzes - "
                      "centimetros; bez pārveidošanas rēķins neiznāk.",
            kapec="Viena aizmirsta nulle nozīmē simtkārtīgu kļūdu."),

    Kopsavilkums([
        "Pārveidoju laukuma mērvienības abos virzienos.",
        "Zinu, ka laukuma reizinātājs ir garuma reizinātājs kvadrātā.",
        "Pamatoju likumu ar kvadrāta zīmējumu.",
        "Lietoju to praktiskos aprēķinos.",
    ]),

    Majas([
        "Izsaki savas istabas grīdas laukumu gan m², gan cm².",
        "Pieraksti, cik cm² ir 0,5 m².",
        "Paskaidro kādam mājās, kāpēc 1 m² nav 100 cm².",
    ]),
]
