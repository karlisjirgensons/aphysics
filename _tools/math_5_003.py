# -*- coding: utf-8 -*-
"""5. klase, 3. stunda: «Kādi skaitļi der nosacījumiem?»

Pirmā stunda, kurā atbilde nav viens skaitlis, bet visi skaitļi, kas der.
Te sākas doma par skaitļu kopu: nosacījumu izlasa, pārbauda uz vairākiem
skaitļiem un tikai tad pieraksta visus, kas der. Nākamajā stundā divas
šādas kopas salīdzinās Venna diagrammā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, kolonnas)

TEMA = "Kādi skaitļi der nosacījumiem?"

MERKIS = ("Iemācīsimies atrast visus skaitļus, kas der dotajam nosacījumam, "
          "un pateikt, kas tiem kopīgs.")

SATURS = [
    Sakums("Cik planētu der nosacījumam?",
           zimejums=kolonnas([("Merkurs", 0), ("Venera", 0), ("Zeme", 1),
                              ("Marss", 2), ("Jupiters", 95)]),
           paraksts="Pavadoņu skaits. Nosacījums «vairāk par vienu» der "
                    "divām planētām.",
           fakti=["Atbilde nav viens skaitlis, bet viss saraksts."]),

    Doma("Nosacījumu pārbauda pa vienam skaitlim",
         "Der tie un tikai tie skaitļi, kuriem izpildās visi nosacījumi "
         "vienlaikus.",
         soli=[
             "Izlasi nosacījumu un pasaki to saviem vārdiem.",
             "Sāc ar mazāko skaitli, kas vispār varētu derēt.",
             "Katru pārbaudi: der vai neder.",
             "Uzraksti visus, kas der, no mazākā uz lielāko.",
         ],
         pieze="Ja nosacījumi ir divi, skaitlim jāatbilst abiem. Vārdiņš "
               "«un» sašaurina sarakstu, vārdiņš «vai» to paplašina."),

    Paraugs("Kuri divciparu skaitļi der?",
            uzd="Uzraksti visus divciparu skaitļus, kas dalās ar 15.",
            soli=[
                ("Divciparu skaitļi ir no 10 līdz 99.",
                 "Vispirms nosaka, kur vispār meklēt."),
                ("15, 30, 45, 60, 75, 90",
                 "Skaita pa 15: 15 · 1, 15 · 2, 15 · 3 un tā tālāk, kamēr "
                 "vēl ietilpst divos ciparos."),
                ("15 · 7 = 105 - jau par lielu",
                 "Pēdējo pārbauda: tālāk skaitlis vairs nav divciparu."),
            ],
            atbilde="15, 30, 45, 60, 75, 90 - kopā seši skaitļi"),

    Ievadi("Cik skaitļu der?", [
        {"jaut": "Cik ir divciparu skaitļu, kas dalās ar 25?",
         "atb": ["3"], "padoms": "25, 50, 75 - un tad jau 100."},
        {"jaut": "Cik ir skaitļu no 1 līdz 30, kas dalās ar 7?",
         "atb": ["4"], "padoms": "7, 14, 21, 28."},
        {"jaut": "Cik ir trīsciparu skaitļu, kas sākas ar 9 un beidzas ar 0?",
         "atb": ["10"], "padoms": "9_0 - vidū var būt jebkurš cipars."},
        {"jaut": "Cik ir divciparu skaitļu, kuru abi cipari ir vienādi?",
         "atb": ["9"], "padoms": "11, 22, 33 ... 99."},
        {"jaut": "Cik ir skaitļu no 40 līdz 60, kas dalās ar 10?",
         "atb": ["3"], "padoms": "40, 50, 60 - abus galus arī skaita."},
        {"jaut": "Cik ir divciparu skaitļu, kuru ciparu summa ir 3?",
         "atb": ["3"], "padoms": "12, 21, 30."},
    ], pamats=4,
        ievads="Uzraksti sarakstu melnrakstā un tad ieraksti, cik to ir."),

    Varianti("Vai šis skaitlis der?", [
        {"jaut": "Nosacījums: trīsciparu skaitlis, kas dalās ar 5. Kurš der?",
         "opcijas": ["405", "45", "4 050", "406"],
         "pareizi": 0,
         "padoms": "Jābūt tieši trim cipariem un jābeidzas ar 0 vai 5."},
        {"jaut": "Nosacījums: skaitlis lielāks par 100 *un* mazāks par 110. "
                 "Kurš neder?",
         "opcijas": ["110", "101", "105", "109"],
         "pareizi": 0,
         "padoms": "«Mazāks par 110» nozīmē, ka pats 110 neder."},
        {"jaut": "Kurš saraksts ir pilns: divciparu skaitļi, kas dalās ar 30?",
         "opcijas": ["30, 60, 90", "30, 60", "30, 60, 90, 120", "60, 90"],
         "pareizi": 0,
         "padoms": "120 jau ir trīsciparu skaitlis."},
        {"jaut": "Nosacījums: pāra skaitlis *un* lielāks par 8. Kurš der?",
         "opcijas": ["10", "9", "7", "8"],
         "pareizi": 0,
         "padoms": "Jāizpildās abiem nosacījumiem reizē."},
    ], pamats=4),

    Pasaule("Kuri gadi der?",
            Ievadi("", [
                {"jaut": "Cik gadu no 2020 līdz 2030 dalās ar 4?",
                 "atb": ["3"], "padoms": "2020, 2024, 2028."},
                {"jaut": "Cik ir divciparu skaitļu, kas dalās ar 12?",
                 "atb": ["8"], "padoms": "No 12 līdz 96."},
                {"jaut": "Starp 1 un 20 - cik skaitļu dalās ar 6?",
                 "atb": ["3"], "padoms": "6, 12, 18."},
                {"jaut": "Cik gadu no 2000 līdz 2050 dalās ar 25?",
                 "atb": ["3"], "padoms": "2000, 2025, 2050."},
            ]),
            pavediens="kosmoss",
            konteksts="Raķešu startus plāno pēc nosacījumiem: logs atveras "
                      "tikai dažas dienas gadā.",
            kapec="Kad nosacījumu ir vairāki, der tikai tie datumi, kas "
                  "izpilda visus reizē."),

    Kopsavilkums([
        "Izlasu nosacījumu un pārbaudu, vai skaitlis tam der.",
        "Uzrakstu visus skaitļus, kas der, kārtībā no mazākā uz lielāko.",
        "Zinu, ka divi nosacījumi ar «un» jāizpilda abi reizē.",
    ]),

    Majas([
        "Uzraksti visus divciparu skaitļus, kuru ciparu summa ir 10.",
        "Padomā, cik ir trīsciparu skaitļu, kas sākas un beidzas ar vienu un "
        "to pašu ciparu.",
        "Atrodi mājās trīs skaitļus, kas der nosacījumam «lielāks par 100».",
    ]),
]
