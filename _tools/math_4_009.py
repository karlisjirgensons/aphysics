# -*- coding: utf-8 -*-
"""4. klase, 9. stunda: «Kurš skaitlis lielāks?»

Salīdzināšana pa šķirām no kreisās: pirmā šķira, kurā cipari atšķiras,
izšķir visu. Tāpēc 5099 < 5100, lai gan deviņnieku ir daudz. Stunda
nostiprina arī zīmes «>» un «<» lasīšanu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, kolonnas,
                         restis)

TEMA = "Kurš skaitlis lielāks?"

MERKIS = ("Salīdzināsim četrciparu skaitļus pa šķirām un pierakstīsim "
          "rezultātu ar zīmēm «>» un «<».")

SATURS = [
    Sakums("Kurš kalns augstāks?",
           zimejums=kolonnas([("Everests", 8849), ("K2", 8611),
                              ("Mont Blanc", 4806)], " m"),
           paraksts="Pirmie cipari 8 un 8 - izšķir simti: 8 un 6.",
           fakti=["Everests ir augstākais kalns pasaulē.",
                  "Tā augstums ir četrciparu skaitlis metros.",
                  "Salīdzinot sāk ar tūkstošiem."]),

    Doma("Salīdzini pa šķirām no kreisās",
         "Pirmā šķira, kurā cipari atšķiras, pasaka, kurš skaitlis ir "
         "lielāks.",
         soli=[
             "Ja ciparu skaits atšķiras, lielāks ir garākais skaitlis.",
             "Salīdzini tūkstošus.",
             "Ja tie vienādi - simtus, tad desmitus, tad vienus.",
             "Atvērtā zīmes puse skatās uz lielāko: 8849 > 8611.",
         ],
         pieze="5099 < 5100: tūkstoši vienādi, bet simtos 0 < 1 - tālāk "
               "vairs nav jāskatās."),

    Paraugs("3457 vai 3475?",
            uzd="Salīdzini 3457 un 3475.",
            soli=[
                ("3 = 3", "Tūkstoši vienādi."),
                ("4 = 4", "Simti vienādi."),
                ("5 < 7", "Desmitos atšķiras - te viss izšķiras."),
                ("3457 < 3475", None),
            ],
            atbilde="3457 < 3475"),

    Varianti("Liec zīmi", [
        {"jaut": "4520 ☐ 4502", "opcijas": [">", "<", "="], "pareizi": 0,
         "padoms": "Desmitos 2 > 0."},
        {"jaut": "6099 ☐ 6100", "opcijas": ["<", ">", "="], "pareizi": 0,
         "padoms": "Simtos 0 < 1."},
        {"jaut": "999 ☐ 1000", "opcijas": ["<", ">", "="], "pareizi": 0,
         "padoms": "Trīs cipari pret četriem."},
        {"jaut": "7000 + 300 ☐ 7300", "opcijas": ["=", "<", ">"],
         "pareizi": 0, "padoms": "Summa ir tieši 7300."},
        {"jaut": "8888 ☐ 8889", "opcijas": ["<", ">", "="], "pareizi": 0,
         "padoms": "Atšķiras tikai vieni."},
        {"jaut": "5010 ☐ 5001", "opcijas": [">", "<", "="], "pareizi": 0,
         "padoms": "Desmitos 1 > 0."},
    ], pamats=4),

    Ievadi("Sakārto un atrodi", [
        {"jaut": "Kurš ir lielākais: 3809, 3890, 3098, 3980?",
         "atb": ["3980"], "padoms": "Salīdzini simtus."},
        {"jaut": "Kurš ir mazākais: 2451, 2415, 2541, 2514?",
         "atb": ["2415"], "padoms": "Simtos 4 < 5, tad desmitos."},
        {"jaut": "Lielākais četrciparu skaitlis no cipariem 3, 8, 1, 6?",
         "atb": ["8631"], "padoms": "Lielāko ciparu liec priekšā."},
        {"jaut": "Mazākais četrciparu skaitlis no cipariem 0, 5, 2, 7?",
         "atb": ["2057"], "padoms": "Nulli nedrīkst likt priekšā."},
    ]),

    Zimejums("Kur izšķiras?",
             restis([["", "T", "S", "D", "V"],
                     ["5099", 5, 0, 9, 9],
                     ["5100", 5, 1, 0, 0]],
                    "salīdzina no kreisās"),
             paskaidro="Simtu šķirā 0 < 1 - tāpēc 5099 ir mazāks, "
                       "lai cik lieli būtu tālākie cipari.",
             ievads="Tabula parāda, kur tieši skaitļi atšķiras."),

    Pasaule("Kurš kalns ir kurš?",
            Varianti("", [
                {"jaut": "Kilimandžaro ir 5895 m, Elbruss - 5642 m. Kurš "
                         "augstāks?",
                 "opcijas": ["Kilimandžaro", "Elbruss", "vienādi"],
                 "pareizi": 0, "padoms": "Simtos 8 > 6."},
                {"jaut": "Mont Blanc ir 4806 m, Materhorns - 4478 m. Kurš "
                         "zemāks?",
                 "opcijas": ["Materhorns", "Mont Blanc", "vienādi"],
                 "pareizi": 0, "padoms": "Simtos 4 < 8."},
                {"jaut": "Kurš no šiem kalniem ir augstāks par 5000 m?",
                 "opcijas": ["Elbruss 5642 m", "Mont Blanc 4806 m",
                             "Materhorns 4478 m"],
                 "pareizi": 0, "padoms": "Skaties tūkstošus."},
            ]),
            pavediens="celojums",
            konteksts="Alpīnisti plāno kāpienus pēc augstuma - un tie visi "
                      "ir četrciparu skaitļi.",
            kapec="Kas salīdzina pa šķirām, tas nekad nesajauc 4806 un "
                  "4860."),

    Kopsavilkums([
        "Salīdzinu četrciparu skaitļus pa šķirām no kreisās.",
        "Zinu, ka garāks skaitlis ir lielāks.",
        "Pareizi lietoju zīmes «>» un «<».",
        "Sastādu lielāko un mazāko skaitli no dotiem cipariem.",
    ]),

    Majas([
        "Atrodi trīs cenas virs 1000 € (reklāmā vai internetā) un sakārto.",
        "Uzraksti lielāko un mazāko četrciparu skaitli no sava tālruņa "
        "pēdējiem četriem cipariem.",
        "Pajautā vecākiem dzimšanas gadus un sakārto tos augošā secībā.",
    ]),
]
