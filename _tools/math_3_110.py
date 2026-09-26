# -*- coding: utf-8 -*-
"""3. klase, 110. stunda: «Kā ar locīšanu iegūt taisnu leņķi?»

Praktiska stunda: taisnu leņķi var uztaisīt no jebkura papīra gabala, arī no
saplēsta - divi locījumi, un leņķis ir precīzs. Tas parāda, ka taisns leņķis
nav «kaut kas no lineāla», bet rodas no pašas simetrijas.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         lenkis)

TEMA = "Kā ar locīšanu iegūt taisnu leņķi?"

MERKIS = ("Lokot papīru, iegūsim taisnus, šaurus un platus leņķus.")

SATURS = [
    Sakums("Kā uztaisīt taisnu leņķi bez lineāla?",
           zimejums=lenkis([(0, ""), (90, ""), (180, "")],
                           [(0, 90, "taisns"), (90, 180, "taisns")],
                           "divi taisni leņķi"),
           paraksts="Izstiepts leņķis, salocīts uz pusēm, dod divus taisnus.",
           fakti=["Taisnu leņķi var salocīt no jebkura papīra gabala.",
                  "Divi locījumi - un leņķis ir precīzs."]),

    Doma("Puse no izstiepta leņķa ir taisns leņķis",
         "Izstiepts leņķis ir taisna līnija; salokot to tieši uz pusēm, "
         "sanāk divi vienādi leņķi - taisni.",
         soli=[
             "Saloc papīru vienreiz - locījums ir taisna līnija.",
             "Saloc vēlreiz tā, lai pirmā locījuma malas sakristu.",
             "Atloc - sanāca četri vienādi leņķi.",
             "Katrs no tiem ir taisns leņķis.",
         ],
         pieze="Ja otro locījumu izdara nevienmērīgi, malas nesakrīt un "
               "leņķi nav vienādi - tieši sakrišana ir pārbaude."),

    Petijums("Saloc leņķus",
             vajag="papīra gabals (var būt saplēsts) un zīmulis",
             soli=[
                 "Saloc papīru vienreiz un atloc.",
                 "Saloc vēlreiz tā, lai locījuma malas sakristu.",
                 "Atloc un apvelc visus četrus leņķus.",
                 "Salieciet papīru vēl reizi un iegūstiet šaurāku leņķi.",
             ],
             secinajums="Divi locījumi dod taisnu leņķi, trešais - pusi no "
                        "tā, tas ir, šauru leņķi."),

    Paraugs("Cik leņķu sanāk pēc diviem locījumiem?",
            uzd="Papīru saloka divas reizes, otro reizi uz pusēm. Cik leņķu "
                "sanāk ap locījuma punktu?",
            soli=[
                ("Pirmais locījums - taisna līnija",
                 "Tas ir izstiepts leņķis."),
                ("Otrais locījums - uz pusēm",
                 "Katrā pusē sanāk divi vienādi leņķi."),
                ("Kopā četri taisni leņķi",
                 "Tie aizpilda pilnu apgriezienu."),
            ],
            atbilde="4 taisni leņķi"),

    Ievadi("Locījumi un leņķi", [
        {"jaut": "Cik taisnu leņķu sanāk ap locījuma punktu?", "atb": ["4"],
         "padoms": "Pilns apgrieziens."},
        {"jaut": "Cik taisnu leņķu ir izstieptā leņķī?", "atb": ["2"],
         "padoms": "Puse apgrieziena."},
        {"jaut": "Cik šauru leņķu sanāk, ja taisnu leņķi saloc uz pusēm?",
         "atb": ["2"], "padoms": "Katrs ir puse no taisnā."},
        {"jaut": "Cik leņķu sanāk pēc trim locījumiem uz pusēm?",
         "atb": ["8"], "padoms": "4 · 2."},
        {"jaut": "Cik taisnu leņķu ir divos pilnos apgriezienos?",
         "atb": ["8"], "padoms": "2 · 4."},
        {"jaut": "Cik locījumu vajag, lai iegūtu taisnu leņķi?",
         "atb": ["2"], "padoms": "Viens dod līniju, otrs to dala."},
    ], pamats=4),

    Zimejums("Taisns leņķis, salocīts uz pusēm",
             lenkis([(0, ""), (45, ""), (90, "")],
                    [(0, 45, "šaurs"), (45, 90, "šaurs")],
                    "divi šauri leņķi"),
             paskaidro="Taisns leņķis, salocīts uz pusēm, dod divus vienādus "
                       "šaurus leņķus.",
             ievads="Trešais locījums."),

    Varianti("Ko dod locījums?", [
        {"jaut": "Cik locījumu vajag taisnam leņķim?",
         "opcijas": ["Divi", "Viens", "Trīs", "Četri"],
         "pareizi": 0, "padoms": "Vispirms līnija, tad puse."},
        {"jaut": "Kā pārbaudīt, vai locījums izdevās?",
         "opcijas": ["Malām jāsakrīt", "Papīram jābūt gludam",
                     "Locījumam jābūt garam", "Nekā"],
         "pareizi": 0, "padoms": "Sakrišana nozīmē vienādus leņķus."},
        {"jaut": "Kāds leņķis sanāk, salokot taisnu leņķi uz pusēm?",
         "opcijas": ["Šaurs", "Plats", "Taisns", "Izstiepts"],
         "pareizi": 0, "padoms": "Puse no taisnā."},
        {"jaut": "Cik taisnu leņķu aizpilda pilnu apgriezienu?",
         "opcijas": ["4", "2", "3", "8"],
         "pareizi": 0, "padoms": "Četri pagriezieni."},
    ], pamats=4),

    Pasaule("Kā pārbauda detaļas leņķi?",
            Ievadi("", [
                {"jaut": "Detaļai jābūt 4 taisniem leņķiem. Cik ir kopā "
                         "10 detaļām?",
                 "atb": ["40"], "padoms": "10 · 4."},
                {"jaut": "Vienas detaļas pārbaude aizņem 3 minūtes. Cik "
                         "minūšu vajag 10 detaļām?",
                 "atb": ["30"], "padoms": "10 · 3."},
                {"jaut": "Cik detaļu var pārbaudīt vienā stundā?",
                 "atb": ["20"], "padoms": "60 : 3."},
                {"jaut": "Cik taisnu leņķu tas ir?", "atb": ["80"],
                 "padoms": "20 · 4."},
            ]),
            pavediens="tehnika",
            konteksts="Rūpnīcā detaļu leņķus pārbauda ar uzstūri - tieši "
                      "tāpat kā tu ar papīra stūri.",
            kapec="Ja leņķis nav taisns, detaļa neietilps savā vietā."),

    Kopsavilkums([
        "Iegūstu taisnu leņķi, lokot papīru.",
        "Zinu, ka divi locījumi dod taisnu leņķi.",
        "Iegūstu šauru leņķi, salokot taisno uz pusēm.",
        "Pārbaudu locījumu pēc malu sakrišanas.",
    ]),

    Majas([
        "Saloc taisnu leņķi no saplēsta papīra gabala.",
        "Pārbaudi ar to kādu mājas stūri.",
        "Saloc arī šauru un platu leņķi.",
    ]),
]
