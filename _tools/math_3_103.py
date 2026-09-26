# -*- coding: utf-8 -*-
"""3. klase, 103. stunda: «Kāda daļa no decimetra ir centimetrs?»

Mērvienības ir daļu sistēma: centimetrs ir decimetra desmitdaļa, decimetrs -
metra desmitdaļa, milimetrs - centimetra desmitdaļa. Tas savieno 3.3. temata
pārrēķinus ar šī temata daļām.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         restis)

TEMA = "Kāda daļa no decimetra ir centimetrs?"

MERKIS = ("Ar lineālu noteiksim daļu no garuma mērvienības.")

SATURS = [
    Sakums("Kāpēc mērvienības iet pa desmit?",
           zimejums=restis([["1 mm", "=", "1/10 cm"],
                            ["1 cm", "=", "1/10 dm"],
                            ["1 dm", "=", "1/10 m"]],
                           "katra vienība ir nākamās desmitdaļa"),
           paraksts="Katra mazākā vienība ir nākamās desmitdaļa.",
           fakti=["1 dm = 10 cm, tāpēc 1 cm ir {1|10} dm.",
                  "1 m = 10 dm, tāpēc 1 dm ir {1|10} m."]),

    Doma("Mazākā vienība ir lielākās desmitdaļa",
         "Ja lielākā vienība sadalās 10 mazākās, tad mazākā ir tās "
         "desmitdaļa.",
         soli=[
             "Noskaidro, cik mazo vienību ir vienā lielajā.",
             "Tas skaitlis ir daļas saucējs.",
             "Viena mazā vienība ir {1|n} no lielās.",
             "Vairākas vienības ir {k|n}.",
         ],
         pieze="Metrs un centimetrs ir izņēmums: metrā ir 100 centimetru, "
               "tāpēc centimetrs ir metra *simtdaļa*, ne desmitdaļa."),

    Paraugs("Kāda daļa no metra ir 25 cm?",
            uzd="Nosaki, kāda daļa no metra ir 25 cm.",
            soli=[
                ("1 m = 100 cm",
                 "Vispirms abas vienības izsaka vienādi."),
                ("{25|100}",
                 "Divdesmit pieci centimetri no simta."),
                ("100 : 25 = 4, tātad {1|4}",
                 "25 cm ir ceturtdaļa metra."),
            ],
            atbilde="{1|4} metra"),

    Petijums("Atrodi daļas uz lineāla",
             vajag="lineāls un papīra sloksne",
             soli=[
                 "Nogriez sloksni, kas ir tieši 1 dm gara.",
                 "Saloc to uz pusēm un izmēri - cik centimetru?",
                 "Saloc vēlreiz un izmēri vēlreiz.",
                 "Pieraksti katru garumu gan centimetros, gan kā daļu no "
                 "decimetra.",
             ],
             secinajums="Puse decimetra ir 5 cm jeb {5|10} dm - abi pieraksti "
                        "nozīmē vienu un to pašu."),

    Ievadi("Daļa no mērvienības", [
        {"jaut": "Cik centimetru ir 1 dm?", "atb": ["10"],
         "padoms": "Desmit centimetru."},
        {"jaut": "Kāds ir saucējs daļai «1 cm no 1 dm»?", "atb": ["10"],
         "padoms": "Decimetrā ir 10 cm."},
        {"jaut": "Kāds ir saucējs daļai «1 cm no 1 m»?", "atb": ["100"],
         "padoms": "Metrā ir 100 cm."},
        {"jaut": "Cik centimetru ir {1|2} dm?", "atb": ["5"],
         "padoms": "10 : 2."},
        {"jaut": "Cik centimetru ir {1|4} m?", "atb": ["25"],
         "padoms": "100 : 4."},
        {"jaut": "Cik milimetru ir {1|2} cm?", "atb": ["5"],
         "padoms": "10 : 2."},
    ], pamats=4),

    Zimejums("Metrs un tā daļas",
             restis([["daļa", "1/10 m", "1/4 m", "1/2 m"],
                     ["cm", 10, 25, 50]],
                    "metrs ir 100 cm"),
             paskaidro="Katru daļu no metra var pateikt arī centimetros.",
             ievads="Trīs daļas no viena metra."),

    Varianti("Kāda daļa tā ir?", [
        {"jaut": "Kāda daļa no decimetra ir 1 cm?",
         "opcijas": ["{1|10}", "{1|100}", "{1|2}", "{10|1}"],
         "pareizi": 0, "padoms": "Decimetrā ir 10 cm."},
        {"jaut": "Kāda daļa no metra ir 50 cm?",
         "opcijas": ["{1|2}", "{1|4}", "{1|5}", "{1|50}"],
         "pareizi": 0, "padoms": "100 : 50 = 2."},
        {"jaut": "Kāda daļa no centimetra ir 1 mm?",
         "opcijas": ["{1|10}", "{1|100}", "{1|5}", "{1|2}"],
         "pareizi": 0, "padoms": "Centimetrā ir 10 mm."},
        {"jaut": "Cik centimetru ir {3|4} metra?",
         "opcijas": ["75", "25", "50", "34"],
         "pareizi": 0, "padoms": "3 · 25."},
    ], pamats=4),

    Pasaule("Cik auduma vajag?",
            Ievadi("", [
                {"jaut": "Auduma gabals ir 1 m. Cik centimetru ir {1|2}?",
                 "atb": ["50"], "padoms": "100 : 2."},
                {"jaut": "Cik centimetru ir {1|4} metra?", "atb": ["25"],
                 "padoms": "100 : 4."},
                {"jaut": "Cik centimetru ir {3|4} metra?", "atb": ["75"],
                 "padoms": "3 · 25."},
                {"jaut": "Nopirka 2 m un 25 cm. Cik centimetru kopā?",
                 "atb": ["225"], "padoms": "200 + 25."},
            ]),
            pavediens="veikals",
            konteksts="Audumu veikalā pārdod metros, bet griež pa "
                      "ceturtdaļām - tāpēc daļas te ir katru dienu.",
            kapec="Bez daļām audumu varētu pirkt tikai veselos metros."),

    Kopsavilkums([
        "Nosaku, kāda daļa no lielākās mērvienības ir mazākā.",
        "Zinu, ka 1 cm ir {1|10} dm un {1|100} m.",
        "Izsaku daļu no metra centimetros.",
        "Pārbaudu daļas ar lineālu.",
    ]),

    Majas([
        "Izmēri kādu priekšmetu un pasaki tā garumu kā daļu no metra.",
        "Nogriez sloksni, kas ir {1|4} metra gara.",
        "Atrodi mājās kaut ko, kas ir tieši puse metra.",
    ]),
]
