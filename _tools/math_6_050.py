# -*- coding: utf-8 -*-
"""6. klase, 50. stunda: «Kāds dalījums sanāk, dalot 42 : 7 un 4,2 : 7?»

Stunda par skaitļa decimālo sastāvu. Ja dalāmais kļūst desmit reižu mazāks,
tikpat reižu sarūk arī dalījums - un tas nozīmē, ka vienu izrēķinātu
dalījumu var izmantot veselā rindā citu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti)

TEMA = "Kāds dalījums sanāk, dalot 42 : 7 un 4,2 : 7?"

MERKIS = ("Salīdzināsim dalāmā decimālo sastāvu un saistīsim to ar "
          "rezultātu.")

SATURS = [
    Sakums("Viens rēķins - visa rinda atbilžu",
           fakti=["42 : 7 = 6; 4,2 : 7 = 0,6; 0,42 : 7 = 0,06.",
                  "Dalāmais sarūk desmit reižu - tikpat sarūk dalījums.",
                  "Dalītājs visu laiku paliek tas pats."]),

    Doma("Dalījums seko dalāmajam",
         "Ja dalāmo samazina vai palielina 10, 100 vai 1000 reižu un "
         "dalītājs nemainās, dalījums mainās tikpat reižu.",
         soli=[
             "Izrēķini dalījumu ar veseliem skaitļiem.",
             "Salīdzini savu dalāmo ar veselo: cik reižu tas ir mazāks?",
             "Samazini dalījumu tikpat reižu.",
             "Pārbaudi ar reizināšanu.",
         ],
         pieze="Tāpēc rēķinot vispirms atmet komatu: 4,2 : 7 nozīmē 42 : 7, "
               "un tikai beigās komatu ieliek atpakaļ - par vienu vietu "
               "pa kreisi."),

    Slidnis("Viens un tas pats dalītājs",
            [{"v": "420 : 7", "teksts": "= 60", "josla": 100},
             {"v": "42 : 7", "teksts": "= 6", "josla": 70},
             {"v": "4,2 : 7", "teksts": "= 0,6", "josla": 45},
             {"v": "0,42 : 7", "teksts": "= 0,06", "josla": 20}],
            ievads="Spied soli pa solim: dalītājs paliek 7. Cipari dalījumā "
                   "nemainās - mainās tikai komata vieta."),

    Paraugs("No viena dalījuma uz citiem",
            uzd="Zinot, ka 56 : 8 = 7, izrēķini 5,6 : 8 un 0,56 : 8.",
            soli=[
                ("5,6 ir 10 reižu mazāks par 56",
                 "Komats pārcelts vienu vietu pa kreisi."),
                ("Tāpēc 5,6 : 8 = 0,7",
                 "Dalījums arī 10 reižu mazāks."),
                ("0,56 ir 100 reižu mazāks par 56",
                 "Divas vietas pa kreisi."),
                ("Tāpēc 0,56 : 8 = 0,07",
                 "Dalījums arī 100 reižu mazāks."),
            ],
            atbilde="0,7 un 0,07"),

    Ievadi("Izmanto zināmo dalījumu", [
        {"jaut": "Zināms: 36 : 4 = 9. Cik ir 3,6 : 4?",
         "atb": ["0,9", "0.9"], "padoms": "Desmit reižu mazāk."},
        {"jaut": "Zināms: 36 : 4 = 9. Cik ir 0,36 : 4?",
         "atb": ["0,09", "0.09"], "padoms": "Simt reižu mazāk."},
        {"jaut": "Zināms: 81 : 9 = 9. Cik ir 8,1 : 9?",
         "atb": ["0,9", "0.9"], "padoms": "Viena vieta pa kreisi."},
        {"jaut": "Zināms: 144 : 12 = 12. Cik ir 14,4 : 12?",
         "atb": ["1,2", "1.2"], "padoms": "Desmit reižu mazāk."},
        {"jaut": "Zināms: 25 : 5 = 5. Cik ir 250 : 5?",
         "atb": ["50"], "padoms": "Desmit reižu vairāk."},
        {"jaut": "Zināms: 63 : 7 = 9. Cik ir 0,063 : 7?",
         "atb": ["0,009", "0.009"], "padoms": "Tūkstoš reižu mazāk."},
    ], pamats=4,
        ievads="Vispirms izrēķini ar veseliem, tad pārcel komatu."),

    Varianti("Kas mainās un kas ne?", [
        {"jaut": "Dalāmo samazina 10 reižu, dalītājs nemainās. Kas notiek "
                 "ar dalījumu?",
         "opcijas": ["Tas kļūst 10 reižu mazāks", "Tas nemainās",
                     "Tas kļūst 10 reižu lielāks", "Tas kļūst par nulli"],
         "pareizi": 0,
         "padoms": "Dalījums seko dalāmajam."},
        {"jaut": "Zināms: 48 : 6 = 8. Cik ir 4,8 : 6?",
         "opcijas": ["0,8", "8", "0,08", "80"],
         "pareizi": 0,
         "padoms": "Viena vieta pa kreisi."},
        {"jaut": "Kāpēc var rēķināt bez komata?",
         "opcijas": ["Jo cipari dalījumā nemainās",
                     "Jo komats nav svarīgs",
                     "Jo dalītājs ir vesels", "Tā nedrīkst"],
         "pareizi": 0,
         "padoms": "Mainās tikai komata vieta."},
        {"jaut": "Ja dalāmo palielina 100 reižu, dalījums...",
         "opcijas": ["kļūst 100 reižu lielāks", "nemainās",
                     "kļūst 100 reižu mazāks", "kļūst 10 reižu lielāks"],
         "pareizi": 0,
         "padoms": "Tas pats likums otrā virzienā."},
    ], pamats=4),

    Pasaule("Cik izmaksā viens grams?",
            Ievadi("", [
                {"jaut": "250 g produkta maksā 2 €. Cik eiro maksā 25 g?",
                 "atb": ["0,2", "0.2"], "padoms": "Desmit reižu mazāk."},
                {"jaut": "Cik eiro maksā 2,5 g?",
                 "atb": ["0,02", "0.02"], "padoms": "Simt reižu mazāk."},
                {"jaut": "8 kastes sver 96 kg. Cik kg sver viena?",
                 "atb": ["12"], "padoms": "96 : 8."},
                {"jaut": "8 mazās kastes sver 9,6 kg. Cik kg sver viena?",
                 "atb": ["1,2", "1.2"], "padoms": "Desmit reižu mazāk nekā "
                                                  "iepriekš."},
            ]),
            pavediens="veikals",
            konteksts="Cenu salīdzināšanā skaitļi atšķiras tikai ar komata "
                      "vietu - viens rēķins der visiem iepakojumiem.",
            kapec="Zinot vienu dalījumu, pārējos var pateikt uzreiz."),

    Kopsavilkums([
        "Saistu dalāmā decimālo sastāvu ar dalījuma lielumu.",
        "Rēķinu dalījumu bez komata un ieliku to beigās.",
        "Izmantoju vienu zināmu dalījumu, lai iegūtu vairākus citus.",
        "Pārbaudu rezultātu ar reizināšanu.",
    ]),

    Majas([
        "Zinot, ka 72 : 8 = 9, pieraksti četrus dalījumus ar komatu.",
        "Atrodi divus dalījumus, kuru atbilde atšķiras tikai ar komata "
        "vietu.",
        "Paskaidro, kāpēc 0,42 : 7 nav 6.",
    ]),
]
