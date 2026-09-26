# -*- coding: utf-8 -*-
"""3. klase, 133. stunda: «Kurš skaitlis trūkst?»

Virknes ar dotu soli. Prasme ir divējāda: atrast soli un pamatot izvēli. Tas
pats uzdevums 29. stundā bija ar reizināšanu; te solis ir saskaitīšana, un
skaitļi ir trīsciparu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         restis)

TEMA = "Kurš skaitlis trūkst?"

MERKIS = ("Ievietosim trūkstošos skaitļus virknē un pamatosim izvēli.")

SATURS = [
    Sakums("Kāds skaitlis slēpjas tukšajā rūtiņā?",
           zimejums=restis([[200, 250, 300, None, 400]],
                           "virkne ar soli 50"),
           paraksts="Katrs nākamais ir par 50 lielāks.",
           fakti=["Virknes solis ir starpība starp diviem blakus skaitļiem.",
                  "Soli atrod, atņemot vienu skaitli no nākamā."]),

    Doma("Vispirms atrodi soli",
         "Atņem vienu skaitli no nākamā - tas ir solis; tad pārbaudi to vēl "
         "vienā pārī.",
         soli=[
             "Atņem pirmo skaitli no otrā.",
             "Pārbaudi ar nākamo pāri - solim jābūt tam pašam.",
             "Pieskaiti soli pēdējam zināmajam skaitlim.",
             "Pārbaudi, vai virkne turpinās pareizi.",
         ],
         pieze="Ja divi pāri dod dažādus soļus, virknes noteikums nav "
               "saskaitīšana - varbūt tā ir reizināšana."),

    Paraugs("Kurš skaitlis trūkst?",
            uzd="Virkne: 200, 250, 300, ?, 400. Kurš skaitlis trūkst?",
            soli=[
                ("250 − 200 = 50",
                 "Solis ir 50."),
                ("300 − 250 = 50",
                 "Pārbaude: tas pats solis."),
                ("300 + 50 = 350",
                 "Trūkstošais skaitlis; pārbaude: 350 + 50 = 400."),
            ],
            atbilde="350"),

    Ievadi("Atrodi trūkstošo", [
        {"jaut": "200, 250, 300, ?, 400 - kurš skaitlis trūkst?",
         "atb": ["350"], "padoms": "Solis 50."},
        {"jaut": "100, 200, ?, 400 - kurš skaitlis trūkst?",
         "atb": ["300"], "padoms": "Solis 100."},
        {"jaut": "125, 150, 175, ? - kurš skaitlis ir nākamais?",
         "atb": ["200"], "padoms": "Solis 25."},
        {"jaut": "900, 800, 700, ? - kurš skaitlis ir nākamais?",
         "atb": ["600"], "padoms": "Solis −100."},
        {"jaut": "Kāds ir solis virknē 340, 360, 380?", "atb": ["20"],
         "padoms": "360 − 340."},
        {"jaut": "460, 470, 480, ? - kurš skaitlis ir nākamais?",
         "atb": ["490"], "padoms": "Solis 10."},
    ], pamats=4),

    Petijums("Izveido savu virkni",
             vajag="lapa un zīmulis",
             soli=[
                 "Izvēlies sākuma skaitli un soli.",
                 "Uzraksti sešus virknes locekļus.",
                 "Aizsedz vienu no tiem un iedod virkni klasesbiedram.",
                 "Pārbaudi, vai viņš atrada to pašu skaitli.",
             ],
             secinajums="Ja solis ir viens un tas pats visā virknē, "
                        "trūkstošo skaitli var atrast tikai viens."),

    Zimejums("Divas virknes",
             restis([[100, 200, 300, 400, 500],
                     [100, 125, 150, 175, 200]],
                    "solis 100 un solis 25"),
             paskaidro="Abas sākas ar 100, bet aug dažādi - tāpēc solis "
                       "vienmēr jāpārbauda.",
             ievads="Salīdzini abas rindas."),

    Varianti("Kāds ir solis?", [
        {"jaut": "Kāds ir solis virknē 150, 200, 250?",
         "opcijas": ["50", "100", "25", "150"],
         "pareizi": 0, "padoms": "200 − 150."},
        {"jaut": "Kurš skaitlis ir nākamais: 600, 550, 500?",
         "opcijas": ["450", "550", "400", "650"],
         "pareizi": 0, "padoms": "Solis −50."},
        {"jaut": "Kurš skaitlis trūkst: 210, ?, 230, 240?",
         "opcijas": ["220", "215", "225", "250"],
         "pareizi": 0, "padoms": "Solis 10."},
        {"jaut": "Kā pārbaudīt atrasto soli?",
         "opcijas": ["Vēl vienā skaitļu pārī", "Skaitot no gala",
                     "Reizinot", "Nekā"],
         "pareizi": 0, "padoms": "Solim jābūt vienam visā virknē."},
    ], pamats=4),

    Pasaule("Cik ilgi darbojas satelīts?",
            Ievadi("", [
                {"jaut": "Satelīts apriņķo Zemi ik pēc 90 minūtēm. Cik "
                         "minūtēs tas apriņķos 2 reizes?",
                 "atb": ["180"], "padoms": "2 · 90."},
                {"jaut": "Cik minūtēs tas apriņķos 4 reizes?",
                 "atb": ["360"], "padoms": "4 · 90."},
                {"jaut": "Cik apriņķojumu tas paveic 720 minūtēs?",
                 "atb": ["8"], "padoms": "720 : 90."},
                {"jaut": "Cik apriņķojumu tas paveic diennaktī (1440 min)?",
                 "atb": ["16"], "padoms": "1440 : 90."},
            ]),
            pavediens="kosmoss",
            konteksts="Satelīta apriņķojumi veido virkni ar soli 90 minūtes - "
                      "un tā turpinās gadiem.",
            kapec="Zinot soli, var pateikt, kad satelīts būs virs mājas."),

    Kopsavilkums([
        "Atrodu virknes soli.",
        "Ievietoju trūkstošos skaitļus virknē.",
        "Pārbaudu soli vairākos pāros.",
        "Pamatoju savu izvēli.",
    ]),

    Majas([
        "Uzraksti virkni ar soli 25 un aizsedz vienu locekli.",
        "Atrodi trūkstošo skaitli virknē 480, 490, ?, 510.",
        "Izveido virkni, kas iet dilstoši ar soli 50.",
    ]),
]
