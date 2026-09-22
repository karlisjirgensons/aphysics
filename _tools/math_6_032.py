# -*- coding: utf-8 -*-
"""6. klase, 32. stunda: «Kāpēc dalot var iegūt lielāku skaitli?»

Mikrotemata noslēgums un otrs priekšstata lūzums. Pēc stundas par
reizināšanu, kas samazina, šī runā par dalīšanu, kas palielina. Abus kopā
nevar iemācīties no galvas - tos var tikai saprast.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Kustiba, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti)

TEMA = "Kāpēc dalot var iegūt lielāku skaitli?"

MERKIS = ("Skaidrosim, kad dalīšanas rezultāts ir lielāks nekā dalāmais, un "
          "kāpēc tā notiek.")

SATURS = [
    Sakums("Dalīšana ne vienmēr samazina",
           fakti=["12 : {1|2} = 24 - rezultāts ir divreiz lielāks.",
                  "Jo mazāks dalītājs, jo vairāk reižu tas ietilpst.",
                  "Robeža atkal ir vieninieks."]),

    Doma("Viss atkarīgs no tā, vai dalītājs ir mazāks par 1",
         "Dalot ar skaitli, kas mazāks par 1, rezultāts ir lielāks par "
         "dalāmo; dalot ar lielāku par 1 - mazāks.",
         soli=[
             "Paskaties, vai dalītājs ir lielāks vai mazāks par 1.",
             "Ja mazāks - gaidi lielāku rezultātu.",
             "Ja lielāks - gaidi mazāku.",
             "Ja tieši 1 - rezultāts būs tas pats skaitlis.",
             "Izrēķini un salīdzini ar savu minējumu.",
         ],
         pieze="Tas nav pretrunā ar veselajiem skaitļiem: 12 : 3 = 4 ir "
               "mazāks, jo 3 ir lielāks par 1. Likums ir viens - tikai "
               "sākumskolā dalītājs nekad nebija mazāks par vieninieku."),

    Slidnis("Maini dalītāju",
            [{"v": "12 : 4", "teksts": "= 3 - daudz mazāks", "josla": 12},
             {"v": "12 : 2", "teksts": "= 6 - uz pusi mazāks", "josla": 25},
             {"v": "12 : 1", "teksts": "= 12 - nekas nemainās", "josla": 50},
             {"v": "12 : {1|2}", "teksts": "= 24 - divreiz lielāks",
              "josla": 75},
             {"v": "12 : {1|4}", "teksts": "= 48 - četrreiz lielāks",
              "josla": 100}],
            ievads="Spied soli pa solim: dalāmais paliek 12, mainās tikai "
                   "dalītājs. Pie vieninieka rezultāts pāriet otrā pusē."),

    Paraugs("Kurš rezultāts būs lielāks?",
            uzd="Nerēķinot salīdzini: 20 : {4|5} un 20 : {5|4}.",
            soli=[
                ("{4|5} ir mazāks par 1",
                 "Tāpēc rezultāts būs lielāks par 20."),
                ("{5|4} ir lielāks par 1",
                 "Tāpēc rezultāts būs mazāks par 20."),
                ("20 : {4|5} = 20 · {5|4} = 25",
                 "Pārbaude pirmajam."),
                ("20 : {5|4} = 20 · {4|5} = 16",
                 "Pārbaude otrajam."),
            ],
            atbilde="lielāks ir 20 : {4|5}"),

    Ievadi("Izrēķini un salīdzini", [
        {"jaut": "Cik ir 10 : {1|2}?",
         "atb": ["20"], "padoms": "10 · 2."},
        {"jaut": "Cik ir 9 : {3|4}?",
         "atb": ["12"], "padoms": "9 · {4|3}."},
        {"jaut": "Cik ir 15 : {5|3}?",
         "atb": ["9"], "padoms": "15 · {3|5}."},
        {"jaut": "Cik ir 8 : {2|5}?",
         "atb": ["20"], "padoms": "8 · {5|2}."},
        {"jaut": "Cik ir 6 : 1?",
         "atb": ["6"], "padoms": "Dalot ar 1, nekas nemainās."},
        {"jaut": "Cik ir {3|4} : {1|8}?",
         "atb": ["6"], "padoms": "{3|4} · 8."},
    ], pamats=4,
        ievads="Vispirms pasaki, vai rezultāts būs lielāks vai mazāks."),

    Pasaule("Cik ilgi darbosies stacija?",
            Kustiba("", [
                {"jaut": "Enerģijas ir 12 vienības, stundā izlieto {1|2}. "
                         "Cik stundas pietiks?",
                 "atb": 24, "beigas": 60, "iedala": 10, "mers": "stundas",
                 "merkis": "beigas", "objekts": "Stacija",
                 "padoms": "12 · 2."},
                {"jaut": "Taupības režīmā stundā izlieto {1|4}. Cik stundas "
                         "pietiks?",
                 "atb": 48, "beigas": 60, "iedala": 10, "mers": "stundas",
                 "merkis": "beigas", "objekts": "Stacija",
                 "padoms": "12 · 4."},
                {"jaut": "Pastiprinātā režīmā stundā izlieto {3|2}. Cik "
                         "stundas pietiks?",
                 "atb": 8, "beigas": 60, "iedala": 10, "mers": "stundas",
                 "merkis": "beigas", "objekts": "Stacija",
                 "padoms": "12 · {2|3}."},
                {"jaut": "Parastajā režīmā stundā izlieto 1 vienību. Cik "
                         "stundas pietiks?",
                 "atb": 12, "beigas": 60, "iedala": 10, "mers": "stundas",
                 "merkis": "beigas", "objekts": "Stacija",
                 "padoms": "Dalot ar 1, nekas nemainās."},
            ]),
            pavediens="kosmoss",
            konteksts="Jo taupīgāks režīms, jo tālāk aizbrauc rādītājs - "
                      "mazāks dalītājs dod lielāku rezultātu.",
            kapec="Tieši tāpēc dalīšana ar daļu var palielināt skaitli."),

    Varianti("Bez rēķināšanas", [
        {"jaut": "Kurš skaitlis ir lielāks: 30 : {2|3} vai 30?",
         "opcijas": ["30 : {2|3}", "30", "Abi vienādi", "Nevar zināt"],
         "pareizi": 0,
         "padoms": "{2|3} ir mazāks par 1."},
        {"jaut": "Kurš skaitlis ir mazāks: 50 : {5|4} vai 50?",
         "opcijas": ["50 : {5|4}", "50", "Abi vienādi", "Nevar zināt"],
         "pareizi": 0,
         "padoms": "{5|4} ir lielāks par 1."},
        {"jaut": "Kad dalījums ir tieši tāds pats kā dalāmais?",
         "opcijas": ["Kad dalītājs ir 1", "Kad dalāmais ir 1",
                     "Nekad", "Vienmēr"],
         "pareizi": 0,
         "padoms": "{4|4} arī ir 1."},
        {"jaut": "Kā mainās rezultāts, ja dalītāju samazina uz pusi?",
         "opcijas": ["Tas kļūst divreiz lielāks",
                     "Tas kļūst divreiz mazāks",
                     "Tas nemainās", "Tas kļūst par nulli"],
         "pareizi": 0,
         "padoms": "Mazāks gabals ietilpst vairāk reižu."},
    ], pamats=4),

    Kopsavilkums([
        "Paskaidroju, kad dalīšanas rezultāts ir lielāks par dalāmo.",
        "Zinu robežu: dalītājs mazāks, vienāds vai lielāks par 1.",
        "Pirms rēķināšanas paredzu rezultāta lielumu.",
        "Savienoju šo likumu ar reizināšanas likumu.",
    ]),

    Majas([
        "Izdomā trīs dalījumus, kuru rezultāts ir lielāks par dalāmo.",
        "Pieraksti dalījumu, kura rezultāts ir tieši tāds pats kā dalāmais.",
        "Paskaidro, kāpēc 1 : {1|100} ir 100.",
    ]),
]
