# -*- coding: utf-8 -*-
"""3. klase, 139. stunda: «Kādā secībā saskaitīt vairākus skaitļus?»

Saskaitīšanas maiņas un grupēšanas īpašība praksē: saskaitāmos drīkst
pārkārtot, un gudrs kārtojums pārvērš grūtu rēķinu vieglā. Tā ir pirmā reize,
kad skolēns rēķinu *plāno*, nevis vienkārši izpilda.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         restis)

TEMA = "Kādā secībā saskaitīt vairākus skaitļus?"

MERKIS = ("Saskaitīsim 2-4 divciparu skaitļus, izvēloties izdevīgu secību.")

SATURS = [
    Sakums("Kā saskaitīt 27 + 45 + 73 vienā mirklī?",
           zimejums=restis([["27", "+", "45", "+", "73"],
                            ["27", "+", "73", "+", "45"],
                            ["100", "+", "45", "=", "145"]],
                           "pārkārtots rēķins"),
           paraksts="27 un 73 kopā dod apaļu simtu.",
           fakti=["Saskaitāmos drīkst pārkārtot - summa nemainās.",
                  "Gudrs kārtojums pārvērš grūtu rēķinu vieglā."]),

    Doma("Meklē pārus, kas dod apaļu skaitli",
         "Saskaitāmos drīkst mainīt vietām, tāpēc vispirms saliec kopā tos, "
         "kas dod apaļu desmitu vai simtu.",
         soli=[
             "Paskaties uz visiem saskaitāmajiem.",
             "Atrodi pāri, kura vieni kopā dod 10 vai 0.",
             "Saskaiti šo pāri vispirms.",
             "Pieskaiti pārējos.",
         ],
         pieze="Tas strādā tikai saskaitīšanai un reizināšanai. Atņemšanā "
               "secību mainīt nedrīkst: 10 − 3 nav 3 − 10."),

    Paraugs("Kā ērtāk saskaitīt 27 + 45 + 73?",
            uzd="Izrēķini 27 + 45 + 73, izvēloties izdevīgu secību.",
            soli=[
                ("27 + 73 = 100",
                 "Šie divi dod apaļu simtu."),
                ("100 + 45 = 145",
                 "Pieskaita atlikušo."),
                ("Summa ir 145",
                 "Tā pati, kas rēķinot pēc kārtas."),
            ],
            atbilde="145"),

    Petijums("Atrodi ērtos pārus",
             vajag="lapa un zīmulis",
             soli=[
                 "Uzraksti sešus divciparu skaitļus.",
                 "Atrodi pārus, kuru vieni kopā dod 10.",
                 "Saskaiti šos pārus vispirms.",
                 "Saskaiti visu un pārbaudi, rēķinot pēc kārtas.",
             ],
             secinajums="Abās reizēs summa ir tā pati - bet ar pāriem "
                        "rēķināt ir daudz ātrāk."),

    Ievadi("Izvēlies ērtu secību", [
        {"jaut": "27 + 45 + 73 = ?", "atb": ["145"], "padoms": "27 + 73."},
        {"jaut": "38 + 26 + 62 = ?", "atb": ["126"], "padoms": "38 + 62."},
        {"jaut": "19 + 57 + 41 = ?", "atb": ["117"], "padoms": "19 + 41."},
        {"jaut": "25 + 36 + 75 = ?", "atb": ["136"], "padoms": "25 + 75."},
        {"jaut": "48 + 17 + 52 + 3 = ?", "atb": ["120"],
         "padoms": "48 + 52 un 17 + 3."},
        {"jaut": "64 + 29 + 36 + 11 = ?", "atb": ["140"],
         "padoms": "64 + 36 un 29 + 11."},
    ], pamats=4),

    Zimejums("Pāri, kas dod apaļu skaitli",
             restis([["27 + 73", "= 100"],
                     ["38 + 62", "= 100"],
                     ["19 + 41", "= 60"]],
                    "meklē tieši tādus pārus"),
             paskaidro="Pārī vienu cipari kopā dod 10 - tieši tāpēc summa "
                       "iznāk apaļa.",
             ievads="Trīs ērti pāri."),

    Varianti("Kurš pāris ir ērtākais?", [
        {"jaut": "Kurš pāris dod apaļu simtu?",
         "opcijas": ["27 + 73", "27 + 45", "45 + 73", "27 + 27"],
         "pareizi": 0, "padoms": "7 + 3 = 10."},
        {"jaut": "Vai drīkst mainīt saskaitāmo secību?",
         "opcijas": ["Jā, summa nemainās", "Nē", "Tikai diviem",
                     "Tikai apaļiem skaitļiem"],
         "pareizi": 0, "padoms": "Saskaitīšanas maiņas īpašība."},
        {"jaut": "Vai drīkst mainīt secību atņemšanā?",
         "opcijas": ["Nē", "Jā", "Tikai lieliem skaitļiem", "Vienmēr"],
         "pareizi": 0, "padoms": "10 − 3 un 3 − 10 nav vienādi."},
        {"jaut": "Cik ir 15 + 28 + 85?",
         "opcijas": ["128", "118", "138", "125"],
         "pareizi": 0, "padoms": "15 + 85 = 100."},
    ], pamats=4),

    Pasaule("Cik kilometru ir visā ceļojumā?",
            Ievadi("", [
                {"jaut": "Posmi 27, 45 un 73 km. Cik kopā?", "atb": ["145"],
                 "padoms": "27 + 73 = 100."},
                {"jaut": "Posmi 38, 26 un 62 km. Cik kopā?", "atb": ["126"],
                 "padoms": "38 + 62 = 100."},
                {"jaut": "Cik kilometru ir abos ceļojumos kopā?",
                 "atb": ["271"], "padoms": "145 + 126."},
                {"jaut": "Cik kilometru vēl trūkst līdz 300?",
                 "atb": ["29"], "padoms": "300 − 271."},
            ]),
            pavediens="celojums",
            konteksts="Maršrutā posmi ir nevienādi - bet bieži divi no tiem "
                      "kopā dod apaļu skaitli.",
            kapec="Apaļi skaitļi ļauj saskaitīt bez papīra, arī braucot."),

    Kopsavilkums([
        "Saskaitu vairākus skaitļus izdevīgā secībā.",
        "Meklēju pārus, kas dod apaļu desmitu vai simtu.",
        "Zinu, ka saskaitāmo secību drīkst mainīt.",
        "Zinu, ka atņemšanā secību mainīt nedrīkst.",
    ]),

    Majas([
        "Izrēķini 34 + 19 + 66 + 11, izvēloties ērtu secību.",
        "Atrodi trīs pārus, kuri kopā dod 100.",
        "Saskaiti trīs cenas no mājas čeka, sākot ar ērtāko pāri.",
    ]),
]
