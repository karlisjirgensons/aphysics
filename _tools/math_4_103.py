# -*- coding: utf-8 -*-
"""4. klase, 103. stunda: «Kā salīdzināt daļas ar dažādiem saucējiem?»

Vienkāršos gadījumos - kad viens saucējs ir otra reizinājums ({1|2} un
{3|8}) - daļas salīdzina ar divām skaitļu taisnēm vai joslām, kas
novietotas viena zem otras. Vispārīgs kopsaucējs ir 5. klases tēma.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, dala, taisne)

TEMA = "Kā salīdzināt daļas ar dažādiem saucējiem?"

MERKIS = ("Vienkāršos gadījumos salīdzināsim daļas ar dažādiem saucējiem, "
          "veidojot zīmējumu vai divas skaitļu taisnes.")

SATURS = [
    Sakums("Kas vairāk - {3|4} vai {5|8}?",
           zimejums=taisne(0, 1, 1, [(0.75, "3/4")], sikas=4)
           + taisne(0, 1, 1, [(5 / 8.0, "5/8")], sikas=8),
           paraksts="Divas taisnes viena zem otras - {3|4} ir tālāk.",
           fakti=["Taisnes vienādi garas - veselais tas pats.",
                  "Tad var redzēt, kura daļa ir tālāk pa labi."]),

    Doma("Pārvērt vienos gabalos",
         "Ja viens saucējs ir otra reizinājums, lielākos gabalus sadala "
         "mazākos: {3|4} = {6|8}, un tad salīdzina skaitītājus.",
         soli=[
             "Pārbaudi, vai viens saucējs dalās ar otru: 8 : 4 = 2.",
             "Katru ceturtdaļu sadali 2 astotdaļās.",
             "{3|4} = {6|8}.",
             "Salīdzini: {6|8} > {5|8}.",
         ],
         pieze="Tas pats, ko joslas zīmējumā redz ar aci."),

    Zimejums("Ceturtdaļas un astotdaļas",
             dala(4, 3, "3/4") + dala(8, 6, "6/8"),
             paskaidro="Iekrāsotās daļas vienāda garuma: {3|4} = {6|8}.",
             ievads="Sadalot katru ceturtdaļu uz pusēm."),

    Paraugs("{2|3} vai {5|6}?",
            uzd="Salīdzini {2|3} un {5|6}.",
            soli=[
                ("6 : 3 = 2", "Trešdaļu sadala 2 sestdaļās."),
                ("{2|3} = {4|6}", None),
                ("{4|6} < {5|6}", None),
            ],
            atbilde="{2|3} < {5|6}"),

    Varianti("Liec zīmi", [
        {"jaut": "{1|2} ☐ {3|8}", "opcijas": [">", "<", "="], "pareizi": 0,
         "padoms": "{1|2} = {4|8}."},
        {"jaut": "{3|5} ☐ {7|10}", "opcijas": ["<", ">", "="], "pareizi": 0,
         "padoms": "{3|5} = {6|10}."},
        {"jaut": "{1|3} ☐ {2|6}", "opcijas": ["=", "<", ">"], "pareizi": 0,
         "padoms": "{1|3} = {2|6}."},
        {"jaut": "{3|4} ☐ {9|12}", "opcijas": ["=", "<", ">"],
         "pareizi": 0, "padoms": "{3|4} = {9|12}."},
    ], pamats=4),

    Ievadi("Pārvērt", [
        {"jaut": "{1|2} = {?|8}", "atb": ["4"], "padoms": "1 · 4."},
        {"jaut": "{3|4} = {?|12}", "atb": ["9"], "padoms": "3 · 3."},
        {"jaut": "{2|5} = {?|10}", "atb": ["4"], "padoms": "2 · 2."},
        {"jaut": "{5|6} = {?|12}", "atb": ["10"], "padoms": "5 · 2."},
    ]),

    Pasaule("Kurš veikals izdevīgāks?",
            Varianti("", [
                {"jaut": "Veikalā A atlaide {1|4} cenas, B - {3|8}. Kur "
                         "lielāka atlaide?",
                 "opcijas": ["B", "A", "vienādi"], "pareizi": 0,
                 "padoms": "{1|4} = {2|8} < {3|8}."},
                {"jaut": "Sula: {2|3} l vai {5|6} l - kur vairāk?",
                 "opcijas": ["{5|6} l", "{2|3} l", "vienādi"], "pareizi": 0,
                 "padoms": "{2|3} = {4|6}."},
                {"jaut": "Siers: {1|2} kg vai {5|10} kg?",
                 "opcijas": ["vienādi", "{1|2} kg", "{5|10} kg"],
                 "pareizi": 0, "padoms": "{1|2} = {5|10}."},
            ]),
            pavediens="veikals",
            konteksts="Atlaides un iepakojumi bieži doti daļās ar dažādiem "
                      "saucējiem.",
            kapec="Pārvēršot vienos gabalos, izvēle kļūst skaidra."),

    Kopsavilkums([
        "Salīdzinu daļas ar divām taisnēm vai joslām.",
        "Pārvēršu daļu mazākos gabalos: {3|4} = {6|8}.",
        "Salīdzinu, kad viens saucējs dalās ar otru.",
    ]),

    Majas([
        "Uzzīmē divas joslas un salīdzini {2|5} un {3|10}.",
        "Pārvērt {1|2} desmitdaļās, divpadsmitdaļās un sestdaļās.",
        "Atrodi veikalā atlaides un salīdzini tās.",
    ]),
]
