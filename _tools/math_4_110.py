# -*- coding: utf-8 -*-
"""4. klase, 110. stunda: «Kurš skaitlis trūkst?»

Nezināmais darbībā ar daļām: {2|9} + x = {7|9}, x − {3|10} = {5|10}.
Tas pats, ko 16. stundā ar veseliem skaitļiem - viss un daļas -, tikai
skaitītāji ir tie, ar ko rēķina. Skolēns paskaidro, kā ieguva rezultātu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, dala)

TEMA = "Kurš skaitlis trūkst?"

MERKIS = ("Noteiksim nezināmo lielumu darbībā ar daļām un paskaidrosim, kā "
          "ieguvām rezultātu.")

SATURS = [
    Sakums("{2|9} + ? = {7|9}",
           zimejums=dala(9, 7, "2/9 + ? = 7/9"),
           paraksts="Iekrāsoti 7 gabali; 2 zināmi - cik vēl?",
           fakti=["Tas pats «cik vēl», ko ar veseliem skaitļiem.",
                  "Rēķina ar skaitītājiem: 7 − 2 = 5."]),

    Doma("Viss un daļas - arī daļām",
         "Nezināmo saskaitāmo atrod, no summas atņemot zināmo; nezināmo "
         "mazināmo - saskaitot starpību un atņēmēju.",
         soli=[
             "{2|9} + x = {7|9} → x = {7|9} − {2|9} = {5|9}.",
             "x − {3|10} = {5|10} → x = {5|10} + {3|10} = {8|10}.",
             "1 − x = {1|4} → x = {4|4} − {1|4} = {3|4}.",
             "Pārbaudi, ieliekot x vienādībā.",
         ],
         pieze="Saucējs visos soļos paliek tas pats."),

    Paraugs("x − {3|10} = {5|10}",
            uzd="Atrodi x: x − {3|10} = {5|10}.",
            soli=[
                ("x ir viss (mazināmais)", None),
                ("x = {5|10} + {3|10} = {8|10}", None),
                ("{8|10} − {3|10} = {5|10}", "Pārbaude."),
            ],
            atbilde="x = {8|10}"),

    Ievadi("Atrodi x", [
        {"jaut": "{2|9} + x = {7|9}", "atb": ["5/9"], "vieta": "piem., 1/2",
         "padoms": "7 − 2."},
        {"jaut": "x + {4|11} = {10|11}", "atb": ["6/11"],
         "vieta": "piem., 1/2", "padoms": "10 − 4."},
        {"jaut": "x − {3|10} = {5|10}", "atb": ["8/10"],
         "vieta": "piem., 1/2", "padoms": "5 + 3."},
        {"jaut": "{6|7} − x = {2|7}", "atb": ["4/7"], "vieta": "piem., 1/2",
         "padoms": "6 − 2."},
        {"jaut": "1 − x = {1|4}", "atb": ["3/4"], "vieta": "piem., 1/2",
         "padoms": "{4|4} − {1|4}."},
        {"jaut": "x + x = {6|8}", "atb": ["3/8"], "vieta": "piem., 1/2",
         "padoms": "Divas vienādas daļas: 6 : 2."},
    ], pamats=4),

    Varianti("Kā atrast x?", [
        {"jaut": "{3|5} + x = {4|5}",
         "opcijas": ["{4|5} − {3|5}", "{4|5} + {3|5}", "{3|5} − {4|5}"],
         "pareizi": 0, "padoms": "Summa − zināmais."},
        {"jaut": "x − {1|6} = {4|6}",
         "opcijas": ["{4|6} + {1|6}", "{4|6} − {1|6}", "{1|6} − {4|6}"],
         "pareizi": 0, "padoms": "Mazināmais = starpība + atņēmējs."},
        {"jaut": "Kāds ir x: {9|12} − x = {9|12}?",
         "opcijas": ["0", "{9|12}", "1", "{18|12}"], "pareizi": 0,
         "padoms": "Neko neatņēma."},
    ]),

    Zimejums("Josla ar nezināmo",
             dala(10, 8, "3/10 + x = 8/10"),
             paskaidro="Iekrāsoti 8 gabali: 3 zināmi, x = {5|10}.",
             ievads="Shēma parāda, kas jāatņem."),

    Pasaule("Ūdens pudele pārgājienā",
            Ievadi("", [
                {"jaut": "Pudelē bija {9|10} l. Izdzēra x, palika {4|10} l. "
                         "Cik izdzēra?",
                 "atb": ["5/10"], "vieta": "piem., 1/2", "padoms": "9 − 4."},
                {"jaut": "Pēc tam pielēja x no avota un bija {7|10} l. Cik "
                         "pielēja (no {4|10})?",
                 "atb": ["3/10"], "vieta": "piem., 1/2", "padoms": "7 − 4."},
                {"jaut": "Draugam iedeva x un palika {2|10} l (no {7|10}). "
                         "Cik iedeva?",
                 "atb": ["5/10"], "vieta": "piem., 1/2", "padoms": "7 − 2."},
                {"jaut": "Cik desmitdaļu litra trūkst līdz 1 l (no {2|10})?",
                 "atb": ["8"], "padoms": "10 − 2."},
            ]),
            pavediens="celojums",
            konteksts="Pārgājienā ūdeni dzer, pielej un dalās - un rēķina, "
                      "cik vēl palicis.",
            kapec="Nezināmais daļās ir tikpat vienkāršs kā veselos."),

    Kopsavilkums([
        "Atrodu nezināmo saskaitāmo, mazināmo un atņēmēju ar daļām.",
        "Paskaidroju, kā ieguvu rezultātu.",
        "Pārbaudu, ieliekot atbildi vienādībā.",
    ]),

    Majas([
        "Izdomā «pudeles» uzdevumu ar nezināmo un atrisini.",
        "Atrisini: x + {5|12} = 1.",
        "Uzzīmē joslu vienādībai {2|6} + x = {5|6}.",
    ]),
]
