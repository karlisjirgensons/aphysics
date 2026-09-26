# -*- coding: utf-8 -*-
"""3. klase, 121. stunda: «Cik kubu ietilpst kastē?»

Tilpums - trešais lielums pēc garuma un laukuma. Modelis ir tas pats, kas
laukumam, tikai ar vienu dimensiju vairāk: kubiņi rindās, rindas slāņos,
slāņi kastē.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Slidnis, Varianti,
                         Zimejums, kermenis)

TEMA = "Cik kubu ietilpst kastē?"

MERKIS = ("No vienādiem kubiem veidosim taisnstūru skaldni un noteiksim tā "
          "tilpumu kubos.")

SATURS = [
    Sakums("Cik kastu ar ledu ietilpst konteinerā?",
           zimejums=kermenis("kvadrs", virsraksts="taisnstūru skaldnis"),
           paraksts="Tilpums ir tas, cik vienādu kubu ietilpst ķermenī.",
           fakti=["Tilpumu mēra ar vienādiem kubiem.",
                  "Kubus liek rindās, rindas - slāņos."]),

    Doma("Tilpums ir kubu skaits",
         "Saskaiti kubus vienā slānī un reizini ar slāņu skaitu.",
         soli=[
             "Saskaiti kubus vienā rindā.",
             "Reizini ar rindu skaitu slānī.",
             "Reizini ar slāņu skaitu.",
             "Pieraksti tilpumu kopā ar vienību - «kubi».",
         ],
         pieze="Tas ir tas pats, kas laukumam, tikai ar vienu reizināšanu "
               "vairāk: garums reiz platums reiz augstums."),

    Slidnis("Kā aug tilpums",
            soli=[
                {"v": "1 rinda = 4 kubi", "teksts": "Viena rinda.",
                 "josla": 17},
                {"v": "1 slānis = 12 kubi",
                 "teksts": "Trīs rindas pa 4.", "josla": 50},
                {"v": "2 slāņi = 24 kubi",
                 "teksts": "Divi slāņi.", "josla": 100},
            ],
            ievads="Kaste 4 x 3 x 2 kubi."),

    Paraugs("Cik kubu ietilpst kastē?",
            uzd="Kaste ir 4 kubus gara, 3 plata un 2 augsta. Cik kubu tajā "
                "ietilpst?",
            soli=[
                ("4 · 3 = 12",
                 "Kubu skaits vienā slānī."),
                ("12 · 2 = 24",
                 "Divi slāņi."),
                ("24 kubi",
                 "Tāds ir kastes tilpums."),
            ],
            atbilde="24 kubi"),

    Ievadi("Aprēķini tilpumu", [
        {"jaut": "Kaste 4 x 3 x 2 kubi. Cik kubu tajā ietilpst?",
         "atb": ["24"], "padoms": "12 · 2."},
        {"jaut": "Kaste 5 x 2 x 3 kubi. Cik kubu?", "atb": ["30"],
         "padoms": "10 · 3."},
        {"jaut": "Kubs ar malu 3 kubiņi. Cik kubiņu tajā ir?",
         "atb": ["27"], "padoms": "9 · 3."},
        {"jaut": "Kaste 6 x 2 x 2 kubi. Cik kubu?", "atb": ["24"],
         "padoms": "12 · 2."},
        {"jaut": "Kastē 36 kubi, slānī 12. Cik slāņu ir?", "atb": ["3"],
         "padoms": "36 : 12."},
        {"jaut": "Kubs ar malu 4 kubiņi. Cik kubiņu tajā ir?",
         "atb": ["64"], "padoms": "16 · 4."},
    ], pamats=4),

    Petijums("Uzbūvē kasti no kubiem",
             vajag="vienādi kubiņi vai cukurgraudi",
             soli=[
                 "Saliec vienu rindu no 4 kubiem.",
                 "Pieliec vēl divas tādas rindas - sanāk slānis.",
                 "Uzliec vēl vienu slāni virsū.",
                 "Saskaiti visus kubus un pārbaudi ar reizināšanu.",
             ],
             secinajums="Skaitīšana un reizināšana dod vienu un to pašu "
                        "skaitli - 24 kubus."),

    Zimejums("Kubs",
             kermenis("kubs", virsraksts="kubs"),
             paskaidro="Kubam visas trīs malas ir vienādas, tāpēc tilpums ir "
                       "malas reizinājums ar sevi trīs reizes.",
             ievads="Īpašais gadījums."),

    Varianti("Cik kubu ietilpst?", [
        {"jaut": "Kaste 3 x 3 x 3. Cik kubu?",
         "opcijas": ["27", "9", "18", "12"],
         "pareizi": 0, "padoms": "9 · 3."},
        {"jaut": "Kurš rēķins dod tilpumu?",
         "opcijas": ["garums · platums · augstums",
                     "garums · platums", "garums + platums + augstums",
                     "2 · (garums + platums)"],
         "pareizi": 0, "padoms": "Trīs reizinātāji."},
        {"jaut": "Kastē 48 kubi, slānī 16. Cik slāņu?",
         "opcijas": ["3", "4", "2", "6"],
         "pareizi": 0, "padoms": "48 : 16."},
        {"jaut": "Kaste 5 x 4 x 2. Cik kubu?",
         "opcijas": ["40", "20", "11", "80"],
         "pareizi": 0, "padoms": "20 · 2."},
    ], pamats=4),

    Pasaule("Cik ledus kubu ir ledājā?",
            Ievadi("", [
                {"jaut": "Ledus bloks 4 x 3 x 2 kubi. Cik kubu tajā ir?",
                 "atb": ["24"], "padoms": "12 · 2."},
                {"jaut": "Cik kubu ir 5 tādos blokos?", "atb": ["120"],
                 "padoms": "5 · 24."},
                {"jaut": "Viens kubs sver 2 kg. Cik kilogramu sver viens "
                         "bloks?",
                 "atb": ["48"], "padoms": "24 · 2."},
                {"jaut": "Cik kilogramu sver 5 bloki?", "atb": ["240"],
                 "padoms": "5 · 48."},
            ]),
            pavediens="planeta",
            konteksts="Ledāju biezumu un tilpumu mēra tieši tāpat - tikai "
                      "kubi tur ir kilometru lieli.",
            kapec="No tilpuma zina, cik ūdens ledājā ir sasalis."),

    Kopsavilkums([
        "Zinu, ka tilpums ir vienādu kubu skaits ķermenī.",
        "Aprēķinu tilpumu, reizinot garumu, platumu un augstumu.",
        "Saskaitu kubus pa slāņiem.",
        "Atrodu slāņu skaitu, ja zināms tilpums.",
    ]),

    Majas([
        "Saliec no kubiņiem kasti 3 x 2 x 2 un saskaiti kubus.",
        "Atrodi mājās kastīti un novērtē, cik kubiņu tajā ietilptu.",
        "Izrēķini kuba ar malu 5 tilpumu.",
    ]),
]
