# -*- coding: utf-8 -*-
"""2. klase, 134. stunda: «Cik gara ir otra sloksnīte?»

Tēmas noslēgums: situāciju uzdevumi, kuros viens lielums ir 2 reizes lielāks
vai mazāks nekā otrs, un reizēm jāatrod arī abu summa. Sloksņu zīmējums
izvēlas darbību.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, sloksnes)

TEMA = "Cik gara ir otra sloksnīte?"

MERKIS = ("Šodien risināsim situāciju uzdevumus, kuros viens lielums ir "
          "2 reizes lielāks vai mazāks nekā otrs.")

SATURS = [
    Sakums("Zila lente 8 cm, sarkana 2 reizes garāka. Cik garas abas "
           "kopā?",
           zimejums=sloksnes([("zila", 8, "8 cm"), ("sarkana", 16, "?")]),
           paraksts="Sarkanā - divas zilās.",
           fakti=["Sarkanā: 8 · 2 = 16 cm.",
                  "Kopā: 8 + 16 = 24 cm.",
                  "Divi soļi: vispirms reizes, tad kopā."]),

    Doma("Uzzīmē un rēķini",
         "Zīmējumā redz, vai reizināt, dalīt vai saskaitīt.",
         soli=[
             "Uzzīmē zināmo sloksni.",
             "2 reizes garāka - divas tādas; 2 reizes īsāka - puse.",
             "Aprēķini otru sloksni.",
             "Ja jautā «kopā» - saskaiti abas.",
         ]),

    Paraugs("2 reizes īsāka",
            uzd="Virve 18 m, aukla 2 reizes īsāka. Cik gara aukla?",
            soli=[("18 : 2 = 9", "Īsāka 2 reizes - dala."),
                  ("9 m", "Pārbaude: 9 · 2 = 18.")],
            atbilde="9 m"),

    Ievadi("Rēķini", [
        {"jaut": "Zīmulis 7 cm, pildspalva 2 reizes garāka. Cik gara "
                 "pildspalva?", "atb": ["14"], "mers": "cm",
         "padoms": "7 · 2."},
        {"jaut": "Galds 80 cm, sols 2 reizes zemāks. Cik augsts sols?",
         "atb": ["40"], "mers": "cm", "padoms": "80 : 2."},
        {"jaut": "Mārtiņam 9 uzlīmes, Annai 2 reizes vairāk. Cik abiem "
                 "kopā?", "atb": ["27"], "padoms": "18 + 9."},
        {"jaut": "Suns sver 20 kg, kucēns 2 reizes vieglāks. Cik sver "
                 "kucēns?", "atb": ["10"], "mers": "kg",
         "padoms": "20 : 2."},
        {"jaut": "Upe 30 m plata, strauts 2 reizes šaurāks. Cik plats "
                 "strauts?", "atb": ["15"], "mers": "m", "padoms": "30 : 2."},
        {"jaut": "Dēlis 10 dm, otrs 2 reizes garāks. Cik abi kopā?",
         "atb": ["30"], "mers": "dm", "padoms": "10 + 20."},
    ], pamats=4),

    Varianti("Kura darbība?", [
        {"jaut": "«Grāmata 2 reizes biezāka nekā burtnīca (6 mm).»",
         "opcijas": ["6 · 2", "6 : 2", "6 + 2"], "pareizi": 0,
         "padoms": "Biezāka - vairāk."},
        {"jaut": "«Kaķēns 2 reizes vieglāks nekā kaķe (4 kg).»",
         "opcijas": ["4 : 2", "4 · 2", "4 − 2"], "pareizi": 0,
         "padoms": "Vieglāks - mazāk, reizes - dala."},
    ]),

    Pasaule("Sniegavīrs",
            Ievadi("", [
                {"jaut": "Apakšējā bumba 60 cm augsta, vidējā 2 reizes "
                         "mazāka. Cik augsta vidējā?", "atb": ["30"],
                 "mers": "cm", "padoms": "60 : 2."},
                {"jaut": "Galva vēl 2 reizes mazāka nekā vidējā. Cik augsta?",
                 "atb": ["15"], "mers": "cm", "padoms": "30 : 2."},
                {"jaut": "Cik augsts viss sniegavīrs?", "atb": ["105"],
                 "mers": "cm", "padoms": "60 + 30 + 15."},
            ]),
            pavediens="daba",
            konteksts="Ziemā pagalmā ceļ sniegavīru no trim bumbām.",
            kapec="Katra bumba ir 2 reizes mazāka nekā apakšējā."),

    Kopsavilkums([
        "Risinu uzdevumus ar «2 reizes lielāks / mazāks».",
        "Zīmēju sloksnes, lai izvēlētos darbību.",
        "Atrodu arī abu lielumu summu.",
    ]),

    Majas([
        "Atrodi divus priekšmetus, kur viens 2 reizes garāks.",
        "Izmēri un pārbaudi.",
        "Izdomā uzdevumu ar tiem mājiniekam.",
    ]),
]
