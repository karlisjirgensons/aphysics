# -*- coding: utf-8 -*-
"""7. klase, 138. stunda: «Cik sakņu var būt?»

Lineāram vienādojumam ir viena sakne, bet var gadīties, ka x pazūd. Tad
atliek skaitliska vienādība: ja tā patiesa (5 = 5) - sakņu ir bezgalīgi
daudz, ja aplama (5 = 7) - sakņu nav. Grafiski - sakrītošas vai paralēlas
taisnes.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, plakne, restis)

TEMA = "Cik sakņu var būt?"

MERKIS = ("Analizēsim gadījumus, kad vienādojumam nav sakņu vai ir "
          "bezgalīgi daudz sakņu.")

SATURS = [
    Sakums("x pazuda - ko tagad?",
           zimejums=restis([["pēc pārveidojuma", "saknes"],
                            ["3x = 12", "viena: x = 4"],
                            ["0x = 5", "nav"],
                            ["0x = 0", "bezgalīgi daudz"]]),
           fakti=["0 · x = 5 - neviens skaitlis nedod 5.",
                  "0 · x = 0 - der jebkurš skaitlis.",
                  "Tās nav kļūdas - tās ir atbildes."]),

    Doma("Trīs gadījumi",
         "Pēc pārveidojumiem lineārs vienādojums kļūst kx = b. Ja k ≠ 0 - "
         "viena sakne x = {b|k}. Ja k = 0 un b ≠ 0 - sakņu nav. Ja k = 0 un "
         "b = 0 - sakņu ir bezgalīgi daudz.",
         soli=[
             "Pārveido līdz formai kx = b.",
             "k ≠ 0: dali.",
             "k = 0: pārbaudi, vai b = 0.",
             "Pieraksti atbildi vārdiem, ja sakņu nav vai ir bezgalīgi.",
         ],
         pieze="Grafiski: paralēlas taisnes - nav sakņu; sakrītošas - "
               "bezgalīgi daudz."),

    Paraugs("Nav sakņu",
            uzd="Atrisini 2(x + 3) = 2x + 1.",
            soli=[
                ("2x + 6 = 2x + 1", "Atver iekavas."),
                ("2x − 2x = 1 − 6", "Pārnes."),
                ("0x = −5", "x pazūd."),
                ("Neviens x nedod −5", "Aplama vienādība."),
            ],
            atbilde="Sakņu nav."),

    Zimejums("Paralēlas taisnes: y = 2x + 6 un y = 2x + 1",
             plakne(grafiki=[(2, 6, "y = 2x + 6"), (2, 1, "y = 2x + 1")],
                    no_x=-4, lidz_x=3, no_y=-3, lidz_y=8, solis=1),
             paskaidro="Krustpunkta nav - sakņu nav."),

    Varianti("Cik sakņu?", [
        {"jaut": "3(x − 1) = 3x − 3",
         "opcijas": ["Bezgalīgi daudz", "Viena", "Nav", "Divas"],
         "pareizi": 0, "padoms": "0x = 0."},
        {"jaut": "4x + 1 = 4x − 1",
         "opcijas": ["Nav", "Viena", "Bezgalīgi daudz", "Divas"],
         "pareizi": 0, "padoms": "0x = −2."},
        {"jaut": "5x = 0",
         "opcijas": ["Viena: x = 0", "Nav", "Bezgalīgi daudz", "Divas"],
         "pareizi": 0, "padoms": "k = 5 ≠ 0."},
        {"jaut": "x + x = 2x",
         "opcijas": ["Bezgalīgi daudz", "Viena", "Nav", "Divas"],
         "pareizi": 0, "padoms": "Identitāte."},
    ], pamats=4),

    Ievadi("Atrisini vai pasaki", [
        {"jaut": "2(x − 4) = x − 3. Sakne?",
         "atb": ["5"], "padoms": "2x − 8 = x − 3."},
        {"jaut": "Cik sakņu vienādojumam 6x − 2 = 2(3x − 1)?",
         "atb": ["bezgalīgi daudz", "bezgalīgi", "∞"],
         "padoms": "0x = 0.", "tastatura": "text"},
        {"jaut": "Cik sakņu vienādojumam x + 4 = x?",
         "atb": ["0", "nav"], "padoms": "0x = −4.", "tastatura": "text"},
    ]),

    Pasaule("Divi autobusi",
            Varianti("", [
                {"jaut": "Divi autobusi brauc pa vienu šoseju vienā virzienā "
                         "ar 60 km/h; viens 10 km priekšā. Kad satiksies? "
                         "(60t + 10 = 60t)",
                 "opcijas": ["Nekad - sakņu nav", "Pēc 1 h",
                             "Pēc 10 min", "Uzreiz"],
                 "pareizi": 0, "padoms": "0t = −10."},
                {"jaut": "Ja abi startē no vienas vietas vienlaikus?",
                 "opcijas": ["Vienmēr blakus - bezgalīgi daudz sakņu",
                             "Nekad", "Pēc 1 h", "Tikai sākumā"],
                 "pareizi": 0, "padoms": "60t = 60t."},
            ]),
            pavediens="celojums",
            konteksts="Ja ātrumi vienādi, attālums starp transportlīdzekļiem "
                      "nemainās - vienādojums to parāda.",
            kapec="«Nav sakņu» arī ir atbilde situācijai."),

    Kopsavilkums([
        "Pārveidoju vienādojumu līdz kx = b.",
        "Nosaku: viena sakne, nav sakņu vai bezgalīgi daudz.",
        "Saistu ar paralēlām un sakrītošām taisnēm.",
        "Pierakstu atbildi vārdiem.",
    ]),

    Majas([
        "Izdomā vienādojumu bez saknēm un ar bezgalīgi daudzām.",
        "Atrisini: 3(2x − 1) = 6x + 4.",
        "Uzzīmē abu pušu grafikus.",
    ]),
]
