# -*- coding: utf-8 -*-
"""7. klase, 62. stunda: «Ko var nolasīt no grafika?»

No lineāras funkcijas grafika nolasa vērtību dotam argumentam, argumentu
dotai vērtībai un krustpunktus ar asīm. Krustpunkts ar y asi ir (0; b),
ar x asi - tur, kur y = 0 (funkcijas nulle).
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, plakne)

TEMA = "Ko var nolasīt no grafika?"

MERKIS = ("Nolasīsim no grafika funkcijas vērtību, argumentu un "
          "krustpunktus ar asīm.")

_G = plakne(grafiki=[(-2, 4, "y = −2x + 4")],
            punkti=[(0, 4, "(0; 4)"), (2, 0, "(2; 0)")],
            no_x=-2, lidz_x=5, no_y=-4, lidz_y=6, solis=1)

SATURS = [
    Sakums("Kur grafiks šķērso asis?",
           zimejums=_G,
           paraksts="Ar y asi - (0; 4), ar x asi - (2; 0).",
           fakti=["Krustpunkts ar y asi: x = 0, tātad y = b.",
                  "Krustpunkts ar x asi: y = 0 - funkcijas nulle.",
                  "Šie divi punkti ir ērtākie grafika zīmēšanai."]),

    Doma("Krustpunkti ar asīm",
         "Lineāras funkcijas y = kx + b grafiks krusto y asi punktā (0; b). "
         "Krustpunktu ar x asi atrod, atrisinot kx + b = 0 - šo x sauc par "
         "funkcijas nulli.",
         soli=[
             "Vērtība argumentam: no x ass vertikāli līdz grafikam.",
             "Arguments vērtībai: no y ass horizontāli līdz grafikam.",
             "Ar y asi: ievieto x = 0.",
             "Ar x asi: ievieto y = 0 un atrod x.",
         ],
         pieze="Nolasot no grafika, rezultāts var būt aptuvens; aprēķinot "
               "pēc formulas - precīzs. Nolasīto pārbauda ar formulu."),

    Paraugs("Atrodi krustpunktus",
            uzd="Funkcija y = −2x + 4. Atrodi krustpunktus ar asīm.",
            soli=[
                ("Ar y asi: x = 0, y = 4", "Punkts (0; 4)."),
                ("Ar x asi: −2x + 4 = 0", "y = 0."),
                ("2x = 4, x = 2", "Punkts (2; 0)."),
            ],
            atbilde="(0; 4) un (2; 0)"),

    Ievadi("Nolasi un aprēķini", [
        {"jaut": "y = −2x + 4. Cik ir y, ja x = −1?",
         "atb": ["6"], "padoms": "2 + 4."},
        {"jaut": "y = −2x + 4. Kuram x vērtība ir −2?",
         "atb": ["3"], "padoms": "−2x = −6."},
        {"jaut": "y = 3x − 6. Funkcijas nulle x = ?",
         "atb": ["2"], "padoms": "3x = 6."},
        {"jaut": "y = 3x − 6. Krustpunkta ar y asi y = ?",
         "atb": ["−6", "-6"], "padoms": "x = 0."},
        {"jaut": "y = {1|2}x + 3. Funkcijas nulle x = ?",
         "atb": ["−6", "-6"], "padoms": "{1|2}x = −3."},
        {"jaut": "y = 5x. Kurā punktā grafiks krusto asis? Raksti x.",
         "atb": ["0"], "padoms": "Caur (0; 0)."},
    ], pamats=4),

    Varianti("Kas redzams grafikā?", [
        {"jaut": "Grafiks krusto y asi punktā (0; −3). Kāds ir b?",
         "opcijas": ["−3", "3", "0", "Nevar zināt"],
         "pareizi": 0,
         "padoms": "b = y, kad x = 0."},
        {"jaut": "Funkcijai y = 4 - cik krustpunktu ar x asi?",
         "opcijas": ["Neviena", "Viens", "Divi", "Bezgalīgi daudz"],
         "pareizi": 0,
         "padoms": "Horizontāla taisne virs x ass."},
        {"jaut": "No grafika nolasīja x ≈ 1,3. Kā pārbaudīt?",
         "opcijas": ["Ievietot formulā", "Nomērīt ar lineālu vēlreiz",
                     "Nav iespējams", "Uzminēt"],
         "pareizi": 0,
         "padoms": "Formula ir precīza."},
    ]),

    Pasaule("Kad akumulators būs tukšs?",
            Ievadi("", [
                {"jaut": "Dronam akumulators L = 100 − 4t (%, t - min). "
                         "Kad L = 0 (min)?",
                 "atb": ["25"], "padoms": "Funkcijas nulle."},
                {"jaut": "Drons jāatgriež, kad paliek 20 %. Pēc cik min?",
                 "atb": ["20"], "padoms": "100 − 4t = 20."},
                {"jaut": "Kāds ir krustpunkts ar L asi (%)?",
                 "atb": ["100"], "padoms": "t = 0."},
            ]),
            pavediens="tehnika",
            konteksts="Drona pults rāda, cik minūšu atlicis - tas ir "
                      "aprēķināts krustpunkts ar asi.",
            kapec="Funkcijas nulle ir brīdis, kad «beidzas»."),

    Zimejums("Drona akumulators",
             plakne(grafiki=[(-4, 100, "")], punkti=[(0, 100), (25, 0)],
                    no_x=0, lidz_x=30, no_y=0, lidz_y=100, solis=5,
                    solis_y=20, x_nos="min", y_nos="%"),
             paskaidro="Krustpunkti: (0; 100) un (25; 0)."),

    Kopsavilkums([
        "Nolasu vērtību un argumentu no grafika.",
        "Atrodu krustpunktu ar y asi: (0; b).",
        "Atrodu funkcijas nulli: kx + b = 0.",
        "Pārbaudu nolasīto ar formulu.",
    ]),

    Majas([
        "Atrodi krustpunktus ar asīm funkcijai y = −3x + 9.",
        "Uzzīmē grafiku, izmantojot tikai šos divus punktus.",
        "Izdomā situāciju, kur funkcijas nulle ir svarīga.",
    ]),
]
