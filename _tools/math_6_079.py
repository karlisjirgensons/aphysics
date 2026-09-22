# -*- coding: utf-8 -*-
"""6. klase, 79. stunda: «Kāda likumsakarība ir ķermeņu virknē?»

Temata pēdējā mācību stunda. Virkne ķermeņu, kuru izmēri aug pēc likuma,
savieno šo tematu ar visu pārējo matemātiku: jāatrod likums, jāpieraksta tas
un jāparedz nākamais loceklis - to pašu prasa skaitļu virknes.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         restis)

TEMA = "Kāda likumsakarība ir ķermeņu virknē?"

MERKIS = ("Pētīsim sakarības starp daudzskaldņu lielumiem virknē un "
          "formulēsim likumsakarību.")

SATURS = [
    Sakums("Kubu virkne aug pēc likuma",
           zimejums=restis([["šķautne", "1", "2", "3", "4"],
                            ["tilpums", "1", "8", "27", "64"]]),
           paraksts="Katrs tilpums ir šķautne trešajā pakāpē. Nākamais būs "
                    "125.",
           fakti=["Virknē svarīgs nav skaitlis, bet likums.",
                  "Ja likums atrasts, nākamo locekli var pateikt uzreiz.",
                  "To pašu prasa gan ķermeņu, gan skaitļu virknes."]),

    Doma("Atrodi likumu, tad pieraksti to",
         "Ķermeņu virknē vispirms salīdzina blakus locekļus, atrod likumu un "
         "tikai tad rēķina nākamo.",
         soli=[
             "Izveido tabulu: virknes numurs un lielums.",
             "Salīdzini blakus locekļus: cik pieaug vai cik reižu?",
             "Pārbaudi likumu uz vairākiem locekļiem.",
             "Pieraksti likumu vārdiem vai izteiksmē.",
             "Aprēķini nākamo un pārbaudi to.",
         ],
         pieze="Ja starpība nav vienāda, meklē citu likumu: varbūt lielums "
               "aug tikpat reižu vai ir kāpinājums. Tilpumu virknē visbiežāk "
               "ir tieši kāpinājums."),

    Paraugs("Virkne kastēm ar augošu augstumu",
            uzd="Kastes pamats ir 4 x 3 cm, augstums 1, 2, 3 un 4 cm. Kāda "
                "ir tilpuma likumsakarība?",
            soli=[
                ("Tilpumi: 12, 24, 36, 48 cm³",
                 "Katram augstumam savs tilpums."),
                ("Starpība vienmēr 12",
                 "Likums ir saskaitīšana."),
                ("Tilpums ir 12 reiz augstums",
                 "Pamata laukums ir nemainīgs."),
                ("Piektais loceklis: 12 · 5 = 60 cm³",
                 "Likums ļauj pateikt uzreiz."),
            ],
            atbilde="tilpums aug par 12 cm³; piektais ir 60 cm³"),

    Ievadi("Turpini virkni", [
        {"jaut": "Tilpumi 12, 24, 36. Kāds ir nākamais?",
         "atb": ["48"], "padoms": "Starpība 12."},
        {"jaut": "Tilpumi 1, 8, 27. Kāds ir nākamais?",
         "atb": ["64"], "padoms": "Šķautne trešajā pakāpē."},
        {"jaut": "Virsmas 6, 24, 54. Kāda ir nākamā?",
         "atb": ["96"], "padoms": "6 reiz šķautne kvadrātā."},
        {"jaut": "Kuba tilpums ir 125 cm³. Cik cm ir šķautne?",
         "atb": ["5"], "padoms": "5 · 5 · 5."},
        {"jaut": "Tilpumi 20, 40, 60. Kāds ir piektais loceklis?",
         "atb": ["100"], "padoms": "Starpība 20."},
        {"jaut": "Tilpumi 2, 4, 8, 16. Kāds ir nākamais?",
         "atb": ["32"], "padoms": "Katrs divreiz lielāks."},
    ], pamats=4),

    Petijums("Izveido savu virkni",
             vajag="burtnīca un kubiņi",
             soli=[
                 "Izvēlies pamatu 3 x 2 kubiņi.",
                 "Saliec kastes ar augstumu 1, 2 un 3 slāņi.",
                 "Pieraksti katras tilpumu un virsmu tabulā.",
                 "Atrodi likumu abiem lielumiem.",
                 "Paredzi ceturtās kastes tilpumu un pārbaudi to.",
             ],
             secinajums="Tilpums aug vienmērīgi, jo pamats nemainās; virsma "
                        "aug citādi, jo augšējā un apakšējā skaldne paliek "
                        "tās pašas."),

    Varianti("Kāds ir likums?", [
        {"jaut": "Virknē 5, 10, 15, 20 likums ir...",
         "opcijas": ["pieskaitīt 5", "reizināt ar 2",
                     "kāpināt kvadrātā", "atņemt 5"],
         "pareizi": 0,
         "padoms": "Starpība ir vienāda."},
        {"jaut": "Virknē 1, 8, 27, 64 likums ir...",
         "opcijas": ["kāpināt trešajā pakāpē", "pieskaitīt 7",
                     "reizināt ar 8", "pieskaitīt 19"],
         "pareizi": 0,
         "padoms": "Kubu tilpumi."},
        {"jaut": "Kā pārbaudīt, vai likums ir pareizs?",
         "opcijas": ["Uz vairākiem locekļiem", "Uz viena locekļa",
                     "Uz pēdējā locekļa", "Pārbaudīt nevar"],
         "pareizi": 0,
         "padoms": "Viens loceklis var sakrist nejauši."},
        {"jaut": "Kastēm ar vienādu pamatu tilpums aug...",
         "opcijas": ["vienmērīgi līdz ar augstumu",
                     "kvadrātā", "trešajā pakāpē", "nemainīgi"],
         "pareizi": 0,
         "padoms": "Pamata laukums ir nemainīgs reizinātājs."},
    ], pamats=4),

    Pasaule("Cik ietilpīga būs nākamā tvertne?",
            Ievadi("", [
                {"jaut": "Tvertņu tilpumi ir 50, 100, 150 l. Cik litru būs "
                         "ceturtajai?",
                 "atb": ["200"], "padoms": "Starpība 50."},
                {"jaut": "Citā sērijā tilpumi ir 10, 20, 40 l. Cik litru būs "
                         "ceturtajai?",
                 "atb": ["80"], "padoms": "Katra divreiz lielāka."},
                {"jaut": "Kubveida tvertnes ar šķautni 1, 2 un 3 m. Cik m³ "
                         "ir trešā?",
                 "atb": ["27"], "padoms": "3 · 3 · 3."},
                {"jaut": "Cik m³ būs ceturtajai?",
                 "atb": ["64"], "padoms": "4 · 4 · 4."},
            ]),
            pavediens="planeta",
            konteksts="Tvertnes ražo sērijās, un to izmēri aug pēc likuma - "
                      "tāpēc katalogā nākamo var paredzēt.",
            kapec="Likumsakarība ļauj pateikt atbildi, to neizmērot."),

    Kopsavilkums([
        "Izveidoju tabulu ķermeņu virknes lielumiem.",
        "Atrodu likumsakarību un pārbaudu to uz vairākiem locekļiem.",
        "Pierakstu likumu vārdiem vai izteiksmē.",
        "Paredzu nākamo virknes locekli.",
    ]),

    Majas([
        "Izveido virkni no trim kastēm ar vienādu pamatu un pieraksti "
        "tilpumus.",
        "Atrodi likumu un paredzi ceturto tilpumu.",
        "Pieraksti, kāpēc virsmas likums ir citāds nekā tilpuma.",
    ]),
]
