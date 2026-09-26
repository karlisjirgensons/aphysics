# -*- coding: utf-8 -*-
"""3. klase, 29. stunda: «Kā aug virkne, kas trīskāršojas?»

Virknes, kurās katrs nākamais loceklis ir 2 vai 3 reizes lielāks, ir pirmā
sastapšanās ar augšanu, kas nav vienmērīga. Skolēns redz, ka reizināšanas
virkne no saskaitīšanas virknes atšķiras ļoti ātri - un tieši tas vēlāk
paskaidro, kāpēc daudzkāršošanās ir bīstama vai izdevīga.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, Zimejums,
                         kolonnas)

TEMA = "Kā aug virkne, kas trīskāršojas?"

MERKIS = ("Veidosim virknes, kurās katrs nākamais skaitlis ir 2 vai 3 reizes "
          "lielāks vai mazāks, un aprakstīsim to augšanu.")

SATURS = [
    Sakums("Kas notiek, ja katru dienu skaits trīskāršojas?",
           zimejums=kolonnas([("1. d.", 1), ("2. d.", 3), ("3. d.", 9),
                              ("4. d.", 27), ("5. d.", 81)]),
           paraksts="Pirmās dienas stabiņu gandrīz neredz.",
           fakti=["Saskaitot pa 3, piektajā dienā būtu 13.",
                  "Reizinot ar 3, piektajā dienā jau ir 81."]),

    Doma("Reizināšanas virkne aug daudz ātrāk",
         "Ja katrs nākamais skaitlis ir 3 reizes lielāks, virkne dažos "
         "soļos aizskrien tālu prom.",
         soli=[
             "Pieraksti pirmo skaitli.",
             "Reizini to ar virknes soli - 2 vai 3.",
             "Ar iegūto skaitli dari to pašu vēlreiz.",
             "Lai ietu atpakaļ, katru skaitli dali ar to pašu soli.",
         ],
         pieze="Salīdzini divas virknes: 1, 4, 7, 10, 13 aug pa 3, bet "
               "1, 3, 9, 27, 81 aug *reizes* 3. Sākums ir vienāds, beigas - "
               "pavisam citas."),

    Slidnis("Divkāršošanās piecos soļos",
            soli=[
                {"v": "2", "teksts": "Sākums.", "josla": 6},
                {"v": "4", "teksts": "Divreiz vairāk.", "josla": 12},
                {"v": "8", "teksts": "Vēl divreiz.", "josla": 25},
                {"v": "16", "teksts": "Un vēl.", "josla": 50},
                {"v": "32", "teksts": "Pieci soļi - un skaitlis jau ir 32.",
                 "josla": 100},
            ],
            ievads="Katrs solis reizina ar 2. Skaties, cik ātri aug josla."),

    Paraugs("Kāds skaitlis ir nākamais?",
            uzd="Virkne: 2, 6, 18, ... Kāds skaitlis ir nākamais?",
            soli=[
                ("6 : 2 = 3",
                 "Vispirms noskaidro, kā no pirmā iegūst otro."),
                ("18 : 6 = 3",
                 "Pārbaude: tas pats solis der arī tālāk."),
                ("18 · 3 = 54",
                 "Nākamo iegūst, reizinot ar 3."),
            ],
            atbilde="54"),

    Ievadi("Turpini virkni", [
        {"jaut": "1, 2, 4, 8, ... Kāds ir nākamais skaitlis?",
         "atb": ["16"], "padoms": "Katrs nākamais ir divreiz lielāks."},
        {"jaut": "3, 9, 27, ... Kāds ir nākamais skaitlis?",
         "atb": ["81"], "padoms": "Reizini ar 3."},
        {"jaut": "80, 40, 20, ... Kāds ir nākamais skaitlis?",
         "atb": ["10"], "padoms": "Katrs nākamais ir divreiz mazāks."},
        {"jaut": "2, 6, 18, 54, ... Kāds ir nākamais skaitlis?",
         "atb": ["162"], "padoms": "54 · 3."},
        {"jaut": "5, 10, 20, 40, ... Kāds ir nākamais skaitlis?",
         "atb": ["80"], "padoms": "40 · 2."},
        {"jaut": "243, 81, 27, ... Kāds ir nākamais skaitlis?",
         "atb": ["9"], "padoms": "27 : 3."},
    ], pamats=4),

    Zimejums("Divas virknes blakus",
             kolonnas([("pa 3", 13), ("reizes 3", 81)]),
             paskaidro="Abas sākās ar 1 un gāja piecus soļus - bet viena "
                       "nonāca pie 13, otra pie 81.",
             ievads="Kreisā virkne aug pa 3, labā - reizes 3."),

    Varianti("Kāds ir virknes solis?", [
        {"jaut": "4, 12, 36, 108 - kāds ir solis?",
         "opcijas": ["Reizina ar 3", "Pieskaita 8", "Reizina ar 2",
                     "Pieskaita 4"],
         "pareizi": 0, "padoms": "12 : 4 = 3."},
        {"jaut": "64, 32, 16, 8 - kāds ir solis?",
         "opcijas": ["Dala ar 2", "Atņem 32", "Dala ar 4", "Atņem 8"],
         "pareizi": 0, "padoms": "64 : 32 = 2."},
        {"jaut": "Kura virkne aug ātrāk?",
         "opcijas": ["1, 3, 9, 27", "1, 4, 7, 10", "1, 2, 3, 4",
                     "1, 6, 11, 16"],
         "pareizi": 0, "padoms": "Tikai pirmā reizina, pārējās saskaita."},
        {"jaut": "Virknē 3, 6, 12, 24 trūkst nākamā. Kāds tas ir?",
         "opcijas": ["48", "36", "30", "27"],
         "pareizi": 0, "padoms": "24 · 2."},
    ], pamats=4),

    Pasaule("Cik ātri izplatās ziņa?",
            Ievadi("", [
                {"jaut": "Pirmais bērns pastāsta 2 draugiem, katrs no tiem "
                         "vēl 2. Cik bērnu zina otrajā solī?",
                 "atb": ["4"], "padoms": "2 · 2."},
                {"jaut": "Cik bērnu uzzinās trešajā solī?",
                 "atb": ["8"], "padoms": "4 · 2."},
                {"jaut": "Cik bērnu uzzinās ceturtajā solī?",
                 "atb": ["16"], "padoms": "8 · 2."},
                {"jaut": "Cik bērnu uzzinās piektajā solī?",
                 "atb": ["32"], "padoms": "16 · 2."},
            ]),
            pavediens="dati",
            konteksts="Ziņa internetā izplatās tieši tā: katrs, kas to "
                      "redzēja, parāda to vēl dažiem.",
            kapec="Tāpēc daži video dažās dienās sasniedz miljonu cilvēku."),

    Kopsavilkums([
        "Veidoju virknes, kurās katrs nākamais ir 2 vai 3 reizes lielāks.",
        "Nosaku virknes soli, dalot vienu locekli ar iepriekšējo.",
        "Turpinu virkni uz priekšu un atpakaļ.",
        "Zinu, ka reizināšanas virkne aug daudz ātrāk nekā saskaitīšanas.",
    ]),

    Majas([
        "Uzraksti virkni, kas sākas ar 1 un katru reizi divkāršojas, līdz "
        "skaitlis pārsniedz 100.",
        "Salīdzini to ar virkni, kas aug pa 10.",
        "Saloc lapu uz pusēm cik reižu vien vari un saskaiti slāņus.",
    ]),
]
