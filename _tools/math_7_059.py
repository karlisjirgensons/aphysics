# -*- coding: utf-8 -*-
"""7. klase, 59. stunda: «Cik punktu vajag taisnei?»

Caur diviem punktiem iet tieši viena taisne, tāpēc lineāras funkcijas
grafikam pietiek ar diviem punktiem. Trešais ir pārbaude: ja tas nav uz
taisnes - kaut kur ir kļūda. Stunda iemāca izvēlēties ērtus punktus.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, plakne, restis)

TEMA = "Cik punktu vajag taisnei?"

MERKIS = ("Zīmēsim lineāras funkcijas grafiku pēc formulas, izvēloties "
          "punktu skaitu, un pamatosim izvēli.")

SATURS = [
    Sakums("Divi punkti, lineāls - gatavs",
           zimejums=plakne(grafiki=[(0.5, -1, "y = 0,5x − 1")],
                           punkti=[(0, -1, "(0; −1)"), (4, 1, "(4; 1)")],
                           no_x=-2, lidz_x=6, no_y=-3, lidz_y=3, solis=1),
           paraksts="x = 0 un x = 4 - abi dod veselus y.",
           fakti=["Caur diviem punktiem iet tieši viena taisne.",
                  "Trešais punkts ir drošības pārbaude."]),

    Doma("Divi punkti - un trešais pārbaudei",
         "Lineāras funkcijas grafiks ir taisne, tāpēc to nosaka divi punkti. "
         "Izvēlas argumentus, kuriem vērtības ir ērti aprēķināt un atzīmēt.",
         soli=[
             "Izvēlies x = 0: y = b - krustpunkts ar y asi.",
             "Izvēlies otru x, lai y ir vesels (ja k ir daļa - ņem saucēju).",
             "Aprēķini trešo punktu un pārbaudi, vai tas ir uz taisnes.",
             "Novelc taisni caur punktiem līdz plaknes malām.",
         ],
         pieze="Punktus labāk ņemt tālāk vienu no otra - tad taisne ir "
               "precīzāka."),

    Paraugs("Uzzīmē y = {2|3}x + 1",
            uzd="Izvēlies ērtus punktus funkcijai y = {2|3}x + 1.",
            soli=[
                ("x = 0: y = 1 - punkts (0; 1)", "b."),
                ("x = 3: y = 2 + 1 = 3 - punkts (3; 3)",
                 "3 ir saucējs - vesels y."),
                ("x = −3: y = −2 + 1 = −1 - punkts (−3; −1)", "Pārbaude."),
                ("Visi trīs uz vienas taisnes", "Grafiks pareizs."),
            ],
            atbilde="Punkti (0; 1), (3; 3), (−3; −1)"),

    Zimejums("y = {2|3}x + 1",
             plakne(grafiki=[(2 / 3.0, 1, "")],
                    punkti=[(-3, -1), (0, 1), (3, 3)],
                    no_x=-4, lidz_x=5, no_y=-2, lidz_y=4, solis=1),
             paskaidro="Argumenti −3; 0; 3 dod veselas vērtības."),

    Varianti("Kurš x ir ērtākais?", [
        {"jaut": "y = {1|4}x − 2. Kurš otrais x dod veselu y?",
         "opcijas": ["4", "1", "3", "5"],
         "pareizi": 0,
         "padoms": "Saucējs."},
        {"jaut": "Trešais punkts nav uz taisnes caur pirmajiem diviem. Ko "
                 "dara?",
         "opcijas": ["Pārrēķina visus trīs punktus",
                     "Zīmē līkni caur visiem trim",
                     "Izmet trešo", "Neko"],
         "pareizi": 0,
         "padoms": "Kaut kur ir kļūda."},
        {"jaut": "Cik punktu vajag parabolas y = x² grafikam?",
         "opcijas": ["Vairāk nekā divus", "Tieši divus", "Vienu",
                     "Trīs vienmēr pietiek"],
         "pareizi": 0,
         "padoms": "Tā nav taisne."},
    ]),

    Ievadi("Aprēķini punktus", [
        {"jaut": "y = 3x − 4. Cik ir y, ja x = 2?",
         "atb": ["2"], "padoms": "6 − 4."},
        {"jaut": "y = {1|2}x + 3. Cik ir y, ja x = −4?",
         "atb": ["1"], "padoms": "−2 + 3."},
        {"jaut": "y = −x + 5. Kurā punktā grafiks krusto y asi? Raksti y.",
         "atb": ["5"], "padoms": "x = 0."},
        {"jaut": "y = −x + 5. Kurā punktā grafiks krusto x asi? Raksti x.",
         "atb": ["5"], "padoms": "y = 0: x = 5."},
    ]),

    Pasaule("Ūdens tvertne",
            Ievadi("", [
                {"jaut": "Tvertnē 200 l, katru minūti izlej 8 l: "
                         "V = 200 − 8t. Cik litru pēc 10 min?",
                 "atb": ["120"], "padoms": "200 − 80."},
                {"jaut": "Kad tvertne būs tukša (min)?",
                 "atb": ["25"], "padoms": "200 : 8."},
                {"jaut": "Grafikam izvēlas punktus t = 0 un t = 25. Kāda ir "
                         "V vērtība pie t = 25?",
                 "atb": ["0"], "padoms": "Tukša."},
            ]),
            pavediens="planeta",
            konteksts="Lai grafikā redzētu visu procesu, ērtākie punkti ir "
                      "sākums un beigas.",
            kapec="Divi labi izvēlēti punkti - viss grafiks."),

    Zimejums("Tabula ar pārbaudi",
             restis([["t", "0", "10", "25"],
                     ["V", "200", "120", "0"]]),
             paskaidro="Trešais punkts (10; 120) - pārbaude."),

    Kopsavilkums([
        "Zinu, ka taisnei pietiek ar diviem punktiem.",
        "Izvēlos ērtus argumentus: 0 un saucēja daudzkārtni.",
        "Pārbaudu ar trešo punktu.",
        "Zinu, ka līknei vajag vairāk punktu.",
    ]),

    Majas([
        "Uzzīmē y = {3|4}x − 2, izvēloties ērtus punktus.",
        "Uzzīmē y = −2x + 3 ar trīs punktiem.",
        "Paskaidro, kāpēc x = 0 ir ērts punkts.",
    ]),
]
