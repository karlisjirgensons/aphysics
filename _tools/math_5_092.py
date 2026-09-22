# -*- coding: utf-8 -*-
"""5. klase, 92. stunda: «Kā neīstu daļu pārvērst jauktā skaitlī?»

Visa stunda balstās uz vienu jau zināmu darbību - dalīšanu ar atlikumu -,
tikai tagad tai ir jēga: nepilnais dalījums kļūst par veselo daļu, bet
atlikums - par jauno skaitītāju. Saucējs nemainās nekad, un tieši to skolēni
visbiežāk aizmirst.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis, taisne)

TEMA = "Kā neīstu daļu pārvērst jauktā skaitlī?"

MERKIS = ("Iemācīsimies pārveidot neīstu daļu par jauktu skaitli, izmantojot "
          "dalīšanu ar atlikumu.")

SATURS = [
    Sakums("Vienpadsmit ceturtdaļas - cik tas ir veselu?",
           zimejums=taisne(0, 3, 1, [(11 / 4.0, "11/4")],
                           virsraksts="Kur uz taisnes ir 11/4"),
           paraksts="{11|4} atrodas starp 2 un 3, tātad tajā ir divi veseli.",
           fakti=["Četras ceturtdaļas ir viens vesels.",
                  "Vienpadsmit ceturtdaļās veselu ir vairāk nekā viens.",
                  "Cik tieši - pasaka dalīšana ar atlikumu."]),

    Doma("Dali skaitītāju ar saucēju",
         "Lai neīstu daļu pārvērstu jauktā skaitlī, skaitītāju dala ar "
         "saucēju: nepilnais dalījums ir veselā daļa, atlikums - jaunais "
         "skaitītājs, saucējs paliek tas pats.",
         soli=[
             "Dali skaitītāju ar saucēju.",
             "Pieraksti nepilno dalījumu kā veselo daļu.",
             "Pieraksti atlikumu kā jauno skaitītāju.",
             "Saucēju atstāj neskartu.",
             "Pārbaudi, vai jaunā daļa ir īsta.",
         ],
         pieze="Ja atlikums ir 0, jaukta skaitļa nav - iznāk vesels skaitlis: "
               "{12|4} = 3. Ja skaitītājs ir mazāks par saucēju, daļa jau ir "
               "īsta un pārveidot nav ko."),

    Paraugs("Pārvērt {11|4} par jauktu skaitli",
            uzd="Pieraksti neīsto daļu {11|4} kā jauktu skaitli.",
            soli=[
                ("11 : 4 = 2, atlikums 3",
                 "Dalīšana ar atlikumu."),
                ("Veselā daļa ir 2",
                 "Nepilnais dalījums."),
                ("Jaunais skaitītājs ir 3",
                 "Atlikums."),
                ("Saucējs paliek 4",
                 "To nemaina nekad."),
                ("{11|4} = 2{3|4}",
                 "Jauktais skaitlis."),
            ],
            atbilde="{11|4} = 2{3|4}"),

    Ievadi("Pārvērt jauktā skaitlī", [
        {"jaut": "{11|4} kā jaukts skaitlis. Atbildi raksti kā a b/c.",
         "atb": ["2 3/4"], "padoms": "11 : 4 = 2, atl. 3."},
        {"jaut": "{7|2} kā jaukts skaitlis. Atbildi raksti kā a b/c.",
         "atb": ["3 1/2"], "padoms": "7 : 2 = 3, atl. 1."},
        {"jaut": "{9|5} kā jaukts skaitlis. Atbildi raksti kā a b/c.",
         "atb": ["1 4/5"], "padoms": "9 : 5 = 1, atl. 4."},
        {"jaut": "{17|3} kā jaukts skaitlis. Atbildi raksti kā a b/c.",
         "atb": ["5 2/3"], "padoms": "17 : 3 = 5, atl. 2."},
        {"jaut": "{13|6} kā jaukts skaitlis. Atbildi raksti kā a b/c.",
         "atb": ["2 1/6"], "padoms": "13 : 6 = 2, atl. 1."},
        {"jaut": "Cik ir {12|4}? Ieraksti veselu skaitli.",
         "atb": ["3"], "padoms": "Atlikuma nav."},
        {"jaut": "Cik ir {20|5}? Ieraksti veselu skaitli.",
         "atb": ["4"], "padoms": "Atlikuma nav."},
        {"jaut": "{25|8} kā jaukts skaitlis. Atbildi raksti kā a b/c.",
         "atb": ["3 1/8"], "padoms": "25 : 8 = 3, atl. 1."},
    ], pamats=4,
        ievads="Dali skaitītāju ar saucēju un skaties gan uz dalījumu, gan "
               "uz atlikumu."),

    Zimejums("No daļas uz jauktu skaitli",
             restis([["11/4", "2 3/4"],
                     ["7/2", "3 1/2"]],
                    virsraksts="Kreisajā ailē neīsta daļa"),
             paskaidro="Labajā ailē ir tas pats skaitlis, tikai ar atdalītu "
                       "veselo. Saucējs abās ailēs ir viens un tas pats.",
             ievads="Pārveidojot mainās pieraksts, nevis skaitlis."),

    Varianti("Kas kļūst par ko?", [
        {"jaut": "Kas kļūst par jauktā skaitļa veselo daļu?",
         "opcijas": ["Nepilnais dalījums", "Atlikums", "Saucējs",
                     "Skaitītājs"],
         "pareizi": 0,
         "padoms": "Cik reižu saucējs ietilpst skaitītājā."},
        {"jaut": "Kas kļūst par jauno skaitītāju?",
         "opcijas": ["Atlikums", "Dalījums", "Saucējs", "Vecais skaitītājs"],
         "pareizi": 0,
         "padoms": "Tas, kas palika pāri."},
        {"jaut": "Kas notiek ar saucēju?",
         "opcijas": ["Paliek tas pats", "Kļūst par veselo",
                     "Dalās ar 2", "Pazūd"],
         "pareizi": 0,
         "padoms": "Gabalu lielums nemainās."},
        {"jaut": "{12|4} kā jaukts skaitlis ir...",
         "opcijas": ["3", "3{0|4}", "2{4|4}", "{3|1}"],
         "pareizi": 0,
         "padoms": "Atlikuma nav."},
        {"jaut": "Vai {3|5} var pārvērst jauktā skaitlī?",
         "opcijas": ["Nevar, tā jau ir īsta daļa", "Var, būs 0{3|5}",
                     "Var, būs 1{3|5}", "Var vienmēr"],
         "pareizi": 0,
         "padoms": "Veselu tajā nav."},
        {"jaut": "{9|5} kā jaukts skaitlis ir...",
         "opcijas": ["1{4|5}", "4{1|5}", "2{1|5}", "1{5|4}"],
         "pareizi": 0,
         "padoms": "9 : 5 = 1, atl. 4."},
    ], pamats=4),

    Pasaule("Cik veselu glāžu vajag?",
            Ievadi("", [
                {"jaut": "Receptē {11|4} glāzes miltu. Cik tas ir kā jaukts "
                         "skaitlis? Atbildi raksti kā a b/c.",
                 "atb": ["2 3/4"], "padoms": "11 : 4."},
                {"jaut": "Cik veselu glāžu vajag vismaz?",
                 "atb": ["2"], "padoms": "Veselā daļa."},
                {"jaut": "Receptē {7|2} glāzes ūdens. Cik tas ir kā jaukts "
                         "skaitlis? Atbildi raksti kā a b/c.",
                 "atb": ["3 1/2"], "padoms": "7 : 2."},
                {"jaut": "Receptē {8|4} glāzes piena. Cik veselu glāžu tas "
                         "ir?",
                 "atb": ["2"], "padoms": "Atlikuma nav."},
            ]),
            pavediens="virtuve",
            konteksts="Receptē reizēm raksta {11|4} glāzes, bet virtuvē "
                      "skaita veselas glāzes un atlikumu.",
            kapec="Jaukts skaitlis pasaka uzreiz, cik glāžu ņemt."),

    Kopsavilkums([
        "Pārveidoju neīstu daļu par jauktu skaitli.",
        "Lietoju dalīšanu ar atlikumu un zinu, kas kļūst par ko.",
        "Atstāju saucēju nemainīgu.",
        "Atpazīstu gadījumu, kad iznāk vesels skaitlis.",
    ]),

    Majas([
        "Pārvērt jauktos skaitļos {15|4}, {23|5} un {19|6}.",
        "Atrodi neīstu daļu, kas pārvēršas par veselu skaitli.",
        "Paskaidro, kāpēc saucējs pārveidojot nemainās.",
    ]),
]
