# -*- coding: utf-8 -*-
"""7. klase, 60. stunda: «Kā izskatās y = 2 grafiks?»

Funkcija y = b ar k = 0 ir nemainīga: jebkuram argumentam vērtība ir tā
pati. Tās grafiks ir horizontāla taisne. Stunda to atklāj ar abonementu,
kas nemainās neatkarīgi no lietošanas.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, plakne, restis)

TEMA = "Kā izskatās y = 2 grafiks?"

MERKIS = ("Zīmēsim grafikus funkcijām ar nemainīgu vērtību un formulēsim "
          "vispārinājumu.")

SATURS = [
    Sakums("Neierobežots internets: 15 € mēnesī",
           zimejums=plakne(grafiki=[(0, 15, "S = 15")],
                           no_x=0, lidz_x=50, no_y=0, lidz_y=25, solis=10,
                           solis_y=5, x_nos="GB", y_nos="€"),
           paraksts="Neatkarīgi no GB - vienmēr 15 €.",
           fakti=["Patērē 1 GB vai 50 GB - summa tā pati.",
                  "Grafiks ir horizontāla taisne.",
                  "Tā ir lineāra funkcija ar k = 0."]),

    Doma("y = b - horizontāla taisne",
         "Funkcijai y = b visiem argumentiem ir viena un tā pati vērtība b. "
         "Tās grafiks ir taisne, kas paralēla x asij un krusto y asi punktā "
         "(0; b).",
         soli=[
             "Izveido tabulu: jebkuram x vērtība ir b.",
             "Visi punkti ir vienā augstumā.",
             "Novelc horizontālu taisni caur (0; b).",
             "y = 0 ir pati x ass.",
         ],
         pieze="Nejauc ar x = 2: tā ir vertikāla taisne, un tā nav "
               "funkcija (sk. 55. stundu)."),

    Zimejums("y = 2, y = 0 un y = −3",
             plakne(grafiki=[(0, 2, "y = 2"), (0, -3, "y = −3")],
                    no_x=-4, lidz_x=4, no_y=-4, lidz_y=4, solis=1),
             paskaidro="y = 0 sakrīt ar x asi."),

    Paraugs("Tabula un grafiks",
            uzd="Aizpildi tabulu funkcijai y = −3 un apraksti grafiku.",
            soli=[
                ("x = −2; 0; 5 - y = −3; −3; −3", "Vērtība nemainās."),
                ("Punkti (−2; −3), (0; −3), (5; −3)", "Vienā augstumā."),
                ("Horizontāla taisne 3 vienības zem x ass",
                 "Paralēla x asij."),
            ],
            atbilde="Horizontāla taisne caur (0; −3)."),

    Zimejums("Tabula y = −3",
             restis([["x", "−2", "0", "5", "100"],
                     ["y", "−3", "−3", "−3", "−3"]]),
             paskaidro="Arguments mainās - vērtība nē."),

    Varianti("Atpazīsti", [
        {"jaut": "Kurai funkcijai grafiks ir horizontāla taisne?",
         "opcijas": ["y = 7", "y = 7x", "x = 7", "y = x + 7"],
         "pareizi": 0,
         "padoms": "k = 0."},
        {"jaut": "Kurš punkts ir uz y = −1 grafika?",
         "opcijas": ["(100; −1)", "(−1; 100)", "(0; 1)", "(−1; 0)"],
         "pareizi": 0,
         "padoms": "y jābūt −1."},
        {"jaut": "Kāds ir k funkcijai y = 4?",
         "opcijas": ["0", "4", "1", "Nav k"],
         "pareizi": 0,
         "padoms": "y = 0 · x + 4."},
        {"jaut": "Kāda ir funkcijas y = 4 vērtību kopa?",
         "opcijas": ["{4}", "Visi skaitļi", "y ≥ 4", "∅"],
         "pareizi": 0,
         "padoms": "Tikai 4."},
    ], pamats=4),

    Ievadi("Aprēķini", [
        {"jaut": "f(x) = 6. Cik ir f(−100)?",
         "atb": ["6"], "padoms": "Vienmēr 6."},
        {"jaut": "Horizontāla taisne iet caur (3; −5). Cik ir b?",
         "atb": ["−5", "-5"], "padoms": "y = −5."},
        {"jaut": "Cik krustpunktu ir y = 2 un y = −3 grafikiem?",
         "atb": ["0"], "padoms": "Paralēlas."},
        {"jaut": "Cik krustpunktu ir y = 2 un y = x grafikiem?",
         "atb": ["1"], "padoms": "Punktā (2; 2)."},
    ]),

    Pasaule("Kurš tarifs izdevīgāks?",
            Ievadi("", [
                {"jaut": "A: 15 € mēnesī neierobežoti. B: 1,5 € par GB. "
                         "Cik € maksā 8 GB ar B?",
                 "atb": ["12"], "padoms": "1,5 · 8."},
                {"jaut": "Pie cik GB abi tarifi maksā vienādi?",
                 "atb": ["10"], "padoms": "15 : 1,5."},
                {"jaut": "Tu patērē 20 GB. Kurš izdevīgāks - «A» vai «B»?",
                 "atb": ["A"], "padoms": "B: 30 € > 15 €.",
                 "tastatura": "text"},
            ]),
            pavediens="dati",
            konteksts="Horizontāla taisne (abonements) un slīpa taisne "
                      "(maksa par GB) krustojas - tur tarifi vienādi.",
            kapec="Salīdzinot tarifus, krustpunkts ir robeža."),

    Kopsavilkums([
        "Zinu, ka y = b grafiks ir horizontāla taisne.",
        "Zinu, ka tā ir lineāra funkcija ar k = 0.",
        "Atšķiru y = b no x = a.",
        "Salīdzinu nemainīgu un mainīgu tarifu.",
    ]),

    Majas([
        "Uzzīmē y = 3, y = −1 un y = 0 vienā plaknē.",
        "Atrodi dzīvē fiksētu maksu un uzzīmē tās grafiku.",
        "Kur krustojas y = 4 un y = 2x?",
    ]),
]
