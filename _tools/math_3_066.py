# -*- coding: utf-8 -*-
"""3. klase, 66. stunda: «Cik precīzi jāmēra?»

Mērījums nekad nav pilnīgi precīzs, un plānam tas arī nav vajadzīgs. Stunda
māca izvēlēties precizitāti pēc uzdevuma: telpu mēra līdz pilniem desmitiem
centimetru, jo plānā milimetrs tāpat pazustu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         restis)

TEMA = "Cik precīzi jāmēra?"

MERKIS = ("Mērīsim telpas izmērus un noapaļosim mērījumus līdz pilniem "
          "desmitiem centimetru.")

SATURS = [
    Sakums("Vai 4 m 37 cm un 4 m 40 cm ir liela starpība?",
           zimejums=restis([["mērījums", "noapaļots"],
                            ["437 cm", "440 cm"],
                            ["612 cm", "610 cm"],
                            ["255 cm", "260 cm"]],
                           "līdz pilniem desmitiem"),
           paraksts="Plānā 3 cm starpība pazūd - tā ir mazāka par zīmuļa "
                    "svītru.",
           fakti=["Neviens mērījums nav pilnīgi precīzs.",
                  "Precizitāti izvēlas pēc tā, kam mērījums vajadzīgs."]),

    Doma("Noapaļo uz tuvāko desmitu",
         "Ja pēdējais cipars ir 5 vai vairāk, noapaļo uz augšu; ja mazāk - "
         "uz leju.",
         soli=[
             "Paskaties uz pēdējo ciparu - vienu vietu.",
             "Ja tas ir 0, 1, 2, 3 vai 4 - noapaļo uz leju.",
             "Ja tas ir 5, 6, 7, 8 vai 9 - noapaļo uz augšu.",
             "Vienu vietā ieraksti 0.",
         ],
         pieze="Noapaļots mērījums nav kļūda - tas ir *izvēle*. Svarīgi ir "
               "pateikt, līdz kam noapaļoji."),

    Paraugs("Kā noapaļot 437 cm?",
            uzd="Noapaļo mērījumu 437 cm līdz pilniem desmitiem centimetru.",
            soli=[
                ("437 - vienu vietā ir 7",
                 "Skatās uz pēdējo ciparu."),
                ("7 ≥ 5, tātad uz augšu",
                 "Desmitu skaits palielinās par vienu."),
                ("437 cm ≈ 440 cm",
                 "Noapaļotu vērtību raksta ar zīmi «≈»."),
            ],
            atbilde="440 cm"),

    Petijums("Izmēri klasi",
             vajag="mērlente vai 1 m garš lineāls",
             soli=[
                 "Izmēri klases garumu centimetros.",
                 "Izmēri klases platumu centimetros.",
                 "Noapaļo abus mērījumus līdz pilniem desmitiem.",
                 "Pieraksti abus skaitļus - precīzo un noapaļoto.",
             ],
             secinajums="Plānam pietiek ar noapaļoto skaitli, bet mērījumu "
                        "lapā jāpaliek arī precīzajam."),

    Ievadi("Noapaļo līdz desmitiem", [
        {"jaut": "Noapaļo 437 cm līdz desmitiem. Cik sanāk?",
         "atb": ["440"], "padoms": "Vienu vietā ir 7."},
        {"jaut": "Noapaļo 612 cm līdz desmitiem. Cik sanāk?",
         "atb": ["610"], "padoms": "Vienu vietā ir 2."},
        {"jaut": "Noapaļo 255 cm līdz desmitiem. Cik sanāk?",
         "atb": ["260"], "padoms": "Vienu vietā ir 5 - uz augšu."},
        {"jaut": "Noapaļo 304 cm līdz desmitiem. Cik sanāk?",
         "atb": ["300"], "padoms": "Vienu vietā ir 4."},
        {"jaut": "Noapaļo 198 cm līdz desmitiem. Cik sanāk?",
         "atb": ["200"], "padoms": "198 → 200."},
        {"jaut": "Noapaļo 745 cm līdz desmitiem. Cik sanāk?",
         "atb": ["750"], "padoms": "Vienu vietā ir 5."},
    ], pamats=4),

    Zimejums("Kurp noapaļot",
             restis([["pēdējais cipars", "0-4", "5-9"],
                     ["virziens", "uz leju", "uz augšu"]],
                    "noapaļošanas noteikums"),
             paskaidro="Piecinieks vienmēr iet uz augšu - tā ir vienošanās, "
                       "lai visi noapaļotu vienādi.",
             ievads="Divi gadījumi, divi virzieni."),

    Varianti("Cik precīzi vajag?", [
        {"jaut": "Cik precīzi jāmēra telpa plānam?",
         "opcijas": ["Līdz pilniem desmitiem cm", "Līdz milimetram",
                     "Līdz metram", "Pavisam precīzi"],
         "pareizi": 0, "padoms": "Plānā milimetrs tāpat pazūd."},
        {"jaut": "Noapaļo 486 cm līdz desmitiem.",
         "opcijas": ["490 cm", "480 cm", "500 cm", "400 cm"],
         "pareizi": 0, "padoms": "Vienu vietā ir 6."},
        {"jaut": "Kura zīme jālieto pie noapaļota mērījuma?",
         "opcijas": ["≈", "=", ">", "<"],
         "pareizi": 0, "padoms": "Vērtība vairs nav precīza."},
        {"jaut": "Kad precizitāte ir svarīga līdz milimetram?",
         "opcijas": ["Izgatavojot detaļu", "Mērot istabu",
                     "Mērot ceļu", "Mērot dārzu"],
         "pareizi": 0, "padoms": "Jo mazāks objekts, jo precīzāk."},
    ], pamats=4),

    Pasaule("Cik precīzi mēra ceļu?",
            Ievadi("", [
                {"jaut": "Ceļš ir 1237 km. Noapaļo līdz pilniem simtiem.",
                 "atb": ["1200"], "padoms": "Desmitu vietā ir 3."},
                {"jaut": "Otrs ceļš ir 856 km. Noapaļo līdz pilniem simtiem.",
                 "atb": ["900"], "padoms": "Desmitu vietā ir 5."},
                {"jaut": "Cik apmēram ir abi ceļi kopā?",
                 "atb": ["2100"], "padoms": "1200 + 900."},
                {"jaut": "Cik precīzi ir abi ceļi kopā?",
                 "atb": ["2093"], "padoms": "1237 + 856."},
            ]),
            pavediens="celojums",
            konteksts="Ceļazīmēs attālumus raksta noapaļotus - neviens "
                      "nebrauc pēc metriem.",
            kapec="Precizitāti izvēlas pēc tā, kam skaitlis vajadzīgs."),

    Kopsavilkums([
        "Mēru telpas izmērus centimetros.",
        "Noapaļoju mērījumu līdz pilniem desmitiem.",
        "Zinu noapaļošanas noteikumu un lietoju zīmi «≈».",
        "Izvēlos precizitāti pēc tā, kam mērījums vajadzīgs.",
    ]),

    Majas([
        "Izmēri savas istabas garumu un noapaļo to līdz desmitiem "
        "centimetru.",
        "Pieraksti gan precīzo, gan noapaļoto skaitli.",
        "Noapaļo trīs mājas priekšmetu garumus.",
    ]),
]
