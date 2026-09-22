# -*- coding: utf-8 -*-
"""5. klase, 61. stunda: «Vairāk vai mazāk nekā puse?»

Iepriekšējā stunda deva drošu paņēmienu, bet lēnu. Te māca otru prasmi, kas
sportā un veikalā noder biežāk: novērtēt daļu galvā, salīdzinot to ar pusi.
Viss balstās uz vienu jautājumu - vai skaitītājs ir lielāks par pusi saucēja.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, taisne)

TEMA = "Vairāk vai mazāk nekā puse?"

MERKIS = ("Mācīsimies galvā salīdzināt daļu ar pusi un pamatot savu "
          "spriedumu.")

SATURS = [
    Sakums("Puslaiks ir pagājis - vai vairāk?",
           zimejums=taisne(0, 1, 1, [(1 / 2.0, "1/2"), (7 / 12.0, "7/12")],
                           virsraksts="Puse un mazliet vairāk"),
           paraksts="{7|12} stāv pa labi no puses, tātad ir lielāka.",
           fakti=["Spēlē nospēlētas 7 no 12 minūtēm - vai puslaiks pagājis?",
                  "Kopīgo saucēju te meklēt nevajag.",
                  "Pietiek salīdzināt skaitītāju ar pusi saucēja."]),

    Doma("Puse saucēja ir robeža",
         "Daļa ir lielāka par pusi tad, ja tās skaitītājs ir lielāks nekā "
         "puse no saucēja.",
         soli=[
             "Izdali saucēju ar 2.",
             "Salīdzini skaitītāju ar šo pusi.",
             "Skaitītājs lielāks - daļa lielāka par pusi.",
             "Skaitītājs mazāks - daļa mazāka par pusi.",
             "Vienādi - daļa ir tieši puse.",
         ],
         pieze="Daļā {7|12} puse no saucēja ir 6, bet skaitītājs ir 7, tātad "
               "{7|12} > {1|2}. Tas pats darbojas arī ar nepāra saucēju: "
               "{4|9} ir mazāka par pusi, jo puse no 9 ir 4,5."),

    Paraugs("Vai {5|9} ir vairāk nekā puse?",
            uzd="Nosaki galvā, vai {5|9} ir lielāka vai mazāka par pusi.",
            soli=[
                ("Puse no 9 ir 4,5",
                 "Saucēju dala ar 2."),
                ("Skaitītājs ir 5",
                 "Salīdzina ar 4,5."),
                ("5 > 4,5",
                 "Skaitītājs pārsniedz pusi."),
                ("{5|9} > {1|2}",
                 "Atbilde - bez paplašināšanas."),
            ],
            atbilde="{5|9} ir lielāka par pusi"),

    Ievadi("Vairāk vai mazāk par pusi?", [
        {"jaut": "{3|5} - vairāk vai mazāk par pusi? Raksti «vairāk» vai "
                 "«mazāk».",
         "atb": ["vairāk", "vairak"], "padoms": "Puse no 5 ir 2,5."},
        {"jaut": "{2|7} - vairāk vai mazāk par pusi?",
         "atb": ["mazāk", "mazak"], "padoms": "Puse no 7 ir 3,5."},
        {"jaut": "{6|11} - vairāk vai mazāk par pusi?",
         "atb": ["vairāk", "vairak"], "padoms": "Puse no 11 ir 5,5."},
        {"jaut": "{4|10} - vairāk vai mazāk par pusi?",
         "atb": ["mazāk", "mazak"], "padoms": "Puse no 10 ir 5."},
        {"jaut": "{9|16} - vairāk vai mazāk par pusi?",
         "atb": ["vairāk", "vairak"], "padoms": "Puse no 16 ir 8."},
        {"jaut": "{7|15} - vairāk vai mazāk par pusi?",
         "atb": ["mazāk", "mazak"], "padoms": "Puse no 15 ir 7,5."},
        {"jaut": "Cik liels skaitītājs daļai ar saucēju 14 ir tieši puse?",
         "atb": ["7"], "padoms": "14 : 2."},
        {"jaut": "Cik liels skaitītājs daļai ar saucēju 100 ir tieši puse?",
         "atb": ["50"], "padoms": "100 : 2."},
    ], pamats=4,
        ievads="Saucēju dala ar 2 un salīdzina ar skaitītāju - tas ir viss."),

    Zimejums("Puse sadala taisni divās pusēs",
             taisne(0, 1, 1, [(2 / 7.0, "2/7"), (1 / 2.0, "1/2"),
                              (5 / 9.0, "5/9")],
                    virsraksts="Kas pa kreisi, kas pa labi"),
             paskaidro="{2|7} ir pa kreisi no puses, {5|9} - pa labi. Vairāk "
                       "nekas nav jārēķina.",
             ievads="Puse ir atzīme, pret kuru mēra pārējās daļas."),

    Varianti("Spried galvā", [
        {"jaut": "Kad daļa ir lielāka par pusi?",
         "opcijas": ["Kad skaitītājs lielāks par pusi saucēja",
                     "Kad skaitītājs lielāks par saucēju",
                     "Kad saucējs ir pāra skaitlis",
                     "Kad skaitītājs ir nepāra skaitlis"],
         "pareizi": 0,
         "padoms": "Robeža ir puse no saucēja."},
        {"jaut": "Kura daļa ir tieši puse?",
         "opcijas": ["{9|18}", "{9|20}", "{8|18}", "{10|21}"],
         "pareizi": 0,
         "padoms": "Skaitītājs ir tieši puse no saucēja."},
        {"jaut": "{11|20} un {9|20} - kura ir lielāka par pusi?",
         "opcijas": ["{11|20}", "{9|20}", "Abas", "Neviena"],
         "pareizi": 0,
         "padoms": "Puse no 20 ir 10."},
        {"jaut": "Komanda uzvarēja 7 no 15 spēlēm. Vai tā ir vairāk nekā "
                 "puse?",
         "opcijas": ["Nē, puse būtu 7,5", "Jā", "Tieši puse",
                     "To nevar zināt"],
         "pareizi": 0,
         "padoms": "15 : 2 = 7,5."},
        {"jaut": "Kāpēc šis paņēmiens ir ātrāks par kopīgo saucēju?",
         "opcijas": ["Jāizdara tikai viena dalīšana",
                     "Nav jāzina saucējs",
                     "Nav jāzina skaitītājs",
                     "Tas nav ātrāks"],
         "pareizi": 0,
         "padoms": "Paplašināt neko nevajag."},
        {"jaut": "{4|9} un {5|9} - kura ir lielāka par pusi?",
         "opcijas": ["{5|9}", "{4|9}", "Abas", "Neviena"],
         "pareizi": 0,
         "padoms": "Puse no 9 ir 4,5."},
    ], pamats=4),

    Pasaule("Vai komanda nospēlējusi vairāk nekā pusi?",
            Ievadi("", [
                {"jaut": "Sezonā ir 18 spēles, nospēlētas 11. Vairāk vai "
                         "mazāk par pusi? Raksti «vairāk» vai «mazāk».",
                 "atb": ["vairāk", "vairak"], "padoms": "Puse no 18 ir 9."},
                {"jaut": "Spēle ilgst 60 minūtes, pagājušas 26. Vairāk vai "
                         "mazāk par pusi?",
                 "atb": ["mazāk", "mazak"], "padoms": "Puse no 60 ir 30."},
                {"jaut": "Distance ir 24 km, noskrieti 13 km. Vairāk vai "
                         "mazāk par pusi?",
                 "atb": ["vairāk", "vairak"], "padoms": "Puse no 24 ir 12."},
                {"jaut": "Cik kilometru ir tieši puse no 24 km distances?",
                 "atb": ["12"], "padoms": "24 : 2."},
            ]),
            pavediens="sports",
            konteksts="Treneris spēles laikā nerēķina kopīgos saucējus - "
                      "viņam jāzina tikai, vai puse jau pagājusi.",
            kapec="Novērtējums galvā der tur, kur precīzs rēķins nav "
                  "vajadzīgs."),

    Kopsavilkums([
        "Salīdzinu daļu ar pusi, nedalot to kopīgā saucējā.",
        "Atrodu pusi no saucēja un salīdzinu to ar skaitītāju.",
        "Pamatoju spriedumu ar skaitļiem, ne ar izskatu.",
        "Atpazīstu daļas, kas ir tieši puse.",
    ]),

    Majas([
        "Uzraksti trīs daļas, kas ir mazliet lielākas par pusi.",
        "Atrodi sporta ziņās skaitli, ko var salīdzināt ar pusi.",
        "Padomā, kā tāpat galvā salīdzināt daļu ar ceturtdaļu.",
    ]),
]
