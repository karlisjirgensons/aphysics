# -*- coding: utf-8 -*-
"""7. klase, 171. stunda: «Kā lasu un zīmēju funkcijas grafiku?»

Atkārto lineāro funkciju y = kx + b: ko nozīmē k un b, kā grafiku uzzīmē
pēc diviem punktiem un kā no grafika nolasa vērtības. Slīdnis groza k, lai
visas gada taisnes redz vienā vietā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, Zimejums, plakne)

TEMA = "Kā lasu un zīmēju funkcijas grafiku?"

MERKIS = ("Atkārtosim lineāras funkcijas grafiku, koeficientu k un b nozīmi "
          "un grafika īpašības.")


def _k(k, uzr):
    """Taisne ar b = 1 un doto k - blakus pelēkajai y = 1 salīdzinājumam."""
    return plakne(grafiki=[(0, 1, "y = 1"), (k, 1, uzr)], no_x=-4,
                  lidz_x=4, no_y=-4, lidz_y=5, solis=1)


SATURS = [
    Sakums("Divi skaitļi nosaka visu taisni",
           zimejums=plakne(grafiki=[(2, -1, "y = 2x − 1")],
                           punkti=[(0, -1), (2, 3)],
                           no_x=-3, lidz_x=4, no_y=-4, lidz_y=5, solis=1),
           paraksts="b = −1 - kur taisne krusto y asi; k = 2 - cik tā "
                    "kāpj uz katru soli pa labi.",
           fakti=["k > 0 - funkcija augoša, k < 0 - dilstoša.",
                  "Vienāds k - taisnes paralēlas.",
                  "Taisnei pietiek ar diviem punktiem."]),

    Doma("Kā uzzīmēt y = kx + b",
         "Lineāras funkcijas grafiks vienmēr ir taisne, tāpēc tabulā "
         "pietiek ar diviem punktiem - trešais ir pārbaude.",
         soli=[
             "Atzīmē punktu (0; b) uz y ass.",
             "No tā ej 1 pa labi un k uz augšu (ja k < 0 - uz leju).",
             "Ja k ir daļa {p|q}, ej q pa labi un p uz augšu.",
             "Novelc taisni caur abiem punktiem.",
             "Pārbaudi ar trešo punktu no tabulas.",
         ],
         pieze="Astotajā klasē grafiks kļūs liekts - parabola y = x². "
               "Lasīt to mācīsies tieši tāpat."),

    Slidnis("Maini k (b = 1)", [
        {"v": "k = −2", "teksts": "Strauji dilst", "zim": _k(-2, "y = −2x + 1")},
        {"v": "k = −1", "teksts": "Dilst", "zim": _k(-1, "y = −x + 1")},
        {"v": "k = 0", "teksts": "Paralēla x asij", "zim": _k(0, "")},
        {"v": "k = 1", "teksts": "Aug", "zim": _k(1, "y = x + 1")},
        {"v": "k = 2", "teksts": "Strauji aug", "zim": _k(2, "y = 2x + 1")},
    ], ievads="Visas taisnes iet caur (0; 1) - mainās tikai slīpums."),

    Paraugs("Zīmē pēc k un b",
            uzd="Uzzīmē y = −{1|2}x + 2 un atrod, kur tā krusto x asi.",
            soli=[
                ("b = 2 - punkts (0; 2)", "Sākums uz y ass."),
                ("k = −{1|2}: 2 pa labi, 1 uz leju", "Veseli soļi."),
                ("Otrs punkts (2; 1)", "No (0; 2)."),
                ("−{1|2}x + 2 = 0, x = 4", "Uz x ass y = 0."),
            ],
            atbilde="Taisne caur (0; 2) un (2; 1); krusto x asi (4; 0)"),

    Zimejums("Nolasi k un b",
             plakne(grafiki=[(-1, 3, "")], punkti=[(0, 3), (3, 0)],
                    no_x=-2, lidz_x=5, no_y=-2, lidz_y=5, solis=1),
             paskaidro="Taisne iet caur (0; 3) un (3; 0)."),

    Ievadi("Lasi un rēķini", [
        {"jaut": "Zīmējumā: kāds ir b?",
         "atb": ["3"], "padoms": "Krustpunkts ar y asi."},
        {"jaut": "Zīmējumā: kāds ir k?",
         "atb": ["−1", "-1"], "padoms": "3 pa labi, 3 uz leju."},
        {"jaut": "y = 3x − 5. Kāds ir y, ja x = 2?",
         "atb": ["1"], "padoms": "6 − 5."},
        {"jaut": "Kurā punktā y = −2x + 4 krusto x asi? x = ?",
         "atb": ["2"], "padoms": "−2x + 4 = 0."},
        {"jaut": "Vai punkts (3; 7) pieder grafikam y = 2x + 1?",
         "atb": ["jā", "ja"], "padoms": "2 · 3 + 1 = 7.",
         "tastatura": "text"},
        {"jaut": "Taisne iet caur (0; −1) un (2; 5). Kāds ir k?",
         "atb": ["3"], "padoms": "6 uz augšu uz 2 pa labi."},
    ], pamats=4),

    Varianti("Grafika īpašības", [
        {"jaut": "Funkcija y = −3x + 2 ir...",
         "opcijas": ["dilstoša", "augoša", "konstanta",
                     "nav lineāra"],
         "pareizi": 0, "padoms": "k < 0."},
        {"jaut": "Kuras taisnes ir paralēlas?",
         "opcijas": ["y = 2x + 1 un y = 2x − 3", "y = 2x + 1 un y = x + 1",
                     "y = 2x un y = −2x", "y = x + 3 un y = 3x"],
         "pareizi": 0, "padoms": "Vienāds k."},
        {"jaut": "Grafiks y = 5 ir...",
         "opcijas": ["paralēls x asij", "paralēls y asij",
                     "iet caur (0; 0)", "dilstošs"],
         "pareizi": 0, "padoms": "k = 0."},
        {"jaut": "k > 0 un b < 0. Kurā koordinātu ceturtdaļā taisne "
                 "neiet?",
         "opcijas": ["II", "I", "III", "IV"],
         "pareizi": 0, "padoms": "Aug un krusto y asi zem nulles."},
    ]),

    Pasaule("Taksometra cena",
            Ievadi("", [
                {"jaut": "Iekāpšana 2 €, katrs km 0,80 €. Cik eiro maksā "
                         "5 km?",
                 "atb": ["6"], "padoms": "2 + 0,8 · 5."},
                {"jaut": "Cik km var nobraukt par 10 €?",
                 "atb": ["10"], "padoms": "2 + 0,8x = 10."},
                {"jaut": "Kāds ir b šajā funkcijā?",
                 "atb": ["2"], "padoms": "Cena, kad vēl nav braukts."},
            ]),
            pavediens="celojums",
            konteksts="Cena y = 0,8x + 2 ir lineāra funkcija: b ir "
                      "iekāpšanas maksa, k - maksa par kilometru.",
            kapec="No grafika cenu nolasa bez rēķināšanas.",
            zimejums=plakne(grafiki=[(0.8, 2, "y = 0,8x + 2")],
                            punkti=[(5, 6), (10, 10)],
                            no_x=0, lidz_x=10, no_y=0, lidz_y=10, solis=1,
                            solis_y=2, x_nos="km", y_nos="€")),

    Kopsavilkums([
        "Zīmēju taisni pēc k un b vai pēc diviem punktiem.",
        "Nolasu k un b no grafika.",
        "Atrodu krustpunktu ar asīm.",
        "Pārbaudu, vai punkts pieder grafikam.",
    ]),

    Majas([
        "Uzzīmē y = 2x − 3 un y = −x + 3 vienā plaknē.",
        "Nolasi to krustpunktu un pārbaudi ar vienādojumu.",
        "Atrodi vienu reālu cenu (taksometrs, tarifs) un pieraksti tās "
        "funkciju.",
    ]),
]
