# -*- coding: utf-8 -*-
"""3. klase, 132. stunda: «Kur skaitlis atrodas uz skaitļu taisnes?»

Skaitļu taisne ar lielu iedaļas vērtību. Galvenā prasme ir nolasīt iedaļu:
ja starp 0 un 1000 ir desmit iedaļas, katra ir 100, un skaitli 640 jāliek
starp divām atzīmēm - aptuveni, bet pareizajā vietā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, taisne)

TEMA = "Kur skaitlis atrodas uz skaitļu taisnes?"

MERKIS = ("Attēlosim skaitļus uz skaitļu taisnes ar dotu iedaļas vērtību.")

SATURS = [
    Sakums("Kur uz taisnes likt 640?",
           zimejums=taisne(0, 1000, 200, [(640, "640")]),
           paraksts="Starp 600 un 800, tuvāk sešsimtiem.",
           fakti=["Vispirms noskaidro iedaļas vērtību.",
                  "Tad atrodi, starp kurām atzīmēm skaitlis atrodas."]),

    Doma("Vispirms iedaļa, tad vieta",
         "Izdali attālumu starp divām atzīmēm ar iedaļu skaitu - tikai tad "
         "meklē skaitļa vietu.",
         soli=[
             "Atrodi uz taisnes divus uzrakstītus skaitļus.",
             "Saskaiti iedaļas starp tiem un izrēķini iedaļas vērtību.",
             "Atrodi, starp kurām atzīmēm ir tavs skaitlis.",
             "Atzīmē to attiecīgajā vietā.",
         ],
         pieze="Ja skaitlis ir tuvāk vienai atzīmei, punkts arī jāliek tuvāk "
               "tai - taisne rāda ne tikai kārtību, bet arī attālumu."),

    Paraugs("Kur atrodas 640?",
            uzd="Uz taisnes no 0 līdz 1000 ar iedaļu 200 atzīmē skaitli 640.",
            soli=[
                ("Atzīmes: 0, 200, 400, 600, 800, 1000",
                 "Iedaļa ir 200."),
                ("640 ir starp 600 un 800",
                 "Lielāks par 600, mazāks par 800."),
                ("Tuvāk 600",
                 "No 600 līdz 640 ir tikai 40."),
            ],
            atbilde="starp 600 un 800, tuvu 600"),

    Ievadi("Nolasi taisni", [
        {"jaut": "Starp 0 un 1000 ir 5 iedaļas. Cik liela ir viena?",
         "atb": ["200"], "padoms": "1000 : 5."},
        {"jaut": "Starp 0 un 1000 ir 10 iedaļas. Cik liela ir viena?",
         "atb": ["100"], "padoms": "1000 : 10."},
        {"jaut": "Starp kurām simtu atzīmēm ir 640? Ieraksti mazāko.",
         "atb": ["600"], "padoms": "600 < 640 < 700."},
        {"jaut": "Par cik 640 ir lielāks par 600?", "atb": ["40"],
         "padoms": "640 − 600."},
        {"jaut": "Kurš skaitlis ir tieši pa vidu starp 400 un 600?",
         "atb": ["500"], "padoms": "Puse no 200 ir 100."},
        {"jaut": "Kurš skaitlis ir tieši pa vidu starp 0 un 1000?",
         "atb": ["500"], "padoms": "1000 : 2."},
    ], pamats=4),

    Zimejums("Smalkāka skala",
             taisne(0, 1000, 100, [(350, "350"), (720, "720")]),
             paskaidro="Ar iedaļu 100 skaitļus var atzīmēt precīzāk nekā ar "
                       "iedaļu 200.",
             ievads="Tā pati taisne, smalkāka skala."),

    Varianti("Kur tas atrodas?", [
        {"jaut": "Starp kurām atzīmēm ir 350, ja iedaļa ir 100?",
         "opcijas": ["300 un 400", "200 un 300", "400 un 500", "0 un 100"],
         "pareizi": 0, "padoms": "300 < 350 < 400."},
        {"jaut": "Kurš skaitlis ir tuvāk 1000?",
         "opcijas": ["950", "850", "500", "100"],
         "pareizi": 0, "padoms": "Vismazākā starpība."},
        {"jaut": "Starp 0 un 500 ir 5 iedaļas. Cik liela ir viena?",
         "opcijas": ["100", "50", "500", "5"],
         "pareizi": 0, "padoms": "500 : 5."},
        {"jaut": "Kurš skaitlis ir tieši pa vidu starp 200 un 400?",
         "opcijas": ["300", "250", "350", "600"],
         "pareizi": 0, "padoms": "Puse no 200."},
    ], pamats=4),

    Pasaule("Cik tālu ir lidojums?",
            Ievadi("", [
                {"jaut": "Kuģis nolidojis 640 km no 1000 km. Cik kilometru "
                         "atlicis?",
                 "atb": ["360"], "padoms": "1000 − 640."},
                {"jaut": "Vai pusceļš jau ir pagājis? Raksti «jā» vai «nē».",
                 "atb": ["jā", "ja"], "padoms": "640 > 500.",
                 "tastatura": "text"},
                {"jaut": "Cik kilometru ir pusceļš?", "atb": ["500"],
                 "padoms": "1000 : 2."},
                {"jaut": "Par cik kilometriem kuģis ir pārsniedzis pusceļu?",
                 "atb": ["140"], "padoms": "640 − 500."},
            ]),
            pavediens="kosmoss",
            konteksts="Lidojuma gaitu rāda uz skalas - tieši tāpat kā skaitli "
                      "uz skaitļu taisnes.",
            kapec="No vietas uz skalas uzreiz redz, cik ceļa vēl priekšā."),

    Kopsavilkums([
        "Nosaku skaitļu taisnes iedaļas vērtību.",
        "Atzīmēju skaitli uz taisnes.",
        "Atrodu, starp kurām atzīmēm skaitlis atrodas.",
        "Atrodu skaitli, kas ir tieši pa vidu.",
    ]),

    Majas([
        "Uzzīmē taisni no 0 līdz 1000 ar iedaļu 100 un atzīmē tajā 250 un "
        "780.",
        "Atrodi skaitli, kas ir tieši pa vidu starp 300 un 700.",
        "Atzīmē uz taisnes savu mājas numuru.",
    ]),
]
