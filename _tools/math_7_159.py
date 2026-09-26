# -*- coding: utf-8 -*-
"""7. klase, 159. stunda: «Kā atrisināt grafiski?»

Nevienādību f(x) > g(x) atrisina grafiski: uzzīmē abas funkcijas un nolasa,
kur viens grafiks ir virs otra. Robeža ir krustpunkta x. Tā pati ideja,
ko lietojām tarifu salīdzināšanā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, plakne, taisne)

TEMA = "Kā atrisināt grafiski?"

MERKIS = ("Atrisināsim nevienādību grafiski, abas puses attēlojot kā "
          "funkciju grafikus.")

_G = plakne(grafiki=[(2, -1, "y = 2x − 1"), (-1, 5, "y = 5 − x")],
            punkti=[(2, 3, "(2; 3)")],
            no_x=-2, lidz_x=6, no_y=-3, lidz_y=8, solis=1)

SATURS = [
    Sakums("Kur violetā taisne ir virs dzintara?",
           zimejums=_G,
           paraksts="2x − 1 > 5 − x, kad x > 2.",
           fakti=["Pa labi no krustpunkta violetā ir augstāk.",
                  "Pa kreisi - zemāk.",
                  "Krustpunkta x = 2 ir robeža."]),

    Doma("Virs vai zem",
         "Lai grafiski atrisinātu f(x) > g(x), uzzīmē y = f(x) un y = g(x). "
         "Atrisinājumi ir tie x, kuriem f grafiks ir virs g grafika. Robeža ir "
         "krustpunkta x koordināta.",
         soli=[
             "Uzzīmē abus grafikus.",
             "Atrodi krustpunktu.",
             "Nosaki, kurā pusē f ir virs g.",
             "Robežu ieskaita, ja zīme ≥ vai ≤.",
         ],
         pieze="Nevienādība f(x) > 0: kur grafiks ir virs x ass (63. stunda)."),

    Paraugs("Nolasi",
            uzd="Atrisini grafiski 2x − 1 > 5 − x.",
            soli=[
                ("Krustpunkts (2; 3)", "Nolasa."),
                ("Pa labi no x = 2: 2x − 1 augstāk", "Pārbaude x = 3: 5 > 2."),
                ("x > 2", "Robeža neieskaitīta."),
            ],
            atbilde="x ∈ (2; +∞)"),

    Zimejums("Atbilde uz taisnes",
             taisne(-2, 6, 1, intervali=[(2, None, False, False)]),
             paskaidro="Tukšs punkts pie 2."),

    Varianti("Nolasi no sākuma grafika", [
        {"jaut": "2x − 1 < 5 − x, kad...",
         "opcijas": ["x < 2", "x > 2", "x = 2", "visiem x"],
         "pareizi": 0, "padoms": "Violetā zemāk."},
        {"jaut": "2x − 1 ≥ 5 − x, kad...",
         "opcijas": ["x ≥ 2", "x > 2", "x ≤ 2", "x < 2"],
         "pareizi": 0, "padoms": "Arī krustpunktā."},
        {"jaut": "5 − x > 0, kad...",
         "opcijas": ["x < 5", "x > 5", "x < 0", "x > 0"],
         "pareizi": 0, "padoms": "Virs x ass."},
    ]),

    Ievadi("Aprēķini pārbaudei", [
        {"jaut": "Pārbaudi algebriski: 2x − 1 > 5 − x ⇒ 3x > 6 ⇒ x > ?",
         "atb": ["2"], "padoms": "6 : 3."},
        {"jaut": "Grafiki y = x + 1 un y = 7 − x krustojas pie x = ?",
         "atb": ["3"], "padoms": "2x = 6."},
        {"jaut": "Kad x + 1 ≤ 7 − x? x ≤ ?",
         "atb": ["3"], "padoms": "Pa kreisi no krustpunkta."},
    ]),

    Pasaule("Elektroauto vai benzīna auto?",
            Ievadi("", [
                {"jaut": "Elektroauto: 8000 € + 0,03 € par km. Benzīna: "
                         "0,08 € par km (auto jau ir). Pie cik km izmaksas "
                         "vienādas?",
                 "atb": ["160000"], "padoms": "0,05x = 8000."},
                {"jaut": "Ja brauc 20 000 km gadā - pēc cik gadiem "
                         "elektroauto atmaksājas?",
                 "atb": ["8"], "padoms": "160 000 : 20 000."},
                {"jaut": "Ja brauc 40 000 km gadā - pēc cik gadiem?",
                 "atb": ["4"], "padoms": "160 000 : 40 000."},
            ]),
            pavediens="planeta",
            konteksts="Atmaksāšanās punkts ir grafiku krustpunkts; pēc tā "
                      "elektroauto kļūst izdevīgāks.",
            kapec="Nevienādība - kad viens ir lētāks par otru."),

    Kopsavilkums([
        "Attēloju abas nevienādības puses kā grafikus.",
        "Nolasu, kur viens grafiks ir virs otra.",
        "Krustpunkta x ir robeža.",
        "Pārbaudu algebriski.",
    ]),

    Majas([
        "Atrisini grafiski: x + 2 ≥ 2x − 1.",
        "Pārbaudi algebriski.",
        "Izdomā situāciju ar atmaksāšanās punktu.",
    ]),
]
