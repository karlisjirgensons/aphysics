# -*- coding: utf-8 -*-
"""5. klase, 84. stunda: «Kā daļu pierakstīt kā dalījumu?»

80. stundā dalījums jau pavīdēja kā viens no pierakstiem; te tas kļūst par
stundas tematu. Svarīgais atklājums ir tas, ka dalīt drīkst arī tad, kad
dalāmais ir mazāks par dalītāju - atbilde vienkārši ir daļa. Tieši tas
5. klasē atver ceļu uz decimāldaļām nākamajā tematā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, dala, restis)

TEMA = "Kā daļu pierakstīt kā dalījumu?"

MERKIS = ("Iemācīsimies pierakstīt dalījumu kā daļu un daļu kā dalījumu.")

SATURS = [
    Sakums("Trīs pīrāgi, četri skolēni",
           zimejums=dala(4, 3, "3/4 katram"),
           paraksts="3 : 4 = {3|4} - katram tiek trīs ceturtdaļas pīrāga.",
           fakti=["Trīs pīrāgus var sadalīt arī četriem cilvēkiem.",
                  "Katram tiek mazāk nekā viens vesels.",
                  "Dalījuma atbilde ir daļa."]),

    Doma("Daļa un dalījums ir viens un tas pats",
         "Daļas svītra nozīmē dalīšanu: skaitītājs ir dalāmais, saucējs - "
         "dalītājs, tāpēc {a|b} un a : b ir viens un tas pats skaitlis.",
         soli=[
             "Skaitītāju raksti dalāmā vietā.",
             "Saucēju raksti dalītāja vietā.",
             "Ja dalāmais dalās, atbilde ir vesels skaitlis.",
             "Ja nedalās, atbilde paliek kā daļa.",
             "Saīsini daļu, ja tā ir saīsināma.",
         ],
         pieze="Tāpēc dalīt drīkst jebkurus divus naturālus skaitļus: "
               "3 : 4 nav «neiznāk», bet gan {3|4}. Vienīgais aizliegums "
               "paliek dalīšana ar nulli."),

    Paraugs("Sadali 3 pīrāgus starp 4 skolēniem",
            uzd="Cik pīrāga tiek katram skolēnam?",
            soli=[
                ("3 : 4",
                 "Dalāmais 3, dalītājs 4."),
                ("Katru pīrāgu sadala 4 daļās",
                 "Iznāk 12 ceturtdaļas."),
                ("12 : 4 = 3 ceturtdaļas katram",
                 "Katram pa trim gabaliem."),
                ("3 : 4 = {3|4}",
                 "Dalījums pierakstīts kā daļa."),
            ],
            atbilde="Katram tiek {3|4} pīrāga"),

    Ievadi("Pieraksti kā daļu vai skaitli", [
        {"jaut": "3 : 4 kā daļa. Atbildi raksti kā a/b.",
         "atb": ["3/4"], "padoms": "Dalāmais skaitītājā."},
        {"jaut": "5 : 8 kā daļa. Atbildi raksti kā a/b.",
         "atb": ["5/8"], "padoms": "Dalāmais skaitītājā."},
        {"jaut": "2 : 6 kā saīsināta daļa. Atbildi raksti kā a/b.",
         "atb": ["1/3", "2/6"], "padoms": "Abus dala ar 2."},
        {"jaut": "Cik ir 12 : 4?",
         "atb": ["3"], "padoms": "Dalās bez atlikuma."},
        {"jaut": "Cik ir 20 : 5?",
         "atb": ["4"], "padoms": "Dalās bez atlikuma."},
        {"jaut": "{7|9} kā dalījums. Ieraksti dalāmo.",
         "atb": ["7"], "padoms": "Skaitītājs ir dalāmais."},
        {"jaut": "{7|9} kā dalījums. Ieraksti dalītāju.",
         "atb": ["9"], "padoms": "Saucējs ir dalītājs."},
        {"jaut": "6 : 8 kā saīsināta daļa. Atbildi raksti kā a/b.",
         "atb": ["3/4", "6/8"], "padoms": "Abus dala ar 2."},
    ], pamats=4,
        ievads="Svītra un dalīšanas zīme nozīmē vienu un to pašu."),

    Zimejums("Dalījums un daļa blakus",
             restis([["3:4", "3/4"],
                     ["5:8", "5/8"]],
                    virsraksts="Divi pieraksti, viens skaitlis"),
             paskaidro="Kreisajā ailē ir dalījums, labajā - tā pati atbilde "
                       "kā daļa. Pārrakstīt var jebkurā virzienā.",
             ievads="Pāriet no viena pieraksta uz otru var bez rēķināšanas."),

    Varianti("Ko nozīmē daļas svītra?", [
        {"jaut": "Ko nozīmē svītra daļā {5|7}?",
         "opcijas": ["Dalīšanu", "Reizināšanu", "Atņemšanu", "Saskaitīšanu"],
         "pareizi": 0,
         "padoms": "Skaitītājs dalīts ar saucēju."},
        {"jaut": "Kurš skaitlis daļā ir dalāmais?",
         "opcijas": ["Skaitītājs", "Saucējs", "Abi", "Neviens"],
         "pareizi": 0,
         "padoms": "Tas, kas stāv augšā."},
        {"jaut": "Cik ir 3 : 4?",
         "opcijas": ["{3|4}", "{4|3}", "0", "12"],
         "pareizi": 0,
         "padoms": "Dalāmais skaitītājā."},
        {"jaut": "Vai 3 : 4 var izdalīt?",
         "opcijas": ["Var, atbilde ir daļa", "Nevar",
                     "Var tikai ar atlikumu", "Var tikai kalkulatorā"],
         "pareizi": 0,
         "padoms": "Daļa arī ir skaitlis."},
        {"jaut": "Ar ko dalīt nedrīkst?",
         "opcijas": ["Ar nulli", "Ar vieninieku", "Ar pirmskaitli",
                     "Ar lielāku skaitli"],
         "pareizi": 0,
         "padoms": "Saucējs nekad nav nulle."},
        {"jaut": "{12|4} kā skaitlis ir...",
         "opcijas": ["3", "{3|1}", "48", "{1|3}"],
         "pareizi": 0,
         "padoms": "12 : 4."},
    ], pamats=4),

    Pasaule("Kā sadalīt klasei?",
            Ievadi("", [
                {"jaut": "3 pīrāgi 4 skolēniem. Cik tiek katram? Atbildi "
                         "raksti kā a/b.",
                 "atb": ["3/4"], "padoms": "3 : 4."},
                {"jaut": "5 picas 8 skolēniem. Cik tiek katram? Atbildi "
                         "raksti kā a/b.",
                 "atb": ["5/8"], "padoms": "5 : 8."},
                {"jaut": "6 kūkas 8 skolēniem. Cik tiek katram? Atbildi "
                         "raksti kā a/b.",
                 "atb": ["3/4", "6/8"], "padoms": "6 : 8 = {3|4}."},
                {"jaut": "12 maizītes 4 skolēniem. Cik tiek katram?",
                 "atb": ["3"], "padoms": "12 : 4 = 3."},
            ]),
            pavediens="skola",
            konteksts="Klases svētkos cepumu skaits reti dalās ar skolēnu "
                      "skaitu.",
            kapec="Dalījums kā daļa ļauj sadalīt godīgi arī tad."),

    Kopsavilkums([
        "Pierakstu dalījumu kā daļu.",
        "Pierakstu daļu kā dalījumu.",
        "Zinu, ka daļas svītra nozīmē dalīšanu.",
        "Dalu arī tad, ja dalāmais ir mazāks par dalītāju.",
    ]),

    Majas([
        "Pieraksti kā daļas: 7 : 10, 9 : 12 un 4 : 5.",
        "Pieraksti kā dalījumus: {2|9}, {5|6} un {11|4}.",
        "Sadali 5 ābolus 4 cilvēkiem un pieraksti, cik tiek katram.",
    ]),
]
