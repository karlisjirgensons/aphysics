# -*- coding: utf-8 -*-
"""4. klase, 146. stunda: «Kur lieto hektāru?»

Hektārs - laukums 100 m × 100 m = 10 000 m². Futbola laukums ir apmēram
0,7 ha, tāpēc hektārs ir «pusotrs futbola laukums». Ar hektāriem mēra
laukus, mežus un parkus - skolēns min piemērus un novērtē.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Sakums, Varianti, kolonnas)

TEMA = "Kur lieto hektāru?"

MERKIS = ("Novērtēsim apkārtnes objektu laukumu hektāros un minēsim "
          "piemērus.")

SATURS = [
    Sakums("Cik futbola laukumu ir hektārā?",
           zimejums=kolonnas([("futbola laukums", 7140),
                              ("1 hektārs", 10000)], " m²"),
           paraksts="105 m × 68 m = 7140 m² - mazliet vairāk nekā "
                    "{2|3} hektāra.",
           fakti=["1 ha = 100 m × 100 m = 10 000 m².",
                  "Hektārs ir mazliet lielāks par futbola laukumu."]),

    Doma("Hektārs lieliem laukumiem",
         "1 ha = 10 000 m²; ar hektāriem mēra laukus, mežus, parkus - "
         "laukumus, kas m² būtu pārāk lieli skaitļi.",
         soli=[
             "Iedomājies kvadrātu 100 m × 100 m.",
             "Tas ir 1 ha = 10 000 m².",
             "Lauks 200 m × 100 m = 20 000 m² = 2 ha.",
             "Mazas platības (dārzs) - m², lielas (lauks) - ha.",
         ],
         pieze="Latvijā lielākā daļa zemnieku saimniecību ir desmitiem "
               "hektāru lielas."),

    Ievadi("Hektāri", [
        {"jaut": "Cik m² ir 1 ha?", "atb": ["10000", "10 000"],
         "padoms": "100 · 100."},
        {"jaut": "Lauks 200 m × 100 m. Cik ha?", "atb": ["2"],
         "padoms": "20 000 : 10 000."},
        {"jaut": "Mežs 300 m × 300 m. Cik ha?", "atb": ["9"],
         "padoms": "3 · 3."},
        {"jaut": "Cik ha ir 50 000 m²?", "atb": ["5"],
         "padoms": "50 000 : 10 000."},
    ]),

    Varianti("m² vai ha?", [
        {"jaut": "Kartupeļu lauks saimniecībā",
         "opcijas": ["ha", "cm²", "mm²"], "pareizi": 0,
         "padoms": "Liels laukums."},
        {"jaut": "Istabas grīda",
         "opcijas": ["m²", "ha", "mm²"], "pareizi": 0,
         "padoms": "Neliels laukums."},
        {"jaut": "Nacionālais parks",
         "opcijas": ["ha", "cm²", "dm²"], "pareizi": 0,
         "padoms": "Ļoti liels."},
        {"jaut": "Kas lielāks: 1 ha vai futbola laukums?",
         "opcijas": ["1 ha", "futbola laukums", "vienādi"], "pareizi": 0,
         "padoms": "10 000 > 7140."},
    ], pamats=4),

    Pasaule("Zemnieka saimniecība",
            Ievadi("", [
                {"jaut": "Saimniecībā 40 ha. Kviešiem {1|2}. Cik ha?",
                 "atb": ["20"], "padoms": "40 : 2."},
                {"jaut": "Rapsim {1|4}. Cik ha?", "atb": ["10"],
                 "padoms": "40 : 4."},
                {"jaut": "No 1 ha iegūst 5 t kviešu. Cik t no 20 ha?",
                 "atb": ["100"], "padoms": "20 · 5."},
                {"jaut": "Ganības 5 ha. Cik m²?", "atb": ["50000",
                 "50 000"], "padoms": "5 · 10 000."},
            ]),
            pavediens="daba",
            konteksts="Zemnieki plāno sējumus hektāros - un raža ir tonnās "
                      "no hektāra.",
            kapec="Hektārs ir lauksaimniecības pamata vienība."),

    Kopsavilkums([
        "Zinu, ka 1 ha = 10 000 m².",
        "Izvēlos, kad lietot m² un kad ha.",
        "Novērtēju lielus laukumus hektāros.",
    ]),

    Majas([
        "Kartē atrodi parku vai lauku un novērtē tā laukumu ha.",
        "Pajautā vecvecākiem, cik ha zemes ir viņu vai kaimiņu saimniecībā.",
        "Aprēķini, cik m² ir 3 ha.",
    ]),
]
