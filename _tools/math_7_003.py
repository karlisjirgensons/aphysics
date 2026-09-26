# -*- coding: utf-8 -*-
"""7. klase, 3. stunda: «Kas ir apakškopa?»

Apakškopa ir kopa, kuras visi elementi pieder arī citai kopai. Labākais
piemērs ir četrstūru klasifikācija: katrs kvadrāts ir taisnstūris, katrs
taisnstūris - paralelograms. Stunda iemāca zīmi ⊂ un to, ka «katrs»
jāpārbauda līdz galam.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kas ir apakškopa?"

MERKIS = ("Uzzināsim, kas ir apakškopa, un sakārtosim četrstūrus pēc tā, "
          "kurš ir kura apakškopa.")

SATURS = [
    Sakums("Katrs kvadrāts ir taisnstūris. Bet otrādi?",
           fakti=["Kvadrātam ir visas taisnstūra īpašības - un vēl viena.",
                  "Tāpēc kvadrātu kopa ir taisnstūru kopas apakškopa.",
                  "Ne katrs taisnstūris ir kvadrāts: 2 cm × 5 cm nav."]),

    Doma("B ⊂ A, ja katrs B elements pieder A",
         "Kopa B ir kopas A apakškopa (B ⊂ A), ja katrs kopas B elements ir "
         "arī kopas A elements.",
         soli=[
             "Paņem katru B elementu pēc kārtas.",
             "Pārbaudi, vai tas ir arī kopā A.",
             "Ja visi ir - B ⊂ A.",
             "Ja kaut viens nav - B nav A apakškopa.",
         ],
         pieze="Tukšā kopa ir jebkuras kopas apakškopa, un katra kopa ir "
               "pati savas apakškopa: A ⊂ A."),

    Zimejums("Četrstūru ģimene",
             restis([["četrstūri"], ["paralelogrami"], ["taisnstūri"],
                     ["kvadrāti"]]),
             ievads="Katra nākamā rinda ir iepriekšējās apakškopa.",
             paskaidro="Kvadrāti ⊂ taisnstūri ⊂ paralelogrami ⊂ četrstūri."),

    Paraugs("Pārbaudi apakškopu",
            uzd="A = {1; 2; 3; 4; 5; 6}, B = {2; 4; 6}, C = {4; 6; 8}. "
                "Vai B ⊂ A? Vai C ⊂ A?",
            soli=[
                ("2 ∈ A, 4 ∈ A, 6 ∈ A",
                 "Visi B elementi ir kopā A."),
                ("B ⊂ A", "Apakškopa."),
                ("8 ∉ A", "Viens C elements nav kopā A."),
                ("C nav A apakškopa", "Pietiek ar vienu izņēmumu."),
            ],
            atbilde="B ⊂ A; C nav kopas A apakškopa"),

    Varianti("Apakškopa vai nē?", [
        {"jaut": "Kura kopa ir {1; 3; 5; 7; 9} apakškopa?",
         "opcijas": ["{3; 7}", "{2; 3}", "{1; 11}", "{5; 6; 7}"],
         "pareizi": 0,
         "padoms": "Visiem elementiem jābūt dotajā kopā."},
        {"jaut": "Kurš apgalvojums ir patiess?",
         "opcijas": ["Kvadrātu kopa ⊂ rombu kopa",
                     "Rombu kopa ⊂ kvadrātu kopa",
                     "Taisnstūru kopa ⊂ kvadrātu kopa",
                     "Paralelogramu kopa ⊂ taisnstūru kopa"],
         "pareizi": 0,
         "padoms": "Kvadrātam visas malas ir vienādas - tātad tas ir rombs."},
        {"jaut": "Pāra skaitļu kopa un skaitļu, kas dalās ar 4, kopa. "
                 "Kura ir kuras apakškopa?",
         "opcijas": ["Dalās ar 4 ⊂ pāra skaitļi",
                     "Pāra skaitļi ⊂ dalās ar 4",
                     "Neviena nav otras apakškopa",
                     "Tās ir vienādas"],
         "pareizi": 0,
         "padoms": "6 ir pāra skaitlis, bet nedalās ar 4."},
        {"jaut": "Vai ∅ ir kopas {1; 2} apakškopa?",
         "opcijas": ["Jā, tā ir jebkuras kopas apakškopa",
                     "Nē, tajā nav elementu",
                     "Tikai tad, ja kopā ir 0",
                     "Nevar zināt"],
         "pareizi": 0,
         "padoms": "Tukšajā kopā nav neviena elementa, kas «neder»."},
    ], pamats=4),

    Ievadi("Cik apakškopu ar noteikumu?", [
        {"jaut": "A = {2; 5; 8}. Cik ir A apakškopu ar tieši 1 elementu?",
         "atb": ["3"], "padoms": "{2}, {5}, {8}."},
        {"jaut": "A = {2; 5; 8}. Cik ir A apakškopu ar tieši 2 elementiem?",
         "atb": ["3"], "padoms": "{2; 5}, {2; 8}, {5; 8}."},
        {"jaut": "Kuru elementu vajag pievienot {1; 2}, lai tā nebūtu "
                 "kopas {1; 2; 3; 4} apakškopa - 3 vai 5?",
         "atb": ["5"], "padoms": "Kurš nav lielajā kopā?"},
        {"jaut": "Cik elementu ir lielākajai kopas {a; b; c; d} "
                 "apakškopai?",
         "atb": ["4"], "padoms": "Kopa pati sev ir apakškopa."},
    ]),

    Pasaule("Dzīvnieku klasifikācija",
            Varianti("", [
                {"jaut": "Kura sakarība ir patiesa?",
                 "opcijas": ["suņi ⊂ zīdītāji", "zīdītāji ⊂ suņi",
                             "putni ⊂ zīdītāji", "zivis ⊂ putni"],
                 "pareizi": 0,
                 "padoms": "Katrs suns ir zīdītājs."},
                {"jaut": "Pingvīni ⊂ putni. Ko tas nozīmē?",
                 "opcijas": ["Katrs pingvīns ir putns",
                             "Katrs putns ir pingvīns",
                             "Pingvīni nav putni",
                             "Daži putni ir pingvīni, daži pingvīni - nē"],
                 "pareizi": 0,
                 "padoms": "Apakškopa nozīmē «katrs elements»."},
                {"jaut": "Vaļi ir zīdītāji un dzīvo jūrā. Ko var secināt?",
                 "opcijas": ["Ne visi jūras dzīvnieki ir zivis",
                             "Vaļi ⊂ zivis",
                             "Jūras dzīvnieki ⊂ zivis",
                             "Zīdītāji ⊂ jūras dzīvnieki"],
                 "pareizi": 0,
                 "padoms": "Valis ir jūrā, bet nav zivs."},
            ]),
            pavediens="daba",
            konteksts="Biologi dzīvniekus kārto kopās, kur katra nākamā ir "
                      "iepriekšējās apakškopa.",
            kapec="Viens pretpiemērs pierāda, ka kopa nav apakškopa."),

    Kopsavilkums([
        "Zinu, ka B ⊂ A nozīmē: katrs B elements pieder A.",
        "Pārbaudu apakškopu pa elementiem.",
        "Ar vienu pretpiemēru parādu, ka kopa nav apakškopa.",
        "Kārtoju četrstūrus: kvadrāti ⊂ taisnstūri ⊂ paralelogrami.",
    ]),

    Majas([
        "Uzraksti ķēdi no trim kopām, kur katra ir nākamās apakškopa.",
        "Vai rombu kopa ir taisnstūru kopas apakškopa? Pamato.",
        "Uzraksti visas {x; y} apakškopas.",
    ]),
]
