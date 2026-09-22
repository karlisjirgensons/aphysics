# -*- coding: utf-8 -*-
"""6. klase, 22. stunda: «Kā pārbaudīt rezultātu?»

Mikrotemata noslēgums. Pārbaude ar reizināšanu nav papildu darbs - tā ir
vienīgais veids pašam uzzināt, vai atbilde ir pareiza, kad skolotāja nav
blakus. Te to prasa katram uzdevumam.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti)

TEMA = "Kā pārbaudīt rezultātu?"

MERKIS = ("Iemācīsimies pārbaudīt dalījumu ar reizināšanu un skaidri "
          "pierakstīt savu risinājumu.")

SATURS = [
    Sakums("Lidmašīnas pilots pārbauda divreiz",
           fakti=["Kļūdu pamana nevis tas, kurš rēķina lēni, bet tas, kurš "
                  "pārbauda.",
                  "Dalījumu pārbauda ar reizināšanu: rezultāts reiz "
                  "dalītājs.",
                  "Ja iznāk dalāmais, atbilde ir pareiza."]),

    Doma("Reizināšana ir dalīšanas spogulis",
         "Ja a : b = c, tad c · b = a - tāpēc katru dalījumu var pārbaudīt, "
         "neprasot nevienam.",
         soli=[
             "Pieraksti dalījumu un tā rezultātu.",
             "Reizini rezultātu ar dalītāju.",
             "Salīdzini ar dalāmo.",
             "Ja nesakrīt, meklē kļūdu: visbiežāk tā ir saucējā.",
             "Pieraksti pārbaudi blakus risinājumam, nevis galvā.",
         ],
         pieze="Pārbaude der arī otrādi: reizinājumu pārbauda ar dalīšanu. "
               "Tieši tāpēc abas darbības mācās kopā."),

    Paraugs("Izrēķini un pārbaudi",
            uzd="Cik ir {8|9} : 4? Pieraksti arī pārbaudi.",
            soli=[
                ("{8|9} : 4 = {8 : 4|9}",
                 "Skaitītājs dalās ar 4."),
                ("= {2|9}",
                 "Tas ir rezultāts."),
                ("Pārbaude: {2|9} · 4 = {8|9}",
                 "Reizina rezultātu ar dalītāju."),
                ("{8|9} = {8|9}",
                 "Sakrīt ar dalāmo - atbilde pareiza."),
            ],
            atbilde="{2|9}"),

    Ievadi("Izrēķini un pārbaudi pats", [
        {"jaut": "Cik ir {6|11} : 3? Atbildi raksti kā a/b.",
         "atb": ["2/11"], "padoms": "6 : 3 = 2; pārbaude {2|11} · 3."},
        {"jaut": "Cik ir {9|10} : 3? Atbildi raksti kā a/b.",
         "atb": ["3/10"], "padoms": "9 : 3 = 3."},
        {"jaut": "Cik ir {1|2} · 6?",
         "atb": ["3"], "padoms": "{6|2} = 3; pārbaude 3 : 6 = {1|2}."},
        {"jaut": "Cik ir 4 : {1|7}?",
         "atb": ["28"], "padoms": "4 · 7; pārbaude 28 · {1|7} = 4."},
        {"jaut": "{3|8} : 3 = ? Atbildi raksti kā a/b.",
         "atb": ["1/8"], "padoms": "Pārbaude: {1|8} · 3 = {3|8}."},
        {"jaut": "Kāds skaitlis, reizināts ar 5, dod {5|6}? Atbildi raksti "
                 "kā a/b.",
         "atb": ["1/6"], "padoms": "{5|6} : 5."},
    ], pamats=4,
        ievads="Katrai atbildei pieraksti arī pārbaudi - burtnīcā, ne galvā."),

    Varianti("Vai pārbaude izdevās?", [
        {"jaut": "{2|3} : 2 = {1|3}. Kāda ir pārbaude?",
         "opcijas": ["{1|3} · 2 = {2|3}", "{1|3} : 2",
                     "{2|3} · 2", "{2|3} + {1|3}"],
         "pareizi": 0,
         "padoms": "Rezultāts reiz dalītājs."},
        {"jaut": "Skolēns ieguva {3|4} : 3 = {1|12}. Pārbaude dod "
                 "{1|12} · 3 = {1|4}. Ko tas nozīmē?",
         "opcijas": ["Atbilde ir nepareiza", "Atbilde ir pareiza",
                     "Pārbaude ir nepareiza", "Nevar spriest"],
         "pareizi": 0,
         "padoms": "{1|4} nav {3|4} - kaut kur ir kļūda."},
        {"jaut": "Kura ir pareizā atbilde uzdevumam {3|4} : 3?",
         "opcijas": ["{1|4}", "{1|12}", "{9|4}", "{3|12}"],
         "pareizi": 0,
         "padoms": "3 : 3 = 1; saucējs paliek 4."},
        {"jaut": "Kāpēc pārbaude ir vērtīga tieši mājās?",
         "opcijas": ["Jo neviens cits atbildi nepateiks",
                     "Jo tā ir ātrāka par rēķinu",
                     "Jo skolotājs to prasa",
                     "Tā nav vērtīga"],
         "pareizi": 0,
         "padoms": "Pārbaude aizstāj atbilžu lapu."},
    ], pamats=4),

    Pasaule("Vai pasūtījums ir pareizs?",
            Ievadi("", [
                {"jaut": "Vienam dzērienam vajag {1|4} l sulas. Cik litru "
                         "vajag 8 dzērieniem?",
                 "atb": ["2"], "padoms": "{8|4} = 2."},
                {"jaut": "Pārbaude: 2 l sadala 8 glāzēs. Cik litru ir vienā? "
                         "Atbildi raksti kā a/b.",
                 "atb": ["1/4"], "padoms": "2 : 8."},
                {"jaut": "Vienai porcijai vajag {2|5} kg kartupeļu. Cik kg "
                         "vajag 10 porcijām?",
                 "atb": ["4"], "padoms": "{20|5} = 4."},
                {"jaut": "Pārbaude: 4 kg sadala 10 porcijās. Cik kg ir "
                         "vienā? Atbildi raksti kā a/b.",
                 "atb": ["2/5", "4/10"], "padoms": "4 : 10 = {4|10} = {2|5}."},
            ]),
            pavediens="veikals",
            konteksts="Pasūtot produktus klases pasākumam, kļūda nozīmē vai "
                      "nu tukšu galdu, vai izmestu pārtiku.",
            kapec="Pārbaude ar pretējo darbību atklāj kļūdu uzreiz."),

    Kopsavilkums([
        "Pārbaudu dalījumu ar reizināšanu un reizinājumu ar dalīšanu.",
        "Pierakstu pārbaudi blakus risinājumam.",
        "Pēc pārbaudes pasaku, vai atbilde ir pareiza, un kāpēc.",
        "Meklēju kļūdu tur, kur tā visbiežāk ir: saucējā.",
    ]),

    Majas([
        "Izrēķini trīs dalījumus ar daļām un pieraksti katram pārbaudi.",
        "Atrodi kādā savā vecā darbā kļūdu, ko pārbaude būtu pamanījusi.",
        "Izdomā uzdevumu, kurā pārbaude ir vienkāršāka par pašu rēķinu.",
    ]),
]
