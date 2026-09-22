# -*- coding: utf-8 -*-
"""5. klase, 111. stunda: «Kā pierakstīt leņķa aprēķinu?»

Rēķins jau ir zināms; te tas dabū pareizu apģērbu. Apzīmējums ∠AOB nav
formalitāte - tas ir vienīgais veids, kā pateikt, par kuru no vairākiem
leņķiem ir runa. Tāpēc stunda sākas ar burtu lasīšanu un beidzas ar pilnu
pierakstu: dots, jāatrod, risinājums, atbilde.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, lenkis)

TEMA = "Kā pierakstīt leņķa aprēķinu?"

MERKIS = ("Iemācīsimies pierakstīt leņķa lieluma aprēķinu, lietojot "
          "pieņemtos apzīmējumus.")

SATURS = [
    Sakums("Trīs burti vienam leņķim",
           zimejums=lenkis([(0, "A"), (70, "C"), (180, "B")],
                           loki=[(0, 70, "∠AOC"), (70, 180, "∠COB")],
                           virsraksts="Virsotne O, stari OA, OB un OC"),
           paraksts="∠AOC un ∠COB ir divi dažādi leņķi ar vienu virsotni.",
           fakti=["Vidējais burts vienmēr ir leņķa virsotne.",
                  "Malējie burti nosauc abus starus.",
                  "Bez burtiem nevar pateikt, par kuru leņķi ir runa."]),

    Doma("Pieraksts stāsta, kurš leņķis",
         "Leņķi apzīmē ar trim burtiem, no kuriem vidējais ir virsotne; "
         "aprēķinu pieraksta ar šiem apzīmējumiem, nevis ar vārdiem.",
         soli=[
             "Pieraksti, kas dots: ∠AOC = 70°.",
             "Pieraksti, kas jāatrod: ∠COB = ?",
             "Uzraksti sakarību: ∠AOC + ∠COB = 180°.",
             "Izteic nezināmo un izrēķini.",
             "Uzraksti atbildi ar grādu zīmi.",
         ],
         pieze="Ja pie virsotnes ir tikai viens leņķis, to drīkst apzīmēt ar "
               "vienu burtu - ∠O. Tiklīdz leņķu ir vairāki, viens burts vairs "
               "nepalīdz, un vajag visus trīs."),

    Paraugs("Pilns aprēķina pieraksts",
            uzd="∠AOC = 70°, stari OA un OB veido izstieptu leņķi. Atrodi "
                "∠COB.",
            soli=[
                ("Dots: ∠AOC = 70°, ∠AOB = 180°",
                 "Viss, kas zināms."),
                ("Jāatrod: ∠COB",
                 "Kas prasīts."),
                ("∠AOC + ∠COB = ∠AOB",
                 "Sakarība."),
                ("∠COB = 180° - 70° = 110°",
                 "Izteic un izrēķina."),
                ("Atbilde: ∠COB = 110°",
                 "Ar grādu zīmi."),
            ],
            atbilde="∠COB = 110°"),

    Ievadi("Lasi pierakstu", [
        {"jaut": "Pierakstā ∠AOB - kurš burts ir virsotne? Ieraksti burtu.",
         "atb": ["O", "o"], "padoms": "Vidējais burts."},
        {"jaut": "Pierakstā ∠MKN - kurš burts ir virsotne? Ieraksti burtu.",
         "atb": ["K", "k"], "padoms": "Vidējais burts."},
        {"jaut": "∠AOC = 70°, ∠AOB = 180°. Cik grādu ir ∠COB?",
         "atb": ["110"], "padoms": "180 - 70."},
        {"jaut": "∠AOC = 45°, ∠AOB = 180°. Cik grādu ir ∠COB?",
         "atb": ["135"], "padoms": "180 - 45."},
        {"jaut": "∠AOC = 120°, ∠COB = 90°. Cik grādu ir ∠AOB?",
         "atb": ["210"], "padoms": "120 + 90."},
        {"jaut": "∠AOB = 360°, ∠AOC = 150°. Cik grādu ir ∠COB?",
         "atb": ["210"], "padoms": "360 - 150."},
        {"jaut": "∠AOC = 30°, ∠COD = 40°, ∠DOB = ? Kopā izstiepts leņķis. "
                 "Cik grādu ir ∠DOB?",
         "atb": ["110"], "padoms": "180 - 70."},
        {"jaut": "∠AOB = 180°, un abi leņķi ir vienādi. Cik grādu ir katrs?",
         "atb": ["90"], "padoms": "180 : 2."},
    ], pamats=4,
        ievads="Vispirms izlasi, kurš leņķis ir domāts, tikai tad rēķini."),

    Zimejums("Katram leņķim savs vārds",
             lenkis([(0, "A"), (40, "C"), (110, "D"), (180, "B")],
                    loki=[(0, 40, "∠AOC"), (40, 110, "∠COD"),
                          (110, 180, "∠DOB")],
                    virsraksts="Trīs leņķi, trīs pieraksti"),
             paskaidro="Visiem trim leņķiem virsotne ir O, bet stari "
                       "atšķiras - tāpēc arī pieraksti ir dažādi.",
             ievads="Ar burtiem katru leņķi var nosaukt precīzi."),

    Varianti("Ko nozīmē šis pieraksts?", [
        {"jaut": "Kurš burts pierakstā ∠XYZ ir virsotne?",
         "opcijas": ["Y", "X", "Z", "Visi trīs"],
         "pareizi": 0,
         "padoms": "Vidējais."},
        {"jaut": "Vai ∠AOB un ∠BOA ir viens un tas pats leņķis?",
         "opcijas": ["Jā, virsotne ir tā pati", "Nē", "Tikai taisnam leņķim",
                     "To nevar zināt"],
         "pareizi": 0,
         "padoms": "Mainījās tikai staru secība."},
        {"jaut": "Kad leņķi drīkst apzīmēt ar vienu burtu?",
         "opcijas": ["Kad pie virsotnes ir tikai viens leņķis", "Vienmēr",
                     "Nekad", "Kad leņķis ir taisns"],
         "pareizi": 0,
         "padoms": "Citādi nav skaidrs, par kuru runa."},
        {"jaut": "∠AOC = 70°, ∠AOB = 180°. Kāds ir ∠COB?",
         "opcijas": ["110°", "70°", "250°", "90°"],
         "pareizi": 0,
         "padoms": "180 - 70."},
        {"jaut": "Ar ko sākas pareizs pieraksts?",
         "opcijas": ["Ar «Dots» un «Jāatrod»", "Ar atbildi",
                     "Ar zīmējumu", "Ar rēķinu"],
         "pareizi": 0,
         "padoms": "Vispirms izraksta zināmo."},
        {"jaut": "Kas obligāti jāraksta pie atbildes?",
         "opcijas": ["Grādu zīme", "Leņķa veids", "Zīmējums", "Nekas"],
         "pareizi": 0,
         "padoms": "Leņķi mēra grādos."},
    ], pamats=4),

    Pasaule("Rasējums ar apzīmējumiem",
            Ievadi("", [
                {"jaut": "Rasējumā ∠AOC = 55°, ∠AOB = 180°. Cik grādu ir "
                         "∠COB?",
                 "atb": ["125"], "padoms": "180 - 55."},
                {"jaut": "Citā rasējumā ∠AOC = 25°, ∠COD = 65°. Cik grādu ir "
                         "∠AOD?",
                 "atb": ["90"], "padoms": "25 + 65."},
                {"jaut": "∠AOB = 360°, ∠AOC = 200°. Cik grādu ir ∠COB?",
                 "atb": ["160"], "padoms": "360 - 200."},
                {"jaut": "∠AOC = 90°, ∠COB = 90°. Cik grādu ir ∠AOB?",
                 "atb": ["180"], "padoms": "90 + 90."},
            ]),
            pavediens="tehnika",
            konteksts="Rasējumā leņķu ir daudz, un katram jābūt nosauktam "
                      "tā, lai otrs cilvēks saprastu.",
            kapec="Apzīmējums ir vienīgais veids, kā pateikt, par kuru leņķi "
                  "ir runa."),

    Kopsavilkums([
        "Lasu leņķa apzīmējumu un atrodu tā virsotni.",
        "Pierakstu leņķa aprēķinu ar apzīmējumiem, nevis vārdiem.",
        "Sāku pierakstu ar doto un prasīto.",
        "Uzrakstu atbildi ar grādu zīmi.",
    ]),

    Majas([
        "Uzzīmē trīs starus no punkta O un pieraksti visus trīs leņķus.",
        "Pieraksti pilnu aprēķinu uzdevumam ∠AOC = 35°, ∠AOB = 180°.",
        "Paskaidro, kāpēc ∠AOB un ∠AOC nav viens un tas pats.",
    ]),
]
