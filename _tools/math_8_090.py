# -*- coding: utf-8 -*-
"""8. klase, 90. stunda: «Kāda ir četrstūra leņķu summa?»

Diagonāle sadala jebkuru četrstūri divos trijstūros: 180° + 180° = 360°.
Leņķi pie diagonāles galiem sadalās divās daļās, bet kopā dod četrstūra
leņķus. Blokā «Četrstūri un to leņķi» šī ir pamatstunda.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, geometrija)

TEMA = "Kāda ir četrstūra leņķu summa?"

MERKIS = ("Iegūsim četrstūra leņķu summu, izmantojot trijstūra leņķu "
          "summu.")

SATURS = [
    Sakums("Cik grādu kopā ir četrstūra leņķiem?",
           zimejums=geometrija([("A", 0, 0), ("B", 6, 0), ("C", 7, 4),
                                ("D", 1, 3)],
                               nogriezni=["AB", "BC", "CD", "DA", "AC"],
                               iekrasot=[("ABC", 0), ("ACD", 1)]),
           paraksts="Diagonāle AC sadala četrstūri divos trijstūros.",
           fakti=["Četrstūra leņķu summa ir 360°.",
                  "Pamatojums: divi trijstūri pa 180°.",
                  "Tas der jebkuram četrstūrim."]),

    Doma("Divi trijstūri",
         "180° + 180° = 360°.",
         soli=[
             "Novelc diagonāli AC.",
             "Trijstūrī ABC leņķu summa ir 180°, trijstūrī ACD - arī 180°.",
             "Leņķi pie A un C sadalās divās daļās, bet kopā dod četrstūra "
             "leņķus.",
             "Tātad ∠A + ∠B + ∠C + ∠D = 360°.",
         ]),

    Paraugs("Ceturtais leņķis",
            uzd="Četrstūrī ∠A = 80°, ∠B = 95°, ∠C = 110°. Atrodi ∠D.",
            soli=[
                ("80° + 95° + 110° = 285°", "Zināmie leņķi."),
                ("∠D = 360° − 285° = 75°", "Leņķu summa 360°."),
            ],
            atbilde="75°"),

    Ievadi("Atrodi ceturto leņķi", [
        {"jaut": "90°, 90°, 90°. Ceturtais?", "atb": ["90"],
         "padoms": "360 − 270."},
        {"jaut": "100°, 70°, 120°. Ceturtais?", "atb": ["70"],
         "padoms": "360 − 290."},
        {"jaut": "Visi četri leņķi vienādi. Katrs?", "atb": ["90"],
         "padoms": "360 : 4."},
        {"jaut": "Leņķi attiecas 1 : 2 : 3 : 4. Lielākais?", "atb": ["144"],
         "padoms": "10 daļas = 360°, 1 daļa = 36°."},
        {"jaut": "Trīs leņķi pa 100°. Ceturtais?", "atb": ["60"],
         "padoms": "360 − 300."},
    ]),

    Varianti("Vai tā var būt?", [
        {"jaut": "Četrstūris ar leņķiem 100°, 100°, 100°, 70°.",
         "opcijas": ["Nē - summa 370°", "Jā", "Tikai ieliekts",
                     "Tikai trapece"],
         "pareizi": 0, "padoms": "Summai jābūt 360°."},
        {"jaut": "Cik trijstūros diagonāle sadala četrstūri?",
         "opcijas": ["2", "3", "4", "1"],
         "pareizi": 0, "padoms": "Skaties zīmējumu."},
        {"jaut": "Vai četrstūrim var būt četri šauri leņķi?",
         "opcijas": ["Nē - summa būtu mazāka par 360°", "Jā",
                     "Tikai rombam", "Tikai kvadrātam"],
         "pareizi": 0, "padoms": "4 · 89° = 356°."},
    ]),

    Pasaule("Rāmja stūri",
            Ievadi("", [
                {"jaut": "Galdnieks nozāģēja rāmja stūrus 90°, 90° un 85°. "
                         "Cik grādu būs ceturtajam?",
                 "atb": ["95"], "padoms": "360 − 265."},
                {"jaut": "Pūķa rāmja leņķi 70°, 130° un 70°. Ceturtais?",
                 "atb": ["90"], "padoms": "360 − 270."},
                {"jaut": "Cik grādu kopā ir visiem četriem stūriem jebkuram "
                         "rāmim?",
                 "atb": ["360"], "padoms": "Leņķu summa."},
            ]),
            pavediens="maja",
            konteksts="Ja vienu rāmja stūri nozāģē nepareizi, mainās arī "
                      "citi.",
            kapec="Četru leņķu summa vienmēr ir 360°."),

    Kopsavilkums([
        "Pamatoju četrstūra leņķu summu ar diviem trijstūriem.",
        "Aprēķinu nezināmo četrstūra leņķi.",
        "Pārbaudu, vai leņķi var veidot četrstūri.",
    ]),

    Majas([
        "Uzzīmē četrstūri, izmēri leņķus un saskaiti tos.",
        "Izgriez četrstūri, noplēs stūrus un saliec tos kopā - kas sanāk?",
        "Izdomā četrstūri ar leņķiem, kas attiecas 2 : 3 : 3 : 4.",
    ]),
]
