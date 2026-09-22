# -*- coding: utf-8 -*-
"""6. klase, 110. stunda: «Kuri skaitļi atbilst nosacījumiem?»

Mikrotemata noslēgums. Uzdevums vairs nav «izrēķini», bet «atrodi visus» -
un atbilde ir skaitļu kopa. Nosacījumi ir par moduli un novietojumu, tāpēc
te satiekas viss, ko šis mikrotemats mācīja.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, taisne)

TEMA = "Kuri skaitļi atbilst nosacījumiem?"

MERKIS = ("Noteiksim skaitļu kopu pēc nosacījumiem par moduli un "
          "novietojumu.")

SATURS = [
    Sakums("Atbilde var būt vairāki skaitļi",
           zimejums=taisne(-5, 5, 1, [(-4, "−4"), (4, "4")]),
           paraksts="«Modulis ir 4» der diviem skaitļiem: −4 un 4. Abi ir "
                    "pareizi.",
           fakti=["Nosacījums par moduli parasti dod divus skaitļus.",
                  "Papildu nosacījums par zīmi atstāj vienu.",
                  "Atbildi pieraksta kā visu derīgo skaitļu sarakstu."]),

    Doma("Pārbaudi katru nosacījumu atsevišķi",
         "Skaitļu kopu atrod, vispirms uzskaitot visus skaitļus, kas atbilst "
         "pirmajam nosacījumam, un tad izsvītrojot tos, kas neatbilst "
         "pārējiem.",
         soli=[
             "Izlasi pirmo nosacījumu un uzskaiti visus derīgos skaitļus.",
             "Izlasi nākamo nosacījumu.",
             "Izsvītro tos, kas tam neatbilst.",
             "Atkārto, kamēr visi nosacījumi ir pārbaudīti.",
             "Pieraksti atlikušos skaitļus augošā secībā.",
         ],
         pieze="Ja nosacījumi ir pretrunīgi, kopa var būt arī tukša: "
               "«modulis ir 3 un skaitlis ir lielāks par 5» neder nevienam "
               "skaitlim. Arī tā ir pareiza atbilde."),

    Paraugs("Atrodi visus derīgos skaitļus",
            uzd="Kuri veselie skaitļi atbilst nosacījumiem: modulis mazāks "
                "par 3 un skaitlis negatīvs?",
            soli=[
                ("Modulis mazāks par 3",
                 "Der −2; −1; 0; 1; 2."),
                ("Skaitlis negatīvs",
                 "Izsvītro 0; 1 un 2."),
                ("Paliek −2 un −1",
                 "Abi atbilst abiem nosacījumiem."),
                ("Pārbaude: abu moduļi ir 2 un 1",
                 "Mazāki par 3."),
            ],
            atbilde="−2 un −1"),

    Ievadi("Atrodi skaitļus", [
        {"jaut": "Kuriem skaitļiem modulis ir 4? Ieraksti negatīvo.",
         "atb": ["-4", "−4"], "padoms": "4 un −4."},
        {"jaut": "Cik veselu skaitļu ir ar moduli, mazāku par 3?",
         "atb": ["5"], "padoms": "−2; −1; 0; 1; 2."},
        {"jaut": "Cik no tiem ir negatīvi?",
         "atb": ["2"], "padoms": "−2 un −1."},
        {"jaut": "Kurš vesels negatīvs skaitlis ir ar moduli 1?",
         "atb": ["-1", "−1"], "padoms": "Viens solis pa kreisi."},
        {"jaut": "Cik veselu skaitļu ir starp −3 un 3, ieskaitot galus?",
         "atb": ["7"], "padoms": "No −3 līdz 3."},
        {"jaut": "Cik skaitļu atbilst nosacījumam «modulis ir 3 un skaitlis "
                 "lielāks par 5»?",
         "atb": ["0"], "padoms": "Pretrunīgi nosacījumi."},
    ], pamats=4),

    Varianti("Kura kopa ir pareizā?", [
        {"jaut": "«Modulis ir 5.» Kuri skaitļi der?",
         "opcijas": ["5 un −5", "Tikai 5", "Tikai −5", "0 un 5"],
         "pareizi": 0,
         "padoms": "Vienāds attālums abās pusēs."},
        {"jaut": "«Modulis mazāks par 2 un skaitlis vesels.» Cik tādu ir?",
         "opcijas": ["3", "2", "4", "1"],
         "pareizi": 0,
         "padoms": "−1; 0; 1."},
        {"jaut": "«Skaitlis negatīvs un modulis lielāks par 10.» Kurš der?",
         "opcijas": ["−12", "12", "−8", "0"],
         "pareizi": 0,
         "padoms": "Abi nosacījumi reizē."},
        {"jaut": "Kad kopa ir tukša?",
         "opcijas": ["Kad nosacījumi ir pretrunīgi",
                     "Kad skaitļi ir negatīvi",
                     "Kad ir vairāki nosacījumi", "Nekad"],
         "pareizi": 0,
         "padoms": "Neviens skaitlis neatbilst visiem."},
    ], pamats=4),

    Pasaule("Kuras dienas der?",
            Ievadi("", [
                {"jaut": "Der dienas, kurās temperatūra bija zem nulles, bet "
                         "ne aukstāka par −5 °C. Vai −3 °C der? Raksti «jā» "
                         "vai «nē».",
                 "atb": ["jā", "ja"], "padoms": "Starp −5 un 0."},
                {"jaut": "Vai −7 °C der?",
                 "atb": ["nē", "ne"], "padoms": "Aukstāks par −5."},
                {"jaut": "Cik veselu grādu vērtību atbilst nosacījumam?",
                 "atb": ["4"], "padoms": "−4; −3; −2; −1."},
                {"jaut": "Vai 0 °C der? Raksti «jā» vai «nē».",
                 "atb": ["nē", "ne"], "padoms": "Jābūt zem nulles."},
            ]),
            pavediens="planeta",
            konteksts="Meteorologi dienas šķiro tieši pēc šādiem "
                      "nosacījumiem - un robežas te ir svarīgas.",
            kapec="Katrs nosacījums sašaurina kopu, nevis paplašina to."),

    Zimejums("Kopa uz skaitļu taisnes",
             taisne(-5, 5, 1, [(-2, "der"), (-1, "der")]),
             paskaidro="Nosacījumiem «modulis mazāks par 3» un «skaitlis "
                       "negatīvs» atbilst tikai −2 un −1.",
             ievads="Uz taisnes kopu var iekrāsot."),

    Kopsavilkums([
        "Atrodu visus skaitļus, kas atbilst nosacījumam par moduli.",
        "Pārbaudu katru nosacījumu atsevišķi.",
        "Pierakstu atbildi kā skaitļu kopu augošā secībā.",
        "Atpazīstu pretrunīgus nosacījumus un tukšu kopu.",
    ]),

    Majas([
        "Atrodi visus veselos skaitļus ar moduli, mazāku par 4.",
        "Atrodi tos, kas turklāt ir negatīvi.",
        "Izdomā nosacījumu pāri, kuram atbilst tikai viens skaitlis.",
    ]),
]
