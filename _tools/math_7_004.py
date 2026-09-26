# -*- coding: utf-8 -*-
"""7. klase, 4. stunda: «Kas ir kopu apvienojums un šķēlums?»

Divas kopas var savienot divējādi: paņemt visu, kas ir kaut vienā
(apvienojums ∪), vai tikai to, kas ir abās (šķēlums ∩). Venna diagrammā
apvienojums ir abi apļi kopā, šķēlums - to kopīgā daļa.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, venna)

TEMA = "Kas ir kopu apvienojums un šķēlums?"

MERKIS = ("Iemācīsimies atrast divu kopu apvienojumu un šķēlumu un "
          "attēlot tos Venna diagrammā.")

SATURS = [
    Sakums("Kuras dziesmas ir abos playlistos?",
           zimejums=venna(["A", "B"], ["E", "F"], ["C", "D"],
                          ("Annas", "Emīla")),
           paraksts="Dziesmas C un D patīk abiem - tās ir šķēlumā.",
           fakti=["Kopīgais playlists ir šķēlums - tikai kopīgās dziesmas.",
                  "Ballītes playlists ir apvienojums - visas dziesmas.",
                  "Kopīgās dziesmas apvienojumā neliek divreiz."]),

    Doma("∪ - kaut vienā, ∩ - abās",
         "Kopu A un B apvienojums A ∪ B ir visi elementi, kas pieder kaut "
         "vienai no kopām. Šķēlums A ∩ B ir elementi, kas pieder abām "
         "kopām.",
         soli=[
             "Uzzīmē divus apļus, kas pārklājas.",
             "Kopīgos elementus ieraksti pārklājumā - tas ir A ∩ B.",
             "Pārējos ieraksti katru savā aplī.",
             "Visi elementi abos apļos kopā ir A ∪ B.",
         ],
         pieze="Ja kopām nav kopīgu elementu, A ∩ B = ∅. Tad apļi "
               "nepārklājas."),

    Paraugs("Apvienojums un šķēlums",
            uzd="A = {1; 2; 3; 4; 6; 12} (12 dalītāji), "
                "B = {1; 2; 3; 6; 9; 18} (18 dalītāji). Atrodi A ∩ B un "
                "A ∪ B.",
            soli=[
                ("A ∩ B = {1; 2; 3; 6}",
                 "Skaitļi, kas ir abos sarakstos - kopīgie dalītāji."),
                ("A ∪ B = {1; 2; 3; 4; 6; 9; 12; 18}",
                 "Visi, bet kopīgos tikai vienu reizi."),
                ("Pārbaude: 6 + 6 − 4 = 8",
                 "Elementu skaits apvienojumā."),
            ],
            atbilde="A ∩ B = {1; 2; 3; 6}; A ∪ B = {1; 2; 3; 4; 6; 9; 12; 18}"),

    Zimejums("Dalītāji Venna diagrammā",
             venna(["4", "12"], ["9", "18"], ["1", "2", "3", "6"],
                   ("12 dalītāji", "18 dalītāji")),
             paskaidro="Lielākais skaitlis šķēlumā - 6 - ir lielākais "
                       "kopīgais dalītājs."),

    Ievadi("Saskaiti elementus", [
        {"jaut": "A = {2; 4; 6; 8}, B = {4; 8; 12}. Cik elementu ir "
                 "A ∩ B?",
         "atb": ["2"], "padoms": "4 un 8."},
        {"jaut": "A = {2; 4; 6; 8}, B = {4; 8; 12}. Cik elementu ir "
                 "A ∪ B?",
         "atb": ["5"], "padoms": "2; 4; 6; 8; 12."},
        {"jaut": "A = {1; 3; 5}, B = {2; 4}. Cik elementu ir A ∩ B?",
         "atb": ["0"], "padoms": "Kopīgu nav - šķēlums ir ∅."},
        {"jaut": "A = {a; b; c}, B = {a; b; c; d}. Cik elementu ir A ∪ B?",
         "atb": ["4"], "padoms": "A ⊂ B, tāpēc A ∪ B = B."},
        {"jaut": "Cik elementu ir šķēlumā: burti vārdā «LATVIJA» un "
                 "burti vārdā «LIETUVA»?",
         "atb": ["5"], "padoms": "L, A, T, V, I."},
        {"jaut": "Cik elementu ir apvienojumā: burti vārdā «LATVIJA» un "
                 "burti vārdā «LIETUVA»?",
         "atb": ["8"], "padoms": "L, A, T, V, I, J, E, U."},
    ], pamats=4),

    Varianti("Kas ir kas?", [
        {"jaut": "A - klases skolēni, kas spēlē basketbolu, B - kas "
                 "spēlē futbolu. Ko nozīmē A ∩ B?",
         "opcijas": ["Skolēni, kas spēlē abas spēles",
                     "Skolēni, kas spēlē kaut vienu",
                     "Skolēni, kas nespēlē neko",
                     "Visi klases skolēni"],
         "pareizi": 0,
         "padoms": "Šķēlums - abās kopās vienlaikus."},
        {"jaut": "Ja A ⊂ B, tad A ∩ B ir...",
         "opcijas": ["A", "B", "∅", "A ∪ B"],
         "pareizi": 0,
         "padoms": "Visi A elementi jau ir B."},
        {"jaut": "Kura zīme nozīmē «vai»?",
         "opcijas": ["∪", "∩", "⊂", "∈"],
         "pareizi": 0,
         "padoms": "Apvienojumā - kaut vienā vai otrā."},
    ]),

    Pasaule("Kopīgie brīvie vakari",
            Ievadi("", [
                {"jaut": "Marta ir brīva P, O, C, S; Kārlis - O, T, S, Sv. "
                         "Cik vakaru viņi var iet uz kino kopā?",
                 "atb": ["2"], "padoms": "O un S - šķēlums."},
                {"jaut": "Cik dažādu nedēļas vakaru ir brīvs kaut viens no "
                         "viņiem?",
                 "atb": ["6"], "padoms": "P, O, T, C, S, Sv."},
                {"jaut": "Cik nedēļas vakaru abi ir aizņemti?",
                 "atb": ["1"], "padoms": "7 − 6."},
            ]),
            pavediens="skola",
            konteksts="Kalendāra lietotne meklē kopīgu laiku tieši tā - "
                      "atrod divu kopu šķēlumu.",
            kapec="Šķēlums ir tas, kas der abiem."),

    Kopsavilkums([
        "Atrodu divu kopu šķēlumu A ∩ B.",
        "Atrodu divu kopu apvienojumu A ∪ B.",
        "Attēloju kopas Venna diagrammā.",
        "Zinu, ka kopīgos elementus apvienojumā raksta vienu reizi.",
    ]),

    Majas([
        "Atrodi 24 un 36 dalītāju šķēlumu un apvienojumu.",
        "Uzzīmē Venna diagrammu savām un drauga mīļākajām ēdienu kopām.",
        "Kad A ∪ B = A? Izdomā piemēru.",
    ]),
]
