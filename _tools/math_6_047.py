# -*- coding: utf-8 -*-
"""6. klase, 47. stunda: «Kāpēc dalot ar 0,1 skaitlis aug?»

Ceturtais algoritms un otrs priekšstata lūzums šajā tematā. Tas pats
jautājums, kas bija parastajām daļām - cik reižu 0,1 ietilpst? -, tikai
decimālajā pierakstā. Atbilde tāpēc ir zināma jau iepriekš.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Kustiba, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti)

TEMA = "Kāpēc dalot ar 0,1 skaitlis aug?"

MERKIS = ("Skaidrosim dalīšanu ar 0,1; 0,01 un 0,001 un saistīsim to ar "
          "reizināšanu.")

SATURS = [
    Sakums("Cik desmitdaļas ietilpst vienā?",
           fakti=["1 : 0,1 = 10, jo vienā veselā ir desmit desmitdaļas.",
                  "Dalot ar 0,1, komats pārceļas par vienu vietu pa labi.",
                  "Dalīt ar 0,1 ir tas pats, kas reizināt ar 10."]),

    Doma("Mazāks dalītājs - lielāks rezultāts",
         "Dalot ar 0,1; 0,01 vai 0,001, komatu pārceļ pa labi, jo mazie "
         "gabali ietilpst daudz reižu.",
         soli=[
             "Saskaiti ciparus aiz komata dalītājā.",
             "Pārcel komatu par tik vietām pa labi.",
             "Ja ciparu nepietiek, beigās pieraksti nulles.",
             "Pārbaudi: skaitlim jākļūst lielākam.",
             "Pārbaudi ar reizināšanu.",
         ],
         pieze="Pamatojums ir daļas pamatīpašība: 4,5 : 0,1 = {4,5|0,1} = "
               "{45|1} = 45. Abus locekļus reizinot ar 10, dalījums "
               "nemainās, bet dalītājs kļūst par veselu skaitli."),

    Slidnis("Jo mazāks dalītājs, jo lielāks rezultāts",
            [{"v": "6 : 10", "teksts": "= 0,6", "josla": 10},
             {"v": "6 : 1", "teksts": "= 6", "josla": 25},
             {"v": "6 : 0,1", "teksts": "= 60", "josla": 50},
             {"v": "6 : 0,01", "teksts": "= 600", "josla": 100}],
            ievads="Spied soli pa solim: dalāmais paliek 6, dalītājs sarūk. "
                   "Rezultāts aug desmitkārt katrā solī."),

    Paraugs("Dali ar 0,01",
            uzd="Cik ir 3,4 : 0,01?",
            soli=[
                ("0,01 - divi cipari aiz komata",
                 "Tik vietas komats pārceļas pa labi."),
                ("3,4 → 34 → 340",
                 "Divi soļi pa labi; beigās pieraksta nulli."),
                ("Pārbaude: 340 · 0,01 = 3,4",
                 "Reizināšana atgriež dalāmo."),
            ],
            atbilde="340"),

    Ievadi("Dali ar 0,1; 0,01 un 0,001", [
        {"jaut": "Cik ir 5 : 0,1?",
         "atb": ["50"], "padoms": "Viena vieta pa labi."},
        {"jaut": "Cik ir 0,8 : 0,1?",
         "atb": ["8"], "padoms": "Viena vieta pa labi."},
        {"jaut": "Cik ir 2,5 : 0,01?",
         "atb": ["250"], "padoms": "Divas vietas pa labi."},
        {"jaut": "Cik ir 0,07 : 0,001?",
         "atb": ["70"], "padoms": "Trīs vietas pa labi."},
        {"jaut": "Cik ir 12 : 0,01?",
         "atb": ["1200"], "padoms": "Divas vietas; beigās nulles."},
        {"jaut": "Cik ir 0,45 : 0,1?",
         "atb": ["4,5", "4.5"], "padoms": "Viena vieta pa labi."},
    ], pamats=4,
        ievads="Cipari aiz komata dalītājā ir soļi pa labi."),

    Pasaule("Cik gabalu sanāks no sloksnes?",
            Kustiba("", [
                {"jaut": "Sloksne ir 5 m, viens gabals 0,1 m. Cik gabalu?",
                 "atb": 50, "beigas": 200, "iedala": 50, "mers": "gabali",
                 "merkis": "gabalu skaits", "objekts": "Griezējs",
                 "padoms": "5 : 0,1 = 50."},
                {"jaut": "Tā pati sloksne, gabals 0,05 m. Cik gabalu?",
                 "atb": 100, "beigas": 200, "iedala": 50, "mers": "gabali",
                 "merkis": "gabalu skaits", "objekts": "Griezējs",
                 "padoms": "5 : 0,05 = 100."},
                {"jaut": "Sloksne 2 m, gabals 0,01 m. Cik gabalu?",
                 "atb": 200, "beigas": 200, "iedala": 50, "mers": "gabali",
                 "merkis": "gabalu skaits", "objekts": "Griezējs",
                 "padoms": "2 : 0,01 = 200."},
                {"jaut": "Sloksne 1,5 m, gabals 0,1 m. Cik gabalu?",
                 "atb": 15, "beigas": 200, "iedala": 50, "mers": "gabali",
                 "merkis": "gabalu skaits", "objekts": "Griezējs",
                 "padoms": "1,5 : 0,1 = 15."},
            ]),
            pavediens="tehnika",
            konteksts="Jo sīkāks gabals, jo vairāk to sanāk - un griezējs "
                      "apstājas tieši pie tā skaitļa, ko aprēķināji.",
            kapec="Dalīšana ar decimāldaļu jautā to pašu: cik reižu "
                  "ietilpst?"),

    Varianti("Uz kuru pusi un kāpēc?", [
        {"jaut": "Dalot ar 0,001, komats pārceļas...",
         "opcijas": ["par trim vietām pa labi",
                     "par trim vietām pa kreisi",
                     "par vienu vietu pa labi", "nekur"],
         "pareizi": 0,
         "padoms": "Trīs cipari aiz komata dalītājā."},
        {"jaut": "Dalīt ar 0,1 ir tas pats, kas...",
         "opcijas": ["reizināt ar 10", "dalīt ar 10",
                     "reizināt ar 0,1", "atņemt 0,1"],
         "pareizi": 0,
         "padoms": "Desmitdaļas vienā veselajā ir desmit."},
        {"jaut": "Kāpēc rezultāts aug?",
         "opcijas": ["Jo dalītājs ir mazāks par 1",
                     "Jo komats pazūd", "Jo cipari mainās",
                     "Tas neaug"],
         "pareizi": 0,
         "padoms": "Sīks gabals ietilpst daudz reižu."},
        {"jaut": "Cik ir 0,9 : 0,1?",
         "opcijas": ["9", "0,09", "0,9", "90"],
         "pareizi": 0,
         "padoms": "Deviņas desmitdaļas."},
    ], pamats=4),

    Kopsavilkums([
        "Dalu ar 0,1; 0,01 un 0,001, pārceļot komatu pa labi.",
        "Paskaidroju, kāpēc rezultāts kļūst lielāks.",
        "Pamatoju likumu ar daļas pamatīpašību.",
        "Saistu dalīšanu ar 0,1 ar reizināšanu ar 10.",
    ]),

    Majas([
        "Izrēķini 0,36 : 0,01 un 7 : 0,001.",
        "Pieraksti, cik 0,1 l glāzes ietilpst 2 l pudelē.",
        "Paskaidro kādam mājās, kāpēc 1 : 0,01 ir 100.",
    ]),
]
