# -*- coding: utf-8 -*-
"""3. klase, 155. stunda: «Cik maksās klases pasākums?»

Temata pēdējā mācību stunda: grupu darbs ar datiem no teksta un tabulas.
Uzdevums ir atvērts - izmaksas var saplānot dažādi -, un galvenais rezultāts
ir tāme, kuru var pamatot.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         restis)

TEMA = "Cik maksās klases pasākums?"

MERKIS = ("Grupā plānosim pasākuma izmaksas, izmantojot datus no teksta un "
          "tabulas.")

SATURS = [
    Sakums("Cik naudas vajag klases pasākumam?",
           zimejums=restis([["prece", "cena", "vajag"],
                            ["sula", "2 eiro", "8 gab."],
                            ["cepumi", "3 eiro", "5 pac."],
                            ["telpa", "40 eiro", "1"]],
                           "pasākuma tāme"),
           paraksts="Katrai rindai savs rēķins, beigās - kopsumma.",
           fakti=["Tāmē katrai precei ir cena un daudzums.",
                  "Kopsummu iegūst, saskaitot visas rindas."]),

    Doma("Katrai rindai savs rēķins",
         "Reizini cenu ar daudzumu katrā rindā, tad saskaiti visas rindas.",
         soli=[
             "Izraksti visas preces, cenas un daudzumus.",
             "Katrai rindai izrēķini cenu reiz daudzums.",
             "Saskaiti visas rindas.",
             "Salīdzini kopsummu ar naudu, kas ir klases kasē.",
         ],
         pieze="Ja kopsumma ir par lielu, maina vienu rindu un pārrēķina - "
               "tāme tieši tam arī ir domāta."),

    Petijums("Saplānojiet savu pasākumu",
             vajag="cenu saraksts, lapa un zīmulis",
             soli=[
                 "Vienojieties, ko pirksiet.",
                 "Uzzīmējiet tāmi ar trim ailēm.",
                 "Izrēķiniet katru rindu un kopsummu.",
                 "Salīdziniet ar klases kasi un, ja vajag, mainiet plānu.",
             ],
             secinajums="Tāme ir gatava tad, kad kopsumma ietilpst kasē un "
                        "katru rindu var pamatot."),

    Paraugs("Cik maksās pasākums?",
            uzd="8 sulas pa 2 eiro, 5 cepumu paciņas pa 3 eiro, telpa 40 "
                "eiro. Cik maksās viss?",
            soli=[
                ("8 · 2 = 16",
                 "Sulas."),
                ("5 · 3 = 15",
                 "Cepumi."),
                ("16 + 15 + 40 = 71",
                 "Kopsumma ir 71 eiro."),
            ],
            atbilde="71 eiro"),

    Ievadi("Rēķini tāmi", [
        {"jaut": "8 sulas pa 2 eiro. Cik eiro?", "atb": ["16"],
         "padoms": "8 · 2."},
        {"jaut": "5 paciņas pa 3 eiro. Cik eiro?", "atb": ["15"],
         "padoms": "5 · 3."},
        {"jaut": "Cik eiro ir kopā ar telpu par 40 eiro?", "atb": ["71"],
         "padoms": "16 + 15 + 40."},
        {"jaut": "Klases kasē 100 eiro. Cik paliks pāri?", "atb": ["29"],
         "padoms": "100 − 71."},
        {"jaut": "Klasē 25 skolēni. Cik eiro jāsaziedo katram, ja kases nav "
                 "un vajag 75 eiro?",
         "atb": ["3"], "padoms": "75 : 25."},
        {"jaut": "Cik eiro saziedos 25 skolēni pa 4 eiro?", "atb": ["100"],
         "padoms": "25 · 4."},
    ], pamats=4),

    Zimejums("Gatava tāme",
             restis([["rinda", "rēķins", "eiro"],
                     ["sulas", "8 · 2", 16],
                     ["cepumi", "5 · 3", 15],
                     ["telpa", "1 · 40", 40],
                     ["kopā", "", 71]],
                    "viss vienā lapā"),
             paskaidro="Vidējā aile parāda, no kā radies katrs skaitlis - "
                       "tāpēc tāmi var pārbaudīt arī cits.",
             ievads="Tā izskatās pabeigta tāme."),

    Varianti("Kā plānot izmaksas?", [
        {"jaut": "Kurš rēķins der rindai «8 sulas pa 2 eiro»?",
         "opcijas": ["8 · 2", "8 + 2", "8 : 2", "2 : 8"],
         "pareizi": 0, "padoms": "Daudzums reiz cena."},
        {"jaut": "Ko dara, ja kopsumma ir par lielu?",
         "opcijas": ["Maina vienu rindu un pārrēķina",
                     "Atmet tāmi", "Pērk tik un tā", "Neko"],
         "pareizi": 0, "padoms": "Tieši tam tāme ir domāta."},
        {"jaut": "Kāpēc tāmē raksta arī rēķinu?",
         "opcijas": ["Lai to varētu pārbaudīt", "Lai būtu garāka",
                     "Tā prasa skolotājs", "Nav vajadzīgs"],
         "pareizi": 0, "padoms": "Cits redz, no kā radies skaitlis."},
        {"jaut": "25 skolēni pa 3 eiro. Cik eiro sanāk?",
         "opcijas": ["75", "28", "50", "100"],
         "pareizi": 0, "padoms": "25 · 3."},
    ], pamats=4),

    Pasaule("Cik maksās klases ekskursija?",
            Ievadi("", [
                {"jaut": "25 biļetes pa 4 eiro. Cik eiro?", "atb": ["100"],
                 "padoms": "25 · 4."},
                {"jaut": "Autobuss 150 eiro. Cik eiro kopā?",
                 "atb": ["250"], "padoms": "100 + 150."},
                {"jaut": "Cik eiro jāsaziedo katram no 25 skolēniem?",
                 "atb": ["10"], "padoms": "250 : 25."},
                {"jaut": "Ja brauktu 50 skolēni un autobuss maksātu 300 eiro, "
                         "cik eiro būtu katram? (Biļete 4 eiro.)",
                 "atb": ["10"], "padoms": "200 + 300 = 500; 500 : 50."},
            ]),
            pavediens="skola",
            konteksts="Klases ekskursiju plāno kopā: biļetes, autobuss un "
                      "ēdiens - katrs savā rindā.",
            kapec="Tāme pasaka, cik jāsaziedo katram, un to var pārbaudīt "
                  "ikviens."),

    Kopsavilkums([
        "Plānoju pasākuma izmaksas tāmē.",
        "Izmantoju datus no teksta un tabulas.",
        "Izrēķinu katru rindu un kopsummu.",
        "Mainu plānu, ja kopsumma nav pieņemama.",
    ]),

    Majas([
        "Saplāno dzimšanas dienas svinību tāmi ar četrām rindām.",
        "Izrēķini kopsummu.",
        "Pārlasi tematu un atzīmē, kas vēl jāatkārto pirms pārbaudes darba.",
    ], ievads="Šī ir pēdējā stunda pirms pārbaudes darba."),
]
