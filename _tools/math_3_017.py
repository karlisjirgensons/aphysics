# -*- coding: utf-8 -*-
"""3. klase, 17. stunda: «Kā reizinājums palīdz atrast dalījumu?»

Dalīšana te nav jauna darbība, bet reizināšanas otra puse: 42 : 6 nozīmē
«kurš skaitlis reiz 6 dod 42». Tāpēc apgūtā tabula uzreiz kļūst par dalīšanas
tabulu, un jauna rinda nav jāmācās.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kā reizinājums palīdz atrast dalījumu?"

MERKIS = ("Iemācīsimies atrast dalījumu, domājot par atbilstošo reizinājumu, "
          "un pārbaudīt rezultātu.")

SATURS = [
    Sakums("Kā izdalīt 42 ar 6, ja dalīšanas tabulu neviens nav mācījis?",
           zimejums=restis([["6 · ?", "=", 42],
                            ["6 · 7", "=", 42]],
                           "meklē trūkstošo reizinātāju"),
           paraksts="Dalīšana ir jautājums par trūkstošo reizinātāju.",
           fakti=["Dalīšanas tabulas nav - ir tā pati reizināšanas tabula.",
                  "42 : 6 nozīmē: kurš skaitlis reiz 6 dod 42?"]),

    Doma("Dalīt nozīmē meklēt trūkstošo reizinātāju",
         "a : b = c tad un tikai tad, ja c · b = a - tāpēc katrs zināms "
         "reizinājums dod arī divus dalījumus.",
         soli=[
             "Izlasi dalījumu kā jautājumu: 56 : 8 - cik reiz 8 ir 56?",
             "Meklē atbildi astotnieku rindā: 48, 56 - tas ir septītais.",
             "Pieraksti atbildi: 56 : 8 = 7.",
             "Pārbaudi: 7 · 8 = 56.",
         ],
         pieze="No viena reizinājuma 6 · 7 = 42 rodas divi dalījumi: "
               "42 : 6 = 7 un 42 : 7 = 6. Trīs skaitļi - četri rēķini."),

    Paraugs("Cik ir 63 : 9?",
            uzd="Izrēķini 63 : 9, izmantojot reizināšanas tabulu.",
            soli=[
                ("9 · ? = 63",
                 "Dalījumu pārraksta kā reizinājumu ar trūkstošu skaitli."),
                ("9 · 7 = 63",
                 "Deviņnieku rindā 63 ir septītais skaitlis."),
                ("63 : 9 = 7",
                 "Pārbaude: 7 · 9 = 63 - sakrīt."),
            ],
            atbilde="7"),

    Ievadi("Atrodi dalījumu", [
        {"jaut": "48 : 6 = ?", "atb": ["8"], "padoms": "6 · 8 = 48."},
        {"jaut": "56 : 7 = ?", "atb": ["8"], "padoms": "7 · 8 = 56."},
        {"jaut": "72 : 9 = ?", "atb": ["8"], "padoms": "9 · 8 = 72."},
        {"jaut": "64 : 8 = ?", "atb": ["8"], "padoms": "8 · 8 = 64."},
        {"jaut": "54 : 6 = ?", "atb": ["9"], "padoms": "6 · 9 = 54."},
        {"jaut": "81 : 9 = ?", "atb": ["9"], "padoms": "9 · 9 = 81."},
    ], pamats=4),

    Zimejums("Trīs skaitļi - četri rēķini",
             restis([["6 · 7 = 42", "7 · 6 = 42"],
                     ["42 : 6 = 7", "42 : 7 = 6"]],
                    "viena skaitļu saime"),
             paskaidro="No katra reizinājuma var uzrakstīt vēl trīs rēķinus - "
                       "tos visus sauc par vienu skaitļu saimi.",
             ievads="Skaitļi visos četros rēķinos ir tie paši."),

    Varianti("Kurš rēķins ir no tās pašas saimes?", [
        {"jaut": "8 · 9 = 72. Kurš dalījums no tā izriet?",
         "opcijas": ["72 : 9 = 8", "72 : 8 = 10", "9 : 8 = 72", "72 · 9 = 8"],
         "pareizi": 0, "padoms": "Lielo skaitli dala ar vienu no "
                                 "reizinātājiem."},
        {"jaut": "Kurš rēķins *nepieder* saimei 6, 7 un 42?",
         "opcijas": ["42 + 6 = 48", "6 · 7 = 42", "42 : 7 = 6",
                     "7 · 6 = 42"],
         "pareizi": 0, "padoms": "Saimē ir tikai reizināšana un dalīšana."},
        {"jaut": "Cik ir 45 : 5?",
         "opcijas": ["9", "8", "7", "40"],
         "pareizi": 0, "padoms": "5 · 9 = 45."},
        {"jaut": "Kurš skaitlis ir trūkstošais: 8 · ? = 56?",
         "opcijas": ["7", "6", "8", "9"],
         "pareizi": 0, "padoms": "Astotnieku rinda: 48, 56."},
    ], pamats=4),

    Pasaule("Cik porciju sanāks?",
            Ievadi("", [
                {"jaut": "Pavārs izcepa 48 plāceņus un liek pa 6 šķīvī. Cik "
                         "šķīvju vajag?",
                 "atb": ["8"], "padoms": "48 : 6."},
                {"jaut": "56 ogas salika pa 7 traukos. Cik ogu ir vienā "
                         "traukā?",
                 "atb": ["8"], "padoms": "56 : 7."},
                {"jaut": "Receptei vajag 9 vienādas porcijas no 63 kartupeļu "
                         "gabaliņiem. Cik gabaliņu ir porcijā?",
                 "atb": ["7"], "padoms": "63 : 9."},
                {"jaut": "Cik plāceņu būs 5 šķīvjos, ja katrā ir 6?",
                 "atb": ["30"], "padoms": "5 · 6 - pārbaude ar reizināšanu."},
            ]),
            pavediens="virtuve",
            konteksts="Virtuvē visu dala vienādās porcijās - un tieši tā ir "
                      "dalīšana ar atbilstošo reizinājumu.",
            kapec="Kad zini reizinājumu, porciju skaitu pasaki uzreiz."),

    Kopsavilkums([
        "Atrodu dalījumu, domājot par atbilstošo reizinājumu.",
        "No viena reizinājuma uzrakstu visu skaitļu saimi.",
        "Pārbaudu dalīšanas rezultātu ar reizināšanu.",
        "Zinu, ka atsevišķa dalīšanas tabula nav vajadzīga.",
    ]),

    Majas([
        "Izvēlies trīs reizinājumus un uzraksti katram visu skaitļu saimi.",
        "Sadali 24 lietas mājās pa 6 un pārbaudi, cik grupu sanāca.",
        "Pajautā mājiniekiem piecus dalījumus no tabulas.",
    ]),
]
