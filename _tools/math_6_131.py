# -*- coding: utf-8 -*-
"""6. klase, 131. stunda: «Kas notiek, atņemot negatīvu skaitli?»

Grūtākā vieta visā tematā. Tāpēc te nav likuma - ir virkne, kurā mazinātājs
samazinās pa vienam, un skolēns pats pamana, ka starpība aug. Likums nāk
nākamajā stundā, kad tas jau ir redzēts.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         restis)

TEMA = "Kas notiek, atņemot negatīvu skaitli?"

MERKIS = ("Aprēķināsim starpību virknē un komentēsim saskatīto sakarību.")

SATURS = [
    Sakums("Virkne, kas turpinās pati",
           zimejums=restis([["5 − 2", "5 − 1", "5 − 0", "5 − (−1)"],
                            ["3", "4", "5", "6"]]),
           paraksts="Mazinātājs samazinās pa vienam - starpība katru reizi "
                    "aug par vienu. Virkne neapstājas pie nulles.",
           fakti=["Jo mazāks mazinātājs, jo lielāka starpība.",
                  "Pie nulles virkne neapstājas.",
                  "Tāpēc 5 − (−1) ir 6, nevis 4."]),

    Doma("Turpini virkni, un likums parādās pats",
         "Ja mazinātājs samazinās par vienu, starpība palielinās par vienu; "
         "tas turpinās arī tad, kad mazinātājs kļūst negatīvs.",
         soli=[
             "Pieraksti virkni, kurā mazinātājs samazinās pa vienam.",
             "Izrēķini katru starpību.",
             "Paskaties, kā mainās rezultāti.",
             "Turpini virkni pāri nullei.",
             "Pieraksti, ko pamanīji.",
         ],
         pieze="Tieši tāpēc atņemt negatīvu skaitli nozīmē pieskaitīt: "
               "virkne 3; 4; 5; 6 turpinās vienmērīgi, un tas ir vienīgais "
               "veids, kā tā nesalūzt."),

    Paraugs("Turpini virkni",
            uzd="Izrēķini 5 − 2; 5 − 1; 5 − 0; 5 − (−1); 5 − (−2).",
            soli=[
                ("5 − 2 = 3; 5 − 1 = 4",
                 "Mazinātājs sarūk, starpība aug."),
                ("5 − 0 = 5",
                 "Pie nulles nekas neapstājas."),
                ("5 − (−1) = 6",
                 "Virkne turpinās vienmērīgi."),
                ("5 − (−2) = 7",
                 "Vēl par vienu vairāk."),
            ],
            atbilde="3; 4; 5; 6; 7"),

    Ievadi("Turpini virkni", [
        {"jaut": "Cik ir 5 − 1?",
         "atb": ["4"], "padoms": "Parasta atņemšana."},
        {"jaut": "Cik ir 5 − 0?",
         "atb": ["5"], "padoms": "Neko neatņem."},
        {"jaut": "Cik ir 5 − (−1)?",
         "atb": ["6"], "padoms": "Virkne turpinās."},
        {"jaut": "Cik ir 5 − (−3)?",
         "atb": ["8"], "padoms": "5 + 3."},
        {"jaut": "Cik ir −2 − (−5)?",
         "atb": ["3"], "padoms": "−2 + 5."},
        {"jaut": "Cik ir −4 − (−1)?",
         "atb": ["-3", "−3"], "padoms": "−4 + 1."},
    ], pamats=4),

    Petijums("Izveido savu virkni",
             vajag="burtnīca",
             soli=[
                 "Izvēlies mazināmo, piemēram, 8.",
                 "Pieraksti virkni: 8 − 3; 8 − 2; 8 − 1; 8 − 0.",
                 "Izrēķini katru starpību.",
                 "Turpini virkni ar 8 − (−1) un 8 − (−2).",
                 "Pieraksti, par cik katra nākamā starpība atšķiras.",
             ],
             secinajums="Katra nākamā starpība ir par vienu lielāka - arī "
                        "tad, kad mazinātājs kļūst negatīvs."),

    Varianti("Ko rāda virkne?", [
        {"jaut": "Jo mazāks mazinātājs, jo starpība...",
         "opcijas": ["lielāka", "mazāka", "nemainās", "negatīva"],
         "pareizi": 0,
         "padoms": "Mazāk atņem - vairāk paliek."},
        {"jaut": "Kāpēc virkne neapstājas pie nulles?",
         "opcijas": ["Jo aiz nulles ir negatīvi skaitļi",
                     "Jo nulle nav skaitlis",
                     "Jo tā ir kļūda", "Tā apstājas"],
         "pareizi": 0,
         "padoms": "Skaitļu taisne turpinās."},
        {"jaut": "5 − (−2) ir vienāds ar...",
         "opcijas": ["7", "3", "−7", "−3"],
         "pareizi": 0,
         "padoms": "Turpini virkni."},
        {"jaut": "−3 − (−4) ir vienāds ar...",
         "opcijas": ["1", "−7", "7", "−1"],
         "pareizi": 0,
         "padoms": "−3 + 4."},
    ], pamats=4),

    Pasaule("Kā mainās parāds?",
            Ievadi("", [
                {"jaut": "Kontā −50 €. Atceļ rēķinu par 20 € jeb atņem "
                         "−20 €. Cik eiro ir kontā?",
                 "atb": ["-30", "−30"], "padoms": "−50 − (−20) = −50 + 20."},
                {"jaut": "Atceļ vēl vienu rēķinu par 30 €. Cik eiro ir "
                         "kontā?",
                 "atb": ["0"], "padoms": "−30 + 30."},
                {"jaut": "Temperatūra bija −5 °C. Atceļ prognozēto "
                         "pazeminājumu par 3 grādiem. Cik grādu ir?",
                 "atb": ["-2", "−2"], "padoms": "−5 − (−3)."},
                {"jaut": "Bija 2 °C, atceļ pazeminājumu par 6 grādiem. Cik "
                         "grādu ir?",
                 "atb": ["8"], "padoms": "2 + 6."},
            ]),
            pavediens="veikals",
            konteksts="Atcelts rēķins ir tieši negatīva skaitļa atņemšana - "
                      "un atlikums no tā aug.",
            kapec="Noņemt parādu nozīmē pievienot naudu."),

    Zimejums("Virkne, kas neapstājas",
             restis([["5 − 2", "5 − 1", "5 − 0", "5 − (−1)", "5 − (−2)"],
                     ["3", "4", "5", "6", "7"]]),
             paskaidro="Apakšējā rinda aug vienmērīgi - tieši tas pierāda, "
                       "ka atņemt negatīvu nozīmē pieskaitīt.",
             ievads="Visa virkne kopā."),

    Kopsavilkums([
        "Aprēķinu starpības virknē ar sarūkošu mazinātāju.",
        "Pamanu, ka starpība aug vienmērīgi.",
        "Turpinu virkni pāri nullei.",
        "Paskaidroju, kāpēc atņemt negatīvu nozīmē pieskaitīt.",
    ]),

    Majas([
        "Izveido virkni no 10 un turpini to līdz 10 − (−3).",
        "Pieraksti, par cik aug katra nākamā starpība.",
        "Izrēķini −6 − (−2) un −6 − (−9).",
    ]),
]
