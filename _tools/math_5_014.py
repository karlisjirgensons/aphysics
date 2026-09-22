# -*- coding: utf-8 -*-
"""5. klase, 14. stunda: «Kā noapaļo līdz simtiem un tūkstošiem?»

Mikrotemata galvenā stunda: no «kurš apaļais skaitlis ir tuvāk» uz kārtulu.
Kārtulu neizdomā no gaisa - to nolasa no skaitļu taisnes, kas zīmēta jau
5. stundā, tāpēc arī puses gadījums (5) ir redzams, nevis iekalts.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, taisne)

TEMA = "Kā noapaļo līdz simtiem un tūkstošiem?"

MERKIS = ("Iemācīsimies noapaļot naturālus skaitļus līdz noteiktai šķirai un "
          "skaidrot, kāpēc kārtula ir tieši tāda.")

SATURS = [
    Sakums("Kurš tūkstotis ir tuvāk?",
           zimejums=taisne(3000, 4000, 500, [(3470, "3 470")]),
           paraksts="3 470 atrodas starp 3 000 un 4 000 - bet jau pāri "
                    "vidum.",
           fakti=["Noapaļot nozīmē izvēlēties tuvāko apaļo skaitli.",
                  "Uz taisnes uzreiz redz, kurš no diviem ir tuvāk."]),

    Doma("Izšķir viens cipars - nākamais aiz šķiras",
         "Skaties uz ciparu tieši aiz tās šķiras, līdz kurai noapaļo.",
         soli=[
             "Atrodi šķiras ciparu, līdz kurai jānoapaļo.",
             "Paskaties uz nākamo ciparu pa labi.",
             "Ja tas ir 0, 1, 2, 3 vai 4 - šķiras ciparu atstāj.",
             "Ja tas ir 5, 6, 7, 8 vai 9 - šķiras ciparam pieskaita 1.",
             "Visus ciparus pa labi aizstāj ar nullēm.",
         ],
         pieze="Kārtula nav izdomāta: cipari no 5 līdz 9 nozīmē, ka skaitlis "
               "ir pārkāpis vidu, tāpēc tuvāks ir nākamais apaļais skaitlis."),

    Zimejums("Tuvāks skats uz to pašu skaitli",
             taisne(3400, 3500, 50, [(3470, "3 470")]),
             paskaidro="Vidus ir 3 450. Skaitlis 3 470 ir pa labi no vidus, "
                       "tāpēc līdz simtiem tas noapaļojas uz 3 500.",
             ievads="Pietuvinām to pašu taisni - tagad no 3 400 līdz 3 500."),

    Paraugs("Noapaļo 3 470 līdz tūkstošiem",
            uzd="Kāds skaitlis sanāk, noapaļojot 3 470 līdz tūkstošiem?",
            soli=[
                ("Tūkstošu cipars ir 3",
                 "Skaitlī 3 470 tūkstoši ir pirmais cipars."),
                ("Nākamais cipars pa labi ir 4",
                 "Tas ir simtu cipars."),
                ("4 ir mazāks par 5, tāpēc tūkstošus neaiztiek",
                 "Skaitlis vidu vēl nav pārkāpis."),
                ("Pārējos ciparus aizstāj ar nullēm: 3 000",
                 "Sanāk apaļš skaitlis."),
            ],
            atbilde="3 470 ≈ 3 000"),

    Ievadi("Noapaļo līdz prasītajai šķirai", [
        {"jaut": "Noapaļo 4 812 līdz tūkstošiem.", "atb": ["5000"],
         "padoms": "Nākamais cipars aiz tūkstošiem ir 8."},
        {"jaut": "Noapaļo 3 470 līdz simtiem.", "atb": ["3500"],
         "padoms": "Aiz simtiem ir 7."},
        {"jaut": "Noapaļo 2 149 līdz simtiem.", "atb": ["2100"],
         "padoms": "Aiz simtiem ir 4 - simtus neaiztiek."},
        {"jaut": "Noapaļo 6 500 līdz tūkstošiem.", "atb": ["7000"],
         "padoms": "Tieši 5 - noapaļo uz augšu."},
        {"jaut": "Noapaļo 18 964 līdz tūkstošiem.", "atb": ["19000"],
         "padoms": "Aiz tūkstošiem ir 9."},
        {"jaut": "Noapaļo 749 līdz simtiem.", "atb": ["700"],
         "padoms": "Aiz simtiem ir 4, nevis 5."},
        {"jaut": "Noapaļo 96 305 līdz tūkstošiem.", "atb": ["96000"],
         "padoms": "Aiz tūkstošiem ir 3."},
        {"jaut": "Noapaļo 9 951 līdz simtiem.", "atb": ["10000"],
         "padoms": "Simti pāriet tūkstošos: 99 simti + 1 = 100 simti."},
    ], pamats=4,
        ievads="Uzraksti tikai gala skaitli."),

    Varianti("Kāpēc kārtula ir tāda?", [
        {"jaut": "Noapaļojot līdz simtiem, uz kuru ciparu skatās?",
         "opcijas": ["Uz desmitu ciparu", "Uz simtu ciparu",
                     "Uz pirmo ciparu", "Uz pēdējo ciparu"],
         "pareizi": 0,
         "padoms": "Uz to, kas ir tieši pa labi no šķiras."},
        {"jaut": "Kāpēc 5 noapaļo uz augšu?",
         "opcijas": ["Tā vienojušies, jo 5 ir tieši vidū",
                     "Jo 5 ir nepāra skaitlis",
                     "Jo 5 ir tuvāk nākamajam simtam",
                     "Jo pieci ir vairāk nekā seši"],
         "pareizi": 0,
         "padoms": "Uz taisnes 250 ir vienādā attālumā no 200 un 300."},
        {"jaut": "Kurš skaitlis, noapaļots līdz simtiem, dod 500?",
         "opcijas": ["463", "552", "550", "449"],
         "pareizi": 0,
         "padoms": "Pārbaudi katru: uz kuru simtu tas noapaļojas?"},
        {"jaut": "Noapaļo 9 951 līdz simtiem. Kāpēc sanāk 10 000?",
         "opcijas": ["Simti pāriet tūkstošos",
                     "Jo skaitlis ir nepāra",
                     "Jo simtu nedrīkst būt vairāk par 99",
                     "Jo tā ir kļūda"],
         "pareizi": 0,
         "padoms": "99 simtiem pieskaita vienu simtu."},
    ], pamats=4),

    Pasaule("Cik dzīvnieku dzīvo mežā?",
            Ievadi("", [
                {"jaut": "Mežā saskaitīti 1 462 stirnas. Noapaļo līdz "
                         "simtiem.",
                 "atb": ["1500"], "padoms": "Aiz simtiem ir 6."},
                {"jaut": "Aļņu ir 872. Noapaļo līdz simtiem.",
                 "atb": ["900"], "padoms": "Aiz simtiem ir 7."},
                {"jaut": "Purva platība ir 4 350 ha. Noapaļo līdz "
                         "tūkstošiem.",
                 "atb": ["4000"], "padoms": "Aiz tūkstošiem ir 3."},
                {"jaut": "Ligzdojošo dzērvju ir 12 604. Noapaļo līdz "
                         "tūkstošiem.",
                 "atb": ["13000"], "padoms": "Aiz tūkstošiem ir 6."},
            ]),
            pavediens="daba",
            konteksts="Dzīvnieku uzskaitē skaitli vienmēr pieraksta "
                      "noapaļotu - nākamajā dienā tas jau ir cits.",
            kapec="Noapaļots skaitlis parāda, cik precīzi vispār var zināt."),

    Kopsavilkums([
        "Noapaļoju naturālu skaitli līdz simtiem un tūkstošiem.",
        "Zinu, ka izšķir cipars tieši aiz noapaļojamās šķiras.",
        "Skaidroju kārtulu ar skaitļu taisni: kurš apaļais skaitlis ir tuvāk.",
        "Lietoju zīmi ≈, kad skaitlis ir noapaļots.",
    ]),

    Majas([
        "Uzraksti piecus skaitļus no čeka vai ziņām un noapaļo katru līdz "
        "simtiem.",
        "Uzzīmē skaitļu taisni vienam no tiem un parādi, kāpēc sanāk tieši "
        "tas apaļais skaitlis.",
        "Atrodi skaitli, kas līdz simtiem un līdz tūkstošiem noapaļojas "
        "dažādi.",
    ]),
]
