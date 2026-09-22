# -*- coding: utf-8 -*-
"""6. klase, 100. stunda: «Kā izskatās pilna skaitļu taisne?»

Skaitļu taisne, kas līdz šim sākās nullē, turpinās arī pa kreisi. Uz tās
jāatrod vieta ne tikai veseliem skaitļiem, bet arī daļām un decimāldaļām -
un tieši negatīvās daļas mēdz nokļūt nepareizajā pusē.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Kustiba, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, taisne)

TEMA = "Kā izskatās pilna skaitļu taisne?"

MERKIS = ("Iemācīsimies atlikt uz skaitļu taisnes negatīvus veselus "
          "skaitļus, daļas un decimāldaļas.")

SATURS = [
    Sakums("Taisne turpinās abos virzienos",
           zimejums=taisne(-5, 5, 1, [(-2.5, "−2,5"), (3.5, "3,5")]),
           paraksts="Starp veseliem skaitļiem ir vieta daļām - arī negatīvā "
                    "pusē.",
           fakti=["Pa labi no nulles skaitļi aug, pa kreisi - sarūk.",
                  "−2,5 atrodas starp −3 un −2, tuvāk vidum.",
                  "Jo tālāk pa kreisi, jo mazāks skaitlis."]),

    Doma("Vispirms veselie, tad daļas starp tiem",
         "Uz skaitļu taisnes skaitli atliek divos soļos: atrod, starp kuriem "
         "veseliem skaitļiem tas atrodas, un tad sadala šo posmu.",
         soli=[
             "Nosaki skaitļa zīmi - kurā pusē no nulles to likt.",
             "Atrodi, starp kuriem veseliem skaitļiem tas atrodas.",
             "Sadali šo posmu tik daļās, cik pasaka saucējs.",
             "Atzīmē punktu un pieraksti skaitli virs tā.",
             "Pārbaudi: vai skaitlis ir pareizajā pusē no nulles?",
         ],
         pieze="Negatīvas daļas biežākā kļūda: −{1|2} ir starp −1 un 0, "
               "nevis starp 0 un 1. Mīnuss attiecas uz visu daļu, ne tikai "
               "uz skaitītāju."),

    Paraugs("Atliec trīs skaitļus",
            uzd="Atliec uz skaitļu taisnes −3; −2,5 un −{1|2}.",
            soli=[
                ("−3 ir trīs soļi pa kreisi no nulles",
                 "Vesels skaitlis."),
                ("−2,5 ir starp −3 un −2",
                 "Tieši vidū."),
                ("−{1|2} ir starp −1 un 0",
                 "Tieši vidū pirmajā posmā pa kreisi."),
                ("Secība no kreisās: −3; −2,5; −{1|2}",
                 "Jo tālāk pa kreisi, jo mazāks."),
            ],
            atbilde="−3 < −2,5 < −{1|2}"),

    Ievadi("Kur atrodas skaitlis?", [
        {"jaut": "Starp kuriem veseliem skaitļiem ir −2,5? Ieraksti mazāko.",
         "atb": ["-3", "−3"], "padoms": "−3 un −2."},
        {"jaut": "Starp kuriem veseliem skaitļiem ir −{1|2}? Ieraksti "
                 "mazāko.",
         "atb": ["-1", "−1"], "padoms": "−1 un 0."},
        {"jaut": "Kurš skaitlis atrodas tieši vidū starp −4 un −2?",
         "atb": ["-3", "−3"], "padoms": "Viens solis no katra."},
        {"jaut": "Starp kuriem veseliem skaitļiem ir −0,25? Ieraksti "
                 "lielāko.",
         "atb": ["0"], "padoms": "−1 un 0."},
        {"jaut": "Kurš skaitlis ir par 1 mazāks nekā −3?",
         "atb": ["-4", "−4"], "padoms": "Solis pa kreisi."},
        {"jaut": "Kurš skaitlis ir par 2 lielāks nekā −5?",
         "atb": ["-3", "−3"], "padoms": "Divi soļi pa labi."},
    ], pamats=4),

    Pasaule("Kur apstāsies zonde?",
            Kustiba("", [
                {"jaut": "Zonde nolaižas no 0 par 4 vienībām uz leju. Kurā "
                         "atzīmē tā apstājas?",
                 "atb": -4, "sakums": -10, "beigas": 10, "iedala": 5,
                 "mers": "vienības", "merkis": "mērķis", "objekts": "Zonde",
                 "padoms": "Četri soļi pa kreisi no nulles."},
                {"jaut": "No −4 tā paceļas par 6 vienībām. Kur tā ir tagad?",
                 "atb": 2, "sakums": -10, "beigas": 10, "iedala": 5,
                 "mers": "vienības", "merkis": "mērķis", "objekts": "Zonde",
                 "padoms": "No −4 seši soļi pa labi."},
                {"jaut": "No 2 tā nolaižas par 7,5 vienībām. Kur tā ir?",
                 "atb": -5.5, "sakums": -10, "beigas": 10, "iedala": 5,
                 "mers": "vienības", "merkis": "mērķis", "objekts": "Zonde",
                 "padoms": "2 − 7,5."},
                {"jaut": "Kurš skaitlis ir tieši vidū starp −8 un −2?",
                 "atb": -5, "sakums": -10, "beigas": 10, "iedala": 5,
                 "mers": "vienības", "merkis": "mērķis", "objekts": "Zonde",
                 "padoms": "Trīs soļi no katra."},
            ]),
            pavediens="planeta",
            konteksts="Zonde jūrā nolaižas zem nulles - un tās dziļumu "
                      "pieraksta tieši kā negatīvu skaitli.",
            kapec="Kustība pa skaitļu taisni ir tas pats, kas saskaitīšana "
                  "un atņemšana."),

    Varianti("Kurā pusē no nulles?", [
        {"jaut": "Kur atrodas −{3|4}?",
         "opcijas": ["Starp −1 un 0", "Starp 0 un 1",
                     "Starp −4 un −3", "Pie nulles"],
         "pareizi": 0,
         "padoms": "Mīnuss attiecas uz visu daļu."},
        {"jaut": "Jo tālāk pa kreisi uz taisnes, jo skaitlis...",
         "opcijas": ["mazāks", "lielāks", "tuvāks nullei", "pozitīvāks"],
         "pareizi": 0,
         "padoms": "Skaitļi aug pa labi."},
        {"jaut": "Kurš skaitlis ir tuvāk nullei: −0,5 vai −2?",
         "opcijas": ["−0,5", "−2", "Vienādi", "Nevar zināt"],
         "pareizi": 0,
         "padoms": "Attālums no nulles."},
        {"jaut": "Starp −2 un −1 atrodas...",
         "opcijas": ["−1,5", "1,5", "−2,5", "0"],
         "pareizi": 0,
         "padoms": "Posma vidus."},
    ], pamats=4),

    Zimejums("Daļas negatīvajā pusē",
             taisne(-2, 2, 1, [(-1.5, "−1,5"), (-0.5, "−0,5"),
                               (0.5, "0,5")]),
             paskaidro="Starp katriem diviem veseliem skaitļiem ir tikpat "
                       "daudz daļu abās pusēs no nulles.",
             ievads="Negatīvā pusē daļas izvietotas tieši tāpat."),

    Kopsavilkums([
        "Atlieku uz skaitļu taisnes negatīvus veselus skaitļus.",
        "Atlieku negatīvas daļas un decimāldaļas.",
        "Zinu, ka mīnuss attiecas uz visu skaitli.",
        "Nosaku skaitļa vietu starp diviem veseliem skaitļiem.",
    ]),

    Majas([
        "Uzzīmē skaitļu taisni no −5 līdz 5 un atzīmē uz tās piecus "
        "skaitļus.",
        "Atzīmē vismaz divas negatīvas daļas.",
        "Pieraksti, kurš no taviem skaitļiem ir vistuvāk nullei.",
    ]),
]
