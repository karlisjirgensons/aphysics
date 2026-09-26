# -*- coding: utf-8 -*-
"""9. klase, 104. stunda: «Kā atrisinājumus attēlot plaknē?»

Katrs pāris (x; y) ir punkts plaknē. Lineāra vienādojuma atrisinājumi
izkārtojas uz taisnes - un katrs taisnes punkts ir atrisinājums. Slīdnis
pievieno punktus, līdz redz taisni.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, plakne)

TEMA = "Kā atrisinājumus attēlot plaknē?"

MERKIS = ("Attēlosim vienādojuma atrisinājumus koordinātu plaknē un "
          "raksturosim iegūto līniju.")

_PUNKTI = [(0, 5, ""), (1, 4, ""), (2, 3, ""), (3, 2, ""), (4, 1, ""),
           (5, 0, ""), (-1, 6, "")]
_PLAKNE = dict(no_x=-2, lidz_x=7, no_y=-2, lidz_y=7)

SATURS = [
    Sakums("x + y = 5: kur ir visi atrisinājumi?",
           zimejums=plakne(grafiki=[(-1, 5, "x + y = 5")], punkti=_PUNKTI,
                           **_PLAKNE),
           paraksts="Visi pāri guļ uz vienas taisnes.",
           fakti=["Katrs atrisinājums - punkts plaknē.",
                  "Lineāra vienādojuma grafiks - taisne.",
                  "Punkts ārpus taisnes nav atrisinājums."]),

    Slidnis("Pievieno punktus", [
        {"v": "2 punkti", "teksts": "(0; 5) un (5; 0)",
         "zim": plakne(punkti=_PUNKTI[0:1] + _PUNKTI[5:6], **_PLAKNE)},
        {"v": "5 punkti", "teksts": "Vēl (1; 4), (2; 3), (3; 2)",
         "zim": plakne(punkti=_PUNKTI[:4] + _PUNKTI[5:6], **_PLAKNE)},
        {"v": "Taisne", "teksts": "Visi atrisinājumi - taisne y = −x + 5",
         "zim": plakne(grafiki=[(-1, 5, "x + y = 5")], punkti=_PUNKTI,
                       **_PLAKNE)},
    ]),

    Doma("Vienādojuma grafiks",
         "Vienādojuma ax + by = c (a un b nav abi 0) visu atrisinājumu kopa "
         "plaknē ir taisne.",
         soli=[
             "Atrodi divus atrisinājumus (ērti: x = 0 un y = 0).",
             "Atliec punktus plaknē.",
             "Novelc taisni caur tiem.",
             "Pārbaudi ar trešo punktu.",
         ],
         pieze="Punkti (0; {c|b}) un ({c|a}; 0) ir krustpunkti ar asīm."),

    Ievadi("Krustpunkti ar asīm", [
        {"jaut": "2x + 3y = 12: krustpunkts ar y asi (0; ?)", "atb": ["4"],
         "padoms": "x = 0: 3y = 12."},
        {"jaut": "2x + 3y = 12: krustpunkts ar x asi (?; 0)", "atb": ["6"],
         "padoms": "y = 0: 2x = 12."},
        {"jaut": "x − 2y = 4: krustpunkts ar y asi (0; ?)",
         "atb": ["−2", "-2"], "padoms": "−2y = 4."},
        {"jaut": "x − 2y = 4: krustpunkts ar x asi (?; 0)", "atb": ["4"],
         "padoms": "x = 4."},
    ]),

    Varianti("Vai punkts ir uz taisnes?", [
        {"jaut": "(2; 1) un 3x − 2y = 4",
         "opcijas": ["Jā", "Nē"], "jaukt": False,
         "pareizi": 0, "padoms": "6 − 2 = 4."},
        {"jaut": "(1; 1) un 3x − 2y = 4",
         "opcijas": ["Jā", "Nē"], "jaukt": False,
         "pareizi": 1, "padoms": "3 − 2 = 1."},
        {"jaut": "Kāda līnija ir x = 3 grafiks?",
         "opcijas": ["Vertikāla taisne", "Horizontāla taisne",
                     "Punkts", "Parabola"],
         "pareizi": 0, "padoms": "y var būt jebkurš."},
    ]),

    Pasaule("Budžets divām lietām",
            Ievadi("", [
                {"jaut": "Kinobiļete 6 €, kafejnīcas apmeklējums 4 €, mēnesī "
                         "tērē 24 €: 6x + 4y = 24. Ja kino neiet (x = 0), cik "
                         "reižu kafejnīcā?", "atb": ["6"], "padoms": "4y = 24."},
                {"jaut": "Ja kafejnīcā neiet, cik reižu kino?", "atb": ["4"],
                 "padoms": "6x = 24."},
                {"jaut": "Ja kino 2 reizes, cik reižu kafejnīcā?", "atb": ["3"],
                 "padoms": "12 + 4y = 24."},
            ]),
            pavediens="veikals",
            konteksts="Budžeta taisne rāda visas izvēles, kurās tērē tieši "
                      "24 €.",
            kapec="Krustpunkti ar asīm - «tikai viens» variants.",
            zimejums=plakne(grafiki=[(-1.5, 6, "6x + 4y = 24")],
                            punkti=[(0, 6, ""), (4, 0, ""), (2, 3, "")],
                            no_x=0, lidz_x=6, no_y=0, lidz_y=7,
                            x_nos="kino", y_nos="kafejnīca")),

    Kopsavilkums([
        "Attēloju atrisinājumus kā punktus plaknē.",
        "Zīmēju taisni pēc diviem punktiem.",
        "Atrodu krustpunktus ar asīm.",
    ]),

    Majas([
        "Uzzīmē 3x + y = 6 grafiku ar krustpunktiem ar asīm.",
        "Pārbaudi, vai (1; 3) un (2; 1) ir uz taisnes.",
        "Uzzīmē savu budžeta taisni divām lietām.",
    ]),
]
