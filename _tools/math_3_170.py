# -*- coding: utf-8 -*-
"""3. klase, 170. stunda: «Cik veikli rēķinu 1000 apjomā?»

Gada noslēguma otrā stunda: saskaitīšana, atņemšana un vairākdarbību
izteiksmes vienā piegājienā. Pārbaudes mērķis ir tas pats - saraksts, ko
atkārtot, nevis atzīme.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Cik veikli rēķinu 1000 apjomā?"

MERKIS = ("Pārbaudīsim saskaitīšanu un atņemšanu 1000 apjomā un izteiksmju "
          "aprēķināšanu.")

SATURS = [
    Sakums("Vai visi četri gadījumi ir droši?",
           zimejums=restis([["+ ar pāreju", "− ar aizņēmumu"],
                            ["izteiksmes ar iekavām", "darbību secība"]],
                           "četras prasmes"),
           paraksts="Katra no tām 4. klasē būs vajadzīga katru nedēļu.",
           fakti=["Grūtākie gadījumi ir pāreja un aizņēmums.",
                  "Izteiksmēs izšķirošā ir darbību secība."]),

    Doma("Vispirms atpazīsti gadījumu",
         "Pirms rēķini, pasaki sev: vai te būs pāreja, aizņēmums vai "
         "iekavas?",
         soli=[
             "Izlasi piemēru un nosaki gadījumu.",
             "Izrēķini, ievērojot darbību secību.",
             "Pārbaudi ar pretējo darbību vai aptuveno vērtību.",
             "Atzīmē gadījumus, kuros kļūdījies.",
         ],
         pieze="Vairums kļūdu rodas nevis rēķinot, bet tāpēc, ka gadījums "
               "netika pamanīts - pārnesums vienkārši aizmirstas."),

    Paraugs("Kā rēķināt izteiksmi ar iekavām?",
            uzd="Aprēķini (450 − 180) : 3 + 60.",
            soli=[
                ("450 − 180 = 270",
                 "Vispirms iekavas."),
                ("270 : 3 = 90",
                 "Tad dalīšana."),
                ("90 + 60 = 150",
                 "Visbeidzot saskaitīšana."),
            ],
            atbilde="150"),

    Ievadi("Gada noslēguma pārbaude", [
        {"jaut": "268 + 154 = ?", "atb": ["422"], "padoms": "Divi pārnesumi."},
        {"jaut": "703 − 258 = ?", "atb": ["445"], "padoms": "Caur nulli."},
        {"jaut": "(450 − 180) : 3 = ?", "atb": ["90"],
         "padoms": "Vispirms iekavas."},
        {"jaut": "(450 − 180) : 3 + 60 = ?", "atb": ["150"],
         "padoms": "90 + 60."},
        {"jaut": "500 − 3 · 40 = ?", "atb": ["380"],
         "padoms": "Vispirms reizināšana."},
        {"jaut": "Cik pietrūkst 645 līdz 1000?", "atb": ["355"],
         "padoms": "5 + 50 + 300."},
        {"jaut": "24 · 3 = ?", "atb": ["72"], "padoms": "60 + 12."},
        {"jaut": "96 : 4 = ?", "atb": ["24"], "padoms": "80 : 4 un 16 : 4."},
    ], pamats=6),

    Zimejums("Darbību secība",
             restis([["1.", "iekavas"],
                     ["2.", "· un :"],
                     ["3.", "+ un −"]],
                    "trīs pakāpieni"),
             paskaidro="Šī tabula der arī 4. klasē - tikai skaitļi būs "
                       "lielāki.",
             ievads="Noteikums, kas nemainās."),

    Varianti("Kurš gadījums tas ir?", [
        {"jaut": "Kurā piemērā būs aizņēmums?",
         "opcijas": ["703 − 258", "568 − 234", "342 + 215", "400 + 300"],
         "pareizi": 0, "padoms": "3 − 8 nesanāk."},
        {"jaut": "Cik ir 500 − 3 · 40?",
         "opcijas": ["380", "20 000", "460", "120"],
         "pareizi": 0, "padoms": "Vispirms 3 · 40."},
        {"jaut": "Kura darbība ir pirmā izteiksmē (450 − 180) : 3?",
         "opcijas": ["Atņemšana", "Dalīšana", "Abas reizē", "Vienalga"],
         "pareizi": 0, "padoms": "Iekavas."},
        {"jaut": "Cik apmēram ir 268 + 154?",
         "opcijas": ["400", "300", "500", "1000"],
         "pareizi": 0, "padoms": "300 + 200."},
    ], pamats=4),

    Pasaule("Cik maksās vasaras nometne?",
            Ievadi("", [
                {"jaut": "Nometne maksā 268 eiro, brauciens 154 eiro. Cik "
                         "kopā?",
                 "atb": ["422"], "padoms": "268 + 154."},
                {"jaut": "Saziedoti 703 eiro, iztērēti 258. Cik palika?",
                 "atb": ["445"], "padoms": "703 − 258."},
                {"jaut": "Par atlikumu pirks 5 komplektus pa 80 eiro. Cik "
                         "tas maksās?",
                 "atb": ["400"], "padoms": "5 · 80."},
                {"jaut": "Cik eiro paliks pēc tam?", "atb": ["45"],
                 "padoms": "445 − 400."},
            ]),
            pavediens="skola",
            konteksts="Vasaras nometnes budžetā ir gan saskaitīšana, gan "
                      "atņemšana, gan reizināšana - viss gada saturs.",
            kapec="Tieši tādus rēķinus 4. klasē darīsi ar vēl lielākiem "
                  "skaitļiem."),

    Kopsavilkums([
        "Saskaitu un atņemu 1000 apjomā ar pāreju un aizņēmumu.",
        "Aprēķinu izteiksmes, ievērojot darbību secību.",
        "Pārbaudu katru atbildi.",
        "Zinu, kuri gadījumi man jāatkārto.",
    ]),

    Majas([
        "Izrēķini astoņus piemērus un pārbaudi katru.",
        "Pieraksti, kuri gadījumi nepadevās.",
        "Uzraksti sev vienu uzdevumu vasarai.",
    ]),
]
