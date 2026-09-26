# -*- coding: utf-8 -*-
"""2. klase, 167. stunda: «Cik daudz jau protu?»

Tēmas un reizināšanas bloka noslēgums: jaukti uzdevumi ar visām četrām
darbībām - saskaitīšana un atņemšana 100 apjomā, reizināšana un dalīšana ar
2, 3, 4, 5, darbību secība un divu soļu uzdevumi.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti)

TEMA = "Cik daudz jau protu?"

MERKIS = ("Šodien patstāvīgi risināsim jauktus uzdevumus ar visām četrām "
          "darbībām.")

SATURS = [
    Sakums("Visas četras darbības - vai tu tās jau proti?",
           fakti=["+ un −: līdz 100.",
                  "· un :: ar 2, 3, 4, 5.",
                  "Secība: iekavas, · un :, tad + un −."]),

    Doma("Kā risināt jauktus uzdevumus",
         "Izlasi, izvēlies darbību, aprēķini, pārbaudi.",
         soli=[
             "Nosaki, kura darbība vajadzīga.",
             "Ja ir vairākas - ievēro secību.",
             "Aprēķini.",
             "Pārbaudi ar pretējo darbību.",
         ]),

    Ievadi("Jaukti piemēri", [
        {"jaut": "47 + 36 = ?", "atb": ["83"], "padoms": "70 + 13."},
        {"jaut": "82 − 45 = ?", "atb": ["37"], "padoms": "12 − 5, 7 − 4."},
        {"jaut": "7 · 4 = ?", "atb": ["28"], "padoms": "14, 28."},
        {"jaut": "45 : 5 = ?", "atb": ["9"], "padoms": "5 · 9."},
        {"jaut": "20 + 3 · 5 = ?", "atb": ["35"], "padoms": "20 + 15."},
        {"jaut": "(20 + 3) · 2 = ?", "atb": ["46"], "padoms": "23 · 2."},
        {"jaut": "60 − 24 : 4 = ?", "atb": ["54"], "padoms": "60 − 6."},
        {"jaut": "9 · 3 − 7 = ?", "atb": ["20"], "padoms": "27 − 7."},
    ], pamats=6),

    Varianti("Kura darbība?", [
        {"jaut": "«5 dārzi, katrā 4 koki. Cik koku?»",
         "opcijas": ["5 · 4", "5 + 4", "20 : 4"], "pareizi": 0,
         "padoms": "Vienādas grupas."},
        {"jaut": "«32 bērni sadalās 4 grupās. Cik katrā?»",
         "opcijas": ["32 : 4", "32 − 4", "32 · 4"], "pareizi": 0,
         "padoms": "Dalīšana."},
        {"jaut": "«Bija 50 €, iztērēja 18 €.»",
         "opcijas": ["50 − 18", "50 : 18", "50 + 18"], "pareizi": 0,
         "padoms": "Iztērēja - mīnus."},
    ]),

    Pasaule("Klases gada noslēguma pikniks",
            Ievadi("", [
                {"jaut": "Piknikā 24 bērni. Pa 4 pie katras segas. Cik "
                         "segu?", "atb": ["6"], "padoms": "24 : 4."},
                {"jaut": "Katram bērnam 2 pīrādziņi. Cik pīrādziņu?",
                 "atb": ["48"], "padoms": "24 · 2."},
                {"jaut": "Sulas pakas pa 5. Nopirka 6 pakas. Vai pietiks 24 "
                         "bērniem? Cik paliks pāri?", "atb": ["6"],
                 "padoms": "30 − 24."},
            ]),
            pavediens="skola",
            konteksts="Gada beigās klase dodas piknikā uz parku.",
            kapec="Visas četras darbības vienā dienā."),

    Kopsavilkums([
        "Risinu uzdevumus ar visām četrām darbībām.",
        "Ievēroju darbību secību.",
        "Pārbaudu atbildes.",
    ]),

    Majas([
        "Izdomā 4 uzdevumus - katram savu darbību.",
        "Atrisini tos.",
        "Lai mājinieks pārbauda.",
    ]),
]
