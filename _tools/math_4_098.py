# -*- coding: utf-8 -*-
"""4. klase, 98. stunda: «Kā neīstu daļu izteikt ar veselo?»

Mikrotemata noslēgums. {7|3} = 2 + {1|3}: cik reižu saucējs ietilpst
skaitītājā - tik veselo; atlikums - skaitītājs īstajai daļai. Tā ir
dalīšana ar atlikumu no 33. stundas. Jaukta skaitļa pierakstu (2{1|3})
4. klasē vēl nelieto, tāpēc raksta summu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, taisne)

TEMA = "Kā neīstu daļu izteikt ar veselo?"

MERKIS = ("Izteiksim neīstu daļu kā vesela skaitļa un īstas daļas summu.")

SATURS = [
    Sakums("Cik veselu picu ir 11 ceturtdaļās?",
           zimejums=taisne(0, 3, 1, [(2.75, "11/4")], sikas=4),
           paraksts="{11|4} = 2 + {3|4}.",
           fakti=["Katras 4 ceturtdaļas ir 1 vesela pica.",
                  "11 : 4 = 2 (atl. 3) - divas veselas un 3 ceturtdaļas."]),

    Doma("Dali skaitītāju ar saucēju",
         "Neīstu daļu izsaka kā veselu skaitli un īstu daļu: dalījums ir "
         "veselie, atlikums - jaunās daļas skaitītājs.",
         soli=[
             "Izdali skaitītāju ar saucēju: 11 : 4 = 2 (atl. 3).",
             "Dalījums 2 - veselo skaits.",
             "Atlikums 3 - skaitītājs, saucējs paliek 4.",
             "Pieraksti: {11|4} = 2 + {3|4}.",
         ],
         pieze="Ja atlikums 0, daļa ir vesels skaitlis: {12|4} = 3."),

    Paraugs("{17|5}",
            uzd="Izsaki {17|5} kā vesela skaitļa un daļas summu.",
            soli=[
                ("17 : 5 = 3 (atl. 2)", None),
                ("{17|5} = 3 + {2|5}", None),
                ("3 · 5 + 2 = 17", "Pārbaude."),
            ],
            atbilde="3 + {2|5}"),

    Slidnis("{7|3} pa gabaliem",
            soli=[
                {"v": "{7|3}", "teksts": "Septiņas trešdaļas."},
                {"v": "{3|3} + {3|3} + {1|3}", "teksts": "Grupē pa trim."},
                {"v": "1 + 1 + {1|3}", "teksts": "Katra grupa - viens "
                 "vesels."},
                {"v": "2 + {1|3}", "teksts": "Divi veseli un trešdaļa."},
            ]),

    Ievadi("Cik veselo?", [
        {"jaut": "{11|4} = ? + {3|4}. Cik veselo?", "atb": ["2"],
         "padoms": "11 : 4."},
        {"jaut": "{17|5} = 3 + {?|5}. Kāds skaitītājs?", "atb": ["2"],
         "padoms": "17 − 15."},
        {"jaut": "{9|2} = ? + {1|2}. Cik veselo?", "atb": ["4"],
         "padoms": "9 : 2."},
        {"jaut": "{20|6} = 3 + {?|6}. Kāds skaitītājs?", "atb": ["2"],
         "padoms": "20 − 18."},
        {"jaut": "{15|5} = ?", "atb": ["3"], "padoms": "Atlikuma nav."},
        {"jaut": "2 + {1|3} = {?|3}. Kāds skaitītājs?", "atb": ["7"],
         "padoms": "2 · 3 + 1."},
    ], pamats=4),

    Varianti("Pareizi vai nē?", [
        {"jaut": "{13|4} = 3 + {1|4}",
         "opcijas": ["pareizi", "aplami"], "pareizi": 0,
         "padoms": "12 + 1 = 13."},
        {"jaut": "{13|4} = 4 + {1|3}",
         "opcijas": ["aplami", "pareizi"], "pareizi": 0,
         "padoms": "Saucējs jāsaglabā - 4."},
        {"jaut": "{10|3} = 3 + {1|3}",
         "opcijas": ["pareizi", "aplami"], "pareizi": 0,
         "padoms": "9 + 1 = 10."},
        {"jaut": "{8|4} = 2",
         "opcijas": ["pareizi", "aplami"], "pareizi": 0,
         "padoms": "8 : 4 = 2, atlikums 0."},
    ], pamats=4),

    Pasaule("Skrējiena apļi",
            Ievadi("", [
                {"jaut": "Stadiona aplis sadalīts 4 posmos. Skrējējs "
                         "noskrēja 11 posmus. Cik pilnu apļu?",
                 "atb": ["2"], "padoms": "11 : 4."},
                {"jaut": "Cik posmu no nākamā apļa?", "atb": ["3"],
                 "padoms": "Atlikums."},
                {"jaut": "Cik posmu vēl līdz 3 pilniem apļiem?", "atb": ["1"],
                 "padoms": "12 − 11."},
                {"jaut": "Aplis 400 m. Cik metru ir 11 posmi (katrs 100 m)?",
                 "atb": ["1100"], "padoms": "11 · 100."},
            ]),
            pavediens="sports",
            konteksts="Stadiona aplis ir 400 m; skrējēji skaita apļus un "
                      "to daļas.",
            kapec="«Divi apļi un trīs ceturtdaļas» ir {11|4} apļa."),

    Kopsavilkums([
        "Izsaku neīstu daļu kā veselo un īstas daļas summu.",
        "Lietoju dalīšanu ar atlikumu.",
        "Pārbaudu: veselais · saucējs + skaitītājs.",
    ]),

    Majas([
        "Izsaki {23|5} un {14|3} ar veselajiem.",
        "Saskaiti, cik ceturtdaļstundu ir 2 stundās un 15 minūtēs.",
        "Paskaidro kādam, kāpēc {12|4} = 3.",
    ]),
]
