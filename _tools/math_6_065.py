# -*- coding: utf-8 -*-
"""6. klase, 65. stunda: «Kā izskatās kastes izklājums?»

Jauns mikrotemats. Izklājums ir tilts starp plakanu papīru un telpisku
ķermeni: viss, kas vēlāk būs virsmas laukums, te ir redzams kā seši
taisnstūri. Tāpēc šī stunda ir pirms jebkuras formulas.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         izklajums, kermenis)

TEMA = "Kā izskatās kastes izklājums?"

MERKIS = ("Iemācīsimies zīmēt taisnstūra paralēlskaldņa izklājumu pēc "
          "dotiem izmēriem.")

SATURS = [
    Sakums("Katra kaste sākas kā plakans papīrs",
           zimejums=izklajums(4, 3, 2),
           paraksts="Seši taisnstūri, kas saloka kasti. Pretējās skaldnes "
                    "vienmēr ir vienādas.",
           fakti=["Izklājums ir ķermenis, izklāts uz plaknes.",
                  "Kvadram tajā ir seši taisnstūri - trīs vienādu pāri.",
                  "Fabrikā kartona kastes griež tieši šādā formā."]),

    Doma("Trīs pāri vienādu taisnstūru",
         "Kvadra izklājumā ir seši taisnstūri: priekšas un aizmugures pāris, "
         "abu sānu pāris un augšas un apakšas pāris.",
         soli=[
             "Pieraksti trīs izmērus: garumu, platumu un augstumu.",
             "Uzzīmē priekšējo skaldni: garums reiz augstums.",
             "Blakus tai zīmē sānu skaldni: platums reiz augstums.",
             "Virs un zem priekšējās zīmē augšu un apakšu: garums reiz "
             "platums.",
             "Pārbaudi, vai kopā ir seši taisnstūri un trīs vienādu pāri.",
         ],
         pieze="Izklājumu var uzzīmēt vairākos veidos - krustā, T burta "
               "formā vai kā kāpnes. Svarīgi, lai katra skaldne pieskartos "
               "kaimiņam ar vienāda garuma malu."),

    Paraugs("Uzzīmē izklājumu kastei 4 x 3 x 2",
            uzd="Kaste ir 4 cm gara, 3 cm plata un 2 cm augsta. Kādi "
                "taisnstūri būs izklājumā?",
            soli=[
                ("Priekša un aizmugure: 4 x 2",
                 "Garums reiz augstums, divi gabali."),
                ("Sāni: 3 x 2",
                 "Platums reiz augstums, divi gabali."),
                ("Augša un apakša: 4 x 3",
                 "Garums reiz platums, divi gabali."),
                ("Kopā seši taisnstūri",
                 "Trīs vienādu pāri."),
            ],
            atbilde="2 gab. 4 x 2, 2 gab. 3 x 2 un 2 gab. 4 x 3"),

    Ievadi("Nosaki izklājuma daļas", [
        {"jaut": "Kaste 5 x 4 x 3. Cik taisnstūru ir izklājumā?",
         "atb": ["6"], "padoms": "Trīs vienādu pāri.",
         "zim": izklajums(5, 3, 4)},
        {"jaut": "Tā pati kaste. Kāds ir augšas taisnstūra laukums cm²?",
         "atb": ["20"], "padoms": "5 · 4."},
        {"jaut": "Kāds ir priekšas taisnstūra laukums cm²?",
         "atb": ["15"], "padoms": "5 · 3."},
        {"jaut": "Kāds ir sāna taisnstūra laukums cm²?",
         "atb": ["12"], "padoms": "4 · 3."},
        {"jaut": "Cik vienādu taisnstūru ir kuba izklājumā?",
         "atb": ["6"], "padoms": "Visas skaldnes vienādas."},
        {"jaut": "Kuba šķautne ir 3 cm. Kāds ir vienas skaldnes laukums cm²?",
         "atb": ["9"], "padoms": "3 · 3."},
    ], pamats=4),

    Petijums("Izgriez un saloka kasti",
             vajag="rūtiņu lapa, šķēres, līmlente",
             soli=[
                 "Uzzīmē izklājumu kastei 4 x 3 x 2 rūtiņas.",
                 "Izgriez to vienā gabalā.",
                 "Saloka un salīmē kasti.",
                 "Pārbaudi, vai pretējās skaldnes tiešām sakrita.",
                 "Pamēģini uzzīmēt citu izklājumu tai pašai kastei.",
             ],
             secinajums="Vienai kastei ir daudz dažādu izklājumu, bet "
                        "taisnstūru izmēri visos ir vienādi."),

    Varianti("Vai izklājums der?", [
        {"jaut": "Cik vienādu taisnstūru pāru ir kvadra izklājumā?",
         "opcijas": ["Trīs", "Divi", "Seši", "Viens"],
         "pareizi": 0,
         "padoms": "Pretējās skaldnes ir vienādas."},
        {"jaut": "Kubam ar šķautni 4 cm izklājumā ir...",
         "opcijas": ["seši kvadrāti 4 x 4", "seši dažādi taisnstūri",
                     "četri kvadrāti", "divi kvadrāti un četri taisnstūri"],
         "pareizi": 0,
         "padoms": "Visas šķautnes vienādas."},
        {"jaut": "Kas notiks, ja divas blakus skaldnes saliks ar dažāda "
                 "garuma malām?",
         "opcijas": ["Kaste nesalocīsies", "Nekas",
                     "Kaste būs lielāka", "Kaste būs mazāka"],
         "pareizi": 0,
         "padoms": "Salokot malām jāsakrīt."},
        {"jaut": "Cik izklājumu ir vienai kastei?",
         "opcijas": ["Daudz dažādu", "Tikai viens", "Divi", "Seši"],
         "pareizi": 0,
         "padoms": "Formas atšķiras, izmēri - ne."},
    ], pamats=4),

    Pasaule("Cik kartona vajag kastei?",
            Ievadi("", [
                {"jaut": "Kaste 20 x 15 x 10 cm. Kāds ir augšas laukums cm²?",
                 "atb": ["300"], "padoms": "20 · 15."},
                {"jaut": "Kāds ir priekšas laukums cm²?",
                 "atb": ["200"], "padoms": "20 · 10."},
                {"jaut": "Kāds ir sāna laukums cm²?",
                 "atb": ["150"], "padoms": "15 · 10."},
                {"jaut": "Cik cm² ir visu sešu skaldņu laukums kopā?",
                 "atb": ["1300"], "padoms": "2 · (300 + 200 + 150)."},
            ]),
            pavediens="maja",
            konteksts="Kartona patēriņu rēķina pēc izklājuma laukuma, nevis "
                      "pēc kastes izskata.",
            kapec="Izklājums pārvērš telpisku uzdevumu par plakanu."),

    Zimejums("No izklājuma uz ķermeni",
             kermenis("kvadrs"),
             paskaidro="Tas pats ķermenis, kas iepriekšējā zīmējumā bija "
                       "izklāts - seši taisnstūri, salocīti kopā.",
             ievads="Salokot izklājumu, sanāk tieši šāda kaste."),

    Kopsavilkums([
        "Zīmēju kvadra izklājumu pēc dotiem izmēriem.",
        "Zinu, ka izklājumā ir trīs vienādu taisnstūru pāri.",
        "Aprēķinu katras skaldnes laukumu.",
        "Saprotu, ka vienai kastei ir vairāki dažādi izklājumi.",
    ]),

    Majas([
        "Uzzīmē un izgriez izklājumu kubam ar šķautni 5 cm.",
        "Izjauc kādu mājās esošu kartona kastīti un apskati tās izklājumu.",
        "Pieraksti, cik taisnstūru bija un kuri no tiem bija vienādi.",
    ]),
]
