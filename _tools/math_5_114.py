# -*- coding: utf-8 -*-
"""5. klase, 114. stunda: «Kas nosaka riņķa līniju?»

Jauns mikrotemats. Riņķa līnija ir vienīgā figūra, ko nosaka viens vienīgs
skaitlis - rādiuss -, un tieši tas padara to par ērtu darbarīku. Stunda
sākas ar cirkuli rokās: kāju attālums ir rādiuss, un zīmējums sanāk pats.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         rinkis)

TEMA = "Kas nosaka riņķa līniju?"

MERKIS = ("Iemācīsimies skaidrot, ka riņķa līniju nosaka rādiuss, un zīmēt "
          "riņķa līniju ar dotu rādiusu vai diametru.")

SATURS = [
    Sakums("Viens skaitlis - viena riņķa līnija",
           zimejums=rinkis(radiuss="r", virsraksts="Centrs un rādiuss"),
           paraksts="Ja zināms centrs un rādiuss, riņķa līnija ir tikai "
                    "viena.",
           fakti=["Rādiuss ir attālums no centra līdz līnijai.",
                  "Visi riņķa līnijas punkti ir vienādi tālu no centra.",
                  "Diametrs ir divi rādiusi: d = 2 · r."]),

    Doma("Rādiuss nosaka visu",
         "Riņķa līnija ir visu to punktu kopa, kas atrodas vienādā attālumā "
         "no centra; šo attālumu sauc par rādiusu.",
         soli=[
             "Atzīmē centru un apzīmē to ar burtu O.",
             "Izvēlies rādiusu - cirkuļa kāju attālumu.",
             "Apvelc riņķa līniju, neizmainot cirkuļa atvērumu.",
             "Diametru iegūsti, rādiusu reizinot ar 2.",
             "Rādiusu iegūsti, diametru dalot ar 2.",
         ],
         pieze="Riņķa līnija ir pati līnija, bet riņķis ir viss laukums, ko "
               "tā ietver. Tāpēc riņķa līnijai mēra garumu, bet riņķim - "
               "laukumu."),

    Paraugs("Uzzīmē riņķa līniju ar diametru 6 cm",
            uzd="Kāds cirkuļa atvērums vajadzīgs?",
            soli=[
                ("Diametrs ir 6 cm",
                 "Dots lielums."),
                ("r = d : 2",
                 "Rādiuss ir puse no diametra."),
                ("6 : 2 = 3 (cm)",
                 "Cirkuļa atvērums."),
                ("Atzīmē centru un apvelc līniju",
                 "Atvērums 3 cm."),
            ],
            atbilde="Cirkuļa atvērums ir 3 cm"),

    Petijums("Zīmē ar cirkuli",
             soli=["Atzīmē lapā punktu O - tas būs centrs.",
                   "Iestati cirkuļa atvērumu 4 cm un apvelc riņķa līniju.",
                   "Novelc rādiusu un izmēri to ar lineālu.",
                   "Novelc diametru caur centru un izmēri arī to.",
                   "Salīdzini: vai diametrs ir tieši divi rādiusi?"],
             vajag="cirkulis, lineāls, zīmulis",
             secinajums="Diametrs vienmēr ir divas reizes garāks par "
                        "rādiusu."),

    Ievadi("Rādiuss un diametrs", [
        {"jaut": "Rādiuss ir 3 cm. Cik centimetru ir diametrs?",
         "atb": ["6"], "padoms": "d = 2 · r."},
        {"jaut": "Diametrs ir 10 cm. Cik centimetru ir rādiuss?",
         "atb": ["5"], "padoms": "r = d : 2."},
        {"jaut": "Rādiuss ir 7 cm. Cik centimetru ir diametrs?",
         "atb": ["14"], "padoms": "2 · 7."},
        {"jaut": "Diametrs ir 9 cm. Cik centimetru ir rādiuss? Atbildi "
                 "raksti kā a b/c.",
         "atb": ["4 1/2"], "padoms": "9 : 2."},
        {"jaut": "Cirkuļa atvērums ir 5 cm. Cik centimetru ir diametrs?",
         "atb": ["10"], "padoms": "Atvērums ir rādiuss."},
        {"jaut": "Diametrs ir 24 cm. Cik centimetru ir rādiuss?",
         "atb": ["12"], "padoms": "24 : 2."},
        {"jaut": "Cik rādiusu ir vienā diametrā?",
         "atb": ["2"], "padoms": "Diametrs iet caur centru."},
        {"jaut": "Rādiuss ir 1{1|2} cm. Cik centimetru ir diametrs?",
         "atb": ["3"], "padoms": "1{1|2} · 2."},
    ], pamats=4,
        ievads="Diametrs ir divi rādiusi - abos virzienos no rēķina."),

    Zimejums("Rādiuss un diametrs vienā zīmējumā",
             rinkis(radiuss="r = 3 cm", diametrs="d = 6 cm",
                    virsraksts="Viena riņķa līnija, divi mērījumi"),
             paskaidro="Rādiuss iet no centra līdz līnijai, diametrs - cauri "
                       "centram no malas līdz malai.",
             ievads="Abi nogriežņi ir saistīti: d = 2 · r."),

    Varianti("Kas ir kas?", [
        {"jaut": "Kas ir rādiuss?",
         "opcijas": ["Attālums no centra līdz līnijai",
                     "Attālums no malas līdz malai",
                     "Riņķa laukums",
                     "Līnijas garums"],
         "pareizi": 0,
         "padoms": "No centra."},
        {"jaut": "Kas ir diametrs?",
         "opcijas": ["Nogrieznis caur centru no malas līdz malai",
                     "Attālums no centra līdz līnijai",
                     "Riņķa laukums",
                     "Cirkuļa atvērums"],
         "pareizi": 0,
         "padoms": "Divi rādiusi."},
        {"jaut": "Rādiuss ir 4 cm. Kāds ir diametrs?",
         "opcijas": ["8 cm", "2 cm", "4 cm", "16 cm"],
         "pareizi": 0,
         "padoms": "2 · 4."},
        {"jaut": "Ar ko riņķa līnija atšķiras no riņķa?",
         "opcijas": ["Līnija ir mala, riņķis ir viss laukums",
                     "Tās ir viens un tas pats",
                     "Riņķim nav centra",
                     "Līnijai nav rādiusa"],
         "pareizi": 0,
         "padoms": "Vienam mēra garumu, otram laukumu."},
        {"jaut": "Cik riņķa līniju var uzzīmēt ar vienu centru un vienu "
                 "rādiusu?",
         "opcijas": ["Tikai vienu", "Divas", "Bezgalīgi daudz", "Nevienu"],
         "pareizi": 0,
         "padoms": "Abi skaitļi nosaka visu."},
        {"jaut": "Visi riņķa līnijas punkti ir...",
         "opcijas": ["Vienādā attālumā no centra", "Dažādā attālumā",
                     "Uz viena rādiusa", "Uz diametra"],
         "pareizi": 0,
         "padoms": "Tā ir definīcija."},
    ], pamats=4),

    Pasaule("Cik liels ir galda paklājs?",
            Ievadi("", [
                {"jaut": "Apaļa paklāja diametrs ir 2 m. Cik metru ir "
                         "rādiuss?",
                 "atb": ["1"], "padoms": "2 : 2."},
                {"jaut": "Apaļa galda rādiuss ir 60 cm. Cik centimetru ir "
                         "diametrs?",
                 "atb": ["120"], "padoms": "2 · 60."},
                {"jaut": "Caurules diametrs ir 16 cm. Cik centimetru ir "
                         "rādiuss?",
                 "atb": ["8"], "padoms": "16 : 2."},
                {"jaut": "Lampas abažūra rādiuss ir 25 cm. Cik centimetru ir "
                         "diametrs?",
                 "atb": ["50"], "padoms": "2 · 25."},
            ]),
            pavediens="maja",
            konteksts="Mājā apaļas lietas mēra pa diametru, bet zīmē pēc "
                      "rādiusa.",
            kapec="Pāriet no viena uz otru var ar vienu reizināšanu."),

    Kopsavilkums([
        "Skaidroju, ka riņķa līniju nosaka centrs un rādiuss.",
        "Zīmēju riņķa līniju ar dotu rādiusu.",
        "Zīmēju riņķa līniju ar dotu diametru.",
        "Pārrēķinu rādiusu diametrā un otrādi.",
    ]),

    Majas([
        "Uzzīmē riņķa līnijas ar rādiusiem 2 cm, 3 cm un 5 cm.",
        "Izmēri kādas apaļas lietas diametru mājās.",
        "Aprēķini tās rādiusu.",
    ]),
]
