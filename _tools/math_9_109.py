# -*- coding: utf-8 -*-
"""9. klase, 109. stunda: «Kā atrisināt grafiski?»

Grafiskā metode: katru vienādojumu pārvērš par funkciju, uzzīmē abas
taisnes un nolasa krustpunktu. Stunda sākas ar diviem mobilo sakaru
tarifiem - kad tie maksā vienādi.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Slidnis, Varianti, paris, plakne)

TEMA = "Kā atrisināt grafiski?"

MERKIS = ("Atrisināsim lineāru vienādojumu sistēmu grafiski un nolasīsim "
          "krustpunktu.")

_T = "text"
_PLAKNE = dict(no_x=-2, lidz_x=6, no_y=-2, lidz_y=7)

SATURS = [
    Sakums("Kurš tarifs izdevīgāks?",
           zimejums=plakne(grafiki=[(0.5, 4, "A: 4 + 0,5x"),
                                    (1, 2, "B: 2 + x")],
                           punkti=[(4, 6, "(4; 6)")],
                           no_x=0, lidz_x=8, no_y=0, lidz_y=10,
                           x_nos="GB", y_nos="€"),
           paraksts="Pie 4 GB abi maksā 6 €; vairāk - izdevīgāks A.",
           fakti=["Katrs tarifs - taisne.",
                  "Krustpunkts - kur cenas vienādas.",
                  "Tas ir sistēmas y = 4 + 0,5x, y = 2 + x atrisinājums."]),

    Doma("Grafiskā metode",
         "Uzzīmē abu vienādojumu grafikus vienā plaknē; krustpunkta "
         "koordinātas ir sistēmas atrisinājums.",
         soli=[
             "Izsaki y katrā vienādojumā (vai atrodi 2 punktus).",
             "Uzzīmē abas taisnes precīzi (rūtiņu lapā).",
             "Nolasi krustpunktu (x; y).",
             "Pārbaudi pāri abos vienādojumos.",
         ]),

    Slidnis("Pa soļiem: x + y = 5, 2x − y = 1", [
        {"v": "1. taisne", "teksts": "y = −x + 5",
         "zim": plakne(grafiki=[(-1, 5, "y = −x + 5")], **_PLAKNE)},
        {"v": "2. taisne", "teksts": "y = 2x − 1",
         "zim": plakne(grafiki=[(-1, 5, "y = −x + 5"),
                                (2, -1, "y = 2x − 1")], **_PLAKNE)},
        {"v": "Krustpunkts", "teksts": "(2; 3) - pārbaude: 2 + 3 = 5, "
                                       "4 − 3 = 1 ✔",
         "zim": plakne(grafiki=[(-1, 5, "y = −x + 5"),
                                (2, -1, "y = 2x − 1")],
                       punkti=[(2, 3, "(2; 3)")], **_PLAKNE)},
    ]),

    Paraugs("Nolasi un pārbaudi",
            uzd="Atrisini grafiski: y = x + 1 un y = −2x + 4.",
            soli=[
                ("Taisnes krustojas punktā (1; 2)", "Nolasa no zīmējuma."),
                ("2 = 1 + 1 ✔; 2 = −2 + 4 ✔", "Pārbaude."),
            ],
            atbilde="(1; 2)"),

    Ievadi("Nolasi krustpunktu (sākuma zīmējums)", [
        {"jaut": "Tarifu krustpunkts: cik GB?", "atb": ["4"],
         "padoms": "x koordināta."},
        {"jaut": "Cik € tad maksā abi?", "atb": ["6"],
         "padoms": "y koordināta."},
        {"jaut": "Atrisini grafiski y = x un y = −x + 6", "atb": paris(3, 3),
         "tastatura": _T, "vieta": "(x; y)", "padoms": "x = −x + 6."},
    ]),

    Varianti("Kurš grafiks atbilst?", [
        {"jaut": "y = 3 ir...",
         "opcijas": ["horizontāla taisne", "vertikāla taisne",
                     "taisne caur (0; 0)", "punkts"],
         "pareizi": 0, "padoms": "y visur 3."},
        {"jaut": "Taisnes y = 2x + 1 un y = 2x − 3...",
         "opcijas": ["ir paralēlas", "krustojas (0; 1)",
                     "sakrīt", "krustojas (1; 3)"],
         "pareizi": 0, "padoms": "Vienāds slīpums."},
    ]),

    Pasaule("Mobilo datu tarifi",
            Ievadi("", [
                {"jaut": "Tarifs A: 5 € + 1 €/GB, tarifs B: 11 € bez limita. "
                         "Pie cik GB maksā vienādi?", "atb": ["6"],
                 "padoms": "5 + x = 11."},
                {"jaut": "Tev vajag 9 GB. Cik € ietaupa ar B?", "atb": ["3"],
                 "padoms": "14 − 11."},
            ]),
            pavediens="dati",
            konteksts="Operatori piedāvā tarifus ar maksu par GB un bez "
                      "limita.",
            kapec="Krustpunkts ir robeža, kur izdevīgums mainās.",
            zimejums=plakne(grafiki=[(1, 5, "A"), (0, 11, "B")],
                            punkti=[(6, 11, "(6; 11)")],
                            no_x=0, lidz_x=12, no_y=0, lidz_y=18, solis=2,
                            solis_y=2, x_nos="GB", y_nos="€")),

    Kopsavilkums([
        "Zīmēju abas taisnes vienā plaknē.",
        "Nolasu krustpunktu kā atrisinājumu.",
        "Pārbaudu to abos vienādojumos.",
    ]),

    Majas([
        "Atrisini grafiski: x + y = 4, x − y = 2.",
        "Atrisini grafiski: y = 2x − 3, y = −x + 3.",
        "Salīdzini divus reālus tarifus (telefons, sporta zāle).",
    ]),
]
