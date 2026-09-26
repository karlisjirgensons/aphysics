# -*- coding: utf-8 -*-
"""4. klase, 7. stunda: «Kas ir skaitļu šķira?»

Šķiras ir kāpnes, kurās katrs nākamais pakāpiens ir desmit reizes lielāks.
10 vieni ir desmits, 10 desmiti - simts, 10 simti - tūkstotis. Tas ir viss
decimālās sistēmas noslēpums, un uz tā balstās rakstiskā saskaitīšana.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, kolonnas)

TEMA = "Kas ir skaitļu šķira?"

MERKIS = ("Nosauksim šķiras - vienus, desmitus, simtus, tūkstošus - un "
          "noteiksim četrciparu skaitļa decimālo sastāvu.")

SATURS = [
    Sakums("Cik monētu ir tūkstotī?",
           zimejums=kolonnas([("1", 1), ("10", 10), ("100", 100),
                              ("1000", 1000)]),
           paraksts="Katrs stabiņš ir desmit reizes augstāks nekā iepriekšējais.",
           fakti=["10 vieni = 1 desmits.",
                  "10 desmiti = 1 simts.",
                  "10 simti = 1 tūkstotis."]),

    Doma("Katra šķira ir desmit reizes lielāka par iepriekšējo",
         "Skaitļa decimālais sastāvs pasaka, cik katrā šķirā ir tūkstošu, "
         "simtu, desmitu un vienu.",
         soli=[
             "Pēdējais cipars ir vieni.",
             "Otrais no beigām - desmiti.",
             "Trešais no beigām - simti.",
             "Ceturtais no beigām - tūkstoši.",
         ],
         pieze="Skaitlī 4735 ir 4 tūkstoši, 7 simti, 3 desmiti, 5 vieni. "
               "Bet pavisam tajā ir 47 simti un 473 desmiti."),

    Paraugs("Cik simtu ir skaitlī 3820?",
            uzd="Cik simtu pavisam ir skaitlī 3820?",
            soli=[
                ("3 tūkstoši = 30 simti",
                 "Katrā tūkstotī ir 10 simtu."),
                ("30 simti + 8 simti = 38 simti", None),
                ("20 ir mazāk par simtu",
                 "Desmiti un vieni vēl nav vesels simts."),
            ],
            atbilde="38 simti"),

    Slidnis("Kāpnes: 1, 10, 100, 1000",
            soli=[
                {"v": "1", "teksts": "Viens vienums.", "josla": 1},
                {"v": "10 = 10 · 1", "teksts": "Desmit vieni - desmits.",
                 "josla": 3},
                {"v": "100 = 10 · 10", "teksts": "Desmit desmiti - simts.",
                 "josla": 10},
                {"v": "1000 = 10 · 100",
                 "teksts": "Desmit simti - tūkstotis.", "josla": 100},
            ],
            ievads="Katrs pakāpiens ir desmit reizes lielāks."),

    Ievadi("Nosaki sastāvu", [
        {"jaut": "Cik tūkstošu ir skaitlī 6348?", "atb": ["6"],
         "padoms": "Pirmais cipars."},
        {"jaut": "Kurš cipars ir desmitu šķirā skaitlī 5172?",
         "atb": ["7"], "padoms": "Otrais no beigām."},
        {"jaut": "Cik desmitu pavisam ir skaitlī 2450?",
         "atb": ["245"], "padoms": "Nosvītro pēdējo ciparu."},
        {"jaut": "Cik simtu pavisam ir skaitlī 7900?",
         "atb": ["79"], "padoms": "7 tūkstoši = 70 simti."},
        {"jaut": "Kāds skaitlis ir 5 tūkstoši, 0 simti, 4 desmiti, 9 vieni?",
         "atb": ["5049"], "padoms": "5 | 0 | 4 | 9."},
        {"jaut": "Cik vienu ir 3 tūkstošos?", "atb": ["3000"],
         "padoms": "Katrā tūkstotī ir 1000 vienu."},
    ], pamats=4),

    Varianti("Kura šķira?", [
        {"jaut": "Kādā šķirā ir cipars 8 skaitlī 8123?",
         "opcijas": ["tūkstošu", "simtu", "desmitu", "vienu"],
         "pareizi": 0, "padoms": "Tas ir pirmais no četriem."},
        {"jaut": "Cik vērts ir cipars 6 skaitlī 2635?",
         "opcijas": ["600", "6", "60", "6000"], "pareizi": 0,
         "padoms": "Tas ir simtu šķirā."},
        {"jaut": "Kurš skaitlis sastāv no 7 T, 2 D un 3 V?",
         "opcijas": ["7023", "7230", "723", "7203"], "pareizi": 0,
         "padoms": "Simtu nav - tur 0."},
        {"jaut": "Cik desmitu ir vienā tūkstotī?",
         "opcijas": ["100", "10", "1000", "1"], "pareizi": 0,
         "padoms": "1000 : 10."},
    ], pamats=4),

    Pasaule("Cik kastu ar zīmuļiem?",
            Ievadi("", [
                {"jaut": "Rūpnīca saražoja 4725 zīmuļus. Zīmuļus pako pa 10 "
                         "kastītē. Cik pilnu kastīšu?",
                 "atb": ["472"], "padoms": "Cik desmitu ir 4725?"},
                {"jaut": "Cik zīmuļu paliek ārpus kastītēm?",
                 "atb": ["5"], "padoms": "Vienu šķira."},
                {"jaut": "Kastītes liek lielās kastēs pa 10. Cik lielo kastu "
                         "būs pilnas?",
                 "atb": ["47"], "padoms": "Cik simtu ir 4725?"},
                {"jaut": "Cik zīmuļu ir vienā lielajā kastē?",
                 "atb": ["100"], "padoms": "10 kastītes pa 10."},
            ]),
            pavediens="tehnika",
            konteksts="Rūpnīcās preces pako pa 10, 100 un 1000 - tieši "
                      "šķiru dēļ tās ir viegli saskaitīt.",
            kapec="Šķiras ļauj uzreiz redzēt, cik pilnu iepakojumu sanāk."),

    Kopsavilkums([
        "Nosaucu šķiras: vieni, desmiti, simti, tūkstoši.",
        "Nosaku, cik vērts ir cipars savā šķirā.",
        "Zinu, cik simtu vai desmitu pavisam ir skaitlī.",
        "Zinu, ka katra šķira ir 10 reizes lielāka par iepriekšējo.",
    ]),

    Majas([
        "Paskaties uz naudu: kuras monētas un banknotes ir 1, 10 un 100 "
        "reizes lielākas par 1 €?",
        "Uzraksti savu mīļāko četrciparu skaitli šķiru tabulā.",
        "Izrēķini, cik desmitu pavisam ir skaitlī 2026.",
    ]),
]
