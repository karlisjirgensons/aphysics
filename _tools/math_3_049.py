# -*- coding: utf-8 -*-
"""3. klase, 49. stunda: «Cik jāmaksā par klases pasākumu?»

Pirmais garākais uzdevums: trīs darbības, vairāki dati un shematisks
zīmējums. Zīmējums te nav rotājums - tas ir solis, kas neļauj sajaukt, kas ar
ko jāreizina. No šī modeļa vēlāk aug uzdevumu risināšanas shēmas.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, Zimejums,
                         restis)

TEMA = "Cik jāmaksā par klases pasākumu?"

MERKIS = ("Risināsim 2-3 darbību uzdevumu, veidojot shematisku zīmējumu un "
          "pierakstot risinājumu.")

SATURS = [
    Sakums("Cik maksā svētki 24 bērniem?",
           zimejums=restis([["24 bērni", "×", "3 cepumi"],
                            ["24 bērni", "×", "1 sula"],
                            ["telpa", "", "200 ct"]],
                           "trīs izdevumu daļas"),
           paraksts="Katra rinda ir viens rēķins; kopsummu saskaita beigās.",
           fakti=["Garā uzdevumā vispirms saprot, kas ar ko jāreizina.",
                  "Shēma to parāda ātrāk nekā teksts."]),

    Doma("Vispirms shēma, tad rēķins",
         "Uzzīmē, kas ir grupas un kas - grupas lielums; tikai tad raksti "
         "darbības.",
         soli=[
             "Izraksti visus skaitļus un pieraksti, ko katrs nozīmē.",
             "Uzzīmē shēmu: cik grupu un cik katrā.",
             "Izrēķini katru daļu atsevišķi.",
             "Saskaiti daļas kopā.",
             "Pārbaudi, vai atbilde ir saprātīga.",
         ],
         pieze="Ja skaitļu ir daudz, viens no tiem uzdevumā var būt lieks - "
               "shēma parāda, kurš tajā neiederas."),

    Slidnis("Kā aug kopsumma",
            soli=[
                {"v": "24 · 3 = 72",
                 "teksts": "Cepumi: 24 bērni pa 3 cepumiem.", "josla": 25},
                {"v": "72 · 2 = 144",
                 "teksts": "Cepums maksā 2 ct.", "josla": 50},
                {"v": "24 · 5 = 120",
                 "teksts": "Sula: 24 bērni pa 5 ct.", "josla": 75},
                {"v": "144 + 120 = 264",
                 "teksts": "Kopā par ēdienu.", "josla": 100},
            ],
            ievads="Spied soļus un skaties, kā katra daļa pieliek savu summu."),

    Paraugs("Cik maksās pasākums?",
            uzd="Klasē 24 bērni. Katram vajag 3 cepumus pa 2 ct un vienu "
                "sulu par 5 ct. Cik maksās viss?",
            soli=[
                ("24 · 3 = 72",
                 "Cik cepumu vajag pavisam."),
                ("72 · 2 = 144",
                 "Cik maksā visi cepumi."),
                ("24 · 5 = 120",
                 "Cik maksā visas sulas."),
                ("144 + 120 = 264",
                 "Kopsumma; pārbaude: 264 ct ir mazāk par 3 eiro."),
            ],
            atbilde="264 ct"),

    Ievadi("Rēķini pa daļām", [
        {"jaut": "20 bērni, katram 2 cepumi. Cik cepumu vajag?",
         "atb": ["40"], "padoms": "20 · 2."},
        {"jaut": "Cepums maksā 3 ct. Cik maksā 40 cepumi?",
         "atb": ["120"], "padoms": "40 · 3."},
        {"jaut": "20 sulas pa 6 ct. Cik maksā?",
         "atb": ["120"], "padoms": "20 · 6."},
        {"jaut": "Cik maksā cepumi un sulas kopā?",
         "atb": ["240"], "padoms": "120 + 120."},
        {"jaut": "Klases kasē 300 ct. Cik paliks pāri?",
         "atb": ["60"], "padoms": "300 − 240."},
        {"jaut": "Cik tas ir uz vienu bērnu?",
         "atb": ["3"], "padoms": "60 : 20."},
    ], pamats=4),

    Zimejums("Uzdevuma shēma",
             restis([["daļa", "rēķins", "summa"],
                     ["cepumi", "24 · 3 · 2", "144"],
                     ["sulas", "24 · 5", "120"],
                     ["kopā", "144 + 120", "264"]],
                    "trīs rindas, viena atbilde"),
             paskaidro="Katrai izdevumu daļai sava rinda - tad neviens "
                       "skaitlis nepaliek neizmantots.",
             ievads="Tā izskatās pasākuma tāme."),

    Varianti("Kura darbība ir pirmā?", [
        {"jaut": "«24 bērni, katram 3 cepumi pa 2 ct» - kura darbība pirmā?",
         "opcijas": ["24 · 3", "3 · 2", "24 · 2", "24 + 3"],
         "pareizi": 0, "padoms": "Vispirms cik cepumu, tad cik maksā."},
        {"jaut": "Kura izteiksme dod to pašu atbildi?",
         "opcijas": ["24 · (3 · 2)", "24 + 3 · 2", "(24 + 3) · 2",
                     "24 · 3 + 2"],
         "pareizi": 0, "padoms": "Reizinātājus var grupēt, kā ērtāk."},
        {"jaut": "Kāpēc uzdevumā vajadzīga shēma?",
         "opcijas": ["Lai redzētu, kas ar ko jāreizina",
                     "Lai darbs izskatītos skaistāks",
                     "Tā prasa skolotājs", "Lai būtu ātrāk"],
         "pareizi": 0, "padoms": "Shēma novērš sajaukšanu."},
        {"jaut": "Kā pārbaudīt, vai atbilde ir saprātīga?",
         "opcijas": ["Salīdzināt ar naudu, kas ir klases kasē",
                     "Pārrakstīt atbildi", "Izrēķināt vēlreiz tāpat",
                     "Nekā"],
         "pareizi": 0, "padoms": "Atbildei jāiederas dzīvē."},
    ], pamats=4),

    Pasaule("Cik maksās ekskursija?",
            Ievadi("", [
                {"jaut": "25 bērni, biļete 4 ct. Cik maksā biļetes?",
                 "atb": ["100"], "padoms": "25 · 4."},
                {"jaut": "Autobuss maksā 150 ct. Cik kopā ar biļetēm?",
                 "atb": ["250"], "padoms": "100 + 150."},
                {"jaut": "Cik tas ir uz vienu bērnu?",
                 "atb": ["10"], "padoms": "250 : 25."},
                {"jaut": "Ja brauktu 50 bērni, cik maksātu uz vienu, "
                         "autobusam paliekot 150 ct? (Biļete 4 ct.)",
                 "atb": ["7"], "padoms": "50 · 4 = 200; 200 + 150 = 350; "
                                         "350 : 50."},
            ]),
            pavediens="skola",
            konteksts="Jo vairāk bērnu brauc, jo lētāk iznāk uz vienu - "
                      "autobusa cena taču nemainās.",
            kapec="Tieši šis rēķins izšķir, vai ekskursija vispār notiks."),

    Kopsavilkums([
        "Risinu 2-3 darbību situācijas uzdevumu.",
        "Veidoju shematisku zīmējumu vai tāmi.",
        "Rēķinu katru izdevumu daļu atsevišķi un saskaitu kopā.",
        "Pārbaudu, vai atbilde ir saprātīga.",
    ]),

    Majas([
        "Izrēķini, cik maksātu dzimšanas dienas svinības 10 viesiem.",
        "Uzzīmē tāmi ar trim rindām un kopsummu.",
        "Pastāsti mājiniekiem, kāpēc lielākai grupai iznāk lētāk.",
    ]),
]
