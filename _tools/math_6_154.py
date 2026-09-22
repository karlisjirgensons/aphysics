# -*- coding: utf-8 -*-
"""6. klase, 154. stunda: «Kas ir racionāls skaitlis?»

Jauns vārds jau zināmām lietām. Racionāls skaitlis ir tas, kuru var uzrakstīt
kā daļu ar veseliem locekļiem - un izrādās, ka visi šogad lietotie skaitļi
tādi ir.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, venna)

TEMA = "Kas ir racionāls skaitlis?"

MERKIS = ("Iemācīsimies, kas ir racionāls skaitlis, un pārbaudīsim, vai "
          "skaitlis tāds ir.")

SATURS = [
    Sakums("Viens vārds visiem šī gada skaitļiem",
           zimejums=venna([1, 2, 3], ["0,5", "−0,7"], [0, -5],
                          ("naturālie", "daļskaitļi")),
           paraksts="Visi šie skaitļi ir racionāli: katru var uzrakstīt kā "
                    "daļu ar veseliem locekļiem.",
           fakti=["Racionāls skaitlis ir daļa, kuras abi locekļi ir veseli.",
                  "Saucējs nedrīkst būt nulle.",
                  "Arī vesels skaitlis un decimāldaļa ir racionāli."]),

    Doma("Ja var uzrakstīt kā daļu - tas ir racionāls",
         "Skaitlis ir racionāls, ja to var pierakstīt kā daļu, kuras "
         "skaitītājs ir vesels skaitlis un saucējs - vesels skaitlis, kas "
         "nav nulle.",
         soli=[
             "Pamēģini skaitli uzrakstīt kā daļu.",
             "Veselam skaitlim saucējs ir 1.",
             "Decimāldaļai saucējs ir 10, 100 vai 1000.",
             "Pārbaudi, vai abi locekļi ir veseli.",
             "Ja izdevās, skaitlis ir racionāls.",
         ],
         pieze="Negatīvs skaitlis arī ir racionāls: −5 = {−5|1}, bet "
               "−0,7 = {−7|10}. Mīnuss neko nemaina - svarīgi ir tikai tas, "
               "vai locekļi ir veseli."),

    Paraugs("Pārbaudi, vai skaitlis ir racionāls",
            uzd="Vai 7; −0,7 un {2|3} ir racionāli skaitļi?",
            soli=[
                ("7 = {7|1}",
                 "Abi locekļi veseli - racionāls."),
                ("−0,7 = {−7|10}",
                 "Arī abi veseli - racionāls."),
                ("{2|3} jau ir daļa",
                 "Abi locekļi veseli - racionāls."),
                ("Visi trīs ir racionāli",
                 "Katru var pierakstīt kā daļu."),
            ],
            atbilde="visi trīs ir racionāli"),

    Ievadi("Uzraksti kā daļu", [
        {"jaut": "Kāds ir skaitļa 7 saucējs, ja to raksta kā daļu?",
         "atb": ["1"], "padoms": "{7|1}."},
        {"jaut": "Kāds ir skaitļa 0,7 saucējs, ja to raksta kā daļu?",
         "atb": ["10"], "padoms": "{7|10}."},
        {"jaut": "Kāds ir skaitļa 0,25 saucējs, ja to raksta kā daļu?",
         "atb": ["100"], "padoms": "{25|100}."},
        {"jaut": "Kāds ir skaitļa −3 skaitītājs, ja saucējs ir 1?",
         "atb": ["-3", "−3"], "padoms": "{−3|1}."},
        {"jaut": "Vai saucējs drīkst būt nulle? Raksti «jā» vai «nē».",
         "atb": ["nē", "ne"], "padoms": "Ar nulli dalīt nedrīkst."},
        {"jaut": "Cik ir {25|100} saīsinātā veidā? Atbildi raksti kā a/b.",
         "atb": ["1/4"], "padoms": "Dala ar 25."},
    ], pamats=4),

    Varianti("Vai tas ir racionāls?", [
        {"jaut": "Racionāls skaitlis ir tas, kuru var uzrakstīt kā...",
         "opcijas": ["daļu ar veseliem locekļiem", "veselu skaitli",
                     "decimāldaļu", "pozitīvu skaitli"],
         "pareizi": 0,
         "padoms": "Abi locekļi veseli."},
        {"jaut": "Vai −5 ir racionāls skaitlis?",
         "opcijas": ["Jā, tas ir {−5|1}", "Nē, tas ir negatīvs",
                     "Nē, tas nav daļa", "Tikai dažreiz"],
         "pareizi": 0,
         "padoms": "Saucējs var būt 1."},
        {"jaut": "Kas nedrīkst būt saucējā?",
         "opcijas": ["Nulle", "Negatīvs skaitlis",
                     "Liels skaitlis", "Viens"],
         "pareizi": 0,
         "padoms": "Ar nulli dalīt nedrīkst."},
        {"jaut": "Vai 0 ir racionāls skaitlis?",
         "opcijas": ["Jā, tas ir {0|1}", "Nē", "Tikai kā daļa",
                     "Nevar zināt"],
         "pareizi": 0,
         "padoms": "Skaitītājs var būt nulle."},
    ], pamats=4),

    Pasaule("Kādus skaitļus lieto mērījumos?",
            Ievadi("", [
                {"jaut": "Temperatūra −2,5 °C. Kāds ir saucējs, ja to raksta "
                         "kā daļu?",
                 "atb": ["10"], "padoms": "{−25|10}."},
                {"jaut": "Masa 0,125 kg. Kāds ir saucējs?",
                 "atb": ["1000"], "padoms": "{125|1000}."},
                {"jaut": "Cik ir {125|1000} saīsinātā veidā? Atbildi raksti "
                         "kā a/b.",
                 "atb": ["1/8"], "padoms": "Dala ar 125."},
                {"jaut": "Dziļums −40 m. Kāds ir saucējs, ja to raksta kā "
                         "daļu?",
                 "atb": ["1"], "padoms": "Vesels skaitlis."},
            ]),
            pavediens="planeta",
            konteksts="Katrs mērījums, ko var pierakstīt ar ciparu un "
                      "komatu, ir racionāls skaitlis.",
            kapec="Racionālie skaitļi ir viss, ar ko šogad rēķinājām."),

    Kopsavilkums([
        "Zinu, kas ir racionāls skaitlis.",
        "Pārbaudu, vai skaitli var uzrakstīt kā daļu ar veseliem locekļiem.",
        "Zinu, ka saucējs nedrīkst būt nulle.",
        "Atpazīstu, ka veselie un decimāldaļas arī ir racionāli.",
    ]),

    Majas([
        "Uzraksti kā daļu skaitļus 9; −4; 0,3 un 1,25.",
        "Pieraksti, kāds ir katra saucējs.",
        "Paskaidro, kāpēc visi šie skaitļi ir racionāli.",
    ]),
]
