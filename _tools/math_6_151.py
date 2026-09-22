# -*- coding: utf-8 -*-
"""6. klase, 151. stunda: «Kā kāpināt negatīvu skaitli?»

Kāpināšana ir vienādu reizinātāju reizinājums, tāpēc zīmi nosaka kāpinātājs:
pāra pakāpe dod plusu, nepāra - mīnusu. Te parādās arī pieraksta smalkums:
(−3) kvadrātā un −3 kvadrātā nav viens un tas pats.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti)

TEMA = "Kā kāpināt negatīvu skaitli?"

MERKIS = ("Kāpināsim negatīvus skaitļus un noteiksim rezultāta zīmi pēc "
          "kāpinātāja.")

SATURS = [
    Sakums("Iekavas te maina visu",
           fakti=["(−3) otrajā pakāpē ir (−3) · (−3) = 9.",
                  "−3 otrajā pakāpē nozīmē −(3 · 3) = −9.",
                  "Iekavas pasaka, vai kāpina arī zīmi."]),

    Doma("Pāra pakāpe - pluss, nepāra - mīnuss",
         "Kāpinot negatīvu skaitli, rezultāta zīmi nosaka kāpinātājs: pāra "
         "pakāpe dod pozitīvu rezultātu, nepāra - negatīvu.",
         soli=[
             "Paskaties, vai skaitlis ar zīmi ir iekavās.",
             "Ja ir, kāpini arī zīmi.",
             "Saskaiti, cik reizinātāju būs - tas ir kāpinātājs.",
             "Pāra kāpinātājs dod plusu, nepāra - mīnusu.",
             "Kāpini moduli un pieliec zīmi.",
         ],
         pieze="Bez iekavām mīnuss paliek ārpusē: −3 otrajā pakāpē ir "
               "−(3 · 3) = −9. Tāpēc negatīvu skaitli kāpinot vienmēr raksta "
               "iekavas."),

    Slidnis("Pakāpes maina zīmi pēc kārtas",
            [{"v": "(−2) pirmajā", "teksts": "= −2", "josla": 12},
             {"v": "(−2) otrajā", "teksts": "= 4", "josla": 25},
             {"v": "(−2) trešajā", "teksts": "= −8", "josla": 50},
             {"v": "(−2) ceturtajā", "teksts": "= 16", "josla": 100}],
            ievads="Spied soli pa solim: modulis aug, bet zīme mainās katrā "
                   "solī - pāra pakāpēs pluss, nepāra pakāpēs mīnuss."),

    Paraugs("Divi pieraksti, divas atbildes",
            uzd="Cik ir (−3) otrajā pakāpē un −3 otrajā pakāpē?",
            soli=[
                ("(−3) otrajā: skaitlis ar zīmi ir iekavās",
                 "(−3) · (−3)."),
                ("Divi mīnusi - pāra skaits",
                 "Rezultāts 9."),
                ("−3 otrajā: mīnuss ir ārpus kāpināšanas",
                 "−(3 · 3)."),
                ("= −9",
                 "Zīme paliek ārpusē."),
            ],
            atbilde="9 un −9"),

    Ievadi("Kāpini negatīvu skaitli", [
        {"jaut": "Cik ir (−3) otrajā pakāpē?",
         "atb": ["9"], "padoms": "Divi mīnusi."},
        {"jaut": "Cik ir (−3) trešajā pakāpē?",
         "atb": ["-27", "−27"], "padoms": "Trīs mīnusi."},
        {"jaut": "Cik ir (−2) ceturtajā pakāpē?",
         "atb": ["16"], "padoms": "Četri mīnusi."},
        {"jaut": "Cik ir (−1) piektajā pakāpē?",
         "atb": ["-1", "−1"], "padoms": "Pieci mīnusi."},
        {"jaut": "Cik ir −3 otrajā pakāpē, ja mīnuss ir ārpus iekavām?",
         "atb": ["-9", "−9"], "padoms": "−(3 · 3)."},
        {"jaut": "Cik ir (−5) otrajā pakāpē?",
         "atb": ["25"], "padoms": "Divi mīnusi."},
    ], pamats=4,
        ievads="Vispirms paskaties, vai zīme ir iekavās."),

    Varianti("Kāda būs zīme?", [
        {"jaut": "Negatīvs skaitlis pāra pakāpē dod...",
         "opcijas": ["pozitīvu rezultātu", "negatīvu rezultātu",
                     "nulli", "nevar zināt"],
         "pareizi": 0,
         "padoms": "Pāra skaits mīnusu."},
        {"jaut": "Negatīvs skaitlis nepāra pakāpē dod...",
         "opcijas": ["negatīvu rezultātu", "pozitīvu rezultātu",
                     "nulli", "nevar zināt"],
         "pareizi": 0,
         "padoms": "Nepāra skaits mīnusu."},
        {"jaut": "(−4) otrajā pakāpē ir...",
         "opcijas": ["16", "−16", "8", "−8"],
         "pareizi": 0,
         "padoms": "Divi mīnusi."},
        {"jaut": "Kāpēc negatīvu skaitli kāpinot raksta iekavas?",
         "opcijas": ["Lai kāpinātu arī zīmi",
                     "Lai izteiksme būtu garāka",
                     "Tā prasa likums", "Nav iemesla"],
         "pareizi": 0,
         "padoms": "Bez iekavām mīnuss paliek ārpusē."},
    ], pamats=4),

    Pasaule("Cik paliek pēc katras kārtas?",
            Ievadi("", [
                {"jaut": "Katrā kārtā vērtība mainās ar reizinātāju −2. Cik "
                         "tā ir pēc divām kārtām, ja sākumā bija 1?",
                 "atb": ["4"], "padoms": "(−2) otrajā pakāpē."},
                {"jaut": "Cik tā ir pēc trim kārtām?",
                 "atb": ["-8", "−8"], "padoms": "(−2) trešajā pakāpē."},
                {"jaut": "Cik tā ir pēc četrām kārtām?",
                 "atb": ["16"], "padoms": "(−2) ceturtajā pakāpē."},
                {"jaut": "Pēc kurām kārtām vērtība ir pozitīva - pāra vai "
                         "nepāra? Raksti «pāra» vai «nepāra».",
                 "atb": ["pāra"], "padoms": "Pāra skaits mīnusu."},
            ]),
            pavediens="dati",
            konteksts="Programmā koeficients −2 katrā kārtā apgriež zīmi un "
                      "dubulto vērtību.",
            kapec="Zīmi nosaka kārtu skaita pāra vai nepāra raksturs."),

    Kopsavilkums([
        "Kāpinu negatīvus skaitļus.",
        "Nosaku zīmi pēc kāpinātāja: pāra dod plusu, nepāra - mīnusu.",
        "Atšķiru pierakstu ar iekavām no pieraksta bez tām.",
        "Kāpinu moduli un pielieku zīmi.",
    ]),

    Majas([
        "Izrēķini (−2) otrajā, trešajā un ceturtajā pakāpē.",
        "Izrēķini −2 otrajā pakāpē, ja mīnuss ir ārpus iekavām.",
        "Pieraksti, ar ko abas atbildes atšķiras.",
    ]),
]
