# -*- coding: utf-8 -*-
"""6. klase, 143. stunda: «Kā plānot savu risinājumu?»

Stunda par to, kas notiek pirms pirmās rindas burtnīcā. Skolēns izstāsta
plānu vārdiem - ko darīs vispirms, ko pēc tam -, un tikai tad rēķina. Tā
ir prasme, kuru vēlāk prasa katrs teksta uzdevums.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti)

TEMA = "Kā plānot savu risinājumu?"

MERKIS = ("Pirms aprēķina strukturēti stāstīsim, ko darīsim vispirms un kā "
          "veidosim pierakstu.")

SATURS = [
    Sakums("Plāns aizņem minūti, kļūdas - stundu",
           fakti=["Plāns ir trīs teikumi: ko meklēju, ko darīšu, kā "
                  "pārbaudīšu.",
                  "Plānu izstāsta pirms rēķināšanas, ne pēc tās.",
                  "Ja plānu nevar izstāstīt, uzdevums vēl nav saprasts."]),

    Doma("Trīs teikumi pirms pirmās rindas",
         "Risinājuma plāns sastāv no trim teikumiem: ko meklē, kādā secībā "
         "rēķinās un kā pārbaudīs rezultātu.",
         soli=[
             "Pasaki, ko uzdevums prasa atrast.",
             "Pasaki, kura darbība būs pirmā un kāpēc.",
             "Pasaki, kura būs nākamā.",
             "Pasaki, kā pārbaudīsi atbildi.",
             "Tikai tad sāc rakstīt risinājumu.",
         ],
         pieze="Plānā nav skaitļu - tajā ir darbību nosaukumi. «Vispirms "
               "pārrakstīšu atņemšanu par saskaitīšanu, tad sagrupēšu "
               "saskaitāmos» ir labs plāns."),

    Paraugs("Izstāsti plānu",
            uzd="Kā risināsi −7 + 12 − (−3) + (−5)?",
            soli=[
                ("Meklēju izteiksmes vērtību",
                 "Pirmais teikums."),
                ("Vispirms pārrakstīšu atņemšanu par saskaitīšanu",
                 "Otrais teikums."),
                ("Tad sagrupēšu pozitīvos un negatīvos",
                 "Trešais teikums."),
                ("Pārbaudīšu, rēķinot no kreisās uz labo",
                 "Ceturtais teikums."),
                ("−7 + 12 + 3 + (−5) = 15 + (−12) = 3",
                 "Tikai tagad rēķins."),
            ],
            atbilde="3"),

    Ievadi("Izrēķini pēc plāna", [
        {"jaut": "Cik ir −7 + 12 − (−3) + (−5)?",
         "atb": ["3"], "padoms": "15 un −12."},
        {"jaut": "Cik ir 8 − (−4) − 15?",
         "atb": ["-3", "−3"], "padoms": "12 − 15."},
        {"jaut": "Cik ir −2,5 + 4 − 1,5?",
         "atb": ["0"], "padoms": "4 − 4."},
        {"jaut": "Cik ir −{1|2} + {1|4} + {1|4}?",
         "atb": ["0"], "padoms": "Kopsaucējs 4."},
        {"jaut": "Cik ir (−6 + 10) − (2 − 7)?",
         "atb": ["9"], "padoms": "4 − (−5)."},
        {"jaut": "Cik ir −3 − (−3) + (−3)?",
         "atb": ["-3", "−3"], "padoms": "Pirmie divi dod nulli."},
    ], pamats=4,
        ievads="Pirms katras atbildes pasaki sev, kura darbība būs pirmā."),

    Petijums("Izstāsti plānu soļabiedram",
             vajag="trīs uzdevumi un soļabiedrs",
             soli=[
                 "Izvēlieties trīs uzdevumus ar vairākām darbībām.",
                 "Katram izstāstiet plānu vārdiem, neko nerēķinot.",
                 "Soļabiedrs pieraksta, vai plāns bija saprotams.",
                 "Tikai tad atrisiniet uzdevumus.",
                 "Salīdziniet, vai risinājums sakrita ar plānu.",
             ],
             secinajums="Ja plāns bija skaidrs, risinājums parasti ir īsāks "
                        "un bez atgriešanās atpakaļ."),

    Varianti("Kurš plāns ir labs?", [
        {"jaut": "Kas plānā ir obligāts?",
         "opcijas": ["Darbību secība", "Visi skaitļi",
                     "Atbilde", "Zīmējums"],
         "pareizi": 0,
         "padoms": "Plāns ir par darbībām."},
        {"jaut": "Kad izstāsta plānu?",
         "opcijas": ["Pirms rēķināšanas", "Pēc rēķināšanas",
                     "Rēķināšanas laikā", "Nekad"],
         "pareizi": 0,
         "padoms": "Tas ir plāns, ne pārskats."},
        {"jaut": "Izteiksmē ar iekavām plāna pirmais solis ir...",
         "opcijas": ["izrēķināt iekavas", "sagrupēt saskaitāmos",
                     "pārrakstīt atņemšanu", "pārbaudīt atbildi"],
         "pareizi": 0,
         "padoms": "Iekavas vienmēr pirmās."},
        {"jaut": "Ja plānu nevar izstāstīt, tas nozīmē...",
         "opcijas": ["uzdevums vēl nav saprasts",
                     "uzdevums ir par grūtu",
                     "plāns nav vajadzīgs", "jāsāk rēķināt"],
         "pareizi": 0,
         "padoms": "Saprašana nāk pirms rēķina."},
    ], pamats=4),

    Pasaule("Kā plānot mēneša aprēķinu?",
            Ievadi("", [
                {"jaut": "Ienākumi 320 €, izdevumi 145 € un 88 €. Cik eiro "
                         "ir izdevumi kopā?",
                 "atb": ["233"], "padoms": "145 + 88."},
                {"jaut": "Cik eiro paliek?",
                 "atb": ["87"], "padoms": "320 − 233."},
                {"jaut": "Ja pienāktu vēl rēķins 120 €, cik eiro būtu?",
                 "atb": ["-33", "−33"], "padoms": "87 − 120."},
                {"jaut": "Cik eiro trūktu, lai to samaksātu?",
                 "atb": ["33"], "padoms": "Modulis."},
            ]),
            pavediens="veikals",
            konteksts="Mēneša aprēķinā plāns ir vienkāršs: vispirms visi "
                      "izdevumi, tad starpība - un tikai tad secinājums.",
            kapec="Plāns pasaka, kura darbība ir pirmā, pirms skaitļi to "
                  "apjuko."),

    Kopsavilkums([
        "Izstāstu risinājuma plānu pirms rēķināšanas.",
        "Nosaucu, kura darbība būs pirmā un kāpēc.",
        "Pasaku, kā pārbaudīšu atbildi.",
        "Rakstu risinājumu tādā secībā, kā plānoju.",
    ]),

    Majas([
        "Izvēlies uzdevumu ar trim darbībām un izstāsti tā plānu kādam "
        "mājās.",
        "Tikai tad atrisini to.",
        "Pieraksti, vai risinājums sakrita ar plānu.",
    ]),
]
