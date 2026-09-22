# -*- coding: utf-8 -*-
"""6. klase, 76. stunda: «Kā izveidot izdevīgāko iepakojumu?»

Pēdējais mikrotemats sākas ar optimizācijas uzdevumu. Tilpums ir dots,
materiāla patēriņš - jāsamazina, un atbilde nav acīmredzama: izrādās, ka
visizdevīgākā forma ir tā, kas vistuvāk kubam.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         restis)

TEMA = "Kā izveidot izdevīgāko iepakojumu?"

MERKIS = ("Veidosim kastīti ar iespējami lielāku tilpumu un mazāku "
          "materiāla patēriņu.")

SATURS = [
    Sakums("Viens tilpums, dažādi kartona daudzumi",
           zimejums=restis([["24 x 1 x 1", "6 x 2 x 2", "4 x 3 x 2"],
                            ["98 cm²", "56 cm²", "52 cm²"]]),
           paraksts="Visām trim kastēm tilpums ir 24 cm³, bet kartona "
                    "patēriņš atšķiras gandrīz divas reizes.",
           fakti=["Jo tuvāk kubam, jo mazāka virsma pie vienāda tilpuma.",
                  "Garas šauras kastes prasa visvairāk materiāla.",
                  "Tieši tāpēc ražotāji izvēlas kompaktas formas."]),

    Doma("Meklē formu, kas tuvāka kubam",
         "Pie vienāda tilpuma vismazākā virsma ir tam ķermenim, kura trīs "
         "izmēri ir vistuvāk viens otram.",
         soli=[
             "Pieraksti doto tilpumu.",
             "Atrodi visus veidus, kā to sadalīt trīs veselos reizinātājos.",
             "Katram variantam aprēķini virsmas laukumu.",
             "Salīdzini un izvēlies to, kuram virsma ir vismazākā.",
             "Pārbaudi: vai izvēlētie izmēri ir vistuvāk viens otram?",
         ],
         pieze="Dabā tas pats: ūdens piliens ir lodīte, jo lode ir forma ar "
               "vismazāko virsmu pie dota tilpuma. Kastēm lodi nevar "
               "izmantot, tāpēc tuvākā ir kubs."),

    Paraugs("Izvēlies izdevīgāko kasti",
            uzd="Tilpums ir 24 cm³. Kura kaste prasa vismazāk kartona?",
            soli=[
                ("24 = 24 · 1 · 1 → virsma 2 · (24 + 24 + 1) = 98 cm²",
                 "Gara un šaura."),
                ("24 = 6 · 2 · 2 → virsma 2 · (12 + 12 + 4) = 56 cm²",
                 "Jau kompaktāka."),
                ("24 = 4 · 3 · 2 → virsma 2 · (12 + 8 + 6) = 52 cm²",
                 "Izmēri vistuvāk viens otram."),
                ("Vismazākā virsma ir 52 cm²",
                 "Kaste 4 x 3 x 2 ir izdevīgākā."),
            ],
            atbilde="kaste 4 x 3 x 2 cm"),

    Ievadi("Salīdzini iepakojumus", [
        {"jaut": "Kaste 24 x 1 x 1 cm. Cik cm³ ir tilpums?",
         "atb": ["24"], "padoms": "24 · 1 · 1."},
        {"jaut": "Kaste 4 x 3 x 2 cm. Cik cm³ ir tilpums?",
         "atb": ["24"], "padoms": "Tas pats tilpums."},
        {"jaut": "Kaste 4 x 3 x 2 cm. Cik cm² ir virsma?",
         "atb": ["52"], "padoms": "2 · (12 + 8 + 6)."},
        {"jaut": "Kaste 6 x 2 x 2 cm. Cik cm² ir virsma?",
         "atb": ["56"], "padoms": "2 · (12 + 12 + 4)."},
        {"jaut": "Kubs ar šķautni 3 cm. Cik cm³ ir tilpums?",
         "atb": ["27"], "padoms": "27."},
        {"jaut": "Kubs ar šķautni 3 cm. Cik cm² ir virsma?",
         "atb": ["54"], "padoms": "6 · 9."},
    ], pamats=4),

    Petijums("Atrodi izdevīgāko kasti tilpumam 36 cm³",
             vajag="burtnīca",
             soli=[
                 "Pieraksti visus veidus, kā 36 sadalīt trīs reizinātājos.",
                 "Katram variantam aprēķini virsmas laukumu.",
                 "Sakārto variantus pēc virsmas augošā secībā.",
                 "Pieraksti, kuram variantam izmēri ir vistuvāk viens otram.",
             ],
             secinajums="Vismazākā virsma sanāk variantam 4 x 3 x 3 - tam, "
                        "kas vistuvāk kubam."),

    Varianti("Kura kaste ir izdevīgāka?", [
        {"jaut": "Pie vienāda tilpuma vismazākā virsma ir...",
         "opcijas": ["formai, kas tuvāka kubam", "garākajai formai",
                     "plakanākajai formai", "visām vienāda"],
         "pareizi": 0,
         "padoms": "Kompakta forma."},
        {"jaut": "Kura kaste ar tilpumu 8 cm³ ir izdevīgākā?",
         "opcijas": ["2 x 2 x 2", "8 x 1 x 1", "4 x 2 x 1",
                     "Visām vienāda virsma"],
         "pareizi": 0,
         "padoms": "Kubs."},
        {"jaut": "Kāpēc ražotājam tas ir svarīgi?",
         "opcijas": ["Mazāk kartona - lētāks iepakojums",
                     "Lielāka kaste izskatās labāk",
                     "Tā prasa likums", "Tas nav svarīgi"],
         "pareizi": 0,
         "padoms": "Materiāls maksā."},
        {"jaut": "Kāpēc ūdens piliens ir apaļš?",
         "opcijas": ["Jo lodei ir vismazākā virsma pie dota tilpuma",
                     "Jo tā ir vieglāk",
                     "Jo ūdens ir smags", "Tas ir nejauši"],
         "pareizi": 0,
         "padoms": "Tā pati sakarība kā kastēm."},
    ], pamats=4),

    Pasaule("Kuru iepakojumu izvēlēties?",
            Ievadi("", [
                {"jaut": "Kaste 20 x 10 x 5 cm. Cik cm³ ir tilpums?",
                 "atb": ["1000", "1 000"], "padoms": "200 · 5."},
                {"jaut": "Cik cm² ir tās virsma?",
                 "atb": ["700"], "padoms": "2 · (200 + 100 + 50)."},
                {"jaut": "Kubs ar šķautni 10 cm. Cik cm³ ir tilpums?",
                 "atb": ["1000", "1 000"], "padoms": "Tas pats tilpums."},
                {"jaut": "Cik cm² ir kuba virsma?",
                 "atb": ["600"], "padoms": "6 · 100."},
            ]),
            pavediens="veikals",
            konteksts="Divi iepakojumi ar vienādu saturu var prasīt "
                      "krietni atšķirīgu kartona daudzumu.",
            kapec="Kubs ietaupa 100 cm² kartona uz katru litru produkta."),

    Kopsavilkums([
        "Salīdzinu iepakojumus ar vienādu tilpumu pēc virsmas laukuma.",
        "Zinu, ka vismazākā virsma ir formai, kas tuvāka kubam.",
        "Atrodu visus veidus, kā tilpumu sadalīt trīs reizinātājos.",
        "Pamatoju savu izvēli ar aprēķinu.",
    ]),

    Majas([
        "Atrodi visus veidus, kā 16 sadalīt trīs veselos reizinātājos.",
        "Aprēķini katra virsmu un izvēlies izdevīgāko.",
        "Atrodi mājās iepakojumu, kas *nav* izdevīgākais, un pieraksti, "
        "kāpēc ražotājs to tomēr izvēlējies.",
    ]),
]
