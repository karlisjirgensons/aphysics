# -*- coding: utf-8 -*-
"""4. klase, 29. stunda: «Kā izdevīgāk reizināt trīs skaitļus?»

Mikrotemata noslēgums. Reizinātājus drīkst mainīt vietām un grupēt, tāpēc
25 · 7 · 4 labāk rēķināt kā 25 · 4 · 7 = 100 · 7. Galvenā prasme - meklēt
pārus, kas dod 10, 100 vai 1000: 2 · 5, 4 · 25, 8 · 125.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kā izdevīgāk reizināt trīs skaitļus?"

MERKIS = ("Noteiksim 3-4 skaitļu reizinājumu, izvēloties izdevīgu secību un "
          "pārveidojumu.")

SATURS = [
    Sakums("Kā izrēķināt 25 · 7 · 4 vienā sekundē?",
           zimejums=restis([["2 · 5", "= 10"],
                            ["4 · 25", "= 100"],
                            ["8 · 125", "= 1000"]],
                           "draudzīgie pāri"),
           paraksts="25 · 4 = 100, un 100 · 7 = 700.",
           fakti=["Reizinātājus drīkst mainīt vietām.",
                  "Meklē pārus, kas dod apaļu skaitli."]),

    Doma("Vispirms sareizini draudzīgo pāri",
         "Reizinājums nemainās, ja reizinātājus maina vietām vai grupē "
         "citādi - izvēlies secību, kurā rēķins kļūst viegls.",
         soli=[
             "Atrodi pāri, kas dod 10, 100 vai 1000.",
             "Sareizini to vispirms.",
             "Tad reizini ar pārējiem.",
             "Pārbaudi, vai neviens reizinātājs nav pazaudēts.",
         ],
         pieze="2 · 9 · 5 = (2 · 5) · 9 = 10 · 9 = 90."),

    Paraugs("4 · 13 · 25",
            uzd="Izrēķini izdevīgi 4 · 13 · 25.",
            soli=[
                ("4 · 25 = 100", "Draudzīgais pāris."),
                ("100 · 13 = 1300", None),
            ],
            atbilde="1300"),

    Ievadi("Atrodi pāri", [
        {"jaut": "5 · 17 · 2 = ?", "atb": ["170"], "padoms": "5 · 2 = 10."},
        {"jaut": "25 · 9 · 4 = ?", "atb": ["900"], "padoms": "25 · 4 = 100."},
        {"jaut": "2 · 3 · 5 · 7 = ?", "atb": ["210"], "padoms": "2 · 5 = 10, "
         "3 · 7 = 21."},
        {"jaut": "50 · 6 · 2 = ?", "atb": ["600"], "padoms": "50 · 2 = 100."},
        {"jaut": "4 · 8 · 25 = ?", "atb": ["800"], "padoms": "4 · 25."},
        {"jaut": "125 · 3 · 8 = ?", "atb": ["3000"],
         "padoms": "125 · 8 = 1000."},
    ], pamats=4),

    Varianti("Kurš pāris draudzīgs?", [
        {"jaut": "5 · 13 · 4 · 5 - kurus reizināt vispirms?",
         "opcijas": ["4 · 5 · 5 = 100", "13 · 4", "13 · 5"], "pareizi": 0,
         "padoms": "4 · 5 = 20, 20 · 5 = 100, tad 100 · 13."},
        {"jaut": "Vai 3 · 20 · 5 = 3 · 100?",
         "opcijas": ["jā", "nē"], "pareizi": 0,
         "padoms": "20 · 5 = 100."},
        {"jaut": "Cik ir 2 · 2 · 5 · 5?",
         "opcijas": ["100", "20", "14", "50"], "pareizi": 0,
         "padoms": "(2 · 5) · (2 · 5) = 10 · 10."},
        {"jaut": "Kurš reizinājums ir 1000?",
         "opcijas": ["8 · 125", "4 · 125", "8 · 25", "5 · 100"],
         "pareizi": 0, "padoms": "125 · 8."},
    ], pamats=4),

    Zimejums("Kaste ar kastītēm",
             restis([["kastē", "kastītes", "zīmuļi", "kopā"],
                     ["4 rindas", "25 kastītes", "7 katrā", "4 · 25 · 7"]],
                    "4 · 25 · 7 = 100 · 7 = 700"),
             paskaidro="Kastīšu skaits 4 · 25 = 100 - un tad tikai 100 · 7.",
             ievads="Trīs reizinātāji dzīvē ir kaste kastē."),

    Pasaule("Noliktavas pasūtījums",
            Ievadi("", [
                {"jaut": "Paletē 5 slāņi, katrā 20 kastes, katrā kastē 6 "
                         "pudeles. Cik pudeļu? (5 · 20 · 6)",
                 "atb": ["600"], "padoms": "5 · 20 = 100."},
                {"jaut": "Kravas auto ved 4 paletes pa 25 kastēm, katrā 9 "
                         "grāmatas. Cik grāmatu?",
                 "atb": ["900"], "padoms": "4 · 25 = 100."},
                {"jaut": "3 plauktu blokos ir pa 8 plauktiem, katrā plauktā 125 "
                         "kārbas. Cik kārbu pavisam?",
                 "atb": ["3000"], "padoms": "8 · 125 = 1000, · 3."},
                {"jaut": "2 mašīnas, katrā 7 paletes pa 50 kastēm. Cik "
                         "kastu?",
                 "atb": ["700"], "padoms": "2 · 50 = 100."},
            ]),
            pavediens="tehnika",
            konteksts="Noliktavā preces krauj slāņos, rindās un kastēs - "
                      "trīs vai četri reizinātāji.",
            kapec="Pareizā secība ļauj izrēķināt bez kalkulatora."),

    Kopsavilkums([
        "Zinu, ka reizinātājus drīkst mainīt vietām un grupēt.",
        "Atrodu draudzīgos pārus: 2 · 5, 4 · 25, 8 · 125.",
        "Izvēlos izdevīgāko secību.",
    ]),

    Majas([
        "Atrodi mājās kaut ko, kas sakrauts rindās un slāņos, un izrēķini "
        "kopskaitu.",
        "Izdomā reizinājumu ar 4 reizinātājiem, kurā ir divi draudzīgi pāri.",
        "Izrēķini 25 · 25 · 4 · 4 izdevīgi.",
    ]),
]
