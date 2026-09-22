# -*- coding: utf-8 -*-
"""5. klase, 125. stunda: «Kā rēķināt, ja malas dotas dažādās vienībās?»

Jauns mikrotemats sākas ar kļūdu, ko pieļauj gandrīz visi: malas 2 m un
50 cm sareizina tieši, un laukums iznāk simtkārt greizs. Tāpēc pirmā stunda
par laukumiem nav par formulu, bet par soli pirms tās - abas malas vispirms
jāizsaka vienās un tajās pašās vienībās.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, figura, restis)

TEMA = "Kā rēķināt, ja malas dotas dažādās vienībās?"

MERKIS = ("Iemācīsimies aprēķināt taisnstūra laukumu, malu garumus "
          "pārveidojot vienādās mērvienībās.")

SATURS = [
    Sakums("Divi metri un piecdesmit centimetru",
           zimejums=figura([(0, 0), (8, 0), (8, 2), (0, 2)],
                           uzraksti=[(4, -0.4, "2 m"), (8.7, 1, "50 cm")],
                           virsraksts="Viens taisnstūris, divas vienības"),
           paraksts="2 m = 200 cm, tāpēc laukums ir 200 · 50 = 10 000 cm².",
           fakti=["Malu garumi doti dažādās vienībās.",
                  "Sareizināt tos tieši nedrīkst.",
                  "Vispirms abus izsaka vienās vienībās."]),

    Doma("Vispirms vienas vienības",
         "Taisnstūra laukumu rēķina, reizinot malas; abām malām jābūt "
         "izteiktām vienās un tajās pašās mērvienībās.",
         soli=[
             "Pieraksti abas malas ar to vienībām.",
             "Izvēlies vienu vienību abām.",
             "Pārveido otru malu šajā vienībā.",
             "Sareizini malas.",
             "Pieraksti laukumu ar kvadrātvienību.",
         ],
         pieze="1 m = 100 cm, bet 1 m² = 10 000 cm², jo kvadrātā ietilpst "
               "100 · 100 mazie kvadrāti. Tāpēc laukuma vienības pārveido "
               "citādi nekā garuma."),

    Paraugs("Malas 2 m un 50 cm",
            uzd="Aprēķini taisnstūra laukumu.",
            soli=[
                ("2 m = 200 cm",
                 "Izvēlas centimetrus."),
                ("200 · 50 = 10 000",
                 "Reizina malas."),
                ("S = 10 000 cm²",
                 "Laukums centimetros kvadrātā."),
                ("Pārbaude: abas malas bija centimetros",
                 "Viena vienība abām malām."),
            ],
            atbilde="S = 10 000 cm²"),

    Ievadi("Pārveido un aprēķini", [
        {"jaut": "Cik centimetru ir 2 m?",
         "atb": ["200"], "padoms": "1 m = 100 cm."},
        {"jaut": "Cik centimetru ir 5 m?",
         "atb": ["500"], "padoms": "5 · 100."},
        {"jaut": "Malas 200 cm un 50 cm. Cik ir laukums kvadrātcentimetros?",
         "atb": ["10000", "10 000"], "padoms": "200 · 50."},
        {"jaut": "Malas 3 m un 4 m. Cik ir laukums kvadrātmetros?",
         "atb": ["12"], "padoms": "3 · 4."},
        {"jaut": "Malas 300 cm un 200 cm. Cik ir laukums "
                 "kvadrātcentimetros?",
         "atb": ["60000", "60 000"], "padoms": "300 · 200."},
        {"jaut": "Cik milimetru ir 4 cm?",
         "atb": ["40"], "padoms": "1 cm = 10 mm."},
        {"jaut": "Malas 40 mm un 30 mm. Cik ir laukums kvadrātmilimetros?",
         "atb": ["1200", "1 200"], "padoms": "40 · 30."},
        {"jaut": "Cik kvadrātcentimetru ir 1 m²?",
         "atb": ["10000", "10 000"], "padoms": "100 · 100."},
    ], pamats=4,
        ievads="Vispirms viena vienība abām malām, tikai tad reizināšana."),

    Zimejums("Mērvienību pāreja",
             restis([["1 m", "100 cm"],
                     ["1 cm", "10 mm"]],
                    virsraksts="Garuma vienības"),
             paskaidro="Garumam pāreja ir 100 vai 10; laukumam tie paši "
                       "skaitļi jāreizina divreiz, jo laukums ir divas "
                       "malas.",
             ievads="Šie divi pāri der gandrīz visiem uzdevumiem."),

    Varianti("Kur rodas kļūda?", [
        {"jaut": "Malas ir 2 m un 50 cm. Ko dara vispirms?",
         "opcijas": ["Pārveido vienās vienībās", "Sareizina",
                     "Saskaita", "Dala"],
         "pareizi": 0,
         "padoms": "Reizināt drīkst tikai vienādas vienības."},
        {"jaut": "Skolēns rēķina 2 · 50 = 100 un raksta S = 100. Kur ir "
                 "kļūda?",
         "opcijas": ["Malas nav vienās vienībās", "Reizinājums ir nepareizs",
                     "Trūkst kvadrātvienības", "Kļūdas nav"],
         "pareizi": 0,
         "padoms": "Metri un centimetri kopā."},
        {"jaut": "Cik kvadrātcentimetru ir 1 m²?",
         "opcijas": ["10 000", "100", "1 000", "1 000 000"],
         "pareizi": 0,
         "padoms": "100 · 100."},
        {"jaut": "Malas 3 m un 200 cm. Cik ir laukums kvadrātmetros?",
         "opcijas": ["6", "600", "60", "3"],
         "pareizi": 0,
         "padoms": "200 cm = 2 m."},
        {"jaut": "Kāda vienība ir laukumam?",
         "opcijas": ["Kvadrātvienība", "Garuma vienība", "Grāds",
                     "Nav vienības"],
         "pareizi": 0,
         "padoms": "cm², m²."},
        {"jaut": "Kuru vienību izvēlēties?",
         "opcijas": ["To, kurā abas malas ir veseli skaitļi",
                     "Vienmēr metrus",
                     "Vienmēr centimetrus",
                     "Tas ir vienalga"],
         "pareizi": 0,
         "padoms": "Lai nebūtu jārēķina ar daļām."},
    ], pamats=4),

    Pasaule("Cik flīžu vajag?",
            Ievadi("", [
                {"jaut": "Grīda ir 4 m x 3 m. Cik kvadrātmetru ir laukums?",
                 "atb": ["12"], "padoms": "4 · 3."},
                {"jaut": "Siena ir 250 cm x 200 cm. Cik "
                         "kvadrātcentimetru ir laukums?",
                 "atb": ["50000", "50 000"], "padoms": "250 · 200."},
                {"jaut": "Logs ir 2 m x 150 cm. Cik centimetru ir pirmā "
                         "mala?",
                 "atb": ["200"], "padoms": "2 · 100."},
                {"jaut": "Cik kvadrātcentimetru ir šī loga laukums?",
                 "atb": ["30000", "30 000"], "padoms": "200 · 150."},
            ]),
            pavediens="maja",
            konteksts="Remontā izmērus raksta gan metros, gan centimetros, "
                      "reizēm vienā un tajā pašā rindā.",
            kapec="Viena aizmirsta pārveide padara rēķinu simtkārt greizu."),

    Kopsavilkums([
        "Pārveidoju malu garumus vienās mērvienībās.",
        "Aprēķinu taisnstūra laukumu, reizinot malas.",
        "Pierakstu laukumu ar kvadrātvienību.",
        "Zinu, ka 1 m² ir 10 000 cm².",
    ]),

    Majas([
        "Aprēķini laukumu taisnstūrim ar malām 3 m un 80 cm.",
        "Izmēri kādu virsmu mājās un aprēķini tās laukumu.",
        "Pieraksti, kāpēc laukuma vienības pārveido citādi nekā garuma.",
    ]),
]
