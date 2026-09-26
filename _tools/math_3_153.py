# -*- coding: utf-8 -*-
"""3. klase, 153. stunda: «Kā savākt un pierakstīt mērījumus?»

Datu vākšana ar plānu. 67. stundā skolēns mācījās mērījumu tabulu; te nāk
klāt plānošana - ko mēra, kas mēra, kādā secībā - un datu apkopošana, kad
mērījumu ir daudz un tos veic vairāki cilvēki.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         restis)

TEMA = "Kā savākt un pierakstīt mērījumus?"

MERKIS = ("Plānosim un veiksim mērījumus apkārtnē, apkopojot tos tabulā.")

SATURS = [
    Sakums("Kā savākt divdesmit mērījumus un nevienu nepazaudēt?",
           zimejums=restis([["objekts", "mērījums", "kas mērīja"],
                            ["gaitenis", "24 m", "Anna"],
                            ["klase", "8 m", "Jānis"],
                            ["zāle", "24 m", "Marta"]],
                           "mērījumu lapa"),
           paraksts="Tabulā ir arī trešā aile - kas mērīja.",
           fakti=["Pirms mērīšanas sastāda plānu.",
                  "Tabulā pieraksta arī to, kas mērīja."]),

    Doma("Vispirms plāns, tad mērījumi",
         "Uzraksti, ko mērīsi, kādā vienībā un kas to darīs - tikai tad ņem "
         "mērlenti.",
         soli=[
             "Saraksti visus objektus, ko mērīsi.",
             "Izvēlies vienu mērvienību visiem.",
             "Sadali objektus starp grupas dalībniekiem.",
             "Pēc mērīšanas apkopo visu vienā tabulā.",
         ],
         pieze="Ja katrs mēra savā vienībā, rezultātus salīdzināt nevar - "
               "tāpēc vienību izvēlas pirms, nevis pēc mērīšanas."),

    Petijums("Izmēri skolas telpas",
             vajag="mērlente, mērījumu lapa un zīmulis",
             soli=[
                 "Sastādiet sarakstu ar pieciem objektiem.",
                 "Vienojieties par mērvienību.",
                 "Sadaliet objektus starp grupas dalībniekiem.",
                 "Apkopojiet visus mērījumus vienā tabulā.",
                 "Sakārtojiet tabulu pēc garuma, sākot ar lielāko.",
             ],
             secinajums="Sakārtota tabula uzreiz parāda, kas ir lielākais un "
                        "kas mazākais."),

    Paraugs("Kā apkopot mērījumus?",
            uzd="Gaitenis 24 m, klase 8 m, zāle 24 m. Cik metru ir kopā un "
                "kurš ir lielākais?",
            soli=[
                ("24 + 8 + 24 = 56",
                 "Kopgarums."),
                ("24 = 24 > 8",
                 "Lielākie ir divi - gaitenis un zāle."),
                ("Kopā 56 m",
                 "Tabula apkopota."),
            ],
            atbilde="56 m; lielākie ir gaitenis un zāle"),

    Ievadi("Apkopo datus", [
        {"jaut": "Gaitenis 24 m, klase 8 m, zāle 24 m. Cik metru kopā?",
         "atb": ["56"], "padoms": "24 + 8 + 24."},
        {"jaut": "Kurš ir garākais? Ieraksti garumu metros.",
         "atb": ["24"], "padoms": "Divi objekti ir vienādi."},
        {"jaut": "Par cik metriem gaitenis ir garāks par klasi?",
         "atb": ["16"], "padoms": "24 − 8."},
        {"jaut": "Pieci mērījumi pa 12 m. Cik metru kopā?", "atb": ["60"],
         "padoms": "5 · 12."},
        {"jaut": "Kopgarums 60 m, pieci objekti. Cik metru vidēji vienam?",
         "atb": ["12"], "padoms": "60 : 5."},
        {"jaut": "Četri mērījumi: 15, 20, 25 un 20 m. Cik metru kopā?",
         "atb": ["80"], "padoms": "35 + 45."},
    ], pamats=4),

    Zimejums("Sakārtota tabula",
             restis([["objekts", "garums"],
                     ["zāle", "24 m"],
                     ["gaitenis", "24 m"],
                     ["klase", "8 m"]],
                    "sakārtots dilstošā secībā"),
             paskaidro="Sakārtotā tabulā atbildi uz jautājumu «kurš "
                       "lielākais» var nolasīt uzreiz.",
             ievads="Tie paši dati, cita kārtība."),

    Varianti("Kā vākt datus?", [
        {"jaut": "Ko dara vispirms?",
         "opcijas": ["Sastāda plānu", "Ņem mērlenti",
                     "Zīmē tabulu", "Mēra pirmo objektu"],
         "pareizi": 0, "padoms": "Bez plāna kaut kas paliks neizmērīts."},
        {"jaut": "Kāpēc visiem jāmēra vienā vienībā?",
         "opcijas": ["Lai rezultātus varētu salīdzināt",
                     "Lai būtu ātrāk", "Tā prasa skolotājs",
                     "Nav vajadzīgs"],
         "pareizi": 0, "padoms": "Metrus un centimetrus salīdzināt nevar "
                                 "tieši."},
        {"jaut": "Kas vēl jāpieraksta tabulā?",
         "opcijas": ["Kas mērīja", "Cik ilgi mērīja", "Kāds laiks bija",
                     "Nekas"],
         "pareizi": 0, "padoms": "Lai varētu pajautāt, ja rodas šaubas."},
        {"jaut": "Seši mērījumi pa 15 m. Cik metru kopā?",
         "opcijas": ["90", "80", "60", "21"],
         "pareizi": 0, "padoms": "6 · 15."},
    ], pamats=4),

    Pasaule("Cik gari ir skolas gaiteņi?",
            Ievadi("", [
                {"jaut": "Trīs gaiteņi: 24 m, 18 m un 30 m. Cik metru kopā?",
                 "atb": ["72"], "padoms": "42 + 30."},
                {"jaut": "Cik metru vidēji ir vienam gaitenim?",
                 "atb": ["24"], "padoms": "72 : 3."},
                {"jaut": "Par cik metriem garākais ir garāks par īsāko?",
                 "atb": ["12"], "padoms": "30 − 18."},
                {"jaut": "Cik reižu jāiet cauri visiem trim, lai sanāktu "
                         "vismaz 500 m?",
                 "atb": ["7"], "padoms": "7 · 72 = 504."},
            ]),
            pavediens="skola",
            konteksts="Skolas plānošanai vajag zināt visu telpu izmērus - un "
                      "tos savāc skolēni paši.",
            kapec="Apkopoti dati ļauj atbildēt uz jautājumiem, kas mērīšanas "
                  "brīdī vēl nebija uzdoti."),

    Kopsavilkums([
        "Plānoju mērījumus pirms to veikšanas.",
        "Vienojos par vienu mērvienību.",
        "Apkopoju mērījumus tabulā.",
        "Sakārtoju tabulu un nolasu no tās atbildes.",
    ]),

    Majas([
        "Izmēri piecas mājas telpas un apkopo datus tabulā.",
        "Sakārto tabulu pēc garuma.",
        "Izrēķini kopgarumu un vidējo garumu.",
    ]),
]
