# -*- coding: utf-8 -*-
"""9. klase, 131. stunda: «Kā atrast jebkuru locekli?»

a_n = a_1 + (n − 1)d - formula no eksāmena formulu lapas. Līdz n-tajam
loceklim ir n − 1 solis, katrs d garumā. Ar to atrod 100. locekli bez
99 saskaitīšanām.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Kustiba, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, taisne)

TEMA = "Kā atrast jebkuru locekli?"

MERKIS = ("Lietosim vispārīgā locekļa formulu, lai aprēķinātu doto "
          "locekli.")

SATURS = [
    Sakums("Līdz 5. loceklim - 4 soļi",
           zimejums=taisne(0, 16, 2, atzimes=[(2, "a₁"), (14, "a₅")],
                           bultas=[(2, 14, "4d")]),
           paraksts="a₁ = 2, d = 3: a₅ = 2 + 4 · 3 = 14.",
           fakti=["No a_1 līdz a_n ir (n − 1) soļi.",
                  "a_n = a_1 + (n − 1)d.",
                  "Formula ir eksāmena formulu lapā."]),

    Doma("Vispārīgā locekļa formula",
         "a_n = a_1 + (n − 1)d.",
         soli=[
             "Nosaki a_1 un d.",
             "Ievieto n.",
             "Vispirms (n − 1) · d, tad pieskaiti a_1.",
             "Pārbaude: n = 1 dod a_1.",
         ]),

    Paraugs("100. loceklis",
            uzd="Progresija 7, 11, 15, ... Atrodi a_{100}.",
            soli=[
                ("a_1 = 7, d = 4", "Dati."),
                ("a_{100} = 7 + 99 · 4", "Formula."),
                ("= 7 + 396 = 403", "Aprēķins."),
            ],
            atbilde="a_{100} = 403"),

    Ievadi("Aprēķini", [
        {"jaut": "a_1 = 5, d = 3. a_{10} = ?", "atb": ["32"],
         "padoms": "5 + 27."},
        {"jaut": "a_1 = 100, d = −7. a_{11} = ?", "atb": ["30"],
         "padoms": "100 − 70."},
        {"jaut": "2, 9, 16, ... a_{20} = ?", "atb": ["135"],
         "padoms": "2 + 19 · 7."},
        {"jaut": "a_1 = −3, d = 0,5. a_9 = ?", "atb": ["1"],
         "padoms": "−3 + 4."},
        {"jaut": "a_1 = 4, d = 6. Vispārīgā formula a_n = 6n − ?",
         "atb": ["2"], "padoms": "4 + 6n − 6."},
    ], pamats=3),

    Varianti("Kur kļūda?", [
        {"jaut": "a_1 = 3, d = 5. Skolēns: a_{10} = 3 + 10 · 5 = 53.",
         "opcijas": ["Jāreizina ar 9: a_{10} = 48", "Pareizi",
                     "Jābūt 3 · 10 + 5", "Jābūt 50"],
         "pareizi": 0, "padoms": "n − 1 soļi."},
        {"jaut": "a_n = a_1 + (n − 1)d ar a_1 = 8, d = 2 dod...",
         "opcijas": ["a_n = 2n + 6", "a_n = 8n + 2", "a_n = 2n + 8",
                     "a_n = 10n"],
         "pareizi": 0, "padoms": "8 + 2n − 2."},
    ]),

    Pasaule("Mēneša krājkonts",
            Kustiba("", [
                {"jaut": "Janvārī kontā 50 €, katru mēnesi +25 €. Cik € būs "
                         "12. mēnesī?",
                 "atb": 325, "beigas": 400, "iedala": 50, "mers": "€",
                 "merkis": "decembris", "objekts": "Konts",
                 "padoms": "50 + 11 · 25."},
                {"jaut": "Kurā mēnesī kontā būs 200 €?",
                 "atb": 7, "beigas": 12, "iedala": 1, "mers": "",
                 "merkis": "200 €", "objekts": "Mēnesis",
                 "padoms": "50 + (n − 1) · 25 = 200."},
            ]),
            pavediens="veikals",
            konteksts="Regulārs krājums ir aritmētiskā progresija.",
            kapec="Formula atbild par jebkuru mēnesi uzreiz."),

    Kopsavilkums([
        "Lietoju a_n = a_1 + (n − 1)d.",
        "Aprēķinu tālu locekli bez visiem iepriekšējiem.",
        "Pārveidoju formulu formā a_n = dn + b.",
    ]),

    Majas([
        "Atrodi a_{50} progresijai 3, 8, 13, ...",
        "Atrodi a_{15}, ja a_1 = 60, d = −4.",
        "Aprēķini, cik būs sakrāts pēc gada, ja krāj 10 € nedēļā.",
    ]),
]
