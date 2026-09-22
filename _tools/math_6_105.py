# -*- coding: utf-8 -*-
"""6. klase, 105. stunda: «Kurš skaitlis ir tieši vidū?»

Jauns mikrotemats par sakarībām starp skaitļiem. Vidus punkts ir pirmais
uzdevums, kurā negatīvi skaitļi jālieto rēķinā, nevis tikai jāsalīdzina - un
uz taisnes atbildi var arī vienkārši saskaitīt.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Kustiba, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, taisne)

TEMA = "Kurš skaitlis ir tieši vidū?"

MERKIS = ("Iemācīsimies noteikt skaitli, kas uz skaitļu taisnes atrodas vidū "
          "starp diviem dotajiem.")

SATURS = [
    Sakums("Vidus ir vienādā attālumā no abiem",
           zimejums=taisne(-8, 2, 2, [(-6, "−6"), (-2, "−2"), (-4, "vidus")]),
           paraksts="No −4 līdz −6 ir divi soļi un no −4 līdz −2 arī divi - "
                    "tāpēc −4 ir tieši vidū.",
           fakti=["Vidus punkts ir vienādā attālumā no abiem galiem.",
                  "To atrod, saskaitot abus skaitļus un dalot ar 2.",
                  "Uz taisnes to var arī vienkārši saskaitīt."]),

    Doma("Saskaiti abus un izdali ar diviem",
         "Skaitlis, kas atrodas tieši vidū starp diviem dotajiem, ir to "
         "summa, dalīta ar 2.",
         soli=[
             "Pieraksti abus skaitļus.",
             "Saskaiti tos, ievērojot zīmes.",
             "Izdali summu ar 2.",
             "Pārbaudi uz taisnes: vai attālumi līdz abiem galiem sakrīt?",
             "Ja skaitļi ir tuvu, vidu var arī vienkārši saskaitīt.",
         ],
         pieze="Vidus starp −6 un −2: summa ir −8, un −8 : 2 = −4. Ja "
               "skaitļiem ir dažādas zīmes, vidus var iznākt arī nulle: "
               "starp −5 un 5 vidū ir tieši 0."),

    Paraugs("Atrodi vidu",
            uzd="Kurš skaitlis ir tieši vidū starp −6 un −2?",
            soli=[
                ("−6 + (−2) = −8",
                 "Summa ar zīmēm."),
                ("−8 : 2 = −4",
                 "Vidus punkts."),
                ("No −4 līdz −6 ir 2 soļi",
                 "Pārbaude pa kreisi."),
                ("No −4 līdz −2 arī 2 soļi",
                 "Pārbaude pa labi."),
            ],
            atbilde="−4"),

    Ievadi("Kurš ir vidū?", [
        {"jaut": "Kurš skaitlis ir vidū starp −6 un −2?",
         "atb": ["-4", "−4"], "padoms": "Summa dalīta ar 2."},
        {"jaut": "Kurš skaitlis ir vidū starp −5 un 5?",
         "atb": ["0"], "padoms": "Simetriski pret nulli."},
        {"jaut": "Kurš skaitlis ir vidū starp −10 un 0?",
         "atb": ["-5", "−5"], "padoms": "−10 : 2."},
        {"jaut": "Kurš skaitlis ir vidū starp −8 un −3?",
         "atb": ["-5,5", "−5,5", "-5.5"], "padoms": "−11 : 2."},
        {"jaut": "Kurš skaitlis ir vidū starp −3 un 7?",
         "atb": ["2"], "padoms": "4 : 2."},
        {"jaut": "Kurš skaitlis ir vidū starp −1 un −2?",
         "atb": ["-1,5", "−1,5", "-1.5"], "padoms": "−3 : 2."},
    ], pamats=4),

    Pasaule("Kur apstāties pusceļā?",
            Kustiba("", [
                {"jaut": "Stacija ir −8 stāvā, izeja - 2. stāvā. Kurā stāvā "
                         "ir pusceļš?",
                 "atb": -3, "sakums": -10, "beigas": 10, "iedala": 5,
                 "mers": "stāvs", "merkis": "pusceļš", "objekts": "Lifts",
                 "padoms": "(−8 + 2) : 2."},
                {"jaut": "No −10 līdz 0 - kurā stāvā ir pusceļš?",
                 "atb": -5, "sakums": -10, "beigas": 10, "iedala": 5,
                 "mers": "stāvs", "merkis": "pusceļš", "objekts": "Lifts",
                 "padoms": "−10 : 2."},
                {"jaut": "No −6 līdz 6 - kurā stāvā ir pusceļš?",
                 "atb": 0, "sakums": -10, "beigas": 10, "iedala": 5,
                 "mers": "stāvs", "merkis": "pusceļš", "objekts": "Lifts",
                 "padoms": "Simetriski pret nulli."},
                {"jaut": "No −4 līdz 10 - kurā stāvā ir pusceļš?",
                 "atb": 3, "sakums": -10, "beigas": 10, "iedala": 5,
                 "mers": "stāvs", "merkis": "pusceļš", "objekts": "Lifts",
                 "padoms": "6 : 2."},
            ]),
            pavediens="maja",
            konteksts="Lifts apstājas pusceļā starp diviem stāviem - un "
                      "pagrabstāvi te ir tikpat īsti kā pārējie.",
            kapec="Vidus punkts ir summa, dalīta ar 2, arī ar zīmēm."),

    Varianti("Kā atrast vidu?", [
        {"jaut": "Vidus punktu starp diviem skaitļiem atrod...",
         "opcijas": ["saskaitot un dalot ar 2", "atņemot",
                     "reizinot", "dalot vienu ar otru"],
         "pareizi": 0,
         "padoms": "Vidējā vērtība."},
        {"jaut": "Vidus starp −7 un 7 ir...",
         "opcijas": ["0", "7", "−7", "14"],
         "pareizi": 0,
         "padoms": "Simetriski pret nulli."},
        {"jaut": "Ja vidus starp diviem skaitļiem ir 0, tad skaitļi ir...",
         "opcijas": ["pretēji", "vienādi", "abi pozitīvi", "abi negatīvi"],
         "pareizi": 0,
         "padoms": "To summa ir nulle."},
        {"jaut": "Vidus starp −9 un −1 ir...",
         "opcijas": ["−5", "−4", "−10", "5"],
         "pareizi": 0,
         "padoms": "−10 : 2."},
    ], pamats=4),

    Zimejums("Vidus ir vienādā attālumā",
             taisne(-10, 2, 2, [(-9, "−9"), (-5, "vidus"), (-1, "−1")]),
             paskaidro="No −5 līdz abiem galiem ir četri soļi. Tieši tāpēc "
                       "−5 ir vidus punkts.",
             ievads="Vidu vienmēr var pārbaudīt ar soļiem."),

    Kopsavilkums([
        "Atrodu skaitli, kas ir tieši vidū starp diviem dotajiem.",
        "Rēķinu to kā summu, dalītu ar 2.",
        "Pārbaudu rezultātu ar attālumiem uz skaitļu taisnes.",
        "Zinu, ka pretēju skaitļu vidus ir nulle.",
    ]),

    Majas([
        "Atrodi vidus punktu starp −12 un −4.",
        "Atrodi vidus punktu starp −7 un 3.",
        "Izdomā divus skaitļus, kuru vidus ir −2.",
    ]),
]
