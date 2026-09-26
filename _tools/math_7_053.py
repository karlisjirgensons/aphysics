# -*- coding: utf-8 -*-
"""7. klase, 53. stunda: «Kas ir arguments un funkcijas vērtība?»

Neatkarīgo mainīgo x funkcijā sauc par argumentu, bet y - par funkcijas
vērtību. No grafika nolasa abos virzienos: argumentam atrod vērtību un
vērtībai - argumentu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, plakne)

TEMA = "Kas ir arguments un funkcijas vērtība?"

MERKIS = ("Lietosim jēdzienus arguments un funkcijas vērtība, nolasot "
          "informāciju no grafika.")

_TEMP = [(0, -2), (3, -4), (6, -3), (9, 1), (12, 4), (15, 5), (18, 2),
         (21, -1), (24, -2)]

SATURS = [
    Sakums("Diennakts temperatūra martā",
           zimejums=plakne(grafiki=[(_TEMP, "")],
                           no_x=0, lidz_x=24, no_y=-6, lidz_y=6, solis=3,
                           solis_y=1.5, x_nos="h", y_nos="°C"),
           paraksts="Katrai stundai - viena temperatūra.",
           fakti=["Laiks ir arguments, temperatūra - funkcijas vērtība.",
                  "Pulksten 12 bija 4 °C.",
                  "0 °C bija divreiz - ap pl. 8 un ap pl. 20."]),

    Doma("Arguments → vērtība",
         "Funkcijā y = f(x) mainīgo x sauc par argumentu, y - par funkcijas "
         "vērtību. f(3) ir funkcijas vērtība, kad arguments ir 3.",
         soli=[
             "Lai atrastu vērtību: uz x ass atrodi argumentu.",
             "Ej vertikāli līdz grafikam, tad horizontāli līdz y asij.",
             "Lai atrastu argumentu: uz y ass atrodi vērtību.",
             "Ej horizontāli līdz grafikam (var būt vairāki punkti!), tad "
             "uz leju līdz x asij.",
         ],
         pieze="Vienai vērtībai var atbilst vairāki argumenti, bet vienam "
               "argumentam - tikai viena vērtība."),

    Paraugs("Nolasi grafikā",
            uzd="Sākuma grafikā: kāda ir temperatūra pl. 15? Kad bija −3 °C?",
            soli=[
                ("x = 15: y = 5", "Vērtība argumentam 15."),
                ("f(15) = 5 °C", "Pieraksts."),
                ("y = −3: x = 1,5 un x = 6",
                 "Grafiks šķērso −3 divreiz: krītot un kāpjot."),
                ("Starp 21 un 24 grafiks līdz −3 nenokrīt",
                 "Pārbauda visu grafiku, ne tikai pirmo vietu."),
            ],
            atbilde="5 °C; pl. 1.30 un pl. 6"),

    Ievadi("Nolasi no grafika", [
        {"jaut": "Kāda temperatūra bija pl. 3?",
         "atb": ["−4", "-4"], "padoms": "Punkts (3; −4)."},
        {"jaut": "Kāda bija augstākā temperatūra?",
         "atb": ["5"], "padoms": "Augstākais punkts."},
        {"jaut": "Cikos bija augstākā temperatūra?",
         "atb": ["15"], "padoms": "Tā punkta x."},
        {"jaut": "Kāda temperatūra bija pl. 18?",
         "atb": ["2"], "padoms": "Punkts (18; 2)."},
    ]),

    Zimejums("y = 2x − 1",
             plakne(grafiki=[(2, -1, "y = 2x − 1")],
                    punkti=[(3, 5, "(3; 5)")],
                    no_x=-2, lidz_x=5, no_y=-3, lidz_y=8, solis=1),
             paskaidro="f(3) = 2 · 3 − 1 = 5."),

    Ievadi("Aprēķini f(x)", [
        {"jaut": "f(x) = 2x − 1. Cik ir f(3)?",
         "atb": ["5"], "padoms": "2 · 3 − 1."},
        {"jaut": "f(x) = 2x − 1. Cik ir f(0)?",
         "atb": ["−1", "-1"], "padoms": "2 · 0 − 1."},
        {"jaut": "f(x) = 2x − 1. Kuram argumentam f(x) = 9?",
         "atb": ["5"], "padoms": "2x = 10."},
        {"jaut": "g(x) = 10 − x. Cik ir g(−2)?",
         "atb": ["12"], "padoms": "10 − (−2)."},
    ]),

    Varianti("Pieraksts", [
        {"jaut": "Ko nozīmē f(4) = 7?",
         "opcijas": ["Argumentam 4 funkcijas vērtība ir 7",
                     "Argumentam 7 vērtība ir 4",
                     "f reizināts ar 4 ir 7",
                     "Punkts (7; 4) ir uz grafika"],
         "pareizi": 0,
         "padoms": "Iekavās - arguments."},
        {"jaut": "Kurš punkts ir uz grafika, ja f(−2) = 3?",
         "opcijas": ["(−2; 3)", "(3; −2)", "(−2; −3)", "(2; 3)"],
         "pareizi": 0,
         "padoms": "(arguments; vērtība)."},
    ]),

    Pasaule("Nolasi sava telefona akumulatoru",
            Ievadi("", [
                {"jaut": "Telefona lādiņš L(t) = 100 − 8t (%), t - stundas. "
                         "Cik % pēc 5 h?",
                 "atb": ["60"], "padoms": "100 − 40."},
                {"jaut": "Kad lādiņš būs 20 %? (h)",
                 "atb": ["10"], "padoms": "8t = 80."},
                {"jaut": "Cik ir L(12,5)?",
                 "atb": ["0"], "padoms": "100 − 100."},
            ]),
            pavediens="dati",
            konteksts="Telefona iestatījumos ir akumulatora grafiks - tur "
                      "arguments ir laiks, vērtība - procenti.",
            kapec="Vērtību un argumentu nolasa abos virzienos."),

    Kopsavilkums([
        "Lietoju jēdzienus arguments un funkcijas vērtība.",
        "Nolasu no grafika vērtību dotam argumentam.",
        "Nolasu argumentu dotai vērtībai - arī vairākus.",
        "Aprēķinu f(a) pēc formulas.",
    ]),

    Majas([
        "Pieraksti temperatūru ik pēc 3 stundām un uzzīmē grafiku.",
        "f(x) = 3x + 2. Aprēķini f(−1), f(0), f(4).",
        "Atrodi argumentu, kuram f(x) = 20.",
    ]),
]
