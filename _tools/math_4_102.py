# -*- coding: utf-8 -*-
"""4. klase, 102. stunda: «Vairāk vai mazāk nekā puse?»

Puse kā etalons: ja skaitītājs divreiz mazāks par saucēju - tieši puse; ja
divkāršs skaitītājs mazāks par saucēju - mazāk nekā puse. Tā var salīdzināt
{3|8} un {4|7} bez kopsaucēja: viena ir mazāka par pusi, otra - lielāka.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis, taisne)

TEMA = "Vairāk vai mazāk nekā puse?"

MERKIS = ("Grupēsim daļas ar vienu saucēju, salīdzinot tās ar pusi.")

SATURS = [
    Sakums("Vai glāze ir pustukša vai puspilna?",
           zimejums=taisne(0, 1, 1, [(3 / 8.0, "3/8"), (0.5, "1/2"),
                                     (5 / 8.0, "5/8")], sikas=8),
           paraksts="{3|8} pa kreisi no puses, {5|8} - pa labi.",
           fakti=["Puse ir ērts salīdzināšanas punkts.",
                  "{4|8} ir tieši puse."]),

    Doma("Salīdzini divkāršoto skaitītāju ar saucēju",
         "Daļa ir tieši puse, ja skaitītājs · 2 = saucējs; mazāka par pusi, "
         "ja skaitītājs · 2 < saucējs; lielāka - ja lielāks.",
         soli=[
             "Divkāršo skaitītāju: {3|8} → 3 · 2 = 6.",
             "Salīdzini ar saucēju: 6 < 8.",
             "Tātad {3|8} < {1|2}.",
             "Ja divas daļas ir abās pusēs no {1|2}, tās uzreiz var "
             "salīdzināt.",
         ],
         pieze="{4|7}: 4 · 2 = 8 > 7, tātad vairāk nekā puse. Tāpēc "
               "{3|8} < {4|7}."),

    Paraugs("{5|12} vai {4|6}?",
            uzd="Salīdzini {5|12} un {4|6}, izmantojot pusi.",
            soli=[
                ("5 · 2 = 10 < 12", "{5|12} mazāk nekā puse."),
                ("4 · 2 = 8 > 6", "{4|6} vairāk nekā puse."),
                ("{5|12} < {4|6}", None),
            ],
            atbilde="{5|12} < {4|6}"),

    Zimejums("Daļas ar saucēju 10",
             restis([["mazāk par pusi", "tieši puse", "vairāk par pusi"],
                     ["1/10, 2/10", "5/10", "6/10, 7/10"],
                     ["3/10, 4/10", "", "8/10, 9/10"]],
                    "grupēšana"),
             paskaidro="Robeža ir 5 - puse no saucēja 10.",
             ievads="Visas desmitdaļas trīs grupās."),

    Varianti("Mazāk, tieši vai vairāk nekā puse?", [
        {"jaut": "{3|7}", "opcijas": ["mazāk", "tieši puse", "vairāk"],
         "pareizi": 0, "padoms": "6 < 7."},
        {"jaut": "{6|12}", "opcijas": ["tieši puse", "mazāk", "vairāk"],
         "pareizi": 0, "padoms": "12 = 6 · 2."},
        {"jaut": "{5|9}", "opcijas": ["vairāk", "mazāk", "tieši puse"],
         "pareizi": 0, "padoms": "10 > 9."},
        {"jaut": "{2|5}", "opcijas": ["mazāk", "vairāk", "tieši puse"],
         "pareizi": 0, "padoms": "4 < 5."},
        {"jaut": "Kura lielāka: {3|8} vai {4|7}?",
         "opcijas": ["{4|7}", "{3|8}", "vienādas"], "pareizi": 0,
         "padoms": "{4|7} vairāk nekā puse, {3|8} - mazāk."},
        {"jaut": "Kura lielāka: {7|12} vai {2|5}?",
         "opcijas": ["{7|12}", "{2|5}", "vienādas"], "pareizi": 0,
         "padoms": "14 > 12, 4 < 5."},
    ], pamats=4),

    Ievadi("Robeža", [
        {"jaut": "Kāds skaitītājs dod pusi ar saucēju 14?", "atb": ["7"],
         "padoms": "14 : 2."},
        {"jaut": "Cik daļu ar saucēju 8 ir mazākas par pusi (skaitītājs no "
                 "1)?", "atb": ["3"], "padoms": "1, 2, 3."},
        {"jaut": "Kāds saucējs, lai {9|?} būtu tieši puse?", "atb": ["18"],
         "padoms": "9 · 2."},
        {"jaut": "Mazākais skaitītājs, lai {?|11} būtu vairāk nekā puse?",
         "atb": ["6"], "padoms": "6 · 2 = 12 > 11."},
    ]),

    Pasaule("Vēlēšanu balsis",
            Ievadi("", [
                {"jaut": "Klasē 24 skolēni. Lai uzvarētu, vajag vairāk nekā "
                         "pusi balsu. Mazākais balsu skaits?",
                 "atb": ["13"], "padoms": "Puse ir 12."},
                {"jaut": "Anna saņēma 11 balsis no 24. Vai vairāk nekā puse? "
                         "Raksti «jā» vai «nē».",
                 "atb": ["nē", "ne"], "tastatura": "text",
                 "padoms": "11 < 12."},
                {"jaut": "Juris saņēma 13 no 24. Kāda daļa? Raksti daļu.",
                 "atb": ["13/24"], "vieta": "piem., 1/2",
                 "padoms": "13 no 24."},
                {"jaut": "Skolas padomē 30 cilvēki. Mazākais balsu skaits "
                         "vairākumam?",
                 "atb": ["16"], "padoms": "Puse ir 15."},
            ]),
            pavediens="skola",
            konteksts="Balsojumā «vairāk nekā puse» nozīmē uzvaru - tā ir "
                      "daļu salīdzināšana ar pusi.",
            kapec="Puse ir robeža, kas izšķir lēmumus."),

    Kopsavilkums([
        "Salīdzinu daļu ar pusi, divkāršojot skaitītāju.",
        "Grupēju daļas: mazāk, tieši, vairāk nekā puse.",
        "Salīdzinu dažādas daļas, izmantojot pusi.",
    ]),

    Majas([
        "Sagrupē: {2|9}, {5|10}, {7|12}, {3|6}, {4|9}, {5|8}.",
        "Pavēro, cik bija balsotāju un balsu kādā sacensībā vai šovā.",
        "Izdomā divas daļas ar dažādiem saucējiem, ko var salīdzināt ar "
        "pusi.",
    ]),
]
