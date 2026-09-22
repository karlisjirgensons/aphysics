# -*- coding: utf-8 -*-
"""5. klase, 73. stunda: «Cik ir trīs ceturtdaļas kilograma?»

Iepriekšējā stunda rēķināja pamatdaļu; te skaitītājs kļūst lielāks par vienu,
un darbību ir divas. Otra stundas puse ir mērvienības: {3|4} kg atbildē ir
750 g, nevis 0,75 kg, jo decimāldaļas 5. klasē nāk tikai 5.7. tematā. Tāpēc
te vienmēr pāriet uz sīkāku mērvienību.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, dala)

TEMA = "Cik ir trīs ceturtdaļas kilograma?"

MERKIS = ("Iemācīsimies noteikt daļu no garuma, masas un laika vienībām un "
          "pierakstīt rezultātu ar piemērotu mērvienību.")

SATURS = [
    Sakums("Trīs ceturtdaļas kilograma uz svariem",
           zimejums=dala(4, 3, "3/4 kg"),
           paraksts="Viens kilograms ir 1000 g; trīs ceturtdaļas no tā - "
                    "750 g.",
           fakti=["Ceturtdaļa kilograma ir 250 g.",
                  "Trīs tādas ceturtdaļas ir 750 g.",
                  "Vispirms dala, tad reizina."]),

    Doma("Vispirms dala, tad reizina",
         "Lai atrastu daļas vērtību, veselo dala ar saucēju un iegūto "
         "reizina ar skaitītāju.",
         soli=[
             "Pārvērt veselo sīkākā mērvienībā, ja tas ir ērtāk.",
             "Dali veselo ar saucēju - iegūsi vienu daļu.",
             "Reizini to ar skaitītāju.",
             "Pieraksti atbildi ar mērvienību.",
         ],
         pieze="1 kg = 1000 g, 1 m = 100 cm, 1 h = 60 min, 1 t = 1000 kg. "
               "Ja veselo pārvērš sīkākā vienībā, dalījums gandrīz vienmēr "
               "iznāk vesels skaitlis."),

    Paraugs("Cik gramu ir {3|4} kg?",
            uzd="Aprēķini {3|4} no viena kilograma un pieraksti atbildi "
                "gramos.",
            soli=[
                ("1 kg = 1000 g",
                 "Pāriet uz sīkāku mērvienību."),
                ("1000 : 4 = 250",
                 "Viena ceturtdaļa ir 250 g."),
                ("250 · 3 = 750",
                 "Trīs ceturtdaļas."),
                ("{3|4} kg = 750 g",
                 "Atbilde ar mērvienību."),
            ],
            atbilde="750 g"),

    Ievadi("Daļa no mērvienības", [
        {"jaut": "Cik gramu ir {1|2} kg?",
         "atb": ["500"], "padoms": "1000 : 2."},
        {"jaut": "Cik gramu ir {3|4} kg?",
         "atb": ["750"], "padoms": "1000 : 4 = 250; 250 · 3."},
        {"jaut": "Cik gramu ir {2|5} kg?",
         "atb": ["400"], "padoms": "1000 : 5 = 200; 200 · 2."},
        {"jaut": "Cik centimetru ir {3|4} m?",
         "atb": ["75"], "padoms": "100 : 4 = 25; 25 · 3."},
        {"jaut": "Cik centimetru ir {2|5} m?",
         "atb": ["40"], "padoms": "100 : 5 = 20; 20 · 2."},
        {"jaut": "Cik minūšu ir {2|3} stundas?",
         "atb": ["40"], "padoms": "60 : 3 = 20; 20 · 2."},
        {"jaut": "Cik minūšu ir {3|4} stundas?",
         "atb": ["45"], "padoms": "60 : 4 = 15; 15 · 3."},
        {"jaut": "Cik kilogramu ir {3|5} tonnas?",
         "atb": ["600"], "padoms": "1000 : 5 = 200; 200 · 3."},
    ], pamats=4,
        ievads="Vispirms pārvērt mērvienību, tad dali un reizini."),

    Zimejums("Trīs gabali no četriem",
             dala(4, 3, "3/4"),
             paskaidro="Katrs gabals ir 250 g, tāpēc trīs gabali ir 750 g. "
                       "Ceturtais gabals paliek - tie ir 250 g.",
             ievads="Josla ir viens kilograms, sadalīts ceturtdaļās."),

    Varianti("Kura mērvienība der?", [
        {"jaut": "Kā ērtāk pierakstīt {3|4} kg?",
         "opcijas": ["750 g", "3 kg", "4 kg", "34 g"],
         "pareizi": 0,
         "padoms": "Sīkākā mērvienībā skaitlis ir vesels."},
        {"jaut": "Kāda ir pareizā darbību secība?",
         "opcijas": ["Vispirms dala ar saucēju, tad reizina ar skaitītāju",
                     "Vispirms reizina ar saucēju",
                     "Vispirms dala ar skaitītāju",
                     "Secība nav svarīga"],
         "pareizi": 0,
         "padoms": "Vienu daļu atrod, dalot."},
        {"jaut": "Cik minūšu ir {1|4} stundas?",
         "opcijas": ["15", "20", "25", "40"],
         "pareizi": 0,
         "padoms": "60 : 4."},
        {"jaut": "Cik centimetru ir {1|2} m?",
         "opcijas": ["50", "20", "5", "500"],
         "pareizi": 0,
         "padoms": "100 : 2."},
        {"jaut": "Kāpēc kilogramu pārvērš gramos?",
         "opcijas": ["Lai dalījums iznāktu vesels skaitlis",
                     "Lai skaitlis būtu lielāks",
                     "Tā prasa likums",
                     "Tas nav vajadzīgs"],
         "pareizi": 0,
         "padoms": "1000 dalās ar daudz ko, 1 - nē."},
        {"jaut": "Cik gramu ir {7|10} kg?",
         "opcijas": ["700", "70", "7", "170"],
         "pareizi": 0,
         "padoms": "1000 : 10 = 100; 100 · 7."},
    ], pamats=4),

    Pasaule("Ko ielikt somā?",
            Ievadi("", [
                {"jaut": "Ceļojumā atļauts ņemt {3|4} kg saldumu. Cik gramu "
                         "tas ir?",
                 "atb": ["750"], "padoms": "1000 : 4 · 3."},
                {"jaut": "Pārgājiens ilgst {3|4} stundas. Cik minūšu tas ir?",
                 "atb": ["45"], "padoms": "60 : 4 · 3."},
                {"jaut": "Teltij vajag {2|5} m auklas. Cik centimetru tas ir?",
                 "atb": ["40"], "padoms": "100 : 5 · 2."},
                {"jaut": "Ūdens pudelē ir {3|5} l. Cik mililitru tas ir?",
                 "atb": ["600"], "padoms": "1000 : 5 · 3."},
            ]),
            pavediens="celojums",
            konteksts="Somā viss ir noteikts daļās, bet uz svariem un "
                      "mērlentes ir grami un centimetri.",
            kapec="Bez pārrēķina daļa paliek tikai vārds, nevis skaitlis."),

    Kopsavilkums([
        "Aprēķinu daļas vērtību, dalot ar saucēju un reizinot ar skaitītāju.",
        "Pārvēršu veselo sīkākā mērvienībā, ja tas atvieglo rēķinu.",
        "Nosaku daļu no garuma, masas un laika vienībām.",
        "Pierakstu atbildi ar piemērotu mērvienību.",
    ]),

    Majas([
        "Aprēķini {2|3} no 90 minūtēm un {3|8} no 1 kg.",
        "Nosver mājās kaut ko, kas sver ap {1|4} kg.",
        "Uzraksti, cik centimetru ir {4|5} m.",
    ]),
]
