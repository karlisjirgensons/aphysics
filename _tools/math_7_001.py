# -*- coding: utf-8 -*-
"""7. klase, 1. stunda: «Kas ir kopa?»

Kopa ir matemātikas vārds tam, ko ikdienā sauc par komandu, kolekciju vai
sarakstu. Stunda sāk ar to, ka kopa ir jebkurš skaidri noteikts objektu
kopums, un iemāca pierakstu ar figūriekavām un zīmēm ∈ un ∉.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, venna)

TEMA = "Kas ir kopa?"

MERKIS = ("Uzzināsim, kas matemātikā ir kopa un tās elementi, un "
          "iemācīsimies to pierakstīt.")

SATURS = [
    Sakums("Playlist, komanda, klase - visas ir kopas",
           fakti=["Mūzikas lietotnes playlist ir dziesmu kopa.",
                  "Latvijas izlase ir spēlētāju kopa - katrs ir vai nav tajā.",
                  "Kopā katrs elements ir tieši vienu reizi."]),

    Doma("Kopa ir skaidri noteikts objektu kopums",
         "Kopa ir objektu kopums, par kuru vienmēr var pateikt, vai dotais "
         "objekts tajā ietilpst. Objektus sauc par kopas elementiem.",
         soli=[
             "Kopu apzīmē ar lielo burtu: A, B, M.",
             "Elementus raksta figūriekavās un atdala ar semikolu: "
             "A = {2; 4; 6}.",
             "3 ∈ B lasa «3 pieder kopai B».",
             "5 ∉ A lasa «5 nepieder kopai A».",
             "Kopa bez neviena elementa ir tukšā kopa ∅.",
         ],
         pieze="«Skaistas dziesmas» nav kopa: par to, vai dziesma ir "
               "skaista, katrs spriež citādi. Kopai vajag skaidru noteikumu."),

    Paraugs("Pieraksti kopu",
            uzd="Kopa C ir visi viencipara pāra skaitļi, kas lielāki nekā 3. "
                "Pieraksti to un nosaki, vai 8 ∈ C un vai 2 ∈ C.",
            soli=[
                ("Viencipara pāra skaitļi: 0; 2; 4; 6; 8",
                 "Uzskaita visus, lai neviens nepaliek ārpusē."),
                ("Lielāki nekā 3: 4; 6; 8",
                 "0 un 2 atmet."),
                ("C = {4; 6; 8}",
                 "Figūriekavas, elementi atdalīti ar semikolu."),
                ("8 ∈ C, bet 2 ∉ C",
                 "8 ir sarakstā, 2 - nav."),
            ],
            atbilde="C = {4; 6; 8}; 8 ∈ C; 2 ∉ C"),

    Varianti("Kopa vai nav kopa?", [
        {"jaut": "Kura no šīm ir kopa?",
         "opcijas": ["Latvijas galvaspilsētas skolas",
                     "Garšīgas pusdienas",
                     "Interesantas grāmatas",
                     "Garie cilvēki klasē"],
         "pareizi": 0,
         "padoms": "Kopai vajag noteikumu, par kuru nav jāstrīdas."},
        {"jaut": "A = {1; 3; 5; 7}. Kurš apgalvojums ir patiess?",
         "opcijas": ["5 ∈ A", "4 ∈ A", "7 ∉ A", "1 ∉ A"],
         "pareizi": 0,
         "padoms": "Pārbaudi, vai skaitlis ir starp figūriekavām."},
        {"jaut": "Kas ir ∅?",
         "opcijas": ["Kopa bez neviena elementa", "Skaitlis nulle",
                     "Kopa ar elementu 0", "Jebkura kopa"],
         "pareizi": 0,
         "padoms": "{0} ir kopa ar vienu elementu - nulli."},
        {"jaut": "Kā pareizi pierakstīt kopu no burtiem vārdā «ALA»?",
         "opcijas": ["{A; L}", "{A; L; A}", "{ALA}", "(A; L)"],
         "pareizi": 0,
         "padoms": "Kopā katrs elements ir tikai vienu reizi."},
    ], pamats=4),

    Ievadi("Cik elementu kopā?", [
        {"jaut": "Cik elementu ir kopā {2; 4; 6; 8; 10}?",
         "atb": ["5"], "padoms": "Saskaiti elementus."},
        {"jaut": "Cik elementu ir kopā no burtiem vārdā «MATEMĀTIKA»?",
         "atb": ["7"], "padoms": "M, A, T, E, Ā, I, K - katru vienu reizi."},
        {"jaut": "Cik elementu ir kopā ∅?",
         "atb": ["0"], "padoms": "Tukšā kopa."},
        {"jaut": "Cik elementu ir kopā no nedēļas dienām, kuru nosaukums "
                 "sākas ar «p»?",
         "atb": ["2"], "padoms": "Pirmdiena un piektdiena."},
        {"jaut": "Cik divciparu skaitļu ir kopā, kuros abi cipari ir 5 "
                 "vai 7?",
         "atb": ["4"], "padoms": "55; 57; 75; 77."},
        {"jaut": "Cik elementu ir kopā {0}?",
         "atb": ["1"], "padoms": "Tā nav tukša - tajā ir nulle."},
    ], pamats=4),

    Zimejums("Kopa kā aplis",
             venna(["3", "9"], ["4", "8"], ["6"],
                   ("dalās ar 3", "pāra")),
             ievads="Kopu ērti zīmēt kā apli: iekšā ir tās elementi.",
             paskaidro="Skaitlis 6 ir abās kopās - tas dalās ar 3 un ir pāra."),

    Pasaule("Kurš ir izlasē?",
            Ievadi("", [
                {"jaut": "Treneris izlasē ņem visus, kas 60 m noskrēja "
                         "ātrāk nekā 9 s. Laiki: 8,6; 9,4; 8,9; 9,0; 8,7. "
                         "Cik skrējēju ir izlases kopā?",
                 "atb": ["3"], "padoms": "9,0 nav ātrāk nekā 9 s."},
                {"jaut": "Izlases kopa ir S = {Anna; Rihards; Elza}. "
                         "Vai Rihards ∈ S? Raksti «jā» vai «nē».",
                 "atb": ["jā", "ja"], "padoms": "Viņš ir sarakstā."},
                {"jaut": "Ja visi skrējēji būtu lēnāki par 9 s, cik elementu "
                         "būtu izlases kopā?",
                 "atb": ["0"], "padoms": "Tad izlase ir tukšā kopa."},
            ]),
            pavediens="sports",
            konteksts="Izlasē iekļauj pēc skaidra noteikuma - tieši tāpēc "
                      "tā ir kopa.",
            kapec="Skaidrs noteikums nozīmē, ka par izlasi nav jāstrīdas."),

    Kopsavilkums([
        "Zinu, ka kopa ir skaidri noteikts objektu kopums.",
        "Pierakstu kopu ar figūriekavām: A = {2; 4; 6}.",
        "Lietoju zīmes ∈ un ∉.",
        "Zinu, ka tukšā kopa ∅ ir kopa bez elementiem.",
    ]),

    Majas([
        "Pieraksti trīs kopas no savas dzīves (ar noteikumu!).",
        "Uzraksti vienu «nekopu» un paskaidro, kāpēc tā nav kopa.",
        "Pieraksti kopu no burtiem savā vārdā un saskaiti elementus.",
    ]),
]
