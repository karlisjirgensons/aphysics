# -*- coding: utf-8 -*-
"""3. klase, 69. stunda: «Cik liels objekts ir plānā?»

Kad samazinājums izvēlēts, pārējais ir rēķins - katram objektam pa vienam.
Kalkulators te ir atļauts un vajadzīgs: rēķinu ir daudz, un stundas mērķis ir
plāns, nevis dalīšanas treniņš.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         restis)

TEMA = "Cik liels objekts ir plānā?"

MERKIS = ("Aprēķināsim objektu izmērus plānā, izmantojot kalkulatoru.")

SATURS = [
    Sakums("Cik liels plānā ir skolas galds?",
           zimejums=restis([["objekts", "telpā", "plānā : 50"],
                            ["galds", "120 cm", "?"],
                            ["skapis", "200 cm", "?"],
                            ["durvis", "90 cm", "?"]],
                           "aizpildi trešo aili"),
           paraksts="Katram objektam tas pats samazinājums.",
           fakti=["Plānā visiem objektiem viens samazinājums.",
                  "Ja kāds objekts plānā ir mazāks par 1 mm, to neatzīmē."]),

    Doma("Katru izmēru izdali ar samazinājumu",
         "Plāna izmērs = īstais izmērs : samazinājums - un tā katram "
         "objektam.",
         soli=[
             "Pieraksti objekta īstos izmērus centimetros.",
             "Izdali tos ar izvēlēto samazinājumu.",
             "Noapaļo rezultātu līdz veselam milimetram.",
             "Ieraksti rezultātu tabulā.",
         ],
         pieze="Ja objekts plānā sanāk mazāks par 2 mm, to labāk apzīmēt ar "
               "zīmi, nevis zīmēt mērogā - citādi to neviens neredzēs."),

    Paraugs("Cik liels plānā ir galds?",
            uzd="Galds ir 120 cm garš. Cik garš tas ir plānā, ja "
                "samazinājums ir 50 reizes?",
            soli=[
                ("120 : 50",
                 "Īsto izmēru dala ar samazinājumu."),
                ("120 : 50 = 2,4",
                 "Ar kalkulatoru: divi komats četri centimetri."),
                ("2,4 cm ≈ 24 mm",
                 "Plānā galdu zīmē 24 mm garu."),
            ],
            atbilde="2,4 cm jeb 24 mm"),

    Petijums("Aizpildi plāna tabulu",
             vajag="kalkulators, mērījumu tabula un lapa",
             soli=[
                 "Pieraksti visus klases objektus un to izmērus.",
                 "Izdali katru izmēru ar izvēlēto samazinājumu.",
                 "Ieraksti rezultātus jaunā ailē.",
                 "Atzīmē objektus, kas plānā sanāk mazāki par 2 mm.",
             ],
             secinajums="Tabula ar plāna izmēriem ir viss, kas vajadzīgs "
                        "zīmēšanai - tālāk vairs nav jārēķina."),

    Ievadi("Izrēķini plāna izmērus", [
        {"jaut": "200 cm : 50. Cik centimetru plānā?", "atb": ["4"],
         "padoms": "200 : 50."},
        {"jaut": "90 cm : 50. Cik centimetru plānā?",
         "atb": ["1,8", "1.8"], "padoms": "Ar kalkulatoru."},
        {"jaut": "800 cm : 50. Cik centimetru plānā?", "atb": ["16"],
         "padoms": "800 : 50."},
        {"jaut": "150 cm : 50. Cik centimetru plānā?", "atb": ["3"],
         "padoms": "150 : 50."},
        {"jaut": "Plānā 4 cm, samazinājums 50. Cik centimetru telpā?",
         "atb": ["200"], "padoms": "4 · 50."},
        {"jaut": "Plānā 6 cm, samazinājums 50. Cik centimetru telpā?",
         "atb": ["300"], "padoms": "6 · 50."},
    ], pamats=4,
        ievads="Kalkulators ir atļauts - svarīgs ir rezultāts, ne rēķins."),

    Zimejums("Aizpildīta tabula",
             restis([["objekts", "telpā", "plānā"],
                     ["galds", "120 cm", "2,4 cm"],
                     ["skapis", "200 cm", "4 cm"],
                     ["durvis", "90 cm", "1,8 cm"]],
                    "samazinājums 50 reizes"),
             paskaidro="Visi trīs rēķini ir viens un tas pats: dalīšana ar 50.",
             ievads="Tā izskatās gatava plāna tabula."),

    Varianti("Vai rēķins ir pareizs?", [
        {"jaut": "Objekts ir 300 cm, samazinājums 50. Cik plānā?",
         "opcijas": ["6 cm", "60 cm", "3 cm", "250 cm"],
         "pareizi": 0, "padoms": "300 : 50."},
        {"jaut": "Plānā objekts ir 5 cm, samazinājums 50. Cik telpā?",
         "opcijas": ["250 cm", "55 cm", "10 cm", "500 cm"],
         "pareizi": 0, "padoms": "5 · 50."},
        {"jaut": "Ko darīt, ja objekts plānā sanāk 1 mm?",
         "opcijas": ["Apzīmēt to ar zīmi", "Zīmēt tik un tā",
                     "Neatzīmēt vispār", "Mainīt samazinājumu tikai tam"],
         "pareizi": 0, "padoms": "Samazinājums visiem jābūt vienam."},
        {"jaut": "Kurš rēķins dod plāna izmēru?",
         "opcijas": ["īstais : samazinājums", "īstais · samazinājums",
                     "samazinājums : īstais", "īstais + samazinājums"],
         "pareizi": 0, "padoms": "Plānā izmērs ir mazāks."},
    ], pamats=4),

    Pasaule("Cik liela skolas zāle ir plānā?",
            Ievadi("", [
                {"jaut": "Zāle 2400 cm gara, samazinājums 100. Cik "
                         "centimetru plānā?",
                 "atb": ["24"], "padoms": "2400 : 100."},
                {"jaut": "Zāle 1200 cm plata. Cik centimetru plānā?",
                 "atb": ["12"], "padoms": "1200 : 100."},
                {"jaut": "Basketbola grozs ir 300 cm no sienas. Cik "
                         "centimetru plānā?",
                 "atb": ["3"], "padoms": "300 : 100."},
                {"jaut": "Cik centimetru ir plāna perimetrs?",
                 "atb": ["72"], "padoms": "2 · (24 + 12)."},
            ]),
            pavediens="skola",
            konteksts="Skolas plānā sporta zāle aizņem visvairāk vietas - "
                      "tāpēc tieši pēc tās izvēlējās samazinājumu.",
            kapec="Viens rēķins, atkārtots katram objektam, un plāns ir "
                  "gatavs zīmēšanai."),

    Kopsavilkums([
        "Aprēķinu objekta izmēru plānā, dalot ar samazinājumu.",
        "Atrodu īsto izmēru, reizinot plāna izmēru ar samazinājumu.",
        "Lietoju kalkulatoru, kad rēķinu ir daudz.",
        "Zinu, ko darīt ar objektu, kas plānā sanāk pārāk mazs.",
    ]),

    Majas([
        "Izrēķini, cik liela plānā būs tava gulta, ja samazina 50 reizes.",
        "Izrēķini to pašu savam galdam un skapim.",
        "Pieraksti visus rezultātus tabulā.",
    ]),
]
