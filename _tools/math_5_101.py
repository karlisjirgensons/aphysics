# -*- coding: utf-8 -*-
"""5. klase, 101. stunda: «Kurš skaitlis trūkst vienādībā?»

Mikrotemata noslēgums, un tas atgriežas pie 21. un 28. stundas: nezināmo
atrod pēc tā, kurā vietā tas stāv. Jaunais ir tikai skaitļu veids - tagad
saskaitāmais vai atņēmējs ir jaukts skaitlis. Tieši tāpēc pārbaude te ir
obligāta: aizņemšanās vietā viegli pazūd viens veselais.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kurš skaitlis trūkst vienādībā?"

MERKIS = ("Iemācīsimies noteikt nezināmo vienādībā ar jauktiem skaitļiem un "
          "veidot pierakstu.")

SATURS = [
    Sakums("Vienādībā trūkst viena skaitļa",
           zimejums=restis([["1 1/4", "+", "?", "3 1/2"]],
                           virsraksts="Saskaitāmais, saskaitāmais, summa"),
           paraksts="Nezināmo saskaitāmo atrod, no summas atņemot zināmo.",
           fakti=["Nezināmais var būt jebkurā vietā.",
                  "Kārtula ir tā pati, kas ar veseliem skaitļiem.",
                  "Mainās tikai skaitļu veids."]),

    Doma("Kārtula ir tā pati",
         "Nezināmo saskaitāmo atrod, no summas atņemot zināmo saskaitāmo; "
         "nezināmo mazināmo - summējot starpību ar atņēmēju.",
         soli=[
             "Nosaki, kurā vietā stāv nezināmais.",
             "Izvēlies atbilstošo kārtulu.",
             "Izrēķini, aizņemoties veselo, ja vajag.",
             "Ieliec atrasto skaitli vienādībā.",
             "Pārbaudi, vai vienādība ir patiesa.",
         ],
         pieze="Nezināmo atņēmēju atrod, no mazināmā atņemot starpību; "
               "nezināmo mazināmo - starpībai pieskaitot atņēmēju. Abas "
               "kārtulas ir tās pašas, kas 4. klasē."),

    Paraugs("1{1|4} + x = 3{1|2}",
            uzd="Atrodi nezināmo saskaitāmo.",
            soli=[
                ("x = 3{1|2} - 1{1|4}",
                 "No summas atņem zināmo saskaitāmo."),
                ("3{1|2} = 3{2|4}",
                 "Vienādo saucējus."),
                ("3{2|4} - 1{1|4} = 2{1|4}",
                 "Atņem veselos un daļas."),
                ("Pārbaude: 1{1|4} + 2{1|4} = 3{2|4} = 3{1|2}",
                 "Vienādība ir patiesa."),
            ],
            atbilde="x = 2{1|4}"),

    Ievadi("Atrodi nezināmo", [
        {"jaut": "1{1|4} + x = 3{1|2}. Cik ir x? Atbildi raksti kā a b/c.",
         "atb": ["2 1/4"], "padoms": "3{2|4} - 1{1|4}."},
        {"jaut": "x + 2{1|3} = 4{2|3}. Cik ir x? Atbildi raksti kā a b/c.",
         "atb": ["2 1/3"], "padoms": "4{2|3} - 2{1|3}."},
        {"jaut": "5{3|4} - x = 2{1|4}. Cik ir x? Atbildi raksti kā a b/c.",
         "atb": ["3 1/2", "3 2/4"], "padoms": "5{3|4} - 2{1|4}."},
        {"jaut": "x - 1{1|5} = 2{3|5}. Cik ir x? Atbildi raksti kā a b/c.",
         "atb": ["3 4/5"], "padoms": "2{3|5} + 1{1|5}."},
        {"jaut": "2{1|6} + x = 4. Cik ir x? Atbildi raksti kā a b/c.",
         "atb": ["1 5/6"], "padoms": "4 - 2{1|6}."},
        {"jaut": "x + {3|8} = 2. Cik ir x? Atbildi raksti kā a b/c.",
         "atb": ["1 5/8"], "padoms": "2 - {3|8}."},
        {"jaut": "4{1|2} - x = 1{1|2}. Cik ir x? Ieraksti skaitli.",
         "atb": ["3"], "padoms": "4{1|2} - 1{1|2}."},
        {"jaut": "3 - x = 1{1|4}. Cik ir x? Atbildi raksti kā a b/c.",
         "atb": ["1 3/4"], "padoms": "3 - 1{1|4}."},
    ], pamats=4,
        ievads="Vispirms nosaki, kurā vietā stāv nezināmais."),

    Zimejums("Kur stāv nezināmais",
             restis([["?", "+", "2 1/3", "4 2/3"],
                     ["5 3/4", "-", "?", "2 1/4"]],
                    virsraksts="Augšā trūkst saskaitāmā, apakšā atņēmēja"),
             paskaidro="Augšējā rindā nezināmo atrod, atņemot; apakšējā - "
                       "arī atņemot, bet no mazināmā.",
             ievads="Vieta vienādībā nosaka, kura kārtula der."),

    Varianti("Kura kārtula te der?", [
        {"jaut": "Kā atrod nezināmo saskaitāmo?",
         "opcijas": ["No summas atņem zināmo saskaitāmo",
                     "Summai pieskaita zināmo",
                     "Summu dala ar diviem",
                     "Summu reizina"],
         "pareizi": 0,
         "padoms": "Atņemšana ir pretējā darbība."},
        {"jaut": "Kā atrod nezināmo mazināmo?",
         "opcijas": ["Starpībai pieskaita atņēmēju",
                     "No starpības atņem atņēmēju",
                     "Starpību reizina",
                     "Starpību dala"],
         "pareizi": 0,
         "padoms": "Mazināmais ir lielākais no trim."},
        {"jaut": "Kā atrod nezināmo atņēmēju?",
         "opcijas": ["No mazināmā atņem starpību",
                     "Mazināmajam pieskaita starpību",
                     "Starpībai pieskaita mazināmo",
                     "Mazināmo dala"],
         "pareizi": 0,
         "padoms": "Abi zināmie ir mazināmais un starpība."},
        {"jaut": "2{1|6} + x = 4. Cik ir x?",
         "opcijas": ["1{5|6}", "2{5|6}", "1{1|6}", "6{1|6}"],
         "pareizi": 0,
         "padoms": "4 = 3{6|6}."},
        {"jaut": "Kā pārbauda atrasto skaitli?",
         "opcijas": ["Ieliek to vienādībā un izrēķina",
                     "Salīdzina ar summu",
                     "Saīsina to",
                     "Pārbaudīt nevar"],
         "pareizi": 0,
         "padoms": "Vienādībai jāpaliek patiesai."},
        {"jaut": "Vai kārtulas mainās, ja skaitļi ir jaukti?",
         "opcijas": ["Nē, tās ir tās pašas", "Jā, visas",
                     "Tikai atņemšanai", "Tikai saskaitīšanai"],
         "pareizi": 0,
         "padoms": "Mainās skaitļu veids, ne likumi."},
    ], pamats=4),

    Pasaule("Cik materiāla vēl jānopērk?",
            Ievadi("", [
                {"jaut": "Vajag 3{1|2} m līstes, ir 1{1|4} m. Cik metru vēl "
                         "jānopērk? Atbildi raksti kā a b/c.",
                 "atb": ["2 1/4"], "padoms": "3{2|4} - 1{1|4}."},
                {"jaut": "Vajag 4 l krāsas, ir 2{1|6} l. Cik litru vēl "
                         "jānopērk? Atbildi raksti kā a b/c.",
                 "atb": ["1 5/6"], "padoms": "4 - 2{1|6}."},
                {"jaut": "Bija 5{3|4} m auklas, palika 2{1|4} m. Cik metru "
                         "izlietots? Atbildi raksti kā a b/c.",
                 "atb": ["3 1/2", "3 2/4"], "padoms": "5{3|4} - 2{1|4}."},
                {"jaut": "Izlietoti 2{3|5} kg, palika 1{1|5} kg. Cik "
                         "kilogramu bija sākumā? Atbildi raksti kā a b/c.",
                 "atb": ["3 4/5"], "padoms": "2{3|5} + 1{1|5}."},
            ]),
            pavediens="maja",
            konteksts="Remontā biežākais jautājums ir tieši par trūkstošo "
                      "skaitli: cik vēl vajag.",
            kapec="Nezināmā vieta vienādībā pasaka, kuru darbību izvēlēties."),

    Kopsavilkums([
        "Nosaku, kurā vienādības vietā stāv nezināmais.",
        "Izvēlos atbilstošo kārtulu nezināmā atrašanai.",
        "Rēķinu ar jauktiem skaitļiem, aizņemoties veselo, ja vajag.",
        "Pārbaudu atbildi, ieliekot to vienādībā.",
    ]),

    Majas([
        "Atrodi x: x + 1{2|7} = 3{5|7} un 5{1|3} - x = 2{2|3}.",
        "Pārbaudi abas atbildes.",
        "Izdomā vienādību ar jauktiem skaitļiem draugam.",
    ]),
]
