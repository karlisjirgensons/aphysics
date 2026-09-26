# -*- coding: utf-8 -*-
"""3. klase, 119. stunda: «Kas notiek ar laukumu, mainot malas?»

Pētījuma stunda: ja vienu malu palielina divas reizes, laukums arī kļūst
divreiz lielāks; ja abas - četras reizes. Tas ir pirmais gadījums, kad
izmaiņa vienā vietā rada lielāku izmaiņu citā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Slidnis, Varianti,
                         Zimejums, kolonnas)

TEMA = "Kas notiek ar laukumu, mainot malas?"

MERKIS = ("Pētīsim, kā mainās laukums, mainot malu garumus, un formulēsim "
          "pamanīto.")

SATURS = [
    Sakums("Kas notiek, ja istabu padara divreiz platāku?",
           zimejums=kolonnas([("3 x 4", 12), ("6 x 4", 24), ("6 x 8", 48)],
                             " m²"),
           paraksts="Katra malas dubultošana laukumu arī dubulto.",
           fakti=["Dubultojot vienu malu, laukums kļūst divreiz lielāks.",
                  "Dubultojot abas malas, laukums kļūst četras reizes "
                  "lielāks."]),

    Doma("Katra malas dubultošana dubulto laukumu",
         "Ja vienu malu palielina divas reizes, laukums aug divas reizes; ja "
         "abas - četras reizes.",
         soli=[
             "Izrēķini sākotnējo laukumu.",
             "Palielini vienu malu un izrēķini vēlreiz.",
             "Salīdzini abus laukumus.",
             "Atkārto, palielinot arī otru malu.",
         ],
         pieze="Perimetrs tā neaug: dubultojot vienu malu, perimetrs kļūst "
               "lielāks, bet ne divas reizes."),

    Slidnis("Kā aug laukums",
            soli=[
                {"v": "3 x 4 = 12", "teksts": "Sākuma taisnstūris.",
                 "josla": 25},
                {"v": "6 x 4 = 24",
                 "teksts": "Platums dubultots - laukums divreiz lielāks.",
                 "josla": 50},
                {"v": "6 x 8 = 48",
                 "teksts": "Arī garums dubultots - vēl divreiz lielāks.",
                 "josla": 100},
            ],
            ievads="Katrs solis dubulto vienu malu."),

    Petijums("Pārbaudi pats",
             vajag="rūtiņu lapa un zīmulis",
             soli=[
                 "Uzzīmē taisnstūri 3 x 4 un saskaiti rūtiņas.",
                 "Uzzīmē blakus taisnstūri 6 x 4 un saskaiti.",
                 "Uzzīmē trešo - 6 x 8 - un saskaiti.",
                 "Pieraksti visus trīs laukumus vienā rindā.",
             ],
             secinajums="12, 24, 48 - katru reizi divreiz vairāk, tieši tā, "
                        "kā rāda rēķins."),

    Paraugs("Cik reižu laukums kļūst lielāks?",
            uzd="Taisnstūra malas 3 cm un 4 cm. Abas malas palielina divas "
                "reizes. Cik reižu aug laukums?",
            soli=[
                ("3 · 4 = 12 cm²",
                 "Sākotnējais laukums."),
                ("6 · 8 = 48 cm²",
                 "Jaunais laukums."),
                ("48 : 12 = 4",
                 "Laukums kļuva četras reizes lielāks."),
            ],
            atbilde="četras reizes"),

    Ievadi("Kā mainās laukums?", [
        {"jaut": "Taisnstūris 3 x 4. Cik ir laukums?", "atb": ["12"],
         "padoms": "3 · 4."},
        {"jaut": "Taisnstūris 6 x 4. Cik ir laukums?", "atb": ["24"],
         "padoms": "6 · 4."},
        {"jaut": "Cik reižu laukums kļuva lielāks?", "atb": ["2"],
         "padoms": "24 : 12."},
        {"jaut": "Taisnstūris 6 x 8. Cik ir laukums?", "atb": ["48"],
         "padoms": "6 · 8."},
        {"jaut": "Cik reižu 48 ir lielāks par 12?", "atb": ["4"],
         "padoms": "48 : 12."},
        {"jaut": "Kvadrāts 5 x 5. Cik ir laukums, ja malu dubulto?",
         "atb": ["100"], "padoms": "10 · 10."},
    ], pamats=4),

    Zimejums("Malas trīskāršošana",
             kolonnas([("2 x 3", 6), ("6 x 3", 18), ("6 x 9", 54)], " cm²"),
             paskaidro="Trīskāršojot vienu malu, laukums aug trīs reizes; "
                       "abas - deviņas reizes.",
             ievads="Tas pats likums ar trijnieku."),

    Varianti("Cik reižu aug laukums?", [
        {"jaut": "Vienu malu palielina 2 reizes. Cik reižu aug laukums?",
         "opcijas": ["2", "4", "1", "8"],
         "pareizi": 0, "padoms": "Otra mala nemainās."},
        {"jaut": "Abas malas palielina 2 reizes. Cik reižu aug laukums?",
         "opcijas": ["4", "2", "8", "16"],
         "pareizi": 0, "padoms": "2 · 2."},
        {"jaut": "Abas malas palielina 3 reizes. Cik reižu aug laukums?",
         "opcijas": ["9", "3", "6", "12"],
         "pareizi": 0, "padoms": "3 · 3."},
        {"jaut": "Vienu malu samazina 2 reizes. Kas notiek ar laukumu?",
         "opcijas": ["Kļūst 2 reizes mazāks", "Nemainās",
                     "Kļūst 4 reizes mazāks", "Kļūst lielāks"],
         "pareizi": 0, "padoms": "Tas pats likums otrādi."},
    ], pamats=4),

    Pasaule("Cik maksās lielāka istaba?",
            Ievadi("", [
                {"jaut": "Istaba 3 m x 4 m. Cik kvadrātmetru ir grīda?",
                 "atb": ["12"], "padoms": "3 · 4."},
                {"jaut": "Grīdas segums maksā 5 eiro par kvadrātmetru. Cik "
                         "eiro maksās šī grīda?",
                 "atb": ["60"], "padoms": "12 · 5."},
                {"jaut": "Istabu padara divreiz platāku: 6 m x 4 m. Cik "
                         "kvadrātmetru?",
                 "atb": ["24"], "padoms": "6 · 4."},
                {"jaut": "Cik eiro maksās šīs istabas grīda?",
                 "atb": ["120"], "padoms": "24 · 5."},
            ]),
            pavediens="maja",
            konteksts="Divreiz platāka istaba prasa divreiz vairāk materiāla "
                      "un maksā divreiz vairāk.",
            kapec="Tāpēc remonta tāmē vienmēr vispirms rēķina laukumu."),

    Kopsavilkums([
        "Pētu, kā mainās laukums, mainot malas.",
        "Zinu, ka vienas malas dubultošana dubulto laukumu.",
        "Zinu, ka abu malu dubultošana laukumu palielina četras reizes.",
        "Formulēju pamanīto savos vārdos.",
    ]),

    Majas([
        "Uzzīmē taisnstūri 2 x 5 un tādu, kuram abas malas ir divreiz "
        "lielākas.",
        "Saskaiti abu laukumus un salīdzini.",
        "Pastāsti mājiniekiem, kāpēc laukums aug četras reizes.",
    ]),
]
