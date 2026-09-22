# -*- coding: utf-8 -*-
"""6. klase, 31. stunda: «Kā izskatās pieraksts?»

Stunda par kārtību uz papīra. Algoritms jau ir; tagad tas jāpieraksta tā, lai
pēc nedēļas to saprastu arī pats. Eksāmenā vērtē tieši pierakstu, nevis to,
kas notika galvā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti)

TEMA = "Kā izskatās pieraksts?"

MERKIS = ("Mācīsimies dalīt daļu ar daļu, veidojot skaidru un pilnīgu "
          "pierakstu.")

SATURS = [
    Sakums("Pieraksts, kuru saprot arī cits cilvēks",
           fakti=["Katrs solis ir viena rinda, un katrā rindā ir vienādības "
                  "zīme.",
                  "Jaukto skaitli pārveido *pirms* dalīšanas, ne pēc.",
                  "Atbildi pieraksta vienkāršākajā formā."]),

    Doma("Trīs rindas, ne vairāk",
         "Pilnīgs dalīšanas pieraksts ir: jauktie skaitļi par neīstām daļām, "
         "dalīšana par reizināšanu, saīsināšana un rezultāts.",
         soli=[
             "1. rinda: pārraksti uzdevumu, jauktos skaitļus pārveidojot.",
             "2. rinda: aizstāj dalīšanu ar reizināšanu ar apgriezto.",
             "3. rinda: saīsini un pieraksti rezultātu.",
             "Ja rezultāts ir neīsta daļa, atdali veselās daļas.",
             "Pieraksti atbildi ar mērvienību, ja tāda uzdevumā ir.",
         ],
         pieze="Rindu nav vairāk par trim, un neviena nav izlaista. Tieši "
               "izlaistā rinda ir tā, kurā parasti pazūd apgriešana."),

    Paraugs("Pilns pieraksts",
            uzd="Cik ir 2{1|4} : {3|8}?",
            soli=[
                ("2{1|4} : {3|8} = {9|4} : {3|8}",
                 "Jauktais skaitlis kļūst par neīstu daļu."),
                ("= {9|4} · {8|3}",
                 "Dalīšana kļūst par reizināšanu."),
                ("= {3|1} · {2|1} = 6",
                 "Saīsina 9 ar 3 un 8 ar 4."),
                ("Pārbaude: 6 · {3|8} = {18|8} = {9|4} = 2{1|4}",
                 "Atgriežas dalāmais."),
            ],
            atbilde="6"),

    Ievadi("Izrēķini, rakstot visus soļus", [
        {"jaut": "Cik ir 1{1|2} : {3|4}?",
         "atb": ["2"], "padoms": "{3|2} · {4|3}."},
        {"jaut": "Cik ir 2{2|3} : {4|9}?",
         "atb": ["6"], "padoms": "{8|3} · {9|4}."},
        {"jaut": "Cik ir {5|8} : 1{1|4}? Atbildi raksti kā a/b.",
         "atb": ["1/2"], "padoms": "{5|8} · {4|5}."},
        {"jaut": "Cik ir 3{1|3} : {5|6}?",
         "atb": ["4"], "padoms": "{10|3} · {6|5}."},
        {"jaut": "Cik ir 1{1|5} : {2|5}?",
         "atb": ["3"], "padoms": "{6|5} · {5|2}."},
        {"jaut": "Cik ir {9|10} : 2{1|4}? Atbildi raksti kā a/b.",
         "atb": ["2/5"], "padoms": "{9|10} · {4|9}."},
    ], pamats=4,
        ievads="Jauktos skaitļus pārveido pirmajā rindā, ne vēlāk."),

    Varianti("Kur pieraksts salūza?", [
        {"jaut": "Skolēns raksta 1{1|2} : {1|4} = 1{4|2}. Kas notika?",
         "opcijas": ["Viņš neapgrieza un nepārveidoja jaukto skaitli",
                     "Viņš saīsināja nepareizi",
                     "Viņš aizmirsa pārbaudi", "Viss ir pareizi"],
         "pareizi": 0,
         "padoms": "Vispirms 1{1|2} = {3|2}."},
        {"jaut": "Kurā rindā pārveido jaukto skaitli?",
         "opcijas": ["Pirmajā", "Pēdējā", "Tikai atbildē", "Nekad"],
         "pareizi": 0,
         "padoms": "Pirms jebkuras darbības."},
        {"jaut": "Kādā formā pieraksta atbildi {14|4}?",
         "opcijas": ["3{1|2}", "{14|4}", "{7|2} un nekā citādi", "3,5 tikai"],
         "pareizi": 0,
         "padoms": "Saīsina un atdala veselās daļas."},
        {"jaut": "Kāpēc pieraksts ir svarīgs arī tad, ja atbilde pareiza?",
         "opcijas": ["Jo pēc tā var atrast kļūdu un to saprot arī citi",
                     "Jo tā prasa skolotājs",
                     "Jo tas aizņem vietu", "Tas nav svarīgs"],
         "pareizi": 0,
         "padoms": "Bez pieraksta kļūdu meklē no jauna."},
    ], pamats=4),

    Pasaule("Cik ilgi pietiks krājumu?",
            Ievadi("", [
                {"jaut": "Stacijā ir 4{1|2} kg pārtikas, dienā apēd {3|4} "
                         "kg. Cik dienu pietiks?",
                 "atb": ["6"], "padoms": "{9|2} · {4|3}."},
                {"jaut": "Ūdens ir 2{1|4} l, dienā izlieto {3|8} l. Cik "
                         "dienu pietiks?",
                 "atb": ["6"], "padoms": "{9|4} · {8|3}."},
                {"jaut": "Skābekļa pietiek 7{1|2} stundām, viens izgājiens "
                         "prasa 1{1|4} stundas. Cik izgājienu?",
                 "atb": ["6"], "padoms": "{15|2} · {4|5}."},
                {"jaut": "Enerģijas ir 3{1|3} vienības, viens mērījums prasa "
                         "{5|6}. Cik mērījumu var veikt?",
                 "atb": ["4"], "padoms": "{10|3} · {6|5}."},
            ]),
            pavediens="kosmoss",
            konteksts="Kosmosa stacijā krājumus rēķina dienās, nevis "
                      "kilogramos - un kļūda pierakstā maksā dienu.",
            kapec="Skaidrs pieraksts ļauj pārbaudīt rēķinu arī citam."),

    Kopsavilkums([
        "Pierakstu dalīšanu trijās skaidrās rindās.",
        "Pārveidoju jauktos skaitļus pirms darbības.",
        "Saīsinu pirms reizināšanas un pierakstu atbildi vienkāršākajā formā.",
        "Pievienoju pārbaudi.",
    ]),

    Majas([
        "Izrēķini 3{3|4} : 1{1|4} ar pilnu pierakstu.",
        "Pārraksti kādu savu veco risinājumu skaidrākā formā.",
        "Iedod savu pierakstu kādam mājās un pajautā, vai viņš to saprot.",
    ]),
]
