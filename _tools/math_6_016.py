# -*- coding: utf-8 -*-
"""6. klase, 16. stunda: «Kā uzzīmēt plānu mērogā?»

Temata pēdējā mācību stunda un programmas praktiskā daļa: grupa izmēra īstu
telpu un uzzīmē to mērogā. Pirms izejas no soliem - īss atgādinājums par
visu, kas šajā tematā mācīts, jo plānā satiekas attiecība, dalīšana un
mērvienības.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         restis)

TEMA = "Kā uzzīmēt plānu mērogā?"

MERKIS = ("Grupā veiksim mērījumus un uzzīmēsim telpas vai dobes plānu "
          "norādītajā mērogā.")

SATURS = [
    Sakums("Arhitekts sāk ar mērlenti",
           zimejums=restis([["6 m", "→", "12 cm"],
                            ["4 m", "→", "8 cm"]],
                           "mērogs 1 : 50"),
           paraksts="6 m ir 600 cm; 600 : 50 = 12 cm. Tik gara būs līnija "
                    "lapā.",
           fakti=["Plānā vispirms izvēlas mērogu, tad zīmē.",
                  "Ja mērogs izvēlēts slikti, plāns neietilpst lapā."]),

    Doma("Izvēlies mērogu pēc lapas",
         "Mērogu izvēlas tā, lai lielākais izmērs ietilptu lapā - un tikai "
         "tad pārrēķina visus pārējos.",
         soli=[
             "Izmēri telpu un pieraksti izmērus metros.",
             "Pārvērt tos centimetros.",
             "Izvēlies mērogu tā, lai lielākais izmērs sanāktu mazāks par "
             "lapas malu.",
             "Izdali katru izmēru ar mēroga skaitli.",
             "Uzzīmē plānu un pieraksti mērogu zem tā.",
         ],
         pieze="Mērogs jāpieraksta obligāti. Plāns bez mēroga ir tikai "
               "zīmējums - no tā neko izmērīt nevar."),

    Paraugs("Klases plāns mērogā 1 : 50",
            uzd="Klase ir 6 m gara un 4 m plata. Cik liels būs plāns mērogā "
                "1 : 50?",
            soli=[
                ("6 m = 600 cm; 4 m = 400 cm",
                 "Abus izmērus vienā mērvienībā."),
                ("600 : 50 = 12 cm",
                 "Garums plānā."),
                ("400 : 50 = 8 cm",
                 "Platums plānā."),
                ("12 cm x 8 cm ietilpst A4 lapā",
                 "Mērogs izvēlēts labi."),
            ],
            atbilde="taisnstūris 12 cm x 8 cm"),

    Ievadi("Pārrēķini izmērus plānam", [
        {"jaut": "Mērogs 1 : 50. Siena ir 3 m. Cik cm tā ir plānā?",
         "atb": ["6"], "padoms": "300 : 50."},
        {"jaut": "Tas pats mērogs. Siena ir 5 m. Cik cm plānā?",
         "atb": ["10"], "padoms": "500 : 50."},
        {"jaut": "Mērogs 1 : 100. Dobe ir 2,5 m. Cik cm plānā?",
         "atb": ["2,5", "2.5"], "padoms": "250 : 100."},
        {"jaut": "Mērogs 1 : 25. Galds ir 1,5 m. Cik cm plānā?",
         "atb": ["6"], "padoms": "150 : 25."},
        {"jaut": "Plānā mērogā 1 : 50 durvis ir 1,6 cm. Cik cm tās ir dabā?",
         "atb": ["80"], "padoms": "1,6 · 50."},
        {"jaut": "Zāle ir 20 m gara. Kāds mērogs vajadzīgs, lai plānā tā "
                 "būtu 20 cm? Ieraksti tikai otro skaitli.",
         "atb": ["100"], "padoms": "2000 cm : 20 cm."},
    ], pamats=4),

    Varianti("Vai plāns iznāks?", [
        {"jaut": "Telpa 10 m, mērogs 1 : 20. Cik cm plānā?",
         "opcijas": ["50 cm - A4 lapā neietilps", "20 cm",
                     "10 cm", "5 cm"],
         "pareizi": 0,
         "padoms": "1000 : 20."},
        {"jaut": "Kurš mērogs der 12 m garai zālei uz A4 lapas?",
         "opcijas": ["1 : 100", "1 : 10", "1 : 5", "1 : 2"],
         "pareizi": 0,
         "padoms": "1200 : 100 = 12 cm."},
        {"jaut": "Ko obligāti pieraksta zem plāna?",
         "opcijas": ["Mērogu", "Zīmētāja vārdu", "Datumu", "Lapas numuru"],
         "pareizi": 0,
         "padoms": "Bez mēroga plāns neko nemēra."},
        {"jaut": "Divās sienās sanāca 8 cm un 12 cm. Kāda ir to attiecība?",
         "opcijas": ["2 : 3", "3 : 2", "8 : 10", "1 : 2"],
         "pareizi": 0,
         "padoms": "Abus dala ar 4."},
    ], pamats=4),

    Petijums("Uzzīmējiet klases plānu",
             vajag="mērlente, rūtiņu lapa, lineāls; strādājiet pa trim",
             soli=[
                 "Izmēriet klases garumu un platumu ar mērlenti.",
                 "Izmēriet durvju un vismaz viena loga platumu.",
                 "Izvēlieties mērogu tā, lai plāns ietilptu lapā.",
                 "Pārrēķiniet visus izmērus un uzzīmējiet plānu.",
                 "Pierakstiet mērogu un salīdziniet plānus ar citu grupu.",
             ],
             secinajums="Ja abas grupas mērīja pareizi, plāni būs vienādi "
                        "pēc formas, arī tad, ja mērogs izvēlēts cits."),

    Pasaule("Cik materiāla vajag telpai?",
            Ievadi("", [
                {"jaut": "Klase ir 6 m x 4 m. Cik kvadrātmetru ir grīda?",
                 "atb": ["24"], "padoms": "6 · 4."},
                {"jaut": "Grīdas segums maksā 9 € par kvadrātmetru. Cik eiro "
                         "maksā visa grīda?",
                 "atb": ["216"], "padoms": "24 · 9."},
                {"jaut": "Plānā mērogā 1 : 50 klase ir 12 cm x 8 cm. Cik "
                         "kvadrātcentimetru aizņem plāns?",
                 "atb": ["96"], "padoms": "12 · 8."},
                {"jaut": "Ap klasi liek līsti. Cik metru līstes vajag?",
                 "atb": ["20"], "padoms": "Perimetrs: 2 · (6 + 4)."},
            ]),
            pavediens="maja",
            konteksts="Plāns nav zīmējums izskatam - pēc tā pasūta grīdu, "
                      "līsti un krāsu.",
            kapec="Viens mērījums plānā pasaka gan garumu, gan cenu."),

    Kopsavilkums([
        "Izmēru telpu un pierakstu izmērus vienā mērvienībā.",
        "Izvēlos mērogu tā, lai plāns ietilptu lapā.",
        "Pārrēķinu visus izmērus un uzzīmēju plānu.",
        "Pierakstu mērogu zem plāna.",
    ]),

    Majas([
        "Uzzīmē savas istabas plānu mērogā 1 : 50.",
        "Ieliec plānā gultu un galdu - arī tos pārrēķini mērogā.",
        "Pārbaudi, vai starp mēbelēm paliek vismaz 60 cm platas ejas.",
    ]),
]
