# -*- coding: utf-8 -*-
"""4. klase, 1. stunda: «Ko es protu no 3. klases?»

Gada pirmā stunda ir diagnostika, bet ne kontroldarbs: skolēns pats redz,
ko trīsciparu skaitļos jau proti, un atzīmē, kas vēl klibo. Viss 4.1.
temats aug no šejienes - četrciparu skaitlis ir tas pats trīsciparu
skaitlis ar vēl vienu šķiru priekšā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Ko es protu no 3. klases?"

MERKIS = ("Atcerēsimies, kā uzbūvēts trīsciparu skaitlis, un pārbaudīsim, "
          "ko jau protam, lai zinātu, ko šogad trenēt.")

SATURS = [
    Sakums("Cik augsts ir Rīgas televīzijas tornis?",
           zimejums=restis([["simti", "desmiti", "vieni"],
                            [3, 6, 8]],
                           "368 metri"),
           paraksts="Trīs cipari - trīs šķiras: 3 simti, 6 desmiti, 8 vieni.",
           fakti=["Rīgas TV tornis ir augstākā būve Baltijā - 368 m.",
                  "Tas ir gandrīz deviņi Brīvības pieminekļi viens uz "
                  "otra.",
                  "Visu šo gadu mēs rēķināsim ar skaitļiem līdz 10 000."]),

    Doma("Katram ciparam ir sava vieta",
         "Trīsciparu skaitlī pirmais cipars skaita simtus, otrais - "
         "desmitus, trešais - vienus.",
         soli=[
             "Nosauc katru ciparu un tā šķiru: 368 - 3 simti, 6 desmiti, "
             "8 vieni.",
             "Uzraksti skaitli kā summu: 368 = 300 + 60 + 8.",
             "Ja kādas šķiras nav, tās vietā raksta 0: 305 = 300 + 5.",
             "Salīdzinot sāk ar lielāko šķiru - ar simtiem.",
         ],
         pieze="Nulle nav «nekas» - tā notur vietu. Bez tās 305 kļūtu par "
               "35."),

    Paraugs("Kas ir skaitlī 407?",
            uzd="Nosaki skaitļa 407 sastāvu un uzraksti to kā summu.",
            soli=[
                ("4 simti, 0 desmiti, 7 vieni",
                 "Katram ciparam nosaka tā šķiru."),
                ("407 = 400 + 7",
                 "Desmitu nav, tāpēc summā tie nav jāraksta."),
                ("407 = 40 desmiti + 7 vieni",
                 "To pašu var pateikt arī desmitos."),
            ],
            atbilde="407 = 400 + 7"),

    Ievadi("Salasi skaitli no šķirām", [
        {"jaut": "3 simti, 5 desmiti un 2 vieni. Kāds tas ir skaitlis?",
         "atb": ["352"], "padoms": "300 + 50 + 2."},
        {"jaut": "7 simti un 9 vieni. Kāds tas ir skaitlis?",
         "atb": ["709"], "padoms": "Desmitu vietā raksta 0."},
        {"jaut": "Cik desmitu ir skaitlī 460 pavisam?",
         "atb": ["46"], "padoms": "4 simti ir 40 desmiti, plus vēl 6."},
        {"jaut": "600 + 40 + 1 = ?", "atb": ["641"],
         "padoms": "Katrs saskaitāmais aizņem savu šķiru."},
        {"jaut": "Kāds ir lielākais trīsciparu skaitlis?",
         "atb": ["999"], "padoms": "Visās šķirās lielākais cipars."},
        {"jaut": "Kāds ir mazākais trīsciparu skaitlis?",
         "atb": ["100"], "padoms": "Simtu vietā nevar būt nulle."},
    ], pamats=4,
        ievads="Ieraksti skaitli un spied «Pārbaudīt»."),

    Zimejums("Mana gada karte",
             restis([["ko pārbaudām", "3. klasē", "4. klasē"],
                     ["skaitļi līdz", "1000", "10 000"],
                     ["saskaitīšana", "līdz 1000", "līdz 10 000"],
                     ["reizināšana", "tabula", "ar divciparu"],
                     ["daļas", "puse, ceturtdaļa", "salīdzina, saskaita"]],
                    "no kurienes nāku un kurp eju"),
             paskaidro="Viss, ko šogad mācīsies, ir tas pats, ko jau proti, "
                       "tikai ar lielākiem skaitļiem.",
             ievads="Šī tabula parāda, cik tālu esi ticis un kur ceļš ved."),

    Varianti("Pārbaudi sevi", [
        {"jaut": "Kurā šķirā ir cipars 5 skaitlī 356?",
         "opcijas": ["desmitu", "vienu", "simtu", "tūkstošu"],
         "pareizi": 0, "padoms": "Skaiti no labās: vieni, desmiti, simti."},
        {"jaut": "Kurš skaitlis ir lielāks: 409 vai 490?",
         "opcijas": ["490", "409", "abi vienādi", "nevar pateikt"],
         "pareizi": 0, "padoms": "Simti vienādi - salīdzini desmitus."},
        {"jaut": "Kura summa ir skaitlis 830?",
         "opcijas": ["800 + 30", "800 + 3", "80 + 30", "8 + 3 + 0"],
         "pareizi": 0, "padoms": "8 simti un 3 desmiti."},
        {"jaut": "Kas notiek ar 35, ja starpā ieliek nulli - 305?",
         "opcijas": ["Tas kļūst gandrīz desmit reizes lielāks",
                     "Tas nemainās", "Tas kļūst mazāks",
                     "Tas kļūst par 1 lielāks"],
         "pareizi": 0, "padoms": "3 no desmitiem pārceļas uz simtiem."},
    ], pamats=4),

    Pasaule("Cik augsti ir Latvijas torņi?",
            Ievadi("", [
                {"jaut": "Rīgas TV tornis ir 368 m augsts. Cik simtu metru "
                         "tas ir, noapaļojot?",
                 "atb": ["4"], "padoms": "368 ir tuvāk 400 nekā 300."},
                {"jaut": "Sv. Pētera baznīcas tornis ir 123 m. Par cik "
                         "metriem TV tornis ir augstāks?",
                 "atb": ["245"], "padoms": "368 − 123."},
                {"jaut": "Gaiziņkalns ir 312 m virs jūras līmeņa. Cik "
                         "desmitu metru tas ir pavisam?",
                 "atb": ["31"], "padoms": "3 simti ir 30 desmiti, plus 1."},
                {"jaut": "Brīvības piemineklis ir 42 m. Cik metru ir trīs "
                         "šādi pieminekļi viens uz otra?",
                 "atb": ["126"], "padoms": "42 + 42 + 42."},
            ]),
            pavediens="celojums",
            konteksts="Ceļojot pa Latviju, augstumi un attālumi ir "
                      "trīsciparu skaitļi - un tos tu jau proti.",
            kapec="Kas lasa skaitli pa šķirām, tas nesajauc 312 m ar "
                  "31 m."),

    Kopsavilkums([
        "Nosaku trīsciparu skaitļa simtus, desmitus un vienus.",
        "Uzrakstu skaitli kā šķiru summu.",
        "Zinu, kāpēc nulle skaitlī notur vietu.",
        "Zinu, ko šogad trenēšu.",
    ]),

    Majas([
        "Atrodi mājās trīs trīsciparu skaitļus (uz iepakojuma, grāmatā) un "
        "uzraksti katru kā summu.",
        "Pajautā mājiniekiem, cik metru augsta ir jūsu māja, un salīdzini "
        "ar TV torni.",
        "Uzraksti savas trīs grūtākās lietas no 3. klases matemātikas.",
    ], ievads="Skaitļi ir visur - pamēģini tos izlasīt pa šķirām."),
]
