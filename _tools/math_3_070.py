# -*- coding: utf-8 -*-
"""3. klase, 70. stunda: «Kā uzzīmēt telpas plānu?»

Praktiskā darba galvenā stunda: visi aprēķini ir gatavi, atliek zīmēt. Stunda
dod zīmēšanas kārtību - vispirms sienas, tad durvis un logi, tad objekti -,
jo tieši secība izšķir, vai plāns sanāks vai nesanāks.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         figura)

TEMA = "Kā uzzīmēt telpas plānu?"

MERKIS = ("Izveidosim telpas plānu, attēlojot logus, durvis un galvenos "
          "objektus.")

SATURS = [
    Sakums("No kā sākt - no sienām vai no galdiem?",
           zimejums=figura([(0, 0), (16, 0), (16, 12), (0, 12)],
                           [(8, -0.8, "16 cm"), (17, 6, "12 cm")],
                           "klases plāns"),
           paraksts="Vispirms uzzīmē taisnstūri - visu telpu.",
           fakti=["Plānu vienmēr sāk ar sienām.",
                  "Tikai tad, kad telpa ir uzzīmēta, tajā var likt objektus."]),

    Doma("Zīmē no lielā uz mazo",
         "Vispirms sienas, tad durvis un logi, tad lielie objekti, tad "
         "sīkumi.",
         soli=[
             "Uzzīmē taisnstūri ar plāna izmēriem.",
             "Atzīmē durvis ar pārtrauktu līniju sienā.",
             "Atzīmē logus ar dubultu līniju.",
             "Ieliec galdus, skapjus un citus objektus.",
             "Pieraksti samazinājumu un uzzīmē ziemeļu virzienu.",
         ],
         pieze="Objektu vietu mēra no sienas, nevis no acs: ja galds ir 50 cm "
               "no sienas, plānā tam jābūt 1 cm no līnijas."),

    Paraugs("Kur plānā likt galdu?",
            uzd="Galds ir 100 cm no sienas. Kur to zīmēt plānā, ja "
                "samazinājums ir 50 reizes?",
            soli=[
                ("100 : 50 = 2",
                 "Attālums plānā ir 2 cm."),
                ("Mēra no sienas līnijas",
                 "Lineālu liek pie sienas, ne pie lapas malas."),
                ("Galds sākas 2 cm no sienas",
                 "Tikai tad zīmē pašu galdu."),
            ],
            atbilde="2 cm no sienas"),

    Petijums("Uzzīmē savas klases plānu",
             vajag="plāna tabula, lineāls, zīmulis un lapa",
             soli=[
                 "Uzzīmē telpas taisnstūri ar plāna izmēriem.",
                 "Atzīmē durvis un logus.",
                 "Ieliec galdus un skapjus pēc izmērītajiem attālumiem.",
                 "Pieraksti samazinājumu un savu vārdu.",
             ],
             secinajums="Plāns ir gatavs, kad pēc tā var atrast katru "
                        "objektu, telpā neieejot."),

    Ievadi("Attālumi plānā", [
        {"jaut": "100 cm no sienas, samazinājums 50. Cik centimetru plānā?",
         "atb": ["2"], "padoms": "100 : 50."},
        {"jaut": "250 cm no sienas, samazinājums 50. Cik centimetru plānā?",
         "atb": ["5"], "padoms": "250 : 50."},
        {"jaut": "Plānā 3 cm no sienas, samazinājums 50. Cik centimetru "
                 "telpā?",
         "atb": ["150"], "padoms": "3 · 50."},
        {"jaut": "Durvis 90 cm platas, samazinājums 50. Cik milimetru plānā?",
         "atb": ["18"], "padoms": "1,8 cm ir 18 mm."},
        {"jaut": "Logs 150 cm plats, samazinājums 50. Cik centimetru plānā?",
         "atb": ["3"], "padoms": "150 : 50."},
        {"jaut": "Klase 800 cm gara, samazinājums 50. Cik centimetru plānā?",
         "atb": ["16"], "padoms": "800 : 50."},
    ], pamats=4),

    Zimejums("Kas plānā jāatzīmē",
             figura([(0, 0), (16, 0), (16, 12), (0, 12)],
                    [(3, 0.7, "durvis"), (13, 11.3, "logi"),
                     (8, 6, "galdi")],
                    "gatavs plāns"),
             paskaidro="Durvis, logi un galvenie objekti - bez tiem plāns ir "
                       "tikai taisnstūris.",
             ievads="Šie ir trīs obligātie elementi."),

    Varianti("Kāda ir pareizā secība?", [
        {"jaut": "Ar ko sāk plāna zīmēšanu?",
         "opcijas": ["Ar sienām", "Ar galdiem", "Ar durvīm", "Ar virsrakstu"],
         "pareizi": 0, "padoms": "Vispirms telpa, tad tās saturs."},
        {"jaut": "No kurienes mēra objekta vietu?",
         "opcijas": ["No sienas", "No lapas malas", "No telpas vidus",
                     "No durvīm"],
         "pareizi": 0, "padoms": "Sienas ir tas, kas nekustas."},
        {"jaut": "Kas obligāti jāpieraksta pie plāna?",
         "opcijas": ["Samazinājums", "Zīmētāja vecums", "Krāsu saraksts",
                     "Lapas izmērs"],
         "pareizi": 0, "padoms": "Bez tā izmērus atjaunot nevar."},
        {"jaut": "Objekts ir 200 cm no sienas, samazinājums 50. Cik "
                 "centimetru plānā?",
         "opcijas": ["4 cm", "40 cm", "2 cm", "250 cm"],
         "pareizi": 0, "padoms": "200 : 50."},
    ], pamats=4),

    Pasaule("Kā izkārtot klases telpu?",
            Ievadi("", [
                {"jaut": "Klase ir 800 cm gara. Galdu rinda aizņem 600 cm. "
                         "Cik centimetru paliek ejai?",
                 "atb": ["200"], "padoms": "800 − 600."},
                {"jaut": "Viens galds ir 120 cm. Cik galdu ietilpst 600 cm?",
                 "atb": ["5"], "padoms": "600 : 120."},
                {"jaut": "Cik galdu ietilpst, ja rindas ir divas?",
                 "atb": ["10"], "padoms": "2 · 5."},
                {"jaut": "Pie katra galda sēž 2 skolēni. Cik skolēnu "
                         "ietilpst?",
                 "atb": ["20"], "padoms": "10 · 2."},
            ]),
            pavediens="skola",
            konteksts="Pirms galdus pārbīda, izkārtojumu izmēģina uz plāna - "
                      "tas ir daudz vieglāk nekā telpā.",
            kapec="Plāns pasaka, vai izkārtojums vispār ir iespējams."),

    Kopsavilkums([
        "Uzzīmēju telpas plānu ar izvēlēto samazinājumu.",
        "Zīmēju no lielā uz mazo: sienas, durvis, objekti.",
        "Mēru objektu vietu no sienas, ne no lapas malas.",
        "Pierakstu pie plāna samazinājumu.",
    ]),

    Majas([
        "Uzzīmē savas istabas plānu ar samazinājumu 50 reizes.",
        "Atzīmē tajā durvis, logu un gultu.",
        "Pārbaudi, vai pēc plāna var atrast katru lietu.",
    ]),
]
