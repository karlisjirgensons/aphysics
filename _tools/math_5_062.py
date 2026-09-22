# -*- coding: utf-8 -*-
"""5. klase, 62. stunda: «Kura daļa ir tuvāk vieniniekam?»

Trešais salīdzināšanas paņēmiens, un tas ir visātrākais: skatās nevis uz
pašu daļu, bet uz to, cik tai trūkst līdz vieniniekam. Skolēnam tas ir
negaidīti - jautā par lielāko, bet salīdzina mazāko. Tāpēc modelis te rāda
tieši tukšo gabalu, ne iekrāsoto.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, dala, taisne)

TEMA = "Kura daļa ir tuvāk vieniniekam?"

MERKIS = ("Mācīsimies noteikt, kura no divām daļām atrodas tuvāk skaitlim 1, "
          "un pamatot atbildi.")

SATURS = [
    Sakums("Cik trūkst līdz galam?",
           zimejums=dala(8, 7, "7/8"),
           paraksts="Iekrāsotas septiņas astotdaļas; tukša palikusi viena.",
           fakti=["Līdz vieniniekam trūkst tikai viens gabals.",
                  "Jo mazāks tukšais gabals, jo tuvāk vieniniekam.",
                  "Tāpēc skaties uz tukšo, ne uz iekrāsoto."]),

    Doma("Salīdzini to, kas trūkst",
         "Daļa ir tuvāk vieniniekam tad, ja tai līdz vieniniekam trūkst "
         "mazāka daļa.",
         soli=[
             "Atrodi, cik katrai daļai trūkst līdz vieniniekam.",
             "Trūkstošās daļas skaitītājs ir saucēja un skaitītāja starpība.",
             "Salīdzini abas trūkstošās daļas.",
             "Tuvāk vieniniekam ir tā, kurai trūkst mazāk.",
         ],
         pieze="Daļai {7|8} trūkst {1|8}, bet daļai {9|10} trūkst {1|10}. "
               "Desmitdaļa ir mazāka par astotdaļu, tāpēc {9|10} ir tuvāk "
               "vieniniekam."),

    Paraugs("{7|8} vai {9|10}?",
            uzd="Kura no daļām {7|8} un {9|10} atrodas tuvāk skaitlim 1?",
            soli=[
                ("{7|8} trūkst {1|8}",
                 "8 - 7 = 1 astotdaļa."),
                ("{9|10} trūkst {1|10}",
                 "10 - 9 = 1 desmitdaļa."),
                ("{1|10} < {1|8}",
                 "Desmitdaļa ir sīkāks gabals."),
                ("{9|10} ir tuvāk vieniniekam",
                 "Tai trūkst mazāk."),
            ],
            atbilde="Tuvāk vieniniekam ir {9|10}"),

    Ievadi("Cik trūkst līdz vieniniekam?", [
        {"jaut": "Cik trūkst daļai {3|4} līdz vieniniekam? Atbildi raksti kā "
                 "a/b.",
         "atb": ["1/4"], "padoms": "4 - 3 = 1."},
        {"jaut": "Cik trūkst daļai {5|6} līdz vieniniekam? Atbildi raksti kā "
                 "a/b.",
         "atb": ["1/6"], "padoms": "6 - 5 = 1."},
        {"jaut": "Cik trūkst daļai {7|10} līdz vieniniekam? Atbildi raksti "
                 "kā a/b.",
         "atb": ["3/10"], "padoms": "10 - 7 = 3."},
        {"jaut": "Cik trūkst daļai {11|12} līdz vieniniekam? Atbildi raksti "
                 "kā a/b.",
         "atb": ["1/12"], "padoms": "12 - 11 = 1."},
        {"jaut": "{4|5} vai {5|6} - kura ir tuvāk vieniniekam? Ieraksti kā "
                 "a/b.",
         "atb": ["5/6"], "padoms": "Trūkst {1|5} pret {1|6}."},
        {"jaut": "{2|3} vai {7|8} - kura ir tuvāk vieniniekam? Ieraksti kā "
                 "a/b.",
         "atb": ["7/8"], "padoms": "Trūkst {1|3} pret {1|8}."},
        {"jaut": "{9|10} vai {19|20} - kura ir tuvāk vieniniekam? Ieraksti "
                 "kā a/b.",
         "atb": ["19/20"], "padoms": "Trūkst {1|10} pret {1|20}."},
        {"jaut": "{5|8} vai {3|4} - kura ir tuvāk vieniniekam? Ieraksti kā "
                 "a/b.",
         "atb": ["3/4"], "padoms": "Trūkst {3|8} pret {1|4} jeb {2|8}."},
    ], pamats=4,
        ievads="Vispirms izrēķini, cik trūkst; tikai tad salīdzini."),

    Zimejums("Abas daļas gandrīz pie vieninieka",
             taisne(0, 1, 1, [(7 / 8.0, "7/8"), (9 / 10.0, "9/10")],
                    virsraksts="Kura ir tuvāk labajam galam"),
             paskaidro="Abas ir pie paša vieninieka, bet {9|10} - vēl "
                       "tuvāk. Attālums līdz 1 ir tieši trūkstošā daļa.",
             ievads="Attālums līdz vieniniekam ir redzams uz taisnes."),

    Varianti("Kā spriež par tuvumu?", [
        {"jaut": "Kā noteikt, kura daļa ir tuvāk vieniniekam?",
         "opcijas": ["Salīdzināt, cik katrai trūkst",
                     "Salīdzināt saucējus",
                     "Salīdzināt skaitītājus",
                     "Saskaitīt abas daļas"],
         "pareizi": 0,
         "padoms": "Tuvums ir attālums līdz 1."},
        {"jaut": "Cik trūkst daļai {19|20} līdz vieniniekam?",
         "opcijas": ["{1|20}", "{19|20}", "{1|19}", "{20|19}"],
         "pareizi": 0,
         "padoms": "20 - 19 = 1."},
        {"jaut": "Kura daļa ir vistuvāk vieniniekam?",
         "opcijas": ["{99|100}", "{9|10}", "{4|5}", "{49|50}"],
         "pareizi": 0,
         "padoms": "Trūkst {1|100}."},
        {"jaut": "Daļām trūkst {1|7} un {1|9}. Kura daļa ir tuvāk "
                 "vieniniekam?",
         "opcijas": ["Tā, kurai trūkst {1|9}", "Tā, kurai trūkst {1|7}",
                     "Abas vienādi", "To nevar zināt"],
         "pareizi": 0,
         "padoms": "Devītdaļa ir sīkāka par septītdaļu."},
        {"jaut": "Kāda daļa ir tieši vienāda ar 1?",
         "opcijas": ["{6|6}", "{1|6}", "{6|1}", "{5|6}"],
         "pareizi": 0,
         "padoms": "Visi gabali kopā."},
        {"jaut": "Kāpēc šis paņēmiens ir ērts?",
         "opcijas": ["Trūkstošās daļas skaitītājs bieži ir 1",
                     "Nav jāzina saucējs",
                     "Nav jārēķina starpība",
                     "Tas nav ērts"],
         "pareizi": 0,
         "padoms": "Vienu ar vienu salīdzināt ir viegli."},
    ], pamats=4),

    Pasaule("Kurš skrējējs ir tuvāk finišam?",
            Ievadi("", [
                {"jaut": "Skrējējs noskrējis {7|8} distances. Cik tam trūkst "
                         "līdz finišam? Atbildi raksti kā a/b.",
                 "atb": ["1/8"], "padoms": "8 - 7 = 1."},
                {"jaut": "Otrs skrējējs noskrējis {9|10} distances. Cik tam "
                         "trūkst? Atbildi raksti kā a/b.",
                 "atb": ["1/10"], "padoms": "10 - 9 = 1."},
                {"jaut": "Kurš ir tuvāk finišam? Ieraksti viņa daļu kā a/b.",
                 "atb": ["9/10"], "padoms": "Mazāk trūkst - tuvāk finišam."},
                {"jaut": "Trešais noskrējis {11|12}. Cik tam trūkst? Atbildi "
                         "raksti kā a/b.",
                 "atb": ["1/12"], "padoms": "12 - 11 = 1."},
            ]),
            pavediens="sports",
            konteksts="Distances beigās neviens neskaita noskrieto - skaita "
                      "to, kas palicis.",
            kapec="Atlikums pasaka par tuvumu finišam vairāk nekā pati daļa."),

    Kopsavilkums([
        "Aprēķinu, cik daļai trūkst līdz vieniniekam.",
        "Salīdzinu divas daļas pēc tā, cik katrai trūkst.",
        "Nosaku, kura daļa atrodas tuvāk skaitlim 1.",
        "Pamatoju atbildi ar trūkstošo daļu, nevis ar izskatu.",
    ]),

    Majas([
        "Uzraksti trīs daļas, kurām līdz vieniniekam trūkst mazāk par "
        "{1|10}.",
        "Salīdzini {13|14} un {15|16} un pieraksti, kā sprieda.",
        "Padomā, kā tāpat noteikt, kura daļa ir tuvāk nullei.",
    ]),
]
