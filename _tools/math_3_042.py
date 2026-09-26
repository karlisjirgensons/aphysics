# -*- coding: utf-8 -*-
"""3. klase, 42. stunda: «Kā izskatās saistītais pieraksts?»

Saistītais pieraksts ir tas, ko skolēns rakstīs visu atlikušo skolas laiku:
viena rinda, vienādības zīmes un katrā solī par vienu darbību mazāk. Te to
iemāca uz izteiksmēm, kur soļi vēl ir īsi un redzami.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kā izskatās saistītais pieraksts?"

MERKIS = ("Veidosim saistīto pierakstu, izpildītās darbības vietā rakstot "
          "rezultātu.")

SATURS = [
    Sakums("Kā pierakstīt risinājumu vienā rindā?",
           zimejums=restis([["(24 + 6) : 5 + 7 ="],
                            ["30 : 5 + 7 ="],
                            ["6 + 7 ="],
                            ["13"]],
                           "saistītais pieraksts"),
           paraksts="Katrā rindā viena darbība izpildīta, pārējais pārrakstīts.",
           fakti=["Vienādības zīme nozīmē: abās pusēs ir vienāda vērtība.",
                  "Tāpēc to drīkst likt tikai starp vienādiem skaitļiem."]),

    Doma("Vienādības zīme savieno vienādas vērtības",
         "Katrā jaunā rindā izteiksme ir citāda, bet tās vērtība - tā pati.",
         soli=[
             "Pārraksti izteiksmi un liec vienādības zīmi.",
             "Nākamajā rindā izpildi vienu darbību.",
             "Pārējo pārraksti bez izmaiņām.",
             "Turpini, līdz paliek viens skaitlis.",
         ],
         pieze="Nedrīkst rakstīt 24 + 6 = 30 : 5 = 6, jo 30 un 6 nav vienādi. "
               "Katra vienādības zīme ir apgalvojums, nevis bultiņa."),

    Paraugs("Pieraksti risinājumu saistīti",
            uzd="Aprēķini (24 + 6) : 5 + 7, pierakstot saistīti.",
            soli=[
                ("(24 + 6) : 5 + 7 =",
                 "Pirmā rinda - pati izteiksme."),
                ("= 30 : 5 + 7 =",
                 "Izpildīja iekavas, pārējo pārrakstīja."),
                ("= 6 + 7 =",
                 "Izpildīja dalīšanu."),
                ("= 13",
                 "Palika viens skaitlis."),
            ],
            atbilde="13"),

    Ievadi("Aprēķini un pieraksti", [
        {"jaut": "(18 + 2) : 4 + 6 = ?", "atb": ["11"],
         "padoms": "20 : 4 = 5; 5 + 6."},
        {"jaut": "(35 − 5) : 6 · 2 = ?", "atb": ["10"],
         "padoms": "30 : 6 = 5; 5 · 2."},
        {"jaut": "4 · 7 − (10 + 8) = ?", "atb": ["10"],
         "padoms": "28 − 18."},
        {"jaut": "(12 : 3 + 5) · 2 = ?", "atb": ["18"],
         "padoms": "4 + 5 = 9; 9 · 2."},
        {"jaut": "50 − (6 · 4 + 6) = ?", "atb": ["20"],
         "padoms": "24 + 6 = 30; 50 − 30."},
        {"jaut": "(9 + 6) : 5 · 8 = ?", "atb": ["24"],
         "padoms": "15 : 5 = 3; 3 · 8."},
    ], pamats=4),

    Zimejums("Pareizi un nepareizi",
             restis([["pareizi", "nepareizi"],
                     ["24 + 6 = 30", "24 + 6 = 30 : 5"],
                     ["30 : 5 = 6", "= 6"]],
                    "vienādības zīme nav bultiņa"),
             paskaidro="Labajā pusē starp 30 un 30 : 5 vienādības nav - tās "
                       "vērtības ir dažādas.",
             ievads="Salīdzini abas kolonnas."),

    Varianti("Kur pieraksts ir kļūdains?", [
        {"jaut": "Vai drīkst rakstīt «8 + 4 = 12 · 3 = 36»?",
         "opcijas": ["Nē, 12 un 12 · 3 nav vienādi", "Jā, tā ir ātrāk",
                     "Jā, ja atbilde ir pareiza", "Nē, jo trūkst iekavu"],
         "pareizi": 0, "padoms": "Vienādības zīme savieno vienādas vērtības."},
        {"jaut": "Kā pareizi pierakstīt to pašu?",
         "opcijas": ["(8 + 4) · 3 = 12 · 3 = 36", "8 + 4 · 3 = 36",
                     "8 + 4 = 12; · 3 = 36", "36 = 8 + 4 · 3"],
         "pareizi": 0, "padoms": "Vispirms visa izteiksme, tad soļi."},
        {"jaut": "Ko nozīmē vienādības zīme?",
         "opcijas": ["Abās pusēs ir vienāda vērtība",
                     "Tagad nāks atbilde", "Darbība ir izpildīta",
                     "Rinda ir beigusies"],
         "pareizi": 0, "padoms": "Tas ir apgalvojums par vienādību."},
        {"jaut": "Cik ir (20 − 5) : 3?",
         "opcijas": ["5", "15", "18", "4"],
         "pareizi": 0, "padoms": "15 : 3."},
    ], pamats=4),

    Pasaule("Cik MB paliks brīvi?",
            Ievadi("", [
                {"jaut": "(64 − 4 · 9) MB - cik tas ir?",
                 "atb": ["28"], "padoms": "64 − 36."},
                {"jaut": "(48 + 12) : 5 MB - cik tas ir?",
                 "atb": ["12"], "padoms": "60 : 5."},
                {"jaut": "3 · (20 − 6) MB - cik tas ir?",
                 "atb": ["42"], "padoms": "3 · 14."},
                {"jaut": "100 − (7 · 8 + 4) MB - cik tas ir?",
                 "atb": ["40"], "padoms": "56 + 4 = 60; 100 − 60."},
            ]),
            pavediens="dati",
            konteksts="Programmētājs pieraksta aprēķinu tieši šādā rindā - "
                      "citādi kļūdu vēlāk neatrast.",
            kapec="Saistītais pieraksts parāda katru soli, ne tikai atbildi."),

    Kopsavilkums([
        "Veidoju saistīto pierakstu ar vienādības zīmēm.",
        "Katrā rindā izpildu vienu darbību un pārējo pārrakstu.",
        "Zinu, ka vienādības zīme savieno vienādas vērtības.",
        "Pamanu kļūdainu pierakstu un izlaboju to.",
    ]),

    Majas([
        "Aprēķini (45 − 15) : 5 + 8 ar saistīto pierakstu.",
        "Atrodi kļūdu pierakstā «5 + 3 = 8 · 2 = 16» un izlabo to.",
        "Pieraksti trīs izteiksmes ar saistīto pierakstu burtnīcā.",
    ]),
]
