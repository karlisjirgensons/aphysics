# -*- coding: utf-8 -*-
"""4. klase, 8. stunda: «Kā skaitli uzrakstīt kā summu?»

Šķiru summa ir tas pats skaitlis, tikai «izjaukts»: 4735 = 4000 + 700 +
30 + 5. Šis pieraksts ir tilts uz galvas rēķiniem - kas prot skaitli
sadalīt, tas prot to arī pieskaitīt pa daļām.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, kolonnas,
                         restis)

TEMA = "Kā skaitli uzrakstīt kā summu?"

MERKIS = ("Pierakstīsim četrciparu skaitli kā tūkstošu, simtu, desmitu un "
          "vienu summu un salasīsim skaitli atpakaļ no summas.")

SATURS = [
    Sakums("Kā kasiere izmaksā 3264 €?",
           zimejums=restis([["banknote", "cik gab."],
                            ["1000 €", 3],
                            ["100 €", 2],
                            ["10 €", 6],
                            ["1 €", 4]],
                           "3264 € pa šķirām"),
           paraksts="3000 + 200 + 60 + 4 = 3264.",
           fakti=["Īstenībā 1000 € banknotes nav - tas ir modelis.",
                  "Bet šķiras strādā tieši tā: katrā vietā savs cipars."]),

    Doma("Skaitlis ir savu šķiru summa",
         "Katru ciparu pārvērt par tā vērtību un saliec plusus starp tiem.",
         soli=[
             "Tūkstošu ciparam pieliec trīs nulles: 4 → 4000.",
             "Simtu ciparam - divas: 7 → 700.",
             "Desmitu ciparam - vienu: 3 → 30.",
             "Vieni paliek, kā ir. Nulles summā neraksta.",
         ],
         pieze="4735 = 4000 + 700 + 30 + 5, bet 4035 = 4000 + 30 + 5."),

    Paraugs("No summas uz skaitli",
            uzd="Kāds skaitlis ir 6000 + 80 + 2?",
            soli=[
                ("6000 → 6 tūkstoši", None),
                ("simtu nav → 0", "Trūkstošā šķira ir nulle."),
                ("80 → 8 desmiti, 2 → 2 vieni", None),
                ("6000 + 80 + 2 = 6082", None),
            ],
            atbilde="6082"),

    Ievadi("Salasi skaitli", [
        {"jaut": "3000 + 400 + 20 + 7 = ?", "atb": ["3427"],
         "padoms": "Katrs saskaitāmais savā šķirā."},
        {"jaut": "8000 + 50 + 1 = ?", "atb": ["8051"],
         "padoms": "Simtu nav."},
        {"jaut": "5000 + 900 = ?", "atb": ["5900"],
         "padoms": "Desmitu un vienu nav."},
        {"jaut": "7000 + 7 = ?", "atb": ["7007"],
         "padoms": "Divas tukšas šķiras."},
        {"jaut": "2000 + 300 + 5 = ?", "atb": ["2305"],
         "padoms": "Desmitu nav."},
        {"jaut": "9000 + 90 + 9 = ?", "atb": ["9099"],
         "padoms": "Simtu nav."},
    ], pamats=4),

    Zimejums("Viens skaitlis - četri stabiņi",
             kolonnas([("tūkst.", 4000), ("simti", 700), ("desm.", 30),
                       ("vieni", 5)]),
             paskaidro="4735 lielāko daļu dod tūkstoši - vieni ir gandrīz "
                       "neredzami.",
             ievads="Tā izskatās 4735 kā summa."),

    Varianti("Kura summa pareiza?", [
        {"jaut": "Kā uzrakstīt 5608 kā summu?",
         "opcijas": ["5000 + 600 + 8", "5000 + 60 + 8", "500 + 600 + 8",
                     "5000 + 600 + 80"], "pareizi": 0,
         "padoms": "5 | 6 | 0 | 8."},
        {"jaut": "Kurš skaitlis ir 1000 + 1?",
         "opcijas": ["1001", "1010", "1100", "11"], "pareizi": 0,
         "padoms": "Tūkstotis un viens."},
        {"jaut": "Kas trūkst: 7394 = 7000 + ☐ + 90 + 4?",
         "opcijas": ["300", "3", "30", "3000"], "pareizi": 0,
         "padoms": "Trīs ir simtu šķirā."},
        {"jaut": "Kura summa *nav* 2500?",
         "opcijas": ["2000 + 50", "2000 + 500", "1000 + 1500",
                     "2400 + 100"], "pareizi": 0,
         "padoms": "2000 + 50 = 2050."},
    ], pamats=4),

    Pasaule("Kā tiek būvēts rekords?",
            Ievadi("", [
                {"jaut": "Konstruktoru komplektā ir 2000 + 400 + 50 detaļu. "
                         "Cik detaļu pavisam?",
                 "atb": ["2450"], "padoms": "2 | 4 | 5 | 0."},
                {"jaut": "Otrā komplektā 1000 + 80 + 6 detaļas. Cik tas ir?",
                 "atb": ["1086"], "padoms": "Simtu nav."},
                {"jaut": "Cik detaļu abos komplektos kopā?",
                 "atb": ["3536"], "padoms": "2450 + 1086."},
                {"jaut": "Cik simtu pavisam ir 3536?",
                 "atb": ["35"], "padoms": "3 tūkstoši = 30 simti, plus 5."},
            ]),
            pavediens="tehnika",
            konteksts="Lielajos konstruktoros ir tūkstošiem detaļu - uz "
                      "kastes skaitlis ir četrciparu.",
            kapec="Summa pa šķirām ļauj saskaitīt bez stabiņa."),

    Kopsavilkums([
        "Uzrakstu četrciparu skaitli kā šķiru summu.",
        "Salasu skaitli no šķiru summas.",
        "Zinu, ka tukšu šķiru summā neraksta, bet skaitlī raksta 0.",
    ]),

    Majas([
        "Uzraksti kā summu mājas numuru un pasta indeksa ciparus.",
        "Izdomā summu ar vienu tukšu šķiru un palūdz mājiniekam salasīt "
        "skaitli.",
        "Uzraksti 2026 kā summu divos veidos.",
    ]),
]
