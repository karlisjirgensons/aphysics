# -*- coding: utf-8 -*-
"""4. klase, 134. stunda: «Cik nobrauca trešajā dienā?»

Salikts uzdevums: pirmajā dienā {1|4} ceļa, otrajā {2|4}, cik trešajā?
Divi ceļi - vispirms saskaitīt daļas ({3|4}, atlika {1|4}) vai vispirms
pārvērst kilometros. Uzdevums apvieno 4.5. un 4.6. tematu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, dala)

TEMA = "Cik nobrauca trešajā dienā?"

MERKIS = ("Risināsim uzdevumu, kurā apvienota daļas vērtības aprēķināšana "
          "un daļu saskaitīšana.")

SATURS = [
    Sakums("Velobrauciens 120 km trijās dienās",
           zimejums=dala(8, 5, "1. diena 2/8, 2. diena 3/8, 3. diena ?"),
           paraksts="Pirmās divas dienas kopā - {5|8} ceļa.",
           fakti=["Trešajā dienā atlika {3|8} ceļa.",
                  "{3|8} no 120 km = 45 km."]),

    Doma("Saskaiti daļas, tad rēķini vērtību",
         "Saliktā uzdevumā vispirms saskaita vai atņem daļas, tad aprēķina "
         "prasītās daļas vērtību no veselā.",
         soli=[
             "Saskaiti zināmās daļas: {2|8} + {3|8} = {5|8}.",
             "Atrodi atlikušo daļu: 1 − {5|8} = {3|8}.",
             "Aprēķini vērtību: 120 : 8 · 3 = 45 km.",
             "Pārbaude: 30 + 45 + 45 = 120.",
         ],
         pieze="Otrs ceļš: katras dienas km (30, 45) un 120 − 30 − 45 = 45."),

    Paraugs("Divi ceļi",
            uzd="Ceļš 120 km. 1. dienā {2|8}, 2. dienā {3|8}. Cik km "
                "3. dienā?",
            soli=[
                ("1 − {2|8} − {3|8} = {3|8}", "1. ceļš: daļas."),
                ("120 : 8 · 3 = 45", None),
                ("30 + 45 = 75; 120 − 75 = 45", "2. ceļš: kilometri."),
            ],
            atbilde="45 km"),

    Ievadi("Salikti uzdevumi", [
        {"jaut": "Grāmata 200 lpp. 1. dienā {1|4}, 2. dienā {2|4}. Cik "
                 "lappušu 3. dienā?", "atb": ["50"],
         "padoms": "Atlika {1|4}."},
        {"jaut": "Nauda 60 €. Grāmatai {1|3}, spēlei {1|3}. Cik € palika?",
         "atb": ["20"], "padoms": "Atlika {1|3}."},
        {"jaut": "Ceļš 90 km. Pirmajā stundā {4|9}, otrajā {3|9}. Cik km "
                 "palika?", "atb": ["20"], "padoms": "Atlika {2|9}."},
        {"jaut": "Dārzs 40 m². Kartupeļi {3|8}, burkāni {1|8}. Cik m² "
                 "palika?", "atb": ["20"], "padoms": "Atlika {4|8}."},
    ]),

    Varianti("Kāda daļa atlika?", [
        {"jaut": "{1|5} un {2|5} izlietots. Atlika?",
         "opcijas": ["{2|5}", "{3|5}", "{3|10}", "{1|5}"], "pareizi": 0,
         "padoms": "1 − {3|5}."},
        {"jaut": "{3|10} un {5|10} nobraukts. Atlika?",
         "opcijas": ["{2|10}", "{8|10}", "{2|20}", "{5|10}"], "pareizi": 0,
         "padoms": "10 − 8."},
        {"jaut": "Ja atlika {2|10} no 50 km, cik km?",
         "opcijas": ["10", "20", "25", "5"], "pareizi": 0,
         "padoms": "50 : 10 · 2."},
    ]),

    Pasaule("Ģimenes ceļojums uz Liepāju",
            Ievadi("", [
                {"jaut": "Rīga-Liepāja ap 220 km. Līdz atpūtas vietai nobrauca "
                         "{7|11} ceļa. Cik km?",
                 "atb": ["140"], "padoms": "220 : 11 · 7."},
                {"jaut": "Cik km vēl atlika?", "atb": ["80"],
                 "padoms": "220 − 140."},
                {"jaut": "Kāda daļa ceļa atlika?", "atb": ["4/11"],
                 "vieta": "piem., 1/2", "padoms": "1 − {7|11}."},
                {"jaut": "Nākamā pietura - pēc {1|2} no atlikušā ceļa. Cik km "
                         "līdz tai?",
                 "atb": ["40"], "padoms": "80 : 2."},
            ]),
            pavediens="celojums",
            konteksts="Ceļojumā bieži saka «jau pusi nobraucām» - un "
                      "matemātika parāda, cik tas ir kilometros.",
            kapec="Salikts uzdevums ir vairāki vienkārši, saliekti kopā."),

    Kopsavilkums([
        "Risinu uzdevumus ar vairākām daļām.",
        "Saskaitu daļas un atrodu atlikušo daļu.",
        "Aprēķinu daļas vērtību kilometros vai eiro.",
    ]),

    Majas([
        "Izplāno 3 dienu pārgājienu: kāda daļa ceļa katru dienu?",
        "Atrisini: 1. dienā {1|3}, 2. dienā {1|2} no 60 km. Cik 3. dienā?",
        "Paskaidro, kurš no diviem ceļiem tev ērtāks.",
    ]),
]
