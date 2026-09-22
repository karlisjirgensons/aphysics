# -*- coding: utf-8 -*-
"""5. klase, 98. stunda: «Kā atņemt no vesela skaitļa?»

Īsa, bet svarīga stunda: no vesela skaitļa atņemt daļu ir tas pašas 68.
stundas paņēmiens, tikai tagad vesels skaitlis var būt arī 3 vai 5. Viss
balstās uz vienu soli - no veselā aizņemas vienu vienību un pārraksta to kā
daļu. Tieši šis solis nākamajā stundā būs vajadzīgs jau ar jauktiem
skaitļiem.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, dala, restis)

TEMA = "Kā atņemt no vesela skaitļa?"

MERKIS = ("Iemācīsimies galvā atņemt daļu no vesela skaitļa.")

SATURS = [
    Sakums("No trim metriem nogriež ceturtdaļu",
           zimejums=restis([["3", "-", "1/4", "2 3/4"]],
                           virsraksts="Aizņemas vienu veselo"),
           paraksts="3 - {1|4} = 2{4|4} - {1|4} = 2{3|4}.",
           fakti=["No vesela skaitļa daļu atņemt tieši nevar.",
                  "Tāpēc vienu veselo pārraksta kā daļu.",
                  "Pārējie veselie paliek neskarti."]),

    Doma("Aizņemies vienu veselo",
         "Lai no vesela skaitļa atņemtu daļu, vienu vienību pārraksta kā "
         "daļu ar vajadzīgo saucēju; pārējie veselie paliek kā ir.",
         soli=[
             "Paskaties, kāds saucējs ir atņemamajai daļai.",
             "No veselā skaitļa atdali vienu vienību.",
             "Uzraksti to kā daļu ar šo saucēju.",
             "Atņem daļu no daļas.",
             "Pieraksti atlikušos veselos un jauno daļu.",
         ],
         pieze="3 = 2{4|4}, 5 = 4{8|8}, 1 = {6|6} - vienmēr aizņemas tieši "
               "vienu vienību un pārraksta to ar tādu saucēju, kāds "
               "vajadzīgs."),

    Paraugs("3 - {1|4}",
            uzd="Izrēķini galvā, cik ir 3 - {1|4}.",
            soli=[
                ("Saucējs ir 4",
                 "Tāds būs arī rezultāta saucējs."),
                ("3 = 2{4|4}",
                 "Aizņemas vienu veselo."),
                ("2{4|4} - {1|4}",
                 "Tagad daļas var atņemt."),
                ("{4|4} - {1|4} = {3|4}",
                 "Atņem skaitītājus."),
                ("2{3|4}",
                 "Divi veseli un trīs ceturtdaļas."),
            ],
            atbilde="3 - {1|4} = 2{3|4}"),

    Ievadi("Atņem galvā", [
        {"jaut": "1 - {1|4} = ? Atbildi raksti kā a/b.",
         "atb": ["3/4"], "padoms": "1 = {4|4}."},
        {"jaut": "3 - {1|4} = ? Atbildi raksti kā a b/c.",
         "atb": ["2 3/4"], "padoms": "3 = 2{4|4}."},
        {"jaut": "2 - {1|3} = ? Atbildi raksti kā a b/c.",
         "atb": ["1 2/3"], "padoms": "2 = 1{3|3}."},
        {"jaut": "5 - {2|5} = ? Atbildi raksti kā a b/c.",
         "atb": ["4 3/5"], "padoms": "5 = 4{5|5}."},
        {"jaut": "4 - {5|6} = ? Atbildi raksti kā a b/c.",
         "atb": ["3 1/6"], "padoms": "4 = 3{6|6}."},
        {"jaut": "2 - {7|8} = ? Atbildi raksti kā a b/c.",
         "atb": ["1 1/8"], "padoms": "2 = 1{8|8}."},
        {"jaut": "6 - {1|2} = ? Atbildi raksti kā a b/c.",
         "atb": ["5 1/2"], "padoms": "6 = 5{2|2}."},
        {"jaut": "3 - {3|4} = ? Atbildi raksti kā a b/c.",
         "atb": ["2 1/4"], "padoms": "3 = 2{4|4}."},
    ], pamats=4,
        ievads="Aizņemies vienu veselo un pārraksti to ar vajadzīgo saucēju."),

    Zimejums("Viena vienība kā daļa",
             dala(4, 3, "3/4 no aizņemtā vesela"),
             paskaidro="No aizņemtā vesela atņēma vienu ceturtdaļu, un "
                       "palika trīs. Pārējie divi veselie netika aiztikti.",
             ievads="Atņem tikai no vienas aizņemtās vienības."),

    Varianti("No kā aizņemas?", [
        {"jaut": "Kā uzrakstīt 3, lai varētu atņemt {1|4}?",
         "opcijas": ["2{4|4}", "3{4|4}", "{3|4}", "2{1|4}"],
         "pareizi": 0,
         "padoms": "Aizņemas vienu veselo."},
        {"jaut": "Cik ir 1 - {3|8}?",
         "opcijas": ["{5|8}", "{3|8}", "{8|3}", "1{5|8}"],
         "pareizi": 0,
         "padoms": "1 = {8|8}."},
        {"jaut": "Cik ir 4 - {1|2}?",
         "opcijas": ["3{1|2}", "4{1|2}", "3", "{7|2} un tas nav jaukts"],
         "pareizi": 0,
         "padoms": "4 = 3{2|2}."},
        {"jaut": "Kāds saucējs būs rezultātam?",
         "opcijas": ["Tāds pats kā atņemamajai daļai", "Vienmēr 2",
                     "Veselais skaitlis", "Saucēju summa"],
         "pareizi": 0,
         "padoms": "Gabalu lielums nemainās."},
        {"jaut": "Cik veselu paliek, atņemot daļu no 5?",
         "opcijas": ["4", "5", "3", "0"],
         "pareizi": 0,
         "padoms": "Vienu aizņēmās."},
        {"jaut": "Skolēns raksta 3 - {1|4} = 3{3|4}. Kur ir kļūda?",
         "opcijas": ["Veselais nav samazināts", "Daļa ir nepareiza",
                     "Saucējs ir nepareizs", "Kļūdas nav"],
         "pareizi": 0,
         "padoms": "Atņemot rezultāts kļūst mazāks."},
    ], pamats=4),

    Pasaule("Cik paliek pāri no dēļa?",
            Ievadi("", [
                {"jaut": "No 3 m dēļa nogriež {1|4} m. Cik metru paliek? "
                         "Atbildi raksti kā a b/c.",
                 "atb": ["2 3/4"], "padoms": "3 = 2{4|4}."},
                {"jaut": "No 2 m līstes nogriež {1|3} m. Cik metru paliek? "
                         "Atbildi raksti kā a b/c.",
                 "atb": ["1 2/3"], "padoms": "2 = 1{3|3}."},
                {"jaut": "No 5 l krāsas izlieto {2|5} l. Cik litru paliek? "
                         "Atbildi raksti kā a b/c.",
                 "atb": ["4 3/5"], "padoms": "5 = 4{5|5}."},
                {"jaut": "No 1 m auklas nogriež {3|8} m. Cik metru paliek? "
                         "Atbildi raksti kā a/b.",
                 "atb": ["5/8"], "padoms": "1 = {8|8}."},
            ]),
            pavediens="maja",
            konteksts="Remontā materiālu vienmēr ir veselos skaitļos, bet "
                      "nogriež daļu.",
            kapec="Atlikumu var pateikt uzreiz, aizņemoties vienu veselo."),

    Kopsavilkums([
        "Atņemu daļu no vesela skaitļa.",
        "Pārrakstu vienu vienību kā daļu ar vajadzīgo saucēju.",
        "Atstāju pārējos veselos neskartus.",
        "Rēķinu šo darbību galvā, bez pieraksta.",
    ]),

    Majas([
        "Izrēķini galvā 4 - {1|5}, 7 - {2|3} un 2 - {5|8}.",
        "Uzraksti, kā tu pārraksti veselo skaitli, lai varētu atņemt.",
        "Atrodi mājās priekšmetu, no kura var nogriezt {1|4} no garuma.",
    ]),
]
