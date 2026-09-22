# -*- coding: utf-8 -*-
"""6. klase, 33. stunda: «Kā reizināt jauktus skaitļus?»

Pēdējais mikrotemats tematā. Jauni likumi te nav - ir viens obligāts solis:
jaukto skaitli vispirms pārveido par neīstu daļu. Stunda parāda, kas notiek,
ja to neizdara, jo tieši šī kļūda ir visizplatītākā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, kvadrats)

TEMA = "Kā reizināt jauktus skaitļus?"

MERKIS = ("Iemācīsimies sareizināt jauktus skaitļus, pārveidojot tos par "
          "neīstām daļām.")

SATURS = [
    Sakums("Kāpēc 1{1|2} · 2{1|2} nav 2{1|4}?",
           zimejums=kvadrats(6, 5, 3, 5, paraksts="15 no 30"),
           paraksts="Pareizā atbilde ir 3{3|4}. Veselās un daļas nedrīkst "
                    "reizināt atsevišķi.",
           fakti=["Jauktais skaitlis ir summa: 1{1|2} = 1 + {1|2}.",
                  "Summu reizinot, katra daļa reizinās ar katru.",
                  "Tāpēc vienkāršāk ir pārveidot par neīstu daļu."]),

    Doma("Vispirms neīsta daļa, tikai tad reizināšana",
         "Jauktu skaitli reizinot, to vienmēr pārveido par neīstu daļu - "
         "tikai tad der parastais reizināšanas likums.",
         soli=[
             "Reizini veselo daļu ar saucēju un pieskaiti skaitītāju.",
             "Pieraksti rezultātu kā neīstu daļu ar to pašu saucēju.",
             "Sareizini abas neīstās daļas, saīsinot pirms reizināšanas.",
             "Atdali veselās daļas rezultātā.",
             "Pārbaudi, vai atbilde ir ticama pēc lieluma.",
         ],
         pieze="2{1|3} = {2 · 3 + 1|3} = {7|3}. Šis viens solis izlīdzina "
               "visu: tālāk viss ir tas pats, ko iepriekšējās stundās."),

    Paraugs("Sareizini divus jauktus skaitļus",
            uzd="Cik ir 1{1|2} · 2{1|2}?",
            soli=[
                ("1{1|2} = {3|2}; 2{1|2} = {5|2}",
                 "Abi jauktie skaitļi kļūst par neīstām daļām."),
                ("{3|2} · {5|2} = {15|4}",
                 "Parastā reizināšana."),
                ("{15|4} = 3{3|4}",
                 "15 : 4 = 3 un atlikums 3."),
                ("Novērtējums: nedaudz vairāk par 1,5 · 2,5",
                 "Atbilde ir ticama."),
            ],
            atbilde="3{3|4}"),

    Ievadi("Reizini jauktus skaitļus", [
        {"jaut": "Pārveido 2{3|4} par neīstu daļu. Atbildi raksti kā a/b.",
         "atb": ["11/4"], "padoms": "2 · 4 + 3."},
        {"jaut": "Cik ir 1{1|3} · 3? Atbildi raksti kā vesels skaitlis.",
         "atb": ["4"], "padoms": "{4|3} · 3."},
        {"jaut": "Cik ir 2{1|2} · 1{1|5}?",
         "atb": ["3"], "padoms": "{5|2} · {6|5}."},
        {"jaut": "Cik ir 1{2|3} · 1{1|5}?",
         "atb": ["2"], "padoms": "{5|3} · {6|5}."},
        {"jaut": "Cik ir 2{1|4} · 1{1|3}?",
         "atb": ["3"], "padoms": "{9|4} · {4|3}."},
        {"jaut": "Cik ir 3{1|2} · 2? Atbildi raksti kā vesels skaitlis.",
         "atb": ["7"], "padoms": "{7|2} · 2."},
    ], pamats=4,
        ievads="Pirmais solis vienmēr viens un tas pats - neīsta daļa."),

    Varianti("Kāpēc tā nedrīkst?", [
        {"jaut": "Skolēns rēķina 1{1|2} · 2{1|2} = 2{1|4}. Ko viņš izdarīja?",
         "opcijas": ["Sareizināja veselās un daļas atsevišķi",
                     "Aizmirsa saīsināt", "Saskaitīja", "Viss pareizi"],
         "pareizi": 0,
         "padoms": "Summas reizinājums tā nestrādā."},
        {"jaut": "Kā 3{2|5} pieraksta kā neīstu daļu?",
         "opcijas": ["{17|5}", "{32|5}", "{11|5}", "{6|5}"],
         "pareizi": 0,
         "padoms": "3 · 5 + 2."},
        {"jaut": "Kad rezultātu pārveido atpakaļ par jauktu skaitli?",
         "opcijas": ["Kad tas ir neīsta daļa",
                     "Vienmēr", "Nekad", "Kad saucējs ir pāra skaitlis"],
         "pareizi": 0,
         "padoms": "Atbildi raksta vienkāršākajā formā."},
        {"jaut": "1{1|2} · 2 ir vienāds ar...",
         "opcijas": ["3", "2{1|2}", "2{2|4}", "1{2|2}"],
         "pareizi": 0,
         "padoms": "{3|2} · 2 = 3."},
    ], pamats=4),

    Pasaule("Cik materiāla vajag kastei?",
            Ievadi("", [
                {"jaut": "Dēlis ir 2{1|2} m garš, vajag 4 tādus. Cik metru "
                         "kopā?",
                 "atb": ["10"], "padoms": "{5|2} · 4."},
                {"jaut": "Plātnes laukums: 1{1|2} m reiz 2{2|3} m. Cik "
                         "kvadrātmetru?",
                 "atb": ["4"], "padoms": "{3|2} · {8|3}."},
                {"jaut": "Lentes gabals ir 1{1|4} m, vajag 8 gabalus. Cik "
                         "metru kopā?",
                 "atb": ["10"], "padoms": "{5|4} · 8."},
                {"jaut": "Krāsa: 1{1|3} l uz vienu kārtu, vajag 3 kārtas. "
                         "Cik litru?",
                 "atb": ["4"], "padoms": "{4|3} · 3."},
            ]),
            pavediens="maja",
            konteksts="Veikalā dēļus mēra pusmetros, tāpēc jauktie skaitļi "
                      "ir tikpat bieži kā veselie.",
            kapec="Viens pārveidošanas solis - un tālāk viss ir zināms."),

    Kopsavilkums([
        "Pārveidoju jauktu skaitli par neīstu daļu.",
        "Sareizinu jauktus skaitļus pēc parastā likuma.",
        "Atdalu veselās daļas rezultātā.",
        "Zinu, kāpēc veselās un daļas nedrīkst reizināt atsevišķi.",
    ]),

    Majas([
        "Izrēķini 2{1|4} · 1{3|5}.",
        "Pārbaudi, vai 1{1|2} · 1{1|2} ir vairāk vai mazāk par 2.",
        "Izmēri kādu mājas priekšmetu ar puscentimetra precizitāti un "
        "izrēķini divu tādu kopgarumu.",
    ]),
]
