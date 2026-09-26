# -*- coding: utf-8 -*-
"""8. klase, 36. stunda: «Kur lieto normālformu?»

Temata noslēgums pirms pārbaudes darba: pētnieciska stunda, kurā skolēns
atrod normālformu zinātnē un tehnikā un sakārto «Visuma mērogu» - no atoma
līdz galaktikai. Beigās jaukti atkārtojuma uzdevumi par visu tematu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Varianti, taisne)

TEMA = "Kur lieto normālformu?"

MERKIS = ("Meklēsim normālformas lietojumu zinātnē un tehnikā un atkārtosim "
          "pakāpju tematu.")

SATURS = [
    Sakums("Visuma mērogs metros",
           zimejums=taisne(-10, 25, 5, [(-10, "atoms"), (0, "cilvēks"),
                                         (7, "Zeme"), (16, "gaismas g."),
                                         (21, "galaktika")]),
           paraksts="Uz ass - 10 pakāpes kāpinātājs: katrs solis ir 10 "
                    "reizes.",
           fakti=["Atoms ~ 10⁻¹⁰ m, cilvēks ~ 10⁰ m.",
                  "Zemes diametrs ~ 10⁷ m, gaismas gads ~ 10¹⁶ m.",
                  "Piena Ceļš ~ 10²¹ m - tāpēc raksta pakāpes."]),

    Doma("Kur normālforma sastopama",
         "Visur, kur skaitļi ir ļoti lieli vai ļoti mazi, tos raksta "
         "normālformā vai ar priedēkļiem, kas ir 10 pakāpes.",
         soli=[
             "Astronomija: attālumi un masas.",
             "Ķīmija: atomu un molekulu skaits (6,02 · 10^{23}).",
             "Bioloģija: šūnas, vīrusi, DNS garums.",
             "Datori: baiti (kilo 10^3, mega 10^6, giga 10^9).",
             "Ekonomika: valstu budžeti miljardos.",
         ]),

    Petijums("Atrodi trīs skaitļus",
             vajag="internets vai mācību grāmata",
             soli=[
                 "Atrodi vienu ļoti lielu skaitli dabā vai tehnikā.",
                 "Atrodi vienu ļoti mazu skaitli.",
                 "Pieraksti abus normālformā ar mērvienību.",
                 "Aprēķini, cik reižu lielākais ir lielāks par mazāko.",
                 "Pieraksti avotu.",
             ],
             secinajums="Kāpinātāju starpība pasaka, cik kārtu atšķiras "
                        "skaitļi."),

    Ievadi("Temata atkārtojums", [
        {"jaut": "Aprēķini 4^−2 - atbildi raksti kā a/b",
         "atb": ["{1|16}", "1/16"], "padoms": "{1|4^2}."},
        {"jaut": "Vienkāršo {a^5 · a^−2|a^4}",
         "atb": ["{1|a}", "1/a", "a^-1"], "padoms": "a^{−1}.",
         "tastatura": "text"},
        {"jaut": "(2x^3)^4", "atb": ["16x^12", "16x^{12}"],
         "padoms": "2^4 · x^{12}.", "tastatura": "text"},
        {"jaut": "0,00045 = 4,5 · 10^?", "atb": ["−4", "-4"],
         "padoms": "4 vietas."},
        {"jaut": "(6 · 10^5) · (5 · 10^−2) = 3 · 10^?", "atb": ["4"],
         "padoms": "30 · 10^3."},
        {"jaut": "(−1)^7 + (−2)^2 + 2^0", "atb": ["4"],
         "padoms": "−1 + 4 + 1."},
    ], pamats=6),

    Varianti("Kurš priedēklis?", [
        {"jaut": "1 gigabaits =",
         "opcijas": ["10^9 baitu", "10^6 baitu", "10^{12} baitu",
                     "10^3 baitu"],
         "pareizi": 0, "padoms": "Giga - miljards."},
        {"jaut": "1 nanometrs =",
         "opcijas": ["10^−9 m", "10^−6 m", "10^−3 m", "10^9 m"],
         "pareizi": 0, "padoms": "Nano - miljardā daļa."},
        {"jaut": "1 megavats =",
         "opcijas": ["10^6 W", "10^3 W", "10^9 W", "10^−6 W"],
         "pareizi": 0, "padoms": "Mega - miljons."},
    ]),

    Pasaule("Latvijas elektrība",
            Ievadi("", [
                {"jaut": "Latvija gadā patērē ap 7 · 10^9 kWh. Iedzīvotāju "
                         "ir ap 1,9 · 10^6. Cik kWh uz cilvēku? (noapaļo līdz "
                         "simtiem)",
                 "atb": ["3700"], "padoms": "7 : 1,9 ≈ 3,68; · 10^3."},
                {"jaut": "Viena vēja turbīna gadā dod ap 9 · 10^6 kWh. Cik "
                         "turbīnu vajadzētu visam patēriņam? (noapaļo līdz "
                         "desmitiem)",
                 "atb": ["780"], "padoms": "{7 · 10^9|9 · 10^6} ≈ 778."},
                {"jaut": "Mājsaimniecība patērē 2,4 · 10^3 kWh gadā. Cik "
                         "mājsaimniecību apgādā viena turbīna?",
                 "atb": ["3750"], "padoms": "{9 · 10^6|2,4 · 10^3}."},
            ]),
            pavediens="planeta",
            konteksts="Enerģētikā skaitļi ir miljardos, bet lēmumi - par "
                      "katru māju. Normālforma savieno abus mērogus.",
            kapec="Tā aprēķina, cik vēja parku vajag valstij."),

    Kopsavilkums([
        "Zinu, kur zinātnē un tehnikā lieto normālformu.",
        "Pārveidoju priedēkļus par 10 pakāpēm.",
        "Atkārtoju visas pakāpju īpašības pirms pārbaudes darba.",
    ]),

    Majas([
        "Pabeidz pētījumu: 3 skaitļi normālformā ar avotiem.",
        "Atkārto pakāpju īpašības un atrisini 5 jauktus uzdevumus.",
        "Uzraksti sev atgādni: a^0, a^−n, normālformas nosacījums.",
    ]),
]
