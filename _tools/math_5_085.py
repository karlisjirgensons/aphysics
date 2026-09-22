# -*- coding: utf-8 -*-
"""5. klase, 85. stunda: «Kad dalījums ir mazāks nekā viens?»

Turpinājums iepriekšējai stundai, un tā ir prasme, kas noder vēl ilgi: pirms
rēķina pateikt, vai atbilde būs mazāka, vienāda vai lielāka par vienu. Viss
balstās uz vienu salīdzinājumu - dalāmais pret dalītāju -, un tieši tāpēc tas
strādā arī tad, kad skaitļi ir lieli.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, taisne)

TEMA = "Kad dalījums ir mazāks nekā viens?"

MERKIS = ("Mācīsimies izskaidrot, kad dalīšanas rezultāts ir mazāks, vienāds "
          "vai lielāks nekā 1.")

SATURS = [
    Sakums("Trīs dalījumi, trīs atbildes",
           zimejums=taisne(0, 2, 1, [(3 / 4.0, "3/4"), (1.0, "4/4"),
                                     (5 / 4.0, "5/4")],
                           virsraksts="Pa kreisi, virsū un pa labi no 1"),
           paraksts="3 : 4 < 1, bet 4 : 4 = 1 un 5 : 4 > 1.",
           fakti=["Visos trijos dalījumos dalītājs ir viens un tas pats.",
                  "Atšķiras tikai dalāmais.",
                  "Tas arī izšķir, kurā pusē no vieninieka ir atbilde."]),

    Doma("Salīdzini dalāmo ar dalītāju",
         "Dalījums ir mazāks par 1, ja dalāmais ir mazāks par dalītāju; "
         "vienāds ar 1, ja tie ir vienādi; lielāks par 1, ja dalāmais ir "
         "lielāks.",
         soli=[
             "Pieraksti dalījumu kā daļu.",
             "Salīdzini skaitītāju ar saucēju.",
             "Skaitītājs mazāks - daļa mazāka par 1.",
             "Skaitītājs vienāds - daļa ir tieši 1.",
             "Skaitītājs lielāks - daļa lielāka par 1.",
         ],
         pieze="Daļu, kuras skaitītājs ir mazāks par saucēju, sauc par īstu "
               "daļu; ja skaitītājs ir lielāks vai vienāds - par neīstu. "
               "Neīsta daļa vienmēr ir vismaz viens vesels."),

    Paraugs("Vai 7 : 9 ir lielāks par vienu?",
            uzd="Nosaki, vai dalījumi 7 : 9, 9 : 9 un 11 : 9 ir mazāki, "
                "vienādi vai lielāki nekā 1.",
            soli=[
                ("7 : 9 = {7|9}",
                 "Skaitītājs 7, saucējs 9."),
                ("7 < 9, tātad {7|9} < 1",
                 "Īsta daļa."),
                ("9 : 9 = {9|9} = 1",
                 "Skaitļi vienādi."),
                ("11 : 9 = {11|9} > 1",
                 "Skaitītājs lielāks - neīsta daļa."),
            ],
            atbilde="{7|9} < 1, {9|9} = 1, {11|9} > 1"),

    Ievadi("Mazāks, vienāds vai lielāks?", [
        {"jaut": "{3|5} - salīdzini ar 1. Raksti «mazāks», «vienāds» vai "
                 "«lielāks».",
         "atb": ["mazāks", "mazaks"], "padoms": "3 < 5."},
        {"jaut": "{8|8} - salīdzini ar 1.",
         "atb": ["vienāds", "vienads"], "padoms": "8 = 8."},
        {"jaut": "{9|4} - salīdzini ar 1.",
         "atb": ["lielāks", "lielaks"], "padoms": "9 > 4."},
        {"jaut": "{12|15} - salīdzini ar 1.",
         "atb": ["mazāks", "mazaks"], "padoms": "12 < 15."},
        {"jaut": "7 : 3 - salīdzini ar 1.",
         "atb": ["lielāks", "lielaks"], "padoms": "7 > 3."},
        {"jaut": "5 : 5 - salīdzini ar 1.",
         "atb": ["vienāds", "vienads"], "padoms": "5 = 5."},
        {"jaut": "Cik ir {6|6}?",
         "atb": ["1"], "padoms": "Visi gabali kopā."},
        {"jaut": "Cik veselu ir {8|4}?",
         "atb": ["2"], "padoms": "8 : 4."},
    ], pamats=4,
        ievads="Nekas nav jārēķina - tikai jāsalīdzina divi skaitļi."),

    Zimejums("Vieninieks kā robeža",
             taisne(0, 2, 1, [(2 / 3.0, "2/3"), (1.0, "1"), (3 / 2.0, "3/2")],
                    virsraksts="Īstas daļas pa kreisi, neīstas pa labi"),
             paskaidro="{2|3} ir īsta daļa, tāpēc tā stāv pirms vieninieka; "
                       "{3|2} ir neīsta un stāv aiz tā.",
             ievads="Uz taisnes vieninieks sadala visas daļas divās grupās."),

    Varianti("Kur atradīsies atbilde?", [
        {"jaut": "Kad dalījums ir mazāks par 1?",
         "opcijas": ["Kad dalāmais mazāks par dalītāju",
                     "Kad dalāmais lielāks par dalītāju",
                     "Kad abi ir vienādi",
                     "Vienmēr"],
         "pareizi": 0,
         "padoms": "Mazs gabals no liela veselā."},
        {"jaut": "Kāda ir daļa, kuras skaitītājs ir lielāks par saucēju?",
         "opcijas": ["Neīsta", "Īsta", "Nesaīsināma", "Pamatdaļa"],
         "pareizi": 0,
         "padoms": "Tā ir lielāka par vienu."},
        {"jaut": "Cik ir {15|15}?",
         "opcijas": ["1", "0", "15", "{1|15}"],
         "pareizi": 0,
         "padoms": "Visi gabali kopā."},
        {"jaut": "Kurš dalījums ir lielāks par 1?",
         "opcijas": ["13 : 9", "9 : 13", "9 : 9", "4 : 8"],
         "pareizi": 0,
         "padoms": "Dalāmais lielāks par dalītāju."},
        {"jaut": "Vai 100 : 101 ir lielāks par 1?",
         "opcijas": ["Nē, tas ir mazliet mazāks", "Jā", "Tas ir tieši 1",
                     "To nevar zināt"],
         "pareizi": 0,
         "padoms": "100 < 101."},
        {"jaut": "Kāpēc to var pateikt bez rēķināšanas?",
         "opcijas": ["Pietiek salīdzināt divus skaitļus",
                     "Skaitļi ir mazi",
                     "Atbilde vienmēr ir daļa",
                     "To nevar pateikt"],
         "pareizi": 0,
         "padoms": "Skaitītājs pret saucēju."},
    ], pamats=4),

    Pasaule("Vai katram pietiks ar vienu?",
            Ievadi("", [
                {"jaut": "5 picas 8 skolēniem. Vai katram tiek vismaz viena? "
                         "Raksti «jā» vai «nē».",
                 "atb": ["nē", "ne"], "padoms": "5 < 8."},
                {"jaut": "12 picas 8 skolēniem. Vai katram tiek vismaz viena?",
                 "atb": ["jā", "ja"], "padoms": "12 > 8."},
                {"jaut": "8 picas 8 skolēniem. Cik veselu tiek katram?",
                 "atb": ["1"], "padoms": "8 : 8."},
                {"jaut": "16 picas 8 skolēniem. Cik veselu tiek katram?",
                 "atb": ["2"], "padoms": "16 : 8."},
            ]),
            pavediens="skola",
            konteksts="Pirms dalīšanas vienmēr der zināt, vai katram vispār "
                      "pietiks ar vienu veselu.",
            kapec="To pasaka viens salīdzinājums, nevis rēķins."),

    Kopsavilkums([
        "Salīdzinu dalāmo ar dalītāju, pirms sāku rēķināt.",
        "Nosaku, vai dalījums ir mazāks, vienāds vai lielāks nekā 1.",
        "Atšķiru īstu daļu no neīstas.",
        "Zinu, ka daļa ar vienādu skaitītāju un saucēju ir 1.",
    ]),

    Majas([
        "Uzraksti trīs īstas un trīs neīstas daļas.",
        "Nosaki bez rēķināšanas, vai 47 : 50 ir lielāks par 1.",
        "Atrodi dalījumu, kura atbilde ir tieši 1.",
    ]),
]
