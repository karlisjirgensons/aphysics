# -*- coding: utf-8 -*-
"""3. klase, 161. stunda: «Kas rodas, pārgriežot kastīti?»

Izklājums ir ķermenis, atlocīts plaknē. Šo saikni vislabāk redz, pašam
pārgriežot kastīti pa šķautnēm: skaldņu skaits nemainās, mainās tikai tas,
ka tagad tās visas ir uz vienas lapas.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         izklajums)

TEMA = "Kas rodas, pārgriežot kastīti?"

MERKIS = ("No papīra modeļa iegūsim izklājumu, pārgriežot to pa šķautnēm.")

SATURS = [
    Sakums("Kā kaste pārvēršas par plakanu lapu?",
           zimejums=izklajums(3, 2, 2),
           paraksts="Sešas skaldnes, atlocītas uz vienas lapas.",
           fakti=["Izklājums ir ķermenis, atlocīts plaknē.",
                  "Kvadra izklājumā ir 6 taisnstūri - tik, cik skaldņu."]),

    Doma("Izklājumā ir tikpat skaldņu, cik ķermenim",
         "Griežot pa šķautnēm, skaldnes nesadalās - tās tikai atlokās uz "
         "vienu pusi.",
         soli=[
             "Paņem kartona kastīti.",
             "Pārgriez to pa dažām šķautnēm, bet ne pa visām.",
             "Atloc uz galda tā, lai visas skaldnes būtu plaknē.",
             "Saskaiti skaldnes - to joprojām ir sešas.",
         ],
         pieze="Pretējās skaldnes izklājumā ir vienādas: augša un apakša, "
               "priekša un aizmugure, abi sāni."),

    Petijums("Pārgriez un atloc kastīti",
             vajag="kartona kastīte, šķēres un zīmulis",
             soli=[
                 "Apzīmē kastītes skaldnes: augša, apakša, priekša, "
                 "aizmugure, divi sāni.",
                 "Pārgriez to pa šķautnēm un atloc.",
                 "Apvelc izklājumu uz lapas.",
                 "Atrodi izklājumā pretējo skaldņu pārus.",
             ],
             secinajums="Izklājumā vienādas ir tieši tās skaldnes, kas kastē "
                        "bija pretī viena otrai."),

    Paraugs("Cik taisnstūru ir izklājumā?",
            uzd="Kastītei izmēri 3, 2 un 2. Cik taisnstūru ir tās izklājumā "
                "un kuri ir vienādi?",
            soli=[
                ("6 taisnstūri",
                 "Tik, cik skaldņu."),
                ("Augša un apakša: 3 x 2",
                 "Pirmais vienādo pāris."),
                ("Priekša un aizmugure: 3 x 2; sāni: 2 x 2",
                 "Vēl divi pāri; kopā trīs pāri."),
            ],
            atbilde="6 taisnstūri, trīs vienādu pāri"),

    Ievadi("Izklājuma daļas", [
        {"jaut": "Cik taisnstūru ir kvadra izklājumā?", "atb": ["6"],
         "padoms": "Tik, cik skaldņu."},
        {"jaut": "Cik vienādu pāru ir kvadra izklājumā?", "atb": ["3"],
         "padoms": "Pretējās skaldnes."},
        {"jaut": "Cik kvadrātu ir kuba izklājumā?", "atb": ["6"],
         "padoms": "Visas skaldnes vienādas."},
        {"jaut": "Kastīte 3 x 2 x 2. Cik kvadrātvienību ir vienai 3 x 2 "
                 "skaldnei?",
         "atb": ["6"], "padoms": "3 · 2."},
        {"jaut": "Cik kvadrātvienību ir abām 3 x 2 skaldnēm kopā?",
         "atb": ["12"], "padoms": "2 · 6."},
        {"jaut": "Cik kvadrātvienību ir vienai 2 x 2 skaldnei?",
         "atb": ["4"], "padoms": "2 · 2."},
    ], pamats=4),

    Zimejums("Kuba izklājums",
             izklajums(2, 2, 2),
             paskaidro="Kubam visas sešas skaldnes ir vienādi kvadrāti, tāpēc "
                       "izklājums izskatās kā krusts.",
             ievads="Īpašais gadījums."),

    Varianti("Kas ir izklājums?", [
        {"jaut": "Cik skaldņu ir kvadra izklājumā?",
         "opcijas": ["6", "4", "8", "12"],
         "pareizi": 0, "padoms": "Tikpat, cik ķermenim."},
        {"jaut": "Kuras skaldnes izklājumā ir vienādas?",
         "opcijas": ["Pretējās", "Blakus esošās", "Visas", "Nevienas"],
         "pareizi": 0, "padoms": "Augša un apakša."},
        {"jaut": "Ko dara, iegūstot izklājumu?",
         "opcijas": ["Griež pa šķautnēm", "Griež pa skaldnēm",
                     "Saloka uz pusēm", "Saplēš"],
         "pareizi": 0, "padoms": "Skaldnes paliek veselas."},
        {"jaut": "Cik vienādu kvadrātu ir kuba izklājumā?",
         "opcijas": ["6", "3", "4", "12"],
         "pareizi": 0, "padoms": "Visas skaldnes vienādas."},
    ], pamats=4),

    Pasaule("Cik kartona vajag kastei?",
            Ievadi("", [
                {"jaut": "Kaste 3 x 2 x 2 dm. Cik kvadrātdecimetru ir abas "
                         "3 x 2 skaldnes?",
                 "atb": ["12"], "padoms": "2 · 6."},
                {"jaut": "Cik kvadrātdecimetru ir abas pārējās 3 x 2 "
                         "skaldnes?",
                 "atb": ["12"], "padoms": "2 · 6."},
                {"jaut": "Cik kvadrātdecimetru ir abi 2 x 2 sāni?",
                 "atb": ["8"], "padoms": "2 · 4."},
                {"jaut": "Cik kvadrātdecimetru kartona vajag visai kastei?",
                 "atb": ["32"], "padoms": "12 + 12 + 8."},
            ]),
            pavediens="veikals",
            konteksts="Iepakojuma ražotājs vispirms uzzīmē izklājumu - tikai "
                      "tad zina, cik kartona vajag.",
            kapec="Izklājuma laukums ir tieši tas, cik materiāla aiziet "
                  "vienai kastei."),

    Kopsavilkums([
        "Zinu, ka izklājums ir ķermenis, atlocīts plaknē.",
        "Iegūstu izklājumu, griežot pa šķautnēm.",
        "Atrodu izklājumā vienādo skaldņu pārus.",
        "Aprēķinu izklājuma laukumu.",
    ]),

    Majas([
        "Pārgriez mājās kādu tukšu kastīti un atloc to.",
        "Apvelc izklājumu uz lapas un saskaiti skaldnes.",
        "Atrodi vienādo skaldņu pārus.",
    ]),
]
