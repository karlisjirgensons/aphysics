# -*- coding: utf-8 -*-
"""6. klase, 141. stunda: «Kā saskaitīt negatīvas daļas?»

Pēdējais mikrotemats tematā. Jaunu likumu te nav: kopsaucējs ir zināms no
5. klases, zīmju likums - no šī temata. Jaunais ir tikai tas, ka abi
jālieto vienā uzdevumā, un tieši tā secība ir stundas mācība.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, taisne)

TEMA = "Kā saskaitīt negatīvas daļas?"

MERKIS = ("Saskaitīsim un atņemsim pozitīvus un negatīvus daļskaitļus, kas "
          "doti kā parastās daļas.")

SATURS = [
    Sakums("Vispirms kopsaucējs, tad zīmes",
           zimejums=taisne(-1, 1, 1, [(-0.25, "−1/4"), (0.5, "1/2")]),
           paraksts="−{1|4} un {1|2}: kopsaucējs 4, un tad rēķins ir tāds "
                    "pats kā veseliem skaitļiem.",
           fakti=["Kopsaucējs jāatrod pirms zīmju likuma lietošanas.",
                  "Mīnuss attiecas uz visu daļu, ne tikai uz skaitītāju.",
                  "Pēc kopsaucēja atrašanas rēķina tikai ar skaitītājiem."]),

    Doma("Kopsaucējs, tad skaitītāji ar zīmēm",
         "Daļskaitļus ar zīmēm saskaita divos soļos: vispirms tos pārveido "
         "par daļām ar kopsaucēju, tad skaitītājus saskaita pēc zīmju "
         "likuma.",
         soli=[
             "Atrodi daļu kopsaucēju.",
             "Paplašini abas daļas līdz tam.",
             "Saskaiti skaitītājus, ievērojot zīmes.",
             "Saucēju atstāj nemainīgu.",
             "Saīsini rezultātu un atdali veselās daļas.",
         ],
         pieze="Atņemšanu vispirms pārraksta par saskaitīšanu: "
               "−{1|2} − {1|4} = −{1|2} + (−{1|4}). Tad abās daļās ir tikai "
               "viena darbība."),

    Paraugs("Divas daļas ar zīmēm",
            uzd="Cik ir −{1|4} + {1|2}?",
            soli=[
                ("Kopsaucējs ir 4",
                 "2 · 2 = 4."),
                ("−{1|4} + {2|4}",
                 "Otro daļu paplašina."),
                ("Skaitītāji: −1 + 2 = 1",
                 "Zīmes atšķiras - moduļus atņem."),
                ("= {1|4}",
                 "Saucējs paliek 4."),
            ],
            atbilde="{1|4}"),

    Ievadi("Saskaiti daļas ar zīmēm", [
        {"jaut": "Cik ir −{1|4} + {1|2}? Atbildi raksti kā a/b.",
         "atb": ["1/4"], "padoms": "−1 + 2 ceturtdaļās."},
        {"jaut": "Cik ir −{1|2} + {1|4}? Atbildi raksti kā a/b.",
         "atb": ["-1/4", "−1/4"], "padoms": "−2 + 1 ceturtdaļās."},
        {"jaut": "Cik ir −{1|3} + (−{1|3})? Atbildi raksti kā a/b.",
         "atb": ["-2/3", "−2/3"], "padoms": "Vienādas zīmes."},
        {"jaut": "Cik ir {3|5} − {4|5}? Atbildi raksti kā a/b.",
         "atb": ["-1/5", "−1/5"], "padoms": "3 − 4 piektdaļās."},
        {"jaut": "Cik ir −{2|3} + {2|3}?",
         "atb": ["0"], "padoms": "Pretējas daļas."},
        {"jaut": "Cik ir −{1|6} − {1|3}? Atbildi raksti kā a/b.",
         "atb": ["-1/2", "−1/2", "-3/6", "−3/6"],
         "padoms": "Kopsaucējs 6: −1 − 2."},
    ], pamats=4,
        ievads="Vispirms kopsaucējs, tikai tad zīmes."),

    Varianti("Kāda būs zīme?", [
        {"jaut": "−{1|2} + {1|4}. Rezultāta zīme ir...",
         "opcijas": ["mīnuss", "pluss", "nav zīmes", "nevar zināt"],
         "pareizi": 0,
         "padoms": "{1|2} ir lielāks par {1|4}."},
        {"jaut": "Kāds ir daļu {1|4} un {1|3} kopsaucējs?",
         "opcijas": ["12", "7", "4", "3"],
         "pareizi": 0,
         "padoms": "4 · 3."},
        {"jaut": "Mīnuss daļas priekšā attiecas uz...",
         "opcijas": ["visu daļu", "tikai skaitītāju",
                     "tikai saucēju", "neko"],
         "pareizi": 0,
         "padoms": "−{1|2} ir puse pa kreisi no nulles."},
        {"jaut": "−{3|4} − {1|4} ir vienāds ar...",
         "opcijas": ["−1", "−{1|2}", "{1|2}", "−{2|4}"],
         "pareizi": 0,
         "padoms": "−3 − 1 ceturtdaļās."},
    ], pamats=4),

    Pasaule("Cik palicis no krājumiem?",
            Ievadi("", [
                {"jaut": "Bija {3|4} l sulas, izdzēra {1|2} l. Cik litru "
                         "palika? Atbildi raksti kā a/b.",
                 "atb": ["1/4"], "padoms": "{3|4} − {2|4}."},
                {"jaut": "Bija {1|2} l, izdzēra {3|4} l. Cik litru trūkst? "
                         "Atbildi raksti kā a/b.",
                 "atb": ["1/4"], "padoms": "Rezultāts ir −{1|4}."},
                {"jaut": "Bija {2|3} kg, pielika vēl {1|6} kg. Cik kg ir "
                         "tagad? Atbildi raksti kā a/b.",
                 "atb": ["5/6"], "padoms": "{4|6} + {1|6}."},
                {"jaut": "No {5|6} kg paņēma {1|2} kg. Cik kg palika? "
                         "Atbildi raksti kā a/b.",
                 "atb": ["1/3", "2/6"], "padoms": "{5|6} − {3|6}."},
            ]),
            pavediens="virtuve",
            konteksts="Ja no krājuma paņem vairāk, nekā ir, rezultāts ir "
                      "negatīvs - un tas nozīmē, ka kaut kā pietrūkst.",
            kapec="Negatīva daļa ir tikpat īsta kā negatīvs vesels skaitlis."),

    Zimejums("Daļas abās pusēs no nulles",
             taisne(-1, 1, 1, [(-0.75, "−3/4"), (-0.25, "−1/4"),
                               (0.5, "1/2")]),
             paskaidro="Negatīvas daļas izvietotas tieši tāpat kā pozitīvās, "
                       "tikai pa kreisi no nulles.",
             ievads="Uz taisnes redz, kura daļa ir lielāka."),

    Kopsavilkums([
        "Saskaitu un atņemu daļskaitļus ar zīmēm.",
        "Atrodu kopsaucēju pirms zīmju likuma lietošanas.",
        "Zinu, ka mīnuss attiecas uz visu daļu.",
        "Saīsinu rezultātu un atdalu veselās daļas.",
    ]),

    Majas([
        "Izrēķini −{2|5} + {1|2} un −{1|3} − {1|6}.",
        "Uzzīmē skaitļu taisni un atzīmē abas atbildes.",
        "Pieraksti, kura no tām ir tuvāk nullei.",
    ]),
]
