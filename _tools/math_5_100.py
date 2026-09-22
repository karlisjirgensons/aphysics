# -*- coding: utf-8 -*-
"""5. klase, 100. stunda: «Cik apmēram būs starpība?»

Novērtēšana ir prasme, kas pasargā no kļūdām: ja aptuvenā atbilde ir 2, bet
izrēķinātā 5, kaut kas noteikti ir greizi. Viss balstās uz 61. stundas triku -
salīdzināt daļu ar pusi - un uz noapaļošanu līdz tuvākajam veselam skaitlim.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, taisne)

TEMA = "Cik apmēram būs starpība?"

MERKIS = ("Mācīsimies novērtēt starpības aptuveno vērtību pirms aprēķina un "
          "pamatot spriedumu.")

SATURS = [
    Sakums("Apmēram cik paliks?",
           zimejums=taisne(0, 5, 1, [(4.125, "4 1/8"), (1.9, "1 7/8")],
                           virsraksts="Abi skaitļi tuvu veseliem"),
           paraksts="4{1|8} ir gandrīz 4, bet 1{7|8} - gandrīz 2.",
           fakti=["4{1|8} - 1{7|8} precīzi rēķināt ir garš darbs.",
                  "Bet aptuveni tas ir 4 - 2 = 2.",
                  "Ja atbilde iznāk 3 vai 1, kaut kas ir greizi."]),

    Doma("Noapaļo līdz tuvākajam veselam",
         "Aptuveno starpību iegūst, katru jaukto skaitli noapaļojot līdz "
         "tuvākajam veselam skaitlim un atņemot tos.",
         soli=[
             "Salīdzini katra skaitļa daļu ar {1|2}.",
             "Daļa mazāka par pusi - noapaļo uz leju.",
             "Daļa lielāka par pusi - noapaļo uz augšu.",
             "Atņem noapaļotos veselos skaitļus.",
             "Pēc aprēķina salīdzini precīzo atbildi ar novērtējumu.",
         ],
         pieze="Novērtējums nav atbilde, bet pārbaude. Precīzā atbilde var "
               "atšķirties par mazliet mazāk nekā vienu veselu, bet nekad "
               "ne par diviem vai trim."),

    Paraugs("Novērtē 4{1|8} - 1{7|8}",
            uzd="Novērtē starpību un tad izrēķini to precīzi.",
            soli=[
                ("{1|8} < {1|2}, tāpēc 4{1|8} ir apmēram 4",
                 "Noapaļo uz leju."),
                ("{7|8} > {1|2}, tāpēc 1{7|8} ir apmēram 2",
                 "Noapaļo uz augšu."),
                ("Apmēram 4 - 2 = 2",
                 "Novērtējums."),
                ("Precīzi: 4{1|8} = 3{9|8}; 3{9|8} - 1{7|8} = 2{2|8}",
                 "Aizņemas vienu veselo."),
                ("2{2|8} = 2{1|4}",
                 "Tuvu novērtējumam - viss kārtībā."),
            ],
            atbilde="Apmēram 2; precīzi 2{1|4}"),

    Ievadi("Noapaļo un novērtē", [
        {"jaut": "Līdz kuram veselam noapaļo 4{1|8}? Ieraksti skaitli.",
         "atb": ["4"], "padoms": "{1|8} < {1|2}."},
        {"jaut": "Līdz kuram veselam noapaļo 1{7|8}? Ieraksti skaitli.",
         "atb": ["2"], "padoms": "{7|8} > {1|2}."},
        {"jaut": "Cik apmēram ir 4{1|8} - 1{7|8}?",
         "atb": ["2"], "padoms": "4 - 2."},
        {"jaut": "Līdz kuram veselam noapaļo 3{2|5}? Ieraksti skaitli.",
         "atb": ["3"], "padoms": "{2|5} < {1|2}."},
        {"jaut": "Līdz kuram veselam noapaļo 2{4|5}? Ieraksti skaitli.",
         "atb": ["3"], "padoms": "{4|5} > {1|2}."},
        {"jaut": "Cik apmēram ir 5{1|6} - 2{5|6}?",
         "atb": ["2"], "padoms": "5 - 3."},
        {"jaut": "Cik apmēram ir 7{1|10} + 2{9|10}?",
         "atb": ["10"], "padoms": "7 + 3."},
        {"jaut": "Cik apmēram ir 6{3|4} - 1{1|4}?",
         "atb": ["6"], "padoms": "7 - 1."},
    ], pamats=4,
        ievads="Salīdzini daļu ar pusi un noapaļo - vairāk nekas nav "
               "jārēķina."),

    Zimejums("Kurš vesels ir tuvāk",
             taisne(0, 3, 1, [(1.9, "1 7/8"), (2.4, "2 2/5")],
                    virsraksts="Viens noapaļojas uz augšu, otrs uz leju"),
             paskaidro="1{7|8} ir gandrīz pie divniekiem, bet 2{2|5} - vēl "
                       "tuvāk divniekam no otras puses.",
             ievads="Noapaļošana ir jautājums, kurš vesels ir tuvāk."),

    Varianti("Vai atbilde ir ticama?", [
        {"jaut": "Kā noapaļo jauktu skaitli līdz veselam?",
         "opcijas": ["Salīdzina daļu ar pusi", "Vienmēr uz augšu",
                     "Vienmēr uz leju", "Pēc saucēja"],
         "pareizi": 0,
         "padoms": "Puse ir robeža."},
        {"jaut": "3{2|5} noapaļots ir...",
         "opcijas": ["3", "4", "3{1|2}", "2"],
         "pareizi": 0,
         "padoms": "{2|5} < {1|2}."},
        {"jaut": "Novērtējums ir 2, bet atbilde iznāca 5. Ko tas nozīmē?",
         "opcijas": ["Kaut kur ir kļūda", "Viss ir kārtībā",
                     "Jānoapaļo citādi", "Atbilde ir precīzāka"],
         "pareizi": 0,
         "padoms": "Novērtējums nekad tik ļoti nekļūdās."},
        {"jaut": "Cik apmēram ir 9{1|9} - 3{8|9}?",
         "opcijas": ["5", "6", "4", "12"],
         "pareizi": 0,
         "padoms": "9 - 4."},
        {"jaut": "Kāpēc novērtē pirms rēķina?",
         "opcijas": ["Lai zinātu, kādai atbildei jāsanāk",
                     "Lai nerēķinātu vispār",
                     "Lai atbilde būtu precīzāka",
                     "Tā nav vajadzīgs"],
         "pareizi": 0,
         "padoms": "Novērtējums ir pārbaude."},
        {"jaut": "2{1|2} noapaļojot...",
         "opcijas": ["Parasti noapaļo uz augšu - līdz 3", "Iznāk 2",
                     "Iznāk 2{1|2}", "Noapaļot nevar"],
         "pareizi": 0,
         "padoms": "Puse ir tieši uz robežas."},
    ], pamats=4),

    Pasaule("Vai materiāla pietiks?",
            Ievadi("", [
                {"jaut": "Ir 4{1|8} l krāsas, vajag 1{7|8} l. Cik apmēram "
                         "paliks litru?",
                 "atb": ["2"], "padoms": "4 - 2."},
                {"jaut": "Ir 5{1|6} m līstes, nogriež 2{5|6} m. Cik apmēram "
                         "paliks metru?",
                 "atb": ["2"], "padoms": "5 - 3."},
                {"jaut": "Ir 7{1|10} kg javas, vajag 2{9|10} kg. Cik apmēram "
                         "paliks kilogramu?",
                 "atb": ["4"], "padoms": "7 - 3."},
                {"jaut": "Vajag 6{3|4} m un ir 7 m. Vai pietiks? Raksti «jā» "
                         "vai «nē».",
                 "atb": ["jā", "ja"], "padoms": "7 > 6{3|4}."},
            ]),
            pavediens="maja",
            konteksts="Veikalā nav laika precīziem rēķiniem - jāzina tikai, "
                      "vai materiāla pietiks.",
            kapec="Novērtējums to pasaka dažās sekundēs."),

    Kopsavilkums([
        "Noapaļoju jauktu skaitli līdz tuvākajam veselam.",
        "Novērtēju starpības aptuveno vērtību pirms aprēķina.",
        "Pamatoju noapaļojumu, salīdzinot daļu ar pusi.",
        "Salīdzinu precīzo atbildi ar novērtējumu.",
    ]),

    Majas([
        "Novērtē un tad izrēķini 8{1|5} - 3{4|5}.",
        "Atrodi piemēru, kurā novērtējums un atbilde atšķiras gandrīz par "
        "vienu.",
        "Uzraksti, kā novērtējums palīdz pamanīt kļūdu.",
    ]),
]
