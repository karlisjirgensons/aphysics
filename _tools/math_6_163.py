# -*- coding: utf-8 -*-
"""6. klase, 163. stunda: «Kā uzdevumu pierakstīt matemātiski?»

Pēdējais mikrotemats pirms gada noslēguma. Teksta uzdevums jāpārvērš
izteiksmē - un tieši šis pāreja no vārdiem uz simboliem ir tas, ko eksāmenā
vērtē visvairāk.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kā uzdevumu pierakstīt matemātiski?"

MERKIS = ("Pārvērtīsim teksta uzdevumu izteiksmē vai vienādībā ar "
          "nezināmo.")

SATURS = [
    Sakums("No vārdiem uz zīmēm",
           zimejums=restis([["«no»", "«kopā»", "«par tik mazāk»", "«reižu»"],
                            ["·", "+", "−", "·"]]),
           paraksts="Katram vārdam tekstā atbilst viena darbība izteiksmē.",
           fakti=["Vārds «no» nozīmē reizināšanu.",
                  "«Par tik mazāk» nozīmē atņemšanu.",
                  "«Cik reižu» nozīmē dalīšanu."]),

    Doma("Pasvītro vārdus, kas nosauc darbības",
         "Teksta uzdevumu pārvērš izteiksmē, atrodot vārdus, kas nosauc "
         "darbības, un apzīmējot nezināmo ar burtu.",
         soli=[
             "Izlasi uzdevumu un pasvītro, ko meklē.",
             "Apzīmē nezināmo ar burtu un pieraksti, ko tas nozīmē.",
             "Atrodi vārdus, kas nosauc darbības.",
             "Pieraksti izteiksmi vai vienādību.",
             "Atrisini un pārbaudi, vai atbilde iederas tekstā.",
         ],
         pieze="Ja tekstā ir vairāki soļi, katram raksta savu rindu. Viena "
               "gara izteiksme ir ērta tikai tad, kad visi soļi jau ir "
               "skaidri."),

    Paraugs("No teksta uz izteiksmi",
            uzd="Klasē 24 skolēni. {3|4} no viņiem brauc ar autobusu, "
                "pārējie - kājām. Cik iet kājām?",
            soli=[
                ("Meklēju: cik skolēnu iet kājām",
                 "Pirmais solis."),
                ("{3|4} no 24 = 18",
                 "Vārds «no» nozīmē reizināšanu."),
                ("24 − 18 = 6",
                 "«Pārējie» nozīmē atņemšanu."),
                ("Pārbaude: 18 + 6 = 24",
                 "Visi skolēni saskaitīti."),
            ],
            atbilde="6 skolēni"),

    Ievadi("Pieraksti un izrēķini", [
        {"jaut": "Klasē 24 skolēni, {3|4} brauc ar autobusu. Cik tas ir?",
         "atb": ["18"], "padoms": "24 : 4 · 3."},
        {"jaut": "Cik skolēnu iet kājām?",
         "atb": ["6"], "padoms": "24 − 18."},
        {"jaut": "Cena 40 €, atlaide 25 %. Cik eiro ir atlaide?",
         "atb": ["10"], "padoms": "40 : 4."},
        {"jaut": "Cik eiro jāmaksā pēc atlaides?",
         "atb": ["30"], "padoms": "40 − 10."},
        {"jaut": "Ir 3,5 kg produkta, katrā maisiņā 0,5 kg. Cik maisiņu?",
         "atb": ["7"], "padoms": "3,5 : 0,5."},
        {"jaut": "Temperatūra no −5 °C pieaug par 12 grādiem. Cik grādu ir?",
         "atb": ["7"], "padoms": "−5 + 12."},
    ], pamats=4,
        ievads="Vispirms pasaki, ko meklē."),

    Varianti("Kura darbība te der?", [
        {"jaut": "«{2|3} no 30» nozīmē...",
         "opcijas": ["{2|3} · 30", "30 : {2|3}", "30 − {2|3}", "30 + {2|3}"],
         "pareizi": 0,
         "padoms": "Vārds «no»."},
        {"jaut": "«Cik reižu 0,5 ietilpst 4» nozīmē...",
         "opcijas": ["4 : 0,5", "4 · 0,5", "4 − 0,5", "0,5 : 4"],
         "pareizi": 0,
         "padoms": "«Cik reižu» - dalīšana."},
        {"jaut": "«Par 12 grādiem siltāks nekā −5» nozīmē...",
         "opcijas": ["−5 + 12", "−5 − 12", "12 − 5", "12 · (−5)"],
         "pareizi": 0,
         "padoms": "Siltāks - pieskaita."},
        {"jaut": "Ko obligāti pieraksta pie burta?",
         "opcijas": ["Ko tas nozīmē", "Atbildi",
                     "Uzdevuma numuru", "Neko"],
         "pareizi": 0,
         "padoms": "«x - skolēnu skaits»."},
    ], pamats=4),

    Pasaule("Cik maksās pasākums?",
            Ievadi("", [
                {"jaut": "25 skolēni, biļete 6 €. Cik eiro maksā biļetes?",
                 "atb": ["150"], "padoms": "25 · 6."},
                {"jaut": "Autobuss maksā 90 €. Cik eiro kopā?",
                 "atb": ["240"], "padoms": "150 + 90."},
                {"jaut": "Cik eiro jāmaksā vienam skolēnam?",
                 "atb": ["9,6", "9.6"], "padoms": "240 : 25."},
                {"jaut": "Ja skolēnu būtu 30, cik eiro maksātu viens?",
                 "atb": ["9"], "padoms": "(180 + 90) : 30."},
            ]),
            pavediens="skola",
            konteksts="Pasākuma budžets ir teksta uzdevums ar vairākiem "
                      "soļiem - un katram solim sava rinda.",
            kapec="Pareizs pieraksts pasaka, kurā secībā rēķināt."),

    Kopsavilkums([
        "Pārvēršu teksta uzdevumu izteiksmē.",
        "Apzīmēju nezināmo ar burtu un pierakstu, ko tas nozīmē.",
        "Atrodu vārdus, kas nosauc darbības.",
        "Pārbaudu, vai atbilde iederas tekstā.",
    ]),

    Majas([
        "Pieraksti ar izteiksmi: «{2|5} no 40 un vēl 7».",
        "Atrisini to.",
        "Izdomā savu uzdevumu ar diviem soļiem un pieraksti tā izteiksmi.",
    ]),
]
