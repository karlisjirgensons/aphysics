# -*- coding: utf-8 -*-
"""5. klase, 15. stunda: «Kā noapaļošanu pierakstīt kā algoritmu?»

Kārtula jau zināma (14. stunda) - te to pieraksta tā, lai izpildīt varētu
kāds cits, arī tāds, kas neko nesaprot no skaitļiem. Sazarojums «ja ... tad
... citādi ...» te parādās pirmo reizi, un tieši tāpēc stundā vairāk pārbauda
svešu algoritmu, nekā rēķina.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti)

TEMA = "Kā noapaļošanu pierakstīt kā algoritmu?"

MERKIS = ("Mācīsimies pierakstīt noapaļošanu kā sazarotu algoritmu un "
          "pārbaudīt to ar piemēriem.")

SATURS = [
    Sakums("Vai tavu kārtulu var izpildīt cits?",
           fakti=["Algoritms ir soļu virkne, kuru izpilda, nedomājot līdzi.",
                  "Sazarojums: «ja ... tad ... citādi ...».",
                  "Labs algoritms strādā ar katru skaitli, ne tikai tavējo."]),

    Doma("Algoritmā katrs solis ir viena darbība",
         "Ja solī jādomā, tas vēl nav solis - to jāsadala sīkāk.",
         soli=[
             "Nosaki šķiru, līdz kurai noapaļo.",
             "Pasvītro ciparu pa labi no šķiras.",
             "Ja pasvītrotais cipars ir mazāks par 5, ej uz 5. soli.",
             "Citādi šķiras ciparam pieskaiti 1.",
             "Visus ciparus pa labi no šķiras aizstāj ar nullēm.",
         ],
         pieze="4. solis ir sazarojums: tas notiek tikai tad, ja 3. soļa "
               "nosacījums nav izpildīts. Bez sazarojuma algoritms noapaļotu "
               "vienmēr uz leju."),

    Paraugs("Izpildi algoritmu soli pa solim",
            uzd="Noapaļo 2 749 līdz simtiem, pierakstot katru algoritma soli.",
            soli=[
                ("1. Šķira: simti. Simtu cipars ir 7",
                 "Skaitlī 2 749 simti ir trešais cipars no labās."),
                ("2. Pa labi no simtiem ir 4",
                 "Tas ir desmitu cipars."),
                ("3. Vai 4 < 5? Jā - ejam uz 5. soli",
                 "Sazarojums aizved garām 4. solim."),
                ("5. Ciparus pa labi aizstāj ar nullēm: 2 700",
                 "Simtu cipars paliek 7."),
            ],
            atbilde="2 749 ≈ 2 700"),

    Varianti("Pārbaudi svešu algoritmu", [
        {"jaut": "Kāds solis algoritmam ir jāsāk ar: «Nosaki šķiru...». "
                 "Kāpēc tas ir pirmais?",
         "opcijas": ["Jo bez šķiras nezina, uz kuru ciparu skatīties",
                     "Jo pirmais solis vienmēr ir grūtākais",
                     "Jo šķiru izvēlas nejauši",
                     "Jo citādi skaitlis pazustu"],
         "pareizi": 0,
         "padoms": "Visi pārējie soļi runā par «ciparu pa labi no šķiras»."},
        {"jaut": "Kāds skolēns uzrakstīja: «Ja cipars ir lielāks par 5, "
                 "pieskaiti 1.» Kas tur nepareizi?",
         "opcijas": ["Aizmirsts pats skaitlis 5",
                     "Pieskaitīt vajag 2",
                     "Jāraksta «mazāks par 5»",
                     "Nekas, algoritms ir pareizs"],
         "pareizi": 0,
         "padoms": "Pārbaudi algoritmu ar skaitli 450."},
        {"jaut": "Ko dara solis «aizstāj ciparus ar nullēm»?",
         "opcijas": ["Nogriež skaitli uz leju līdz apaļam",
                     "Palielina skaitli", "Izmet skaitli",
                     "Maina šķiras ciparu"],
         "pareizi": 0,
         "padoms": "Pēc tā skaitlis beidzas ar nullēm."},
        {"jaut": "Kāpēc algoritmā vajag sazarojumu?",
         "opcijas": ["Jo skaitli noapaļo gan uz augšu, gan uz leju",
                     "Jo soļu ir par daudz",
                     "Jo skaitļi ir dažāda garuma",
                     "Jo tā ir skaistāk"],
         "pareizi": 0,
         "padoms": "Bez tā visi skaitļi noapaļotos vienā virzienā."},
        {"jaut": "Kurš algoritms noapaļo 3 500 līdz tūkstošiem pareizi?",
         "opcijas": ["Tas, kurā 5 ietilpst «pieskaiti 1» zarā",
                     "Tas, kurā 5 ietilpst «atstāj» zarā",
                     "Abi", "Neviens"],
         "pareizi": 0,
         "padoms": "3 500 ≈ 4 000."},
        {"jaut": "Ko nozīmē, ja algoritms ar vienu skaitli strādā, bet ar "
                 "citu ne?",
         "opcijas": ["Algoritms ir nepilnīgs",
                     "Skaitlis ir nepareizs",
                     "Tā notiek ar visiem algoritmiem",
                     "Jāmaina skaitlis"],
         "pareizi": 0,
         "padoms": "Algoritmam jāstrādā ar katru skaitli."},
    ], pamats=4),

    Ievadi("Izpildi algoritmu pats", [
        {"jaut": "Šķira: simti. Skaitlis 2 749. Kurš cipars ir pa labi no "
                 "šķiras?",
         "atb": ["4"], "padoms": "Desmitu cipars."},
        {"jaut": "Turpini: kāds skaitlis sanāk?", "atb": ["2700"],
         "padoms": "4 < 5, tāpēc simtus neaiztiek."},
        {"jaut": "Šķira: tūkstoši. Skaitlis 8 573. Kāds skaitlis sanāk?",
         "atb": ["9000"], "padoms": "Pa labi no tūkstošiem ir 5."},
        {"jaut": "Šķira: desmiti. Skaitlis 1 246. Kāds skaitlis sanāk?",
         "atb": ["1250"], "padoms": "Pa labi no desmitiem ir 6."},
        {"jaut": "Šķira: simti. Skaitlis 45 049. Kāds skaitlis sanāk?",
         "atb": ["45000"], "padoms": "Pa labi no simtiem ir 4."},
        {"jaut": "Šķira: tūkstoši. Skaitlis 29 500. Kāds skaitlis sanāk?",
         "atb": ["30000"], "padoms": "9 tūkstošiem pieskaita 1."},
    ], pamats=4,
        ievads="Ej soli pa solim: šķira → cipars pa labi → sazarojums → "
               "nulles."),

    Pasaule("Kā uzskaita putnus?",
            Ievadi("", [
                {"jaut": "Uzskaites lapā jāieraksta skaits, noapaļots līdz "
                         "desmitiem. Saskaitīti 137 gulbji. Ko ieraksta?",
                 "atb": ["140"], "padoms": "Pa labi no desmitiem ir 7."},
                {"jaut": "Saskaitītas 1 462 zosis, noapaļo līdz simtiem.",
                 "atb": ["1500"], "padoms": "Pa labi no simtiem ir 6."},
                {"jaut": "Saskaitīti 24 ērgļi, noapaļo līdz desmitiem.",
                 "atb": ["20"], "padoms": "Pa labi no desmitiem ir 4."},
                {"jaut": "Saskaitīti 8 995 strazdi, noapaļo līdz simtiem.",
                 "atb": ["9000"], "padoms": "89 simtiem pieskaita vienu."},
            ]),
            pavediens="daba",
            konteksts="Putnu uzskaitē visi brīvprātīgie strādā pēc vienas "
                      "instrukcijas - citādi skaitļus nevar salikt kopā.",
            kapec="Algoritms der tikai tad, ja to izpilda visi vienādi."),

    Kopsavilkums([
        "Pierakstu noapaļošanu kā soļu virkni, kurā katrs solis ir viena "
        "darbība.",
        "Lietoju sazarojumu «ja ... tad ... citādi ...».",
        "Pārbaudu algoritmu ar piemēriem, arī ar tādiem, kur cipars ir 5.",
    ]),

    Majas([
        "Uzraksti savu noapaļošanas algoritmu un iedod to kādam mājās "
        "izpildīt bez paskaidrojumiem.",
        "Atrodi skaitli, ar kuru tavs algoritms kļūdās, un izlabo to.",
        "Pieraksti kā algoritmu vēl kaut ko ikdienišķu - piemēram, kā "
        "saklāj galdu.",
    ]),
]
