# -*- coding: utf-8 -*-
"""5. klase, 27. stunda: «Vai dalīšanai ir tāda pati īpašība?»

Iepriekšējās stundas īpašība pārbaudīta uz dalīšanu. Atbilde ir «daļēji», un
tieši tas ir vērtīgākais: b : a + c : a = (b + c) : a strādā, bet apgrieztais
pieraksts a : b + a : c nestrādā. Mācīšanās te ir pārbaudīt, nevis noticēt.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti)

TEMA = "Vai dalīšanai ir tāda pati īpašība?"

MERKIS = ("Mācīsimies lietot īpašību b : a + c : a = (b + c) : a un "
          "pārbaudīt, kad tā strādā un kad ne.")

SATURS = [
    Sakums("Vai to pašu var izdarīt ar dalīšanu?",
           fakti=["Reizināšanā: 7 · 6 + 3 · 6 = (7 + 3) · 6.",
                  "Vai tad arī 60 : 5 + 40 : 5 = (60 + 40) : 5?",
                  "Uzminēt te nav vērts - to var pārbaudīt."]),

    Doma("Dalītājam jābūt vienam un tam pašam",
         "Ja abus skaitļus dala ar vienu un to pašu skaitli, tos drīkst "
         "vispirms saskaitīt: b : a + c : a = (b + c) : a.",
         soli=[
             "Pārbaudi, vai abos dalījumos dalītājs ir viens un tas pats.",
             "Ja ir - saskaiti dalāmos un dali vienu reizi.",
             "Ja dalītāji atšķiras - īpašību lietot nedrīkst.",
             "Pārbaudi atbildi, izrēķinot abus dalījumus atsevišķi.",
         ],
         pieze="Otrādi tas nestrādā: 60 : (5 + 5) nav 60 : 5 + 60 : 5. "
               "Kreisajā pusē sanāk 6, labajā - 24. Dalāmo sadalīt drīkst, "
               "dalītāju - ne."),

    Paraugs("Pārbaudi īpašību",
            uzd="Vai 60 : 5 + 40 : 5 = (60 + 40) : 5?",
            soli=[
                ("Kreisā puse: 12 + 8 = 20",
                 "60 : 5 = 12 un 40 : 5 = 8."),
                ("Labā puse: 100 : 5 = 20",
                 "60 + 40 = 100."),
                ("20 = 20, vienādība ir patiesa",
                 "Dalītājs abos dalījumos bija viens un tas pats - 5."),
            ],
            atbilde="ir patiesa: abas puses dod 20"),

    Ievadi("Izrēķini ērtāk", [
        {"jaut": "60 : 5 + 40 : 5 = ?", "atb": ["20"],
         "padoms": "(60 + 40) : 5."},
        {"jaut": "72 : 8 + 24 : 8 = ?", "atb": ["12"],
         "padoms": "(72 + 24) : 8."},
        {"jaut": "150 : 3 + 60 : 3 = ?", "atb": ["70"],
         "padoms": "(150 + 60) : 3."},
        {"jaut": "900 : 9 − 450 : 9 = ?", "atb": ["50"],
         "padoms": "Atņemšanā tas pats: (900 − 450) : 9."},
        {"jaut": "Cik ir 60 : (5 + 5)?", "atb": ["6"],
         "padoms": "Vispirms iekavas: 60 : 10."},
        {"jaut": "Cik ir 60 : 5 + 60 : 5?", "atb": ["24"],
         "padoms": "12 + 12."},
        {"jaut": "84 : 4 + 16 : 4 = ?", "atb": ["25"],
         "padoms": "(84 + 16) : 4."},
        {"jaut": "1 000 : 8 − 200 : 8 = ?", "atb": ["100"],
         "padoms": "(1 000 − 200) : 8."},
    ], pamats=4,
        ievads="Vispirms paskaties, vai dalītājs ir viens un tas pats."),

    Varianti("Kad īpašību lietot drīkst?", [
        {"jaut": "Kurā izteiksmē īpašību drīkst lietot?",
         "opcijas": ["72 : 8 + 24 : 8", "72 : 8 + 24 : 6",
                     "72 : 8 + 24 · 8", "8 : 72 + 8 : 24"],
         "pareizi": 0,
         "padoms": "Dalītājam jābūt vienam un tam pašam."},
        {"jaut": "Vai 60 : (5 + 5) ir tas pats, kas 60 : 5 + 60 : 5?",
         "opcijas": ["Nē: 6 un 24", "Jā, abi ir 12", "Jā, abi ir 6",
                     "Nē: 24 un 6"],
         "pareizi": 0,
         "padoms": "Izrēķini abas puses atsevišķi."},
        {"jaut": "Ko drīkst sadalīt - dalāmo vai dalītāju?",
         "opcijas": ["Dalāmo", "Dalītāju", "Abus", "Nevienu"],
         "pareizi": 0,
         "padoms": "Sadali 100 : 5 kā (60 + 40) : 5."},
        {"jaut": "Kāpēc šī īpašība palīdz?",
         "opcijas": ["Vienu dalījumu izrēķināt ir ātrāk nekā divus",
                     "Jo skaitļi kļūst lielāki",
                     "Jo dalīšana pazūd",
                     "Jo iekavas rēķina pēdējās"],
         "pareizi": 0,
         "padoms": "(60 + 40) : 5 ir viens rēķins."},
    ], pamats=4),

    Pasaule("Kā sadalīt pirkumu?",
            Ievadi("", [
                {"jaut": "Pirmdien 60 eiro, otrdien 40 eiro; visu dala "
                         "5 cilvēki. Cik eiro katram?",
                 "atb": ["20"], "padoms": "(60 + 40) : 5."},
                {"jaut": "Bija 900 eiro, iztērēja 450; atlikumu dala "
                         "9 cilvēki. Cik katram?",
                 "atb": ["50"], "padoms": "(900 − 450) : 9."},
                {"jaut": "84 konfektes un vēl 16 dala 4 bērniem. Cik "
                         "katram?",
                 "atb": ["25"], "padoms": "(84 + 16) : 4."},
                {"jaut": "1 000 g un vēl 200 g sadala 8 paciņās. Cik gramu "
                         "paciņā?",
                 "atb": ["150"], "padoms": "(1 000 + 200) : 8."},
            ]),
            pavediens="veikals",
            konteksts="Pirkumus parasti dala pa daļām, bet dalītāju skaits "
                      "paliek tas pats - tāpēc summu var salikt kopā.",
            kapec="Viens dalījums ir ātrāks un mazāk kļūdains nekā divi."),

    Kopsavilkums([
        "Lietoju īpašību b : a + c : a = (b + c) : a.",
        "Pārbaudu, vai dalītājs abos dalījumos ir viens un tas pats.",
        "Zinu, ka dalāmo sadalīt drīkst, bet dalītāju - ne.",
        "Pārbaudu savu secinājumu ar konkrētiem skaitļiem.",
    ]),

    Majas([
        "Pārbaudi ar saviem skaitļiem, vai 100 : 4 + 20 : 4 = 120 : 4.",
        "Atrodi piemēru, kurā īpašību lietot nedrīkst, un paskaidro kāpēc.",
        "Padomā, kāpēc reizināšanā drīkst sadalīt jebkuru reizinātāju.",
    ]),
]
