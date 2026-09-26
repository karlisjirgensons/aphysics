# -*- coding: utf-8 -*-
"""4. klase, 143. stunda: «Cik liels ir kvadrātcentimetrs?»

Rūtiņu vietā - standarta vienība. 1 cm² ir kvadrāts ar malu 1 cm, 1 dm² -
ar malu 10 cm. Skolēns tos izgriež un redz: dm² ir 100 cm², nevis 10.
Tieši šis «100, nevis 10» ir biežākā kļūda, ko stunda novērš.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Varianti, kvadrats)

TEMA = "Cik liels ir kvadrātcentimetrs?"

MERKIS = ("Praktiski veidosim 1 cm² un 1 dm² modeļus un paskaidrosim "
          "sakarību starp tiem.")

SATURS = [
    Sakums("Cik kvadrātcentimetru ir kvadrātdecimetrā?",
           zimejums=kvadrats(10, 10, 1, 1, virsraksts="1 dm² = 10 × 10 cm²"),
           paraksts="Viena mazā rūtiņa - 1 cm². Visas kopā - 100 cm².",
           fakti=["1 dm = 10 cm, bet 1 dm² = 100 cm².",
                  "Kvadrātā ir 10 rindas pa 10."]),

    Doma("Kvadrātvienība - kvadrāts ar malu 1",
         "1 cm² ir kvadrāta laukums ar malu 1 cm; 1 dm² - ar malu 1 dm, un "
         "tajā ietilpst 10 · 10 = 100 cm².",
         soli=[
             "1 cm² - apmēram pirksta nags.",
             "1 dm² - apmēram plaukstas virsma.",
             "1 dm² = 100 cm², jo 10 rindas pa 10.",
             "Laukuma vienības raksta ar «²»: cm², dm², m².",
         ],
         pieze="Garums 1 dm = 10 cm, bet laukums 1 dm² = 100 cm²."),

    Petijums("Izgriez vienības",
             soli=[
                 "Uz rūtiņu papīra (rūtiņa 5 mm) izgriez kvadrātu 1 cm × 1 "
                 "cm.",
                 "Izgriez kvadrātu 10 cm × 10 cm.",
                 "Novērtē: cik mazo kvadrātu ietilps lielajā?",
                 "Pārbaudi, uzzīmējot līnijas ik pēc 1 cm.",
             ],
             vajag="rūtiņu papīrs, lineāls, šķēres",
             secinajums="Lielajā ietilpst 100 mazo - 1 dm² = 100 cm²."),

    Ievadi("Laukuma vienības", [
        {"jaut": "Cik cm² ir 1 dm²?", "atb": ["100"], "padoms": "10 · 10."},
        {"jaut": "Cik cm² ir 3 dm²?", "atb": ["300"], "padoms": "3 · 100."},
        {"jaut": "Kvadrāts ar malu 5 cm. Laukums cm²?", "atb": ["25"],
         "padoms": "5 · 5."},
        {"jaut": "Taisnstūris 7 cm × 3 cm. Laukums cm²?", "atb": ["21"],
         "padoms": "7 · 3."},
    ]),

    Varianti("Kas ir lielāks?", [
        {"jaut": "1 dm² vai 50 cm²?",
         "opcijas": ["1 dm²", "50 cm²", "vienādi"], "pareizi": 0,
         "padoms": "100 > 50."},
        {"jaut": "Cik cm² ir 1 dm²?",
         "opcijas": ["100", "10", "1000", "1"], "pareizi": 0,
         "padoms": "10 · 10."},
        {"jaut": "Kas ir apmēram 1 cm²?",
         "opcijas": ["naga virsma", "grāmatas vāks", "galds", "durvis"],
         "pareizi": 0, "padoms": "Maza virsma."},
        {"jaut": "Kas ir apmēram 1 dm²?",
         "opcijas": ["plaukstas virsma", "naga virsma", "grīda",
                     "tāfele"], "pareizi": 0,
         "padoms": "10 × 10 cm."},
    ], pamats=4),

    Pasaule("Mobilā telefona ekrāns",
            Ievadi("", [
                {"jaut": "Ekrāns 7 cm × 15 cm. Laukums cm²?", "atb": ["105"],
                 "padoms": "7 · 15."},
                {"jaut": "Planšete 16 cm × 25 cm. Laukums cm²?",
                 "atb": ["400"], "padoms": "16 · 25."},
                {"jaut": "Cik dm² ir planšetes ekrāns?", "atb": ["4"],
                 "padoms": "400 : 100."},
                {"jaut": "Par cik cm² planšete lielāka nekā telefons?",
                 "atb": ["295"], "padoms": "400 − 105."},
            ]),
            pavediens="dati",
            konteksts="Ekrānu izmērus var salīdzināt ar laukumu - tā redz, "
                      "cik vairāk vietas bildei.",
            kapec="Laukuma vienības salīdzina virsmas, ne garumus."),

    Kopsavilkums([
        "Zinu, kas ir 1 cm² un 1 dm².",
        "Zinu, ka 1 dm² = 100 cm².",
        "Aprēķinu taisnstūra laukumu cm².",
    ]),

    Majas([
        "Izmēri telefona un grāmatas virsmas un salīdzini laukumus.",
        "Atrodi mājās priekšmetu ar laukumu ap 1 dm².",
        "Paskaidro kādam, kāpēc 1 dm² nav 10 cm².",
    ]),
]
