# -*- coding: utf-8 -*-
"""6. klase, 46. stunda: «Kā izskatās dalīšana ar 10?»

Trešais no četriem algoritmiem. Tas ir tas pats, ko iepriekšējā stundā -
tikai citā pierakstā, un skolēniem tas jāpamana pašiem. Kalkulators te ir
nevis rīks, ar ko rēķināt, bet ar ko *pārbaudīt* savu likumu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti)

TEMA = "Kā izskatās dalīšana ar 10?"

MERKIS = ("Formulēsim algoritmu dalīšanai ar 10, 100 un 1000 un pārbaudīsim "
          "to ar kalkulatoru.")

SATURS = [
    Sakums("Divas darbības, viens rezultāts",
           fakti=["45 : 10 = 4,5 un 45 · 0,1 = 4,5 - viens un tas pats.",
                  "Dalot ar 10, komats pārceļas par vienu vietu pa kreisi.",
                  "Dalītāja nulles pasaka soļu skaitu."]),

    Doma("Dalīt ar 10 nozīmē reizināt ar 0,1",
         "Dalot ar 10, 100 vai 1000, komatu pārceļ par tik vietām pa kreisi, "
         "cik nulles ir dalītājā.",
         soli=[
             "Saskaiti nulles dalītājā.",
             "Pārcel komatu par tik vietām pa kreisi.",
             "Ja ciparu nepietiek, priekšā pieraksti nulles.",
             "Pārbaudi ar kalkulatoru vai ar reizināšanu.",
         ],
         pieze="Pārbaudi uz zināma piemēra: 300 : 100 = 3. Trīs simti satur "
               "trīs simtus - atbilde ir acīmredzama, un tā apstiprina "
               "likumu."),

    Paraugs("Dali ar 1000",
            uzd="Cik ir 62,5 : 1000?",
            soli=[
                ("1000 - trīs nulles",
                 "Tik vietas komats pārceļas."),
                ("62,5 → 6,25 → 0,625 → 0,0625",
                 "Trīs soļi pa kreisi."),
                ("Pārbaude: 0,0625 · 1000 = 62,5",
                 "Reizināšana atgriež dalāmo."),
            ],
            atbilde="0,0625"),

    Ievadi("Dali ar 10, 100 un 1000", [
        {"jaut": "Cik ir 45 : 10?",
         "atb": ["4,5", "4.5"], "padoms": "Viena vieta pa kreisi."},
        {"jaut": "Cik ir 8 : 100?",
         "atb": ["0,08", "0.08"], "padoms": "Divas vietas pa kreisi."},
        {"jaut": "Cik ir 3,7 : 10?",
         "atb": ["0,37", "0.37"], "padoms": "Viena vieta pa kreisi."},
        {"jaut": "Cik ir 250 : 1000?",
         "atb": ["0,25", "0.25"], "padoms": "Trīs vietas pa kreisi."},
        {"jaut": "Cik ir 0,6 : 100?",
         "atb": ["0,006", "0.006"], "padoms": "Divas vietas; nulles priekšā."},
        {"jaut": "Cik ir 1205 : 100?",
         "atb": ["12,05", "12.05"], "padoms": "Divas vietas pa kreisi."},
    ], pamats=4,
        ievads="Nulles dalītājā ir soļi pa kreisi."),

    Petijums("Pārbaudi likumu ar kalkulatoru",
             vajag="kalkulators un burtnīca",
             soli=[
                 "Pieraksti piecus savus dalījumus ar 10, 100 vai 1000.",
                 "Izrēķini katru galvā, pārceļot komatu.",
                 "Pārbaudi katru ar kalkulatoru.",
                 "Pieraksti, cik reižu atbildes sakrita.",
             ],
             secinajums="Ja visas sakrita, likums strādā; ja ne - kļūda "
                        "parasti ir soļu skaitā, ne virzienā."),

    Varianti("Kurš pieraksts ir tas pats?", [
        {"jaut": "24 : 100 ir tas pats, kas...",
         "opcijas": ["24 · 0,01", "24 · 100", "24 · 0,1", "24 : 0,01"],
         "pareizi": 0,
         "padoms": "Dalīt ar 100 nozīmē reizināt ar 0,01."},
        {"jaut": "Cik ir 9 : 1000?",
         "opcijas": ["0,009", "0,09", "0,9", "9000"],
         "pareizi": 0,
         "padoms": "Trīs vietas pa kreisi."},
        {"jaut": "Dalot ar 10, skaitlis...",
         "opcijas": ["kļūst mazāks", "kļūst lielāks", "nemainās",
                     "kļūst par nulli"],
         "pareizi": 0,
         "padoms": "10 ir lielāks par 1."},
        {"jaut": "Kā no centimetriem iegūt metrus?",
         "opcijas": ["Dalot ar 100", "Reizinot ar 100", "Dalot ar 10",
                     "Reizinot ar 1000"],
         "pareizi": 0,
         "padoms": "1 m = 100 cm."},
    ], pamats=4),

    Pasaule("Cik tas ir mērvienībās?",
            Ievadi("", [
                {"jaut": "Cik metru ir 385 cm?",
                 "atb": ["3,85", "3.85"], "padoms": "385 : 100."},
                {"jaut": "Cik kilogramu ir 1250 g?",
                 "atb": ["1,25", "1.25"], "padoms": "1250 : 1000."},
                {"jaut": "Cik kilometru ir 640 m?",
                 "atb": ["0,64", "0.64"], "padoms": "640 : 1000."},
                {"jaut": "Cik litru ir 75 ml?",
                 "atb": ["0,075", "0.075"], "padoms": "75 : 1000."},
            ]),
            pavediens="sports",
            konteksts="Sacensību protokolā rezultātus raksta metros, bet "
                      "mēra centimetros - pārveido ar dalīšanu.",
            kapec="Viena mērvienību maiņa ir viens komata solis."),

    Kopsavilkums([
        "Dalu ar 10, 100 un 1000, pārceļot komatu pa kreisi.",
        "Zinu, ka dalīt ar 10 ir tas pats, kas reizināt ar 0,1.",
        "Pārbaudu savu likumu ar kalkulatoru.",
        "Lietoju to mērvienību pārveidošanā.",
    ]),

    Majas([
        "Izrēķini 4,8 : 100 un 56 : 1000.",
        "Pārvērt trīs mājās atrastus svarus no gramiem kilogramos.",
        "Pieraksti, kāpēc dalīšana ar 100 un reizināšana ar 0,01 ir viens "
        "un tas pats.",
    ]),
]
