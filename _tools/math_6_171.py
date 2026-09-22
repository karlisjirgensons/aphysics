# -*- coding: utf-8 -*-
"""6. klase, 171. stunda: «Kā lietoju koordinātu plakni?»

Trešā noslēguma stunda. Koordinātu plakne šogad kalpoja divām lietām:
grafikiem un figūrām. Te abas satiekas vienā stundā, jo 7. klasē tās kļūs
par vienu tematu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, plakne)

TEMA = "Kā lietoju koordinātu plakni?"

MERKIS = ("Atkārtosim koordinātu plakni: punktus, grafikus un figūras.")

SATURS = [
    Sakums("Divas lietas vienā plaknē",
           zimejums=plakne(lauzta=[(-3, -2), (0, 1), (3, 3)],
                           punkti=[(-2, 3, "A")],
                           no_x=-4, lidz_x=4, no_y=-4, lidz_y=4, solis=1),
           paraksts="Tajā pašā plaknē var attēlot gan grafiku, gan atsevišķu "
                    "punktu vai figūru.",
           fakti=["Punkta koordinātas raksta iekavās ar semikolu.",
                  "Grafiks rāda, kā viens lielums mainās līdz ar otru.",
                  "Figūru veido virsotnes, savienotas pēc kārtas."]),

    Doma("Punkts, grafiks, figūra",
         "Koordinātu plaknē skaitļu pāris kļūst par punktu; punktu virkne - "
         "par grafiku; slēgta punktu virkne - par figūru.",
         soli=[
             "Iekārto plakni ar abām asīm un piemērotu vienību.",
             "Atliec punktus pēc koordinātām.",
             "Ja tie apraksta izmaiņu, savieno tos par grafiku.",
             "Ja tie ir virsotnes, savieno un noslēdz figūru.",
             "Nolasi vajadzīgo: vērtību, izmaiņu vai malas garumu.",
         ],
         pieze="Viens un tas pats punkts (3; −2) var būt gan mērījums "
               "grafikā, gan figūras virsotne. Atšķiras tikai tas, ko ar to "
               "dara tālāk."),

    Paraugs("Nolasi no plaknes",
            uzd="Punkti (−3; −2), (0; 1) un (3; 3) ir temperatūras "
                "mērījumi. Ko var pateikt?",
            soli=[
                ("Pirmais mērījums: −2 grādi",
                 "Otrā koordināta."),
                ("Otrais: 1 grāds",
                 "Temperatūra pieauga par 3 grādiem."),
                ("Trešais: 3 grādi",
                 "Vēl par 2 grādiem."),
                ("Kopējā izmaiņa: no −2 līdz 3 ir 5 grādi",
                 "Visa perioda pieaugums."),
            ],
            atbilde="temperatūra pieauga par 5 grādiem"),

    Ievadi("Nolasi un aprēķini", [
        {"jaut": "Punkts (3; −2). Kāda ir tā otrā koordināta?",
         "atb": ["-2", "−2"], "padoms": "Vertikālā ass."},
        {"jaut": "No −2 līdz 3. Par cik pieauga vērtība?",
         "atb": ["5"], "padoms": "3 + 2."},
        {"jaut": "Figūras virsotnes (−2; 1) un (3; 1). Cik vienības gara ir "
                 "mala?",
         "atb": ["5"], "padoms": "No −2 līdz 3."},
        {"jaut": "Virsotnes (3; 1) un (3; −3). Cik vienības gara ir mala?",
         "atb": ["4"], "padoms": "No 1 līdz −3."},
        {"jaut": "Cik kvadrātvienību ir taisnstūra laukums ar malām 5 un 4?",
         "atb": ["20"], "padoms": "5 · 4."},
        {"jaut": "Punktu (2; 3) pārvieto par 4 pa kreisi. Kāda ir jaunā "
                 "pirmā koordināta?",
         "atb": ["-2", "−2"], "padoms": "2 − 4."},
    ], pamats=4),

    Varianti("Ko rāda plakne?", [
        {"jaut": "Punkta (−3; 2) pirmā koordināta rāda...",
         "opcijas": ["attālumu pa horizontālo asi",
                     "attālumu pa vertikālo asi",
                     "punkta vērtību", "kvadrantu"],
         "pareizi": 0,
         "padoms": "Pirmā - horizontālā."},
        {"jaut": "Grafika horizontāla daļa nozīmē...",
         "opcijas": ["lielums nemainās", "lielums aug",
                     "lielums sarūk", "mērījumu trūkst"],
         "pareizi": 0,
         "padoms": "Vērtība paliek tā pati."},
        {"jaut": "Atspoguļojot pret vertikālo asi, mainās...",
         "opcijas": ["pirmā koordināta", "otrā koordināta",
                     "abas", "neviena"],
         "pareizi": 0,
         "padoms": "Attālums līdz vertikālajai asij."},
        {"jaut": "Pagriežot par 180° ap sākumpunktu, mainās...",
         "opcijas": ["abas koordinātas", "tikai pirmā",
                     "tikai otrā", "neviena"],
         "pareizi": 0,
         "padoms": "Simetrija pret punktu."},
    ], pamats=4),

    Pasaule("Kā attēlot nedēļas datus?",
            Ievadi("", [
                {"jaut": "Nedēļas temperatūras: −4; −1; 2; 0; 3 °C. Kāda ir "
                         "augstākā?",
                 "atb": ["3"], "padoms": "Lielākais skaitlis."},
                {"jaut": "Kāda ir zemākā?",
                 "atb": ["-4", "−4"], "padoms": "Mazākais skaitlis."},
                {"jaut": "Kāda ir nedēļas svārstība grādos?",
                 "atb": ["7"], "padoms": "3 + 4."},
                {"jaut": "Cik dienas temperatūra bija zem nulles?",
                 "atb": ["2"], "padoms": "−4 un −1."},
            ]),
            pavediens="planeta",
            konteksts="Nedēļas grafiks pasaka gan katras dienas vērtību, gan "
                      "to, cik strauji tā mainījās.",
            kapec="Viena plakne satur visus nedēļas datus."),

    Kopsavilkums([
        "Atlieku punktus un nolasu to koordinātas.",
        "Veidoju grafiku no mērījumiem un izlasu to.",
        "Zīmēju figūras un aprēķinu malu garumus.",
        "Lietoju pārvietošanu, atspoguļošanu un pagriešanu.",
    ]),

    Majas([
        "Uzzīmē plakni un atzīmē punktus (−3; 2), (1; −4) un (0; 3).",
        "Uzzīmē taisnstūri ar malām 5 un 3 un pieraksti virsotņu "
        "koordinātas.",
        "Attēlo nedēļas temperatūras grafikā.",
    ]),
]
