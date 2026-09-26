# -*- coding: utf-8 -*-
"""7. klase, 134. stunda: «Kā atrisināt grafiski?»

Vienādojuma abas puses var uzskatīt par funkcijām: y = kreisā puse un
y = labā puse. Sakne ir krustpunkta x koordināta. Grafiski redz arī to, ka
paralēlām taisnēm krustpunkta nav - vienādojumam nav sakņu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, plakne)

TEMA = "Kā atrisināt grafiski?"

MERKIS = ("Atrisināsim vienādojumu grafiski, abas puses attēlojot kā "
          "funkcijas.")

SATURS = [
    Sakums("2x − 1 = x + 2: kur taisnes satiekas?",
           zimejums=plakne(grafiki=[(2, -1, "y = 2x − 1"),
                                    (1, 2, "y = x + 2")],
                           punkti=[(3, 5, "(3; 5)")],
                           no_x=-2, lidz_x=6, no_y=-3, lidz_y=8, solis=1),
           paraksts="Krustpunkts (3; 5): sakne x = 3.",
           fakti=["Katra puse - savs grafiks.",
                  "Kur grafiki krustojas, puses ir vienādas.",
                  "Krustpunkta x ir sakne."]),

    Doma("Sakne = krustpunkta x",
         "Lai grafiski atrisinātu vienādojumu f(x) = g(x), uzzīmē abu "
         "funkciju grafikus vienā plaknē. Krustpunktu x koordinātas ir "
         "vienādojuma saknes.",
         soli=[
             "Kreiso pusi apzīmē y = f(x), labo - y = g(x).",
             "Uzzīmē abus grafikus.",
             "Nolasi krustpunkta x.",
             "Pārbaudi, ievietojot vienādojumā (grafiks ir aptuvens).",
         ],
         pieze="Paralēlas taisnes nekrustojas - sakņu nav. Sakrītošas - "
               "bezgalīgi daudz sakņu."),

    Paraugs("Grafiski",
            uzd="Atrisini grafiski 3 − x = 2x − 3.",
            soli=[
                ("y = 3 − x: punkti (0; 3), (3; 0)", "Pirmā taisne."),
                ("y = 2x − 3: punkti (0; −3), (2; 1)", "Otrā."),
                ("Krustpunkts (2; 1)", "Nolasa."),
                ("Pārbaude: 3 − 2 = 1, 4 − 3 = 1", "Sakrīt."),
            ],
            atbilde="x = 2"),

    Zimejums("y = 3 − x un y = 2x − 3",
             plakne(grafiki=[(-1, 3, "y = 3 − x"), (2, -3, "y = 2x − 3")],
                    punkti=[(2, 1, "(2; 1)")],
                    no_x=-2, lidz_x=5, no_y=-4, lidz_y=5, solis=1),
             paskaidro="Krustpunkts x = 2."),

    Varianti("Cik sakņu?", [
        {"jaut": "Taisnes y = 2x + 1 un y = 2x − 3",
         "opcijas": ["Neviena - paralēlas", "Viena", "Divas",
                     "Bezgalīgi daudz"],
         "pareizi": 0, "padoms": "Vienāds k."},
        {"jaut": "Taisnes y = x + 1 un y = −x + 1",
         "opcijas": ["Viena", "Neviena", "Divas", "Bezgalīgi daudz"],
         "pareizi": 0, "padoms": "Krustojas (0; 1)."},
        {"jaut": "2(x + 1) = 2x + 2",
         "opcijas": ["Bezgalīgi daudz - taisnes sakrīt", "Viena",
                     "Neviena", "Divas"],
         "pareizi": 0, "padoms": "Viena un tā pati taisne."},
    ]),

    Ievadi("Nolasi sakni", [
        {"jaut": "Sākuma grafikā: sakne 2x − 1 = x + 2?",
         "atb": ["3"], "padoms": "Krustpunkta x."},
        {"jaut": "Grafiki y = x un y = 4 krustojas punktā ar x = ?",
         "atb": ["4"], "padoms": "x = 4."},
        {"jaut": "y = 2x un y = 6 − x. Sakne?",
         "atb": ["2"], "padoms": "2x = 6 − x."},
    ]),

    Pasaule("Kurš tarifs - grafiski",
            Ievadi("", [
                {"jaut": "Tarifs A: 10 + 2n, tarifs B: 4n (€, n - reizes). "
                         "Pie kāda n tie vienādi?",
                 "atb": ["5"], "padoms": "Krustpunkts: 10 + 2n = 4n."},
                {"jaut": "Cik € tad maksā abi?",
                 "atb": ["20"], "padoms": "4 · 5."},
                {"jaut": "Pie n = 8 lētāks ir «A» vai «B»?",
                 "atb": ["A"], "padoms": "26 < 32.",
                 "tastatura": "text"},
            ]),
            pavediens="veikals",
            konteksts="Tarifu salīdzināšana ir vienādojuma atrisināšana - "
                      "grafiski redz arī, kurš lētāks pirms un pēc.",
            kapec="Krustpunkts ir robeža."),

    Kopsavilkums([
        "Attēloju abas vienādojuma puses kā funkcijas.",
        "Nolasu sakni kā krustpunkta x.",
        "Pārbaudu sakni vienādojumā.",
        "Atpazīstu gadījumus bez saknēm un ar bezgalīgi daudzām.",
    ]),

    Majas([
        "Atrisini grafiski: x + 1 = 7 − x.",
        "Pārbaudi ar aprēķinu.",
        "Uzzīmē vienādojumu bez saknēm.",
    ]),
]
