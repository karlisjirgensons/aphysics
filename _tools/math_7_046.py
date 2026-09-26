# -*- coding: utf-8 -*-
"""7. klase, 46. stunda: «Kā mainās ceļš vienmērīgā kustībā?»

Vienmērīgā kustībā ceļš ir tieši proporcionāls laikam: s = vt. Grafiks ir
taisne caur sākumpunktu, un ātrums ir tas, par cik ceļš pieaug vienā
laika vienībā. Stunda saista formulu, tabulu un grafiku.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Kustiba, Majas,
                         Paraugs, Pasaule, Sakums, Slidnis, Zimejums,
                         plakne, restis)

TEMA = "Kā mainās ceļš vienmērīgā kustībā?"

MERKIS = ("Attēlosim grafiski un pierakstīsim ar formulu sakarību starp "
          "laiku un ceļu.")


def _vilciens(t):
    """Grafiks līdz laikam t - lai slīdnī redz, kā līnija aug."""
    return plakne(grafiki=[([(0, 0), (t, 80 * t)], "")],
                  punkti=[(t, 80 * t)],
                  no_x=0, lidz_x=4, no_y=0, lidz_y=320, solis=1, solis_y=80,
                  x_nos="t, h", y_nos="s, km")


SATURS = [
    Sakums("Vilciens Rīga - Daugavpils",
           zimejums=_vilciens(3),
           paraksts="80 km/h: katrā stundā vēl 80 km.",
           fakti=["Vienmērīgā kustībā ātrums nemainās.",
                  "Tad ceļš katrā stundā pieaug par to pašu gabalu.",
                  "Grafiks ir taisne caur sākumpunktu."]),

    Doma("s = vt",
         "Vienmērīgā kustībā ar ātrumu v ceļu s laikā t aprēķina ar formulu "
         "s = vt. Ceļš ir tieši proporcionāls laikam, un grafiks ir taisne "
         "caur (0; 0).",
         soli=[
             "Nosaki ātrumu v - nemainīgo lielumu.",
             "Uzraksti formulu s = vt.",
             "Izveido tabulu dažiem laika brīžiem.",
             "Atzīmē punktus un savieno - laiks ir nepārtraukts.",
         ],
         pieze="Jo lielāks ātrums, jo stāvāka taisne: katrā stundā tā "
               "paceļas augstāk."),

    Slidnis("Laiks rit", [
        {"v": "t = 1 h", "teksts": "s = 80 · 1 = 80 (km)",
         "zim": _vilciens(1)},
        {"v": "t = 2 h", "teksts": "s = 80 · 2 = 160 (km)",
         "zim": _vilciens(2)},
        {"v": "t = 2,5 h", "teksts": "s = 80 · 2,5 = 200 (km)",
         "zim": _vilciens(2.5)},
        {"v": "t = 3 h", "teksts": "s = 80 · 3 = 240 (km)",
         "zim": _vilciens(3)},
    ], ievads="Spied soļus: punkts slīd pa taisni."),

    Paraugs("No grafika uz formulu",
            uzd="Riteņbraucējs 2 h nobrauca 36 km vienmērīgi. Uzraksti "
                "formulu un aprēķini ceļu pēc 3,5 h.",
            soli=[
                ("v = 36 : 2 = 18 (km/h)", "Ātrums."),
                ("s = 18t", "Formula."),
                ("s = 18 · 3,5 = 63 (km)", "Ievieto t = 3,5."),
            ],
            atbilde="s = 18t; 63 km"),

    Zimejums("Tabula riteņbraucējam",
             restis([["t, h", "0", "1", "2", "3"],
                     ["s, km", "0", "18", "36", "54"]]),
             paskaidro="Katrā stundā +18 km."),

    Ievadi("Aprēķini", [
        {"jaut": "v = 60 km/h. Cik km pēc 2,5 h?",
         "atb": ["150"], "padoms": "60 · 2,5."},
        {"jaut": "s = 18t. Pēc cik stundām s = 90 km?",
         "atb": ["5"], "padoms": "90 : 18."},
        {"jaut": "Gājējs 3 h noiet 15 km. Ātrums (km/h)?",
         "atb": ["5"], "padoms": "15 : 3."},
        {"jaut": "Grafiks iet caur (4; 100). Ātrums (km/h)?",
         "atb": ["25"], "padoms": "100 : 4."},
    ]),

    Pasaule("Kur ir vilciens?",
            Kustiba("", [
                {"jaut": "Vilciens brauc 80 km/h. Kur tas ir pēc 1,5 h?",
                 "atb": 120, "beigas": 240, "iedala": 20, "mers": "km",
                 "merkis": "vilciens", "objekts": "Vilciens",
                 "padoms": "80 · 1,5."},
                {"jaut": "Līdz Daugavpilij ir 230 km. Kur vilciens būs pēc "
                         "2 h 30 min?",
                 "atb": 200, "beigas": 240, "iedala": 20, "mers": "km",
                 "merkis": "vilciens", "objekts": "Vilciens",
                 "padoms": "2,5 h · 80."},
            ]),
            pavediens="celojums",
            konteksts="Vilcienu grafiki ir tieši s = vt aprēķini, tikai ar "
                      "pieturām.",
            kapec="Formula ļauj atrast vilcienu jebkurā brīdī."),

    Kopsavilkums([
        "Lietoju formulu s = vt.",
        "Veidoju tabulu un grafiku vienmērīgai kustībai.",
        "No grafika punkta aprēķinu ātrumu.",
        "Zinu, ka grafiks ir taisne caur sākumpunktu.",
    ]),

    Majas([
        "Izmēri, cik metru tu noej 1 minūtē, un uzraksti formulu.",
        "Uzzīmē sava ceļa uz skolu grafiku.",
        "Aprēķini, cik ilgi ietu līdz tuvākajai pilsētai.",
    ]),
]
