# -*- coding: utf-8 -*-
"""5. klase, 66. stunda: «Kā saskaitīt daļas ar dažādiem saucējiem?»

Visa iepriekšējā mikrotemata jēga saplūst vienā darbībā. Jaunā te ir tikai
viena rinda - tā, kurā abas daļas jau ir ar kopsaucēju; pārējais ir 4. klasē
apgūtā saskaitīšana. Tāpēc pierakstā šī rinda nekad netiek izlaista: tieši
tur redzams, ka saskaitīti vienādi gabali.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, dala)

TEMA = "Kā saskaitīt daļas ar dažādiem saucējiem?"

MERKIS = ("Iemācīsimies saskaitīt daļas ar dažādiem saucējiem, pierakstā "
          "parādot pamatīpašības soli.")

SATURS = [
    Sakums("Puse stundas un ceturtdaļa stundas",
           zimejums=dala(4, 3, "3/4"),
           paraksts="{1|2} + {1|4} = {3|4} - trīs ceturtdaļas stundas.",
           fakti=["Puse un ceturtdaļa nav vienādi gabali.",
                  "Saskaitīt var tikai vienāda lieluma gabalus.",
                  "Tāpēc pusi vispirms pārraksta kā divas ceturtdaļas."]),

    Doma("Vispirms kopsaucējs, tad skaitītāji",
         "Daļas ar dažādiem saucējiem saskaita, pārrakstot tās ar kopsaucēju "
         "un saskaitot skaitītājus; saucējs paliek tas pats.",
         soli=[
             "Atrodi abu daļu kopsaucēju.",
             "Paplašini katru daļu līdz šim saucējam.",
             "Saskaiti skaitītājus, saucēju atstāj neskartu.",
             "Ja iznāk saīsināma daļa, saīsini to.",
             "Ja iznāk neīsta daļa, atdali veselo.",
         ],
         pieze="Saucējus nekad nesaskaita: {1|2} + {1|4} nav {2|6}. Saucējs "
               "pasaka, cik lieli ir gabali, un gabalu lielums, tos saliekot "
               "kopā, nemainās."),

    Paraugs("{1|2} + {1|3}",
            uzd="Saskaiti {1|2} un {1|3}, parādot visus soļus.",
            soli=[
                ("Kopsaucējs ir 6",
                 "6 dalās ar 2 un 3."),
                ("{1|2} = {1 · 3|2 · 3} = {3|6}",
                 "Pirmo daļu paplašina."),
                ("{1|3} = {1 · 2|3 · 2} = {2|6}",
                 "Otro daļu paplašina."),
                ("{3|6} + {2|6} = {5|6}",
                 "Saskaita skaitītājus; saucējs paliek 6."),
                ("{5|6} ir nesaīsināma",
                 "Atbilde gatava."),
            ],
            atbilde="{1|2} + {1|3} = {5|6}"),

    Ievadi("Saskaiti daļas", [
        {"jaut": "Cik ir {1|2} + {1|4}? Atbildi raksti kā a/b.",
         "atb": ["3/4"], "padoms": "{2|4} + {1|4}."},
        {"jaut": "Cik ir {1|3} + {1|6}? Atbildi raksti kā a/b.",
         "atb": ["1/2", "3/6"], "padoms": "{2|6} + {1|6} = {3|6}."},
        {"jaut": "Cik ir {2|5} + {1|10}? Atbildi raksti kā a/b.",
         "atb": ["1/2", "5/10"], "padoms": "{4|10} + {1|10}."},
        {"jaut": "Cik ir {1|4} + {1|3}? Atbildi raksti kā a/b.",
         "atb": ["7/12"], "padoms": "{3|12} + {4|12}."},
        {"jaut": "Cik ir {1|2} + {1|6}? Atbildi raksti kā a/b.",
         "atb": ["2/3", "4/6"], "padoms": "{3|6} + {1|6} = {4|6}."},
        {"jaut": "Cik ir {3|8} + {1|4}? Atbildi raksti kā a/b.",
         "atb": ["5/8"], "padoms": "{3|8} + {2|8}."},
        {"jaut": "Cik ir {2|3} + {1|4}? Atbildi raksti kā a/b.",
         "atb": ["11/12"], "padoms": "{8|12} + {3|12}."},
        {"jaut": "Cik ir {1|6} + {3|4}? Atbildi raksti kā a/b.",
         "atb": ["11/12"], "padoms": "{2|12} + {9|12}."},
    ], pamats=4,
        ievads="Kopsaucējs, paplašināšana, skaitītāju summa - trīs soļi "
               "vienmēr."),

    Zimejums("Divas ceturtdaļas un vēl viena",
             dala(4, 3, "1/2 + 1/4"),
             paskaidro="Puse aizņem divas ceturtdaļas, klāt nāk vēl viena - "
                       "kopā trīs no četrām.",
             ievads="Ar vienādiem gabaliem saskaitīšana ir tikai skaitīšana."),

    Varianti("Kur pieraksts aiziet greizi?", [
        {"jaut": "Skolēns rēķina {1|2} + {1|3} = {2|5}. Kas nav labi?",
         "opcijas": ["Saskaitīti arī saucēji", "Nav saīsināts",
                     "Kopsaucējs par mazu", "Viss ir labi"],
         "pareizi": 0,
         "padoms": "Saucējs pasaka gabala lielumu, to nesaskaita."},
        {"jaut": "Kas notiek ar saucēju, saskaitot daļas ar kopsaucēju?",
         "opcijas": ["Tas paliek nemainīgs", "Tas divkāršojas",
                     "Tas saskaitās", "Tas sareizinās"],
         "pareizi": 0,
         "padoms": "Gabalu lielums nemainās."},
        {"jaut": "Kāds ir pirmais solis, saskaitot {2|3} un {1|4}?",
         "opcijas": ["Atrast kopsaucēju 12", "Saskaitīt skaitītājus",
                     "Saīsināt daļas", "Salīdzināt daļas"],
         "pareizi": 0,
         "padoms": "Vienādi gabali vispirms."},
        {"jaut": "Cik ir {1|4} + {1|4}?",
         "opcijas": ["{1|2}", "{2|8}", "{1|8}", "{1|4}"],
         "pareizi": 0,
         "padoms": "{2|4} saīsināts."},
        {"jaut": "Rezultāts iznāca {6|8}. Ko dara tagad?",
         "opcijas": ["Saīsina līdz {3|4}", "Atstāj kā ir",
                     "Paplašina", "Saskaita vēlreiz"],
         "pareizi": 0,
         "padoms": "Atbildi raksta nesaīsināmu."},
        {"jaut": "Kurš pieraksts parāda pamatīpašību?",
         "opcijas": ["{1|2} = {1 · 3|2 · 3} = {3|6}",
                     "{1|2} = {3|6}",
                     "{1|2} + {1|3} = {5|6}",
                     "{1|2} = 0,5"],
         "pareizi": 0,
         "padoms": "Redzams reizinātājs pie abiem locekļiem."},
    ], pamats=4),

    Pasaule("Cik daļas dienas aizņem skola?",
            Ievadi("", [
                {"jaut": "Stundās paiet {1|3} dienas, mājasdarbos {1|6}. Cik "
                         "kopā? Atbildi raksti kā a/b.",
                 "atb": ["1/2", "3/6"], "padoms": "{2|6} + {1|6}."},
                {"jaut": "Pulciņos paiet {1|12} dienas. Cik kopā ar iepriekšējo "
                         "pusi? Atbildi raksti kā a/b.",
                 "atb": ["7/12"], "padoms": "{6|12} + {1|12}."},
                {"jaut": "Ceļā uz skolu paiet {1|12}, atpakaļ {1|12}. Cik "
                         "kopā? Atbildi raksti kā a/b.",
                 "atb": ["1/6", "2/12"], "padoms": "{2|12} saīsināts."},
                {"jaut": "Miegā paiet {1|3} dienas, skolā {1|4}. Cik kopā? "
                         "Atbildi raksti kā a/b.",
                 "atb": ["7/12"], "padoms": "{4|12} + {3|12}."},
            ]),
            pavediens="skola",
            konteksts="Diena sadalās nevienādos gabalos, un tikai kopsaucējs "
                      "ļauj tos saskaitīt.",
            kapec="Bez tā katra nodarbe paliek savā mērogā."),

    Kopsavilkums([
        "Atrodu divu daļu kopsaucēju un paplašinu abas daļas.",
        "Saskaitu skaitītājus, saucēju atstājot nemainīgu.",
        "Pierakstā parādu pamatīpašības soli.",
        "Saīsinu rezultātu, ja tas ir saīsināms.",
    ]),

    Majas([
        "Saskaiti {2|5} + {1|4} un pieraksti visus soļus.",
        "Atrodi divas daļas, kuru summa ir tieši {1|2}.",
        "Padomā, kāpēc saucējus nedrīkst saskaitīt.",
    ]),
]
