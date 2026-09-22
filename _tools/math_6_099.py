# -*- coding: utf-8 -*-
"""6. klase, 99. stunda: «Kas ir pretējais skaitlis?»

Viens jēdziens, kas vēlāk atrisinās visu atņemšanu. Pretējais skaitlis ir
tas pats attālums otrā pusē no nulles - un pieraksts ar divām zīmēm te tiek
izspēlēts atsevišķi, jo tieši tas vēlāk mulsina.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, taisne)

TEMA = "Kas ir pretējais skaitlis?"

MERKIS = ("Iemācīsimies noteikt un pierakstīt skaitlim pretējo skaitli, arī "
          "pierakstā ar divām zīmēm.")

SATURS = [
    Sakums("Vienāds attālums, pretējs virziens",
           zimejums=taisne(-6, 6, 2, [(-4, "−4"), (4, "4")]),
           paraksts="−4 un 4 atrodas vienādā attālumā no nulles, bet "
                    "dažādās pusēs.",
           fakti=["Pretējo skaitli iegūst, mainot zīmi.",
                  "Skaitļa un tā pretējā skaitļa summa ir nulle.",
                  "Nullei pretējais skaitlis ir pati nulle."]),

    Doma("Maini zīmi, attālumu atstāj",
         "Pretējais skaitlis ir tas pats skaitlis ar pretēju zīmi; abi "
         "atrodas vienādā attālumā no nulles.",
         soli=[
             "Pieraksti doto skaitli.",
             "Maini tā zīmi uz pretējo.",
             "Pārbaudi uz skaitļu taisnes: vai attālums no nulles sakrīt?",
             "Pārbaudi ar saskaitīšanu: summai jābūt nullei.",
             "Ja skaitļa priekšā ir divas zīmes, vienkāršo tās.",
         ],
         pieze="Divas zīmes viena aiz otras: −(−4) nozīmē «skaitlim −4 "
               "pretējais», un tas ir 4. Divi mīnusi dod plusu, jo pretējā "
               "skaitļa pretējais skaitlis ir tas pats skaitlis."),

    Paraugs("Pieraksts ar divām zīmēm",
            uzd="Cik ir −(−7) un kāds skaitlis ir pretējs skaitlim 2,5?",
            soli=[
                ("−(−7) nozīmē «skaitlim −7 pretējais»",
                 "Iekavās ir pats skaitlis."),
                ("Skaitlim −7 pretējais ir 7",
                 "Maina zīmi."),
                ("Tātad −(−7) = 7",
                 "Divi mīnusi dod plusu."),
                ("Skaitlim 2,5 pretējais ir −2,5",
                 "Arī daļskaitļiem."),
            ],
            atbilde="7 un −2,5"),

    Ievadi("Uzraksti pretējo skaitli", [
        {"jaut": "Kāds skaitlis ir pretējs skaitlim 6?",
         "atb": ["-6", "−6"], "padoms": "Maini zīmi."},
        {"jaut": "Kāds skaitlis ir pretējs skaitlim −9?",
         "atb": ["9"], "padoms": "Mīnuss kļūst par plusu."},
        {"jaut": "Cik ir −(−7)?",
         "atb": ["7"], "padoms": "Divi mīnusi."},
        {"jaut": "Kāds skaitlis ir pretējs skaitlim 0?",
         "atb": ["0"], "padoms": "Nulle ir pati sev pretēja."},
        {"jaut": "Kāds skaitlis ir pretējs skaitlim −2,5?",
         "atb": ["2,5", "2.5"], "padoms": "Arī decimāldaļām."},
        {"jaut": "Cik ir −(−(−3))?",
         "atb": ["-3", "−3"], "padoms": "Trīs mīnusi - nepāra skaits."},
    ], pamats=4),

    Varianti("Vai tie ir pretēji?", [
        {"jaut": "Vai 5 un −5 ir pretēji skaitļi?",
         "opcijas": ["Jā, to summa ir nulle", "Nē, tie ir dažādi",
                     "Jā, jo abi ir pieci", "Nē, 5 ir lielāks"],
         "pareizi": 0,
         "padoms": "Vienāds attālums no nulles."},
        {"jaut": "−(−12) ir vienāds ar...",
         "opcijas": ["12", "−12", "0", "24"],
         "pareizi": 0,
         "padoms": "Divi mīnusi."},
        {"jaut": "Kāda ir skaitļa un tā pretējā skaitļa summa?",
         "opcijas": ["0", "1", "Divkāršs skaitlis", "Atkarīgs no skaitļa"],
         "pareizi": 0,
         "padoms": "Tie izlīdzinās."},
        {"jaut": "Kuram skaitlim pretējais ir tas pats skaitlis?",
         "opcijas": ["0", "1", "−1", "Nevienam"],
         "pareizi": 0,
         "padoms": "Nullei nav virziena."},
    ], pamats=4),

    Pasaule("Kas izlīdzina kontu?",
            Ievadi("", [
                {"jaut": "Kontā ir −40 €. Cik eiro jāiemaksā, lai būtu "
                         "nulle?",
                 "atb": ["40"], "padoms": "Pretējais skaitlis."},
                {"jaut": "Kontā ir 25 €, un jāsamaksā 25 €. Cik paliks?",
                 "atb": ["0"], "padoms": "Skaitlis un tā pretējais."},
                {"jaut": "Lifts nolaidās par 3 stāviem uz −3. Par cik "
                         "stāviem jāpaceļas, lai būtu nulles stāvā?",
                 "atb": ["3"], "padoms": "Tas pats attālums."},
                {"jaut": "Temperatūra ir −8 °C. Par cik grādiem "
                         "jāpaaugstinās, lai būtu 0 °C?",
                 "atb": ["8"], "padoms": "Attālums līdz nullei."},
            ]),
            pavediens="veikals",
            konteksts="Kontā pretējais skaitlis ir tieši tā summa, kas "
                      "vajadzīga, lai parāds pazustu.",
            kapec="Skaitlis un tā pretējais kopā vienmēr dod nulli."),

    Zimejums("Trīs pretēju skaitļu pāri",
             taisne(-8, 8, 2, [(-6, "−6"), (6, "6"), (-2, "−2"), (2, "2")]),
             paskaidro="Katrs pāris ir vienādā attālumā no nulles - tikai "
                       "dažādās pusēs.",
             ievads="Uz taisnes pretējie skaitļi vienmēr ir simetriski."),

    Kopsavilkums([
        "Nosaku un pierakstu skaitlim pretējo skaitli.",
        "Zinu, ka skaitļa un tā pretējā skaitļa summa ir nulle.",
        "Vienkāršoju pierakstu ar divām zīmēm.",
        "Zinu, ka nullei pretējais skaitlis ir pati nulle.",
    ]),

    Majas([
        "Uzraksti pretējos skaitļus skaitļiem 15, −8, 0 un 3,5.",
        "Izrēķini −(−(−10)).",
        "Uzzīmē skaitļu taisni un atzīmē trīs pretēju skaitļu pārus.",
    ]),
]
