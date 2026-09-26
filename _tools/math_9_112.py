# -*- coding: utf-8 -*-
"""9. klase, 112. stunda: «Kā digitālie rīki palīdz?»

GeoGebra vai Desmos uzzīmē taisnes un parāda krustpunktu precīzi. Stunda
ir praktiska: skolēns ievada sistēmas, maina parametrus ar slīdni un
pārbauda savus rokas aprēķinus.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Slidnis, Varianti, paris, plakne)

TEMA = "Kā digitālie rīki palīdz?"

MERKIS = ("Lietosim digitālos rīkus sistēmas grafiskajai risināšanai.")

_T = "text"
_PLAKNE = dict(no_x=-3, lidz_x=5, no_y=-3, lidz_y=6)

SATURS = [
    Sakums("Grafiku zīmētājs - tavā telefonā",
           zimejums=plakne(grafiki=[(0.5, 1, "y = 0,5x + 1"),
                                    (-2, 6, "y = −2x + 6")],
                           punkti=[(2, 2, "(2; 2)")], **_PLAKNE),
           paraksts="Ievadi divas formulas - rīks parāda krustpunktu.",
           fakti=["GeoGebra un Desmos ir bez maksas.",
                  "Pieskaroties krustpunktam, redz koordinātas.",
                  "Slīdnis maina koeficientu - taisne kustas."]),

    Petijums("Darbs ar rīku", [
        "Atver geogebra.org vai desmos.com (vai lietotni).",
        "Ievadi y = 0,5x + 1 un y = −2x + 6. Nolasi krustpunktu.",
        "Ievadi y = kx + 1 - izveidojas slīdnis k. Kustini to.",
        "Atrodi k, pie kura taisnes ir paralēlas (nav krustpunkta).",
        "Pieraksti trīs sistēmas un to atrisinājumus.",
    ], vajag="telefons vai dators",
       secinajums="Pie k = −2 taisnes ir paralēlas - sistēmai nav "
                  "atrisinājuma."),

    Slidnis("Slīdnis k: y = kx + 1 un y = −2x + 6", [
        {"v": "k = 1", "teksts": "Krustpunkts (1,67; 2,67)",
         "zim": plakne(grafiki=[(1, 1, "k = 1"), (-2, 6, "")], **_PLAKNE)},
        {"v": "k = 0,5", "teksts": "Krustpunkts (2; 2)",
         "zim": plakne(grafiki=[(0.5, 1, "k = 0,5"), (-2, 6, "")],
                       **_PLAKNE)},
        {"v": "k = −2", "teksts": "Paralēlas - nav krustpunkta",
         "zim": plakne(grafiki=[(-2, 1, "k = −2"), (-2, 6, "")],
                       **_PLAKNE)},
    ]),

    Doma("Rīks - palīgs, ne aizstājējs",
         "Digitālais rīks ātri parāda atbildi un ļauj eksperimentēt, bet "
         "eksāmenā vajag prast arī bez tā.",
         soli=[
             "Izmanto rīku pārbaudei un pētīšanai.",
             "Pamato atbildi ar aprēķinu.",
             "Rīks rāda noapaļotas vērtības - precīzu dod algebra.",
         ]),

    Ievadi("Pārbaudi ar rīku (vai aprēķini)", [
        {"jaut": "y = x + 3 un y = −x + 7", "atb": paris(2, 5),
         "tastatura": _T, "vieta": "(x; y)", "padoms": "2x = 4."},
        {"jaut": "y = 3x − 2 un y = x + 4", "atb": paris(3, 7),
         "tastatura": _T, "vieta": "(x; y)", "padoms": "2x = 6."},
        {"jaut": "y = kx + 1 un y = −2x + 6 krustojas pie x = 1. k = ?",
         "atb": ["3"], "padoms": "y(1) = 4 ⇒ k + 1 = 4."},
    ]),

    Varianti("Ko rāda rīks?", [
        {"jaut": "Rīks rāda krustpunktu (0,333; 1,667). Precīzi tas ir...",
         "opcijas": ["({1|3}; {5|3})", "(0,3; 1,7)", "(1; 5)", "(3; 5)"],
         "pareizi": 0, "padoms": "0,333... = {1|3}."},
        {"jaut": "Rīks nerāda krustpunktu, taisnes paralēlas. Sistēmai...",
         "opcijas": ["nav atrisinājuma", "ir viens", "bezgalīgi daudz",
                     "rīkā kļūda"],
         "pareizi": 0, "padoms": "Paralēlas."},
    ]),

    Pasaule("Mobilā lietotne tarifiem",
            Ievadi("", [
                {"jaut": "Tarifs A: 3 € + 0,5 €/h, tarifs B: 1 € + 0,9 €/h "
                         "(velosipēdu noma). Pie cik h maksā vienādi?",
                 "atb": ["5"], "padoms": "3 + 0,5x = 1 + 0,9x."},
                {"jaut": "Cik € tad maksā?", "atb": ["5,5"],
                 "padoms": "3 + 2,5."},
            ]),
            pavediens="celojums",
            konteksts="Pilsētas velonomas lietotne salīdzina tarifus ar "
                      "grafiku - tieši tāpat kā GeoGebra.",
            kapec="Krustpunkts - robeža starp izdevīgajiem tarifiem."),

    Kopsavilkums([
        "Lietoju GeoGebra vai Desmos sistēmas atrisināšanai.",
        "Pētu, kā koeficients maina taisnes stāvokli.",
        "Pamatoju rīka atbildi ar aprēķinu.",
    ]),

    Majas([
        "Ar rīku atrisini 3 sistēmas no mācību grāmatas un pārbaudi.",
        "Atrodi b, pie kura y = 2x + b iet caur (1; 5).",
        "Izveido ekrānuzņēmumu ar diviem tarifiem un to krustpunktu.",
    ]),
]
